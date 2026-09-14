#!/usr/bin/env python3
"""Compare the physical corner interval and global component difference integrally."""
import json
from fractions import Fraction
from pathlib import Path
R=Path(__file__).resolve().parents[3]
c1=json.loads((R/'research/voevodsky/results/C1_integral_e6_replay.json').read_text())
c4=json.loads((R/'research/voevodsky/results/C4_log_Cut_Gysin_cospan.json').read_text())
pic=json.loads((R/'research/voevodsky/results/infinity_component_picard_marking.json').read_text())
cell=json.loads((R/'research/voevodsky/results/two_node_cellular_unit_incidence.json').read_text())
Cp=pic['vectors']['C_plus'];Cm=pic['vectors']['C_minus'];d=pic['vectors']['e6_Betti=C_minus-C_plus']
def dot(u,v):return u[0]*v[0]-sum(u[i]*v[i] for i in range(1,8))
def lincomb(cols,v):return [sum(cols[j][i]*v[j] for j in range(len(v))) for i in range(8)]
sheet_boundary=[-1,1];image=lincomb([Cp,Cm],sheet_boundary)
# E1 supplies an integral Picard covector restricting to (0,1) on (C+,C-).
E1=[0,1,0,0,0,0,0,0];restriction=[dot(E1,Cp),dot(E1,Cm)]
eta=[Fraction(-1,2),Fraction(1,2)];ell=[Fraction(x) for x in restriction];diagonal_shift=[ell[i]-eta[i] for i in range(2)]
checks={'physical_pair_is_primitive_eta':c1['primitive_Betti_output']==[-1,0,0],'C4_common_line_e6':c4['commuting_value']==[0,0,0,0,2,0],'sheet_boundary_maps_to_global_difference':image==d,'global_half_boundary_maps_to_difference':cell['primitive_width_two_half_boundary']==sheet_boundary,'integral_dual_restriction':restriction==[0,1],'dual_evaluates_difference_one':restriction[0]*sheet_boundary[0]+restriction[1]*sheet_boundary[1]==1,'symmetric_eta_evaluates_difference_one':sum(eta[i]*sheet_boundary[i] for i in range(2))==1,'eta_and_integral_dual_differ_by_diagonal':diagonal_shift==[Fraction(1,2),Fraction(1,2)],'diagonal_shift_vanishes_on_degree_zero':sum(diagonal_shift[i]*sheet_boundary[i] for i in range(2))==0,'Picard_difference_primitive':pic['checks']['difference_primitive']}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.C3-local-global-e6-comparison.v1','normalization_map':{'domain_basis':['sheet_plus','sheet_minus'],'target_basis':pic['basis'],'matrix_columns':[Cp,Cm]},'primitive_sheet_boundary':sheet_boundary,'image_in_Picard':image,'image_name':'d_infinity=C_minus-C_plus=e6_Betti','physical_dual':{'symmetric_representative':['-1/2','1/2'],'integral_Picard_extension':'intersection with E1','restriction_to_sheets':restriction,'difference_between_representatives':'diagonal constant (1/2,1/2)','pairing_with_boundary':1},'comparison':{'physical_corner':'minus one primitive eta by the occurrence-resolved C1 replay','global_Cech':'primitive d_infinity by the two-node cellular boundary','C4_bridge':'both coefficient operations meet on the e6 conductor line'},'C3_status':'confirmed up to overall orientation: the local physical interval is the primitive dual detector of the same global component-difference e6 class','parity_agreement':[1,0],'checks':checks,'passed':True}
(R/'research/voevodsky/results/C3_local_global_e6_comparison.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'C3':out['C3_status'],'sheet_boundary':sheet_boundary,'Picard_image':image,'dual_restriction':restriction,'pairing':1,'parity':out['parity_agreement']}))
