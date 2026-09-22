"""Fixed signed-refinement ladder for Nima's already frozen midpoint task."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib,copy
from flint import arb
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results';N=HERE.parents[1]/'nima'/'results'
def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
q=module('signed',HERE/'certify_signed_fixed_hat_pairing.py');t=module('task',HERE/'three_channel_source_task.py')
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bounds(d):return Q(d['lower']),Q(d['upper'])
def enc(a,b):return {'lower':str(a),'upper':str(b)}
contract={'schema':'marici.midpoint-signed-refinement-ladder.v1','task_contract_sha256':sha(N/'signed-functional-dpc-contract.json'),
 'stages':[{'N':1000000,'bits':192,'mesh_divisions':32},{'N':4000000,'bits':224,'mesh_divisions':64},{'N':16000000,'bits':256,'mesh_divisions':128}],
 'stopping_rule':'stop at first stage whose exact gain interval is wholly on one side of the frozen threshold; otherwise report UNRESOLVED after stage 3',
 'scope':'Post-DPC analytical refinement, not a rerun or rescue of its fixed-method performance prediction.'}
(R/'midpoint-signed-refinement-contract.json').write_text(json.dumps(contract,indent=2)+'\n')
dpc=load(N/'signed-functional-dpc-contract.json');task=dpc['task'];threshold=Q(dpc['threshold']);parent=t.SourceTask(R/'three-channel-source-task-calibration-theta-taylor.json');assert parent.certify(task)['status']=='UNRESOLVED'
old=load(R/'projection-resolution-conjecture-attack.json');theta=load(R/'theta-mass-refinement.json');H=bounds(old['h']);L=bounds(old['L']);X=[bounds(theta['windows'][x]['X']) for x in ('A1','B1')];mu=[bounds(theta['windows'][x]['mu']) for x in ('A1','B1')]
def gain(C):
 def e(k):return 2*X[0][k]*X[1][k]*(C[k]+H[k]*(mu[0][k]-L[1-k]))*(C[k]+H[k]*(mu[1][k]-L[1-k]))
 return e(0),e(1)
stages=[];chosen=None
for p in contract['stages']:
 C,e=q.compute(**p);cc=bounds(e['C']);g=gain(cc);status='CERTIFIED_FEASIBLE' if g[0]>=threshold else 'CERTIFIED_INFEASIBLE' if g[1]<threshold else 'UNRESOLVED'
 stages.append({'parameters':p,'C':enc(*cc),'gain':enc(*g),'prime_tail_bounds':e['prime_tail_bounds'],'status':status})
 if status!='UNRESOLVED':chosen=(p,cc,g,e,status);break
assert chosen is not None,'fixed ladder exhausted without separation'
p,cc,g,e,status=chosen
cal=copy.deepcopy(parent.cal);cal['parent_calibration_file']='three-channel-source-task-calibration-theta-taylor.json';cal['parent_calibration_sha256']=sha(R/cal['parent_calibration_file'])
for mode in ('private','reuse'):
 cal['diagonal_refinements'][mode]['positive']={'lower':[str(g[0].numerator),str(g[0].denominator)],'upper':[str(g[1].numerator),str(g[1].denominator)]}
cal['refinement_evidence']={**cal['refinement_evidence'],'method':'fixed-midpoint-signed-refinement-ladder','ladder_contract_sha256':sha(R/'midpoint-signed-refinement-contract.json'),'pairing_code_sha256':sha(HERE/'certify_signed_fixed_hat_pairing.py'),'chosen_stage':p,'C_bin_lower':[str(cc[0].numerator),str(cc[0].denominator)],'C_bin_upper':[str(cc[1].numerator),str(cc[1].denominator)]}
cp=R/'three-channel-source-task-calibration-midpoint-signed-refinement.json';cp.write_text(json.dumps(cal,indent=2)+'\n');engine=t.SourceTask(cp);result=engine.certify(task);assert result['status']==status
if status=='CERTIFIED_FEASIBLE':assert result['automatic_witness_search']['accepted']
report={'passed':True,'contract':contract,'contract_sha256':sha(R/'midpoint-signed-refinement-contract.json'),'frozen_task_sha256':sha(N/'signed-functional-dpc-contract.json'),'stages':stages,'chosen_stage':p,'threshold':str(threshold),'calibration_file':cp.name,'calibration_sha256':sha(cp),'task_result':result,
 'scope':'Same frozen midpoint task, detector, source family, theta masses, H and L. This is a new fixed refinement experiment after the DPC trial, not evidence that the original fixed N=1e6 method succeeded.'}
(R/'midpoint-signed-refinement.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'status':status,'stage':p,'gain':enc(*g)},indent=2))
