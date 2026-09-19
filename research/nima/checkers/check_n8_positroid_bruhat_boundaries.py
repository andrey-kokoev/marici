#!/usr/bin/env python3
"""Bounded-affine-permutation Bruhat facets of the 20 matched n=8 positroid cells."""
from pathlib import Path
import json,itertools
ROOT=Path(__file__).resolve().parents[3];matches=json.loads((ROOT/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches'];source=json.loads((ROOT/'research/nima/results/n8-transition-refined-source-boundary.json').read_text());n=8
def bases(key):
 zero=set(key['zero_columns']);cls=[set(g) for g in key['parallel_classes']];par={x:i for i,g in enumerate(cls) for x in g}
 return {(i,j) for i in range(1,n+1) for j in range(i+1,n+1) if i not in zero and j not in zero and par[i]!=par[j]}
def affine_perm(key):
 B=bases(key);neck=[]
 for start in range(1,n+1):
  order=[(start+t-1)%n+1 for t in range(n)];pos={x:i for i,x in enumerate(order)};neck.append(min(B,key=lambda z:sorted(pos[x] for x in z)))
 f=[];zero=set(key['zero_columns'])
 for idx in range(n):
  i=idx+1;I=set(neck[idx]);J=set(neck[(idx+1)%n])
  if i not in I:f.append(i if i in zero else i+n)
  else:
   add=list(J-I);assert len(add)==1,(i,I,J);j=add[0];f.append(j if j>i else j+n)
 return tuple(f)
def length(f):
 def F(j):
  q,r=divmod(j-1,n);return f[r]+q*n
 return sum(F(i)>F(j) for i in range(1,n+1) for j in range(i+1,i+n+1))
def covers(f):
 L=length(f);out=set()
 for i in range(n):
  for j in range(i+1,n):
   for q in (-1,0,1):
    g=list(f);g[i]=f[j]+q*n;g[j]=f[i]-q*n
    if all(k+1<=g[k]<=k+1+n for k in range(n)) and len({x%n for x in g})==n and length(tuple(g))==L+1:out.add(tuple(g))
 return out
# Coordinate rank-seven boundaries are identified by their history/alpha records; derive their coarse keys from the legacy complete census.
legacy=json.loads((ROOT/'research/nima/results/n8-full-history-boundary-cancellation.json').read_text());# external file lacks every record, so regenerate keys from its shared/external records is impossible; use transition pair boundary permutations plus external support only after a separate matrix pass.
rows=[]
for m in matches:
 f=affine_perm(m['cell_key']);cs=covers(f);rows.append({'history_index':m['history_index'],'seed':m['seed_type'],'affine_permutation':list(f),'affine_length':length(f),'cell_dimension':2*(n-2)-length(f),'bruhat_facet_count':len(cs),'bruhat_facets':[list(x) for x in sorted(cs)]})
checks={'twenty_cells':len(rows)==20,'all_cells_dimension_eight':all(r['cell_dimension']==8 for r in rows),'every_cell_has_facets':all(r['bruhat_facet_count']>0 for r in rows),'affine_permutations_distinct':len({tuple(r['affine_permutation']) for r in rows})==20}
out={'schema':'marici.nima.n8-positroid-bruhat-boundaries.v1','cells':rows,'total_cell_facet_incidences':sum(r['bruhat_facet_count'] for r in rows),'distinct_bruhat_facets':len({tuple(x) for r in rows for x in r['bruhat_facets']}),'checks':checks,'passed':all(checks.values()),'claim_boundary':'Facet enumeration uses bounded affine permutations reconstructed from rank-two bases and swaps increasing affine inversion length by one. Coordinate-chart coverage comparison remains separate.'};p=ROOT/'research/nima/results/n8-positroid-bruhat-boundaries.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='cells'},indent=2));raise SystemExit(0 if out['passed'] else 1)
