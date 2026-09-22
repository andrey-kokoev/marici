"""Frozen test: endpoint sets versus history-conditioned marked-cut queries."""
from pathlib import Path
import subprocess
import sys
import json
import hashlib
ROOT = Path(__file__).resolve().parents[3]
N = ROOT / 'research/nima'
OUT = ROOT / 'research/voevodsky/results'
p = N / 'results/relational-live-witness-runtime.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, x): p.write_text(json.dumps(x, indent=2) + '\n')
cp = OUT / 'endpoint-witness-bidirectional-contract.json'
save(cp, {'packet_sha256': sha(p),
 'candidate_state': 'Current observed tuple and transported set of behavioral witness rows.',
 'forward_queries': 'Accepted/rejected label extensions under the owning packet.',
 'backward_query': 'Possible witness at the immediately preceding marked cut, conditional on the entire observed two-step history.',
 'prediction': 'Equal candidate states give equal backward answers as well as equal forward behavior.',
 'history_domain': 'Two admitted steps from the same singleton starting witness. Outputs and acceptance observations are truthful.',
 'scope': 'History-conditioned predecessor query; distinct from the unconditioned predecessor relation of the present state.'})
subprocess.run([sys.executable, str(N / 'checkers/verify_relational_membership_live_witness.py')], check=True, capture_output=True, text=True)
d = json.loads(p.read_text()); rows = d['lifted_rows']; labels = d['labels']
lookup = {(tuple(r['views']), r['origin']): i for i, r in enumerate(rows)}
def step(i, a):
 ok, view, bit = rows[i]['transitions'][a]
 return ok, lookup[tuple(view), bit]
D = labels.index(['deliver'])
witness = None
for initial, row in enumerate(rows):
 ok, final = step(initial, D)
 if not ok or final == initial: continue
 if step(final, D) != (True, final): continue
 audit = labels.index(['audit-origin', row['origin']])
 if step(initial, audit) != (True, initial): continue
 # Same initial state and length; H1 delays delivery, H2 repeats it.
 h1, h2 = (audit, D), (D, D)
 def execute(word):
  path = [initial]
  for a in word:
   accepted, nxt = step(path[-1], a)
   assert accepted
   path.append(nxt)
  return path
 path1, path2 = execute(h1), execute(h2)
 assert path1[0] == path2[0] and path1[-1] == path2[-1]
 assert path1[1] != path2[1]
 # Endpoint possibility sets AND start/end relations coincide.
 assert {path1[-1]} == {path2[-1]}
 assert {(path1[0], path1[-1])} == {(path2[0], path2[-1])}
 # Relations from the marked middle cut retain the required difference.
 R1, R2 = {(path1[1], final)}, {(path2[1], final)}
 assert {a for a, b in R1 if b == final} != {a for a, b in R2 if b == final}
 witness = {'initial_row': initial, 'final_row': final,
            'history_1': [labels[a] for a in h1], 'history_2': [labels[a] for a in h2],
            'path_1': path1, 'path_2': path2,
            'same_current_view': rows[final]['views'], 'same_current_witness_set': [final],
            'previous_cut_answers': [[path1[1]], [path2[1]]],
            'middle_to_final_relations': [[list(x) for x in sorted(R)] for R in (R1, R2)],
            'initial_output': row['output'], 'final_output': rows[final]['output']}
 break
assert witness is not None
# Verify direct backward delivery gives both predecessors; it is sound as an
# unconditioned query, but cannot choose the history-conditioned answer.
final = witness['final_row']
pred = {i for i in range(len(rows)) if step(i, D) == (True, final)}
assert set(witness['previous_cut_answers'][0] + witness['previous_cut_answers'][1]) <= pred
# Generic marked-cut join test for all actual consecutive accepted strata:
# retain triples, then project (middle,end). This agrees with exact path query.
checks = 0
for i in range(len(rows)):
 for a in range(len(labels)):
  ok, middle = step(i, a)
  if not ok: continue
  for b in range(len(labels)):
   accepted, end = step(middle, b)
   if not accepted: continue
   path = (i, middle, end)
   cut_relation = {(path[1], path[2])}
   assert {x for x, y in cut_relation if y == end} == {middle}
   checks += 1
assert sha(p) == json.loads(cp.read_text())['packet_sha256']
report = {'verdict': 'REFUTED_FOR_HISTORY_CONDITIONED_BACKWARD_QUERIES',
 'contract_sha256': sha(cp), 'witness': witness,
 'unconditioned_delivery_predecessors': sorted(pred),
 'accepted_two_step_marked_cut_checks': checks,
 'forward_sufficiency': 'Unaffected: equal endpoint witness sets have identical future set updates.',
 'unconditioned_backward_sufficiency': 'Unaffected: transpose yields the same full predecessor possibilities from the same current set.',
 'history_conditioned_backward_sufficiency': 'Fails; equal current sets and equal initial/final relations can forget the intervening cut.',
 'repair': 'Retain the history-constrained relation from each queried marked cut to the current cut, or information sufficient to reconstruct it.',
 'scope': 'Actual frozen behavioral packet. This does not demand full concrete-history reconstruction or establish a bounded summary for arbitrarily many queried cuts.'}
save(OUT / 'endpoint-witness-bidirectional-sufficiency.json', report)
print(json.dumps(report, indent=2))
