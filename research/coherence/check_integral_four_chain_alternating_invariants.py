#!/usr/bin/env python3
"""Compute integral alternating elementary divisors for four-point chains."""

import json, math
from pathlib import Path

def gcd_all(xs):
 g=0
 for x in xs:g=math.gcd(g,abs(x))
 return g
def invariants(x,y,z):
 entries=[x,x*y,x*y*z,y,y*z,z]
 d1=gcd_all(entries);pf=x*z;assert d1 and pf%d1==0
 return d1,abs(pf)//d1,entries

def main():
 cases=[]
 for gaps in ((2,3,4),(2,3,5),(4,6,10),(6,10,15),(3,9,12)):
  d1,d2,e=invariants(*gaps);assert d2%d1==0
  cases.append({'gaps':gaps,'upper_entries':e,'alternating_elementary_divisors':[d1,d2],'adjacent_block_weights':[gaps[0],gaps[2]],'same_prescribed_weights':sorted([d1,d2])==sorted([gaps[0],gaps[2]])})
 result={'schema':'marici.coherence.integral-four-chain-alternating-invariants.v1','cases':cases,'formula':['d1=gcd(x,y,z)','d2=abs(xz)/d1'],'pfaffian':'xz=d1*d2','conclusion':'integral normal blocks redistribute prime factors across adjacent weights; localized adjacent blocks retain different framed data'}
 Path(__file__).with_name('integral-four-chain-alternating-invariants.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
