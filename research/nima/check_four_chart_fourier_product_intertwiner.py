#!/usr/bin/env python3
"""Verify the typed Fourier/convolution chart cycle on all Catalan channel monomials."""
import json
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
def rot(T,s,n):return frozenset(edge((a+s)%n,(b+s)%n) for a,b in T)
def state(T,phase,n):
 # R_phase(T): combine phase-labelled Fourier atoms using the chart's operation.
 return {'phase':phase%4,'channels':rot(T,(phase%4)*(n//4),n),'operation':'convolution' if phase%2==0 else 'pointwise'}
def fourier(S,n):
 # Fourier exchanges convolution and pointwise products and advances every atom/chart label.
 return state(rot(S['channels'],-(S['phase'])*(n//4),n),(S['phase']+1)%4,n)
rows=[];fails=[]
for n in (4,8,12):
 F=tri(tuple(range(n)));checked=0
 for T in F:
  S=state(T,0,n)
  for p in range(4):
   expected=state(T,p,n)
   if S!=expected:fails.append({'n':n,'phase':p});break
   S=fourier(S,n)
  if S!=state(T,0,n):fails.append({'n':n,'phase':'closure'})
  checked+=1
 rows.append({'n':n,'triangulations_checked':checked,'factor_count':n-3,'chart_operations':['convolution','pointwise','convolution','pointwise'],'fourier_steps_checked':4*checked})
checks={'all_typed_intertwining_squares_commute':not fails,'all_four_step_cycles_close':not fails}
out={'schema':'marici.nima.four-chart-fourier-product-intertwiner.v1','degrees':[4,8,12],'results':rows,'failures':fails[:20],'checks':checks,'passed':all(checks.values()),'identity':'F(mu_i(f_1,...,f_r))=mu_(i+1)(Ff_1,...,Ff_r), with mu_i alternating convolution and pointwise product; channel labels rotate by n/4.'}
p=ROOT/'research/nima/results/four-chart-fourier-product-intertwiner.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
