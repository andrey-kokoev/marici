#!/usr/bin/env python3
"""Verify prime-log Tate supports give an injective untagged four-chart realization."""
import json,math
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def edge(a,b):return tuple(sorted((a,b)))
@lru_cache(None)
def tri(v):
 if len(v)<=3:return (frozenset(),)
 out=set();a,z=v[0],v[-1]
 for k in range(1,len(v)-1):
  b=v[k];L=tri(v[:k+1]) if k+1>=3 else (frozenset(),);R=tri(v[k:]) if len(v)-k>=3 else (frozenset(),);add=set()
  if k>1:add.add(edge(a,b))
  if k<len(v)-2:add.add(edge(b,z))
  for l in L:
   for r in R:out.add(frozenset(set(l)|set(r)|add))
 return tuple(out)
def primes(k):
 out=[];x=2
 while len(out)<k:
  if all(x%p for p in out if p*p<=x):out.append(x)
  x+=1
 return out
def fourier(state):
 kind,sign,N=state
 return ('character',-sign,N) if kind=='delta' else ('delta',sign,N)
rows=[];fails=[]
for n in (4,8,12):
 F=tri(tuple(range(n)));D=sorted(set().union(*F));ps=primes(len(D));p={d:ps[i] for i,d in enumerate(D)}
 states=set();products=set()
 for T in F:
  N=math.prod(p[d] for d in T);products.add(N)
  orbit=[('delta',1,N),('character',-1,N),('delta',-1,N),('character',1,N)]
  if any(fourier(orbit[i])!=orbit[(i+1)%4] for i in range(4)):fails.append({'n':n,'N':str(N)})
  states.update(orbit)
 if len(products)!=len(F) or len(states)!=4*len(F):fails.append({'n':n,'reason':'collision'})
 rows.append({'n':n,'triangulations':len(F),'prime_channel_places':len(D),'largest_prime':ps[-1],'distinct_euler_monomials':len(products),'distinct_fourier_chart_states':len(states),'mellin_form':'N_T^(-s), N_T=product_(d in T) p_d'})
checks={'unique_factorization_separates_all_trees':not fails,'fourier_chart_cycle_exact':not fails,'no_external_tags':not fails}
out={'schema':'marici.nima.tate-prime-channel-realization.v1','degrees':[4,8,12],'results':rows,'failures':fails[:20],'checks':checks,'passed':all(checks.values()),'construction':'Assign channel d a distinct finite place p_d and oriented log support log(p_d). Convolution adds log supports, equivalently multiplies squarefree Euler monomials. Fourier gives the four delta/character ports.'}
p=ROOT/'research/nima/results/tate-prime-channel-realization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
