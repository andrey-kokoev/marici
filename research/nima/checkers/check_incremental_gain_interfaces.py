"""Chart-compatible append, component reconciliation, and chart rejection."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,copy
from incremental_gain_interfaces import GainHistory
from balanced_gain_adapter import compile_gain
OUT=Path(__file__).resolve().parents[1]/'results'
def main():
    base={'m':6,'binding':'owning-raw-tail-box-v1','retention':'archive-backed','public':[0,1,6],
      'blocks':[{'nodes':[0,1,2,3],'boundary':[0,1,3],'evidence':[[1,2,'2','4'],[2,3,'1/2','3']]},
                {'nodes':[0,3,4,5,6],'boundary':[0,3,6],'evidence':[[4,5,'3','6'],[5,6,'1/3','2']]}],'exterior':[]}
    prior=json.loads((OUT/'balanced-gain-adapter-contract.json').read_text())['states']['balanced-inconsistent']
    cycle=copy.deepcopy(prior);cycle['blocks'][1]['evidence'][0][3]='0'
    plans={'component-join':{'state':base,'operations':[
      {'kind':'block-gain','block':0,'row':[1,3,'1','2']},
      {'kind':'block-gain','block':1,'row':[3,4,'1/2','4']},
      {'kind':'block-gain','block':0,'row':[1,3,'2','2']},
      {'kind':'block-gain','block':1,'row':[4,6,'1','3']}],
      'statuses':['CONSISTENT','CONSISTENT','UNSUPPORTED','UNSUPPORTED']},
      'chart-compatible-cycle':{'state':cycle,'operations':[
      {'kind':'block-gain','block':1,'row':[3,4,'2','-2']},
      {'kind':'block-gain','block':0,'row':[1,3,'1/2','10']}],
      'statuses':['INCONSISTENT','INCONSISTENT']}}
    # Public gain rows are also admitted only on exposed raw endpoints.
    plans['public-join']={'state':base,'operations':[{'kind':'public-gain','row':[1,6,'1/2','4']}], 'statuses':['CONSISTENT']}
    bindings={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in
      (Path(__file__).with_name('incremental_gain_interfaces.py'),Path(__file__).with_name('balanced_gain_adapter.py'),Path(__file__).with_name('modular_difference_interfaces.py'))}
    contract={'plans':plans,'bindings':bindings,'audit_requests':[{'node':1,'threshold':h} for h in ('40','100')],
      'scope':'Archive-backed raw gains; fresh global chart admission with dependency-bound local closure reuse.'}
    cp=OUT/'incremental-gain-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n')
    packets={};reused=recomputed=0
    for name,plan in plans.items():
        runtime=GainHistory.create(plan['state']);entry={'initial':runtime.certificate(),'steps':[]}
        for op,status in zip(plan['operations'],plan['statuses']):
            previous=runtime;before=previous.descriptor()
            runtime,t=(previous.refine_block(op['block'],op['row']) if op['kind']=='block-gain' else previous.refine_public(op['row']))
            assert previous.descriptor()==before
            live,fresh=compile_gain(runtime.descriptor());assert t['after']==fresh and fresh['status']==status
            step={'transition':t,'fresh':fresh}
            if status!='UNSUPPORTED':
                step['raw_audits']=[runtime.audit(q['node'],q['threshold']) for q in contract['audit_requests']]
                if live is not None:assert step['raw_audits']==[live.audit(q['node'],q['threshold']) for q in contract['audit_requests']]
                else:assert all(a['status']=='INCONSISTENT' for a in step['raw_audits'])
            else:
                step['feasible_raw_witness']=['0']*(runtime.descriptor()['m']+1)
                try:runtime.audit(1,40)
                except NotImplementedError:step['audit_refused']='UNBALANCED_CHART'
                else:raise AssertionError('unsupported chart answered an audit')
            reused+=len(t['reused_blocks']);recomputed+=len(t['recomputed_blocks']);entry['steps'].append(step)
        packets[name]=entry
    join=packets['component-join']['steps'][1]['transition']
    assert join['changed_scale_nodes']==[1,2,3] and join['recomputed_blocks']==[0,1]
    assert packets['component-join']['steps'][0]['transition']['reused_blocks']==[1]
    public=copy.deepcopy(base);public['retention']='public-only'
    try:GainHistory.create(public)
    except PermissionError:pass
    else:raise AssertionError('public-only fine update admitted')
    history=GainHistory.create(base)
    for action in (lambda:history.refine_public([2,6,'1','0']),lambda:history.refine_block(0,[1,2,'0','1'])):
        try:action()
        except ValueError:pass
        else:raise AssertionError('invalid gain update admitted')
    raw=gzip.compress(json.dumps(packets,separators=(',',':')).encode(),mtime=0)
    (OUT/'incremental-gain-packet.json.gz').write_bytes(raw)
    report={'transitions':sum(len(p['steps']) for p in packets.values()),'block_closures_reused':reused,
      'block_closures_recomputed':recomputed,'chart_admission_runs':sum(len(p['steps']) for p in packets.values()),
      'public_only_refusals':1,'invalid_updates_refused':2,'contract_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),
      'packet_sha256':hashlib.sha256(raw).hexdigest()}
    (OUT/'incremental-gain.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
