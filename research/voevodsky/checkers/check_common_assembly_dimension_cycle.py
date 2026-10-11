"""H1: does dimension raising intrinsically stop or reset at a particle level?

Tests repeated coning, boundary/contractibility gates, exact flag completion
from source graphs, protected neutron faces, and retained packaging. Every rule
is particle-independent; any additional source declaration is recorded.
"""
from collections import Counter
from itertools import combinations, permutations
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

from check_common_assembly_symmetry import BASE, RESEARCH, load_targets, determinant, vertex
from check_common_assembly_cones import closure, invariants, cone
from check_common_assembly_gluing import orient
from check_common_assembly_refinement import boundary_chain


def signed_boundary(chain):
    result = Counter()
    for simplex, coefficient in chain.items():
        if len(simplex) <= 1:
            continue
        for i in range(len(simplex)):
            result[simplex[:i]+simplex[i+1:]] += coefficient*(-1)**i
    return {s: v for s, v in result.items() if v}


def elementary_collapse_to_vertex(complex_cells, apex):
    remaining = set(complex_cells)
    for s in sorted((s for s in complex_cells if apex not in s), key=lambda s: (-len(s), s)):
        joined = tuple(sorted((*s, apex)))
        assert {t for t in remaining if len(t) > len(s) and set(s) <= set(t)} == {joined}
        remaining.remove(s)
        remaining.remove(joined)
    assert remaining == {(apex,)}


def simplex_tower():
    maximal = {(0,)}
    rows = []
    for dimension in range(7):
        if dimension:
            maximal = cone(maximal, dimension)
        complex_cells = closure(maximal)
        assert complex_cells == closure([tuple(range(dimension+1))])
        boundary = signed_boundary({next(iter(maximal)): 1})
        assert not signed_boundary(boundary)
        stats = invariants(complex_cells)
        assert stats['rational_betti'] == [1]+[0]*dimension
        elementary_collapse_to_vertex(complex_cells, dimension)
        # Unit-edge regular simplices exist beyond four dimensions as well.
        G = [[Q(1) if i == j else Q(1, 2) for j in range(dimension)] for i in range(dimension)]
        assert determinant(G) == Q(dimension+1, 2**dimension) > 0
        # Packaging stores the whole prior complex. It is admissible at every
        # tested level; its external vertex does not erase the internal record.
        retained = {'dimension': dimension, 'simplices': [list(s) for s in sorted(complex_cells)]}
        payload = json.dumps(retained, sort_keys=True)
        package = {'object_id': hashlib.sha256(payload.encode()).hexdigest(), 'retained': retained}
        assert {tuple(s) for s in package['retained']['simplices']} == complex_cells
        rows.append({'dimension': dimension, 'vertices': dimension+1,
                     'f_vector': stats['f_vector'], 'boundary_facets': len(boundary),
                     'boundary_of_boundary_zero': True, 'filled_top_chain_closed': not boundary,
                     'elementary_collapse_to_dot': True, 'retained_packaging_possible': True,
                     'regular_simplex_gram_determinant': str(determinant(G)),
                     'package_record_digest': package['object_id']})
    assert rows[2]['boundary_facets'] == 3 and rows[4]['boundary_facets'] == 5
    assert rows[5]['dimension'] == 5 and rows[6]['dimension'] == 6
    return {'levels': rows,
            'finding': 'Coning increases dimension indefinitely. Boundary-of-boundary closure, collapsibility and retained packaging are available at every tested level. The 3 and 5 are boundary-facet counts of dimensions 2 and 4, not periods or stopping laws.'}


def clique_completion(vertices, edges, forbidden=()):
    """Fill a vertex subset iff all its edges exist and no forbidden face lies in it."""
    vertices = tuple(sorted(vertices))
    edges = {tuple(sorted(e)) for e in edges}
    forbidden = [set(s) for s in forbidden]
    admitted = set()
    stages = []
    for size in range(1, len(vertices)+1):
        added = set()
        for s in combinations(vertices, size):
            if any(f <= set(s) for f in forbidden):
                continue
            if not all(e in edges for e in combinations(s, 2)):
                continue
            if size > 1:
                assert all(tuple(f) in admitted for f in combinations(s, size-1))
            added.add(s)
        admitted |= added
        if added:
            stages.append({'dimension': size-1, 'cells': len(added)})
    return admitted, stages


def maximal_cells(complex_cells):
    return {s for s in complex_cells if not any(len(t) > len(s) and set(s) <= set(t) for t in complex_cells)}


