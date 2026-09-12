#!/usr/bin/env python3
"""Construct finite signed log-prime evaluation sets through word depth four."""

import json, math
from itertools import product
from pathlib import Path

PRIMES=(2,3,5,7); A=tuple(math.log(p) for p in PRIMES)
def vectors(k): return [n for n in product(range(-k,k+1),repeat=4) if sum(abs(x) for x in n)<=k]
def value(n): return sum(x*a for x,a in zip(n,A))
def key(x): return round(x,12)
def main():
 levels=[]; sets=[]
 for k in range(5):
  vals={key(value(n)) for n in vectors(k) if value(n)>=-1e-12};sets.append(vals)
  levels.append({'depth':k,'nonnegative_evaluation_points':len(vals),'positive_breakpoints':len(vals-{0.0})})
 checks=[]
 for k in range(4):
  ok=True
  for n in vectors(k):
   for i in range(4):
    for sign in (-1,1):
     m=list(n);m[i]+=sign
     if sum(abs(x) for x in m)<=k+1 and value(m)>=-1e-12 and key(value(m)) not in sets[k+1]:ok=False
  checks.append(ok)
 assert all(checks)
 result={'schema':'marici.coherence.log-prime-trace-depth-filtration.v1','primes':PRIMES,'levels':levels,'transport_depth_inclusions':checks,'depth_four_points':sorted(sets[4]),'claim':'operator words of length at most k require a finite signed-log evaluation fiber Gamma_k; one shift maps depth k to k+1'}
 target=Path(__file__).with_name('log-prime-trace-depth-filtration.v1.json');target.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'levels':levels,'transport_depth_inclusions':checks},indent=2))
if __name__=='__main__':main()
