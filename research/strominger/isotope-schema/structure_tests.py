"""Ordered composition, cell/witness payload and cross-structure controls."""
from rdflib import Graph, Literal, RDF
from validation_tests import EX, ISO, SH, expectation, matches


def run(check, shapes, base):
    results = []
    index = ISO["index"]

    def rule(shape, constraint, value=None):
        spec = expectation("SPARQL", shape, constraint=ISO[constraint])
        if value is not None:
            spec["value"] = value
        return spec

    def case(name, removed=(), added=(), requirement=None, focus=EX.structure, reverse_triples=False):
        data = Graph().parse(base / "fixtures" / "two-cells.ttl", format="turtle")
        for triple in removed:
            assert triple in data, (name, triple)
            data.remove(triple)
        for triple in added:
            data.add(triple)
        if reverse_triples:
            rebuilt = Graph()
            for triple in reversed(sorted(data, key=lambda t: tuple(map(str, t)))):
                rebuilt.add(triple)
            data = rebuilt
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

    case("two cells sharing an oppositely oriented support with parallel paths")
    case("triple insertion order cannot change the declared sequence", reverse_triples=True)
    case("negative sequence index", [(EX.l0, index, Literal(0))], [(EX.l0, index, Literal(-1))],
         expectation("MinInclusive", "PathStepShape", index), EX.l0)
    case("noninteger sequence index", [(EX.l0, index, Literal(0))], [(EX.l0, index, Literal("zero"))],
         expectation("Datatype", "PathStepShape", index), EX.l0)
    case("duplicate path indices", [(EX.l1, index, Literal(1))], [(EX.l1, index, Literal(0))],
         rule("SequenceShape", "UniqueStepIndexConstraint"), EX.long)
    case("gapped path indices", [(EX.l1, index, Literal(1))], [(EX.l1, index, Literal(2))],
         rule("SequenceShape", "ConsecutiveStepIndexConstraint"), EX.long)
    case("disconnected consecutive arrows", [(EX.l1, ISO.arrow, EX.aBC)], [(EX.l1, ISO.arrow, EX.aAC)],
         rule("PathShape", "PathCompositionConstraint"), EX.long)
    case("wrong path start", [(EX.long, ISO["from"], EX.A)], [(EX.long, ISO["from"], EX.B)],
         rule("PathShape", "PathEndpointsConstraint"), EX.long)
    case("wrong path end", [(EX.long, ISO.to, EX.C)], [(EX.long, ISO.to, EX.D)],
         rule("PathShape", "PathEndpointsConstraint"), EX.long)
    case("empty path cannot connect different vertices", [(EX.identity, ISO.to, EX.A)], [(EX.identity, ISO.to, EX.B)],
         rule("PathShape", "EmptyPathConstraint"), EX.identity)
    case("step belongs to a different path", [(EX.l0, ISO.inPath, EX.long)], [(EX.l0, ISO.inPath, EX.short)],
         rule("PathShape", "PathOwnerConstraint"), EX.long)
    case("step cannot declare two path owners", added=[(EX.l0, ISO.inPath, EX.short)],
         requirement=expectation("MaxCount", "PathStepShape", ISO.inPath), focus=EX.l0)
    case("orphan path occurrence rejected", [(EX.long, ISO.step, EX.l1)],
         requirement=rule("PathStepShape", "PathStepMembershipConstraint"), focus=EX.l1)
    case("witness cannot be traversed as a path arrow", [(EX.l0, ISO.arrow, EX.aAB)], [(EX.l0, ISO.arrow, EX.f1)],
         expectation("Class", "PathStepShape", ISO.arrow), EX.l0)
    case("path-step provenance required", [(EX.l0, ISO.source, EX.source)],
         requirement=expectation("MinCount", "ProvenanceShape", ISO.source), focus=EX.l0)

    case("duplicate boundary indices", [(EX.b11, index, Literal(1))], [(EX.b11, index, Literal(0))],
         rule("SequenceShape", "UniqueStepIndexConstraint"), EX.b1)
    case("gapped boundary indices", [(EX.b12, index, Literal(2))], [(EX.b12, index, Literal(3))],
         rule("SequenceShape", "ConsecutiveStepIndexConstraint"), EX.b1)
    case("broken interior boundary composition", [(EX.b11, ISO.reversed, Literal(False))], [(EX.b11, ISO.reversed, Literal(True))],
         rule("BoundaryShape", "BoundaryCompositionConstraint"), EX.b1)
    case("boundary does not close at its base", [(EX.b12, ISO.reversed, Literal(True))], [(EX.b12, ISO.reversed, Literal(False))],
         rule("BoundaryShape", "BoundaryClosureConstraint"), EX.b1)
    case("boundary reversal is explicitly boolean", [(EX.b12, ISO.reversed, Literal(True))], [(EX.b12, ISO.reversed, Literal(1))],
         expectation("Datatype", "BoundaryStepShape", ISO.reversed), EX.b12)
    case("boundary reversal cannot be omitted", [(EX.b12, ISO.reversed, Literal(True))],
         requirement=expectation("MinCount", "BoundaryStepShape", ISO.reversed), focus=EX.b12)
    case("boundary step belongs to a different boundary", [(EX.b10, ISO.inBoundary, EX.b1)], [(EX.b10, ISO.inBoundary, EX.b2)],
         rule("BoundaryShape", "BoundaryOwnerConstraint"), EX.b1)
    case("orphan boundary occurrence rejected", [(EX.b1, ISO.step, EX.b12)],
         requirement=rule("BoundaryStepShape", "BoundaryStepMembershipConstraint"), focus=EX.b12)
    case("boundary-step provenance required", [(EX.b10, ISO.source, EX.source)],
         requirement=expectation("MinCount", "ProvenanceShape", ISO.source), focus=EX.b10)
    case("cell must name its boundary", [(EX.c1, ISO.boundary, EX.b1)],
         requirement=expectation("MinCount", "CellShape", ISO.boundary), focus=EX.c1)
    case("cell must name its filling declaration", [(EX.c1, ISO.filling, EX.f1)],
         requirement=expectation("MinCount", "CellShape", ISO.filling), focus=EX.c1)
    case("cell and filling boundaries must agree", [(EX.c1, ISO.boundary, EX.b1)], [(EX.c1, ISO.boundary, EX.b2)],
         rule("CellShape", "CellFillingConstraint"), EX.c1)
    case("filling must name its actual cell", [(EX.f1, ISO.cell, EX.c1)], [(EX.f1, ISO.cell, EX.c2)],
         rule("WitnessShape", "FillingSubjectConstraint"), EX.f1)
    case("boundary declaration requires a boundary payload", [(EX.boundaryDeclaration, ISO.boundary, EX.b1)],
         requirement=rule("WitnessShape", "WitnessPayloadConstraint"), focus=EX.boundaryDeclaration)
    case("comparison declaration requires both paths", [(EX.comparison, ISO.right, EX.short)],
         requirement=rule("WitnessShape", "WitnessPayloadConstraint"), focus=EX.comparison)
    case("comparison declaration cannot carry unrelated boundary payload", added=[(EX.comparison, ISO.boundary, EX.b1)],
         requirement=rule("WitnessShape", "WitnessPayloadConstraint"), focus=EX.comparison)
    case("comparison endpoints must agree", [(EX.comparison, ISO.right, EX.short)], [(EX.comparison, ISO.right, EX.identity)],
         rule("WitnessShape", "ComparisonEndpointsConstraint"), EX.comparison)
    case("a declaration cannot self-promote to verified evidence", [(EX.comparison, ISO.status, ISO.Declared)],
         [(EX.comparison, ISO.status, EX.Verified)], expectation("HasValue", "WitnessShape", ISO.status), EX.comparison)
    case("description-only witness rejected", [
        (EX.boundaryDeclaration, ISO.witnessKind, ISO.BoundaryDeclaration),
        (EX.boundaryDeclaration, ISO.status, ISO.Declared), (EX.boundaryDeclaration, ISO.boundary, EX.b1)],
        [(EX.boundaryDeclaration, ISO.description, Literal("An asserted proof without typed subjects."))],
        expectation("MinCount", "WitnessShape", ISO.witnessKind), EX.boundaryDeclaration)

    for name, predicate, value in [
        ("nested path arrow outside structure", ISO.arrow, EX.aAB),
        ("nested boundary edge outside structure", ISO.edge, EX.BC),
        ("nested cell boundary outside structure", ISO.boundary, EX.b1),
        ("nested cell filling outside structure", ISO.witness, EX.f1),
        ("comparison path outside structure", ISO.path, EX.short),
        ("filling cell outside structure", ISO.cell, EX.c1),
    ]:
        case(name, [(EX.structure, predicate, value)],
             requirement=rule("StructuralMembershipShape", "StructuralMembershipConstraint", value))
    case("new cells cannot double as constituents", added=[(EX.c1, RDF.type, ISO.Proton)],
         requirement=expectation("Not", "ParticleShape"), focus=EX.c1)
    for role in [EX.long, EX.b1, EX.c2]:
        case(f"new structural role {role} participates in total binding coverage",
             [(EX.pbind, ISO.role, EX.c1)], [(EX.pbind, ISO.role, role)])
    case("inventory profile excludes new structural members",
         [(EX.structure, ISO.profile, ISO.PartialStructureProfile), (EX.structure, ISO.bindingScope, ISO.TotalBindings)],
         [(EX.structure, ISO.profile, ISO.InventoryProfile), (EX.structure, ISO.bindingScope, ISO.NoBindings)],
         rule("ProfileShape", "InventoryHasNoStructureConstraint"))

    loop = [(EX.structure, ISO.arrow, EX.aCA), (EX.aCA, RDF.type, ISO.Arrow), (EX.aCA, ISO.source, EX.source),
            (EX.aCA, ISO.support, EX.AC), (EX.aCA, ISO["from"], EX.C), (EX.aCA, ISO.to, EX.A),
            (EX.aCA, ISO.color, Literal("green")), (EX.structure, ISO.path, EX.loop),
            (EX.loop, RDF.type, ISO.Path), (EX.loop, ISO.source, EX.source),
            (EX.loop, ISO["from"], EX.A), (EX.loop, ISO.to, EX.A)]
    for i, arrow in enumerate([EX.aAC, EX.aCA, EX.aAC, EX.aCA]):
        step = EX[f"loop{i}"]
        loop.extend([(EX.loop, ISO.step, step), (step, RDF.type, ISO.PathStep), (step, ISO.source, EX.source),
                     (step, ISO.inPath, EX.loop), (step, index, Literal(i)), (step, ISO.arrow, arrow)])
    case("repeated arrow occurrences are retained in a composable loop", added=loop)

    loop_boundary = [(EX.structure, ISO.edge, EX.loopEdge), (EX.loopEdge, RDF.type, ISO.Edge),
                     (EX.loopEdge, ISO.source, EX.source), (EX.loopEdge, ISO.end0, EX.A), (EX.loopEdge, ISO.end1, EX.A),
                     (EX.structure, ISO.boundary, EX.loopBoundary), (EX.loopBoundary, RDF.type, ISO.Boundary),
                     (EX.loopBoundary, ISO.source, EX.source), (EX.loopBoundary, ISO.base, EX.A)]
    for i, reverse in enumerate([False, True]):
        step = EX[f"loopBoundary{i}"]
        loop_boundary.extend([(EX.loopBoundary, ISO.step, step), (step, RDF.type, ISO.BoundaryStep),
                              (step, ISO.source, EX.source), (step, ISO.inBoundary, EX.loopBoundary),
                              (step, index, Literal(i)), (step, ISO.edge, EX.loopEdge), (step, ISO.reversed, Literal(reverse))])
    case("loop supports retain explicit forward and reverse boundary occurrences", added=loop_boundary)
    return results
