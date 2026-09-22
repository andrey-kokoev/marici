"""Replay the fixed midpoint refinement ladder and its exact task consequence."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results';N=HERE.parents[1]/'nima'/'results'
def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
t=module('task',HERE/'three_channel_source_task.py')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bounds(x):return Q(x['lower']),Q(x['upper'])
r=json.loads((R/'midpoint-signed-refinement.json').read_text());d=json.loads((N/'signed-functional-dpc-contract.json').read_text())
assert r['passed'] and r['frozen_task_sha256']==sha(N/'signed-functional-dpc-contract.json')
assert r['contract_sha256']==sha(R/'midpoint-signed-refinement-contract.json')
assert r['contract']['stages']==[{'N':1000000,'bits':192,'mesh_divisions':32},{'N':4000000,'bits':224,'mesh_divisions':64},{'N':16000000,'bits':256,'mesh_divisions':128}]
assert r['chosen_stage']==r['contract']['stages'][-1]
threshold=Q(r['threshold']);assert threshold==Q(d['threshold'])
for stage in r['stages'][:-1]:
 lo,hi=bounds(stage['gain']);assert lo<threshold<hi and stage['status']=='UNRESOLVED'
lo,hi=bounds(r['stages'][-1]['gain']);assert lo>=threshold and r['stages'][-1]['status']=='CERTIFIED_FEASIBLE'
engine=t.SourceTask(R/r['calibration_file']);assert sha(R/r['calibration_file'])==r['calibration_sha256']
result=engine.certify(d['task']);assert result==r['task_result'] and result['status']=='CERTIFIED_FEASIBLE'
assert result['automatic_witness_search']['accepted']
assert engine.cal['refinement_evidence']['pairing_code_sha256']==sha(HERE/'certify_signed_fixed_hat_pairing.py')
assert engine.cal['refinement_evidence']['ladder_contract_sha256']==r['contract_sha256']
print('PASS: frozen midpoint, three declared stages, exact feasible witness and calibration binding')
