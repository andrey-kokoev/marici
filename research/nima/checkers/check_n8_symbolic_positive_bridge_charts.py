#!/usr/bin/env python3
"""Promote the found n=8 colored bridge chains to symbolic positive dlog charts."""
from pathlib import Path
import json,itertools,sys
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'));import sympy as s
chains=json.loads((R/'research/nima/results/n8-positive-bridge-chain-search.json').read_text());bru=json.loads((R/'research/nima/results/n8-positroid-bruhat-boundaries.json').read_text());byh={x['history_index']:x for x in bru['cells']};n=8;a=s.symbols('a1:9');vals={x:s.Integer(p) for x,p in zip(a,[2,3,5,7,11,13,17,19])}
def perm(C):
 B={(i+1,j+1) for i in range(n) for j in range(i+1,n) if s.det(C[:,[i,j]])!=0};zero={i for i in range(1,n+1) if not any(i in b for b in B)};neck=[]
 for st in range(1,n+1):
  pos=lambda x:(x-st)%n;neck.append(min(B,key=lambda z:sorted(map(pos,z))))
 out=[]
 for z in range(n):
  i=z+1;I=set(neck[z]);J=set(neck[(z+1)%n])
  if J==I:out.append(i+n if i in I else i)
  else:
   d=J-I;assert i in I and len(d)==1
   j=next(iter(d));out.append(j if j>i else j+n)
 return tuple(out)
def matrix(row,zero=None):
 C=s.zeros(2,n);p,q=[x-1 for x in row['decorated_identity_sources']];C[0,p]=1;C[1,q]=1
 for i,b in enumerate(row['bridge_word']):C[:,b['destination']-1]+=b['sign']*(0 if i==zero else a[i])*C[:,b['source']-1]
 return C
rows=[]
for row in chains['cells']:
 h=row['history_index'];C=matrix(row);target=tuple(byh[h]['affine_permutation']);got=perm(C.subs(vals));mins=[s.expand(s.det(C[:,[i,j]])) for i in range(n) for j in range(i+1,n)];coeff_positive=all(not z or all(q>0 for q in s.Poly(z,*a).coeffs()) for z in mins);piv=next((i,j) for i in range(n) for j in range(i+1,n) if s.det(C[:,[i,j]])!=0);N=C[:,list(piv)].inv()*C;coords=[N[i,j] for i in range(2) for j in range(n) if j not in piv];rank=s.Matrix(coords).jacobian(a).subs(vals).rank();facets=set(map(tuple,byh[h]['bruhat_facets']));exposed=[]
 for z in range(8):
  g=perm(matrix(row,z).subs(vals))
  if g in facets:exposed.append({'coordinate':z+1,'boundary_permutation':list(g)})
 rows.append({'history_index':h,'decorated_identity_sources':row['decorated_identity_sources'],'bridge_word':row['bridge_word'],'generic_permutation':list(got),'positive_minor_coefficients':coeff_positive,'chart_rank':rank,'exposed_facets':exposed});print(h,rank,len(exposed),flush=True)
checks={'twenty_symbolic_charts':len(rows)==20,'all_target_permutations':all(tuple(r['generic_permutation'])==tuple(byh[r['history_index']]['affine_permutation']) for r in rows),'all_minor_coefficients_positive':all(r['positive_minor_coefficients'] for r in rows),'all_charts_rank_eight':all(r['chart_rank']==8 for r in rows),'every_chart_exposes_facets':all(r['exposed_facets'] for r in rows)};out={'schema':'marici.nima.n8-symbolic-positive-bridge-charts.v1','cells':rows,'checks':checks,'passed':all(checks.values()),'construction':'Each alpha is the weight of one positive colored single-column bridge. The ordered form is dlog(alpha1)^...^dlog(alpha8).'};p=R/'research/nima/results/n8-symbolic-positive-bridge-charts.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
