"""Two-sided contexts for actual coupled words and an independent action observer.

Candidate Q(w) is the partial transformation of 638 concrete coupled states,
constructed directly from source/evidence transitions. Context observations
are terminal operational outputs, with rejected compositions mapped to bottom.
"""
from pathlib import Path
from collections import deque
import subprocess
import json
import hashlib
import sys
ROOT = Path(__file__).resolve().parents[3]
N = ROOT / 'research/nima'
OUT = ROOT / 'research/voevodsky/results'
p = N / 'results/actual-source-evidence-coupling.json'
labels = [('source', e, m) for e in range(6) for m in (0, 1)] + [('acquire',), ('deliver',), ('issue', 0), ('issue', 1)]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, v): p.write_text(json.dumps(v, indent=2) + '\n')
contract = {'source_sha256': sha(p),
 'Q': 'Partial transformation of all concrete coupled states, induced directly by a word.',
 'contexts': 'Initial-state choice plus admitted left word, followed by tested word and arbitrary right word. Observe terminal typed corner, received and issued values; failed prefix is bottom.',
 'prediction': 'Q equality iff two-sided context equivalence.',
 'scope': 'Independent candidate action observer. No preexisting claim that this is the assembled numerical observer on developments; no time reversal assumption.'}
cp = OUT / 'two-sided-coupled-context-contract.json'; save(cp, contract)
subprocess.run([sys.executable, str(N / 'checkers/verify_source_evidence_coupling.py')], check=True, capture_output=True, text=True)
d = json.loads(p.read_text()); states = d['states']; n = len(states)
edges = [{tuple(a): j for a, j in s['transitions']} for s in states]
step = [[e.get(a, -1) for a in labels] for e in edges]
outputs = [(0, sum(1 << e for e in s['word']), s['received'], s['issued']) for s in states]
# Independent behavioral partition, with rejected words terminally bottom.
def classify(keys):
 ids = {}; return [ids.setdefault(k, len(ids)) for k in keys]
classes = classify(outputs)
while True:
 new = classify([(outputs[i], tuple(-1 if j == -1 else classes[j] for j in row)) for i, row in enumerate(step)])
 if new == classes: break
 classes = new
assert len(set(classes)) == 62
# All states have an explicit initial left context.
left = {i: (i, ()) for i in d['initial_state_ids']}; todo = deque(left)
while todo:
 i = todo.popleft()
 for a, j in enumerate(step[i]):
  if j >= 0 and j not in left:
   initial, word = left[i]; left[j] = (initial, word + (a,)); todo.append(j)
assert len(left) == n
identity = tuple(range(n)); words = {identity: ()}; todo = deque([identity])
while todo:
 f = todo.popleft()
 for a in range(len(labels)):
  g = tuple(-1 if j < 0 else step[j][a] for j in f)
  if g not in words:
   words[g] = words[f] + (a,); todo.append(g)
  assert len(words) <= 100000
# Signature lists resulting right-profile classes for EVERY reachable left state.
def signature(f): return tuple(-1 if j < 0 else classes[j] for j in f)
groups = {}
for f in words: groups.setdefault(signature(f), []).append(f)
witness = None
for sig, fs in groups.items():
 if len(fs) > 1:
  f, g = fs[:2]
  i = next(i for i in range(n) if f[i] != g[i])
  assert f[i] >= 0 and g[i] >= 0 and classes[f[i]] == classes[g[i]]
  initial, prefix = left[i]
  witness = {'word_x': [labels[a] for a in words[f]], 'word_y': [labels[a] for a in words[g]],
             'initial_state': initial, 'left_word': [labels[a] for a in prefix],
             'context_state': i, 'different_concrete_targets': [f[i], g[i]],
             'equal_target_profile_class': classes[f[i]],
             'targets': [states[j] for j in (f[i], g[i])]}
  break
# Test closure of contextual equivalence under left and right generators.
checks = 0
for sig, fs in groups.items():
 for a in range(len(labels)):
  right = set(); left_sigs = set()
  for f in fs:
   right.add(signature(tuple(-1 if j < 0 else step[j][a] for j in f)))
   left_sigs.add(signature(tuple(-1 if step[i][a] < 0 else f[step[i][a]] for i in range(n))))
  assert len(right) == len(left_sigs) == 1
  checks += 2 * len(fs)
assert sha(p) == contract['source_sha256']
report = {'verdict': 'REFUTED_BY_REDUNDANCY' if witness else 'CORROBORATED_FOR_FROZEN_ACTION_OBSERVER',
 'contract_sha256': sha(cp), 'concrete_states': n, 'reachable_left_context_states': len(left),
 'right_profile_classes': len(set(classes)), 'independent_Q_values': len(words),
 'two_sided_context_classes': len(groups), 'generator_congruence_checks': checks,
 'redundancy_witness': witness,
 'sufficiency': 'Equal concrete transformations give equal contextual observations.',
 'completeness_basis': 'Every concrete state is reached by a left context. The fixed-point right-profile partition distinguishes exactly all suffix observations. Hence equal signatures are equivalent under all two-sided finite contexts.',
 'composition': 'Context equivalence is checked stable under both left and right multiplication by every generator, hence every finite word.',
 'reversal': 'Not tested: opposite protocol admission remains a separate frozen-contract requirement.',
 'scope': 'Terminal operational observations, not traces of every interior event; this choice is fixed before computation.'}
save(OUT / 'two-sided-coupled-context.json', report)
print(json.dumps({k: v for k, v in report.items() if k != 'redundancy_witness'}, indent=2))
if witness:
 print(json.dumps({k: v for k, v in witness.items() if k != 'targets'}, indent=2))
