"""Finite strict restriction audit; does not claim general native descent."""
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/voevodsky'
INPUT = BASE / 'results/ramsey-native-PN-overlap-span-input-v1.json'
CLAIM = BASE / 'contracts/ramsey-face-edge-restriction-attempt.v1.json'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    raw = json.loads(INPUT.read_text())
    ports = raw['ports']
    vertices = list(ports[0]['role'])
    assert len(vertices) == 4 and len(ports) == 48
    facets = [set(vertices) - {v} for v in vertices]
    groups = [[p for p in ports if set(p['faceVertices']) == f] for f in facets]
    assert list(map(len, groups)) == [12] * 4
    pairs = list(itertools.combinations(range(4), 2))
    edges = {(i,j): sorted(facets[i] & facets[j]) for i,j in pairs}
    assert len({tuple(e) for e in edges.values()}) == 6
    assert all(len(e) == 2 for e in edges.values())
    assert all(len(set.intersection(*(facets[i] for i in triple))) == 1
               for triple in itertools.combinations(range(4), 3))
    # Restriction does not replace or reinterpret the parent permit.
    chains = 0
    for p in ports:
        assert sum(p['role'][v] == 'M' for v in p['faceVertices']) == 2
        for e in itertools.combinations(p['faceVertices'], 2):
            restricted = {v:p['role'][v] for v in e}
            for v in e:
                assert restricted[v] == p['role'][v]
                chains += 1
    tested = compatible = 0
    histogram = {}
    example = None
    for cover in itertools.product(*groups):
        bad = [(i,j,v) for (i,j), edge in edges.items() for v in edge
               if cover[i]['role'][v] != cover[j]['role'][v]]
        tested += 1
        compatible += not bad
        histogram[len(bad)] = histogram.get(len(bad), 0) + 1
        if example is None:
            assert bad
            i,j,v = bad[0]
            example = {'charts':[p['chart'] for p in cover], 'faces':list(range(4)),
                       'edge_faces':[i,j], 'edge':edges[i,j], 'vertex':v,
                       'left_role':cover[i]['role'][v], 'right_role':cover[j]['role'][v]}
    assert tested == 12**4 and compatible == 0
    # Independent global-role enumeration, not the cover-loop implementation.
    global_solutions = [roles for roles in itertools.product('CM', repeat=4)
                        if all(sum(roles[k] == 'M' for k in range(4) if k != i) == 2
                               for i in range(4))]
    assert not global_solutions
    # Geometry-only acceptance is deliberately too weak.
    assert all(set(groups[i][0]['faceVertices']) & set(groups[j][0]['faceVertices']) == set(edges[i,j])
               for i,j in pairs)
    assert example['left_role'] != example['right_role']
    result = {
        'schema':'marici.ramsey-face-edge-restriction.audit.v1',
        'scope_id':'four-PN-facets-strict-role-restriction-v1',
        'status':'checked-strict-gluing-obstruction',
        'covers':tested, 'strict_compatible_covers':compatible,
        'face_edge_vertex_chains':chains,
        'disagreement_histogram':histogram, 'first_failed_edge_cell':example,
        'argument':'Edge agreement defines one role at each vertex. Each vertex belongs to three facets. Four facets with two M vertices give 8 M incidences, but a global role function gives 3 times an integer. Thus strict gluing is impossible.',
        'native_restriction_constructor_proved':False,
        'general_chart_descent_refuted':False,
        'parent_resolved':False,
        'source_sha256':{str(p.relative_to(ROOT)).replace('\\','/'):digest(p)
                         for p in [INPUT, CLAIM, Path(__file__)]}}
    path = BASE / 'results/ramsey-face-edge-restriction-v1.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
