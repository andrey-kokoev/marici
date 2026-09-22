"""Frozen finite source counterexample to pairwise witnessed gluing.

Source: binary triples of even parity, specified independently of restrictions.
Pieces: all two-coordinate restrictions. Overlap witnesses: literal equality
on common coordinates. Each piece is source-realizable; one compatible family
has no common source lift. Full relation is retained for negative control.
"""
from pathlib import Path
from itertools import product, combinations
import json
ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'research/voevodsky/results'
def save(p, x): p.write_text(json.dumps(x, indent=2) + '\n')
contract = {'source': 'S={(x0,x1,x2) in {0,1}^3 : x0+x1+x2=0 mod 2}',
 'cover': [[0,1],[1,2],[0,2]],
 'local_admission': 'A piece is in the restriction image of S.',
 'overlap_witness': 'Equality of coordinate values on intersections; identity comparisons, hence strict cocycle coherence.',
 'prediction': 'Every locally admitted family with coherent pairwise overlap witnesses lifts to S.',
 'scope': 'Independent finite synthesis fixture motivated by the prior parity control; not a claim about an unconstructed extension of the actual coupled source.'}
save(OUT / 'coherent-gluing-obstruction-contract.json', contract)
S = {x for x in product((0,1), repeat=3) if sum(x)%2 == 0}
cover = ((0,1),(1,2),(0,2))
def restriction(x, U): return tuple(x[i] for i in U)
local = [{restriction(x, U) for x in S} for U in cover]
assert all(len(L)==4 for L in local)
def compatible(family):
 for i,j in combinations(range(3),2):
  di,dj = dict(zip(cover[i],family[i])),dict(zip(cover[j],family[j]))
  if any(di[k] != dj[k] for k in set(di)&set(dj)): return False
 return True
matches=[]; failures=[]
for family in product(*(sorted(L) for L in local)):
 if not compatible(family): continue
 fiber = {x for x in S if all(restriction(x,U)==piece for U,piece in zip(cover,family))}
 record = {'pieces': [list(t) for t in family], 'global_fiber': [list(x) for x in sorted(fiber)]}
 matches.append(record)
 if not fiber: failures.append(record)
assert len(matches)==8 and len(failures)==4
family = ((1,1),(1,1),(1,1))
assert compatible(family)
local_lifts = [[list(x) for x in sorted(S) if restriction(x,U)==v] for U,v in zip(cover,family)]
assert local_lifts == [[[1,1,0]],[[0,1,1]],[[1,0,1]]]
# Pairwise overlap observations are all 1. Their equality witnesses compose
# strictly (all are identity on the shared value), so no comparison choice
# or nonzero loop defect explains the failure.
assert all(set(dict(zip(U,v)).values())=={1} for U,v in zip(cover,family))
forced = tuple(dict(zip(cover[0],family[0]))[i] if i in cover[0] else family[1][1] for i in range(3))
assert forced==(1,1,1) and forced not in S
# Even and odd parity sources have identical restriction images on every
# proper coordinate subset: all lower-arity observation data agree.
odd = set(product((0,1),repeat=3))-S
proper_checks=0
for size in range(3):
 for U in combinations(range(3),size):
  assert {restriction(x,U) for x in S} == {restriction(x,U) for x in odd}
  proper_checks+=1
# Restoring the declared ternary factor recovers exactly the source.
completed = {tuple(v) for v in product((0,1),repeat=3)}
assert {x for x in completed if sum(x)%2==0} == S
# Reversal preserves this obstruction: parity is invariant under coordinate reversal.
assert {x[::-1] for x in S} == S and forced[::-1] not in S
report = {'verdict':'REFUTED_FOR_PAIRWISE_EQUALITY_OVERLAPS',
 'source_states': [list(x) for x in sorted(S)],
 'locally_admitted_families': 64, 'overlap_compatible_families': len(matches),
 'globally_realizable_families':len(matches)-len(failures),
 'nonrealizable_compatible_families':failures,
 'explicit_family':[list(x) for x in family], 'individual_source_lifts':local_lifts,
 'forced_global_assignment':list(forced), 'overlap_witnesses':'Strict coordinate identities; all overlap compositions agree.',
 'identical_proper_restriction_images_even_vs_odd':proper_checks,
 'reversal_preserves_obstruction':True,
 'structural_obstruction':'The source has a genuine ternary constraint invisible in every proper coordinate restriction. Coherence of retained overlap comparisons does not imply completeness of the retained constraints.',
 'scope':contract['scope']}
save(OUT / 'coherent-gluing-obstruction.json', report)
print(json.dumps(report,indent=2))
