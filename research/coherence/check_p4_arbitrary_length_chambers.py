#!/usr/bin/env python3
"""Test the P4 endpoint law for arbitrary distinct positive rational shifts."""

import json, random
from collections import defaultdict, Counter
from fractions import Fraction
from itertools import permutations
from pathlib import Path

ZERO=(0,0,0,0)
def add(*signed):
 o=defaultdict(int)
 for s,e in signed:
  for k,v in e.items():o[k]+=s*v
 return {k:v for k,v in o.items() if v}
def move(x,i,s):
 y=list(x);y[i]+=s;return tuple(y)
def run(lengths):
 def val(x):return sum(n*a for n,a in zip(x,lengths))
 def I(x):return {x:1}
 def R(i,op,x):return op(move(x,i,1))
 def S(i,op,x):return {} if val(x)<lengths[i] else op(move(x,i,-1))
 def K(q,p,op,x):return add((1,R(q,lambda y:S(p,op,y),x)),(-1,S(p,lambda y:R(q,op,y),x)))
 def F(i,j,op,x):return add((1,K(j,i,op,x)),(-1,K(i,j,op,x)))
 def comp(i,j,k,l,op,x):return F(i,j,lambda y:F(k,l,op,y),x)
 def anti(i,j,k,l,op,x):return add((1,comp(i,j,k,l,op,x)),(1,comp(k,l,i,j,op,x)))
 return add((1,anti(0,1,2,3,I,ZERO)),(-1,anti(0,2,1,3,I,ZERO)),(1,anti(0,3,1,2,I,ZERO))),val

def parity(order):return -1 if sum(order[i]>order[j] for i in range(4) for j in range(i+1,4))%2 else 1

def main():
 samples=[(Fraction(1),Fraction(2),Fraction(3),Fraction(4)),(Fraction(1,3),Fraction(5,4),Fraction(11,5),Fraction(19,6))]
 rng=random.Random(20260912)
 while len(samples)<22:
  xs=tuple(sorted(set(Fraction(rng.randrange(1,80),rng.randrange(1,12)) for _ in range(4))))
  if len(xs)==4:samples.append(xs)
 failures=[];tested=0;term_counts=Counter()
 for base in samples:
  expected=(base[1]-base[0])+(base[3]-base[2])
  for order in permutations(range(4)):
   lengths=tuple(base[i] for i in order);expr,val=run(lengths);tested+=1;term_counts[len(expr)]+=1
   observed=defaultdict(int)
   for word,c in expr.items():observed[val(word)]+=c
   observed={x:c for x,c in observed.items() if c}
   wanted={expected:parity(order)}
   if observed!=wanted:failures.append({'base':list(map(str,base)),'order':order,'observed':{str(k):v for k,v in observed.items()},'wanted':{str(k):v for k,v in wanted.items()}})
 assert not failures,failures[:1]
 result={'schema':'marici.coherence.p4-arbitrary-length-chambers.v1','distinct_length_sets':len(samples),'permuted_frames_tested':tested,'all_match_order_statistic_law':True,'law':'sgn(sigma) ev_((a(1)-a(0))+(a(3)-a(2))) for sorted lengths','raw_term_count_distribution':dict(term_counts),'failures':failures}
 Path(__file__).with_name('p4-arbitrary-length-chambers.v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
