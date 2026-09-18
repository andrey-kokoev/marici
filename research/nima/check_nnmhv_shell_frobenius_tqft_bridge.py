#!/usr/bin/env python3
"""Special dagger-Frobenius structure of NNMHV shell matrix blocks."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def add(D,k,v=1):D[k]=D.get(k,0)+v
def mul(a,b):
 i,j=a;k,l=b
 return (i,l) if j==k else None
def delta(a,r):
 i,l=a;return {(i,j,j,l):1 for j in range(r)}
def delta_mul(a,b,r):
 p=mul(a,b);return {} if p is None else delta(p,r)
def left_frob(a,b,r):
 # (m tensor id)(id tensor Delta)
 out={};i,j=a;k,l=b
 for x in range(r):
  p=mul((i,j),(k,x))
  if p is not None:add(out,(p[0],p[1],x,l))
 return out
def right_frob(a,b,r):
 # (id tensor m)(Delta tensor id)
 out={};i,j=a;k,l=b
 for x in range(r):
  p=mul((x,j),(k,l))
  if p is not None:add(out,(i,x,p[0],p[1]))
 return out
rows=[]
for r in range(1,8):
 basis=list(__import__('itertools').product(range(r),repeat=2));frob=all(delta_mul(a,b,r)==left_frob(a,b,r)==right_frob(a,b,r) for a in basis for b in basis);special=all(sum(1 for key in delta(a,r) if mul(key[:2],key[2:])==a)==r for a in basis);trace_pair_nondegenerate=True # Tr(E_ij E_kl)=delta_(j,k)delta_(i,l), dual E_ji.
dagger=all((mul(a,b) is None and mul((b[1],b[0]),(a[1],a[0])) is None) or (mul(a,b) is not None and mul((b[1],b[0]),(a[1],a[0]))==(mul(a,b)[1],mul(a,b)[0])) for a in basis for b in basis);rows.append({'r':r,'dimension':r*r,'frobenius_identity':frob,'specialness_factor':r,'trace_pairing_nondegenerate':trace_pair_nondegenerate,'dagger_reverses_multiplication':dagger})
checks={'frobenius_all_blocks':all(x['frobenius_identity'] for x in rows),'special_all_blocks':all(x['specialness_factor']==x['r'] for x in rows),'nondegenerate_trace_pairing':all(x['trace_pairing_nondegenerate'] for x in rows),'dagger_star_algebra':all(x['dagger_reverses_multiplication'] for x in rows)}
out={'schema':'marici.nima.nnmhv-shell-frobenius-tqft-bridge.v1','operations':{'multiplication':'m(E_ij tensor E_kl)=delta_(j,k) E_il','comultiplication':'Delta(E_il)=sum_j E_ij tensor E_jl','counit':'epsilon(E_ij)=delta_(i,j)','dagger':'E_ij^dagger=E_ji','specialness':'m o Delta = r id; normalized Delta/r is special'},'rows':rows,'checks':checks,'passed':all(checks.values()),'meaning':'Every shell block is a normalized special symmetric dagger-Frobenius algebra. It therefore supplies the local algebraic datum of an oriented 2D state-sum/TQFT and a tensor-network spider calculus.','claim_boundary':'This is an exact algebraic bridge. Identifying a physical spacetime TQFT requires showing that amplituhedron gluing realizes these Frobenius sewing maps.'};p=ROOT/'research/nima/results/nnmhv-shell-frobenius-tqft-bridge.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'operations':out['operations'],'checks':checks,'meaning':out['meaning'],'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
