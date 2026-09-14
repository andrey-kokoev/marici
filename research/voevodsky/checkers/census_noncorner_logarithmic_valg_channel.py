#!/usr/bin/env python3
"""VA2: census the established logarithmic operation outside the Cut-corner family."""
import json,math
from pathlib import Path
R=Path(__file__).resolve().parents[3]
c4=json.loads((R/'research/voevodsky/results/C4_log_Cut_Gysin_cospan.json').read_text())
c10=json.loads((R/'research/voevodsky/results/C10_all_sourced_corner_projection_rank.json').read_text())
# Rows e6,v0 from the declared ambient order (e2,e3,e4,e5,e6,v0).
log=[[c4['log_matrix'][4][j] for j in range(3)],[c4['log_matrix'][5][j] for j in range(3)]]
cut=[[c4['cut_matrix'][4][j] for j in range(3)],[c4['cut_matrix'][5][j] for j in range(3)]]
def minors2(m):return [m[0][i]*m[1][j]-m[0][j]*m[1][i] for i in range(len(m[0])) for j in range(i+1,len(m[0]))]
log_minors=minors2(log);cut_minors=minors2(cut)
# Theta101 plus Theta111_filt gives columns (0,1),(1,0).
primitive_pair=[[log[0][0],log[0][2]],[log[1][0],log[1][2]]]
det=primitive_pair[0][0]*primitive_pair[1][1]-primitive_pair[0][1]*primitive_pair[1][0]
checks={'C4_passed':c4['passed'],'corner_census_rank_one':c10['rank']==1,'log_projection':log==[[0,0,1],[1,1,0]],'cut_projection':cut==[[0,0,1],[0,0,0]],'log_rank_two':any(x!=0 for x in log_minors),'log_Smith_primitive':math.gcd(*map(abs,log_minors))==1,'explicit_unimodular_pair':abs(det)==1,'mixed_log_columns_have_v0':log[1][:2]==[1,1],'mixed_cut_columns_have_no_v0':cut[1][:2]==[0,0]}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.noncorner-logarithmic-v-alg-census.v1','prospective_action':'VA2_alternative_discriminant_census','operation_families':{'frozen_total_energy_Cut_corners':{'projection_matrix_e6_v0':cut,'rank':1,'image':'Z*e6'},'logarithmic_mixed_columns':{'source_basis':c4['log_source_basis'],'projection_matrix_e6_v0':log,'rank':2,'smith_nonzero':[1,1],'primitive_pair':['Theta101','Theta111_filt'],'primitive_pair_matrix':primitive_pair,'determinant':det}},'candidate_v_alg_observable':'Theta101 (or Theta110) has unit v0 projection; Theta111_filt has unit e6 projection','VA2_resolution':'+-','resolution_reason':'The source logarithmic operation supplies a primitive algebraic v_alg channel and rank-two integral projection, but no physical relative-cycle realization/pairing for the mixed logarithmic column is established. The structure is confirmed while its advertised physical interpretation remains open.','new_interface':'primitive_algebraic_valg_channel','missing_interface':'physical_Betti_realization_of_mixed_log_column','required_next':'Construct the physical relative-cycle/Leray realization of Theta101 or Theta110 and compare its integral Betti normalization with v_alg.','checks':checks,'passed':True}
dest=R/'research/voevodsky/results/noncorner_logarithmic_valg_channel.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'VA2':out['VA2_resolution'],'log_projection':log,'det':det,'new':out['new_interface'],'missing':out['missing_interface']}))
