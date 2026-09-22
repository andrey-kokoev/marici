"""Exact three-cut compatibility diagrams for the actual behavioral packet.

Construct path triples by sharing middle witnesses, condition at every cut,
then derive oriented pair relations. No arbitrary Cartesian endpoint join.
"""
from pathlib import Path
from collections import defaultdict
from itertools import product
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
contract = {'packet_sha256': sha(p),
 'domain': 'All initial local-view fibers, all pairs of observed label/admission strata, all resulting observed middle/final view pairs.',
 'constructor': 'Join source-bound transitions on the SAME middle behavioral witness, then restrict all observed cut views.',
 'prediction': 'The two adjacent marked-cut relations reconstruct the complete admitted triple set, and their composition is exactly the endpoint relation. Reversal and all cut queries preserve the conditioned witnesses.',
 'scope': 'Three-cut deterministic behavioral kernel with local per-cut evidence. No nonlocal path constraint is introduced.'}
cp = OUT / 'marked-cut-compatibility-contract.json'; save(cp, contract)
subprocess.run([sys.executable, str(N / 'checkers/verify_relational_membership_live_witness.py')], check=True, capture_output=True, text=True)
d = json.loads(p.read_text()); rows = d['lifted_rows']; labels = d['labels']
lookup = {(tuple(r['views']), r['origin']): i for i, r in enumerate(rows)}
fibers = defaultdict(set)
for i, r in enumerate(rows): fibers[tuple(r['views'])].add(i)
relations = []
for a in range(len(labels)):
 for accepted in (False, True):
  relations.append({(i, lookup[tuple(v), bit]) for i, row in enumerate(rows)
                    for ok, v, bit in [row['transitions'][a]] if ok == accepted})
def transpose(R): return {(j, i) for i, j in R}
def compose(R, S): return {(i, k) for i, j in R for jj, k in S if j == jj}
checks = diagrams = two_witness_diagrams = 0
examples = []
for view, fiber in fibers.items():
 for ai, R in enumerate(relations):
  first = {(i, j) for i, j in R if i in fiber}
  for bi, S in enumerate(relations):
   paths = {(i, j, k) for i, j in first for jj, k in S if j == jj}
   grouped = defaultdict(set)
   for path in paths:
    grouped[tuple(rows[path[1]]['views']), tuple(rows[path[2]]['views'])].add(path)
   for (middle_view, final_view), triples in grouped.items():
    R01 = {(i, j) for i, j, k in triples}
    R12 = {(j, k) for i, j, k in triples}
    R02 = {(i, k) for i, j, k in triples}
    # Lossless join is substantive for this chain of local constraints.
    assert {(i, j, k) for i, j in R01 for jj, k in R12 if j == jj} == triples
    assert compose(R01, R12) == R02
    assert compose(transpose(R12), transpose(R01)) == transpose(R02)
    # Every oriented cut-pair relation is projection of the SAME triple set.
    for a, b in product(range(3), repeat=2):
     Rab = {(t[a], t[b]) for t in triples}
     Rba = {(t[b], t[a]) for t in triples}
     assert transpose(Rab) == Rba
     # Conditioning any one cut on any subset of its possible witnesses.
     possible = sorted({t[a] for t in triples})
     assert len(possible) <= 2
     for mask in range(1 << len(possible)):
      subset = {x for idx, x in enumerate(possible) if mask & (1 << idx)}
      projected = {y for x, y in Rab if x in subset}
      actual = {t[b] for t in triples if t[a] in subset}
      assert projected == actual
      checks += 1
    diagrams += 1
    if len(triples) == 2:
     two_witness_diagrams += 1
     if not examples:
      examples.append({'initial_view': list(view), 'strata': [ai, bi],
                       'middle_view': list(middle_view), 'final_view': list(final_view),
                       'paths': sorted(triples), 'R01': sorted(R01), 'R12': sorted(R12)})
# An empty witness join must remain empty, despite matching projected tuple.
a0 = 2 * labels.index(['audit-origin', 0]) + 1
a1 = 2 * labels.index(['audit-origin', 1]) + 1
assert not compose(relations[a0], relations[a1])
# History counterexample from prior test: retain mark 1, not just endpoints.
wpath = OUT / 'endpoint-witness-bidirectional-sufficiency.json'
w = json.loads(wpath.read_text())['witness']
x, y = tuple(w['path_1']), tuple(w['path_2'])
assert (x[0], x[2]) == (y[0], y[2]) and x[1] != y[1]
assert {(x[1], x[2])} != {(y[1], y[2])}
# Warning: pairwise projections do not reconstruct arbitrary higher-arity data.
parity = {t for t in product((0, 1), repeat=3) if sum(t) % 2 == 0}
P01 = {(i, j) for i, j, k in parity}; P12 = {(j, k) for i, j, k in parity}
assert len({(i, j, k) for i, j in P01 for jj, k in P12 if j == jj}) == 8 > len(parity)
assert sha(p) == contract['packet_sha256']
report = {'passed': True, 'contract_sha256': sha(cp),
 'nonempty_conditioned_three_cut_diagrams': diagrams,
 'two_witness_diagrams': two_witness_diagrams,
 'oriented_conditioning_checks': checks,
 'examples': examples,
 'empty_audit_composition_preserved': True,
 'prior_equal_endpoint_histories_separated_at_marked_cut': True,
 'arbitrary_ternary_relation_negative_control': 'Even parity has four triples but adjacent projections join to eight; locality/factorization is essential.',
 'theorem': 'For the frozen chain-local source kernel, adjacent relations share the actual middle witness and reconstruct exactly the history-conditioned development. Their composites give boundary relations, and transpose reverses orientation coherently.',
 'scope': 'All two-step strata and reachable view fibers. Extension to longer chains follows from the same local path-join definition, not from a claim that arbitrary higher-order constraints factor pairwise.'}
save(OUT / 'marked-cut-compatibility.json', report)
print(json.dumps(report, indent=2))
