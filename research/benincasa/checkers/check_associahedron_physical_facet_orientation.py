#!/usr/bin/env python3
"""Audit the orientation semantics and arbitrary-rank scope of the facet cochain."""
import json
from fractions import Fraction
from pathlib import Path
R=Path(__file__).resolve().parents[2]
x=json.loads((R/'nima/results/n8-physical-facet-cochain.json').read_text())
eps=x['top_boundary_signs']; weights=[Fraction(x['facet_weights'][k]) for k in sorted(x['facet_weights'])]
physical=Fraction(x['physical_scalar'])
raw_eval=sum(e*w for e,w in zip(eps,weights))
twisted_coords=[e*w for e,w in zip(eps,weights)]
twisted_eval=sum(e*c for e,c in zip(eps,twisted_coords))
assert twisted_eval==sum(weights)==physical and raw_eval!=physical
rows=[]
for m in range(1,9):
 pos=m*(m+1)//2; neg=m; facets=m*(m+3)//2
 rows.append({'m':m,'dimension':m,'positive_root_history_facets':pos,'negative_simple_facets':neg,'total_facets':facets,'partition':pos+neg==facets})
out={'schema':'marici.benincasa.associahedron-physical-facet-orientation.v1','n8_orientation_audit':{'top_boundary':'d_m[A_m]=sum_alpha epsilon_alpha F_alpha','ordinary_dual_coordinate_rule':'A cochain phi has evaluation phi(d_m[A_m])=sum epsilon_alpha phi(F_alpha).','raw_weights_as_dual_coordinates':{'evaluation':str(raw_eval),'equals_physical_scalar':False},'orientation_twisted_coordinates':{'rule':'phi(F_alpha)=epsilon_alpha w_alpha','evaluation':str(twisted_eval),'equals_physical_scalar':True},'basis_invariance':'Reorienting one facet flips both epsilon_alpha and its dual coordinate; reversing the top orientation flips every epsilon and every induced coordinate, so the pairing is invariant.','interpretation':'The checker is orientation-consistent only after explicitly treating w_alpha as unoriented facet densities converted to dual coordinates by epsilon_alpha. The equality is then the tautology epsilon_alpha^2=1.'},'cohomological_status':{'delta_phi_on_top_cell':str(twisted_eval),'nonzero':twisted_eval!=0,'is_cocycle':False,'meaning':'Because delta phi([A3])=phi(d3[A3]) is the nonzero physical scalar, this physical facet cochain is not a cocycle. d2 d3=0 says the top boundary is a chain cycle; it does not imply delta phi=0.'},'arbitrary_m_statement':{'carrier':'The m-dimensional type-A_m associahedron has facets indexed by almost-positive roots.','counts':'m(m+1)/2 positive roots plus m negative simple roots equals m(m+3)/2 facets.','conditional_formula':'Given scalar densities w_alpha on every facet and incidence signs epsilon_alpha in d_m[A_m], define phi(F_alpha)=epsilon_alpha w_alpha. Then phi(d_m[A_m])=sum_alpha w_alpha.','physical_scope':'The formula is a finite cellular identity at each m. A physical NNMHV theorem additionally requires source-derived arbitrary-m weights and proof that their sum is the desired physical scalar; those data currently exist only in the tested n=8 case.','rows':rows},'disposition':'orientation convention valid as an orientation-twisted density conversion; arbitrary-m extension is conditional/tautological, not yet a physical or cohomological promotion','passed':True}
p=R/'benincasa/results/associahedron_physical_facet_orientation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
