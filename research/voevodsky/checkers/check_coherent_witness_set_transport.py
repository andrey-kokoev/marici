"""Exact forward/backward witness-set transport on the actual runtime packet.

No hidden concrete source identifiers: indices below address packet rows only.
Knowledge is a subset of a local tuple's compatible behavioral witnesses.
"""
from pathlib import Path
from collections import defaultdict, deque
import subprocess
import sys
import hashlib
import json
ROOT = Path(__file__).resolve().parents[3]
N = ROOT / 'research/nima'
OUT = ROOT / 'research/voevodsky/results'
p = N / 'results/relational-live-witness-runtime.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, x): p.write_text(json.dumps(x, indent=2) + '\n')
cp = OUT / 'coherent-witness-set-transport-contract.json'
save(cp, {'packet_sha256': sha(p),
 'knowledge': 'Nonempty subsets of behavioral witnesses sharing one observed local-view tuple; empty means incompatible observed history.',
 'update': 'Relational image of the CURRENT witness set under the observed label/admission stratum, intersected with the observed next-view fiber.',
 'reverse': 'Transpose of the same stratum for retrospective compatibility, not reverse execution.',
 'prediction': 'Updates preserve coherent witnesses through composition; the projected false audit sequence is rejected without selecting an origin.',
 'scope': 'Faithful initial possibility set and observations under the bound runtime packet; no truth authentication.'})
subprocess.run([sys.executable, str(N / 'checkers/verify_relational_membership_live_witness.py')], check=True, capture_output=True, text=True)
d = json.loads(p.read_text()); rows = d['lifted_rows']; labels = d['labels']
lookup = {(tuple(r['views']), r['origin']): i for i, r in enumerate(rows)}
fibers = defaultdict(set)
for i, r in enumerate(rows): fibers[tuple(r['views'])].add(i)
relations = {}
for a in range(len(labels)):
 for accepted in (False, True):
  relations[a, accepted] = frozenset((i, lookup[tuple(v), b]) for i, r in enumerate(rows)
                                    for ok, v, b in [r['transitions'][a]] if ok == accepted)
def image(K, relation): return frozenset(j for i, j in relation if i in K)
def transpose(R): return frozenset((j, i) for i, j in R)
def compose(R, S): return frozenset((i, k) for i, j in R for jj, k in S if j == jj)
# Complete reachable knowledge family starting from every possible tuple fiber,
# observing label, acceptance and next tuple, in either logical orientation.
initial = {frozenset(f) for f in fibers.values()}
known = initial | {frozenset()}; todo = deque(initial)
update_checks = 0
while todo:
 K = todo.popleft()
 for R in relations.values():
  for relation in (R, transpose(R)):
   post = image(K, relation)
   parts = defaultdict(set)
   for j in post: parts[tuple(rows[j]['views'])].add(j)
   for part in parts.values():
    nxt = frozenset(part)
    assert len({tuple(rows[j]['views']) for j in nxt}) == 1
    if nxt not in known: known.add(nxt); todo.append(nxt)
   update_checks += 1
assert all(len(K) <= 2 for K in known)
# Exact word composition of witness transport (before view filtering).
composition_checks = 0
for R in relations.values():
 for S in relations.values():
  RS = compose(R, S)
  for K in known:
   assert image(image(K, R), S) == image(K, RS)
   composition_checks += 1
# Include observed middle-view filters explicitly: these preserve witness identity.
filter_checks = 0
for K in known:
 for R in relations.values():
  post = image(K, R)
  split = [post & frozenset(f) for f in fibers.values()]
  assert frozenset().union(*split) == post
  filter_checks += 1
zero = labels.index(['audit-origin', 0]); one = labels.index(['audit-origin', 1])
false_path_checks = 0
for view, f in fibers.items():
 if len(f) != 2: continue
 K = frozenset(f)
 K0 = image(K, relations[zero, True]) & K
 assert len(K0) == 1
 K01 = image(K0, relations[one, True]) & K
 assert not K01
 # Resetting to the full fiber between steps produces the false path.
 assert image(K, relations[one, True]) & K
 false_path_checks += 1
assert false_path_checks == 9
# General exactness proof: image distributes over union; sequential images
# existentially quantify the SAME intermediate packet row. Induct on word length.
assert sha(p) == json.loads(cp.read_text())['packet_sha256']
report = {'passed': True, 'packet_sha256': sha(p), 'behavioral_witness_rows': len(rows),
 'initial_view_fibers': len(initial), 'reachable_knowledge_states_including_empty': len(known),
 'knowledge_size_counts': {str(k): sum(len(K) == k for K in known) for k in range(3)},
 'forward_backward_update_checks': update_checks,
 'all_stratum_pair_image_composition_checks': composition_checks,
 'view_filter_partition_checks': filter_checks,
 'false_projected_audit_paths_rejected': false_path_checks,
 'knowledge_states': [[{'views': rows[i]['views'], 'origin': rows[i]['origin']} for i in sorted(K)]
                      for K in sorted(known, key=lambda x: (len(x), sorted(x)))],
 'theorem': 'Current-set relational transport followed by observed-view restriction is exactly the set of endpoints of coherent lifted paths. Initialization and the image-composition identity prove this for every finite observed execution.',
 'structural_result': 'Unknown actual origin can remain set-valued. Coherence requires preserving correlations across steps, not selecting a unique history.',
 'scope': 'Finite behavioral witness packet; knowledge-state size is not a total storage or authentication bound. Backward transport concerns compatibility only.'}
save(OUT / 'coherent-witness-set-transport.json', report)
print(json.dumps({k: v for k, v in report.items() if k != 'knowledge_states'}, indent=2))
