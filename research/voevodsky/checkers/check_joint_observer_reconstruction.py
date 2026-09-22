"""Exact joint image versus common-verdict pullback for actual evidence observers."""
from pathlib import Path
from itertools import product
import subprocess
import sys
import json
import hashlib
ROOT = Path(__file__).resolve().parents[3]
DIR = ROOT / 'research/voevodsky/results/continuation-quotient'
checker = Path(__file__).with_name('check_common_continuation_refinement.py')
subprocess.run([sys.executable, str(checker)], check=True, capture_output=True, text=True)
p = DIR / 'common-continuation-refinement.json'
r = json.loads(p.read_text())
branch_path = DIR / 'incomparable-proof-branch-merge.json'
assert hashlib.sha256(branch_path.read_bytes()).hexdigest() == r['input_sha256']
branch = json.loads(branch_path.read_text())
a, b = r['quotients']['A_only'], r['quotients']['B_only']
states = tuple(a)
status = {s: branch['task_results'][s]['status'] for s in states}
image = {(a[s], b[s]): s for s in states}
assert len(image) == len(states) == 4
cartesian = set(product(set(a.values()), set(b.values())))
def class_status(projection):
    out = {}
    for s in states:
        if projection[s] in out:
            assert out[projection[s]] == status[s]
        out[projection[s]] = status[s]
    return out
sa, sb = class_status(a), class_status(b)
# Shared task binding is fixed throughout. Add common verdict as a consistency
# check, then ask whether its categorical set pullback equals the joint image.
pullback = {(x, y) for x, y in cartesian if sa[x] == sb[y]}
assert len(cartesian) == 9 and len(pullback) == 5
spurious = pullback - set(image)
assert spurious == {(a['B'], b['A'])}
x, y = next(iter(spurious))
assert {s for s in states if a[s] == x} == {'B'}
assert {s for s in states if b[s] == y} == {'A'}
# Reconstruct only through the actual source image: empty fibers reject.
fibers = {pair: [s for s in states if (a[s], b[s]) == pair] for pair in cartesian}
assert all(len(v) <= 1 for v in fibers.values())
assert sum(bool(v) for v in fibers.values()) == 4
# Joint transitions can be realized from the recovered state; individual
# quotients support only the language for which they were minimized.
index = {'P': 0, 'A': 1, 'B': 2, 'AB': 3}
bits = {'P': 0, 'A': 1, 'B': 2, 'AB': 3}
by_bits = {v: k for k, v in bits.items()}
transitions = []
for pair, s in image.items():
    for label, mask in (('A', 1), ('B', 2)):
        # Verify the named successor from actual primitive intersections.
        from fractions import Fraction as Q
        boxes = {k: {j: tuple(map(Q, z)) for j, z in v.items()} for k, v in branch['primitive_boxes'].items()}
        merged = {k: (max(boxes[s][k][0], boxes[label][k][0]), min(boxes[s][k][1], boxes[label][k][1])) for k in boxes[s]}
        successor = by_bits[bits[s] | mask]
        assert merged == boxes[successor]
        target = (a[successor], b[successor])
        assert image[target] == successor
        transitions.append({'from': list(pair), 'extension': label, 'to': list(target)})
# A mixed-time packet has no single-state reconstruction, but admits a joint
# history of evidence accumulation: P -> B -> AB, P -> A -> AB.
assert by_bits[bits['A'] | bits['B']] == 'AB'
report = {
    'passed': True,
    'cartesian_pairs': 9,
    'common_verdict_compatible_pairs': 5,
    'source_realizable_same_state_pairs': 4,
    'joint_image': [{'local_pair': list(pair), 'source_evidence_state': s} for pair, s in image.items()],
    'spurious_common_verdict_pair': list(next(iter(spurious))),
    'spurious_pair_fibers': {'A_observer': ['B'], 'B_observer': ['A']},
    'joint_transitions': transitions,
    'same_state_reconstruction': 'unique on the actual image; reject outside it',
    'asynchronous_boundary': 'Local observations of B and A can come from different cuts of a common accumulated evidence history. Same-state rejection alone does not refute that multi-cut history. Their primitive merge is AB.',
    'scope': 'Four exact frozen evidence states, not unique reconstruction of a physical source. The common-verdict pullback is strictly larger than the actual joint image.',
    'inputs_sha256': {str(f.relative_to(ROOT)): hashlib.sha256(f.read_bytes()).hexdigest() for f in (p, branch_path)},
}
(DIR / 'joint-observer-reconstruction.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
