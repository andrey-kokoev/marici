#!/usr/bin/env python3
"""Compile certified n=7 parity-simplex complements to rank-2 positroids."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];src=json.loads((ROOT/'research/nima/results/seven-point-history-parity-cell-matching.json').read_text());n=7
def compile_cell(simplex):
 omitted=tuple(i for i in range(1,n+1) if i not in simplex);parent={i:i for i in range(1,n+1)}
 def find(a):
  while parent[a]!=a:parent[a]=parent[parent[a]];a=parent[a]
  return a
 def union(a,b):
  a,b=find(a),find(b)
  if a!=b:parent[b]=a
 for i in omitted:union(i,1 if i==n else i+1)
 def basis(a,b):return find(a)!=find(b)
 necklace=[]
 for start in range(1,n+1):
  order=[(start+j-1)%n+1 for j in range(n)];B=next(pair for pair in itertools.combinations(order,2) if basis(*pair));necklace.append(B)
 perm=[]
 for i in range(1,n+1):
  A=set(necklace[i-1]);B=set(necklace[i%n]);added=list(B-A);removed=list(A-B)
  if removed!=[i] or len(added)!=1:raise ValueError((i,A,B))
  j=added[0]
  while j<=i:j+=n
  perm.append(j)
 return omitted,necklace,tuple(perm)
rows=[]
for m in sorted(src['matches'],key=lambda x:x['history_index']):
 omitted,N,p=compile_cell(m['simplex']);rows.append({'history_index':m['history_index'],'simplex':m['simplex'],'vanishing_cyclic_minors':[f'Delta_({i},{1 if i==n else i+1})' for i in omitted],'grassmann_necklace':[list(x) for x in N],'bounded_affine_permutation':list(p),'dimension':8})
checks={'six_cells':len(rows)==6,'all_codimension_two':all(len(r['vanishing_cyclic_minors'])==2 and r['dimension']==8 for r in rows),'permutations_bounded':all(all(i<=v<=i+n for i,v in enumerate(r['bounded_affine_permutation'],1)) for r in rows),'permutations_have_k_two':all(sum(v-i for i,v in enumerate(r['bounded_affine_permutation'],1))==2*n for r in rows),'cells_distinct':len({tuple(r['bounded_affine_permutation']) for r in rows})==6}
out={'schema':'marici.nima.seven-point-positroid-compiler.v1','convention':'An omitted parity-simplex label i is the cyclic positroid boundary Delta_(i,i+1)=0, indices modulo n.','cells':rows,'checks':checks,'passed':all(checks.values()),'scope':'Certified n=7 history/simplex matching plus standard rank-2 cyclic-boundary positroid compilation.'};p=ROOT/'research/nima/results/seven-point-positroid-compiler.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
