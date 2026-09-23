"""Independent translation identities and both backends' arithmetic proofs."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import sys,json,gzip,hashlib,copy
from verify_two_free_tail_queries import reconstruct,verify
if not __debug__:raise RuntimeError('Assertions required')
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
sys.path.insert(0,str(ROOT/'voevodsky/checkers'))
from verify_schema_relative_tail_lp import check

def expected_translation(origin):
    residual=reconstruct(origin);m=origin['m'];frames=[]
    def row(entries,b):
        return {'a':[str(entries.get(k,Q(0))) for k in range(m+2)],'b':str(b)}
    for j,h in origin['pins']:
        frames.extend([row({j+2:Q(1)},Q(h)),row({j+2:Q(-1)},-Q(h))])
    for e in origin['evidence']:
        if e['kind']=='free_halfspace':
            frames.append(row({j+2:Q(a) for j,a in zip(origin['free'],e['normal'])},Q(e['upper'])))
        else:
            for k,(c,error) in enumerate(zip(e['center'],e['error'])):
                for sign in (1,-1):frames.append(row({k:Q(sign)},sign*Q(c)+Q(error)))
    target={'source':'tail-box-100+2j-128^-j-v1','m':m,'audits':list(range(m)),'frames':frames}
    # Coefficient identities, not sampled witnesses: substitute every pin in
    # each translated evidence row and recover exactly the planar row tuple.
    pins={j:Q(h) for j,h in origin['pins']};i,j=origin['free'];projected=[]
    for f in frames[2*len(pins):]:
        a=list(map(Q,f['a']));full=[a[0]+a[1]/128**k+a[k+2] for k in range(m)]
        projected.append(((full[i],full[j]),Q(f['b'])-sum(full[k]*h for k,h in pins.items())))
    assert projected==residual[4:]
    # Box rows on fixed coordinates become true constants; free box rows
    # are precisely the planar caps, up to the reference's row ordering.
    free_caps=[]
    for k in range(m):
        if k in pins:assert 0<=pins[k]<=100+2*k
        else:
            a=tuple(Q(int(k==v)) for v in (i,j))
            free_caps.extend([(a,Q(100+2*k)),(tuple(-v for v in a),Q(0))])
    assert Counter(free_caps)==Counter(residual[:4])
    return target

def check_bridge(request,packet):
    origin=request['state'];query=request['query']
    assert set(packet)=={'origin','query','specialized','general','simplex'}
    assert packet['origin']==origin and packet['query']==query
    specialized_status=verify(origin,query,packet['specialized'])
    target=expected_translation(origin);assert len(packet['general'])==2
    for sign,proof in zip((-1,1),packet['general']):
        obj=['0']*(origin['m']+2);obj[2+origin['free'][0]]=str(sign)
        check(target,{'kind':'maximize','objective':obj},proof)
    assert len(packet['simplex'])==2
    for reference,transported in zip(packet['simplex'],packet['general']):
        if reference['status']=='VERIFIED':
            candidate=reference['certificate'];check(target,transported['query'],candidate)
            assert candidate['status']==transported['status']
            if candidate['status']!='EMPTY':assert Q(candidate['value'])==Q(transported['value'])
        else:
            assert reference['status']=='PROPOSAL_FAILED'
            # Diagnostic only: no mathematical answer or verified failure cause.
            assert set(reference)=={'status','error_type','message'}
    low,high=packet['general'];assert (low['status']=='EMPTY')==(high['status']=='EMPTY')
    if low['status']=='EMPTY':assert specialized_status=='INCONSISTENT'
    else:
        lo,hi=-Q(low['value']),Q(high['value']);h=Q(query['threshold'])
        assert lo<=hi and [lo,hi]==list(map(Q,packet['specialized']['result']['interval']))
        assert specialized_status==('FORCED_TRUE' if hi<=h else 'FORCED_FALSE' if lo>h else 'UNRESOLVED')
    return specialized_status

def main():
    cp=OUT/'two-free-tail-query-contract.json';sp=OUT/'two-free-tail-query-packet.json.gz'
    bc=json.loads((OUT/'two-free-schema-bridge-contract.json').read_text())
    assert hashlib.sha256(cp.read_bytes()).hexdigest()==bc['input_contract_sha256']
    assert hashlib.sha256(sp.read_bytes()).hexdigest()==bc['input_packet_sha256']
    c=json.loads(cp.read_text());requests=c['requests']
    raw=(OUT/'two-free-schema-bridge-packet.json.gz').read_bytes()
    report_path=OUT/'two-free-schema-bridge.json';report=json.loads(report_path.read_text())
    assert hashlib.sha256(raw).hexdigest()==report['packet_sha256'];packets=json.loads(gzip.decompress(raw))
    names=[name for name,r in requests.items() if r['state']['m']<=8]
    assert bc['cases']==names and set(packets)==set(names)
    statuses=Counter()
    for name in names:statuses[check_bridge(requests[name],packets[name])]+=1
    attacks=[];name='m3-worst-at';original=packets[name]
    for defect in ('drop-pin','change-error','swap-schema','change-query','lose-history','binding','dual','witness'):
        bad=copy.deepcopy(original)
        if defect=='drop-pin':del bad['general'][0]['state']['frames'][0]
        if defect=='change-error':bad['general'][0]['state']['frames'][2]['b']='999'
        if defect=='swap-schema':bad['general'][0]['state']['audits'].reverse()
        if defect=='change-query':bad['general'][0]['query']['objective'][3]='0'
        if defect=='lose-history':bad['origin']['evidence']=[]
        if defect=='binding':bad['origin']['source_binding']='foreign'
        if defect=='dual':bad['general'][0]['weights']=[]
        if defect=='witness':bad['general'][0]['x'][0]='0'
        try:check_bridge(requests[name],bad)
        except (AssertionError,ValueError,KeyError,IndexError,TypeError):attacks.append(defect)
        else:raise AssertionError('accepted '+defect)
    # A valid translated certificate cannot be substituted across refinements.
    for old,new in [('wide','narrow'),('narrow','narrow-then-wide'),('wide','linear-refined')]:
        bad=copy.deepcopy(packets[new]);bad['general']=packets[old]['general']
        try:check_bridge(requests[new],bad)
        except AssertionError:attacks.append(old+'->'+new)
        else:raise AssertionError('accepted stale target state')
    result={'passed':True,'report_sha256':hashlib.sha256(report_path.read_bytes()).hexdigest(),
            'translation_identities':len(names),'specialized_certificates':len(names),'general_certificates':2*len(names),
            'statuses':dict(statuses),'attacks_rejected':attacks,
            'simplex_certificates_verified':sum(s['status']=='VERIFIED' for p in packets.values() for s in p['simplex']),
            'reported_simplex_proposal_failures':sum(s['status']=='PROPOSAL_FAILED' for p in packets.values() for s in p['simplex']),
            'scope':'Exact source-set translation and certificate agreement, not witness identity or authentication.'}
    (OUT/'two-free-schema-bridge-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
