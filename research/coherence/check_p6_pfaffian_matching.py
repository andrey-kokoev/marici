#!/usr/bin/env python3
"""Test whether the symmetrized Pfaffian three-cup selects adjacent matching."""

import json
from collections import defaultdict, Counter
from fractions import Fraction
from itertools import permutations
from pathlib import Path

ZERO=(0,)*6
def add(*signed):
 o=defaultdict(int)
 for s,e in signed:
  for k,v in e.items():o[k]+=s*v
 return {k:v for k,v in o.items() if v}
def move(x,i,s):
 y=list(x);y[i]+=s;return tuple(y)
def pf_matchings(items):
 if not items: return [(1,())]
 first=items[0];out=[]
 for pos in range(1,len(items)):
  second=items[pos];rest=items[1:pos]+items[pos+1:]
  sign=1 if pos%2 else -1
  for s,pairs in pf_matchings(rest):out.append((sign*s,((first,second),)+pairs))
 return out
MATCHINGS=pf_matchings(tuple(range(6)))

def run(lengths):
 def val(x):return sum(n*a for n,a in zip(x,lengths))
 def I(x):return {x:1}
 def R(i,op,x):return op(move(x,i,1))
 def S(i,op,x):return {} if val(x)<lengths[i] else op(move(x,i,-1))
 def K(q,p,op,x):return add((1,R(q,lambda y:S(p,op,y),x)),(-1,S(p,lambda y:R(q,op,y),x)))
 def F(i,j,op,x):return add((1,K(j,i,op,x)),(-1,K(i,j,op,x)))
 def compose(order,op,x):
  if not order:return op(x)
  i,j=order[0];return F(i,j,lambda y:compose(order[1:],op,y),x)
 total={}
 for sign,pairs in MATCHINGS:
  sym={}
  for order in permutations(pairs):sym=add((1,sym),(1,compose(order,I,ZERO)))
  total=add((1,total),(sign,sym))
 observed=defaultdict(int)
 for word,c in total.items():observed[val(word)]+=c
 return {x:c for x,c in observed.items() if c}

def parity(order):return -1 if sum(order[i]>order[j] for i in range(6) for j in range(i+1,6))%2 else 1

def main():
 bases=[tuple(Fraction(i) for i in (1,2,3,4,5,6)),tuple(Fraction(i) for i in (1,3,4,8,10,15))]
 tested=0;failures=[];counts=Counter()
 # all permutations for first chamber; deterministic spread for second
 orders=list(permutations(range(6)))
 selected=[orders,orders[::17]]
 for base,frame_orders in zip(bases,selected):
  expected=sum((base[i+1]-base[i]) for i in (0,2,4))
  for order in frame_orders:
   obs=run(tuple(base[i] for i in order));tested+=1;counts[len(obs)]+=1
   wanted={expected:parity(order)}
   if obs!=wanted:failures.append({'base':list(map(str,base)),'order':order,'observed':{str(k):v for k,v in obs.items()},'wanted':{str(k):v for k,v in wanted.items()}})
 assert not failures,failures[:1]
 result={'schema':'marici.coherence.p6-pfaffian-matching.v1','pfaffian_matchings':len(MATCHINGS),'frames_tested':tested,'all_match_adjacent_matching_law':True,'normalization_factor':1,'endpoint_term_count_distribution':dict(counts),'failures':failures}
 Path(__file__).with_name('p6-pfaffian-matching.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
