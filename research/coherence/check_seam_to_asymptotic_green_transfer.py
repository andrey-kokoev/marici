#!/usr/bin/env python3
"""Exact covariance and invertibility of seam-to-asymptotic Green transfer."""

import json, random
from fractions import Fraction
from pathlib import Path

def transfer(y,j0,j1):return (-(j0+j1)/(2*y),y*(j0-j1)/2)
def main():
 rng=random.Random(20260915);rows=[]
 for _ in range(100):
  y=Fraction(rng.randrange(1,10),rng.randrange(1,10));z=Fraction(rng.randrange(1,10),rng.randrange(1,10));j0=Fraction(rng.randrange(-9,10),rng.randrange(1,10));j1=Fraction(rng.randrange(-9,10),rng.randrange(1,10))
  qm,qp=transfer(y,j0,j1)
  assert transfer(y*z,j0,j1)==(qm/z,z*qp)
  assert transfer(1/y,-j0,j1)==(qp,qm)
  rows.append({'y':str(y),'translation_scale':str(z),'covariant':True})
 result={'schema':'marici.coherence.seam-to-asymptotic-green-transfer.v1','cases':len(rows),'all_exact':True,'matrix':'[[-1/(2y),-1/(2y)],[y/2,-y/2]]','determinant':'1/2','translation_covariance':'y -> zy induces (q_minus,q_plus) -> (z^-1 q_minus,z q_plus)','reflection_covariance':'(y,J0,J1) -> (y^-1,-J0,J1) induces charge swap'}
 Path(__file__).with_name('seam-to-asymptotic-green-transfer.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
