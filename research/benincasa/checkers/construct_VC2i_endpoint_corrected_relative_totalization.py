#!/usr/bin/env python3
"""VC2i: add endpoint collar generators cancelling the degree-17 boundary defect."""
import json
from math import gcd
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
bound=json.loads((ROOT/'research/benincasa/results/VC2g1_degree17_signed_minor_restrictions.json').read_text())
collars=json.loads((ROOT/'research/benincasa/physical-cycle-endpoint-normal-lifts.json').read_text())
rows={r['face']:r for r in bound['restrictions']};C=int(rows['b=0']['second_order_coefficient']);boundary=[int(rows['a=0']['second_order_coefficient']),C]
# Endpoint module E=<e_a,e_b>; collar module H=<h_a,h_b>, d(h_a)=e_a,d(h_b)=e_b.
d_collar=[[1,0],[0,1]];correction=[C,-C]
def mv(A,v):return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]
corrected=[x+y for x,y in zip(boundary,mv(d_collar,correction))]
# Exchange swaps endpoint labels. Both defect and correction are anti-invariant.
swap=lambda v:[v[1],v[0]]
checks={'prior_boundary_obstructed':bound['resolution']=='-+','endpoint_collars_source_geometric':collars['incidence_tangency_checks']==9,'opposite_integral_defect':boundary==[-C,C] and C!=0,'primitive_direction':gcd(abs(boundary[0]),abs(boundary[1]))==abs(C),'collar_differential_integral_identity':d_collar==[[1,0],[0,1]],'total_boundary_cancelled':corrected==[0,0],'defect_exchange_odd':swap(boundary)==[-x for x in boundary],'correction_exchange_odd':swap(correction)==[-x for x in correction]}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.VC2i-endpoint-corrected-relative-totalization.v1','prospective_action':'VC2i_enlarge_relative_totalization_with_endpoint_terms','modules':{'bulk':'degree-17 exact weighted-overlap representative','endpoint':'Z<e_a,e_b> for moving faces a=0,b=0','collar':'Z<h_a,h_b>'},'differential':{'d_h_to_e':d_collar,'bulk_boundary':boundary,'collar_correction':correction,'corrected_total_boundary':corrected},'exchange':'a<->b swaps endpoint and collar bases; defect and correction are both odd','resolution':'+-','positive_result':'An integral exchange-equivariant mapping-cylinder correction cancels the complete second-order endpoint defect exactly.','physical_gap':'The endpoint normal lifts establish local geometric collars, but their marked-wall residue pairing and radial normalization were explicitly not recomputed. Thus algebraic relative closure is constructed while the physical pairing remains unvalidated.','interfaces_added':['endpoint_corrected_relative_complex','algebraic_relative_descent'],'interface_withheld':'physical_relative_descent','next':'Compute the marked-wall residue pairing on the a=0 and b=0 collar chains and test whether their normalized contributions remain exactly opposite.','checks':checks,'passed':True};p=ROOT/'research/benincasa/results/VC2i_endpoint_corrected_relative_totalization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':'+-','defect':boundary,'correction':correction,'total':corrected,'next':out['next']}))
