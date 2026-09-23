"""Fresh path/point replay without importing the transport session.
Authority of exported root labels is not established by arithmetic replay.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from continuation_coherence import compare,verify_path,root,point_query,digest
if not __debug__:raise RuntimeError('Assertions required')
def main():
    report=json.loads((OUT/'comparison-checkpoint-transport.json').read_text())
    for p,h in report['bindings'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    f={'normal':['0','0','1'],'upper':'1/2'};g={'normal':['0','0','-1'],'upper':'-1/4'};count=0
    assert len(report['cases'])==4
    for case in report['cases']:
        archive=case['archive'];binding=case['binding'];p=case['point']
        assert archive['history']==case['history'] and binding==root(archive,binding['event'],binding['context'])
        comparison=compare(archive,binding,[[f,g]],case['direct'],[[f],[g]],case['staged'])
        permutation=compare(archive,binding,[[f],[g]],case['staged'],[[g],[f]],case['permuted'])
        assert case['staged_receipt']['comparison']==comparison and case['permuted_receipt']['comparison']==permutation
        receipts=(case['bootstrap'],case['staged_receipt'],case['permuted_receipt'])
        assert len({r['handle'] for r in receipts})==3
        for index,(name,batches,receipt) in enumerate(zip(('direct','staged','permuted'),([[f,g]],[[f],[g]],[[g],[f]]),receipts)):
            state=verify_path(archive,binding,batches,case[name]);answer=receipt['answer']
            assert answer==point_query(state,p)
            assert receipt['state']['binding']==binding and receipt['state']['path_tip']==case[name]['tip']
            assert receipt['state']['semantic_digest']==digest(state) and receipt['state']['point']==p
            assert receipt['state']['policy']=='exact-point-only/no-archive-reexposure/v1'
            if answer['admitted']:
                t=list(map(Q,answer['source_lift']));d=Q(1,128**4);h=(t[0]-50)/d
                assert len(t)==4 and all(0<=v<=100+2*j for j,v in enumerate(t)) and t[1]==51
                slopes=[Q(1,128**j) for j in range(4)];assert sum(t)==206+d*Q(p[0])
                assert sum(v*s for v,s in zip(t,slopes))==sum(v*s for v,s in zip((50,51,52,53),slopes))+d*Q(p[1])
                assert all(sum(a*b for a,b in zip(map(Q,r['normal']),(*map(Q,p),h)))<=Q(r['upper']) for r in state['fine_rows'])
            assert receipt['work']=={'point_checks':1,'point_cache_hits':index,'path_checks':1+2*index,'authority_checks':1+index}
        assert receipts[0]['answer']==receipts[1]['answer']==receipts[2]['answer'];count+=2
    assert report['transported_results']==count
    result={'passed':True,'transported_point_results_replayed':count,
      'scope':'Fresh full semantic/path and point arithmetic replay; live root authority and cache non-replay tested separately in process.'}
    (OUT/'comparison-checkpoint-transport-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
