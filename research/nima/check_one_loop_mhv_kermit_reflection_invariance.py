#!/usr/bin/env python3
"""Exact generic-kinematics reflection invariance of one-loop MHV Kermit sums."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
def det4(cols):return s.det(s.Matrix.hstack(*cols))
def run(n,seed):
 xs=[s.Integer(i*i+(seed+1)*i+2) for i in range(1,n+1)]
 Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)}
 A=s.Matrix([2+seed,3,5,7]);B=s.Matrix([11,13+seed,17,19])
 def br(*q):return det4(q)
 def AB(i,j):return br(A,B,Z[i],Z[j])
 def total(order):
  o=order[0];value=s.Integer(0)
  for pa in range(1,n-2):
   for pb in range(pa+1,n-1):
    a,ap,b,bp=order[pa],order[pa+1],order[pb],order[pb+1]
    num=br(A,Z[o],Z[a],Z[ap])*br(B,Z[o],Z[b],Z[bp])-br(B,Z[o],Z[a],Z[ap])*br(A,Z[o],Z[b],Z[bp])
    den=AB(o,a)*AB(a,ap)*AB(ap,o)*AB(o,b)*AB(b,bp)*AB(bp,o)
    value += s.cancel(num*num/den)
  return s.factor(value)
 forward=tuple(range(1,n+1));reflected=(1,)+tuple(range(n,1,-1))
 f=total(forward);r=total(reflected);difference=s.factor(r-f)
 return {'n':n,'seed':seed,'terms':(n-2)*(n-3)//2,'reflection_order':list(reflected),'difference':str(difference),'passed':difference==0}
rows=[run(n,n+11) for n in range(4,10)]
out={'schema':'marici.nima.one-loop-mhv-kermit-reflection-invariance.v1','fixtures':'exact rational generic momentum twistors','results':rows,'checks':{'all_reflections_equal':all(r['passed'] for r in rows)},'passed':all(r['passed'] for r in rows),'scope':'Exact rational comparison with reversed cyclic order for n=4,...,9; finite evidence, not by itself an arbitrary-n proof.'}
p=ROOT/'research/nima/results/one-loop-mhv-kermit-reflection-invariance.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
