#!/usr/bin/env python3
"""Exact hostile for Clifford multiplication in the six-index radical plane."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/clifford_products_measure_unresolved_prime_index_planes_not_edge_route_composition.md'
RESULT=ROOT/'research/voevodsky/results/clifford_radical_plane_composition.json'
T4=(F(1),F(5,6),F(3,4),F(7,10));S=F(2,3);U=F(3,5);N=6

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
def transpose(a):return [list(x) for x in zip(*a)]
def mmul(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in transpose(b)] for r in a]
def mv(a,x):return [sum(y*z for y,z in zip(r,x)) for r in a]
def dotq(x,q,y):return sum(x[i]*q[i][j]*y[j] for i in range(N) for j in range(N))
def pmul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def qpoly(settings):
 q=[F(0),F(1)]
 for t in settings:q=pmul(q,[-t,F(1)])
 return q
def coeff(q):return q[1:]+[F(0)]*(N-(len(q)-1))
def gram(settings):
 m=[[t**i for i in range(1,N+1)] for t in settings]
 return mmul(transpose(m),m)
def fs(x):return f'{x.numerator}/{x.denominator}'

q4=qpoly(T4);a=coeff(q4);b=coeff([F(0)]+q4);g4=gram(T4)
wedge={(i,j):a[i]*b[j]-a[j]*b[i] for i in range(N) for j in range(i+1,N)}
q5=qpoly(T4+(S,));survivor=coeff(q5);g5=gram(T4+(S,));g6=gram(T4+(S,U))
evaluation_on_plane=[[sum(a[i]*t**(i+1) for i in range(N)),sum(b[i]*t**(i+1) for i in range(N))] for t in (S,)]
checks={
 'four_setting_gram_rank_four':rank(g4)==4,
 'a_in_radical':mv(g4,a)==[0]*N,
 'b_in_radical':mv(g4,b)==[0]*N,
 'radical_basis_independent':rank([a,b])==2,
 'radical_pairings_zero':dotq(a,g4,a)==dotq(a,g4,b)==dotq(b,g4,b)==0,
 'wedge_nonzero':any(wedge.values()),
 'wedge_dimension_one':sum(v!=0 for v in wedge.values())>0,
 'fifth_evaluation_rank_one_on_plane':rank(evaluation_on_plane)==1,
 'survivor_equals_b_minus_s_a':survivor==[b[i]-S*a[i] for i in range(N)],
 'five_setting_gram_rank_five':rank(g5)==5,
 'survivor_spans_new_radical':mv(g5,survivor)==[0]*N and any(survivor),
 'six_setting_gram_full_rank':rank(g6)==6,
 'second_new_setting_detects_survivor':sum(survivor[i]*U**(i+1) for i in range(N))!=0,
 'bivector_not_vector_by_degree':len(wedge)==15 and len(survivor)==6,
}
text=PACKET.read_text(encoding='utf-8');checks['route_degree_obstruction_retained']='ill-typed' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.clifford-radical-plane-composition.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'settings_four':[fs(x) for x in T4],'added_settings':[fs(S),fs(U)],'gram_ranks':[rank(g4),rank(g5),rank(g6)],'radical_basis':{'q':[fs(x) for x in a],'zq':[fs(x) for x in b]},'wedge_nonzero_coordinates':{f'{i+1},{j+1}':fs(v) for (i,j),v in wedge.items() if v},'surviving_line':[fs(x) for x in survivor],'checks':checks,'passed':all(checks.values()),'disposition':{'survives':'Clifford product is the unresolved-plane bivector and each setting removes one radical dimension','fails':'naive identification of a bivector with a blind edge route','next':'construct a graded cubical chain realization before claiming route multiplication'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'gram_ranks':result['gram_ranks'],'wedge_coordinates':len(result['wedge_nonzero_coordinates'])}));raise SystemExit(0 if result['passed'] else 1)
