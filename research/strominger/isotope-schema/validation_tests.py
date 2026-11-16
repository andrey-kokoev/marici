"""Named rejection expectations and adversarial controls for the core validator."""
from rdflib import Graph, Literal, Namespace, RDF

ISO = Namespace("urn:marici:isotope:")
EX = Namespace("urn:marici:isotope-fixture:")
SH = Namespace("http://www.w3.org/ns/shacl#")


def expectation(component, shape, path=None, constraint=None, result_path=None):
    return {"component": SH[component + "ConstraintComponent"], "shape": ISO[shape],
            "property_path": path, "constraint": constraint,
            "result_path": path if result_path is None else result_path}


EXPECTED = {
    "missing source": expectation("MinCount", "ProvenanceShape", ISO.source),
    "missing color": expectation("MinCount", "ArrowShape", ISO.color),
    "unknown color": expectation("In", "ArrowShape", ISO.color),
    "two colors": expectation("MaxCount", "ArrowShape", ISO.color),
    "direction does not match support": expectation("SPARQL", "ArrowShape", constraint=ISO.ArrowSupportEndpointsConstraint),
    "missing endpoint type": expectation("Class", "EdgeShape", ISO.end0),
    "support outside structure": expectation("SPARQL", "StructureShape", constraint=ISO.ArrowSupportMembershipConstraint),
    "vertex outside structure": expectation("SPARQL", "StructureShape", constraint=ISO.EdgeVertexMembershipConstraint),
    "witness used as arrow": expectation("Class", "StructureShape", ISO.arrow),
    "dual arrow witness type": expectation("Not", "ArrowShape"),
    "dual constituent type": expectation("Xone", "ParticleShape"),
    "wrong constituent class": expectation("Class", "NucleusShape", ISO.proton),
    "unknown arrow predicate": expectation("Closed", "ArrowShape", result_path=ISO.colour),
    "missing nucleus": expectation("MinCount", "StructureShape", ISO.nucleus),
    "role outside structure": expectation("SPARQL", "StructureShape", constraint=ISO.InterpretationMembershipConstraint),
    "constituent outside structure": expectation("SPARQL", "StructureShape", constraint=ISO.InterpretationMembershipConstraint),
    "untyped source": expectation("Class", "ProvenanceShape", ISO.source),
    "missing provenance reference": expectation("MinCount", "SourceShape", ISO.reference),
}


def matches(report, shapes, focus, expected):
    if report is None:
        return False
    source_shapes = {expected["shape"]}
    if expected["property_path"] is not None:
        source_shapes = {node for node in shapes.objects(expected["shape"], SH.property)
                         if (node, SH.path, expected["property_path"]) in shapes}
    for result in report.subjects(SH.focusNode, focus):
        if report.value(result, SH.sourceConstraintComponent) != expected["component"]:
            continue
        if report.value(result, SH.sourceShape) not in source_shapes:
            continue
        if report.value(result, SH.resultPath) != expected["result_path"]:
            continue
        if expected["constraint"] is not None and report.value(result, SH.sourceConstraint) != expected["constraint"]:
            continue
        if "value" in expected and report.value(result, SH.value) != expected["value"]:
            continue
        return True
    return False


def additional_controls(check, derive_readouts, fixture, shapes, raw_shacl_evaluator):
    results = []

    # Keep unrelated rejection reasons at the SAME focus node while removing
    # exactly the disjointness rule under test. Focus-only matching would pass.
    data = fixture()
    data.add((EX.arrow, RDF.type, ISO.Witness))
    weakened = Graph()
    for triple in shapes:
        weakened.add(triple)
    weakened.remove((ISO.ArrowShape, SH["not"], None))
    # Production check() rejects altered authoritative shapes. Use the explicit
    # raw evaluator here only to test whether our expectation matcher notices
    # the missing disjointness constraint despite other SHACL failures.
    conforms, report, _ = raw_shacl_evaluator(data, weakened)
    closed_at_arrow = any((r, SH.sourceConstraintComponent, SH.ClosedConstraintComponent) in report
                          for r in report.subjects(SH.focusNode, EX.arrow))
    results.append({"name": "same-focus wrong-reason rejection does not satisfy disjointness test",
                    "pass": not conforms and closed_at_arrow and not matches(
                        report, weakened, EX.arrow, EXPECTED["dual arrow witness type"])})

    variants = [
        ("neutral inventory readout", [], [], {"Z": 1, "N": 1, "A": 2, "electrons": 1, "charge_e": 0}),
        ("unspecified electronic state is unknown, not zero",
         [(EX.structure, ISO.electronicState, EX.electrons)], [],
         {"Z": 1, "N": 1, "A": 2, "electrons": None, "charge_e": None}),
        ("explicit empty electronic state is fully ionized",
         [(EX.electrons, ISO.electron, EX.e)], [],
         {"Z": 1, "N": 1, "A": 2, "electrons": 0, "charge_e": 1}),
        ("extra electron gives negative charge", [],
         [(EX.e2, RDF.type, ISO.Electron), (EX.e2, ISO.source, EX.source), (EX.electrons, ISO.electron, EX.e2)],
         {"Z": 1, "N": 1, "A": 2, "electrons": 2, "charge_e": -1}),
        ("distinct constituent occurrences are counted", [],
         [(EX.p2, RDF.type, ISO.Proton), (EX.p2, ISO.source, EX.source), (EX.nucleus, ISO.proton, EX.p2),
          (EX.n2, RDF.type, ISO.Neutron), (EX.n2, ISO.source, EX.source), (EX.nucleus, ISO.neutron, EX.n2),
          (EX.n3, RDF.type, ISO.Neutron), (EX.n3, ISO.source, EX.source), (EX.nucleus, ISO.neutron, EX.n3)],
         {"Z": 2, "N": 3, "A": 5, "electrons": 1, "charge_e": 1}),
        ("duplicate triples do not invent constituent occurrences", [],
         [(EX.nucleus, ISO.proton, EX.p), (EX.electrons, ISO.electron, EX.e)],
         {"Z": 1, "N": 1, "A": 2, "electrons": 1, "charge_e": 0}),
    ]
    for name, removed, added, expected in variants:
        data = fixture()
        for triple in removed:
            assert triple in data
            data.remove(triple)
        for triple in added:
            data.add(triple)
        before = set(data)
        actual = derive_readouts(data, shapes)
        wanted = {str(EX.structure): expected}
        results.append({"name": name, "expected": wanted, "actual": actual,
                        "pass": actual == wanted and before == set(data)})

    data = fixture()
    data.remove((EX.p, RDF.type, ISO.Proton))
    try:
        derive_readouts(data, shapes)
    except ValueError:
        rejected = True
    else:
        rejected = False
    results.append({"name": "invalid inventory cannot produce readouts", "pass": rejected})
    return results
