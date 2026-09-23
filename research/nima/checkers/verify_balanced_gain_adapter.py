"""Independent raw/chart identities, modular proofs and capability binding."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,copy
from verify_modular_difference_interfaces import check as check_difference,digest
if not __debug__:raise RuntimeError('Assertions required')
OUT=Path(__file__).resolve().parents[1]/'results'
def rows(s):return [r for b in s['blocks'] for r in b['evidence']]+s['exterior']
def raw_lift(state,x):
    x=list(map(Q,x));assert len(x)==state['m']+1 and x[0]==0
    assert all(0<=x[v]<=98+2*v for v in range(1,len(x)))
    assert all(x[v]<=Q(g)*x[u]+Q(b) for u,v,g,b in rows(state))
    return x

def check(state,p,*,_difference_check=check_difference):
    # Internal hook; ordinary callers always replay all normalized blocks.
    assert p['state']==state and p['state_digest']==digest(state)
    edges=rows(state);m=state['m']
    if p['status']=='UNSUPPORTED':
        assert p['reason']=='UNBALANCED_CHART' and p['gain_cycle'];product=Q(1);start=None;current=None
        for k,sign in p['gain_cycle']:
            assert type(k) is int and 0<=k<len(edges) and type(sign) is int and sign in (-1,1)
            u,v,g,b=edges[k];assert Q(g)>0
            if sign==-1:u,v=v,u
            if start is None:start=u;current=u
            assert u==current;current=v;product*=Q(g)**sign
        assert current==start and product!=1;return None
    scales=list(map(Q,p['scales']));assert len(scales)==m+1 and scales[0]==1 and min(scales)>=1
    components=[{j} for j in range(1,m+1)]
    for u,v,g,b in edges:
        assert Q(g)>0 and scales[v]==Q(g)*scales[u]
        a=next(c for c in components if u in c);bset=next(c for c in components if v in c)
        if a is not bset:a.update(bset);components.remove(bset)
    assert all(min(scales[v] for v in component)==1 for component in components)
    normalized=copy.deepcopy(state);normalized['binding']='balanced-gain-chart-v1:'+digest(state)
    for b in normalized['blocks']:
        converted=[]
        for v in b['nodes']:
            if v:converted.append([0,v,str(Q(98+2*v)/scales[v])])
        for u,v,g,bound in b['evidence']:
            assert Q(g)*scales[u]/scales[v]==1
            converted.append([u,v,str(Q(bound)/scales[v])])
        b['evidence']=converted
    normalized['exterior']=[[u,v,str(Q(bound)/scales[v])] for u,v,g,bound in state['exterior']]
    summary=_difference_check(normalized,p['normalized'])
    assert p['status']==p['normalized']['status']
    return (scales,summary) if summary is not None else None

def check_audits(requests,proof,answers):
    scales=list(map(Q,proof['scales']));bounds={(u,v):Q(w) for u,v,w in proof['normalized']['summary']}
    assert len(requests)==len(answers)
    for query,a in zip(requests,answers):
        v=query['node'];h=Q(query['threshold']);lo=-scales[v]*bounds[v,0];hi=scales[v]*bounds[0,v]
        assert a['node']==v and a['threshold']==query['threshold']
        assert list(map(Q,a['interval']))==[lo,hi]
        assert a['status']==('FORCED_TRUE' if hi<=h else 'FORCED_FALSE' if lo>h else 'UNRESOLVED')

def main():
    cp=OUT/'balanced-gain-adapter-contract.json';rp=OUT/'balanced-gain-adapter.json'
    c=json.loads(cp.read_text());report=json.loads(rp.read_text());raw=(OUT/'balanced-gain-adapter-packet.json.gz').read_bytes()
    assert hashlib.sha256(cp.read_bytes()).hexdigest()==report['contract_sha256'] and hashlib.sha256(raw).hexdigest()==report['packet_sha256']
    for path,h in c['bindings'].items():assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==h
    packets=json.loads(gzip.decompress(raw));assert set(packets)==set(c['states'])
    for name,s in c['states'].items():
        entry=packets[name];p=entry['certificate'];result=check(s,p)
        if name.endswith('unbalanced'):
            assert p['status']=='UNSUPPORTED';raw_lift(s,c['unsupported_feasible_witnesses'][name]);continue
        if name=='balanced-inconsistent':assert p['status']=='INCONSISTENT';continue
        assert p['status']=='CONSISTENT';scales,summary=result
        values=dict(zip(s['public'],map(Q,entry['public_point'])))
        assert values[0]==0 and all(values[v]/scales[v]-values[u]/scales[u]<=Q(w) for u,v,w in summary)
        check_audits(c['audit_requests'],p,entry['audits'])
        if s['retention']=='archive-backed':
            x=raw_lift(s,entry['raw_lift']);assert all(x[v]==values[v] for v in s['public'])
            expected=copy.deepcopy(s);v=s['m']-1;expected['public']=sorted(set(s['public'])|{v})
            for b in expected['blocks']:b['boundary']=sorted(set(b['boundary'])|({v}&set(b['nodes'])))
            check(expected,entry['reexposure'])
        else:assert entry['refused']==['fill','expose'] and 'raw_lift' not in entry
    name='m4-archive-backed';state=c['states'][name];base=packets[name]['certificate'];rejected=[]
    for defect in ('scale','scaled-cap','boundary','policy','history'):
        bad=copy.deepcopy(base)
        if defect=='scale':bad['scales'][1]='1'
        if defect=='scaled-cap':bad['normalized']['state']['blocks'][0]['evidence'][0][2]='100'
        if defect=='boundary':bad['normalized']['state']['blocks'][0]['boundary'].pop()
        if defect=='policy':bad['state']['retention']='public-only';bad['state_digest']=digest(bad['state'])
        if defect=='history':bad['state']['blocks'][0]['evidence'].pop();bad['state_digest']=digest(bad['state'])
        try:check(state,bad)
        except (AssertionError,ValueError,KeyError,IndexError):rejected.append(defect)
        else:raise AssertionError('corruption admitted')
    a=copy.deepcopy(packets[name]['audits']);a[1]['threshold']='20'
    try:check_audits(c['audit_requests'],base,a)
    except AssertionError:rejected.append('rescaled-raw-threshold')
    else:raise AssertionError('changed raw threshold admitted')
    bad=copy.deepcopy(packets['m4-unbalanced']['certificate']);bad['status']='INCONSISTENT'
    try:check(c['states']['m4-unbalanced'],bad)
    except (AssertionError,KeyError):rejected.append('unsupported-as-inconsistent')
    else:raise AssertionError('chart failure treated as emptiness')
    maxbits=max(max(abs(Q(v).numerator).bit_length(),Q(v).denominator.bit_length()) for p in packets.values() for v in p['certificate'].get('scales',[]))
    result={'passed':True,'states':len(packets),'raw_audit_answers':28,'raw_source_lifts':4,'reexposures':4,
            'feasible_unbalanced_controls':3,'certified_inconsistent_controls':1,'attacks_rejected':rejected,
            'observed_max_scale_bits':maxbits,'scope':'Shared balanced chart; raw semantics and retention policy; no norm-invariant conditioning claim.'}
    (OUT/'balanced-gain-adapter-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
