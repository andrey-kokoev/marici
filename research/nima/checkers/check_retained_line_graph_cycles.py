"""Retained relationship promotion, with shared-endpoint adjacency supplied.

A graph edge becomes one new record holding its two endpoint record IDs.
Two promoted records are linked exactly when they share a previous endpoint.
Every promoted record and edge is stored once in a persistent ancestry DAG.
This is a new combinatorial rule, not the normalization compiler's dynamics.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json


def promote(vertices, edges, cycle, archive):
    incidence = {v: [] for v in vertices}
    new_vertices = []
    for index, edge in enumerate(sorted(edges)):
        record = f'{cycle}:{index}'
        archive[record] = {'endpoints': list(edge), 'directions': [list(edge), list(reversed(edge))]}
        new_vertices.append(record)
        for endpoint in edge:
            incidence[endpoint].append(record)
    new_edges = set()
    witnesses = {}
    for endpoint, records in incidence.items():
        for pair in combinations(sorted(records), 2):
            assert pair not in new_edges  # simple old edges share at most one endpoint
            new_edges.add(pair)
            witnesses[pair] = endpoint
    assert len(new_vertices) == len(edges)
    assert len(new_edges) == sum(len(es)*(len(es)-1)//2 for es in incidence.values())
    for left, right in new_edges:
        shared = set(archive[left]['endpoints']) & set(archive[right]['endpoints'])
        assert shared == {witnesses[(left, right)]}
    reconstructed = {tuple(archive[v]['endpoints']) for v in new_vertices}
    assert reconstructed == edges
    return new_vertices, new_edges, witnesses


vertices = ['00', '01', '10', '11']
edges = set(combinations(vertices, 2))
archive = {v: {'seed': v} for v in vertices}
initial_directed = {(a,b) for edge in edges for a,b in (edge, edge[::-1])}
assert len(initial_directed) == 12
rows = []
for cycle in range(5):
    degrees = Counter(v for edge in edges for v in edge)
    degree_values = sorted(set(degrees.values()))
    assert len(degree_values) == 1
    assert 2*len(edges) == len(vertices)*degree_values[0]
    rows.append({'promotions': cycle, 'vertices': len(vertices), 'edges': len(edges),
                 'directed_packets': 2*len(edges), 'degree': degree_values[0],
                 'ancestry_depth': cycle})
    if cycle == 4:
        break
    vertices, edges, witnesses = promote(vertices, edges, cycle+1, archive)
    if cycle == 0:
        # Octahedral graph: six vertices, with exactly three disjoint nonedges.
        missing = set(combinations(sorted(vertices), 2)) - edges
        assert len(vertices) == 6 and len(edges) == 12 and len(missing) == 3
        assert Counter(v for pair in missing for v in pair) == Counter({v:1 for v in vertices})
        recovered_directed = {tuple(pair) for v in vertices for pair in archive[v]['directions']}
        assert recovered_directed == initial_directed

assert [(r['vertices'],r['edges']) for r in rows] == [(4,6),(6,12),(12,36),(36,180),(180,1620)]
for old,new in zip(rows, rows[1:]):
    assert new['vertices'] == old['edges']
    assert new['degree'] == 2*(old['degree']-1)

# Growth is not automatic for every seed: degree-two cycles repeat their size.
v = ['a','b','c']; e = set(combinations(v,2)); other_archive = {x:{'seed':x} for x in v}
for k in range(1,5):
    v,e,_ = promote(v,e,k,other_archive)
    assert len(v) == len(e) == 3
# Endpoint-sharing is essential: a disjoint matching yields no new edges.
v = ['a','b','c','d']; e = {('a','b'),('c','d')}
v,e,_ = promote(v,e,1,{x:{'seed':x} for x in v})
assert len(v) == 2 and len(e) == 0

result = {'status':'passed', 'rule':'reciprocal-edge promotion plus shared-endpoint adjacency',
          'cycles':rows, 'archive_record_count':len(archive),
          'preservation':'Every previous edge is reconstructible from its promoted record; first promotion retains all12 original directed packets.',
          'controls':{'triangle_size_stays_3':True,'disjoint_matching_creates_no_links':True},
          'scope':'Combinatorial graph growth under an explicitly supplied new rule; no claim of increased independent information or derived physical dynamics.'}
root = Path(__file__).resolve().parents[1]
(root/'results/retained-line-graph-cycles.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print('promotions | records | undirected links | directed packets | degree')
for r in rows:
    print(f"{r['promotions']:10} | {r['vertices']:7} | {r['edges']:16} | {r['directed_packets']:16} | {r['degree']:6}")
print('PASS: provenance, reconstruction, octahedral incidence, counts, and nongrowing controls.')
