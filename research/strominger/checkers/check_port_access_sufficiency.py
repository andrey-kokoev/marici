"""Exact ideal permutation-network bridge; no hardware or noise claim."""
from pathlib import Path
from itertools import combinations
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/strominger'
receipt = BASE / 'results/endpoint-continuation-cells/verification.json'
r = json.loads(receipt.read_text())
assert r['status'] == 'pass'
for path, digest in r['sha256'].items():
    assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
G = [tuple('ABCD'.index(v) for v in s['g']) for s in r['states'] if s['bit'] == 0]
assert len(set(G)) == 12

def comp(h, g):
    return tuple(h[g[i]] for i in range(4))

def column(g, s):
    return tuple(int(t == g[s]) for t in range(4))

def descends(k, s, side):
    return all(column(comp(k, g) if side == 'left' else comp(g, k), s)
               == column(comp(k, h) if side == 'left' else comp(h, k), s)
               for g, h in combinations(G, 2) if column(g, s) == column(h, s))

checks = []
for s in range(4):
    assert len({column(g, s) for g in G}) == 4
    assert all(sum(column(g, s) == column(h, s) for h in G) == 3 for g in G)
    assert all(descends(k, s, 'left') for k in G)
    right = [k for k in G if descends(k, s, 'right')]
    assert right == [k for k in G if k[s] == s]
    assert len(right) == 3
    for t in range(4):
        if t != s:
            assert len({(column(g, s), column(g, t)) for g in G}) == 12
    checks.append({'source': 'ABCD'[s], 'single_column_classes': 4,
                   'fiber_size': 3, 'descending_output_permutations': 12,
                   'descending_input_permutations': 3})
# Same current output and all output-side permutations; different second column.
g = (0, 1, 2, 3)
h = (0, 2, 3, 1)
assert g in G and h in G
assert column(g, 0) == column(h, 0)
assert column(g, 1) != column(h, 1)
assert all(column(comp(k, g), 0) == column(comp(k, h), 0) for k in G)
result = {
    'status': 'pass',
    'model': 'Ideal four-port permutation transfer P_g e_s = e_g(s), g in A4; persistent network configuration, fixed source input, output-side transports.',
    'checks': checks,
    'witness': {'networks': ['ABCD', 'ACDB'], 'first_input': 'A',
                'first_outputs': ['A', 'A'], 'second_input': 'B',
                'second_outputs': ['B', 'C']},
    'scope': 'Exact matrix/finite-state bridge. No actual apparatus characterization; Boolean XOR pointer and retained controller state are not supplied by passive routing.',
    'sha256': {str(p.relative_to(ROOT)).replace('\\', '/'): hashlib.sha256(p.read_bytes()).hexdigest()
               for p in (receipt, Path(__file__).resolve())},
}
out = BASE / 'results/port-access-sufficiency/verification.json'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