def finite_source_completion(targets):
    source = json.loads((RESEARCH/'nima/inputs/proton-six-arrows.json').read_text())
    labels = list(source['vertices'])
    directed = {tuple(e) for e in source['arrows']}
    seed_edges = {tuple(sorted((labels.index(a), labels.index(b)))) for a, b in directed}
    raw, raw_stages = clique_completion(range(4), seed_edges)
    assert invariants(raw)['f_vector'] == [4, 5, 2]
    # The previously tested cycle-isometry declaration generates the missing
    # edge before dimension completion. Do not silently call this raw input.
    generators = []
    for a, b, c in permutations(labels, 3):
        if {(a, b), (b, c), (c, a)} <= directed:
            rename = {a: b, b: c, c: a}
            generators.append(tuple(labels.index(rename.get(k, k)) for k in labels))
    edges = set(seed_edges)
    while True:
        enlarged = edges | {tuple(sorted((p[a], p[b]))) for p in generators for a, b in edges}
        if enlarged == edges:
            break
        edges = enlarged
    enriched, enriched_stages = clique_completion(range(4), edges)
    assert invariants(enriched)['f_vector'] == [4, 6, 4, 1]
    # Electron supplied skeleton; there is not yet a minimal electron arrow seed.
    electron, electron_stages = clique_completion(range(5), set(combinations(range(5), 2)))
    assert invariants(electron)['f_vector'] == [5, 10, 10, 5, 1]
    nd, nc, marks = targets['neutron_belt']
    target_faces = {tuple(i for i in range(6) if any(v[i] for v in c)) for c in nc}
    target_complex = closure(target_faces)
    belt_edges = {s for s in target_complex if len(s) == 2}
    unprotected, unprotected_stages = clique_completion(range(6), belt_edges)
    protected, protected_stages = clique_completion(range(6), belt_edges, marks)
    assert invariants(unprotected)['f_vector'] == [6, 12, 8]
    assert invariants(unprotected)['rational_betti'] == [1, 0, 1]
    assert protected == target_complex
    assert invariants(protected)['rational_betti'] == [1, 1, 0]
    added_caps = maximal_cells(unprotected)-target_faces
    assert added_caps == {tuple(sorted(m)) for m in marks}
    # One subsequent cone reproduces the six-vs-eight constituent distinction.
    protected_cone = closure(cone(maximal_cells(protected), 6))
    unprotected_cone = closure(cone(maximal_cells(unprotected), 6))
    assert len(maximal_cells(protected_cone)) == 6
    assert len(maximal_cells(unprotected_cone)) == 8
    return {'proton_raw_seed': {'stages': raw_stages, 'topology': invariants(raw)},
            'proton_after_cycle_symmetry_closure': {'stages': enriched_stages, 'topology': invariants(enriched)},
            'electron_supplied_complete_skeleton': {'stages': electron_stages, 'topology': invariants(electron)},
            'neutron_unprotected': {'stages': unprotected_stages, 'topology': invariants(unprotected),
                                     'extra_cap_faces': [list(s) for s in sorted(added_caps)]},
            'neutron_protected': {'stages': protected_stages, 'topology': invariants(protected),
                                  'exact_coarse_belt_recovered': True},
            'neutron_cone_cell_counts': {'protected': 6, 'unprotected': 8},
            'finding': 'Fixed source vertices bound dimension without a dimensional clock. Raw proton arrows stop too early unless symmetry closure is admitted. Ordinary clique completion caps the neutron; prohibiting the two marked rim faces recovers its surface. Electron completion succeeds from its already supplied K5 skeleton.'}


def stopping_gate_test(targets):
    results = {}
    for name, (distances, cells, marks) in targets.items():
        oriented = orient(distances, cells)
        boundary = boundary_chain(oriented)
        # A boundary facet is protected when its barycentric support lies in
        # a declared attachment mark. Same predicate in every dimension.
        protected_facets = {facet for facet in boundary
                            if any(all(all(not weight or i in mark for i, weight in enumerate(v))
                                       for v in facet) for mark in marks)}
        relative_closed = set(boundary) <= protected_facets
        assert relative_closed
        # Coning all three target supports gives an explicit collapse to the apex.
        labels = sorted({v for c in cells for v in c})
        ids = {v: i for i, v in enumerate(labels)}
        base = {tuple(sorted(ids[v] for v in c)) for c in cells}
        coned = closure(cone(base, len(labels)))
        elementary_collapse_to_vertex(coned, len(labels))
        results[name] = {'absolute_boundary_closed': not boundary,
                         'relative_boundary_closed': relative_closed,
                         'cone_collapses_to_vertex': True,
                         'protected_boundary_facets': len(protected_facets),
                         'unmatched_boundary_facets': len(boundary)}
    return results


def main():
    targets, evidence = load_targets()
    report = {'hypothesis': 1, 'status': 'tested', 'dimension_tower': simplex_tower(),
              'source_supported_dimension_completion': finite_source_completion(targets),
              'stopping_gates': stopping_gate_test(targets), 'sources': evidence,
              'implementation_sha256': {name: hashlib.sha256((BASE/'checkers'/name).read_bytes()).hexdigest()
                  for name in ('check_common_assembly_dimension_cycle.py', 'check_common_assembly_symmetry.py',
                               'check_common_assembly_cones.py', 'check_common_assembly_gluing.py',
                               'check_common_assembly_refinement.py')},
              'conclusion': 'No intrinsic four-dimensional reset or particle-specific stopping gate follows from coning, boundary closure or packaging. Finite source incidence can bound dimension, but reconstructing the targets additionally requires the proton symmetry declaration, the supplied electron skeleton and protected neutron interfaces.',
              'scope': 'Exact finite tests through dimension six plus explicit generic cone and clique rules. No physical period, minimal electron/neutron arrow seed or shared coefficient compiler derived.'}
    (BASE/'results/common_assembly_dimension_cycle.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
