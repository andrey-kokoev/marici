"""Independent append-only transitions and cache-dependency replay."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,copy
from verify_modular_difference_interfaces import check,closure_check,digest
if not __debug__:raise RuntimeError('Assertions required')
OUT=Path(__file__).resolve().parents[1]/'results'
def dep(state,i):return digest({'source_rule':'raw-tail-caps-v1','m':state['m'],'binding':state['binding'],'block':state['blocks'][i]})
def next_archive(before,op):
    state=copy.deepcopy(before)
    assert op['kind'] in ('block-edge','public-edge') and len(op['edge'])==3
    u,v,w=op['edge'];assert type(u) is int and type(v) is int;Q(w)
    if op['kind']=='block-edge':
        assert set(op)=={'kind','block','edge'};i=op['block'];assert type(i) is int and 0<=i<len(state['blocks'])
        assert u in state['blocks'][i]['nodes'] and v in state['blocks'][i]['nodes']
        state['blocks'][i]['evidence'].append(op['edge'])
    else:
        assert set(op)=={'kind','edge'} and u in state['public'] and v in state['public']
        state['exterior'].append(op['edge'])
    return state

def archived_transition(before,op,previous,t,*,_check=check):
    assert before['retention']=='archive-backed';_check(before,previous)
    assert t['kind']=='archived-difference-refinement-v1' and t['operation']==op
    assert t['before_digest']==digest(before) and t['previous_proof_digest']==digest(previous)
    after=next_archive(before,op);changed=[op['block']] if op['kind']=='block-edge' else []
    reused=[i for i in range(len(before['blocks'])) if i not in changed]
    assert t['recomputed_blocks']==changed and t['reused_blocks']==reused
    assert t['dependencies']==[[dep(before,i),dep(after,i)] for i in range(len(before['blocks']))]
    for i in reused:
        assert dep(before,i)==dep(after,i) and t['after']['blocks'][i]==previous['blocks'][i]
    _check(after,t['after']);return after

def public_transition(before,op,t):
    assert before['retention']=='public-only' and op['kind']=='public-edge'
    assert set(op)=={'kind','edge'} and len(op['edge'])==3
    u,v,w=op['edge'];assert type(u) is int and type(v) is int and u in before['public'] and v in before['public'];Q(w)
    after=copy.deepcopy(before);after['frames'].append(op['edge'])
    assert t['kind']=='public-difference-refinement-v1' and t['before_digest']==digest(before) and t['operation']==op and t['after']==after
    D=closure_check(after['public'],after['base_summary']+after['frames'],t['closure'])
    if D is not None:
        expected=[[u,v,str(D[i][j])] for i,u in enumerate(after['public']) for j,v in enumerate(after['public']) if i!=j]
        assert t['summary']==expected
    else:assert 'summary' not in t
    return after

def main():
    cp=OUT/'incremental-difference-contract.json';rp=OUT/'incremental-difference.json';raw=(OUT/'incremental-difference-packet.json.gz').read_bytes()
    c=json.loads(cp.read_text());report=json.loads(rp.read_text())
    assert hashlib.sha256(cp.read_bytes()).hexdigest()==report['contract_sha256'] and hashlib.sha256(raw).hexdigest()==report['packet_sha256']
    for p,h in c['bindings'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    packets=json.loads(gzip.decompress(raw));assert set(packets)==set(c['plans']);count=0
    for name,plan in c['plans'].items():
        entry=packets[name];origin=plan['state'];initial=entry['initial'];base=check(origin,initial);assert base is not None
        archive=origin['retention']=='archive-backed'
        before=copy.deepcopy(origin) if archive else {'schema':'public-difference-history-v1','m':origin['m'],'binding':origin['binding'],
          'public':origin['public'],'retention':'public-only','origin_digest':digest(origin),'base_summary':base,'frames':[]}
        assert entry['initial_descriptor']==before;previous=initial
        assert len(entry['steps'])==len(plan['operations'])==len(plan['expected_statuses'])
        for op,status,step in zip(plan['operations'],plan['expected_statuses'],entry['steps']):
            t=step['transition']
            if archive:
                after=archived_transition(before,op,previous,t);check(after,step['fresh'])
                assert t['after']==step['fresh'] and t['after']['status']==status;previous=t['after']
            else:
                after=public_transition(before,op,t);fine=copy.deepcopy(origin);fine['exterior']+=after['frames']
                summary=check(fine,step['fresh']);assert step['fresh']['status']==t['closure']['status']==status
                if summary is not None:assert t['summary']==summary
            before=after;count+=1
    cycle=packets['new-cross-block-cycle']['steps'][0]['transition']['after']
    assert cycle['status']=='INCONSISTENT' and all(b['status']=='CONSISTENT' for b in cycle['blocks']) and cycle['expanded_cycle']
    # Tampering with cached dependencies is rejected even when a copied old
    # local certificate was once valid for the same block index.
    p=c['plans']['archive-8'];before=p['state'];previous=packets['archive-8']['initial'];op=p['operations'][0]
    original=packets['archive-8']['steps'][0]['transition'];rejected=[]
    for defect in ('stale-block','false-cache-hit','changed-dependency','wrong-parent','changed-operation','policy','dropped-history'):
        bad=copy.deepcopy(original)
        if defect=='stale-block':bad['after']['blocks'][0]=copy.deepcopy(previous['blocks'][0])
        if defect=='false-cache-hit':bad['reused_blocks']=[0,1];bad['recomputed_blocks']=[]
        if defect=='changed-dependency':bad['dependencies'][1][1]='foreign'
        if defect=='wrong-parent':bad['previous_proof_digest']='foreign'
        if defect=='changed-operation':bad['operation']['edge'][2]='99'
        if defect=='policy':bad['after']['state']['retention']='public-only';bad['after']['state_digest']=digest(bad['after']['state'])
        if defect=='dropped-history':bad['after']['state']['blocks'][0]['evidence'].pop(0);bad['after']['state_digest']=digest(bad['after']['state'])
        try:archived_transition(before,op,previous,bad)
        except (AssertionError,ValueError,KeyError,IndexError):rejected.append(defect)
        else:raise AssertionError('bad cache transition accepted')
    p=c['plans']['public-8'];entry=packets['public-8'];before=entry['initial_descriptor'];op=p['operations'][0]
    for defect in ('public-origin','public-policy','public-frame'):
        bad=copy.deepcopy(entry['steps'][0]['transition'])
        if defect=='public-origin':bad['after']['origin_digest']='foreign'
        if defect=='public-policy':bad['after']['retention']='archive-backed'
        if defect=='public-frame':bad['after']['frames']=[]
        try:public_transition(before,op,bad)
        except AssertionError:rejected.append(defect)
        else:raise AssertionError('bad public transition accepted')
    result={'passed':True,'transitions':count,'fresh_reference_agreements':count,'new_cross_block_cycle_verified':True,
      'attacks_rejected':rejected,'scope':'Exact dependency-bound block recomputation; arithmetic verification still replays all blocks.'}
    (OUT/'incremental-difference-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
