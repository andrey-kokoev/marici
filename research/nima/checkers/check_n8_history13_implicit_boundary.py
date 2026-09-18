#!/usr/bin/env python3
"""Implicitize the rank-seven history-13 G/alpha4 pushforward hypersurface."""
from pathlib import Path
import json,sys,itertools
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
q={x['history_index']:x for x in json.loads((ROOT/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches']}[13]
a=s.symbols('a1:9');A1,A2,A3,A4,A5,A6,A7,A8=a
G=s.Matrix([[1,A1,A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]).subs(A4,0)
def embed(mat):
 emb=q['embedding'];sup=emb['support'];rot=emb['rotation'];out=s.zeros(2,8)
 for j in range(mat.cols):out[:,sup[(j+rot)%len(sup)]-1]=mat[:,j]
 return out
Z=s.Matrix([[s.Integer(t)**k for k in range(6)] for t in range(1,9)]);Y=s.simplify(embed(G)*Z);free=[x for x in a if x!=A4]
piv=None
trial={x:s.Integer(p) for x,p in zip(a,[2,3,5,7,11,13,17,19])}
for i in range(6):
 for j in range(i+1,6):
  if s.det(Y[:,[i,j]]).subs(trial)!=0:piv=(i,j);break
 if piv:break
N=s.simplify(Y[:,list(piv)].inv()*Y);coords=[s.factor(N[i,j]) for i in range(2) for j in range(6) if j not in piv];x=s.symbols('x1:9')
# Monomials of total degree <=2 in affine target coordinates.
mons2=[s.Integer(1)]+list(x)+[x[i]*x[j] for i in range(8) for j in range(i,8)]
mons3=mons2+[x[i]*x[j]*x[k] for i in range(8) for j in range(i,8) for k in range(j,8)];samples=[]
import random
rng=random.Random(1729)
for seed in range(180):
 sub={v:s.Integer(rng.randrange(1,18)) for v in free};cv=[s.cancel(z.subs(sub)) for z in coords];row=[s.Integer(1)]+cv+[cv[i]*cv[j] for i in range(8) for j in range(i,8)]+[cv[i]*cv[j]*cv[k] for i in range(8) for j in range(i,8) for k in range(j,8)];samples.append(row)
prime=1000003
def modq(v):
 v=s.Rational(v);return (int(v.p)%prime)*pow(int(v.q)%prime,-1,prime)%prime
def rank_mod(mat):
 A=[[modq(v) for v in row] for row in mat];r=0
 for c in range(len(A[0])):
  p=next((i for i in range(r,len(A)) if A[i][c]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];inv=pow(A[r][c],-1,prime);A[r]=[(v*inv)%prime for v in A[r]]
  for i in range(len(A)):
   if i!=r and A[i][c]:
    f=A[i][c];A[i]=[(u-f*v)%prime for u,v in zip(A[i],A[r])]
  r+=1
  if r==len(A):break
 return r
rmod2=rank_mod([row[:len(mons2)] for row in samples]);rmod3=rank_mod(samples)
checks={'history13_seed_G':q['seed_type']=='G','source_dimension_seven':len(free)==7,'target_chart_dimension_eight':len(coords)==8,'degree_le_2_evaluation_has_full_column_rank':rmod2==len(mons2),'degree_le_3_evaluation_has_full_column_rank':rmod3==len(mons3)}
out={'schema':'marici.nima.n8-history13-implicit-boundary.v3','history_index':13,'seed':'G','source_boundary':'alpha4=0','target_pivot_columns':[i+1 for i in piv],'sample_count':len(samples),'finite_field_prime':prime,'degree_le_2':{'monomials':len(mons2),'rank':rmod2,'nullity':len(mons2)-rmod2},'degree_le_3':{'monomials':len(mons3),'rank':rmod3,'nullity':len(mons3)-rmod3},'checks':checks,'passed':all(checks.values()),'conclusion':'No nonzero rational polynomial of total degree at most three vanishes identically on the image. Any implicit hypersurface equation has degree at least four in this chart.','proof_strength':'Full modular column rank gives a nonzero rational evaluation minor, so the degree-at-least-four bound is exact.','claim_boundary':'The statement is for fixed exact moment-curve external data and the chosen affine target chart. Cubic reconstruction and covariantization remain separate.'};p=ROOT/'research/nima/results/n8-history13-implicit-boundary.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
