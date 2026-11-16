"""Validate the proposed core profile without RDF/OWL inference.

uv run --python 3.12 --with pyshacl==0.30.1 --with rdflib==7.1.4 python research/strominger/isotope-schema/check.py --self-test
"""
import argparse
import hashlib
import importlib.metadata
import json
from pathlib import Path

from pyshacl import validate
from rdflib import BNode, Graph, Literal, Namespace, RDF, URIRef

from validation_tests import EXPECTED, additional_controls, matches
from profile_tests import run as profile_controls
from structure_tests import run as structure_controls
from organization_tests import run as organization_controls
from provenance import ROOT, REFERENCE, SourceError, import_reference, verify_sources
from provenance_tests import run as provenance_controls
from adversarial_tests import run as adversarial_controls
from scope_tests import run as scope_controls
from native_replay_tests import run as native_replay_controls
from shape_bundle import load_shapes, require_authoritative_shapes

BASE = Path(__file__).resolve().parent
ISO = Namespace("urn:marici:isotope:")
EX = Namespace("urn:marici:isotope-fixture:")
SH = Namespace("http://www.w3.org/ns/shacl#")


def load(path):
    return Graph().parse(path, format="turtle")


def has_owl_terms(graph):
    prefix = "http://www.w3.org/2002/07/owl#"
    return any((isinstance(term, URIRef) and str(term).startswith(prefix)) or
               (isinstance(term, Literal) and term.datatype is not None and str(term.datatype).startswith(prefix))
               for triple in graph for term in triple)


def _evaluate_shapes(data, shapes):
    """Raw SHACL evaluator for diagnostic tests, NOT overall conformance.

    This deliberately lacks the authority, entry-point and source checks that
    callers obtain through check(). Tests use it to study weakened constraints.
    """
    working_shapes = Graph()
    for triple in shapes:
        working_shapes.add(triple)
    return validate(data, shacl_graph=working_shapes, inference="none", advanced=False,
                    meta_shacl=True, abort_on_first=False, inplace=False, do_owl_imports=False)


def check(data, shapes, repository_root=ROOT):
    require_authoritative_shapes(shapes)
    # Application entry-point requirement: SHACL class targets alone would
    # otherwise accept an empty graph vacuously.
    if not any(data.subjects(RDF.type, ISO.IsotopeStructure)):
        return False, None, "Missing IsotopeStructure entry point."
    if has_owl_terms(data) or has_owl_terms(shapes):
        return False, None, "OWL terms are outside this profile."
    conforms, report, text = _evaluate_shapes(data, shapes)
    if not conforms:
        return conforms, report, text
    try:
        sources = verify_sources(data, repository_root)
    except SourceError as error:
        # Explicit application-stage report: this is NOT a failed SHACL Core
        # constraint, and must not be confused with a mathematical proof check.
        failure = Graph()
        document, result = BNode(), BNode()
        for triple in [
            (document, RDF.type, SH.ValidationReport), (document, SH.conforms, Literal(False)),
            (document, SH.result, result), (document, ISO.validationStage, Literal("source-verification")),
            (result, RDF.type, SH.ValidationResult), (result, SH.resultSeverity, SH.Violation),
            (result, SH.sourceConstraintComponent, ISO.SourceVerificationConstraintComponent),
            (result, ISO.sourceErrorCode, Literal(error.code)), (result, SH.resultMessage, Literal(str(error))),
        ]:
            failure.add(triple)
        if error.source is not None:
            failure.add((result, SH.focusNode, error.source))
        return False, failure, f"SHACL conforms; application source verification failed: {error}"
    return True, report, text + f"\nSource stage: {len(sources['resolved_attributions'])} attribution references resolved; {len(sources['replayed_outputs'])} supported output(s) replayed. Not physical certification.\n"


def derive_readouts(data, shapes):
    """Count declared constituent IRIs after validation, not physical evidence.

    charge_e is net charge in elementary-charge units. An omitted electronic
    state leaves both its electron count and charge unknown. A present state
    declares a complete inventory, including an explicitly empty inventory.
    """
    conforms, _, text = check(data, shapes)
    if not conforms:
        raise ValueError(f"Cannot derive readouts from invalid data:\n{text}")
    readouts = {}
    for structure in sorted(data.subjects(RDF.type, ISO.IsotopeStructure), key=str):
        nucleus = data.value(structure, ISO.nucleus, any=False)
        z = len(set(data.objects(nucleus, ISO.proton)))
        n = len(set(data.objects(nucleus, ISO.neutron)))
        state = data.value(structure, ISO.electronicState, any=False)
        electrons = None if state is None else len(set(data.objects(state, ISO.electron)))
        readouts[str(structure)] = {
            "Z": z, "N": n, "A": z + n, "electrons": electrons,
            "charge_e": None if electrons is None else z - electrons,
        }
    return readouts


