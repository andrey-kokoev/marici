#!/usr/bin/env python3
"""Exact rational checks of the probe-induced Hankel and Clifford structure."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/probe_induced_hankel_metric_and_clifford_algebra.md'
RESULT=ROOT/'research/voevodsky/results/probe_induced_clifford_algebra.json'
T4=(F(1),F(5,6),F(3,4),F(7,10));S=F(2,3);N=5

def rank(a):
 a=[r[:] for r in a];out=0
 for c in range(len(a[0])):
  p=next((i for i in range(out,len(a)) if a[i][c]),None)
  if p is None:continue
  a[out],a[p]=a[p],a[out];q=a[out][c];a[out]=[x/q for x in a[out]]
  for i in range(out+1,len(a)):
   if a[i][c]:
    q=a[i][c];a[i]=[x-q*y for x,y in zip(a[i],a[out])]
  out+=1
 return out
def det(a):
 a=[r[:] for r in a];d=F(1)
 for c in range(len(a)):
  p=next((i for i in range(c,len(a)) if a[i][c]),None)
  if p is None:return F(0)
  if p!=c:a[c],a[p]=a[p],a[c];d=-d
  q=a[c][c];d*=q
  for i in range(c+1,len(a)):
   f=a[i][c]/q
   for j in range(c,len(a)):a[i][j]-=f*a[c][j]
 return d
def transpose(a):return [list(x) for x in zip(*a)]
def mmul(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in transpose(b)] for row in a]
def mv(a,x):return [sum(y*z for y,z in zip(row,x)) for row in a]
def poly_mul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def add_state(out,mask,value):
 out[mask]=out.get(mask,F(0))+value
 if out[mask]==0:del out[mask]
def eps(i,mask):
 if mask>>i&1:return None
 return mask|1<<i, F(-1 if (mask&((1<<i)-1)).bit_count()%2 else 1)
def iota(i,mask):
 if not(mask>>i&1):return None
 return mask&~(1<<i), F(-1 if (mask&((1<<i)-1)).bit_count()%2 else 1)
def c_action(i,state,q):
 out={}
 for mask,coefficient in state.items():
  a=eps(i,mask)
  if a:add_state(out,a[0],coefficient*a[1])
  for j in range(N):
   a=iota(j,mask)
   if a:add_state(out,a[0],coefficient*q[i][j]*a[1])
 return out
def linear_c(coefficients,state,q):
 out={}
 for i,a in enumerate(coefficients):
  for mask,value in c_action(i,state,q).items():add_state(out,mask,a*value)
 return out

def evaluation(settings):return [[t**i for i in range(1,N+1)] for t in settings]
m4=evaluation(T4);m5=evaluation(T4+(S,));q4=mmul(transpose(m4),m4);q5=mmul(transpose(m5),m5);vs=[S**i for i in range(1,N+1)]
update=[[vs[i]*vs[j] for j in range(N)] for i in range(N)]
poly=[F(1)]
for root in (F(0),)+T4:poly=poly_mul(poly,[-root,F(1)])
radical=poly[1:]
checks={
 'hankel_entries':all(q4[i][j]==sum(t**(i+j+2) for t in T4) for i in range(N) for j in range(N)),
 'gram_rank_four':rank(q4)==4,
 'evaluation_rank_four':rank(m4)==4,
 'radical_generator_killed_by_evaluation':mv(m4,radical)==[0]*4,
 'radical_generator_killed_by_gram':mv(q4,radical)==[0]*N,
 'rank_one_update':all(q5[i][j]-q4[i][j]==update[i][j] for i in range(N) for j in range(N)),
 'fifth_gram_full_rank':rank(q5)==5,
 'determinant_square':det(q5)==det(m5)**2,
 'fifth_setting_detects_radical':sum(a*b for a,b in zip(vs,radical))!=0,
}
clifford_ok=True
for i in range(N):
 for j in range(N):
  for mask in range(1<<N):
   state={mask:F(1)};left=c_action(i,c_action(j,state,q4),q4)
   for target,value in c_action(j,c_action(i,state,q4),q4).items():add_state(left,target,value)
   expected={} if q4[i][j]==0 else {mask:2*q4[i][j]}
   if left!=expected:clifford_ok=False;break
checks['all_clifford_anticommutators']=clifford_ok
radical_square=True
for mask in range(1<<N):
 state={mask:F(1)}
 if linear_c(radical,linear_c(radical,state,q4),q4):radical_square=False;break
checks['radical_clifford_generator_square_zero']=radical_square
text=PACKET.read_text(encoding='utf-8');checks['apparatus_conditioning_retained']='apparatus-conditioned geometry' in text;checks={k:bool(v) for k,v in checks.items()}
def fs(x):return f'{x.numerator}/{x.denominator}'
result={'schema':'marici.voevodsky.probe-induced-clifford-algebra.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'settings_four':[fs(x) for x in T4],'fifth_setting':fs(S),'gram_four_rank':rank(q4),'gram_five_rank':rank(q5),'gram_five_determinant':fs(det(q5)),'evaluation_five_determinant':fs(det(m5)),'radical_generator':[fs(x) for x in radical],'fifth_pairing':fs(sum(a*b for a,b in zip(vs,radical))),'checks':checks,'passed':all(checks.values()),'disposition':{'established':'probe-induced Hankel form and exact Clifford action on the Boolean exterior space','residual':'no intrinsic apparatus-independent metric on prime indices established'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'ranks':[rank(q4),rank(q5)],'det_q5':result['gram_five_determinant'],'fifth_pairing':result['fifth_pairing']}));raise SystemExit(0 if result['passed'] else 1)
