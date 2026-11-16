"""Profile distinctions, total-binding coverage, and readout CLI integration."""
import contextlib
import io
import json
from unittest.mock import patch

from rdflib import Graph, RDF
from validation_tests import EX, ISO, SH, expectation, matches


def run(check, shapes, base, cli_main):
    results = []

    def case(name, filename, removed=(), added=(), requirement=None, focus=EX.structure):
        data = Graph().parse(base / "fixtures" / filename, format="turtle")
        for triple in removed:
            assert triple in data, (name, triple)
            data.remove(triple)
        for triple in added:
            data.add(triple)
        before, before_shapes = set(data), set(shapes)
        conforms, report, text = check(data, shapes)
        matched = requirement is None or matches(report, shapes, focus, requirement)
        ok = bool(conforms) == (requirement is None) and matched
        ok = ok and set(data) == before and set(shapes) == before_shapes
        result = {"name": name, "expected_conforms": requirement is None,
                  "conforms": bool(conforms), "expected_constraint_found": matched,
                  "expected_constraint": None if requirement is None else {
                      k: None if v is None else str(v) for k, v in requirement.items()},
                  "pass": ok}
        results.append(result)
        if not ok:
            print(text)

    def profile_rule(constraint):
        return expectation("SPARQL", "ProfileShape", constraint=ISO[constraint])

    def coverage(particle):
        expected = expectation("SPARQL", "BindingCoverageShape", constraint=ISO.ConstituentCoverageConstraint)
        expected["value"] = particle
        return expected

    case("explicit inventory without a diagram conforms only as inventory", "inventory.ttl")
    case("all constituents bound does not imply complete structure", "all-bindings.ttl")
    case("missing profile rejected", "valid.ttl",
         [(EX.structure, ISO.profile, ISO.PartialStructureProfile)],
         requirement=expectation("MinCount", "StructureShape", ISO.profile))
    case("ambiguous profiles rejected", "valid.ttl", added=[(EX.structure, ISO.profile, ISO.InventoryProfile)],
         requirement=expectation("MaxCount", "StructureShape", ISO.profile))
    case("unknown profile rejected", "valid.ttl",
         [(EX.structure, ISO.profile, ISO.PartialStructureProfile)], [(EX.structure, ISO.profile, EX.UnknownProfile)],
         expectation("In", "StructureShape", ISO.profile))
    case("missing binding scope rejected", "valid.ttl",
         [(EX.structure, ISO.bindingScope, ISO.PartialBindings)],
         requirement=expectation("MinCount", "StructureShape", ISO.bindingScope))
    case("inventory cannot contain geometry", "inventory.ttl", added=[
        (EX.structure, ISO.vertex, EX.v0), (EX.v0, RDF.type, ISO.Vertex), (EX.v0, ISO.source, EX.source)],
        requirement=profile_rule("InventoryHasNoStructureConstraint"))
    case("inventory cannot declare total bindings", "inventory.ttl",
         [(EX.structure, ISO.bindingScope, ISO.NoBindings)], [(EX.structure, ISO.bindingScope, ISO.TotalBindings)],
         profile_rule("ProfileBindingScopeConstraint"))
    case("partial structure cannot use inventory-only binding scope", "valid.ttl",
         [(EX.structure, ISO.bindingScope, ISO.PartialBindings)], [(EX.structure, ISO.bindingScope, ISO.NoBindings)],
         profile_rule("ProfileBindingScopeConstraint"))
    case("inventory cannot be relabeled complete", "inventory.ttl",
         [(EX.structure, ISO.profile, ISO.InventoryProfile), (EX.structure, ISO.bindingScope, ISO.NoBindings)],
         [(EX.structure, ISO.profile, ISO.CompleteStructureProfile), (EX.structure, ISO.bindingScope, ISO.TotalBindings)],
         expectation("SPARQL", "CompletenessShape", constraint=ISO.CompleteMembersConstraint))
    case("total bindings cannot be relabeled complete", "all-bindings.ttl",
         [(EX.structure, ISO.profile, ISO.PartialStructureProfile)],
         [(EX.structure, ISO.profile, ISO.CompleteStructureProfile)],
         expectation("SPARQL", "CompletenessShape", constraint=ISO.CompleteMembersConstraint))
    case("complete declaration requires total bindings", "valid.ttl",
         [(EX.structure, ISO.profile, ISO.PartialStructureProfile)],
         [(EX.structure, ISO.profile, ISO.CompleteStructureProfile)],
         profile_rule("ProfileBindingScopeConstraint"))
    case("old partially bound fixture cannot assert total bindings", "valid.ttl",
         [(EX.structure, ISO.bindingScope, ISO.PartialBindings)], [(EX.structure, ISO.bindingScope, ISO.TotalBindings)],
         coverage(EX.p))
    for particle, binding in [(EX.p, EX.pbind), (EX.n, EX.nbind), (EX.e, EX.ebind)]:
        case(f"missing {particle} binding names that constituent", "all-bindings.ttl",
             [(EX.structure, ISO.interpretation, binding)], requirement=coverage(particle))
    case("foreign role does not satisfy constituent coverage", "all-bindings.ttl", added=[],
         removed=[(EX.structure, ISO.witness, EX.witness)], requirement=coverage(EX.n))
    case("new constituent requires a new binding", "all-bindings.ttl", added=[
        (EX.nucleus, ISO.proton, EX.p2), (EX.p2, RDF.type, ISO.Proton), (EX.p2, ISO.source, EX.source)],
        requirement=coverage(EX.p2))
    case("role sharing is not forbidden by an invented bijection", "all-bindings.ttl",
         [(EX.ebind, ISO.role, EX.arrow)], [(EX.ebind, ISO.role, EX.v0)])
    case("one constituent may have several structural roles", "all-bindings.ttl",
         added=[(EX.pbind, ISO.role, EX.edge)])
    case("constituent identity is not structural identity", "all-bindings.ttl",
         added=[(EX.p, RDF.type, ISO.Vertex)],
         requirement=expectation("Not", "ParticleShape"), focus=EX.p)

    # Exercise the actual CLI parser and JSON-output branch without spawning a
    # process, changing the fixture, or bypassing the validation API.
    output = io.StringIO()
    with patch("sys.argv", ["check.py", str(base / "fixtures" / "inventory.ttl"), "--readouts"]):
        with contextlib.redirect_stdout(output):
            cli_main()
    actual = json.loads(output.getvalue())
    expected = {str(EX.structure): {"Z": 1, "N": 0, "A": 1, "electrons": None, "charge_e": None}}
    results.append({"name": "readout CLI validates inventory and emits JSON including zero neutrons",
                    "expected": expected, "actual": actual, "pass": actual == expected})
    return results
