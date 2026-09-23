"""Exact representation-or-storage-obstruction for every frozen query subfamily.

Queries and their independent primal/Farkas validity come from Nima's owning
packet. The constructor selects the query dependency mask before checking
behavioral equivalence. This is a restricted-family theorem, not a universal
termination claim for arbitrary source presentations.
"""
from pathlib import Path
from itertools import combinations
import subprocess
import sys
import json
import hashlib
ROOT = Path(__file__).resolve().parents[3]
N = ROOT / 'research/nima'
OUT = ROOT / 'research/voevodsky/results'
pp = N / 'results/certified-forgetting-storage-obstruction-packet.json'
cp0 = N / 'results/certified-forgetting-storage-obstruction-contract.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, x): p.write_text(json.dumps(x, indent=2) + '\n')
owner = json.loads(cp0.read_text()); coords=owner['finite_test']['probe_coordinates']; n=len(coords)
cp=OUT/'representation-or-obstruction-contract.json'
save(cp, {'packet_sha256':sha(pp),'owning_contract_sha256':sha(cp0),
 'source':'Owning source/tail zero-frame family, same source state and objective certificate.',
 'languages':'Every subset of the ten declared feasibility probe coordinates.',
 'budgets':'Every integer bit budget from zero through ten; all history-dependent information counted.',
 'constructor':'Retain zero-frame membership on queried coordinates. If required bits exceed budget, return an independently separable Boolean family on budget+1 queried coordinates.',
 'prediction':'Sufficient exact representation or checked storage obstruction for every frozen language/budget pair.',
 'scope':'Zero frames and fixed read-only feasibility probes only; no arbitrary linear frames or actual prime adapter.'})
subprocess.run([sys.executable,str(N/'checkers/verify_certified_forgetting_storage_obstruction.py')],check=True,capture_output=True,text=True)
p=json.loads(pp.read_text()); histories=p['histories']
assert len(histories)==2**n
by_mask={h['mask']:h for h in histories}
for h in histories:
 assert h['mask']==sum(1<<i for i,c in enumerate(coords) if c in h['zero_slots'])

def encode(mask,indices): return sum(((mask>>i)&1)<<j for j,i in enumerate(indices))
def embed(code,indices): return sum(((code>>j)&1)<<i for j,i in enumerate(indices))
def answers(code,width): return tuple(not ((code>>j)&1) for j in range(width))

representations=obstructions=answer_checks=separator_checks=0
summary={h:{'query_families':0,'representable_cases':0,'obstructed_cases':0} for h in range(n+1)}
examples={}
for query_mask in range(2**n):
 indices=tuple(i for i in range(n) if query_mask&(1<<i)); h=len(indices)
 summary[h]['query_families']+=1
 signatures={}; encodings=set()
 for history in histories:
  code=encode(history['mask'],indices)
  actual=tuple(history['future_feasibility'][i] for i in indices)
  assert answers(code,h)==actual
  assert code not in signatures or signatures[code]==actual
  signatures[code]=actual;encodings.add(code);answer_checks+=1
 assert len(encodings)==len(set(signatures.values()))==2**h
 for budget in range(n+1):
  if h<=budget:
   representations+=1;summary[h]['representable_cases']+=1
   assert max(encodings)<2**budget or (budget==0 and encodings=={0})
  else:
   obstructions+=1;summary[h]['obstructed_cases']+=1
   witness_indices=indices[:budget+1]
   # This full subcube has 2^(budget+1)>2^budget source-admitted refinements.
   witnesses=[embed(code,witness_indices) for code in range(2**(budget+1))]
   assert len(set(witnesses))>2**budget
   assert all(mask in by_mask for mask in witnesses)
   # Pairwise separator formula is exact: a nonzero xor has a set bit.
   # Check each nonzero difference once; translation covers every pair.
   for difference in range(1,2**(budget+1)):
    j=(difference&-difference).bit_length()-1
    coordinate=witness_indices[j]
    assert by_mask[0]['future_feasibility'][coordinate] != by_mask[embed(difference,witness_indices)]['future_feasibility'][coordinate]
    separator_checks+=1
   if (h,budget)==(10,8):
    examples['ten_queries_eight_bits']={'verdict':'STORAGE_OBSTRUCTION',
      'witness_coordinates':[coords[i] for i in witness_indices],
      'distinguishable_witnesses':len(witnesses),'available_codes':2**budget,
      'separator':'For two different subcube masks, query a coordinate of their xor.'}
assert representations+obstructions==2**n*(n+1)
# Canonical presentations agree under coordinate reordering and restriction.
# This proves projection coherence without making lost bits recoverable.
projection_checks=0
for mask in range(2**n):
 for history in histories[:1]+histories[-1:]:
  indices=tuple(i for i in range(n) if mask&(1<<i))
  code=encode(history['mask'],indices)
  assert embed(code,indices)==history['mask']&mask
  projection_checks+=1
assert sha(pp)==json.loads(cp.read_text())['packet_sha256']
report={'passed':True,'contract_sha256':sha(cp),'query_subfamilies':2**n,
 'language_budget_cases':representations+obstructions,'representations':representations,
 'storage_obstructions':obstructions,'exact_history_query_signature_checks':answer_checks,
 'separating_difference_checks':separator_checks,'projection_regressions':projection_checks,
 'horizon_summary':summary,'examples':examples,
 'theorem':'For any H queried coordinates in this owning zero-frame family, continuation equivalence is exactly equality of the H membership bits. H bits are sufficient and necessary; restricting a language projects its mask, and arbitrary H rules out a uniform finite bound.',
 'proof':'Owning feasible-spike and Farkas certificates establish query answers. A membership mask realizes all answers. The 2^H source-admitted subsets are separated by an xor coordinate, proving the lower bound independently of encoding.',
 'scope':'Exact restricted source/query family. No general algorithm deciding finite representability of arbitrary finitely presented systems.'}
save(OUT/'representation-or-obstruction.json',report)
print(json.dumps({k:v for k,v in report.items() if k!='horizon_summary'},indent=2))
