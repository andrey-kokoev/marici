"""Canonical anti-invariant cokernel generators and their Abel-Jacobi typing."""
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
PAIRS=ROOT/"research/benincasa/results/four-site-qg-pair-curve-types.json"
TRIPLES=ROOT/"research/benincasa/results/four-site-qg-source-pair-triple-differential.json"
OUT=ROOT/"research/benincasa/results/four-site-qg-kummer-normal-functions.json"

def nullspace(m):
 # Right nullspace over Q.
 if not m:return []
 a=[[Fraction(x) for x in row] for row in m];rows=len(a);cols=len(a[0]);r=0;piv=[]
 for c in range(cols):
  p=next((i for i in range(r,rows) if a[i][c]),None)
  if p is None:continue
  a[r],a[p]=a[p],a[r];q=a[r][c];a[r]=[x/q for x in a[r]]
  for i in range(rows):
   if i!=r and a[i][c]:
    q=a[i][c];a[i]=[x-q*y for x,y in zip(a[i],a[r])]
  piv.append(c);r+=1
 free=[c for c in range(cols) if c not in piv];basis=[]
 for f in free:
  x=[Fraction(0)]*cols;x[f]=1
  for i,p in enumerate(piv):x[p]=-a[i][f]
  basis.append(x)
 return basis

pairs=json.loads(PAIRS.read_text());triples=json.loads(TRIPLES.read_text())
# First six-geometric-mark representative.
chosen=None
for pp,tp in zip(pairs["term_packets"],triples["term_packets"]):
 marks=sorted({tuple(side) for p in pp["pairs"] for side in p["marks"]})
 if len(marks)==6:chosen=(pp,tp,marks);break
pp,tp,marks=chosen;mi={k:i for i,k in enumerate(marks)};display={i:"/".join(k) for k,i in mi.items()}
ptype={}
for p in pp["pairs"]:
 e=tuple(sorted((mi[tuple(p["marks"][0])],mi[tuple(p["marks"][1])])))
 ptype[e]="split" if p["curve_type"].startswith("split") else "elliptic"
split=sorted(e for e,t in ptype.items() if t=="split");spos={e:i for i,e in enumerate(split)}
off=[tuple(x["triple"]) for x in tp["triple_meta"] if x["shared_node_count"]==0]
M=[[0]*len(split) for _ in off]
for ri,t in enumerate(off):
 for face,sgn in zip([(t[1],t[2]),(t[0],t[2]),(t[0],t[1])],[1,-1,1]):
  if face in spos:M[ri][spos[face]]=sgn
# Cokernel dual is ker(M^T).
left=nullspace([list(col) for col in zip(*M)])
assert len(left)==2
def ints(v):
 from math import gcd
 from functools import reduce
 den=1
 for x in v:den=den*x.denominator//gcd(den,x.denominator)
 z=[int(x*den) for x in v];g=reduce(gcd,(abs(x) for x in z if x),0);z=[x//g for x in z]
 if next(x for x in z if x)<0:z=[-x for x in z]
 return z
left=[ints(v) for v in left]
generators=[]
for vec in left:
 terms=[]
 for coeff,t in zip(vec,off):
  if coeff:terms.append({"coefficient":coeff,"triple":[display[i] for i in t],"divisor":"[p_+]-[p_-]"})
 generators.append(terms)

packet={"schema":"marici.benincasa.four_site_qg_kummer_normal_functions.v1","representative_term":pp["term_index"],"ordered_marks":[display[i] for i in range(6)],"split_pair_count":len(split),"off_branch_triple_count":len(off),"anti_incidence_matrix":M,"anti_cokernel_rank":2,"dual_cokernel_generators":generators,"extension_typing":"Each triple row is the degree-zero divisor [p_+]-[p_-] on the relevant elliptic/split pair incidence; its Abel-Jacobi image is nonzero whenever p_+ != p_-.","generic_nontriviality":"Individual off-branch divisors are nonzero in Pic^0 of a smooth elliptic pair; cancellation of the two displayed global combinations remains to be tested by a common Jacobian/normal-function computation."}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps({"term":pp["term_index"],"anti_rank":2,"generator_support_sizes":[len(x) for x in generators]}))
