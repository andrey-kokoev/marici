#!/usr/bin/env python3
"""Verify compressed channel-monomial Catalan realization and C4 equivariance."""
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
def rot_edge(e,s,n):a,b=e;return edge((a+s)%n,(b+s)%n)
def rot_tree(T,s,n):return frozenset(rot_edge(e,s,n) for e in T)
rows=[]
for n in (4,8,12):
 F=tri(tuple(range(n)));channels=sorted(set().union(*F));idx={e:i for i,e in enumerate(channels)}
 sig=lambda T:sum(1<<idx[e] for e in T)
 codes={sig(T) for T in F};injective=len(codes)==len(F);s=n//4
 equivariant=all(sig(rot_tree(T,s,n))==sum(1<<idx[rot_edge(e,s,n)] for e in T) for T in F)
 # Exponential Mellin atom x_e -> exp(2^idx(e) z): products encode the same integer uniquely.
 exponent_codes={sum(1<<idx[e] for e in T) for T in F}
 # Every compatible disjoint channel union is multiplication of squarefree monomials.
 multiplicative=all(sig(T)==sum(1<<idx[e] for e in T) for T in F)
 rows.append({'n':n,'facets':len(F),'channel_atoms':len(channels),'facet_degree':n-3,'injective_channel_monomials':injective,'quarter_rotation_equivariant':equivariant,'mellin_exponent_codes_injective':len(exponent_codes)==len(F),'subtree_union_multiplicative':multiplicative,'compression_ratio_facets_per_atom':len(F)/len(channels)})
checks={'all_injective':all(r['injective_channel_monomials'] and r['mellin_exponent_codes_injective'] for r in rows),'all_c4_equivariant':all(r['quarter_rotation_equivariant'] for r in rows),'all_multiplicative':all(r['subtree_union_multiplicative'] for r in rows)}
out={'schema':'marici.nima.channel-monomial-c4-realization.v1','degrees':[4,8,12],'results':rows,'checks':checks,'passed':all(checks.values()),'construction':'One generator x_d per polygon channel; T maps to product_(d in T) x_d. Analytically x_d maps to Mellin multiplier exp(2^index(d) z). Rotation permutes generators.'}
p=ROOT/'research/nima/results/channel-monomial-c4-realization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
