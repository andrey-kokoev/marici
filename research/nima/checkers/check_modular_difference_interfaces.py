"""Modular closures, crossing contradictions, witnesses and retention policy."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,copy
from modular_difference_interfaces import compile_state,closure,block_edges
OUT=Path(__file__).resolve().parents[1]/'results'
def size(x):return len(json.dumps(x,separators=(',',':')).encode())
def main():
    states={}
    for m in (4,8,16,32):
        mid=m//2;blocks=[]
        for start,end in ((1,mid),(mid,m)):
            blocks.append({'nodes':[0]+list(range(start,end+1)),'boundary':sorted({0,start,end}),
              'evidence':[[u,v,w] for j in range(start,end) for u,v,w in ((j,j+1,'1'),(j+1,j,'-1/2'))]})
        for policy in ('archive-backed','public-only'):
            states[f'chain-{m}-{policy}']={'m':m,'binding':'tail-box-100+2j-128^-j-v1','retention':policy,
                 'blocks':blocks,'public':[0,1,m],'exterior':[]}
    states['cross-block-cycle']={'m':4,'binding':'tail-box-100+2j-128^-j-v1','retention':'archive-backed','public':[0,1,3],
      'blocks':[{'nodes':[0,1,2,3],'boundary':[0,1,3],'evidence':[[1,2,'0'],[2,3,'0']]},
                {'nodes':[0,1,3,4],'boundary':[0,1,3],'evidence':[[3,4,'-1'],[4,1,'0']]}],'exterior':[]}
    states['local-cycle']=copy.deepcopy(states['cross-block-cycle']);states['local-cycle']['blocks'][0]['evidence'].append([3,1,'-1'])
    contract={'states':states,'schema':'modular-difference-controls-v1','source':'Raw atoms only; node 0 is zero; node j+1 has cap 100+2j.',
              'capabilities':'public-only denies fine fill/re-exposure; archive-backed recomputes from retained fine rows.',
              'implementation_sha256':hashlib.sha256(Path(__file__).with_name('modular_difference_interfaces.py').read_bytes()).hexdigest(),
              'scope':'Exact closed difference constraints, disjoint block interiors and explicit boundary mappings.'}
    cp=OUT/'modular-difference-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n')
    packets={}
    for name,s in states.items():
        live,proof=compile_state(s);edges=[e for b in s['blocks'] for e in block_edges(b)]+s['exterior']
        mono=closure(list(range(s['m']+1)),edges);entry={'certificate':proof,'monolithic':mono}
        assert proof['status']==mono['status']
        if live:
            assert live.rows==tuple((a,b,mono['distance'][a][b]) for a in s['public'] for b in s['public'] if a!=b)
            entry['live']=live.descriptor();m=s['m'];point=['0','1',str(1+Q(3*(m-1),4))]
            assert live.contains(point) and not live.contains(['0','1','1'])
            entry['membership']=[{'point':point,'admitted':True},{'point':['0','1','1'],'admitted':False}]
            if s['retention']=='archive-backed':
                entry['point']=point;entry['lift']=live.fill(point)
                exposed,p=live.expose([m-1]);entry['reexposure']=p;entry['exposed_live']=exposed.descriptor()
            else:
                assert live._archive is None
                for operation in (lambda:live.expose([m-1]),lambda:live.fill(point)):
                    try:operation()
                    except PermissionError:pass
                    else:raise AssertionError('unauthorized fine continuation')
                entry['refused_continuations']=['expose','fill']
            entry['cost']={'live_bytes':size(live.descriptor()),'retained_archive_bytes':size(s) if live._archive is not None else 0,
                           'migration_proof_bytes':size(proof),'public_rows':len(live.rows)}
        packets[name]=entry
    # Structural mismatches are refused before closure, not treated as emptiness.
    bad=copy.deepcopy(states['chain-8-archive-backed']);bad['blocks'][0]['boundary'].remove(4)
    try:compile_state(bad)
    except ValueError:pass
    else:raise AssertionError('shared interior admitted')
    raw=gzip.compress(json.dumps(packets,separators=(',',':')).encode(),mtime=0)
    (OUT/'modular-difference-packet.json.gz').write_bytes(raw)
    report={'cases':len(packets),'contract_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),'packet_sha256':hashlib.sha256(raw).hexdigest(),
            'runtime_policy_refusals':8,'shared_interior_rejected':True,'costs':{n:p['cost'] for n,p in packets.items() if 'cost' in p}}
    (OUT/'modular-difference.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
