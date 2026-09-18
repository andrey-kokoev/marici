#!/usr/bin/env python3
"""Alternating endpoint-path expansion of the inverse physical kernel."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
src=json.loads((ROOT/'research/nima/results/nnmhv-kernel-wall-tail-boundary.json').read_text());K=s.Matrix([[s.sympify(x) for x in row] for row in src['kernel_matrix']]);K0=s.Matrix([[s.sympify(x) for x in row] for row in src['kernel_without_upper_boundary_transport']]);
def paths(i,j):
 return [p for L in range(1,j-i+1) for mids in itertools.combinations(range(i+1,j),L-1) for p in [(i,)+mids+(j,)]]
def contribution(A,p):
 val=s.Integer(1)/A[p[0],p[0]]
 for a,b in zip(p,p[1:]):val*=A[b,a]/A[b,b]
 return s.factor((-1)**(len(p)-1)*val)
def audit(A):
 records=[];ok=True
 for j in range(3):
  for i in range(j+1):
   if i==j:total=1/A[i,i];terms=[]
   else:terms=[contribution(A,p) for p in paths(i,j)];total=s.factor(sum(terms))
   ok &= s.factor(total-A.inv()[j,i])==0;records.append({'from':i+1,'to':j+1,'terms':[str(x) for x in terms],'sum':str(s.factor(total))})
 return records,ok
r0,o0=audit(K0);r,o=audit(K);long0=next(x for x in r0 if x['from']==1 and x['to']==3);long=next(x for x in r if x['from']==1 and x['to']==3);checks={'path_expansion_exact_without_boundary':o0,'path_expansion_exact_with_boundary':o,'long_range_has_direct_and_mediated_terms':len(long['terms'])==2,'boundary_flips_sum_not_path_parities':s.sign(s.sympify(long0['sum']))==1 and s.sign(s.sympify(long['sum']))==-1}
out={'schema':'marici.nima.nnmhv-inverse-path-sum-bridge.v1','formula':'(K^-1)_(j,i) = sum over increasing paths i=i0<...<il=j of (-1)^l K_(i1,i0)...K_(il,i(l-1)) / [K_(i0,i0)...K_(il,il)]','without_boundary':r0,'with_boundary':r,'checks':{k:bool(v) for k,v in checks.items()},'passed':all(bool(v) for v in checks.values()),'meaning':'Inverse/reflow transport is an exact alternating sum over endpoint paths. Boundary transport changes path magnitudes through diagonal denominators; destructive coherence occurs when the odd direct path overtakes the even mediated path.','bridges':['Neumann/resolvent path expansion','sum over directed histories','parity-signed interference','path cancellation in Green functions','diagonal boundary control of mediated propagation']};p=ROOT/'research/nima/results/nnmhv-inverse-path-sum-bridge.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
