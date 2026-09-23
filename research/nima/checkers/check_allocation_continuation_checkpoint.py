"""Source detachment preserves one allocation, not new-query capability."""
from pathlib import Path
from fractions import Fraction as Q
import copy,json,hashlib
from allocation_continuation_checkpoint import AllocationSession,kernel,allocation
from moment_column_checkpoints import compact,encode
from active_cap_moment_master import Block,query
ROOT=Path(__file__).resolve().parents[3];G=ROOT/'research/grothendieck/results';OUT=ROOT/'research/nima/results'
def main():
    path=G/'moment-column-checkpoints.json';fixture=json.loads(path.read_text())
    for p,h in fixture['bindings'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    records=fixture['records'];first,next_record=records[:2];session=AllocationSession()
    boot=session.bootstrap(first['state'],first['warm'],first['compact'])
    replay=session.replay_allocation(boot['handle']);assert replay['allocation']['objective_value']==first['warm']['value']
    # A new query with attached source access requires full source/pricing
    # verification; it is not answered by optimizing over retained columns.
    fresh=session.check_new_query(boot['handle'],first['state'],first['warm']);assert fresh['status']=='OPTIMUM'
    advanced=session.advance(boot['handle'],first['state'],next_record['operation'],next_record['warm'],next_record['compact'])
    before=session.replay_allocation(advanced['handle']);snapshot=session.receipt()
    new_query=copy.deepcopy(next_record['state']);new_query['objective']=['1','0','0','0']
    new_answer=query([Block(*interval) for interval in new_query['intervals']],
      [(tuple(map(Q,f['normal'])),Q(f['upper'])) for f in new_query['frames']],tuple(map(Q,new_query['objective'])))
    query_receipt=session.check_new_query(advanced['handle'],new_query,new_answer)
    assert session.replay_allocation(advanced['handle'])==before
    detached=session.detach(advanced['handle'],advanced['state']);assert detached['bytes']['attached_checkpoint']==0
    assert session._engine is None and session._engine_handle is None
    rejected=[]
    def reject(name,action):
        try:action()
        except (AssertionError,ValueError,PermissionError,KeyError):rejected.append(name)
        else:raise AssertionError(name+' accepted')
    # Spy on all source arithmetic entrypoints: replay must need none of them,
    # and forbidden continuations must refuse before trying to call them.
    names=('verify','verify_pricing','block','admitted');originals={name:getattr(kernel,name) for name in names}
    def forbidden(*args,**kwargs):raise RuntimeError('DETACHED_SOURCE_WAS_ACCESSED')
    try:
        for name in names:setattr(kernel,name,forbidden)
        after=session.replay_allocation(detached['handle']);assert after==before
        reject('new-query-after-detach',lambda:session.check_new_query(detached['handle'],new_query,new_answer))
        r=records[2]
        reject('public-refinement-after-detach',lambda:session.advance(detached['handle'],next_record['state'],r['operation'],r['warm'],r['compact']))
        reject('stale-attached-head',lambda:session.replay_allocation(advanced['handle']))
        reject('serialized-checkpoint',lambda:session.replay_allocation({'handle':detached['handle'],'checked':True}))
        for name,claim in (('columns-as-history',before['allocation']),('archive-shaped-claim',{'histories':['A','B']}),('self-asserted-owner',{'issuer':'owner','history':'A'})):
            reject(name,lambda:session.restore_fine(detached['handle'],claim))
        mutated=session.receipt();mutated['capabilities']['new_queries']=True;mutated['state']['objective'][0]='999'
        altered=session.replay_allocation(detached['handle']);altered['allocation']['block_allocations'][0][0]='999'
        assert session.replay_allocation(detached['handle'])==before
        assert session.receipt()==detached
    finally:
        for name,fn in originals.items():setattr(kernel,name,fn)
    # An infeasible Phase-I allocation is local data, not a glued source lift.
    last=records[-1];answer=last['cold']
    cp=compact(last['state']['intervals'],answer['columns'],answer['trace'][-1]['master']['point'][:len(answer['columns'])])
    empty=AllocationSession();h=empty.bootstrap(last['state'],answer,cp);off=empty.detach(h['handle'],h['state'])
    local=empty.replay_allocation(off['handle'])
    assert local['allocation']['status']=='INCONSISTENT' and 'global_source' not in local['allocation']
    # Independently replay all six pricing proofs and their exposing forms.
    exposures=fixture['six_exposures'];data=kernel.block([0,3]);checked=[]
    for e in exposures:
        a=tuple(map(Q,e['objective']));s=data[1]
        q=tuple(s[j]*(a[0]*int(j==0)+a[1]*int(j==3)+a[2]+a[3]*Q(1,128**j)) for j in range(4))
        p,upper=kernel.verify_pricing(data,q,e['certificate']);z=p[1:]
        increments=(z[0],z[1]-z[0],z[2]-z[1],z[3]-z[2]);assert list(map(str,increments))==e['increments']
        signs=tuple(map(Q,e['increment_objective']));lower=(Q(0),Q(1,2),Q(1,2),Q(1,2));upper_box=(Q(1),Q(20),Q(20),Q(20))
        assert all(sign in (-1,1) and v==(hi if sign==1 else lo) for sign,v,lo,hi in zip(signs,increments,lower,upper_box))
        assert q==(signs[0]-signs[1],signs[1]-signs[2],signs[2]-signs[3],signs[3])
        checked.append({'source':list(map(str,z)),'objective':list(map(str,a)),'support':str(upper)})
    assert len(checked)==6 and len({tuple(e['source']) for e in checked})==6
    dictionary=checked[:5];missing=checked[5];a=tuple(map(Q,missing['objective']))
    def score(z):
        raw=[Q(1+j%3)*Q(v) for j,v in enumerate(z)]
        observation=(raw[0],raw[-1],sum(raw),sum(Q(1,128**j)*v for j,v in enumerate(raw)))
        return sum(x*y for x,y in zip(a,observation))
    restricted=max(score(e['source']) for e in dictionary);true_support=Q(missing['support']);assert restricted<true_support
    report={'passed':True,'attached':snapshot,'detached':detached,'allocation_replay':after,
      'new_query':{'expected':new_query,'proof':new_answer,'receipt':query_receipt},
      'infeasible_local_replay':local,'source_entrypoints_disabled_during_replay':list(names),
      'six_exposures_verified':6,'dictionary_columns':5,'restricted_support':str(restricted),'true_source_support':str(true_support),
      'missed_exposure':missing,'rejections':rejected,'identity_authority':'NOT_INTEGRATED',
      'bindings':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),Path(__file__).with_name('allocation_continuation_checkpoint.py'),path,
        ROOT/'research/grothendieck/checkers/verify_active_cap_moment_master.py',ROOT/'research/grothendieck/checkers/moment_column_checkpoints.py')},
      'scope':'Process-local allocation replay after logical backend detachment; not erasure of mathematically reconstructible source rules.'}
    (OUT/'allocation-continuation-checkpoint.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('passed','six_exposures_verified','dictionary_columns','restricted_support','true_source_support','rejections')},indent=2))
if __name__=='__main__':main()
