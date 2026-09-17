#!/usr/bin/env python3
"""Exact finite quadrangulation amplitudes for planar quartic scalar theory."""
import itertools,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def edge(a,b):return tuple(sorted((a,b)))
def crosses(d,e):
 a,b=d;c,d=e
 return (a<c<b<d) or (c<a<d<b)
def quadrangulations(n):
 k=(n-4)//2
 # A quadrangulation diagonal cuts the even polygon into two even polygons.
 allowed=[(i,j) for i in range(1,n+1) for j in range(i+1,n+1) if j-i not in (1,n-1) and (j-i)%2==1]
 out=[]
 def rec(start,chosen):
  if len(chosen)==k:out.append(frozenset(chosen));return
  for p in range(start,len(allowed)):
   d=allowed[p]
   if all(not crosses(d,e) for e in chosen):rec(p+1,chosen+[d])
 rec(0,[]);return set(out)
def fuss(q):return math.comb(3*q,q)//(2*q+1)
rows=[];passed=True
for n in range(4,15,2):
 Q=quadrangulations(n);q=(n-2)//2;channels=sorted(set().union(*Q)) if Q and n>4 else [];factor=True;facts=[]
 for d in channels:
  i,j=d;nL=j-i+1;nR=n-(j-i)+1;expected=fuss((nL-2)//2)*fuss((nR-2)//2);actual=sum(d in T for T in Q);ok=actual==expected;factor &= ok;facts.append({'channel':list(d),'residue_terms':actual,'expected_product_terms':expected,'passed':ok})
 # Dihedral maps preserve the support.
 rot=lambda d:edge(d[0]%n+1,d[1]%n+1);ref=lambda d:edge(n+1-d[0],n+1-d[1])
 cyclic={frozenset(rot(d) for d in T) for T in Q}==Q;reflection={frozenset(ref(d) for d in T) for T in Q}==Q
 ok=len(Q)==fuss(q) and all(len(T)==q-1 for T in Q) and factor and cyclic and reflection;passed &= ok
 rows.append({'n':n,'quartic_vertices':q,'quadrangulations':len(Q),'expected_fuss_catalan':fuss(q),'channels':len(channels),'factorizations':facts,'cyclic_invariance':cyclic,'reflection_invariance':reflection,'passed':ok})
out={'schema':'marici.nima.phi4-quadrangulation-amplitudes.v1','model':'planar tree-level scalar phi^4 with unit quartic vertices','definition':'Sum one propagator monomial over every polygon quadrangulation.','range':{'min_n':4,'max_n':14,'even_only':True},'results':rows,'passed':passed,'scope':'Exact finite support, symmetry, and channel term-count factorization. Stokes-polytope weights or reference-quadrangulation restrictions are not asserted.'}
p=ROOT/'research/nima/results/phi4-quadrangulation-amplitudes.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':passed,'summary':[{'n':r['n'],'terms':r['quadrangulations'],'channels':r['channels']} for r in rows]},indent=2));raise SystemExit(0 if passed else 1)
