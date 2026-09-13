#!/usr/bin/env python3
"""Exact linear-time encoding and local decoding by movable-cutoff tail observers."""

import json, random
from fractions import Fraction
from pathlib import Path

def encode(u,rho):
 b=[Fraction(0)]*len(u);b[-1]=u[-1]
 for i in range(len(u)-2,-1,-1):b[i]=u[i]+rho[i]*b[i+1]
 return b
def decode(b,rho):return [b[i]-rho[i]*b[i+1] for i in range(len(b)-1)]+[b[-1]]
def direct(u,rho,i):
 z=Fraction(1);s=Fraction(0)
 for j in range(i,len(u)):
  if j>i:z*=rho[j-1]
  s+=z*u[j]
 return s
def main():
 rng=random.Random(20260929);cases=0
 for n in range(1,31):
  for _ in range(20):
   u=[Fraction(rng.randrange(-9,10),rng.randrange(1,10)) for _ in range(n)];rho=[Fraction(rng.randrange(1,10),10) for _ in range(n-1)]
   b=encode(u,rho);assert decode(b,rho)==u and all(b[i]==direct(u,rho,i) for i in range(n));cases+=1
 result={'schema':'marici.coherence.tail-observer-encoder-decoder.v1','cases':cases,'all_exact':True,'encode':'B_i=u_i+rho_i B_(i+1), scanned right-to-left','decode':'u_i=B_i-rho_i B_(i+1)','complexity':'O(n)','decoder_bandwidth':1,'noise_locality':'observer noise at i affects only reconstructed states i and i-1'}
 Path(__file__).with_name('tail-observer-encoder-decoder.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
