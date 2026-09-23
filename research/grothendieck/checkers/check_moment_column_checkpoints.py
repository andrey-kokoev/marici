"""Bounded source-column checkpoints with cold/warm independent full replay."""
from pathlib import Path
from fractions import Fraction as Q
import json,copy,hashlib
import verify_active_cap_moment_master as kernel
from active_cap_moment_master import Block,query
from moment_column_checkpoints import compact,verify_compaction,VerifierSession,encode
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
verify=kernel.verify
def solve(state,seeds=None):
 return query([Block(*v) for v in state['intervals']],[(tuple(map(Q,f['normal'])),Q(f['upper'])) for f in state['frames']],tuple(map(Q,state['objective'])),local_frames=[(f['block'],tuple(map(Q,f['normal'])),Q(f['upper'])) for f in state.get('local_frames',[])],initial_columns=seeds)
def compress(state,answer):return compact(state['intervals'],answer['columns'],answer['trace'][-1]['master']['point'][:len(answer['columns'])])
def reject(f):
 try:f()
 except (AssertionError,KeyError,IndexError):return
 raise AssertionError('invalid checkpoint accepted')
base=json.loads((R/'active-cap-moment-master-contract.json').read_text())['requests'][3]
state={'intervals':[[0,3],[3,7]],'objective':['0','0','1','0'],'frames':[]}
operations=[base['frames'][0],base['frames'][1],{'normal':['0','1','0','0'],'upper':'30'},{'normal':['-1','0','0','0'],'upper':'-3/4'}]
session=VerifierSession(verify,kernel.verify_pricing);answer=solve(state);cp=compress(state,answer);handle,receipt=session.bootstrap(state,answer,cp);records=[{'state':copy.deepcopy(state),'warm':answer,'compact':cp,'receipt':receipt}]
# Caller mutation cannot alter serialized checkpoint contents.
snapshot=session.snapshot(handle);snapshot['seeds'][0]['potential'][0]='999';assert session.snapshot(handle)['seeds'][0]['potential'][0]!='999'
original=copy.deepcopy(state);state['objective'][0]='999';assert session.snapshot(handle)['state']==original;state=original
foreign=VerifierSession(verify,kernel.verify_pricing);foreign_handle,_=foreign.bootstrap(state,answer,cp);reject(lambda:session.snapshot(foreign_handle));reject(lambda:session.snapshot({'serialized':'handle'}))
attacks=2
for operation in operations:
 old_handle=handle;before=copy.deepcopy(state);old_snapshot=session.snapshot(handle);seeds=old_snapshot['seeds'];state=copy.deepcopy(state);state['frames'].append(copy.deepcopy(operation))
 warm=solve(state,seeds);cold=solve(state);verify(state,cold);verify(state,warm,seeds)
 assert warm['status']==cold['status']
 if warm['status']=='OPTIMUM':assert warm['value']==cold['value']
 cp=compress(state,warm)
 bad=copy.deepcopy(cp);bad[0]['weight']='-1';reject(lambda:session.advance(handle,before,operation,warm,bad));assert session.snapshot(handle)==old_snapshot
 wrong=copy.deepcopy(before);wrong['intervals'][0][1]-=1;reject(lambda:session.advance(handle,wrong,operation,warm,cp))
 wrong_operation=copy.deepcopy(operation);wrong_operation['upper']=str(Q(operation['upper'])+1);reject(lambda:session.advance(handle,before,wrong_operation,warm,cp))
 corrupted=copy.deepcopy(warm);corrupted['trace'][-1]['pricing'][0]['certificate']['flow'][0]='-1';reject(lambda:session.advance(handle,before,operation,corrupted,cp));assert session.snapshot(handle)==old_snapshot
 handle,receipt=session.advance(handle,before,operation,warm,cp);reject(lambda:session.snapshot(old_handle));attacks+=5
 records.append({'state':copy.deepcopy(state),'operation':operation,'seed':seeds,'warm':warm,'cold':cold,'compact':cp,'receipt':receipt})
 print(len(records)-1,'warm/cold solves',len(warm['trace']),len(cold['trace']),'retained',receipt['retained_columns'],flush=True)
