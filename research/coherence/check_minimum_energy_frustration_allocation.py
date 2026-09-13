#!/usr/bin/env python3
"""Exact minimum-energy gauge fixing for block frustration allocation."""
import json, random
from fractions import Fraction
from pathlib import Path

def energy(a,b,wp,wf):return sum(p*x*x+q*y*y for x,y,p,q in zip(a,b,wp,wf))
def allocate(w,wp,wf):
 a=[q*x/(p+q) for x,p,q in zip(w,wp,wf)];b=[-p*x/(p+q) for x,p,q in zip(w,wp,wf)];return a,b
def main():
 rng=random.Random(20261001);cases=0
 for n in range(1,21):
  for _ in range(30):
   w=[Fraction(rng.randrange(-9,10),rng.randrange(1,10)) for _ in range(n)];wp=[Fraction(rng.randrange(1,10)) for _ in range(n)];wf=[Fraction(rng.randrange(1,10)) for _ in range(n)];a,b=allocate(w,wp,wf)
   assert [x-y for x,y in zip(a,b)]==w
   e=energy(a,b,wp,wf)
   for _ in range(5):
    h=[Fraction(rng.randrange(-5,6),rng.randrange(1,8)) for _ in range(n)];assert energy([x+z for x,z in zip(a,h)],[y+z for y,z in zip(b,h)],wp,wf)>=e
   ar,br=allocate(list(reversed(w)),list(reversed(wf)),list(reversed(wp)))
   assert ar==[-x for x in reversed(b)] and br==[-x for x in reversed(a)];cases+=1
 result={'schema':'marici.coherence.minimum-energy-frustration-allocation.v1','cases':cases,'all_exact':True,'past_allocation':'a_i=wf_i/(wp_i+wf_i) omega_i','future_allocation':'b_i=-wp_i/(wp_i+wf_i) omega_i','equal_metric':'a=omega/2, b=-omega/2','reflection_covariant_when_metrics_swap':True,'conclusion':'a positive allocation metric fixes the gauge uniquely; time-symmetric half splitting is selected only by equal past/future costs'}
 Path(__file__).with_name('minimum-energy-frustration-allocation.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
