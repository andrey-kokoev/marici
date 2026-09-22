"""Build minimal finite output/admission quotient of two bound evidence systems.

Branch replay is a NEW current-input composition, written separately. Ladder
edges implement its declared sequential schedule, not arbitrary new proofs.
"""
from pathlib import Path
from itertools import combinations, product
from collections import deque
import importlib.util
import subprocess
import sys
import json
import hashlib

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'research/voevodsky/results/continuation-quotient'
OUT.mkdir(parents=True, exist_ok=True)
N = ROOT / 'research/nima'
G = ROOT / 'research/grothendieck'
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):
    return json.loads(p.read_text())
def module(name, p):
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m
# Freeze and replay current inputs in our own directory, preserving Nima's trial.
for name in ('check_incomparable_proof_branch_merge', 'verify_incomparable_proof_branch_merge'):
    m = module(name, N / 'checkers' / (name + '.py'))
    m.N = OUT
    m.main()
subprocess.run([sys.executable, str(G / 'checkers/check_midpoint_signed_refinement.py')], check=True)
branch = load(OUT / 'incomparable-proof-branch-merge.json')
bc = load(OUT / 'incomparable-proof-branch-contract.json')
ladder = load(G / 'results/midpoint-signed-refinement.json')
old = load(N / 'results/incomparable-proof-branch-merge.json')
# Record whether current reconstruction changed the actual primitive states.
same_archived_boxes = branch['primitive_boxes'] == old['primitive_boxes']
binding = bc['task_sha256']
ladder_binding = ladder['frozen_task_sha256']
assert binding != ladder_binding
outputs = {f'branch:{k}': [binding, v['status']] for k, v in branch['task_results'].items()}
outputs.update({f'ladder:{i+1}': [ladder_binding, s['status']] for i, s in enumerate(ladder['stages'])})
alphabet = ('merge:A', 'merge:B', 'refine:2', 'refine:3')
transitions = {s: {} for s in outputs}
# Derive merge transitions from exact primitive intersections.
from fractions import Fraction as Q
boxes = {k: {j: tuple(map(Q, v)) for j, v in b.items()} for k, b in branch['primitive_boxes'].items()}
for name, box in boxes.items():
    for label in ('A', 'B'):
        merged = {k: (max(box[k][0], boxes[label][k][0]), min(box[k][1], boxes[label][k][1])) for k in box}
        matches = [n for n, b in boxes.items() if b == merged]
        assert len(matches) == 1
        transitions['branch:' + name]['merge:' + label] = 'branch:' + matches[0]
transitions['ladder:1']['refine:2'] = 'ladder:2'
transitions['ladder:2']['refine:3'] = 'ladder:3'
# Missing transitions mean rejection with unchanged state. Rejection is visible.
def step(s, a):
    return ('ADMITTED', transitions[s][a]) if a in transitions[s] else ('REJECTED', s)
def classify(signatures):
    unique = {}
    return {s: unique.setdefault(sig, len(unique)) for s, sig in signatures.items()}
classes = classify({s: tuple(o) for s, o in outputs.items()})
rounds = 0
while True:
    refined = classify({s: (tuple(outputs[s]), tuple((a, step(s, a)[0], classes[step(s, a)[1]]) for a in alphabet)) for s in outputs})
    rounds += 1
    # Compare partitions independently of class-number naming.
    if all((classes[a] == classes[b]) == (refined[a] == refined[b]) for a in outputs for b in outputs):
        classes = refined
        break
    classes = refined
assert len(set(classes.values())) == 7
# Construct finite distinguishing words for every pair: minimality certificate.
def witness(a, b):
    queue = deque([(a, b, ())]); seen = set()
    while queue:
        x, y, word = queue.popleft()
        if outputs[x] != outputs[y]:
            return word
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for label in alphabet:
            ax, xx = step(x, label); ay, yy = step(y, label)
            if ax != ay:
                return word + (label,)
            queue.append((xx, yy, word + (label,)))
    raise AssertionError('claimed distinct classes have no distinguishing continuation')
witnesses = [{'states': [a, b], 'word': list(witness(a, b))} for a, b in combinations(outputs, 2)]
# Verify congruence directly for every class and label.
for a in outputs:
    for b in outputs:
        if classes[a] == classes[b]:
            assert outputs[a] == outputs[b]
            for label in alphabet:
                aa, x = step(a, label); ab, y = step(b, label)
                assert aa == ab and classes[x] == classes[y]
# Exact branch confluence, duplicates and all two-way cut compositions.
def run(s, word):
    for a in word:
        _, s = step(s, a)
    return s
checks = 0
for s in outputs:
    for length in range(5):
        for word in product(alphabet, repeat=length):
            for cut in range(length + 1):
                assert run(run(s, word[:cut]), word[cut:]) == run(s, word)
                checks += 1
for s in boxes:
    state = 'branch:' + s
    assert run(state, ('merge:A', 'merge:B')) == run(state, ('merge:B', 'merge:A'))
    for label in ('merge:A', 'merge:B'):
        assert run(state, (label, label)) == run(state, (label,))
report = {'passed': True, 'current_branch_replay_preserves_archived_boxes': same_archived_boxes,
          'construction': 'coarsest output-and-admission-respecting congruence by finite partition refinement',
          'state_count': len(outputs), 'quotient_class_count': len(set(classes.values())),
          'partition_rounds': rounds, 'outputs': outputs, 'transitions': transitions,
          'alphabet': list(alphabet), 'rejection_policy': 'observable rejection; state unchanged',
          'classes': classes, 'pairwise_distinguishing_words': witnesses,
          'composition_checks': checks,
          'admission_scope': 'Two named branch frames and the sequential recorded ladder only. Cross-binding extensions are rejected; analytical validity remains with owning proofs.',
          'minimality_scope': 'Any deterministic observer preserving these bound outputs and all declared continuation admissions needs seven states; four branch states and three ladder stages. This is not a minimal primitive-numeric representation for arbitrary new refinements.',
          'input_hashes': {str(p.relative_to(ROOT)): sha(p) for p in
                          (OUT / 'incomparable-proof-branch-contract.json', OUT / 'incomparable-proof-branch-merge.json',
                           G / 'results/midpoint-signed-refinement.json', G / 'results/midpoint-signed-refinement-contract.json')},
          'trial_scope': 'Retrospective finite construction; no blinded performance claim or analytical proof generation timing.'}
(OUT / 'minimal-evidence-continuation-quotient.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: report[k] for k in ('passed', 'current_branch_replay_preserves_archived_boxes', 'state_count', 'quotient_class_count', 'partition_rounds', 'composition_checks')}, indent=2))
