"""Hostile test: does moving-centroid admission commute with subdivision?

Uses the source-generated full hull, with explicit interface exclusions disabled.
Each simplicial facet is subdivided at its centroid, without changing geometry.
Compare selecting before subdivision with selecting each child afterward.
"""
from copy import deepcopy
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib
import json

from assemble_relative_geometry import assemble, apply, subtract, dot_metric, determinant
from check_common_assembly_symmetry import BASE


def mean(points):
    return tuple(sum(p[i] for p in points)/len(points) for i in range(len(points[0])))


def intrinsic_gram_determinant(points, G):
    edges = [subtract(p, points[0]) for p in points[1:]]
    return determinant([[dot_metric(a, b, G) for b in edges] for a in edges])


def mode_score(point, generators, G):
    differences = [subtract(apply(g, point), point) for g in generators]
    return sum(dot_metric(v, v, G) for v in differences)


def check_source(source):
    source = deepcopy(source)
    for seed in source['seeds']:
        if seed['role'] == 'external_interface':
            seed['role'] = 'carrier'
    geometry = assemble(source)
    points = [tuple(map(Q, p)) for p in geometry['vertices']]
    G = [[Q(x) for x in row] for row in source['metric']]
    generators = [(tuple(tuple(Q(x) for x in row) for row in g['matrix']), tuple(map(Q, g['translation'])))
                  for g in source['generators']]
    parent_reports, refined_records = [], []
    original_selected = refined_after_selection = selected_after_refinement = 0
    for facet in geometry['carrier_facets']:
        corners = [points[i] for i in facet]
        centroid = mean(corners)
        score = mode_score(centroid, generators, G)
        children = [[centroid]+[v for i, v in enumerate(corners) if i != omitted] for omitted in range(len(corners))]
        child_centroids = [mean(child) for child in children]
        child_scores = [mode_score(v, generators, G) for v in child_centroids]
        parent_gram = intrinsic_gram_determinant(corners, G)
        assert parent_gram > 0
        assert all(intrinsic_gram_determinant(child, G) == parent_gram/(len(corners)**2) for child in children)
        assert mean(child_centroids) == centroid
        # One declared centroid subdivision, equal child volumes, same support.
        original_selected += score > 0
        refined_after_selection += len(children)*(score > 0)
        selected_after_refinement += sum(v > 0 for v in child_scores)
        parent_reports.append({'facet': facet, 'parent_score': str(score),
                               'child_scores': list(map(str, child_scores)),
                               'equal_volume_support_preserving_subdivision': True,
                               'admission_commutes_on_this_facet': all((v > 0) == (score > 0) for v in child_scores),
                               'parent_centroid': list(map(str, centroid)),
                               'child_centroids': [list(map(str, v)) for v in child_centroids]})
        refined_records.extend((facet, child, c, s) for child, c, s in zip(children, child_centroids, child_scores))
    # Control for a narrower rule: rediscover maximal supporting-plane groups
    # from child geometry, not from their stored parent labels.
    groups = {}
    all_refined_points = sorted({p for _, child, _, _ in refined_records for p in child})
    d = len(G)
    for index, (_, child, _, _) in enumerate(refined_records):
        base = child[0]
        rows = [subtract(p, base) for p in child[1:]]
        signs = [determinant(rows+[subtract(p, base)]) for p in all_refined_points]
        assert any(signs)
        assert all(s >= 0 for s in signs) or all(s <= 0 for s in signs)
        key = tuple(i for i, s in enumerate(signs) if s == 0)
        groups.setdefault(key, []).append(index)
    assert len(groups) == len(geometry['carrier_facets'])
    group_selected_children = 0
    for indices in groups.values():
        assert len(indices) == d
        # Equal-area/volume children were certified above. Their weighted
        # centroid can therefore be recovered as their arithmetic mean.
        aggregate = mean([refined_records[i][2] for i in indices])
        selected = mode_score(aggregate, generators, G) > 0
        group_selected_children += len(indices)*selected
        # Parent labels are consulted only to verify the recovered grouping.
        assert len({tuple(sorted(refined_records[i][0])) for i in indices}) == 1
    assert group_selected_children == refined_after_selection
    return {'generated_hull_facets': len(parent_reports), 'original_active_facets': original_selected,
            'select_then_subdivide_cells': refined_after_selection,
            'subdivide_then_select_cells': selected_after_refinement,
            'admission_commutes_with_subdivision': all(r['admission_commutes_on_this_facet'] for r in parent_reports),
            'facet_reports': parent_reports,
            'geometrically_regrouped_supporting_facets': len(groups),
            'regroup_then_select_children': group_selected_children,
            'regrouping_uses_geometry_not_parent_labels': True}


def main():
    sources = [('proton', 'relative-proton.json'), ('neutron', 'mode-neutron.json'), ('electron', 'relative-electron.json')]
    results, hashes = {}, {}
    for name, filename in sources:
        path = BASE/'inputs'/filename
        raw = path.read_bytes()
        hashes[filename] = hashlib.sha256(raw).hexdigest()
        results[name] = check_source(json.loads(raw))
    assert results['proton']['select_then_subdivide_cells'] == results['proton']['subdivide_then_select_cells'] == 12
    assert results['electron']['select_then_subdivide_cells'] == results['electron']['subdivide_then_select_cells'] == 20
    neutron = results['neutron']
    assert neutron['select_then_subdivide_cells'] == 18
    assert neutron['subdivide_then_select_cells'] == 24
    assert not neutron['admission_commutes_with_subdivision']
    failures = [r for r in neutron['facet_reports'] if not r['admission_commutes_on_this_facet']]
    assert len(failures) == 2
    assert all(r['parent_score'] == '0' and r['child_scores'] == ['1/3']*3 for r in failures)
    report = {'status': 'counterexample_verified', 'hypothesis': 'cell admission iff its centroid has a nontrivial source mode',
              'results': results, 'sources': hashes,
              'implementation_sha256': {name: hashlib.sha256((BASE/'checkers'/name).read_bytes()).hexdigest()
                  for name in ('check_centroid_admission_refinement.py', 'assemble_relative_geometry.py')},
              'conclusion': 'The unqualified cellwise rule is not invariant under geometry-preserving subdivision. Both excluded neutron caps become active when subdivided; selecting after refinement fills them back in. A narrower maximal-supporting-facet rule survives this control after geometric regrouping, but is a different hypothesis.',
              'scope': 'Exact rational counterexample and one positive regrouping control. No target face lists used. Not a derivation from WG.'}
    (BASE/'results/centroid_admission_refinement.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
