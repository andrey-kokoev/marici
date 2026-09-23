"""Live composition and loop laws for one-point comparison transport."""
from pathlib import Path
from uuid import uuid4
from copy import deepcopy
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/nima/checkers'))
import comparison_checkpoint_transport as transport
from atomic_fine_restoration import Vault
from continuation_coherence import root,make_path,semantic,point_query,compare,digest
from verify_fine_successor import expected_archive
OUT=ROOT/'research/voevodsky/results'
def main():
 f={'normal':['0','0','1'],'upper':'1/2'};g={'normal':['0','0','-1'],'upper':'-1/4'}
 batches={'P':[[f,g]],'Q':[[f],[g]],'R':[[g],[f]]};reports=[];rejected=[]
 for history in ('A','B'):
  for point in (['1','1'],['1/18','1/324']):
   vault=Vault();event=uuid4().hex;context=digest({'family':'owning-m4','n':18,'trial':point})
   token=vault._admit(event,context,18,history);archive=expected_archive(18,history);binding=root(archive,event,context)
   paths={name:make_path(archive,binding,bs) for name,bs in batches.items()}
   answer=point_query(semantic(archive,[f,g]),point)
   sessions={name:transport.TransportSession(vault) for name in ('direct','staged')}
   current={name:s.bootstrap(event,context,token,batches['P'],paths['P'],point,answer) for name,s in sessions.items()}
   initial={name:deepcopy(r) for name,r in current.items()};steps=[]
   def move(name,destination):
    s=sessions[name];before=current[name]
    after=s.transport(before['handle'],before['state'],token,batches[destination],paths[destination],point)
    assert before['handle']!=after['handle'] and after['answer']==answer
    current[name]=after;steps.append({'session':name,'destination':destination,'receipt':deepcopy(after)})
    return after
   original=transport.verify_point
   def trapped(*args,**kwargs):raise RuntimeError('POINT_ARITHMETIC_REPLAYED_DURING_TRANSPORT')
   transport.verify_point=trapped
   try:
    direct=move('direct','R');move('staged','Q');staged=move('staged','R')
    # Same destination semantics/path policy/root/point; handles and work differ.
    assert direct['state']==staged['state'] and direct['answer']==staged['answer']
    assert direct['handle']!=staged['handle']
    # Closed loop P -> Q -> R -> P has identity action on descriptor/result.
    loop=move('staged','P');assert loop['state']==initial['staged']['state'] and loop['answer']==initial['staged']['answer']
    identity=move('staged','P');assert identity['state']==loop['state'] and identity['answer']==loop['answer']
    # Begin a fresh two-edge route, then revoke between its edges.
    mid=move('staged','Q');vault.revoke(token);before=deepcopy(sessions['staged'].receipt())
    try:move('staged','R')
    except PermissionError:rejected.append('revoked-route')
    else:raise AssertionError('revoked authority transported')
    assert sessions['staged'].receipt()==before
    # The other route already arrived. Its old result remains mathematical
    # evidence, but authority cannot be reused for another transport either.
    before_direct=deepcopy(sessions['direct'].receipt())
    try:move('direct','P')
    except PermissionError:rejected.append('revoked-after-direct-arrival')
    else:raise AssertionError('revoked authority reused')
    assert sessions['direct'].receipt()==before_direct
   finally:transport.verify_point=original
   # Revocation changes authorization, not the fine-relation comparison.
   after_revocation=compare(archive,binding,batches['Q'],paths['Q'],batches['R'],paths['R'])
   assert after_revocation['same_fine_relation']
   for r in list(initial.values())+[step['receipt'] for step in steps]:
    original(semantic(archive,[f,g]),point,r['answer'])
   assert all(s.receipt()['work']['point_checks']==1 for s in sessions.values())
   reports.append({'history':history,'point':point,'binding':binding,'batches':batches,'paths':paths,
    'initial':initial,'steps':steps,'composition_descriptor':direct['state'],
    'loop_descriptor':loop['state'],'mathematical_comparison_after_revocation':after_revocation,
    'final_work':{name:s.receipt()['work'] for name,s in sessions.items()}})
 report={'passed':True,'cases':reports,'refusals':rejected,
 'scope':'Composition and loop laws for checked point evidence, conditional on live authority per edge. Not equality of handles, authorization histories, whole sections or physical executions.'}
 (OUT/'evidence-transport-coherence.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'passed':True,'cases':len(reports),'successful_transports':sum(len(r['steps']) for r in reports),
 'bootstrap_point_checks':8,'transport_point_checks':0,'revocation_refusals':len(rejected)},indent=2))
if __name__=='__main__':main()
