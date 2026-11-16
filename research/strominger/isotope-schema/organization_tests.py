"""Complete combinatorial records, shell assignments and edge-end frames."""
from rdflib import Graph, Literal, RDF
from validation_tests import EX, ISO, expectation, matches


def complete_fixture(base):
    data = Graph().parse(base / "fixtures" / "two-cells.ttl", format="turtle")
    old = (EX.structure, ISO.profile, ISO.PartialStructureProfile)
    assert old in data
    data.remove(old)
    return data.parse(base / "fixtures" / "complete-organization.ttl", format="turtle")


def run(check, shapes, base):
    results = []
    index = ISO["index"]

    def rule(shape, constraint, value=None):
        expected = expectation("SPARQL", shape, constraint=ISO[constraint])
        if value is not None:
            expected["value"] = value
        return expected

    def case(name, removed=(), added=(), requirement=None, focus=EX.structure):
        data = complete_fixture(base)
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
        results.append({"name": name, "expected_conforms": requirement is None, "conforms": bool(conforms),
                        "expected_focus": str(focus), "expected_constraint_found": matched,
                        "expected_constraint": None if requirement is None else {
                            k: None if v is None else str(v) for k, v in requirement.items()}, "pass": ok})
        if not ok:
            print(text)

    case("complete two-cell combinatorial record conforms")
    for predicate in [ISO.vertex, ISO.edge, ISO.arrow, ISO.cell, ISO.shell, ISO.junction]:
        data = complete_fixture(base)
        case(f"complete record cannot omit {predicate} inventory",
             list(data.triples((EX.structure, predicate, None))),
             requirement=rule("CompletenessShape", "CompleteMembersConstraint"))
    case("complete record cannot omit a cell's shell", [(EX.shell2, ISO.cell, EX.c2)],
         requirement=rule("CompletenessShape", "CompleteShellCoverageConstraint", EX.c2))
    case("complete record cannot omit an electron's shell", [(EX.shell1, ISO.electron, EX.e)],
         requirement=rule("CompletenessShape", "CompleteShellCoverageConstraint", EX.e))
    case("complete record cannot omit a vertex frame", [(EX.structure, ISO.junction, EX.jD)],
         requirement=rule("CompletenessShape", "CompleteJunctionCoverageConstraint", EX.D))
    case("complete record cannot omit one edge-end port", [(EX.jA, ISO.port, EX.pAB0)],
         requirement=rule("CompletenessShape", "CompletePortCoverageConstraint", EX.AB))
    case("complete record still requires every constituent binding", [(EX.structure, ISO.interpretation, EX.pbind)],
         requirement=rule("BindingCoverageShape", "ConstituentCoverageConstraint", EX.p))
    case("complete record cannot weaken total binding scope", [(EX.structure, ISO.bindingScope, ISO.TotalBindings)],
         [(EX.structure, ISO.bindingScope, ISO.PartialBindings)],
         rule("ProfileShape", "ProfileBindingScopeConstraint"))
    case("shell levels must be positive", [(EX.shell1, ISO.level, Literal(1))], [(EX.shell1, ISO.level, Literal(0))],
         expectation("MinInclusive", "ShellShape", ISO.level), EX.shell1)
    case("shell levels cannot be duplicated", [(EX.shell2, ISO.level, Literal(2))], [(EX.shell2, ISO.level, Literal(1))],
         rule("OrganizationShape", "ShellLevelConstraint"))
    case("cell cannot belong to two shells", added=[(EX.shell2, ISO.cell, EX.c1)],
         requirement=rule("OrganizationShape", "ShellAssignmentConstraint", EX.c1))
    case("electron cannot belong to two shells", added=[(EX.shell2, ISO.electron, EX.e)],
         requirement=rule("OrganizationShape", "ShellAssignmentConstraint", EX.e))
    case("shell cell must belong to structure", [(EX.structure, ISO.cell, EX.c2)],
         requirement=rule("OrganizationShape", "OrganizationMembershipConstraint", EX.c2))
    case("shell electron must belong to electronic state", [(EX.electrons, ISO.electron, EX.e)],
         requirement=rule("OrganizationShape", "OrganizationMembershipConstraint", EX.e))
    case("junction vertex must belong to structure", [(EX.structure, ISO.vertex, EX.D)],
         requirement=rule("OrganizationShape", "OrganizationMembershipConstraint", EX.D))
    case("port edge must belong to structure", [(EX.structure, ISO.edge, EX.AB)],
         requirement=rule("OrganizationShape", "OrganizationMembershipConstraint", EX.AB))
    case("junction cannot be duplicated for a vertex", added=[
        (EX.structure, ISO.junction, EX.jDuplicate), (EX.jDuplicate, RDF.type, ISO.Junction),
        (EX.jDuplicate, ISO.source, EX.organizationSource), (EX.jDuplicate, ISO.vertex, EX.A)],
        requirement=rule("OrganizationShape", "JunctionUniquenessConstraint", EX.A))
    case("port order cannot duplicate an index", [(EX.pAC0, index, Literal(1))], [(EX.pAC0, index, Literal(0))],
         rule("JunctionShape", "PortOrderConstraint"), EX.jA)
    case("port order cannot skip an index", [(EX.pAD0, index, Literal(2))], [(EX.pAD0, index, Literal(3))],
         rule("JunctionShape", "PortOrderConstraint"), EX.jA)
    case("port indices cannot be negative", [(EX.pAB0, index, Literal(0))], [(EX.pAB0, index, Literal(-1))],
         expectation("MinInclusive", "PortShape", index), EX.pAB0)
    case("edge end selector must be zero or one", [(EX.pAB0, ISO.endIndex, Literal(0))], [(EX.pAB0, ISO.endIndex, Literal(2))],
         expectation("In", "PortShape", ISO.endIndex), EX.pAB0)
    case("edge end must actually meet the junction", [(EX.pAB0, ISO.endIndex, Literal(0))], [(EX.pAB0, ISO.endIndex, Literal(1))],
         rule("PortShape", "PortEndpointConstraint"), EX.pAB0)
    case("port owner must agree with junction membership", [(EX.pAB0, ISO.junction, EX.jA)], [(EX.pAB0, ISO.junction, EX.jB)],
         rule("JunctionShape", "PortOwnerConstraint"), EX.jA)
    case("port owner must list the occurrence", [(EX.jA, ISO.port, EX.pAB0)],
         requirement=rule("PortShape", "PortMembershipConstraint"), focus=EX.pAB0)
    duplicate_port = [(EX.jA, ISO.port, EX.duplicatePort), (EX.duplicatePort, RDF.type, ISO.Port),
                      (EX.duplicatePort, ISO.source, EX.organizationSource), (EX.duplicatePort, ISO.junction, EX.jA),
                      (EX.duplicatePort, ISO.edge, EX.AB), (EX.duplicatePort, ISO.endIndex, Literal(0)),
                      (EX.duplicatePort, index, Literal(3))]
    case("unique cyclic position cannot hide a duplicate edge-end occurrence", added=duplicate_port,
         requirement=rule("JunctionShape", "PortOccurrenceUniquenessConstraint"), focus=EX.jA)
    case("opposite ports must be reciprocal", [(EX.pBC0, ISO.opposite, EX.pAB1)],
         requirement=rule("PortShape", "OppositePortsConstraint"), focus=EX.pAB1)
    case("a port cannot be opposite itself", added=[(EX.pAB0, ISO.opposite, EX.pAB0)],
         requirement=rule("PortShape", "OppositePortsConstraint"), focus=EX.pAB0)
    case("opposite ports cannot cross junctions", added=[(EX.pAB0, ISO.opposite, EX.pAC1), (EX.pAC1, ISO.opposite, EX.pAB0)],
         requirement=rule("PortShape", "OppositePortsConstraint"), focus=EX.pAB0)
    case("multiple straight continuations are not silently chosen", added=[(EX.pAB1, ISO.opposite, EX.pAC0)],
         requirement=expectation("MaxCount", "PortShape", ISO.opposite), focus=EX.pAB1)
    case("omitting an entire opposite pair is permitted", [(EX.pAB1, ISO.opposite, EX.pBC0), (EX.pBC0, ISO.opposite, EX.pAB1)])
    for node in [EX.shell1, EX.jA, EX.pAB0]:
        case(f"organization provenance required for {node}", [(node, ISO.source, EX.organizationSource)],
             requirement=expectation("MinCount", "ProvenanceShape", ISO.source), focus=node)
    for role in [EX.shell1, EX.jA]:
        case(f"organization role {role} participates in constituent coverage",
             [(EX.pbind, ISO.role, EX.c1)], [(EX.pbind, ISO.role, role)])
    case("a shell cannot double as a constituent", added=[(EX.shell1, RDF.type, ISO.Proton)],
         requirement=expectation("Not", "ParticleShape"), focus=EX.shell1)

    loop = [(EX.structure, ISO.edge, EX.loopEdge), (EX.loopEdge, RDF.type, ISO.Edge),
            (EX.loopEdge, ISO.source, EX.organizationSource), (EX.loopEdge, ISO.end0, EX.A), (EX.loopEdge, ISO.end1, EX.A)]
    for i in range(2):
        p = EX[f"loopPort{i}"]
        loop.extend([(EX.jA, ISO.port, p), (p, RDF.type, ISO.Port), (p, ISO.source, EX.organizationSource),
                     (p, ISO.junction, EX.jA), (p, ISO.edge, EX.loopEdge), (p, ISO.endIndex, Literal(i)),
                     (p, index, Literal(i + 3))])
    case("complete frame retains both endpoint occurrences of a loop", added=loop)
    case("one loop port cannot stand for both ends", added=[t for t in loop if EX.loopPort1 not in t],
         requirement=rule("CompletenessShape", "CompletePortCoverageConstraint", EX.loopEdge))
    incomplete = Graph()
    for triple in shapes:
        if triple[0] != ISO.CompletenessShape:
            incomplete.add(triple)
    try:
        check(complete_fixture(base), incomplete)
    except ValueError as error:
        rejected = "Incomplete shape bundle" in str(error)
    else:
        rejected = False
    results.append({"name": "API refuses a shape bundle missing completeness rules", "pass": rejected})
    return results
