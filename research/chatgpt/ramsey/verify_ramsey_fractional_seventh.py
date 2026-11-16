#!/usr/bin/env python3
"""Pure-Python rational check: 4-local Hall + triangle + exact degree feasible, 5-local not."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import json
file=Path(__file__).with_name('ramsey_fractional_seventh.json')
r=json.loads(file.read_text())
s=r['supports']
assert r['schema']=='ramsey.four-local-exception.v1'
assert len(s)==16 and all(sum((m>>i)&1 for m in s)==5 for i in range(6))
weights={(a,b):Fraction(w) for a,b,w in r['edge_weights']}
assert len(weights)==len(r['edge_weights'])
assert all(0<=a<b<16 and (s[a]&s[b])==0 and 0<x<=1 for (a,b),x in weights.items())
for i in range(16):assert sum(x for (a,b),x in weights.items() if a==i or b==i)==6-s[i].bit_count()
for U in combinations(range(16),3):
  assert sum(weights.get((a,b),0) for a,b in combinations(U,2))<=2
violated=[]
for k in range(2,6):
 for U in combinations(range(16),k):
  union=0
  for i in U:union|=s[i]
  if union.bit_count()>=k:continue
  mass=sum(weights.get((a,b),0) for a,b in combinations(U,2))
  if mass<1:violated.append((U,mass))
assert violated and all(len(U)==5 for U,v in violated)
print('VERIFIED exact rational four-local feasible witness; five-local contradictions',len(violated))
print('Weight denominators',sorted({x.denominator for x in weights.values()}))
