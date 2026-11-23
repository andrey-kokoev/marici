"""Exhaust the natural column correspondence and re-sorting; no arbitrary matching of occurrences across ties."""
from itertools import product,permutations
from collections import Counter
from pathlib import Path
import json
P=list(permutations(range(4)));kinds=Counter();patterns=Counter();examples={};traces={}
for x in product(range(10),repeat=4):
 orders=[p for p in P if all(x[p[i]]>=x[p[i+1]] for i in range(3))];cache=set()
 for p in orders:
  borrow=0;Y=[];B=[]
  for i in (3,2,1,0):
   z=x[p[i]]-x[p[3-i]]-borrow;borrow=int(z<0);B.append(borrow);Y.append(z%10)
  assert not borrow;cache.add((tuple(Y[::-1]),tuple(B)))
 assert len(cache)==1;y,b=cache.pop();assert int(''.join(map(str,y)))==int(''.join(map(str,sorted(x,reverse=True))))-int(''.join(map(str,sorted(x))));sig=','.join(sorted({'retain' if {p[0],p[3]}=={0,3} else 'swap' if {p[0],p[3]}=={1,2} else 'split' for p in P if all(y[p[i]]>=y[p[i+1]] for i in range(3))}));kinds[sig]+=1;patterns[b]+=1;xx=''.join(map(str,x));rec=dict(input=xx,output=''.join(map(str,y)),borrows_units_first=b,next_role=sig)
 if len(set(x))==4 and len(set(y))==4:examples.setdefault(sig,rec)
 if xx in ('1123','6174'):traces[xx]=rec
r=dict(inputs=sum(kinds.values()),next_roles=kinds,borrow_types={''.join(map(str,k)):v for k,v in patterns.items()},distinct_digit_examples=examples,special=traces);print(r);(Path(__file__).resolve().parents[1]/'results/kaprekar_borrow_interface.json').write_text(json.dumps(r,indent=2)+'\n')
