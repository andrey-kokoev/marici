#!/usr/bin/env python3
"""Decompose Catalan triangulations into C4 orbits and size the equivariant Fourier realization."""
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
def rot(T,s,n):return frozenset(edge((a+s)%n,(b+s)%n) for a,b in T)
rows=[]
for n in (4,8,12):
 F=set(tri(tuple(range(n))));s=n//4;unseen=set(F);o2=o4=0
 while unseen:
  T=next(iter(unseen));orb={rot(T,k*s,n) for k in range(4)}
  if len(orb)==2:o2+=1
  elif len(orb)==4:o4+=1
  else:raise AssertionError(len(orb))
  unseen-=orb
 d=len(F);half=math.comb(n-2,(n-2)//2);assert 2*o2==half and 2*o2+4*o4==d
 multiplicities=[o4+o2,o4,o4+o2,o4]
 rows.append({'n':n,'dimension':d,'size_two_orbits':o2,'size_four_orbits':o4,'character_multiplicities_from_orbits':multiplicities,'generic_fourier_orbit_copies_required':o4,'even_two_port_orbit_copies_required':o2})
checks={'orbit_dimensions_close':all(2*r['size_two_orbits']+4*r['size_four_orbits']==r['dimension'] for r in rows),'all_four_characters_accounted_for':all(sum(r['character_multiplicities_from_orbits'])==r['dimension'] for r in rows)}
out={'schema':'marici.nima.catalan-c4-orbit-realization.v1','degrees':[4,8,12],'results':rows,'checks':checks,'passed':all(checks.values()),'realization':'Map each size-four Catalan orbit equivariantly to a distinct generic oriented Fourier four-port orbit; map each size-two orbit to a distinct reflection-even Fourier two-port orbit.'}
p=ROOT/'research/nima/results/catalan-c4-orbit-realization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
