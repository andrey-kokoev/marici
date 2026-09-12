#!/usr/bin/env python3
"""Separate reciprocal conjugacy from literal fixed-point equality."""

import json
from fractions import Fraction
from pathlib import Path

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def main():
 R=[[Fraction(0),Fraction(1)],[Fraction(1),Fraction(0)]];I=[[Fraction(1),0],[0,Fraction(1)]];rows=[]
 for z in [Fraction(n,d) for n in range(1,9) for d in range(1,9)]:
  T=[[z,0],[0,1/z]];Ti=[[1/z,0],[0,z]]
  conjugate=mm(R,mm(T,R))==Ti
  literal=T==Ti
  fixed=z*z==1
  assert conjugate and literal==fixed
  rows.append({'z':str(z),'reciprocal_conjugate':conjugate,'literal_fixed':literal})
 result={'schema':'marici.coherence.reciprocal-fixed-locus-vs-orbit.v1','cases':len(rows),'all_reciprocals_conjugate':True,'literal_equality_iff_z_squared_one':True,'positive_fixed_locus':'z=1','conclusion':'an unframed observer identifies reciprocal orbit mates for every z; detecting the fixed locus requires retained orientation/frame data and literal or framed equivalence'}
 Path(__file__).with_name('reciprocal-fixed-locus-vs-orbit.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
