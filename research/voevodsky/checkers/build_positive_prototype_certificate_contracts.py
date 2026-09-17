#!/usr/bin/env python3
"""Materialize proof obligations for source-faithful positive prototype lifts."""
import json
from pathlib import Path
root=Path(__file__).parents[1];res=root/'results';src=json.loads((res/'seven_transition_tetrahedron_prototypes.json').read_text())
base=['source_carrier_id','positive_feature_map','exact_signed_readout','common_positive_summand','translation_covariance','shared_face_restrictions','dagger_compatibility','refinement_naturality']
def extras(name):
 x=[]
 if 'P' in name and 'C' in name:x+=['hermitian_placement_channel','skew_commutator_channel','ordered_placement_not_collapsed']
 if 'E' in name:x+=['endpoint_gamma_row_retained','endpoint_normalization']
 if 'T' in name:x+=['finite_part_trace_row','residue_corrected_boundary_identity']
 if name in ('JPC','JCE'):x+=['full_three_way_braid_identity']
 return x
contracts={}
for name,p in src['prototypes'].items():
 obligations=base+extras(name);contracts[name]={'analytical_form':p['analytical_form'],'kind':p['kind'],'obligations':{q:{'required':True,'witness':None,'verified':False} for q in obligations},'status':'signed_only','positive_certified':False}
contracts['apex_F']={'analytical_form':'positive apex filler comparing completed trace and endpoint routes','kind':'dependency_forced_apex_filler','obligations':{q:{'required':True,'witness':None,'verified':False} for q in base+['douglas_contractivity','robust_complement_positivity','terminal_6_to_7_uniformity','weighted_hankel_discrepancy_control']},'status':'obstructed','positive_certified':False}
checks={'all_12_critical_plus_apex':len(contracts)==13,'all_have_base_obligations':all(set(base)<=set(x['obligations']) for x in contracts.values()),'PC_cells_retain_two_channels':all({'hermitian_placement_channel','skew_commutator_channel','ordered_placement_not_collapsed'}<=set(x['obligations']) for n,x in contracts.items() if 'P' in n and 'C' in n),'endpoint_cells_retain_boundary':all({'endpoint_gamma_row_retained','endpoint_normalization'}<=set(x['obligations']) for n,x in contracts.items() if 'E' in n and n!='apex_F'),'trace_cells_retain_residue':all({'finite_part_trace_row','residue_corrected_boundary_identity'}<=set(x['obligations']) for n,x in contracts.items() if 'T' in n and n!='apex_F'),'apex_carries_global_gates':{'douglas_contractivity','terminal_6_to_7_uniformity','weighted_hankel_discrepancy_control'}<=set(contracts['apex_F']['obligations']),'no_empty_witness_certified':not any(x['positive_certified'] for x in contracts.values())}
out={'schema':'marici.voevodsky.positive-prototype-certificate-contracts.v1','certificate_rule':'positive_certified iff every required obligation has a source-addressed witness verified by a directed or exact checker','base_obligations':base,'contracts':contracts,'checks':checks,'passed_contract_construction':all(checks.values()),'positive_certified_count':0,'universal_positive_realization':False,'rh_proved':False};p=res/'positive_prototype_certificate_contracts.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'prototype_count':len(contracts),'obligation_counts':{k:len(v['obligations']) for k,v in contracts.items()},'checks':checks,'passed_contract_construction':out['passed_contract_construction'],'positive_certified_count':0},indent=2));assert out['passed_contract_construction']
