import json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
inst=json.loads((root/'research/voevodsky/compact-weil-source-identity-instance.json').read_text())
wall=json.loads((root/'research/voevodsky/prime-half-density-makes-the-countable-wall-wronskian-form-continuous.v1.json').read_text())
checks={'source_endpoint_registered':'endpoint' in str(inst).lower(),'source_gamma_registered':'gamma' in str(inst).lower(),'source_prime_translation_registered':'prime_translation' in str(inst),'wall_regular_form_registered':'omega_reg' in wall['complete_linking']['definition'],'wall_boundary_form_registered':'omega_wall' in wall['wall_linking_form']['definition'],'wall_continuity_registered':wall['complete_linking']['continuous'],'external_equality_not_assumed':wall['claim_boundary']['identification_with_old_conservative_linking_metric'] is False}
out={'schema':'marici.nima.qRB-compact-source-wall-comparison-contract.v1','checks':checks,'passed':all(checks.values()),'source_terms':['endpoint','gamma','prime translation'],'wall_terms':['regular linking','weighted jump/endpoint wall linking'],'required_identity':'omega_reg + omega_wall = E + G + P_L','status':'comparison interface complete; equality implementation remains to be written','rh_proved':False}
p=root/'research/nima/results/qRB-compact-source-wall-comparison-contract.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
