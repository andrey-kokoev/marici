#!/usr/bin/env python3
"""Validate the complete 160-chart cyclic colored-BCFW atlas and facet coverage."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'));import sympy as s
chains=json.loads((R/'research/nima/results/n8-cyclic-positive-bridge-chain-search.json').read_text());bru=json.loads((R/'research/nima/results/n8-positroid-bruhat-boundaries.json').read_text());byh={x['history_index']:x for x in bru['cells']};a=s.symbols('a1:9');vals={x:s.Integer(p) for x,p in zip(a,[2,3,5,7,11,13,17,19])};n=8
def perm(C):
 B={(i+1,j+1) for i in range(n) for j in range(i+1,n) if s.det(C[:,[i,j]])!=0};zero={i for i in range(1,n+1) if not any(i in b for b in B)};neck=[]
 for st in range(1,n+1):
  pos=lambda x:(x-st)%n;neck.append(min(B,key=lambda z:sorted(map(pos,z))))
 out=[]
 for z in range(n):
  i=z+1;I=set(neck[z]);J=set(neck[(z+1)%n])
  if J==I:out.append(i+n if i in I else i)
  else:
   d=J-I;assert i in I and len(d)==1;j=next(iter(d));out.append(j if j>i else j+n)
 return tuple(out)
def matrix(row,zero=None):
 D=s.zeros(2,n);p,q=[x-1 for x in row['decorated_identity_sources']];D[0,p]=1;D[1,q]=1
 for i,b in enumerate(row['bridge_word']):D[:,b['destination']-1]+=b['sign']*(0 if i==zero else a[i])*D[:,b['source']-1]
 r=row['cyclic_start']-1;C=s.zeros(2,n)
 for i in range(n):C[:,(i+r)%n]=(-1 if i+r>=n else 1)*D[:,i]
 return C
covered={h:set() for h in byh};rows=[]
for row in chains['charts']:
 h=row['history_index'];C=matrix(row);got=perm(C.subs(vals));target=tuple(byh[h]['affine_permutation']);mins=[s.expand(s.det(C[:,[i,j]])) for i in range(n) for j in range(i+1,n)];positive=all(not z or all(c>0 for c in s.Poly(z,*a).coeffs()) for z in mins);facets=set(map(tuple,byh[h]['bruhat_facets']));ex=[]
 for z in range(8):
  g=perm(matrix(row,z).subs(vals))
  if g in facets:covered[h].add(g);ex.append({'coordinate':z+1,'boundary_permutation':list(g)})
 rows.append({'history_index':h,'cyclic_start':row['cyclic_start'],'decorated_identity_sources':row['decorated_identity_sources'],'bridge_word':row['bridge_word'],'generic_permutation':list(got),'positive_minor_coefficients':positive,'exposed_facets':ex});print(h,row['cyclic_start'],len(ex),flush=True)
checks={'onehundredsixty_symbolic_charts':len(rows)==160,'all_unrotated_targets_match':all(tuple(r['generic_permutation'])==tuple(byh[r['history_index']]['affine_permutation']) for r in rows),'all_charts_manifestly_positive':all(r['positive_minor_coefficients'] for r in rows),'all_166_facet_incidences_exposed':sum(len(x) for x in covered.values())==166,'every_facet_exposed':all(covered[h]==set(map(tuple,byh[h]['bruhat_facets'])) for h in byh)};out={'schema':'marici.nima.n8-complete-cyclic-bcfw-bridge-atlas.v1','charts':rows,'coverage_by_history':{str(h):{'covered':len(covered[h]),'total':len(byh[h]['bruhat_facets'])} for h in byh},'checks':checks,'passed':all(checks.values()),'construction':'Positive colored single-column bridge chains on each cyclic relabeling, symbolically unrotated with the k=2 twisted wrap sign. Coordinates are ordered bridge weights with canonical dlog wedge order.'};p=R/'research/nima/results/n8-complete-cyclic-bcfw-bridge-atlas.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'coverage_by_history':out['coverage_by_history'],'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
