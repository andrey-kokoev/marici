"""Frozen persistent-evidence controls for coherent finite decision witnesses."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,copy
import coherent_tail_refinement as e
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
# Declare scenarios before running any optimization. These are analytical
# controls, NOT frames claiming truth about the actual prime source.
contract={'schema':'coherent-tail-refinement-controls.v1','context':e.CONTEXT,'threshold':'-3/8','scenarios':{
 'separation':[[e.row({1:1},0)],[e.row({2:1},0)]],
 'witness_switching':[[e.row({1:1},0)],[e.row({1:-1},-1)]],
 'noncommitted_optimizer':[[e.row({1:1,2:1},1)],[e.row({1:1},0)]],
 'future_coordinate':[[e.row({1:1},0)],[e.row({17:-1},-1)]]},
 'equality_boundary':'For all n accept x_n<=0; limit infimum equals 0, but every finite prefix has infimum -2^-m. No strict-margin theorem applies.',
 'scope':'Synthetic rational carrier with exact uniform tails; not an actual prime-calibration update adapter.'}
cp=R/'coherent-tail-refinement-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n')
scenarios={}
for name,sequence in contract['scenarios'].items():
 state=e.genesis();stages=[{'state':state,'result':e.evaluate(state,Q(contract['threshold']))}]
 for i,rows in enumerate(sequence):
  f=e.frame(state,f'{name}:{i+1}',rows);state=e.append(state,f)
  stages.append({'state':state,'result':e.evaluate(state,Q(contract['threshold']))})
 scenarios[name]=stages
isolated=[]
for rows in contract['scenarios']['witness_switching']:
 state=e.genesis();state=e.append(state,e.frame(state,'isolated',rows));isolated.append({'state':state,'result':e.evaluate(state,Q(contract['threshold']))})
assert all(s['result']['status']!='EVIDENCE_CONSISTENCY_FAILURE' for s in isolated)
assert scenarios['witness_switching'][-1]['result']['status']=='EVIDENCE_CONSISTENCY_FAILURE'
assert scenarios['separation'][-1]['result']['status']=='UNIVERSAL_THRESHOLD_SEPARATION'
# Equality at the limiting threshold is a genuine boundary, not a failure.
state=e.genesis();boundary=[]
for n in range(1,9):
 state=e.append(state,e.frame(state,f'zero:{n}',[e.row({n:1},0)]));result=e.evaluate(state,Q(0))
 assert Q(result['infinite_optimum'])==-Q(1,2**n)
 boundary.append({'state':state,'result':result})
rejections=[]
base=e.genesis();f=e.frame(base,'good',[e.row({1:1},0)]);state=e.append(base,f)
for kind,bad in [('foreign',dict(f,context='foreign')),('stale_parent',f)]:
 try:e.append(state,bad)
 except ValueError:rejections.append(kind)
 else:raise AssertionError('invalid frame accepted')
# Reversing constraint arrival is equivalent as a set, but not the same
# lineage hash. This checks constraint composition without resetting fibers.
state2=e.genesis()
for i,rows in enumerate(reversed(contract['scenarios']['separation'])):state2=e.append(state2,e.frame(state2,f'reversed:{i}',rows))
reverse={'state':state2,'result':e.evaluate(state2,Q(contract['threshold']))}
assert reverse['result']['infinite_optimum']==scenarios['separation'][-1]['result']['infinite_optimum']
reset=e.genesis();reset=e.append(reset,e.frame(reset,'reset-second-only',contract['scenarios']['separation'][1]));reset_packet={'state':reset,'result':e.evaluate(reset,Q(contract['threshold']))}
out={'schema':'coherent-tail-refinement.v1','reset_second_frame':reset_packet,'contract_sha256':sha(cp),'scenarios':scenarios,'isolated_switch_frames':isolated,'equality_boundary':boundary,'reverse_separation':reverse,'rejected_frames':rejections,'bindings':{str(p):sha(p) for p in (Path(__file__),HERE/'coherent_tail_refinement.py',cp)}}
(R/'coherent-tail-refinement.json').write_text(json.dumps(out,indent=2)+'\n');print('Constructed persistent-frame packets, finite separator and Farkas inconsistency witness.')
