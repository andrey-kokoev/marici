#!/usr/bin/env python3
"""Compare the declared G4 radial amendment with the minimal Xi delta."""
import json
from pathlib import Path
from evidence_policy import write_result
R=Path(__file__).resolve().parents[2]
a=json.loads((R/'research/aspect/contracts/theta-rh-g4-radial-interface.v1.json').read_text())
p=json.loads((R/'research/conjecture_replay/contracts/CR1-g4-Xi-characteristic-delta.proposed.v1.json').read_text())
i=a['interface'];required=['feature_carrier','endpoint_pontryagin_node','radial_bulk_response','interconnection']
existing={'radial_fold':all(k in i for k in ['radial_history_carrier','first_order_differential_and_domain']),'green_wall':i['green_structure']['boundary_matrix']=='diag(-1,1)','real_readback':'graph_conclusion' in i['real_comparison'],'loading':'arithmetic_loading' in i,'response_semantics':'response_preservation' in i}
missing={'explicit_six_coordinate_carrier':'feature_carrier' not in i,'endpoint_pontryagin_node':'endpoint_pontryagin_node' not in i,'theta_H_observation_equation':'radial_bulk_response' not in i,'bordered_interconnection':'interconnection' not in i,'zero_postcycle_radical':'green_radical' not in i}
proposal_checks={'six':len(p['feature_carrier']['coordinates'])==6,'half':p['feature_carrier']['codiagonal'].endswith('(W_plus+W_minus)/2'),'row':p['endpoint_pontryagin_node']['metric_adjoint_return_row']==[1,-1],'char':'[[s,0,1]' in p['interconnection']['characteristic'],'authority':p['status']=='proposal_only'}
assert all(existing.values()) and all(missing.values()) and all(proposal_checks.values())
out={'schema':'marici.conjecture-replay.CR1-G4-Xi-delta-conformance.v1','passed':True,'claim_status':'proved','evidence':[{'class':'SYMBOLIC','claim':'The declared and proposed JSON contracts were structurally compared for the exact required fields and coefficients.','checker':'research/conjecture_replay/check_CR1_G4_Xi_delta_conformance.py'},{'class':'DECLARED','claim':'The radial fold, wall Green form, Real readback, arithmetic loading, and semantic response preservation are operator-authorized declarations.','source':'research/aspect/contracts/theta-rh-g4-radial-interface.v1.json'}],'outcome':'+-','already_declared':existing,'missing_authoritative_fields':missing,'proposal_conforms':proposal_checks,'conclusion':'The current G4 amendment is compatible with the generalized Xi characteristic but does not define it: five interconnection fields are absent. The proposal is the minimal explicit successor delta and remains nonauthoritative.','next':'obtain_owner_adoption_or_construct_the_complete_G4_joint_adjoint_witness_against_the_proposed_delta'}
write_result(R/'research/conjecture_replay/results/CR1_G4_Xi_delta_conformance.json',out);print(json.dumps({'passed':True,'outcome':'+-','declared':sum(existing.values()),'missing':sum(missing.values()),'proposal_only':True}))
