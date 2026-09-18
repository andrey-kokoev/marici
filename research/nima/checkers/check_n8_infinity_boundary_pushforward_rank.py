#!/usr/bin/env python3
"""Exact target census for all 160 alpha=infinity boundaries of the 20 n=8 charts."""
from pathlib import Path
import json,sys,itertools
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
matches=json.loads((ROOT/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches'];a=s.symbols('a1:9');A1,A2,A3,A4,A5,A6,A7,A8=a
M={'F':s.Matrix([[1,A1+A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,1,A5,A6,A7,A8]]),'G':s.Matrix([[1,A1,A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'H':s.Matrix([[1,A1,A2+A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'A':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'B':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'C':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'D':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]]),'E':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]])}
def embed(q,mat):
 emb=q['embedding'];sup=list(range(1,9)) if isinstance(emb,int) else emb['support'];rot=emb if isinstance(emb,int) else emb['rotation'];out=s.zeros(2,8)
 for j in range(mat.cols):out[:,sup[(j+rot)%len(sup)]-1]=mat[:,j]
 return out
def infinity_chart(Y,x,trial):
 minors={}
 for i in range(6):
  for j in range(i+1,6):
   f=s.Poly(s.expand(s.det(Y[:,[i,j]])),x);minors[(i,j)]=f
 d=max(f.degree() for f in minors.values() if not f.is_zero);piv=next(k for k,f in minors.items() if f.degree()==d and f.LC().subs(trial)!=0);den=minors[piv].LC();p,q=piv;N=s.zeros(2,6);N[0,p]=1;N[1,q]=1
 for j in range(6):
  if j in piv:continue
  f0=s.Poly(s.expand(s.det(Y[:,[j,q]])),x);f1=s.Poly(s.expand(s.det(Y[:,[p,j]])),x)
  N[0,j]=0 if f0.is_zero or f0.degree()<d else s.cancel(f0.LC()/den);N[1,j]=0 if f1.is_zero or f1.degree()<d else s.cancel(f1.LC()/den)
 return N,piv,d
Z=s.Matrix([[s.Integer(t)**k for k in range(6)] for t in range(1,9)]);vals={x:s.Integer(p) for x,p in zip(a,[2,3,5,7,11,13,17,19])};vals2={x:s.Integer(p) for x,p in zip(a,[3,5,7,11,13,17,19,23])};quads=list(itertools.combinations(range(8),4));edges=[(i,(i+1)%8) for i in range(8)];standard={tuple(sorted(u+v)) for n,u in enumerate(edges) for v in edges[n+1:] if len(set(u+v))==4};rows=[]
for q in matches:
 C=embed(q,M[q['seed_type']]);Y=C*Z
 for e,x in enumerate(a,1):
  free=[v for v in a if v!=x];N,piv,d=infinity_chart(Y,x,vals);coords=[N[i,j] for i in range(2) for j in range(6) if j not in piv];rank=s.Matrix(coords).jacobian(free).subs(vals).rank();labels=[]
  if rank==7:
   N1=N.subs(vals);N2=N.subs(vals2)
   for quad in quads:
    fixed=tuple(Z[i,:] for i in quad)
    if s.det(s.Matrix.vstack(N1,*fixed))==0 and s.det(s.Matrix.vstack(N2,*fixed))==0:labels.append([i+1 for i in quad])
  rows.append({'history_index':q['history_index'],'seed':q['seed_type'],'alpha':e,'boundary':'infinity','leading_plucker_degree':d,'target_pivot_columns':[piv[0]+1,piv[1]+1],'pushforward_rank':rank,'contracted':rank<7,'target_boundary_brackets':labels,'standard_boundary_brackets':[z for z in labels if tuple(i-1 for i in z) in standard],'nonstandard_boundary_brackets':[z for z in labels if tuple(i-1 for i in z) not in standard]})
checks={'all_160_infinity_branches_tested':len(rows)==160,'rank_never_exceeds_seven':all(r['pushforward_rank']<=7 for r in rows),'every_rank7_has_at_most_one_bracket_label':all(len(r['target_boundary_brackets'])<=1 for r in rows if r['pushforward_rank']==7)}
out={'schema':'marici.nima.n8-infinity-boundary-pushforward-rank.v1','branches':len(rows),'rank_distribution':{str(k):sum(r['pushforward_rank']==k for r in rows) for k in sorted({r['pushforward_rank'] for r in rows})},'rank7_branches':sum(r['pushforward_rank']==7 for r in rows),'contracted_branches':sum(r['pushforward_rank']<7 for r in rows),'standard_labelled_rank7':sum(r['pushforward_rank']==7 and bool(r['standard_boundary_brackets']) for r in rows),'nonstandard_labelled_rank7':sum(r['pushforward_rank']==7 and bool(r['nonstandard_boundary_brackets']) for r in rows),'unlabelled_rank7':sum(r['pushforward_rank']==7 and not r['target_boundary_brackets'] for r in rows),'details':rows,'checks':checks,'passed':all(checks.values()),'interpretation':'Infinity residues carry the negative of the corresponding zero-residue dlog sign. This file classifies target limits only; source-branch matching is separate.'};p=ROOT/'research/nima/results/n8-infinity-boundary-pushforward-rank.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='details'},indent=2));raise SystemExit(0 if out['passed'] else 1)
