"""Actual branch observer refinement and provenance-dependent live-state lift."""
from pathlib import Path
import importlib.util
import hashlib
import json
import copy
import sys
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[3]
DIR = ROOT / 'research/voevodsky/results/continuation-quotient'

def load(p):
    return json.loads(p.read_text())
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
# Fresh independent replay against the separately frozen current-input branch.
vp = ROOT / 'research/nima/checkers/verify_incomparable_proof_branch_merge.py'
spec = importlib.util.spec_from_file_location('verify_branch', vp)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
v.N = DIR
v.main()
qpath = DIR / 'minimal-evidence-continuation-quotient.json'
q = load(qpath)
for name, expected in q['input_hashes'].items():
    assert sha(ROOT / name) == expected
branch_path = DIR / 'incomparable-proof-branch-merge.json'
r = load(branch_path)
states = tuple('branch:' + k for k in ('P', 'A', 'B', 'AB'))
t = q['transitions']
o = q['outputs']

def partition(labels):
    def classify(signatures):
        ids = {}
        return {s: ids.setdefault(sig, len(ids)) for s, sig in signatures.items()}
    classes = classify({s: tuple(o[s]) for s in states})
    while True:
        new = classify({s: (tuple(o[s]), tuple(classes[t[s][a]] for a in labels)) for s in states})
        if all((classes[a] == classes[b]) == (new[a] == new[b]) for a in states for b in states):
            return new
        classes = new
old = partition(('merge:A',))
new = partition(('merge:A', 'merge:B'))
assert old['branch:P'] == old['branch:A']
assert len(set(old.values())) == 3 and len(set(new.values())) == 4
projection = {}
for s in states:
    projection[new[s]] = old[s]
# Refinement projection is well defined and intertwines every old transition.
old_transition, new_transition = {}, {}
for s in states:
    key = old[s]
    target = old[t[s]['merge:A']]
    assert key not in old_transition or old_transition[key] == target
    old_transition[key] = target
    new_transition[new[s]] = new[t[s]['merge:A']]
for s in states:
    assert projection[new_transition[new[s]]] == old_transition[projection[new[s]]]
# No old-state-only function recovers both actual states in the split fiber.
split = [s for s in states if old[s] == old['branch:P']]
assert split == ['branch:P', 'branch:A']
assert all(any(candidate != actual for actual in split) for candidate in split)
assert o[t['branch:P']['merge:B']][1] == 'UNRESOLVED'
assert o[t['branch:A']['merge:B']][1] == 'CERTIFIED_INFEASIBLE'

# Upgrade from a known ancestor plus retained, validated accepted-frame journal.
# This retention assumption is explicit. A digest alone is not a retrievable frame.
A = r['frames']['A']
B = r['frames']['B']
assert digest(A['body']) == A['digest']
assert digest(B['body']) == B['digest']
def admit(frame):
    assert digest(frame['body']) == frame['digest']
    name = frame['body']['branch']
    assert name in r['frames'] and frame == r['frames'][name]
    return 'merge:' + name

def replay(journal):
    state = 'branch:P'
    for frame in journal:
        state = t[state][admit(frame)]
    return state
checks = 0
for duplicates in range(9):
    journal = [copy.deepcopy(A) for _ in range(duplicates)]
    state = replay(journal)
    assert state == ('branch:P' if duplicates == 0 else 'branch:A')
    assert old[state] == old['branch:P']
    # The newly admitted B can now be applied to the faithfully recovered state.
    assert replay(journal + [B]) == t[state]['merge:B']
    checks += 1
# Missing A record is indistinguishable from a legitimately empty journal.
assert old[replay([])] == old[replay([A])]
assert replay([]) != replay([A])
# Integrity of an envelope is insufficient: even a rehashed alteration fails.
bad = copy.deepcopy(A)
bad['body']['status'] = 'CERTIFIED_FEASIBLE'
bad['digest'] = digest(bad['body'])
try:
    admit(bad)
except AssertionError:
    pass
else:
    raise AssertionError('modified frame admitted')
report = {
    'passed': True,
    'old_classes_A_only': old,
    'new_classes_A_and_B': new,
    'refinement_projection': projection,
    'old_transition_square_commutes': True,
    'split_fiber': split,
    'old_state_only_upgrade': 'IMPOSSIBLE uniformly over the split fiber',
    'complete_validated_journal_upgrade': 'VERIFIED from the known P ancestor',
    'journal_cases_checked': checks,
    'missing_journal_entry': 'Undetectable from the compressed state alone in this fixture',
    'rehashed_modified_frame_rejected': True,
    'scope': 'Closed branch evidence family and fixed bindings. Journal completeness and known ancestor are inputs; hashes do not establish either. Existing analytic proofs are reused.',
    'dpc_disposition': 'Constructive refinement exists; live upgrade requires distinguishing retained provenance. Unconditional upgrade from the old minimal state is refuted.',
    'inputs_sha256': {str(p.relative_to(ROOT)): sha(p) for p in (qpath, branch_path, vp)},
}
path = DIR / 'incremental-continuation-refinement.json'
path.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