def self_test(shapes):
    # Each fixture is independently reloaded; no mutation can leak to the next.
    tests = [
        ("valid fixture", [], [], True, None),
        ("reverse direction on undirected support",
         [(EX.arrow, ISO["from"], EX.v0), (EX.arrow, ISO.to, EX.v1)],
         [(EX.arrow, ISO["from"], EX.v1), (EX.arrow, ISO.to, EX.v0)], True, None),
        ("missing source", [(EX.arrow, ISO.source, EX.source)], [], False, EX.arrow),
        ("missing color", [(EX.arrow, ISO.color, Literal("red"))], [], False, EX.arrow),
        ("unknown color", [(EX.arrow, ISO.color, Literal("red"))],
         [(EX.arrow, ISO.color, Literal("purple"))], False, EX.arrow),
        ("two colors", [], [(EX.arrow, ISO.color, Literal("blue"))], False, EX.arrow),
        ("direction does not match support", [(EX.arrow, ISO.to, EX.v1)],
         [(EX.arrow, ISO.to, EX.v0)], False, EX.arrow),
        ("missing endpoint type", [(EX.v0, RDF.type, ISO.Vertex)], [], False, EX.edge),
        ("support outside structure", [(EX.structure, ISO.edge, EX.edge)], [], False, EX.structure),
        ("vertex outside structure", [(EX.structure, ISO.vertex, EX.v0)], [], False, EX.structure),
        ("witness used as arrow", [], [(EX.structure, ISO.arrow, EX.witness)], False, EX.structure),
        ("dual arrow witness type", [], [(EX.arrow, RDF.type, ISO.Witness)], False, EX.arrow),
        ("dual constituent type", [], [(EX.p, RDF.type, ISO.Neutron)], False, EX.p),
        ("wrong constituent class", [(EX.nucleus, ISO.proton, EX.p)],
         [(EX.nucleus, ISO.proton, EX.e)], False, EX.nucleus),
        ("unknown arrow predicate", [], [(EX.arrow, ISO.colour, Literal("red"))], False, EX.arrow),
        ("missing nucleus", [(EX.structure, ISO.nucleus, EX.nucleus)], [], False, EX.structure),
        ("role outside structure", [(EX.structure, ISO.witness, EX.witness)], [], False, EX.structure),
        ("constituent outside structure", [(EX.nucleus, ISO.neutron, EX.n)], [], False, EX.structure),
        ("untyped source", [(EX.source, RDF.type, ISO.Source)], [], False, EX.arrow),
        ("missing provenance reference", [(EX.source, ISO.reference, Literal("research/strominger/isotope-schema/fixtures/valid.ttl"))], [], False, EX.source),
    ]
    tests.append(("valid fixture after all rejection cases", [], [], True, None))
    results = []
    for name, removed, added, expected, focus in tests:
        data = load(BASE / "fixtures" / "valid.ttl")
        for triple in removed:
            assert triple in data, (name, "mutation precondition missing", triple)
            data.remove(triple)
        for triple in added:
            data.add(triple)
        original_data, original_shapes = set(data), set(shapes)
        conforms, report_graph, report_text = check(data, shapes)
        inputs_unchanged = set(data) == original_data and set(shapes) == original_shapes
        requirement = None if expected else EXPECTED[name]
        reason_ok = expected or matches(report_graph, shapes, focus, requirement)
        passed = bool(conforms) == expected and reason_ok and inputs_unchanged
        results.append({"name": name, "expected_conforms": expected, "conforms": bool(conforms),
                        "expected_focus": None if focus is None else str(focus),
                        "expected_constraint": None if requirement is None else {
                            k: None if v is None else str(v) for k, v in requirement.items()},
                        "expected_constraint_found": bool(reason_ok),
                        "inputs_unchanged": inputs_unchanged, "pass": passed})
        if not passed:
            print(report_text)
    conforms, _, _ = check(Graph(), shapes)
    results.append({"name": "empty graph rejected by entry-point guard", "pass": not conforms})
    results.extend(additional_controls(check, derive_readouts,
                                      lambda: load(BASE / "fixtures" / "valid.ttl"), shapes, _evaluate_shapes))
    results.extend(profile_controls(check, shapes, BASE, main))
    results.extend(structure_controls(check, shapes, BASE))
    results.extend(organization_controls(check, shapes, BASE))
    results.extend(provenance_controls(check, shapes, BASE, derive_readouts))
    results.extend(adversarial_controls(check, shapes, BASE, main))
    results.extend(scope_controls(check, shapes, BASE, derive_readouts))
    results.extend(native_replay_controls(check, shapes, BASE, derive_readouts, main))
    paths = [BASE / name for name in (
        "vocabulary.ttl", "shapes.ttl", "profiles.ttl", "fixtures/valid.ttl",
        "fixtures/inventory.ttl", "fixtures/all-bindings.ttl", "check.py",
        "validation_tests.py", "profile_tests.py", "structure-shapes.ttl",
        "structure_tests.py", "fixtures/two-cells.ttl", "STRUCTURE.md",
        "organization-shapes.ttl", "organization_tests.py", "fixtures/complete-organization.ttl",
        "provenance-shapes.ttl", "provenance.py", "provenance_tests.py", "PROVENANCE.md",
        "results/neon-20-inventory.ttl", "results/neon-20-source-replay.json", "adversarial_tests.py",
        "identity-shapes.ttl", "shape_bundle.py", "AUDIT-6.md", "scope_tests.py",
        "SOURCE-SCOPE.md", "results/native-source-inspection.json",
        "native_replay.mjs", "native_replay_tests.py", "results/native-constructor-replay.json",
        "native_projection.py", "reader-shapes.ttl", "NATIVE-REPLAY.md",
        "results/native-ne22-readers.ttl", "results/native-ne22-source-replay.json",
    )]
    receipt = {
        "scope": "Combinatorial constraints, readouts, local source resolution, reference inventory replay and fresh native Ne-22 finite-reader incidence replay/import. No complete spatial isotope diagram derivation, physical certification, arbitrary coherence proof, layout or general runtime routing engine.",
        "inference": "none", "owl_imports": False,
        "versions": {p: importlib.metadata.version(p) for p in ("pyshacl", "rdflib")},
        "sha256": {str(p.relative_to(BASE)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        "passed": sum(t["pass"] for t in results), "total": len(results), "tests": results,
    }
    (BASE / "test-results.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": receipt["passed"], "total": receipt["total"],
                      "failures": [t for t in results if not t["pass"]],
                      "report": str(BASE / "test-results.json")}, indent=2))
    return all(t["pass"] for t in results)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data", nargs="?", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--self-test", action="store_true")
    mode.add_argument("--readouts", action="store_true", help="Validate input and emit inventory-derived Z, N, A and charge_e as JSON")
    mode.add_argument("--source-report", action="store_true", help="Validate input and emit source-resolution/replay evidence")
    mode.add_argument("--import-reference", metavar="ISOTOPE", help="Emit a checked nuclear inventory from the repository reference, e.g. Neon-20")
    mode.add_argument("--import-native-reader", action="store_true", help="Emit checked Ne-22 reader incidence, not spatial geometry")
    args = parser.parse_args()
    # Parse vocabulary separately: it is documentation, not an inference graph.
    vocabulary = load(BASE / "vocabulary.ttl")
    if has_owl_terms(vocabulary):
        parser.error("OWL terms are outside this vocabulary")
    shapes = load_shapes()
    if args.data is not None and (args.self_test or args.import_reference or args.import_native_reader):
        parser.error("Self-test and reference import do not take an input Turtle file")
    if args.import_reference or args.import_native_reader:
        try:
            if args.import_native_reader:
                from native_projection import import_native
                data, _ = import_native()
            else:
                data, _ = import_reference(ROOT, REFERENCE, args.import_reference)
            conforms, _, text = check(data, shapes)
        except SourceError as error:
            print(str(error))
            raise SystemExit(1)
        if not conforms:
            print(text)
            raise SystemExit(1)
        print(data.serialize(format="turtle"))
        return
    if args.self_test:
        raise SystemExit(0 if self_test(shapes) else 1)
    if args.data is None:
        parser.error("Supply a Turtle data file or --self-test")
    data = load(args.data)
    if args.readouts:
        try:
            print(json.dumps(derive_readouts(data, shapes), indent=2))
        except ValueError as error:
            print(str(error))
            raise SystemExit(1)
        return
    conforms, _, text = check(data, shapes)
    if args.source_report and conforms:
        try:
            print(json.dumps(verify_sources(data), indent=2))
        except SourceError as error:
            print(str(error))
            raise SystemExit(1)
    else:
        print(text)
    raise SystemExit(0 if conforms else 1)


if __name__ == "__main__":
    main()
