"""Test label-preserving orientation reversal of the concrete protocol graph.

Forward and opposite states retain identical operational outputs. Opposite
edges reverse actual transitions with labels held fixed. Nondeterministic
trace semantics is used because reversed edges can have several successors.
This constructs a logical opposite, not an authorized reverse-time protocol.
"""
from pathlib import Path
from collections import deque
import json
import hashlib
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[3]
N = ROOT / 'research/nima'
OUT = ROOT / 'research/voevodsky/results'
p = N / 'results/actual-source-evidence-coupling.json'
labels = [('source', e, m) for e in range(6) for m in (0, 1)] + [('acquire',), ('deliver',), ('issue', 0), ('issue', 1)]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, x): p.write_text(json.dumps(x, indent=2) + '\n')
contract = {'source_sha256': sha(p),
 'forward': 'Existing reachable coupled protocol graph.',
 'opposite': 'Reverse every edge, retaining event labels and endpoint output labels.',
 'comparison': 'Forward state s versus opposite state s; same present output. Compare sets of terminal outputs for every word; empty successor set denotes rejection.',
 'orientation_reference': 'Fixed action meanings and fixed typed source-mask/received/issued outputs.',
 'nonclaim': 'No transport of labels or outputs and no admission of a physically executable reverse protocol.'}
cp = OUT / 'coupled-orientation-contract.json'; save(cp, contract)
subprocess.run([sys.executable, str(N / 'checkers/verify_source_evidence_coupling.py')], check=True, capture_output=True, text=True)
d = json.loads(p.read_text()); states = d['states']; n = len(states)
forward = [[set() for _ in labels] for _ in states]
opposite = [[set() for _ in labels] for _ in states]
for i, s in enumerate(states):
 for raw, j in s['transitions']:
  a = labels.index(tuple(raw)); forward[i][a].add(j); opposite[j][a].add(i)
outputs = [(0, sum(1 << e for e in s['word']), s['received'], s['issued']) for s in states]
def observations(subset): return frozenset(outputs[i] for i in subset)
def advance(table, subset, a): return frozenset(j for i in subset for j in table[i][a])
def distinguish(i):
 initial = (frozenset([i]), frozenset([i]))
 queue = deque([(initial, ())]); seen = {initial}
 while queue:
  (f, r), word = queue.popleft()
  if observations(f) != observations(r):
   return word, f, r
  for a in range(len(labels)):
   nxt = (advance(forward, f, a), advance(opposite, r, a))
   if nxt not in seen:
    seen.add(nxt); queue.append((nxt, word + (a,)))
  assert len(seen) <= 100000, 'Search budget exhausted; do not infer equivalence'
 return None
witnesses = []; indistinguishable = []
for i in range(n):
 result = distinguish(i)
 if result is None:
  indistinguishable.append(i)
 else:
  word, f, r = result
  witnesses.append({'state': i, 'word': [labels[a] for a in word],
                    'forward_targets': sorted(f), 'opposite_targets': sorted(r),
                    'forward_outputs': sorted(observations(f), key=repr),
                    'opposite_outputs': sorted(observations(r), key=repr)})
# Replay every separating word, independently of search bookkeeping.
for w in witnesses:
 f = r = frozenset([w['state']])
 for label in w['word']:
  a = labels.index(tuple(label)); f = advance(forward, f, a); r = advance(opposite, r, a)
 assert observations(f) != observations(r)
assert sha(p) == contract['source_sha256']
report = {'passed': True, 'contract_sha256': sha(cp),
 'states_tested': n, 'direction_distinguishable_states': len(witnesses),
 'indistinguishable_states': indistinguishable,
 'maximum_shortest_witness_length': max((len(w['word']) for w in witnesses), default=0),
 'witnesses': witnesses,
 'interpretation': 'Direction is relative to the fixed labels and outputs. This test does not address simultaneous transport of observer, source orientation, labels and outputs.',
 'scope': 'Logical graph opposite with set-valued trace observation; no probabilistic interpretation or physical reverse execution.'}
save(OUT / 'coupled-orientation-distinguishability.json', report)
print(json.dumps({k: v for k, v in report.items() if k != 'witnesses'}, indent=2))
print(json.dumps(witnesses[:2], indent=2))