# Force an actual affine-dependence elimination, not just zero-weight pruning.
block=Block(0,3);columns=[]
for bits in range(8):
 z=[Q(bits&1)];z.append(z[-1]+Q(1,2)+Q((bits>>1)&1));z.append(z[-1]+Q(1,2)+Q((bits>>2)&1));z.append(z[-1]+Q(1,2))
 columns.append({'block':0,'potential':list(map(str,z))})
weights=['1/8']*8;cp=compact([[0,3]],columns,weights);assert len(cp)<=5
stub={'columns':columns,'trace':[{'master':{'point':weights}}]};verify_compaction({'intervals':[[0,3]]},stub,cp)
# These control columns are also checked against the original source graph.
for c in columns:
 p=(Q(0),*map(Q,c['potential']));assert all(p[v]-p[u]<=w for u,v,w in block.edges)
bad=copy.deepcopy(cp);bad[0]['weight']=str(Q(bad[0]['weight'])+Q(1,8));reject(lambda:verify_compaction({'intervals':[[0,3]]},stub,bad));attacks+=1
# Six uniquely exposed feasible corners refute full-interface coverage by
# any fixed five-source-column dictionary, even in the four-atom block.
exposures=[]
for base_value in (Q(0),Q(1)):
 for d1,d2 in ((Q(1,2),Q(1,2)),(Q(20),Q(1,2)),(Q(1,2),Q(20))):
  delta=(base_value,d1,d2,Q(1,2));signs=tuple(Q(1 if v==upper else -1) for v,upper in zip(delta,(Q(1),Q(20),Q(20),Q(20))));q=(signs[0]-signs[1],signs[1]-signs[2],signs[2]-signs[3],signs[3])
  av=(q[1]/block.s[1]-q[2]/block.s[2])/(block.r[1]-block.r[2]);au=q[1]/block.s[1]-av*block.r[1];a=(q[0]/block.s[0]-au-av*block.r[0],q[3]/block.s[3]-au-av*block.r[3],au,av)
  z,proof=block.price(a);expected=tuple(sum(delta[:i+1]) for i in range(4));assert z==expected
  assert Q(proof['value'])==sum(c*v for c,v in zip(signs,delta))
  # Independent source-row and node-balance checks, not optimizer agreement.
  p=(Q(0),*z);f=tuple(map(Q,proof['flow']));balance=[Q(0)]*5;edges=kernel.block([0,3])[2]
  assert tuple(Q(1+j%3)*(a[0]*int(j==0)+a[1]*int(j==3)+a[2]+a[3]*Q(1,128**j)) for j in range(4))==q
  assert len(f)==len(edges) and all(v>=0 for v in f) and all(p[v]-p[u]<=w for u,v,w in edges)
  for weight,(u,v,w) in zip(f,edges):balance[v]+=weight;balance[u]-=weight
  assert tuple(balance)==(-sum(q),*q) and sum(weight*w for weight,(u,v,w) in zip(f,edges))==Q(proof['value'])
  exposures.append({'increments':list(map(str,delta)),'increment_objective':list(map(str,signs)),'objective':list(map(str,a)),'certificate':proof})
assert len({tuple(e['certificate']['potential']) for e in exposures})==6
report={'schema':'moment-column-checkpoints.v1','operations':operations,'records':records,'six_exposures':exposures,'dense_compaction':{'columns':columns,'weights':weights,'compact':cp},'counts':{'transitions':4,'rejections':attacks,'maximum_retained_columns':max(r['receipt']['retained_columns'] for r in records),'warm_successor_master_checks':sum(len(r['warm']['trace']) for r in records[1:]),'cold_successor_master_checks':sum(len(r['cold']['trace']) for r in records[1:]),'max_checkpoint_bytes':max(r['receipt']['checkpoint_bytes'] for r in records),'successor_local_checks':sum(r['receipt']['local_checks'] for r in records[1:]),'successor_local_hits':sum(r['receipt']['local_hits'] for r in records[1:]),'full_warm_pricing_checks':sum(r['receipt']['pricing_proofs_presented'] for r in records[1:]),'predecessor_hits':sum(r['receipt']['predecessor_hits'] for r in records[1:]),'within_candidate_hits':sum(r['receipt']['within_candidate_hits'] for r in records[1:])},'bindings':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),HERE/'moment_column_checkpoints.py',HERE/'active_cap_moment_master.py',HERE/'verify_active_cap_moment_master.py')}}
(R/'moment-column-checkpoints.json').write_bytes(encode(report));print('PASS',report['counts'])
