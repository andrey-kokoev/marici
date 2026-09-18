#!/usr/bin/env python3
"""Generic exact rank of Phi_Z on the transition-refined n=8 source boundary."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
ext=json.loads((ROOT/'research/nima/results/n8-transition-refined-source-boundary.json').read_text())['external_chain_support'];matches={x['history_index']:x for x in json.loads((ROOT/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches']}
a=s.symbols('a1:9');A1,A2,A3,A4,A5,A6,A7,A8=a
M={'F':s.Matrix([[1,A1+A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,1,A5,A6,A7,A8]]),'G':s.Matrix([[1,A1,A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'H':s.Matrix([[1,A1,A2+A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'A':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'B':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'C':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'D':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]]),'E':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]])}
def embed(q,mat):
 emb=q['embedding'];sup=list(range(1,9)) if isinstance(emb,int) else emb['support'];rot=emb if isinstance(emb,int) else emb['rotation'];out=s.zeros(2,8)
 for j in range(mat.cols):out[:,sup[(j+rot)%len(sup)]-1]=(-1 if j+rot>=len(sup) else 1)*mat[:,j]
 return out
# Positive external data on the moment curve.
Z=s.Matrix([[s.Integer(t)**k for k in range(6)] for t in range(1,9)]);vals={x:s.Integer(p) for x,p in zip(a,[2,3,5,7,11,13,17,19])};vals2={x:s.Integer(p) for x,p in zip(a,[3,5,7,11,13,17,19,23])}
edges=[(i,(i+1)%8) for i in range(8)];edgepairs=[(u,v) for q,u in enumerate(edges) for v in edges[q+1:] if len(set(u+v))==4];standard={tuple(sorted(u+v)) for u,v in edgepairs};quadruples=list(__import__('itertools').combinations(range(8),4));rows=[]
for r in ext:
 q=matches[r['history_index']];e=r['alpha'];free=[x for i,x in enumerate(a,1) if i!=e];C=embed(q,M[q['seed_type']]).subs(a[e-1],0);Y=s.simplify(C*Z)
 piv=None
 for i in range(6):
  for j in range(i+1,6):
   if s.det(Y[:,[i,j]]).subs(vals)!=0:piv=(i,j);break
  if piv:break
 N=s.simplify(Y[:,list(piv)].inv()*Y);coords=[N[i,j] for i in range(2) for j in range(6) if j not in piv];J=s.Matrix(coords).jacobian(free).subs(vals);rank=J.rank();labels=[]
 if rank==7:
  Y1=Y.subs(vals);Y2=Y.subs(vals2)
  for quad in quadruples:
   fixed=tuple(Z[i,:] for i in quad)
   if s.det(s.Matrix.vstack(Y1,*fixed))==0 and s.det(s.Matrix.vstack(Y2,*fixed))==0:labels.append([i+1 for i in quad])
 rows.append({'history_index':r['history_index'],'seed':r['seed'],'alpha':e,'source_coefficient':r['coefficient'],'source_grassmannian_rank':r['source_grassmannian_rank'],'pushforward_rank':rank,'contracted':rank<7,'target_boundary_brackets':labels,'standard_boundary_brackets':[z for z in labels if tuple(i-1 for i in z) in standard],'nonstandard_boundary_brackets':[z for z in labels if tuple(i-1 for i in z) not in standard]})
contract=[r for r in rows if r['contracted']];checks={'all_61_tested':len(rows)==61,'rank_never_exceeds_source_rank':all(r['pushforward_rank']<=r['source_grassmannian_rank'] for r in rows),'classification_complete':len(rows)==len(contract)+sum(not r['contracted'] for r in rows)}
out={'schema':'marici.nima.n8-external-boundary-pushforward-rank.v2','external_source_branches':len(rows),'generically_noncontracted_branches':sum(not r['contracted'] for r in rows),'contracted_branches':len(contract),'rank_distribution':{str(k):sum(r['pushforward_rank']==k for r in rows) for k in sorted({r['pushforward_rank'] for r in rows})},'contracted_details':contract,'rank7_details':[r for r in rows if not r['contracted']],'all_bracket_label_distribution':{str(k):sum(tuple(z)==k for r in rows for z in r['target_boundary_brackets']) for k in sorted({tuple(z) for r in rows for z in r['target_boundary_brackets']})},'standard_labelled_rank7_branches':sum(bool(r['standard_boundary_brackets']) for r in rows if not r['contracted']),'nonstandard_only_rank7_branches':sum(bool(r['nonstandard_boundary_brackets']) and not r['standard_boundary_brackets'] for r in rows if not r['contracted']),'unlabelled_rank7_branches':[r for r in rows if not r['contracted'] and not r['target_boundary_brackets']],'multiply_labelled_rank7_branches':[r for r in rows if not r['contracted'] and len(r['target_boundary_brackets'])>1],'checks':checks,'passed':all(checks.values()),'interpretation':'Rank seven means the source facet maps generically to a target codimension-one locus. Lower rank means Phi_Z contracts at least one additional source direction. Rank alone does not identify the target boundary equation or prove nonzero residue.'};p=ROOT/'research/nima/results/n8-external-boundary-pushforward-rank.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
