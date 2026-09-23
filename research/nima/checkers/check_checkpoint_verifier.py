"""Full-replay reference, cache work accounting, and checkpoint attacks."""
from pathlib import Path
import copy,gzip,hashlib,json
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier
from checkpoint_verifier import VerifierSession,encode
from verify_modular_difference_interfaces import check as difference_check,digest
from verify_balanced_gain_adapter import check as gain_check
from verify_incremental_difference_interfaces import archived_transition
from verify_incremental_gain_interfaces import transition as gain_transition
from incremental_difference_interfaces import ArchivedHistory
if not __debug__:raise RuntimeError('Assertions required')
OUT=Path(__file__).resolve().parents[1]/'results'

def load(stem):
    cp=OUT/(stem+'-contract.json');pp=OUT/(stem+'-packet.json.gz');rp=OUT/(stem+'.json')
    c=json.loads(cp.read_text());r=json.loads(rp.read_text());raw=pp.read_bytes()
    assert hashlib.sha256(cp.read_bytes()).hexdigest()==r['contract_sha256'] and hashlib.sha256(raw).hexdigest()==r['packet_sha256']
    for p,h in c['bindings'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    return c,json.loads(gzip.decompress(raw))

def main():
    workloads=[];sources={}
    for kind,stem in (('difference','incremental-difference'),('gain','incremental-gain')):
        c,packets=load(stem);sources[kind]=(c,packets)
        for name,plan in c['plans'].items():
            if plan['state']['retention']!='archive-backed':continue
            workloads.append((kind,name,plan['state'],packets[name]['initial'],plan['operations'],
                              [s['transition'] for s in packets[name]['steps']]))
    # Exercise reuse of a checked local negative cycle (cached result None),
    # not only consistent local matrices and cross-block contradictions.
    state=sources['difference'][0]['plans']['archive-4']['state'];history=ArchivedHistory.create(state)
    initial=history.certificate();ops=[{'kind':'block-edge','block':0,'edge':[1,1,'-1']},
                                     {'kind':'public-edge','edge':[0,1,'100']}]
    next_history,t1=history.refine_block(0,ops[0]['edge']);_,t2=next_history.refine_public(ops[1]['edge'])
    workloads.append(('difference','local-negative-cycle',state,initial,ops,[t1,t2]))
    traces=[];rejected=[]
    for kind,name,state,initial,ops,transitions in workloads:
        session=VerifierSession();receipt=session.bootstrap(kind,state,initial)
        checker=difference_check if kind=='difference' else gain_check
        assert receipt['result']==json.loads(encode(checker(state,initial)))
        trace={'language':kind,'plan':name,'bootstrap':{k:v for k,v in receipt.items() if k!='handle'},'updates':[]}
        before=state;previous=initial
        for index,(op,t) in enumerate(zip(ops,transitions)):
            old_handle=receipt['handle']
            after=(archived_transition(before,op,previous,t) if kind=='difference' else gain_transition(before,op,previous,t))
            receipt=session.advance(old_handle,before,op,t)
            assert receipt['result']==json.loads(encode(checker(after,t['after'])))
            assert receipt['status']==t['after']['status'] and receipt['state_digest']==digest(after)
            trace['updates'].append({k:v for k,v in receipt.items() if k!='handle'})
            try:session.advance(old_handle,before,op,t)
            except ValueError:pass
            else:raise AssertionError('stale checkpoint replay accepted')
            before=after;previous=t['after']
        if name=='local-negative-cycle':
            assert trace['updates'][1]['work']['local_hits']==2
            assert all(r['work']['interface_checks']==0 for r in trace['updates'])
        traces.append(trace)
    # Each failed candidate must leave the old head usable for a valid update.
    dc,dp=sources['difference'];gc,gp=sources['gain']
    cases=[('difference',dc['plans']['archive-8']['state'],dp['archive-8']['initial'],
            dc['plans']['archive-8']['operations'][0],dp['archive-8']['steps'][0]['transition']),
           ('gain',gc['plans']['component-join']['state'],gp['component-join']['initial'],
            gc['plans']['component-join']['operations'][0],gp['component-join']['steps'][0]['transition'])]
    for kind,before,previous,op,original in cases:
        for defect in ('foreign-handle','wrong-before','wrong-parent','changed-boundary','changed-policy','reused-proof','false-hit','interface-proof'):
            session=VerifierSession();head=session.bootstrap(kind,before,previous);handle=head['handle']
            bad=copy.deepcopy(original);expected=copy.deepcopy(before)
            if defect=='foreign-handle':
                other=VerifierSession();handle=other.bootstrap(kind,before,previous)['handle']
            if defect=='wrong-before':expected['binding']='foreign'
            if defect=='wrong-parent':bad['previous_proof_digest']='foreign'
            if defect=='changed-boundary':bad['after']['state']['blocks'][1]['boundary'].pop();bad['after']['state_digest']=digest(bad['after']['state'])
            if defect=='changed-policy':bad['after']['state']['retention']='public-only';bad['after']['state_digest']=digest(bad['after']['state'])
            normalized=bad['after'] if kind=='difference' else bad['after']['normalized']
            if defect=='reused-proof':normalized['blocks'][1]['paths'][0][1]=[]
            if defect=='false-hit':bad['recomputed_blocks']=[];bad['reused_blocks']=[0,1]
            if defect=='interface-proof':normalized['composed']['paths'][0][1]=[]
            try:session.advance(handle,expected,op,bad)
            except (AssertionError,ValueError,KeyError,IndexError):rejected.append(kind+':'+defect)
            else:raise AssertionError('invalid checkpoint transition accepted')
            session.advance(head['handle'],before,op,original)
    # A chart join invalidates an untouched raw block; old proof bytes must
    # not make it a cache hit under the changed normalized caps/scales.
    before=gp['component-join']['steps'][0]['transition']['after']['state'];previous=gp['component-join']['steps'][0]['transition']['after']
    op=gc['plans']['component-join']['operations'][1];original=gp['component-join']['steps'][1]['transition']
    for defect in ('stale-chart-proof','altered-scales'):
        session=VerifierSession();head=session.bootstrap('gain',before,previous);bad=copy.deepcopy(original)
        if defect=='stale-chart-proof':bad['after']['normalized']['blocks'][0]=copy.deepcopy(previous['normalized']['blocks'][0])
        else:bad['after']['scales']=copy.deepcopy(previous['scales'])
        try:session.advance(head['handle'],before,op,bad)
        except (AssertionError,ValueError,KeyError,IndexError):rejected.append('gain:'+defect)
        else:raise AssertionError('stale chart trusted')
        valid=session.advance(head['handle'],before,op,original)
        assert valid['work']['local_hits']==0 and valid['work']['local_checks']==2
    # Expanded contradiction evidence is checked even when local arithmetic
    # has been reused and the composed negative cycle itself is valid.
    before=dc['plans']['new-cross-block-cycle']['state'];previous=dp['new-cross-block-cycle']['initial']
    op=dc['plans']['new-cross-block-cycle']['operations'][0];original=dp['new-cross-block-cycle']['steps'][0]['transition']
    session=VerifierSession();head=session.bootstrap('difference',before,previous);bad=copy.deepcopy(original);bad['after']['expanded_cycle']=[]
    try:session.advance(head['handle'],before,op,bad)
    except AssertionError:rejected.append('difference:expanded-cycle')
    else:raise AssertionError('bad cycle expansion accepted')
    session.advance(head['handle'],before,op,original)
    public=copy.deepcopy(before);public['retention']='public-only'
    try:VerifierSession().bootstrap('difference',public,previous)
    except PermissionError:rejected.append('public-only-checkpoint')
    else:raise AssertionError('fine update authority inferred')
    kind,before,previous,op,original=cases[0]
    session=VerifierSession();mutable_state=copy.deepcopy(before);mutable_proof=copy.deepcopy(previous)
    head=session.bootstrap(kind,mutable_state,mutable_proof);handle=head['handle']
    mutable_state['binding']='foreign';mutable_proof['blocks'][0]['distance'][0][1]='999'
    head['result']=['forged'];head['proof_digest']='foreign'
    session.advance(handle,before,op,original)
    session=VerifierSession();head=session.bootstrap(kind,before,previous);barrier=Barrier(2)
    def racing_update(_):
        barrier.wait()
        try:session.advance(head['handle'],before,op,original)
        except ValueError:return 'stale'
        return 'accepted'
    with ThreadPoolExecutor(max_workers=2) as pool:assert sorted(pool.map(racing_update,range(2)))==['accepted','stale']
    updates=[r for t in traces for r in t['updates']];bootstraps=[t['bootstrap'] for t in traces]
    result={'passed':True,'plans':len(traces),'transitions':len(updates),'full_replay_agreements':len(updates),
      'snapshot_isolation_checked':True,'concurrent_head_advance_atomic':True,
      'bootstrap_local_checks':sum(r['work']['local_checks'] for r in bootstraps),
      'update_local_checks':sum(r['work']['local_checks'] for r in updates),
      'update_local_hits':sum(r['work']['local_hits'] for r in updates),
      'update_interface_checks':sum(r['work']['interface_checks'] for r in updates),
      'update_chart_or_rejection_checks':sum(r['work']['chart_checks'] for r in updates),
      'full_successor_local_checks':sum(r['work']['local_checks']+r['work']['local_hits'] for r in updates),
      'max_checkpoint_encoded_bytes':max(r['checkpoint_encoded_bytes'] for r in updates+bootstraps),
      'update_hashed_local_proof_bytes':sum(r['work']['hashed_local_proof_bytes'] for r in updates),
      'stale_checkpoint_replays_rejected':len(updates),'attacks_rejected':rejected,
      'scope':'Process-local, linear archive checkpoints; only local arithmetic memoized; no import or cross-process trust.'}
    bindings={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_name('checkpoint_verifier.py'),
      *[Path(__file__).with_name(n) for n in ('verify_modular_difference_interfaces.py','verify_balanced_gain_adapter.py',
         'verify_incremental_difference_interfaces.py','verify_incremental_gain_interfaces.py')]]}
    inputs={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for stem in ('incremental-difference','incremental-gain')
      for p in (OUT/(stem+'-contract.json'),OUT/(stem+'-packet.json.gz'))}
    (OUT/'checkpoint-verification-trace.json').write_text(json.dumps({'bindings':bindings,'inputs':inputs,'traces':traces},indent=2)+'\n')
    (OUT/'checkpoint-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
