#!/usr/bin/env python3
"""Exact dependency-free constructor scaffold for small integral relation complexes."""
import itertools, json, math
from fractions import Fraction
from functools import reduce
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"integral-complex-constructor-scaffold.v1.json"
RESULT=ASPECT/"results"/"integral_complex_constructor_scaffold.json"
PACKET=ASPECT/"results"/"integral_complex_constructor_fixture_packet.json"
def gcd_all(xs): return reduce(math.gcd,(abs(int(x)) for x in xs),0)
def rank(a):
 m=[[Fraction(x) for x in r] for r in a]; rows=len(m); cols=len(m[0]) if rows else 0; q=0
 for c in range(cols):
  p=next((i for i in range(q,rows) if m[i][c]),None)
  if p is None: continue
  m[q],m[p]=m[p],m[q]; z=m[q][c]; m[q]=[x/z for x in m[q]]
  for i in range(rows):
   if i!=q and m[i][c]:
    z=m[i][c]; m[i]=[m[i][j]-z*m[q][j] for j in range(cols)]
  q+=1
 return q
def det(a):
 n=len(a); m=[[Fraction(x) for x in r] for r in a]; out=Fraction(1)
 for c in range(n):
  p=next((i for i in range(c,n) if m[i][c]),None)
  if p is None:return 0
  if p!=c:m[c],m[p]=m[p],m[c];out=-out
  z=m[c][c];out*=z
  for i in range(c+1,n):
   f=m[i][c]/z
   for j in range(c,n):m[i][j]-=f*m[c][j]
 return int(out)
def maximal_minor_gcd(a):
 r=rank(a)
 if r==0:return 1
 vals=[]
 for rs in itertools.combinations(range(len(a)),r):
  for cs in itertools.combinations(range(len(a[0])),r): vals.append(det([[a[i][j] for j in cs] for i in rs]))
 return gcd_all(vals)
def nullspace(a):
 m=[[Fraction(x) for x in r] for r in a]; rows=len(m); cols=len(m[0]); piv=[]; q=0
 for c in range(cols):
  p=next((i for i in range(q,rows) if m[i][c]),None)
  if p is None:continue
  m[q],m[p]=m[p],m[q]; z=m[q][c];m[q]=[x/z for x in m[q]]
  for i in range(rows):
   if i!=q and m[i][c]:
    z=m[i][c];m[i]=[m[i][j]-z*m[q][j] for j in range(cols)]
  piv.append(c);q+=1
 free=[c for c in range(cols) if c not in piv]; out=[]
 for f in free:
  v=[Fraction(0) for _ in range(cols)];v[f]=1
  for i,p in enumerate(piv):v[p]=-m[i][f]
  l=1
  for x in v:l=math.lcm(l,x.denominator)
  w=[int(x*l) for x in v];g=gcd_all(w);w=[x//g for x in w]
  if next(x for x in w if x)!=abs(next(x for x in w if x)):w=[-x for x in w]
  out.append(w)
 return out
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8")); relations=[[1,1,1]]; transitions=[[[1,0,0],[0,1,0],[0,0,1]]]
 cov=nullspace(relations); sat=maximal_minor_gcd(relations); primes=c["good_primes"]
 reductions={str(p):{"relations":[[x%p for x in r] for r in relations],"covectors":[[x%p for x in v] for v in cov],"transitions":[[[x%p for x in row] for row in t] for t in transitions]} for p in primes}
 checks={"rank":rank(relations)==1,"saturated":sat==1,"annihilator_rank":len(cov)==2,"annihilation":all(sum(v[i]*relations[0][i] for i in range(3))==0 for v in cov),"primitive":all(gcd_all(v)==1 for v in cov),"good_prime_reductions":set(reductions)=={"32003","32009"},"transition_integral":all(isinstance(x,int) for t in transitions for row in t for x in row),"claim_boundary":not any(c["claim_boundary"].values())}
 packet={"schema":"marici.aspect.integral-complex-constructor-packet.v1","status":"synthetic_fixture","free_modules":{"depth3_rank":3},"relation_matrices":{"depth3":relations},"depth_transitions":{"3_to_4":transitions[0]},"saturation_certificates":{"depth3_index":sat},"smith_invariants":{"depth3_determinantal_divisor":sat},"hermite_invariants":{"depth3_rank":rank(relations)},"good_prime_comparisons":reductions,"quotient_covectors":cov,"dual_pairings":{"annihilates_relations":checks["annihilation"]},"source_normalization":{"primitive":checks["primitive"]},"passed":all(checks.values())}
 out={"schema":"marici.aspect.integral-complex-constructor-scaffold-result.v1","passed":all(checks.values()),"checks":checks,"saturation_index":sat,"primitive_covectors":cov,"packet":str(PACKET.relative_to(ROOT)).replace("\\","/"),"promotion_status":"synthetic_not_source_authorized"}
 PACKET.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8"); RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__":main()
