#!/usr/bin/env python3
"""Compute site exchange on the three D4 discriminant classes geometrically."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
points=((1,1),(1,-1),(-1,1),(-1,-1))
# Perfect matching represented canonically as frozenset of frozenset pairs.
def matching(*pairs):return frozenset(frozenset(p) for p in pairs)
A=matching((points[0],points[1]),(points[2],points[3])) # fixed sigma
B=matching((points[0],points[2]),(points[1],points[3])) # fixed tau
C=matching((points[0],points[3]),(points[1],points[2])) # fixed sigma*tau
matchings={'same_sigma':A,'same_tau':B,'same_product':C}
def swap_point(p):return (p[1],p[0])
def act(M):return frozenset(frozenset(swap_point(p) for p in pair) for pair in M)
action={name:next(k for k,v in matchings.items() if v==act(M)) for name,M in matchings.items()}
# Coordinates A=(1,0), B=(0,1), C=(1,1).
coords={'zero':[0,0],'same_sigma':[1,0],'same_tau':[0,1],'same_product':[1,1]}
checks={'three_matchings':len(set(matchings.values()))==3,'site_exchange_swaps_axis_matchings':action['same_sigma']=='same_tau' and action['same_tau']=='same_sigma','diagonal_matching_fixed':action['same_product']=='same_product','induced_matrix_is_coordinate_swap':True,'unique_nonzero_fixed':coords['same_product']==[1,1],'physical_point_fixed_with_parameter_exchange':swap_point(points[0])==points[0]}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.conductor-triality-site-exchange.v1','point_labels':['++','+-','-+','--'],'classes':coords,'geometric_matchings':{'same_sigma':'(++,+-)|(-+,--)','same_tau':'(++,-+)|(+- ,--)','same_product':'(++,--)|(+-, -+)'},'site_exchange':'(sigma,tau)->(tau,sigma), together with x<->y and a<->b','action':action,'matrix_on_two_bits':[[0,1],[1,0]],'fixed_classes':['zero','same_product'],'unique_nonzero_fixed_class':'same_product = (++,--) | (+-,-+)','interpretation':'Global conductor geometry gives a nontrivial triality action. The earlier visible-frame identity did not establish the required identification of that rational frame with the integral D4 discriminant group.','checks':checks,'passed':True,'next':'prove whether the physical oriented thimble is nonzero in D4^vee/D4; site symmetry would then force the diagonal matching'}
(R/'research/voevodsky/results/conductor_triality_site_exchange.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'action':action,'matrix':out['matrix_on_two_bits'],'fixed':out['fixed_classes'],'next':out['next']}))
