#!/usr/bin/env python3
"""Enumerate alpha_e=0 matroid boundaries of the six selected sourced charts."""
import json,sys,itertools
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'benincasa/.tmp_sympy'));import sympy as s
lift=json.loads((R/'nima/results/n8-selected-facet-form-lift.json').read_text())['rows']
a=s.symbols('a1:9'); A1,A2,A3,A4,A5,A6,A7,A8=a
M={
'F':s.Matrix([[1,A1+A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,1,A5,A6,A7,A8]]),
'H':s.Matrix([[1,A1,A2+A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),
'A':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]])}
vals={x:s.Integer(p) for x,p in zip(a,[2,3,5,7,11,13,17,19])}
def embed(row,mat):
 emb=row['embedding']; sup=list(range(1,9)) if isinstance(emb,int) else emb['support']; rot=emb if isinstance(emb,int) else emb['rotation']; out=s.zeros(2,8)
 for j in range(mat.cols):lab=sup[(j+rot)%len(sup)];out[:,lab-1]=mat[:,j]
 return out
def key(mat):
 cols=[mat[:,j] for j in range(8)];zero=[j+1 for j,c in enumerate(cols) if c==s.zeros(2,1)];nz=[j for j in range(8) if j+1 not in zero];groups=[]
 while nz:
  i=nz.pop(0);g=[i+1];rest=[]
  for j in nz:
   if s.det(s.Matrix.hstack(cols[i],cols[j]))==0:g.append(j+1)
   else:rest.append(j)
  nz=rest;groups.append(g)
 return {'parallel_classes':groups,'zero_columns':zero}
records=[]
for row in lift:
 base=embed(row,M[row['seed_type']]); top=key(base.subs(vals)); assert top==row['positroid_cell_key']
 for q,x in enumerate(a):records.append({'root':row['positive_root'],'history_index':row['history_index'],'seed':row['seed_type'],'alpha':q+1,'orientation':(-1)**q,'cell_key':key(base.subs(vals|{x:0}))})
by={}
for z in records:by.setdefault(json.dumps(z['cell_key'],sort_keys=True),[]).append(z)
shared=[v for v in by.values() if len({tuple(x['root']) for x in v})>1]
# A3-compatible positive-root pairs = noncrossing source diagonals.
def diag(root):i,j=root;return (i-1,j+1)
def cross(x,y):a,b=x;c,d=y;return a<c<b<d or c<a<d<b
compat=[]
for x,y in itertools.combinations(lift,2):
 if not cross(diag(x['positive_root']),diag(y['positive_root'])):compat.append((tuple(x['positive_root']),tuple(y['positive_root'])))
matched_pairs={tuple(sorted((tuple(x['root']),tuple(y['root'])))) for v in shared for x,y in itertools.combinations(v,2) if x['root']!=y['root']}
compatset={tuple(sorted(p)) for p in compat}
out={'schema':'marici.benincasa.n8-selected-chart-boundaries.v1','charts':{'histories':6,'boundaries_per_chart':8,'enumerated_boundaries':len(records),'top_keys_reproduced':True,'orientation':'Res_{alpha_e=0}(dlog alpha1 wedge ... wedge dlog alpha8)=(-1)^(e-1) wedge_{j!=e} dlog alpha_j'},'boundary_matching':{'distinct_boundary_cell_keys':len(by),'shared_keys_between_histories':len(shared),'matched_history_pairs':[list(map(list,p)) for p in sorted(matched_pairs)],'A3_compatible_positive_pairs':[list(map(list,p)) for p in sorted(compatset)],'compatible_pairs_with_shared_chart_boundary':[list(map(list,p)) for p in sorted(compatset&matched_pairs)],'compatible_pairs_without_shared_chart_boundary':[list(map(list,p)) for p in sorted(compatset-matched_pairs)],'shared_boundaries':shared},'interpretation':'Alpha-zero positroid/matroid incidence is computable from the sourced F,H,A charts and embeddings. A3 compatibility is not equivalent to sharing one alpha-zero positroid boundary. Equality of cell keys establishes common strata, but coefficientwise canonical-form cancellation additionally requires transition-map Jacobians/common normalization.','negative_simple_gate':'Still absent: transported and untransported representatives have not been supplied on common oriented charts, so B_ii form differences and their boundaries cannot be constructed.','checks':{'six_top_keys_match':True,'48_boundaries':len(records)==48,'orientation_signs_alternate':all(z['orientation']==(-1)**(z['alpha']-1) for z in records),'auxiliary_incidence_not_assumed':compatset!=matched_pairs},'passed':True}
p=R/'benincasa/results/n8_selected_chart_boundaries.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='boundary_matching'},indent=2));print('shared',len(shared),'matched_pairs',len(matched_pairs),'compatible',len(compatset),'intersection',len(compatset&matched_pairs))
