#!/usr/bin/env python3
"""Exact generic-kinematics cyclic invariance of one-loop MHV Kermit sums."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
def det4(cols):return s.det(s.Matrix.hstack(*cols))
def run(n,seed):
 xs=[s.Integer(i*i+(seed+2)*i+1) for i in range(1,n+1)]
 Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)}
 A=s.Matrix([2+seed,3,5,7]);B=s.Matrix([11,13+seed,17,19])
 def br(*q):return det4(q)
 def AB(i,j):return br(A,B,Z[i],Z[j])
 def cyclic(anchor,pos):return ((anchor-1+pos)%n)+1
 def total(anchor):
  value=s.Integer(0)
  for pa in range(1,n-2): # positions a=2,...,n-2 relative to source anchor
   for pb in range(pa+1,n-1): # b<=n-1
    a=cyclic(anchor,pa);ap=cyclic(anchor,pa+1);b=cyclic(anchor,pb);bp=cyclic(anchor,pb+1);o=anchor
    num=br(A,Z[o],Z[a],Z[ap])*br(B,Z[o],Z[b],Z[bp])-br(B,Z[o],Z[a],Z[ap])*br(A,Z[o],Z[b],Z[bp])
    den=AB(o,a)*AB(a,ap)*AB(ap,o)*AB(o,b)*AB(b,bp)*AB(bp,o)
    value += s.cancel(num*num/den)
  return s.factor(value)
 vals=[total(r) for r in range(1,n+1)];base=vals[0];equal=[s.factor(v-base)==0 for v in vals]
 return {'n':n,'seed':seed,'terms_per_anchor':(n-2)*(n-3)//2,'anchors_checked':n,'all_anchors_equal':all(equal),'passed':all(equal)}
rows=[run(n,n+3) for n in range(4,10)]
out={'schema':'marici.nima.one-loop-mhv-kermit-cyclic-invariance.v1','fixtures':'exact rational generic momentum twistors','results':rows,'checks':{'all_cyclic_anchors_equal':all(r['passed'] for r in rows)},'passed':all(r['passed'] for r in rows),'scope':'Exact rational evaluation for every cyclic anchor at n=4,...,9; finite evidence, not by itself an arbitrary-n proof.'}
p=ROOT/'research/nima/results/one-loop-mhv-kermit-cyclic-invariance.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
