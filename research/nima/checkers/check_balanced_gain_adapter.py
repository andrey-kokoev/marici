"""Gain adapter controls; freeze raw statements before compilation."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,copy
from balanced_gain_adapter import compile_gain
OUT=Path(__file__).resolve().parents[1]/'results'
def main():
    states={};witnesses={}
    for m in (4,8,16):
        scales=[Q(1)]+[Q(1+v%3) for v in range(1,m+1)];blocks=[]
        for start,end in ((1,m//2),(m//2,m)):
            evidence=[[u,v,str(scales[v]/scales[u]),str(scales[v]*w)] for j in range(start,end)
                      for u,v,w in ((j,j+1,Q(1)),(j+1,j,Q(-1,2)))]
            blocks.append({'nodes':[0]+list(range(start,end+1)),'boundary':sorted({0,start,end}),'evidence':evidence})
        base={'m':m,'binding':'owning-raw-tail-box-v1','retention':'archive-backed','blocks':blocks,'public':[0,1,m],
              'exterior':[[1,m,str(scales[m]/scales[1]),str(scales[m]*m)]]}
        for policy in ('archive-backed','public-only'):
            state=copy.deepcopy(base);state['retention']=policy;states[f'm{m}-{policy}']=state
        bad=copy.deepcopy(base);bad['exterior'][0][2]=str(2*Q(bad['exterior'][0][2]));name=f'm{m}-unbalanced';states[name]=bad
        witnesses[name]=['0']+[str(scales[v]*Q(3*(v-1),4)) for v in range(1,m+1)]
    fractional=copy.deepcopy(states['m4-archive-backed'])
    old=[Q(1),Q(2),Q(3),Q(1),Q(2)];new=[Q(1),Q(3,2),Q(5,3),Q(1),Q(7,4)]
    for b in fractional['blocks']:
        b['evidence']=[[u,v,str(new[v]/new[u]),str(Q(w)*new[v]/old[v])] for u,v,g,w in b['evidence']]
    fractional['exterior']=[[u,v,str(new[v]/new[u]),str(Q(w)*new[v]/old[v])] for u,v,g,w in fractional['exterior']]
    states['fractional-archive-backed']=fractional
    s=[Q(1),Q(2),Q(3),Q(1),Q(2)]
    states['balanced-inconsistent']={'m':4,'binding':'owning-raw-tail-box-v1','retention':'archive-backed','public':[0,1,3],
      'blocks':[{'nodes':[0,1,2,3],'boundary':[0,1,3],'evidence':[[u,v,str(s[v]/s[u]),str(s[v]*w)] for u,v,w in ((1,2,0),(2,3,0))]},
                {'nodes':[0,1,3,4],'boundary':[0,1,3],'evidence':[[u,v,str(s[v]/s[u]),str(s[v]*w)] for u,v,w in ((3,4,-1),(4,1,0))]}],'exterior':[]}
    contract={'states':states,'audit_requests':[{'node':1,'threshold':h} for h in ('-1','40','67','100')],
              'unsupported_feasible_witnesses':witnesses,'bindings':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in
              (Path(__file__).with_name('balanced_gain_adapter.py'),Path(__file__).with_name('modular_difference_interfaces.py'))},
              'source':'node v>=1 is raw atom v-1, cap 98+2v; node 0 is zero',
              'scope':'Positive balanced gains only; chart failure is UNSUPPORTED, not emptiness.'}
    cp=OUT/'balanced-gain-adapter-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n')
    packets={};refusals=0
    for name,state in states.items():
        live,proof=compile_gain(state);entry={'certificate':proof}
        if live:
            m=state['m'];values=[str(live.scales[v]*Q(3*(v-1),4)) if v else '0' for v in live.public]
            assert live.contains(values);entry['public_point']=values
            entry['audits']=[live.audit(q['node'],q['threshold']) for q in contract['audit_requests']]
            if state['retention']=='archive-backed':
                entry['raw_lift']=live.fill(values);_,entry['reexposure']=live.expose([m-1])
            else:
                assert live._archive is None and live._live._archive is None
                for op in (lambda:live.fill(values),lambda:live.expose([m-1])):
                    try:op()
                    except PermissionError:refusals+=1
                    else:raise AssertionError('fine continuation accepted')
                entry['refused']=['fill','expose']
        packets[name]=entry
    # Mixed moment rows and nonpositive gains are operationally unsupported.
    bad=copy.deepcopy(states['m4-archive-backed']);bad['blocks'][0]['evidence'][0][2]='0'
    try:compile_gain(bad)
    except ValueError:pass
    else:raise AssertionError('zero gain admitted')
    pp=OUT/'balanced-gain-adapter-packet.json.gz';pp.write_bytes(gzip.compress(json.dumps(packets,separators=(',',':')).encode(),mtime=0))
    report={'cases':len(packets),'contract_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),
      'packet_sha256':hashlib.sha256(pp.read_bytes()).hexdigest(),'fine_continuations_refused':refusals,
      'statuses':{n:p['certificate']['status'] for n,p in packets.items()}}
    (OUT/'balanced-gain-adapter.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
