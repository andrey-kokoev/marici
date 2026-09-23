"""Fresh source-aware replay of saved allocations and missing-column control.

No continuation-session or allocation-constructor import. Offline replay has
source access; this does not grant the detached live service that capability.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results';G=ROOT/'research/grothendieck/results'
sys.path.insert(0,str(ROOT/'research/grothendieck/checkers'))
import verify_active_cap_moment_master as kernel
from moment_column_checkpoints import verify_compaction,compact,encode
if not __debug__:raise RuntimeError('Assertions required')
def replay(spec,answer,compaction,record,seeds=None):
    kernel.verify(spec,answer,seeds);columns=verify_compaction(spec,answer,compaction)
    assert record['state']==spec and record['proof_digest']==hashlib.sha256(encode(answer)).hexdigest()
    result=record['allocation'];assert result['status']==answer['status'];observations=[];local=[]
    for b,interval in enumerate(spec['intervals']):
        data=kernel.block(interval);raw=[Q(0)]*len(data[0]);mass=Q(0)
        for c,entry in zip(columns,compaction):
            if c['block']!=b:continue
            t=kernel.admitted(data,tuple(map(Q,c['potential'])),True);weight=Q(entry['weight']);mass+=weight
            raw=[x+weight*y for x,y in zip(raw,t)]
        assert mass==1;local.append(raw)
        observations.append([str(raw[0]),str(raw[-1]),str(sum(raw)),str(sum(Q(1,128**j)*v for j,v in zip(data[0],raw)))])
    assert result['block_allocations']==observations
    if answer['status']=='INCONSISTENT':
        assert all(k not in result for k in ('global_source','public_allocation','objective_value'));return
    for left,right in zip(local,local[1:]):assert left[-1]==right[0]
    glued=local[0]+[v for block in local[1:] for v in block[1:]]
    first,last=spec['intervals'][0][0],spec['intervals'][-1][1];ids=list(range(first,last+1))
    assert result['global_source']=={str(j):str(v) for j,v in zip(ids,glued)}
    data=kernel.block([first,last]);kernel.admitted(data,tuple(v/s for v,s in zip(glued,data[1])))
    observed=(glued[0],glued[-1],sum(glued),sum(Q(1,128**j)*v for j,v in zip(ids,glued)))
    assert result['public_allocation']==list(map(str,observed))
    assert Q(result['objective_value'])==Q(answer['value'])==sum(Q(a)*v for a,v in zip(spec['objective'],observed))
    assert all(sum(Q(a)*v for a,v in zip(f['normal'],observed))<=Q(f['upper']) for f in spec['frames'])
    assert all(sum(Q(a)*Q(v) for a,v in zip(f['normal'],observations[f['block']]))<=Q(f['upper']) for f in spec.get('local_frames',[]))

def main():
    report=json.loads((OUT/'allocation-continuation-checkpoint.json').read_text())
    for p,h in report['bindings'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    fixture=json.loads((G/'moment-column-checkpoints.json').read_text());r=fixture['records'][1]
    replay(r['state'],r['warm'],r['compact'],report['allocation_replay'],r['seed'])
    r=fixture['records'][-1];answer=r['cold'];cp=compact(r['state']['intervals'],answer['columns'],answer['trace'][-1]['master']['point'][:len(answer['columns'])])
    replay(r['state'],answer,cp,report['infeasible_local_replay'])
    new=report['new_query'];kernel.verify(new['expected'],new['proof'])
    assert new['receipt']['status']==new['proof']['status'] and new['receipt']['value']==new['proof'].get('value')
    assert report['detached']['capabilities']=={'replay_current_allocation':True,'new_queries':False,
      'public_refinement':False,'whole_interface_from_columns':False,'fine_restore':False}
    assert report['detached']['bytes']['attached_checkpoint']==0
    exposures=fixture['six_exposures'];data=kernel.block([0,3]);points=[];objectives=[];values=[]
    for e in exposures:
        a=tuple(map(Q,e['objective']));q=tuple(data[1][j]*(a[0]*int(j==0)+a[1]*int(j==3)+a[2]+a[3]*Q(1,128**j)) for j in range(4))
        potential,upper=kernel.verify_pricing(data,q,e['certificate']);z=potential[1:];delta=(z[0],z[1]-z[0],z[2]-z[1],z[3]-z[2])
        signs=tuple(map(Q,e['increment_objective']));assert q==(signs[0]-signs[1],signs[1]-signs[2],signs[2]-signs[3],signs[3])
        assert all(s in (-1,1) and v==(hi if s==1 else lo) for s,v,lo,hi in zip(signs,delta,(Q(0),Q(1,2),Q(1,2),Q(1,2)),(Q(1),Q(20),Q(20),Q(20))))
        points.append(z);objectives.append(q);values.append(upper)
    assert len(points)==len(set(points))==6
    restricted=max(sum(q*z for q,z in zip(objectives[-1],p)) for p in points[:5]);assert restricted<values[-1]
    assert report['restricted_support']==str(restricted) and report['true_source_support']==str(values[-1])
    result={'passed':True,'allocation_replays':2,'new_query_full_replay':True,'exposures_verified':6,
      'five_column_support':str(restricted),'source_support':str(values[-1]),
      'scope':'Independent arithmetic replay; live detachment and authority refusals are separately exercised in process.'}
    (OUT/'allocation-continuation-checkpoint-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
