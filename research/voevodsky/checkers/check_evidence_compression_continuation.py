"""Exact continuation test on archived primitive boxes, with admission drift gate."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json
import hashlib
import importlib.util
import copy
import sys
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[3]
N = ROOT / 'research/nima/results'
G = ROOT / 'research/grothendieck/results'
def load(p):
    return json.loads(p.read_text())
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
contract_path = N / 'incomparable-proof-branch-contract.json'
report_path = N / 'incomparable-proof-branch-merge.json'
c, r = load(contract_path), load(report_path)
assert r['contract_sha256'] == sha(contract_path)
drift = [{'file': name, 'expected': h, 'actual': sha(G / name)}
         for name, h in c['inputs_sha256'].items() if sha(G / name) != h]
boxes = {name: {k: tuple(map(Q, v)) for k, v in box.items()}
         for name, box in r['primitive_boxes'].items()}
def meet(a, b):
    out = {k: (max(a[k][0], b[k][0]), min(a[k][1], b[k][1])) for k in a}
    assert all(lo <= hi for lo, hi in out.values())
    return out
spec = importlib.util.spec_from_file_location('task_engine', ROOT / 'research/grothendieck/checkers/three_channel_source_task.py')
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)
engine = t.SourceTask(G / 'three-channel-source-task-calibration-projection272.json')
assert sha(G / 'three-channel-source-task-calibration-projection272.json') == c['inputs_sha256']['three-channel-source-task-calibration-projection272.json']
def gain(b):
    assert min(b['C'] + b['H'] + b['XA'] + b['XB']) > 0
    assert b['muA'][0] > b['L'][1] and b['muB'][0] > b['L'][1]
    def end(i):
        return 2*b['XA'][i]*b['XB'][i]*(b['C'][i]+b['H'][i]*(b['muA'][i]-b['L'][1-i]))*(b['C'][i]+b['H'][i]*(b['muB'][i]-b['L'][1-i]))
    p = engine.calibrations('private')['positive']
    return max(end(0), p[0]), min(end(1), p[1])
def status_interval(interval):
    local = copy.copy(engine)
    channels = engine.calibrations('private')
    channels['positive'] = interval
    local.calibrations = lambda mode: dict(channels)
    return local.certify(c['task'])['status']
def status(b):
    return status_interval(gain(b))
for name, box in boxes.items():
    assert gain(box) == tuple(map(Q, r['gain_bounds'][name]))
    assert status(box) == r['task_results'][name]['status']
transitions = {}
for name, box in boxes.items():
    transitions[name] = {}
    for extension in ('A', 'B'):
        new = meet(box, boxes[extension])
        matches = [key for key, value in boxes.items() if new == value]
        assert len(matches) == 1
        transitions[name][extension] = matches[0]
assert status(boxes['P']) == status(boxes['A']) == 'UNRESOLVED'
assert transitions['P']['B'] == 'B' and transitions['A']['B'] == 'AB'
assert status(boxes['B']) == 'UNRESOLVED'
assert status(boxes['AB']) == 'CERTIFIED_INFEASIBLE'
collisions = [[a, b] for a, b in combinations(boxes, 2) if gain(boxes[a]) == gain(boxes[b])]
# Compare the specified scalar-intersection merge with primitive recomputation.
ga, gb = gain(boxes['A']), gain(boxes['B'])
scalar_meet = max(ga[0], gb[0]), min(ga[1], gb[1])
assert status_interval(scalar_meet) == 'UNRESOLVED'
assert scalar_meet != gain(meet(boxes['A'], boxes['B']))
# Continuation signatures distinguish every state using empty, A and B words.
signatures = {name: [status(box), status(meet(box, boxes['A'])), status(meet(box, boxes['B']))]
              for name, box in boxes.items()}
assert len({tuple(v) for v in signatures.values()}) == 4
out = {
    'exact_archived_box_checks_passed': True,
    'fresh_source_admission': 'BLOCKED_INPUT_DRIFT' if drift else 'HASH_BINDINGS_CURRENT_REQUIRES_OWNING_PROOF_REPLAY',
    'drift': drift,
    'transition_table': transitions,
    'status_continuation_signatures_empty_A_B': signatures,
    'verdict_compression': 'Not a continuation congruence on these archived evidence states',
    'equal_gain_interval_pairs': collisions,
    'scalar_interval_congruence': 'No equal-image counterexample established' if not collisions else 'Requires pairwise continuation analysis',
    'scalar_intersection_merge': 'Fails to commute with primitive merge and gain recomputation',
    'scope': 'Exact conditional mathematics on frozen boxes. Changed owning evidence blocks fresh source-admission claim; original contract is not rewritten.',
    'inputs_sha256': {str(p.relative_to(ROOT)): sha(p) for p in (contract_path, report_path)},
}
path = ROOT / 'research/voevodsky/results/evidence-compression-continuation.json'
path.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
