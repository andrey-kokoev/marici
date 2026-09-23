"""Frozen update sequences; compare selective recomputation with fresh closure."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,copy
from modular_difference_interfaces import compile_state,digest
from incremental_difference_interfaces import ArchivedHistory,PublicHistory
OUT=Path(__file__).resolve().parents[1]/'results'
def main():
    source=json.loads((OUT/'modular-difference-contract.json').read_text())['states'];plans={}
    for m in (4,8,16):
        mid=m//2;left=Q(mid-1,2);right=Q(m-mid)
        plans[f'archive-{m}']={'state':source[f'chain-{m}-archive-backed'],'operations':[
          {'kind':'block-edge','block':0,'edge':[1,mid,str(left)]},
          {'kind':'block-edge','block':1,'edge':[m,mid,str(-right)]},
          {'kind':'public-edge','edge':[1,m,str(left+right-Q(1,4))]},
          {'kind':'public-edge','edge':[0,1,'100']}],'expected_statuses':['CONSISTENT','CONSISTENT','INCONSISTENT','INCONSISTENT']}
        plans[f'public-{m}']={'state':source[f'chain-{m}-public-only'],'operations':[
          {'kind':'public-edge','edge':[1,m,str(Q(m-1,2))]},
          {'kind':'public-edge','edge':[m,1,str(-Q(m-1,2)-1)]},
          {'kind':'public-edge','edge':[0,1,'99']}],'expected_statuses':['CONSISTENT','INCONSISTENT','INCONSISTENT']}
    cross=copy.deepcopy(source['cross-block-cycle']);cross['blocks'][1]['evidence'][0][2]='0'
    plans['new-cross-block-cycle']={'state':cross,'operations':[{'kind':'block-edge','block':1,'edge':[3,4,'-1']}],
                                    'expected_statuses':['INCONSISTENT']}
    contract={'schema':'incremental-difference-test-v1','plans':plans,
      'bindings':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__).with_name('incremental_difference_interfaces.py'),Path(__file__).with_name('modular_difference_interfaces.py'))},
      'scope':'Append-only raw difference constraints; block closure reuse, not incremental verification or gain-chart mutation.'}
    cp=OUT/'incremental-difference-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n')
    packets={};refusals=0
    for name,plan in plans.items():
        state=plan['state'];live,initial=compile_state(state);assert live is not None
        archived=state['retention']=='archive-backed'
        runtime=ArchivedHistory.create(state) if archived else PublicHistory.from_live(live.descriptor())
        entry={'initial':initial,'initial_descriptor':runtime.descriptor(),'steps':[]}
        for operation,status in zip(plan['operations'],plan['expected_statuses']):
            old=runtime;before=old.descriptor();before_hash=digest(before)
            if operation['kind']=='block-edge':runtime,transition=old.refine_block(operation['block'],operation['edge'])
            else:runtime,transition=old.refine_public(operation['edge'])
            assert old.descriptor()==before and digest(old.descriptor())==before_hash
            if archived:
                _,fresh=compile_state(runtime.descriptor());assert transition['after']==fresh and fresh['status']==status
            else:
                # Reference the original fine carrier with all accepted public rows.
                fine=copy.deepcopy(state);fine['exterior']+=runtime.descriptor()['frames'];_,fresh=compile_state(fine)
                assert transition['closure']['status']==fresh['status']==status
                if status=='CONSISTENT':assert transition['summary']==fresh['summary']
            entry['steps'].append({'transition':transition,'fresh':fresh})
        if not archived:
            for action in (lambda:runtime.refine_block(0,[1,2,'0']),lambda:runtime.expose([state['m']-1])):
                try:action()
                except PermissionError:refusals+=1
                else:raise AssertionError('hidden continuation allowed')
        else:
            try:runtime.refine_block(0,[1,2,'2','1'])
            except ValueError:pass
            else:raise AssertionError('gain row silently treated as difference')
        packets[name]=entry
    raw=gzip.compress(json.dumps(packets,separators=(',',':')).encode(),mtime=0)
    (OUT/'incremental-difference-packet.json.gz').write_bytes(raw)
    archived_steps=[s['transition'] for p in packets.values() for s in p['steps'] if s['transition']['kind'].startswith('archived')]
    report={'plans':len(plans),'transitions':sum(len(p['steps']) for p in packets.values()),'hidden_continuations_refused':refusals,
      'block_closures_recomputed':sum(len(t['recomputed_blocks']) for t in archived_steps),
      'block_closures_reused':sum(len(t['reused_blocks']) for t in archived_steps),
      'fresh_reference_block_closures':sum(len(t['after']['blocks']) for t in archived_steps),
      'contract_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),'packet_sha256':hashlib.sha256(raw).hexdigest()}
    (OUT/'incremental-difference.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
