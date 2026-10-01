"""Construct record-vectors from twelve explicitly endpoint-labelled packets.

Endpoint wiring is supplied, not inferred from packet count. No face fillers,
physical geometry, particle assignment or cycle dynamics are inferred.
"""
from itertools import combinations
from collections import defaultdict
from pathlib import Path
import json

# Each packet has a label vector (source address, target address).
# These twelve inputs precede construction of the four grouped record-vectors.
packets = (
    ('00', '01'), ('00', '10'), ('00', '11'),
    ('01', '00'), ('01', '10'), ('01', '11'),
    ('10', '00'), ('10', '01'), ('10', '11'),
    ('11', '00'), ('11', '01'), ('11', '10'),
)
assert len(packets) == len(set(packets)) == 12
by_source = defaultdict(list)
for index, (source, target) in enumerate(packets):
    assert source != target
    by_source[source].append(index)
records = {source: tuple(indices) for source, indices in sorted(by_source.items())}
assert len(records) == 4
assert all(len(record) == 3 for record in records.values())
# Every input belongs to exactly one record; targets resolve to record addresses.
assert sorted(i for record in records.values() for i in record) == list(range(12))
assert all(target in records for source, target in packets)
assert all(set(packets[i][1] for i in record) == set(records) - {source}
           for source, record in records.items())
assert all((target, source) in packets for source, target in packets)
# Pair opposite directed packets into undirected incidence edges.
edges = {tuple(sorted((source, target))) for source, target in packets}
assert edges == set(combinations(sorted(records), 2))
assert len(edges) == 6
triangles = [triple for triple in combinations(sorted(records), 3)
             if all(pair in edges for pair in combinations(triple, 2))]
assert len(triangles) == 4
# Filling every clique is an optional added simplicial completion rule.
assert all(edge in edges for edge in combinations(sorted(records), 2))
# Count alone is insufficient: a directed12-cycle has12 packets and12 records.
other = tuple((str(i), str((i + 1) % 12)) for i in range(12))
assert len(other) == 12 and len({a for a, b in other}) == 12
report = {
    'status': 'passed',
    'input': '12 packets with supplied source/target label vectors',
    'packets': [{'id': f'p{i+1:02}', 'labels': pair} for i, pair in enumerate(packets)],
    'records': {label: [f'p{i+1:02}' for i in indices] for label, indices in records.items()},
    'record_count': len(records),
    'directed_relationship_count': len(packets),
    'undirected_edge_count': len(edges),
    'triangular_boundaries': triangles,
    'graph': 'K4 (tetrahedral skeleton)',
    'simplicial_completion': 'Adding all clique fillers gives4 triangular faces and1 tetrahedral3-simplex; fillers are additional to packet grouping.',
    'counterexample': 'A directed12-cycle has the same packet count but12 grouped records.',
}
path = Path(__file__).resolve().parents[1] / 'results/twelve-packets-to-tetrahedron.json'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print('12 endpoint-labelled packets ->4 record-vectors of3 packets each.')
print('All12 packets retained exactly once; all target references resolve.')
print('Incidence:12 directed arrows,6 undirected edges,4 triangular boundaries: K4.')
print('Counterexample checked:12 differently wired packets give a12-cycle.')
