#!/usr/bin/env python3
"""Exact local five-cube kernel and shell-residue factorization."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/local_five_cube_blind_class_is_a_rank_one_residue_polynomial.md'
RESULT=ROOT/'research/voevodsky/results/local_five_cube_residue_factorization.json'
SETTINGS=(F(1),F(5,6),F(3,4),F(7,10),F(2,3))

def rref(a):
 a=[row[:] for row in a];pivots=[];r=0
 for c in range(len(a[0]) if a else 0):
  p=next((i for i in range(r,len(a)) if a[i][c]),None)
  if p is None:continue
  a[r],a[p]=a[p],a[r];q=a[r][c];a[r]=[x/q for x in a[r]]
  for i in range(len(a)):
   if i!=r and a[i][c]:
    q=a[i][c];a[i]=[x-q*y for x,y in zip(a[i],a[r])]
  pivots.append(c);r+=1
  if r==len(a):break
 return a,pivots

def nullvector(a):
 reduced,pivots=rref(a);free=[c for c in range(len(a[0])) if c not in pivots]
 if len(free)!=1:return None,len(free)
 x=[F(0)]*len(a[0]);x[free[0]]=F(1)
 for row,pivot in reversed(list(zip(reduced,pivots))):x[pivot]=-sum(row[c]*x[c] for c in free)
 return x,1

def cube_edges():
 ratios=((3,2),(5,3),(7,5),(11,7),(13,11));base=2310;vertices={}
 for mask in range(32):
  value=base
  for i,(q,p) in enumerate(ratios):
   if mask>>i&1:value=value*q//p
  vertices[mask]=value
 edges=[]
 for mask in range(32):
  for direction in range(5):
   if not(mask>>direction&1):edges.append((mask,mask|1<<direction,direction+1,vertices[mask],vertices[mask|1<<direction]))
 return vertices,edges

def matrix(edges,settings):
 rows=[]
 for t in settings:
  for vertex in range(32):
   row=[F(0)]*len(edges)
   for c,(source,target,shell,_,_) in enumerate(edges):
    if source==vertex:row[c]-=t**shell
    if target==vertex:row[c]+=t**shell
   rows.append(row)
 return rows

def mul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out

def fs(x):return f'{x.numerator}/{x.denominator}'

vertices,edges=cube_edges();ranks=[]
for m in range(1,6):
 _,pivots=rref(matrix(edges,SETTINGS[:m]));ranks.append(len(pivots))
probe4=matrix(edges,SETTINGS[:4]);x,nullity=nullvector(probe4)
q=[F(1)]
for root in (F(0),)+SETTINGS[:4]:q=mul(q,[-root,F(1)])
residue=[[F(0)]*32 for _ in range(6)]
for coefficient,(source,target,shell,_,_) in zip(x,edges):
 residue[shell][source]-=coefficient;residue[shell][target]+=coefficient
anchor=next(j for j in range(1,6) if q[j]);v=[entry/q[anchor] for entry in residue[anchor]]
factorization=all(residue[j][i]==q[j]*v[i] for j in range(1,6) for i in range(32))
fifth_values=[sum(residue[j][i]*SETTINGS[4]**j for j in range(1,6)) for i in range(32)]
final_index=next(c for c,e in enumerate(edges) if e[3]==12705 and e[4]==15015)
without_final=edges[:final_index]+edges[final_index+1:]
_,without_pivots=rref(matrix(without_final,SETTINGS[:4]))
checks={
 'cube_32_vertices':len(vertices)==32,
 'cube_80_edges':len(edges)==80,
 'ranks_are_31_57_73_79_80':ranks==[31,57,73,79,80],
 'four_evaluation_nullity_one':nullity==1,
 'residue_polynomial_rank_one':factorization,
 'residue_vector_nonzero':any(v),
 'fifth_setting_detects':any(fifth_values),
 'deleting_final_edge_restores_four_probe_faithfulness':len(without_pivots)==len(without_final),
 'route_is_cycle_at_coarse_setting':all(sum(residue[j][i] for j in range(1,6))==0 for i in range(32)),
}
text=PACKET.read_text(encoding='utf-8');checks['claim_boundary_retained']='does not identify' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.local-five-cube-residue-factorization.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'settings':[fs(t) for t in SETTINGS],'ranks':ranks,'nullities':[80-r for r in ranks],'kernel_support_edges':sum(c!=0 for c in x),'residue_polynomial_coefficients':[fs(c) for c in q],'residue_vertex_support':sum(c!=0 for c in v),'fifth_evaluation_nonzero_vertices':sum(c!=0 for c in fifth_values),'final_edge_column':final_index,'checks':checks,'passed':all(checks.values()),'disposition':{'established':'unique four-evaluation blind class on local five-cube has R_x(z)=q(z)v','residual':'construct comparison from this rank-one residue to an augmentation-graded cubical class'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'ranks':ranks,'kernel_support_edges':result['kernel_support_edges'],'residue_vertex_support':result['residue_vertex_support'],'q':result['residue_polynomial_coefficients']}));raise SystemExit(0 if result['passed'] else 1)
