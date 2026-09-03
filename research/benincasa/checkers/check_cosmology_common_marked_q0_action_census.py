#!/usr/bin/env python3
"""Census owned result artifacts for serialized marked q0 actions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results';SELF='cosmology_common_marked_q0_action_census.json'
q0_files=[];matrix_fields=[];malformed=[]
def walk(x,path='',hits=None):
 if hits is None:hits=[]
 if isinstance(x,dict):
  for k,v in x.items():
   p=path+k
   if 'q0' in p.lower() and isinstance(v,list) and v and isinstance(v[0],list):hits.append(p)
   walk(v,p+'.',hits)
 elif isinstance(x,list):
  for i,v in enumerate(x):walk(v,path+str(i)+'.',hits)
 return hits
for p in R.glob('*.json'):
 if p.name==SELF:continue
 text=p.read_text(errors='ignore')
 try:d=json.loads(text)
 except json.JSONDecodeError:
  malformed.append({'file':p.name,'contains_q0':'q0' in text.lower()});continue
 if 'q0' in text.lower():
  q0_files.append(p.name)
  for field in walk(d):
   if not (p.name=='cosmology_normalized_Cartan_shear_q0_naturality.json' and field=='deliberate_unequal_q0_residual'):matrix_fields.append({'file':p.name,'field':field})
assert not any(x['contains_q0'] for x in malformed)
assert matrix_fields==[]
torsor=json.loads((R/'e6_global_logarithmic_torsor.json').read_text());prior=json.loads((R/'cosmology_rank12_shear_artifact_census.json').read_text());gate=json.loads((R/'cosmology_e6_rank12_triangular_transport_gate.json').read_text())
assert torsor['e6_v_connection_at_u0']==torsor['qtop_v_connection_at_u0'] and prior['source_derived_q0_to_e6_shear_count']==0 and gate['missing']['marked_quotient_q0_action']
out={'schema':'marici.benincasa.cosmology-common-marked-q0-action-census.v1','owned_valid_result_artifacts_with_q0_text':len(q0_files),'serialized_source_q0_matrix_fields':matrix_fields,'malformed_generated_artifacts_excluded':len(malformed),'malformed_artifacts_containing_q0':0,'scalar_connection_candidate':{'artifact':'e6_global_logarithmic_torsor.json','e6':torsor['e6_v_connection_at_u0'],'qtop':torsor['qtop_v_connection_at_u0'],'difference':torsor['hom_connection_difference'],'typed_as_marked_q0_action':False},'prior_source_derived_q0_to_e6_shear_count':0,'common_marked_q0_action_found':False,'conclusion':'the corpus contains an equal scalar qtop/e6 connection coefficient but no marked q0 action matrices on the two extension grades','next_test':'determine whether the equal scalar qtop/e6 connection can be promoted to a common marked q0 action or is only a one-variable connection coincidence','passed':True};(R/SELF).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
