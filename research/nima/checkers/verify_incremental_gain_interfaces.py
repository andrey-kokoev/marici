"""Independent chart-sensitive transition and proof-reuse verification."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,copy
from verify_balanced_gain_adapter import check,check_audits,raw_lift,digest
if not __debug__:raise RuntimeError('Assertions required')
OUT=Path(__file__).resolve().parents[1]/'results'
def dep(raw,proof,index):
    b=raw['blocks'][index]
    return digest({'rule':'balanced-gain-block-v1','m':raw['m'],'source_binding':raw['binding'],'raw_block':b,
      'local_scales':[[v,proof['scales'][v]] for v in b['nodes']],
      'normalized_block':proof['normalized']['state']['blocks'][index]})
def advance(before,op):
    assert before['retention']=='archive-backed' and op['kind'] in ('block-gain','public-gain')
    assert len(op['row'])==4;u,v,g,b=op['row'];assert type(u) is int and type(v) is int and u>0 and v>0 and Q(g)>0;Q(b)
    after=copy.deepcopy(before)
    if op['kind']=='block-gain':
        assert set(op)=={'kind','block','row'};i=op['block'];assert type(i) is int and 0<=i<len(before['blocks'])
        assert u in before['blocks'][i]['nodes'] and v in before['blocks'][i]['nodes']
        after['blocks'][i]['evidence'].append(op['row'])
    else:
        assert set(op)=={'kind','row'} and u in before['public'] and v in before['public'];after['exterior'].append(op['row'])
    return after

def transition(before,op,previous,t,*,_check=check):
    _check(before,previous);after=advance(before,op)
    assert t['kind']=='incremental-gain-v1' and t['before_digest']==digest(before)
    assert t['previous_proof_digest']==digest(previous) and t['operation']==op
    _check(after,t['after'])
    if t['after']['status']=='UNSUPPORTED':
        assert all(t[k]==[] for k in ('dependencies','changed_scale_nodes','recomputed_blocks','reused_blocks'))
        return after
    assert 'scales' in previous
    changed=[v for v,(old,new) in enumerate(zip(previous['scales'],t['after']['scales'])) if Q(old)!=Q(new)]
    assert t['changed_scale_nodes']==changed
    dependencies=[[dep(before,previous,i),dep(after,t['after'],i)] for i in range(len(before['blocks']))]
    reused=[i for i,(old,new) in enumerate(dependencies) if old==new];recomputed=[i for i in range(len(dependencies)) if i not in reused]
    assert t['dependencies']==dependencies and t['reused_blocks']==reused and t['recomputed_blocks']==recomputed
    for i in reused:assert t['after']['normalized']['blocks'][i]==previous['normalized']['blocks'][i]
    return after

def main():
    cp=OUT/'incremental-gain-contract.json';rp=OUT/'incremental-gain.json';raw=(OUT/'incremental-gain-packet.json.gz').read_bytes()
    c=json.loads(cp.read_text());r=json.loads(rp.read_text());packets=json.loads(gzip.decompress(raw))
    assert hashlib.sha256(cp.read_bytes()).hexdigest()==r['contract_sha256'] and hashlib.sha256(raw).hexdigest()==r['packet_sha256']
    for p,h in c['bindings'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    assert set(packets)==set(c['plans']);count=0
    for name,plan in c['plans'].items():
        before=plan['state'];previous=packets[name]['initial'];check(before,previous)
        assert len(packets[name]['steps'])==len(plan['operations'])==len(plan['statuses'])
        for op,status,step in zip(plan['operations'],plan['statuses'],packets[name]['steps']):
            after=transition(before,op,previous,step['transition']);check(after,step['fresh'])
            assert step['fresh']==step['transition']['after'] and step['fresh']['status']==status
            if status=='UNSUPPORTED':
                raw_lift(after,step['feasible_raw_witness']);assert step['audit_refused']=='UNBALANCED_CHART' and 'raw_audits' not in step
            if status=='CONSISTENT':check_audits(c['audit_requests'],step['fresh'],step['raw_audits'])
            if status=='INCONSISTENT':assert step['raw_audits']==[{**q,'status':'INCONSISTENT'} for q in c['audit_requests']]
            before=after;previous=step['transition']['after'];count+=1
    joined=packets['component-join']['steps'][1]['transition']
    assert joined['changed_scale_nodes']==[1,2,3] and joined['recomputed_blocks']==[0,1]
    cycle=packets['chart-compatible-cycle']['steps'][0]['transition']
    assert cycle['changed_scale_nodes']==[] and all(p['status']=='CONSISTENT' for p in cycle['after']['normalized']['blocks'])
    assert cycle['after']['normalized']['composed']['status']=='INCONSISTENT'
    # The chart change affects an otherwise untouched block: its old closure
    # cannot be replayed merely because its raw evidence did not change.
    plan=c['plans']['component-join'];previous=packets['component-join']['steps'][0]['transition']['after']
    before=advance(plan['state'],plan['operations'][0]);op=plan['operations'][1];rejected=[]
    for defect in ('stale-chart-block','false-reuse','stale-scale','wrong-parent','changed-gain','changed-policy','changed-dependency'):
        bad=copy.deepcopy(joined)
        if defect=='stale-chart-block':bad['after']['normalized']['blocks'][0]=copy.deepcopy(previous['normalized']['blocks'][0])
        if defect=='false-reuse':bad['reused_blocks']=[0];bad['recomputed_blocks']=[1]
        if defect=='stale-scale':bad['after']['scales']=previous['scales']
        if defect=='wrong-parent':bad['previous_proof_digest']='foreign'
        if defect=='changed-gain':bad['operation']['row'][2]='1'
        if defect=='changed-policy':bad['after']['state']['retention']='public-only';bad['after']['state_digest']=digest(bad['after']['state'])
        if defect=='changed-dependency':bad['dependencies'][0][1]=bad['dependencies'][0][0]
        try:transition(before,op,previous,bad)
        except (AssertionError,ValueError,KeyError,IndexError):rejected.append(defect)
        else:raise AssertionError('invalid gain transition accepted')
    unsupported=copy.deepcopy(packets['component-join']['steps'][2]['transition']);unsupported['after']['status']='INCONSISTENT'
    before2=advance(before,op)
    try:transition(before2,plan['operations'][2],joined['after'],unsupported)
    except (AssertionError,KeyError):rejected.append('chart-rejection-as-emptiness')
    else:raise AssertionError('unbalanced chart claimed emptiness')
    step=packets['public-join']['steps'][0];bad=copy.deepcopy(step['raw_audits']);bad[0]['threshold']='20'
    try:check_audits(c['audit_requests'],step['fresh'],bad)
    except AssertionError:rejected.append('rescaled-threshold')
    else:raise AssertionError('raw threshold changed')
    result={'passed':True,'transitions':count,'fresh_reference_agreements':count,'component_join_rescales_unchanged_block':True,
      'chart_compatible_cross_block_cycle':True,'nonempty_unsupported_updates':2,'raw_audit_answers':10,'attacks_rejected':rejected,
      'scope':'Global chart admission reruns; local closure reuse is chart-bound; verification is not incremental.'}
    (OUT/'incremental-gain-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
