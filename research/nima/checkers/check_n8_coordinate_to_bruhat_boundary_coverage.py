#!/usr/bin/env python3
"""Match n=8 alpha-zero chart limits to invariant Bruhat facets."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
bru=json.loads((ROOT/'research/nima/results/n8-positroid-bruhat-boundaries.json').read_text());matches=json.loads((ROOT/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches'];a=s.symbols('a1:9');A1,A2,A3,A4,A5,A6,A7,A8=a
M={'F':s.Matrix([[1,A1+A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,1,A5,A6,A7,A8]]),'G':s.Matrix([[1,A1,A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'H':s.Matrix([[1,A1,A2+A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'A':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'B':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'C':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'D':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]]),'E':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]])};vals={x:s.Integer(p) for x,p in zip(a,[2,3,5,7,11,13,17,19])};n=8
def embed(q,X):
 e=q['embedding'];sup=list(range(1,9)) if isinstance(e,int) else e['support'];rot=e if isinstance(e,int) else e['rotation'];O=s.zeros(2,8)
 for j in range(X.cols):O[:,sup[(j+rot)%len(sup)]-1]=(-1 if j+rot>=len(sup) else 1)*X[:,j]
 return O
def key(X):
 cols=[X[:,j] for j in range(n)];zero=[j+1 for j,c in enumerate(cols) if c==s.zeros(2,1)];left=[j for j in range(n) if j+1 not in zero];groups=[]
 while left:
  i=left.pop(0);g=[i+1];rest=[]
  for j in left:
   if s.det(s.Matrix.hstack(cols[i],cols[j]))==0:g.append(j+1)
   else:rest.append(j)
  left=rest;groups.append(g)
 return {'parallel_classes':groups,'zero_columns':zero}
def bases(k):
 zero=set(k['zero_columns']);par={x:i for i,g in enumerate(k['parallel_classes']) for x in g};return {(i,j) for i in range(1,n+1) for j in range(i+1,n+1) if i not in zero and j not in zero and par[i]!=par[j]}
def perm(k):
 B=bases(k);neck=[]
 for st in range(1,n+1):
  order=[(st+t-1)%n+1 for t in range(n)];pos={x:i for i,x in enumerate(order)};neck.append(min(B,key=lambda z:sorted(pos[x] for x in z)))
 f=[];zero=set(k['zero_columns'])
 for z in range(n):
  i=z+1;I=set(neck[z]);J=set(neck[(z+1)%n])
  if i not in I:f.append(i if i in zero else i+n)
  else:
   j=next(iter(J-I));f.append(j if j>i else j+n)
 return tuple(f)
facets={c['history_index']:{tuple(x) for x in c['bruhat_facets']} for c in bru['cells']};visible=[];nonfacets=[]
for q in matches:
 C=embed(q,M[q['seed_type']])
 for e,x in enumerate(a,1):
  p=perm(key(C.subs(vals|{x:0})));row={'history_index':q['history_index'],'seed':q['seed_type'],'alpha':e,'boundary_permutation':list(p)}
  if p in facets[q['history_index']]:visible.append(row)
  else:nonfacets.append(row)
visby={h:{tuple(r['boundary_permutation']) for r in visible if r['history_index']==h} for h in range(20)};missing=[]
for c in bru['cells']:
 for f in facets[c['history_index']]-visby[c['history_index']]:missing.append({'history_index':c['history_index'],'seed':c['seed'],'boundary_permutation':list(f)})
checks={'onehundredseven_coordinate_visible_facets':len(visible)==107,'fiftythree_coordinate_degenerations':len(nonfacets)==53,'all_visible_limits_distinct_within_chart':all(len(visby[h])==sum(r['history_index']==h for r in visible) for h in range(20)),'fiftynine_missing_facet_incidences':len(missing)==59,'incidence_completion_166':len(visible)+len(missing)==bru['total_cell_facet_incidences']}
out={'schema':'marici.nima.n8-coordinate-to-bruhat-boundary-coverage.v1','visible_facet_incidences':visible,'coordinate_degenerations':nonfacets,'missing_facet_incidences':missing,'coverage_by_history':{str(h):{'visible':len(visby[h]),'total':len(facets[h]),'missing':len(facets[h]-visby[h])} for h in range(20)},'checks':checks,'passed':all(checks.values()),'conclusion':'The eight alpha-zero limits expose exactly 107 of 166 Bruhat facet incidences. The remaining 59 invariant incidences require alternate positive charts or correlated boundary limits.'};p=ROOT/'research/nima/results/n8-coordinate-to-bruhat-boundary-coverage.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'coverage_by_history':out['coverage_by_history'],'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
