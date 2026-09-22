"""Exact relational Beck-Chevalley test on actual observer comparison square.

For X' --g'--> X, f':X'->Y', f:X->Y, g:Y'->Y,
compare inverse_g(direct_f(S)) and direct_f'(inverse_g'(S)).
"""
from pathlib import Path
from itertools import combinations
import json
import hashlib
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[3]
DIR = ROOT / 'research/voevodsky/results/continuation-quotient'
subprocess.run([sys.executable, str(Path(__file__).with_name('check_common_continuation_refinement.py'))], check=True, capture_output=True, text=True)
p = DIR / 'common-continuation-refinement.json'
r = json.loads(p.read_text())
branch_path = DIR / 'incomparable-proof-branch-merge.json'
assert hashlib.sha256(branch_path.read_bytes()).hexdigest() == r['input_sha256']
branch = json.loads(branch_path.read_text())
qa, qb = r['quotients']['A_only'], r['quotients']['B_only']
source = tuple(qa)
X, Yprime = set(qa.values()), set(qb.values())
# The common overlap is the fixed problem's current status.
out = {s: branch['task_results'][s]['status'] for s in source}
f, g = {}, {}
for s in source:
    assert qa[s] not in f or f[qa[s]] == out[s]
    assert qb[s] not in g or g[qb[s]] == out[s]
    f[qa[s]], g[qb[s]] = out[s], out[s]
assert all(f[qa[s]] == g[qb[s]] for s in source)
def powerset(values):
    values = sorted(values)
    for n in range(len(values) + 1):
        for subset in combinations(values, n): yield set(subset)
def lhs(S):
    forward = {f[x] for x in S}
    return {y for y in Yprime if g[y] in forward}
def rhs(S): return {qb[s] for s in source if qa[s] in S}
failures = []
for S in powerset(X):
    left, right = lhs(S), rhs(S)
    assert right <= left
    if left != right:
        failures.append({'input': sorted(S), 'overlap_route': sorted(left), 'source_route': sorted(right), 'spurious': sorted(left - right)})
assert failures
single = next(w for w in failures if w['input'] == [qa['B']])
assert qb['A'] in single['spurious']
# The set-theoretic pullback makes the equality true by adding every overlap pair.
pullback = {(x, y) for x in X for y in Yprime if f[x] == g[y]}
actual_image = {(qa[s], qb[s]) for s in source}
assert len(pullback) == 5 and len(actual_image) == 4
for S in powerset(X):
    assert lhs(S) == {y for x, y in pullback if x in S}
# The source-admitted joint relation instead transports exactly the real witnesses.
for S in powerset(X):
    assert rhs(S) == {y for x, y in actual_image if x in S}
# Transpose preserves the source relation, and exposes the dual failure too.
dual_failures = []
for T in powerset(Yprime):
    left = {x for x in X if f[x] in {g[y] for y in T}}
    right = {qa[s] for s in source if qb[s] in T}
    assert right <= left
    if left != right: dual_failures.append({'input': sorted(T), 'overlap_route': sorted(left), 'source_route': sorted(right)})
assert dual_failures
report = {
    'passed': True,
    'beck_chevalley_equality': 'REFUTED for the actual common-verdict square',
    'commuting_square': True,
    'forward_subset_tests': 2 ** len(X), 'forward_failures': failures,
    'reverse_subset_tests': 2 ** len(Yprime), 'reverse_failures': dual_failures,
    'actual_joint_image_size': len(actual_image), 'overlap_pullback_size': len(pullback),
    'missing_lift_pairs': [list(pair) for pair in sorted(pullback - actual_image)],
    'source_relation_transport_exact': True,
    'criterion': 'For finite sets with existential direct image, BC for every subset iff every overlap-compatible pair has a source lift. Singleton subsets suffice to test this.',
    'scope': 'Actual four-state evidence restrictions and their common status map. Pullback completion adds a pair without an admitted same-state source witness; it is not a source-authorized repair.',
    'inputs_sha256': {str(q.relative_to(ROOT)): hashlib.sha256(q.read_bytes()).hexdigest() for q in (p, branch_path)}
}
(DIR / 'source-beck-chevalley.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
