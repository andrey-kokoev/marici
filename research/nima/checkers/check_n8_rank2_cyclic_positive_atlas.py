#!/usr/bin/env python3
"""Complete cyclic positive polygon-coordinate atlas for the twenty G_+(2,8) cells."""
from pathlib import Path
import json
import sympy as S
R=Path(__file__).resolve().parents[3];matches=json.loads((R/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches'];bru=json.loads((R/'research/nima/results/n8-positroid-bruhat-boundaries.json').read_text());n=8
facets={c['history_index']:{tuple(x) for x in c['bruhat_facets']} for c in bru['cells']}
def bases(C):return {(i+1,j+1) for i in range(n) for j in range(i+1,n) if S.det(C[:,[i,j]])!=0}
def perm(C):
 B=bases(C);zero={i for i in range(1,n+1) if not any(i in b for b in B)};neck=[]
 for a in range(1,n+1):
  pos=lambda x:(x-a)%n;neck.append(min(B,key=lambda z:sorted(map(pos,z))))
 out=[]
 for z in range(n):
  i=z+1;I=set(neck[z]);J=set(neck[(z+1)%n])
  if i not in I:out.append(i if i in zero else i+n)
  else:
   j=next(iter(J-I));out.append(j if j>i else j+n)
 return tuple(out)
def chart(key,start,vals,zero=None):
 zero_cols=set(key['zero_columns']);groups=[list(g) for g in key['parallel_classes']];pos=lambda x:(x-start)%n;groups.sort(key=lambda g:min(pos(x) for x in g));groups=[sorted(g,key=pos) for g in groups];assert len(groups)>=2
 params=[];C=S.zeros(2,n);idx=0
 # Directions 0<t1<...<t_{m-2}<infinity. GL(2) fixes representatives of the first and last classes.
 dirs=[S.Matrix([1,0])];t=S.Integer(0)
 for gi in range(1,len(groups)-1):
  v=S.Integer(0) if zero==idx else S.Integer(vals[idx]);params.append({'kind':'gap','between_groups':[groups[gi-1],groups[gi]],'value_index':idx});idx+=1;t+=v;dirs.append(S.Matrix([1,t]))
 dirs.append(S.Matrix([0,1]))
 for gi,g in enumerate(groups):
  for qi,label in enumerate(g):
   if qi==0 and gi in (0,len(groups)-1):scale=S.Integer(1)
   else:
    scale=S.Integer(0) if zero==idx else S.Integer(vals[idx]);params.append({'kind':'scale','column':label,'value_index':idx});idx+=1
   sign=-1 if label<start else 1 # k=2 twisted cyclic wrap
   C[:,label-1]=sign*scale*dirs[gi]
 assert idx==8,(key,start,idx,groups);return C,params,groups
pr=[2,3,5,7,11,13,17,19];rows=[]
for m in matches:
 h=m['history_index'];covered=set();charts=[]
 for start in range(1,9):
  nz=sorted((x for g in m['cell_key']['parallel_classes'] for x in g),key=lambda x:(x-start)%n);pos={x:i for i,x in enumerate(nz)}
  if any(max(pos[x] for x in g)-min(pos[x] for x in g)+1!=len(g) for g in m['cell_key']['parallel_classes']):continue
  C,params,groups=chart(m['cell_key'],start,pr);assert perm(C)==tuple(next(c['affine_permutation'] for c in bru['cells'] if c['history_index']==h));assert all(S.det(C[:,[i,j]])>=0 for i in range(n) for j in range(i+1,n)),(h,start,groups,[S.det(C[:,[i,j]]) for i in range(n) for j in range(i+1,n)])
  exposed=[]
  for z,p in enumerate(params):
   Cz,_,_=chart(m['cell_key'],start,pr,z);g=perm(Cz)
   if g in facets[h]:covered.add(g);exposed.append({'coordinate':z+1,**p,'boundary_permutation':list(g)})
  charts.append({'cyclic_start':start,'ordered_parallel_classes':groups,'coordinates':params,'exposed_facets':exposed})
 rows.append({'history_index':h,'seed':m['seed_type'],'facet_count':len(facets[h]),'covered_facet_count':len(covered),'missing_facets':[list(x) for x in sorted(facets[h]-covered)],'charts':charts})
checks={'twenty_cells':len(rows)==20,'all_valid_cyclic_cuts_present':all(len(r['charts'])>=4 for r in rows),'all_charts_have_eight_positive_coordinates':all(len(c['coordinates'])==8 for r in rows for c in r['charts']),'all_166_incidences_exposed':sum(r['covered_facet_count'] for r in rows)==166,'every_bruhat_facet_exposed':all(not r['missing_facets'] for r in rows)};out={'schema':'marici.nima.n8-rank2-cyclic-positive-atlas.v1','cells':rows,'checks':checks,'passed':all(checks.values()),'construction':'For each cyclic cut, nonzero columns are positive scales times cyclically ordered RP1 directions; GL(2) fixes representatives of the first and last classes at 0 and infinity. Intermediate positive direction gaps and column scales are canonical dlog coordinates. The k=2 twisted wrap sign is applied. The k=2 twisted wrap sign is applied.'};p=R/'research/nima/results/n8-rank2-cyclic-positive-atlas.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'coverage':[(r['history_index'],r['covered_facet_count'],r['facet_count']) for r in rows],'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
