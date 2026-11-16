"""Iteration-6 hostile audit; expectations fixed before validator repairs."""
import contextlib
import hashlib
import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from rdflib import Graph, Literal, RDF, RDFS, URIRef
from organization_tests import complete_fixture
from provenance import ROOT, REFERENCE, SourceError, import_reference, verify_sources
from validation_tests import EX, ISO, SH, expectation, matches


def clone(graph):
    copy = Graph()
    for triple in graph:
        copy.add(triple)
    return copy


def run(check, shapes, base, cli_main):
    tests = []
    targets = set(shapes.objects(ISO.RecordIdentityShape, SH.targetClass))
    other_targets = {o for s, _, o in shapes.triples((None, SH.targetClass, None)) if s != ISO.RecordIdentityShape}
    identity_property = next(p for p in shapes.objects(ISO.RecordIdentityShape, SH.property)
                             if shapes.value(p, SH.path) == RDF.type)
    values = shapes.value(identity_property, SH.qualifiedValueShape)
    explicit = set(shapes.items(shapes.value(values, SH["in"])))
    effective = {shapes.value(p, SH["class"]) for p in shapes.items(shapes.value(ISO.RecordIdentityShape, SH.xone))}
    tests.append({"name": "identity registry covers every concrete target with matching explicit and effective classes",
                  "pass": bool(targets) and targets == other_targets == explicit == effective})

    data = Graph().parse(base / "fixtures" / "inventory.ttl", format="turtle")
    data.remove((EX.source, RDF.type, ISO.Source))
    data.add((EX.source, RDF.type, EX.SourceAlias))
    data.add((EX.SourceAlias, RDFS.subClassOf, ISO.Source))
    data.set((EX.source, ISO.reference, Literal("research/strominger/isotope-schema/nonexistent-alias-source.json")))
    conforms, report, text = check(data, shapes)
    nominal = expectation("QualifiedMinCount", "RecordIdentityShape", RDF.type)
    tests.append({"name": "inherited Source type cannot evade explicit source enumeration",
                  "observed_conforms": bool(conforms), "pass": not conforms and matches(report, shapes, EX.source, nominal)})
    try:
        verify_sources(data)
    except SourceError as error:
        direct_rejected = error.code == "untyped-source-reference"
    else:
        direct_rejected = False
    tests.append({"name": "standalone source verifier rejects indirectly typed referenced sources", "pass": direct_rejected})

    data = Graph().parse(base / "fixtures" / "valid.ttl", format="turtle")
    data.add((EX.v0, RDF.type, ISO.ElectronicState))
    conforms, report, _ = check(data, shapes)
    tests.append({"name": "empty electronic state cannot masquerade as a vertex",
                  "observed_conforms": bool(conforms),
                  "pass": not conforms and matches(report, shapes, EX.v0, expectation("Xone", "RecordIdentityShape"))})

    data = Graph().parse(base / "fixtures" / "valid.ttl", format="turtle")
    data.add((EX.v0, RDF.type, EX.Annotation))
    conforms, _, _ = check(data, shapes)
    tests.append({"name": "an unrelated annotation type does not create a second record role", "pass": bool(conforms)})
    data.add((EX.Annotation, RDFS.subClassOf, ISO.ElectronicState))
    conforms, report, _ = check(data, shapes)
    tests.append({"name": "an inherited second record role is rejected even with one explicit record type",
                  "pass": not conforms and matches(report, shapes, EX.v0, expectation("Xone", "RecordIdentityShape"))})

    # Retain shape class/name but remove the two substantive coverage rules.
    weakened = clone(shapes)
    weakened.remove((ISO.CompletenessShape, SH.sparql, ISO.CompleteJunctionCoverageConstraint))
    weakened.remove((ISO.CompletenessShape, SH.sparql, ISO.CompletePortCoverageConstraint))
    data = complete_fixture(base)
    data.remove((EX.structure, ISO.junction, EX.jD))
    try:
        conforms, _, _ = check(data, weakened)
    except ValueError as error:
        protected = "shape bundle" in str(error)
        observed = "bundle-refused"
    else:
        protected, observed = False, bool(conforms)
    tests.append({"name": "shape names cannot substitute for authoritative constraint contents",
                  "observed": observed, "pass": protected})

    data = Graph().parse(base / "fixtures" / "valid.ttl", format="turtle")
    data.set((EX.witness, ISO.description, Literal("http://www.w3.org/2002/07/owl#Thing is cited as text, not asserted.")))
    conforms, _, _ = check(data, shapes)
    tests.append({"name": "ordinary text mentioning OWL is not an OWL axiom", "observed_conforms": bool(conforms), "pass": bool(conforms)})
    data.add((EX.v0, RDF.type, URIRef("http://www.w3.org/2002/07/owl#Thing")))
    conforms, _, text = check(data, shapes)
    tests.append({"name": "actual OWL vocabulary is still rejected", "pass": not conforms and "OWL terms" in text})

    data = Graph().parse(base / "fixtures" / "inventory.ttl", format="turtle")
    for triple in [
        (EX.RootAlias, RDFS.subClassOf, ISO.IsotopeStructure), (EX.hiddenRoot, RDF.type, EX.RootAlias),
        (EX.hiddenRoot, ISO.source, EX.source), (EX.hiddenRoot, ISO.profile, ISO.InventoryProfile),
        (EX.hiddenRoot, ISO.bindingScope, ISO.NoBindings), (EX.hiddenRoot, ISO.nucleus, EX.nucleus),
    ]:
        data.add(triple)
    conforms, report, _ = check(data, shapes)
    tests.append({"name": "an inherited extra root cannot disappear from explicit readouts",
                  "pass": not conforms and matches(report, shapes, EX.hiddenRoot, nominal)})

    # Semantically identical fresh blank-node labels are not a weakened schema.
    reparsed = Graph().parse(data=shapes.serialize(format="turtle"), format="turtle")
    conforms, _, _ = check(complete_fixture(base), reparsed)
    tests.append({"name": "shape graph isomorphism permits fresh blank-node labels", "pass": bool(conforms)})
    reparsed.remove((ISO.CompletenessShape, SH.sparql, ISO.CompleteJunctionCoverageConstraint))
    try:
        check(complete_fixture(base), reparsed)
    except ValueError as error:
        cache_safe = "shape bundle" in str(error)
    else:
        cache_safe = False
    tests.append({"name": "mutating an already accepted shape object invalidates its cached acceptance", "pass": cache_safe})

    data = Graph().parse(base / "fixtures" / "valid.ttl", format="turtle")
    data.set((EX.witness, ISO.description, Literal("1", datatype=URIRef("http://www.w3.org/2002/07/owl#real"))))
    conforms, _, text = check(data, shapes)
    tests.append({"name": "OWL datatype IRIs are not mistaken for ordinary quoted text", "pass": not conforms and "OWL terms" in text})

    def invoke(arguments):
        output, error = io.StringIO(), io.StringIO()
        with patch("sys.argv", ["check.py", *map(str, arguments)]):
            with contextlib.redirect_stdout(output), contextlib.redirect_stderr(error):
                try:
                    cli_main()
                except SystemExit as exit_:
                    code = exit_.code
                else:
                    code = 0
        return code, output.getvalue(), error.getvalue()

    code, text, _ = invoke(["--import-reference", "Calcium-46"])
    imported = Graph().parse(data=text, format="turtle") if code == 0 else Graph()
    expected, _ = import_reference(ROOT, REFERENCE, "Calcium-46")
    tests.append({"name": "import CLI emits exactly the checked reference graph", "pass": code == 0 and set(imported) == set(expected)})
    code, text, _ = invoke(["--import-reference", "Unknown-99"])
    tests.append({"name": "import CLI missing selector exits nonzero", "pass": code == 1 and "record-selection" in text})
    code, text, _ = invoke([base / "results" / "neon-20-inventory.ttl", "--source-report"])
    receipt = json.loads(text) if code == 0 else {}
    tests.append({"name": "source-report CLI identifies the replayed output and operation",
                  "pass": code == 0 and len(receipt.get("replayed_outputs", [])) == 1
                  and receipt["replayed_outputs"][0]["key"] == "Neon-20"})
    code, text, _ = invoke([base / "fixtures" / "inventory.ttl", "--source-report"])
    receipt = json.loads(text) if code == 0 else {}
    tests.append({"name": "source-report CLI does not promote fixture attribution to replay",
                  "pass": code == 0 and receipt.get("replayed_outputs") == [] and len(receipt.get("resolved_attributions", [])) == 1})
    code, _, _ = invoke(["--source-report", "--readouts", base / "fixtures" / "inventory.ttl"])
    tests.append({"name": "conflicting CLI result modes are rejected", "pass": code == 2})

    with TemporaryDirectory(prefix="marici-isotope-cli-audit-") as temporary:
        altered = clone(expected)
        output = next(altered.subjects(RDF.type, ISO.IsotopeStructure))
        nucleus = altered.value(output, ISO.nucleus)
        neutron = next(altered.objects(nucleus, ISO.neutron))
        altered.remove((nucleus, ISO.neutron, neutron))
        path = Path(temporary) / "altered.ttl"
        altered.serialize(destination=path, format="turtle")
        code, text, _ = invoke([path, "--source-report"])
        tests.append({"name": "source-report CLI fails rather than certifying tampered output",
                      "pass": code == 1 and "replay-mismatch" in text})

    # This file is written only on the first failing audit. Later green runs
    # retain the original failures and source digests as historical evidence.
    checkpoint = base / "results" / "audit-iteration6-before.json"
    if any(not t["pass"] for t in tests) and not checkpoint.exists():
        checkpoint.parent.mkdir(exist_ok=True)
        paths = [base / "check.py", base / "provenance.py", base / "adversarial_tests.py", *sorted(base.glob("*.ttl"))]
        checkpoint.write_text(json.dumps({"scope": "Pre-repair hostile audit, not current validation status",
            "tests": tests, "sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}, indent=2) + "\n", encoding="utf-8")
    return tests
