"""Synthetic completed-zeta to fixture-only radial-source conformance test."""
import json
from pathlib import Path

ROOT=Path('research/nima')
CONTRACT=ROOT/'contracts/g4-radial-interface-candidate.v1.json'
RESULT=ROOT/'results/synthetic-zeta-g4-source-map.json'
contract=json.loads(CONTRACT.read_text())
assert contract['status']=='test_fixture_only'
required={'prime','grade','shell','ordered_pair','theta_label'}
assert required.issubset(set(contract['radial_carrier']['labels']))

source=[
 {'id':'2^1','kind':'prime_power','prime':2,'grade':1,'log_grade':'log(2)'},
 {'id':'2^2','kind':'prime_power','prime':2,'grade':2,'log_grade':'2 log(2)'},
 {'id':'pole_2','kind':'pole','reciprocal':'pole_half'},
 {'id':'pole_half','kind':'pole','reciprocal':'pole_2'},
]

def map_source(items,collapse_grade=False,drop_pole=False,feature_offset=0):
 out=[]
 for x in items:
  if drop_pole and x['id']=='pole_half': continue
  if x['kind']=='prime_power':
   grade=1 if collapse_grade else x['grade']
   out.append({'source':x['id'],'prime':x['prime'],'grade':grade,'shell':grade,
               'ordered_pair':[x['prime'],grade],'theta_label':x['log_grade'],
               'feature':x['prime']+grade+feature_offset})
  else:
   out.append({'source':x['id'],'prime':'pole','grade':x['id'],'shell':'reciprocal',
               'ordered_pair':[x['id'],x['reciprocal']],'theta_label':x['id'],
               'feature':0+feature_offset})
 return out

def validate(mapped):
 errors=[]
 pp=[x for x in mapped if x['prime']!='pole']
 if len({(x['prime'],x['grade']) for x in pp})!=len(pp): errors.append('collapsed_prime_grade')
 poles={x['source']:x for x in mapped if x['prime']=='pole'}
 if set(poles)!={'pole_2','pole_half'}: errors.append('lost_reciprocal_pole_label')
 elif poles['pole_2']['ordered_pair'][1]!='pole_half' or poles['pole_half']['ordered_pair'][1]!='pole_2':
  errors.append('broken_reciprocal_pair')
 for x in pp:
  if x['feature']!=x['prime']+x['grade']: errors.append('noncommuting_source_feature_square');break
 return errors

baseline=validate(map_source(source))
hostile={
 'collapsed_prime_grade':validate(map_source(source,collapse_grade=True)),
 'lost_reciprocal_pole':validate(map_source(source,drop_pole=True)),
 'noncommuting_square':validate(map_source(source,feature_offset=1)),
}
assert baseline==[]
assert hostile['collapsed_prime_grade']==['collapsed_prime_grade']
assert hostile['lost_reciprocal_pole']==['lost_reciprocal_pole_label']
assert hostile['noncommuting_square']==['noncommuting_source_feature_square']
out={'schema':'marici.synthetic-zeta-g4-source-map.v1','status':'passed','contract_status':'test_fixture_only',
     'baseline_errors':baseline,'hostile_results':hostile,
     'claim_boundary':'synthetic interface conformance only; no authoritative G4 or radial identification'}
RESULT.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
