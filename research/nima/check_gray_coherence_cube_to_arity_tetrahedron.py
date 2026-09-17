#!/usr/bin/env python3
"""Check the coherence-cube resolution of the arity tetrahedron."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def lift(x,y,z):
 lo=max(Fraction(0),x+y-1);hi=min(x,y);t=lo+z*(hi-lo)
 lam=(1-x-y+t,y-t,t,x-t)
 return t,lam
vals=[Fraction(i,8) for i in range(9)];bad=[];samples=[]
for x in vals:
 for y in vals:
  for z in vals:
   t,lam=lift(x,y,z)
   if sum(lam)!=1 or any(a<0 for a in lam):bad.append((x,y,z,lam))
for x,y in [(Fraction(0),Fraction(0)),(0,1),(1,0),(1,1),(Fraction(1,2),Fraction(1,2))]:
 for z in (Fraction(0),Fraction(1)):
  t,lam=lift(Fraction(x),Fraction(y),z);samples.append({'x':str(x),'y':str(y),'coherence_bit':str(z),'t':str(t),'lambda':[str(a) for a in lam]})
gray=[(0,0,0),(0,0,1),(0,1,1),(0,1,0),(1,1,0),(1,1,1),(1,0,1),(1,0,0)]
def hamming(a,b):return sum(x!=y for x,y in zip(a,b))
checks={'cube_gray_cycle_changes_one_bit':all(hamming(gray[i],gray[(i+1)%8])==1 for i in range(8)),'cube_maps_into_tetrahedron':not bad,'coherence_fiber_collapses_at_four_arity_vertices':all(lift(Fraction(x),Fraction(y),0)[0]==lift(Fraction(x),Fraction(y),1)[0] for x,y in ((0,0),(0,1),(1,0),(1,1))),'center_fiber_has_two_diagonal_endpoints':lift(Fraction(1,2),Fraction(1,2),0)[1]==(0,Fraction(1,2),0,Fraction(1,2)) and lift(Fraction(1,2),Fraction(1,2),1)[1]==(Fraction(1,2),0,Fraction(1,2),0)}
out={'schema':'marici.nima.gray-coherence-cube-to-arity-tetrahedron.v1','gray_cycle':[list(v) for v in gray],'map':'t=max(0,x+y-1)+z*(min(x,y)-max(0,x+y-1)); lambda=(1-x-y+t,y-t,t,x-t)','samples':samples,'checks':checks,'passed':all(checks.values()),'interpretation':'x=input arity, y=output arity, z=interchange polarization/order. The tetrahedron is the quotient image obtained by collapsing z where the factorization interval degenerates.'}
p=ROOT/'research/nima/results/gray-coherence-cube-to-arity-tetrahedron.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
