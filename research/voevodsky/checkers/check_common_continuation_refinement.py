"""Common source-backed refinement of two closed primitive merge languages."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import importlib.util
import json
import hashlib
import sys
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[3]
DIR = ROOT / 'research/voevodsky/results/continuation-quotient'
p = ROOT / 'research/nima/checkers/verify_incomparable_proof_branch_merge.py'
spec = importlib.util.spec_from_file_location('owning_replay', p)
v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
v.N = DIR; v.main()
rpath = DIR / 'incomparable-proof-branch-merge.json'
r = json.loads(rpath.read_text())
boxes = {n: {k: tuple(map(Q, x)) for k, x in b.items()} for n, b in r['primitive_boxes'].items()}
states = tuple(boxes)
outputs = {n: r['task_results'][n]['status'] for n in states}
def meet(a, b):
    out = {k: (max(a[k][0], b[k][0]), min(a[k][1], b[k][1])) for k in a}
    assert all(lo <= hi for lo, hi in out.values())
    return out
# Source derivation: each letter denotes its independently replayed primitive
# constraint package; multiplication is exact same-coordinate intersection.
def action(evidence):
    result = []
    for s in states:
        value = meet(boxes[s], evidence)
        matches = [n for n in states if boxes[n] == value]
        assert len(matches) == 1
        result.append(states.index(matches[0]))
    return tuple(result)
identity = tuple(range(len(states)))
A, B = action(boxes['A']), action(boxes['B'])
def then(f, g):
    return tuple(g[f[i]] for i in range(len(states)))
def closure(generators):
    monoid = {identity}
    while True:
        enlarged = monoid | {then(f, g) for f in monoid for g in generators}
        if enlarged == monoid:
            return monoid
        monoid = enlarged
LA, LB = closure((A,)), closure((B,))
common = closure((A, B))
assert len(LA) == len(LB) == 2 and len(common) == 4
assert LA & LB == {identity}
assert then(A, B) == then(B, A) == action(boxes['AB'])
assert then(A, A) == A and then(B, B) == B
# Source semantics for the four elements, including all mixed products.
source_semantics = {action(box): box for box in boxes.values()}
assert set(source_semantics) == common
for f in common:
    for g in common:
        assert then(f, g) == action(meet(source_semantics[f], source_semantics[g]))

def quotient(language):
    order = sorted(language)
    signatures = {s: tuple(outputs[states[f[i]]] for f in order) for i, s in enumerate(states)}
    unique = {}
    return {s: unique.setdefault(sig, len(unique)) for s, sig in signatures.items()}
qa, qb, qc = quotient(LA), quotient(LB), quotient(common)
assert len(set(qa.values())) == len(set(qb.values())) == 3
assert len(set(qc.values())) == 4
projections = []
checks = 0
for language, small in ((LA, qa), (LB, qb)):
    projection = {}
    for s in states:
        if qc[s] in projection:
            assert projection[qc[s]] == small[s]
        projection[qc[s]] = small[s]
    for f in language:
        induced = {}
        for i, s in enumerate(states):
            target = small[states[f[i]]]
            if small[s] in induced:
                assert induced[small[s]] == target
            induced[small[s]] = target
            assert projection[qc[states[f[i]]]] == induced[projection[qc[s]]]
            checks += 1
    projections.append(projection)
# Exhaustive semantic closure makes these checks cover arbitrary word length:
# each word acts as one of the four monoid elements.
for f in common:
    for g in common:
        for h in common:
            assert then(then(f, g), h) == then(f, then(g, h))
# Pair of local observations identifies the common state in this fixture.
assert len({(qa[s], qb[s]) for s in states}) == 4
report = {
    'passed': True,
    'language_semantics': 'A-only and B-only proof-evidence merges on the same frozen primitive source quantities',
    'semantic_language_sizes': {'A': len(LA), 'B': len(LB), 'common': len(common)},
    'overlap': 'identity only; common ancestor merge is identity',
    'quotients': {'A_only': qa, 'B_only': qb, 'common': qc},
    'common_to_local_projections': projections,
    'projection_square_checks': checks,
    'all_mixed_products_checked': 16,
    'associativity_checks': 64,
    'joint_execution': 'All four source-evidence meets are nonempty; A and B commute and are idempotent',
    'joint_local_observation_injective_on_common_states': True,
    'scope': 'Closed finite branch family, independently replayed under its current frozen binding. Arbitrary new languages, signed-ladder cross-task mixing and physical execution are outside this test. Owning analytical proofs justify bound validity.',
    'input_sha256': hashlib.sha256(rpath.read_bytes()).hexdigest(),
}
(DIR / 'common-continuation-refinement.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
