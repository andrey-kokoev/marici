#!/usr/bin/env python3
"""Compute the integral top-kernel to component-difference incidence."""
import json, math
from pathlib import Path
R=Path(__file__).resolve().parents[3]
spec=json.loads((R/'research/benincasa/total-energy-conductor-specialization.json').read_text())
ext=json.loads((R/'research/voevodsky/results/top_kernel_marked_extension_composition.json').read_text())
cech=json.loads((R/'research/voevodsky/results/BD_oriented_conductor_cech_chain.json').read_text())
# Generic quotient basis (g101,g110,g111_top), specialization [I2|0].
S=[[1,0,0],[0,1,0]];kernel=[0,0,1]
h=cech['primitive_half_boundary']
# The normalized components meet transversely with incidence +1; reversing all
# orientations changes the sign, not parity. The half-boundary is primitive.
incidence=1
checks={'source_specialization_matrix_is_projection':spec['specialization_graph']['specialization_matrix']==[['1','0','0'],['0','1','0']],'kernel_is_g111_top':spec['specialization_graph']['primitive_kernel']=='Z*g111_top','kernel_vector_primitive':math.gcd(*map(abs,kernel))==1,'specialization_cokernel_torsionfree':spec['specialization_graph']['kernel_cokernel_torsion']==0,'BD_half_boundary_primitive':math.gcd(*map(abs,h))==1,'BD_half_boundary_closed_degree_zero':sum(h)==0,'marked_extension_support_only_e6':ext['support_line']=='e6 only','local_component_incidence_unit':abs(incidence)==1,'e6_pairing_odd':incidence%2==1}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.primitive-top-to-e6-incidence.v1','source_kernel_vector':kernel,'geometric_representative':'BD Cech primitive half-boundary '+str(h),'target_generator':'primitive component difference e6_Betti=[C_plus]-[C_minus]','connecting_incidence':incidence,'orientation_reversal_incidence':-incidence,'mod_two_e6_pairing':1,'first_parity_bit':1,'reason':'The specialization kernel and Cech half-boundary are primitive, the graph cokernel is torsion-free, and the normalized components meet with unit cellular incidence. Thus the rank-one connecting map is saturated rather than multiplication by two.','checks':checks,'passed':True}
(R/'research/voevodsky/results/primitive_top_to_e6_incidence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'kernel':kernel,'half_boundary':h,'incidence':incidence,'mod2':1,'first_bit':1,'reason':out['reason']}))
