"""Independent rational certificate verifier; imports no producer or LP solver."""
from fractions import Fraction as Q
from pathlib import Path
import json,gzip,hashlib,copy
if not __debug__:raise RuntimeError('Assertions must be enabled')
OUT=Path(__file__).resolve().parents[1]/'results'
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def rational(x):
    assert type(x) in (int,str,Q)
    return Q(x)
def pair(x):
    assert isinstance(x,(list,tuple)) and len(x)==2
    return tuple(map(rational,x))
def reconstruct(state):
    assert set(state)=={'schema','source_rule','source_binding','m','free','pins','evidence'}
    assert state['schema']=='two-free-tail-state-v1' and state['source_rule']=='cap=100+2j;slope=128^-j;0<=j<m'
    assert type(state['source_binding']) is str and state['source_binding']
    m=state['m'];assert type(m) is int and m>=2
    free=state['free'];assert isinstance(free,list) and len(free)==2 and all(type(i) is int for i in free)
    i,j=free;assert 0<=i<j<m
    pins=state['pins'];assert isinstance(pins,list) and all(isinstance(p,list) and len(p)==2 for p in pins)
    assert all(type(k) is int for k,v in pins)
    assert [k for k,v in pins]==[k for k in range(m) if k not in free]
    assert all(0<=rational(v)<=100+2*k for k,v in pins)
    offset=[sum((rational(v) for k,v in pins),Q(0)),sum((rational(v)/128**k for k,v in pins),Q(0))]
    rows=[((-1,0),Q(0)),((1,0),Q(100+2*i)),((0,-1),Q(0)),((0,1),Q(100+2*j))]
    for event in state['evidence']:
        if event['kind']=='free_halfspace':
            assert set(event)=={'kind','normal','upper'}
            rows.append((pair(event['normal']),rational(event['upper'])))
        else:
            assert set(event)=={'kind','center','error'} and event['kind']=='measurement_box'
            center=pair(event['center']);error=pair(event['error']);assert min(error)>=0
            for a,k in (((Q(1),Q(1)),0),((Q(1,128**i),Q(1,128**j)),1)):
                rows.append((a,center[k]+error[k]-offset[k]))
                rows.append((tuple(-x for x in a),-center[k]+error[k]+offset[k]))
    return rows

def combination(rows,terms):
    n=[Q(0),Q(0)];bound=Q(0);seen=set()
    for index,value in terms:
        assert type(index) is int and 0<=index<len(rows) and index not in seen;seen.add(index)
        w=rational(value);assert w>=0
        a,b=rows[index];bound+=w*b
        for k in range(2):n[k]+=w*a[k]
    return tuple(n),bound

def verify(expected_state,expected_query,packet):
    rows=reconstruct(expected_state)
    assert set(expected_query)=={'kind','atom','relation','threshold'}
    assert expected_query['kind']=='free-atom-threshold' and expected_query['relation']=='<='
    assert type(expected_query['atom']) is int and expected_query['atom']==expected_state['free'][0]
    h=rational(expected_query['threshold'])
    assert set(packet)=={'schema','state','query','state_digest','query_digest','result'}
    assert packet['schema']=='two-free-tail-certificate-v1'
    assert packet['state']==expected_state and packet['query']==expected_query
    reconstruct(packet['state'])  # Reject bool/int aliases in packet indices too.
    assert type(packet['query']['atom']) is int
    assert packet['state_digest']==digest(expected_state)
    assert packet['query_digest']==digest({'state_digest':digest(expected_state),'query':expected_query})
    result=packet['result'];status=result['status']
    if status=='INCONSISTENT':
        assert set(result)=={'status','farkas'}
        n,b=combination(rows,result['farkas']);assert n==(0,0) and b<0
    else:
        assert set(result)=={'status','interval','minimum','maximum'}
        values=[]
        for key,objective in (('minimum',(-1,0)),('maximum',(1,0))):
            proof=result[key];assert set(proof)=={'point','value','dual'}
            point=pair(proof['point']);assert all(sum(x*y for x,y in zip(a,point))<=b for a,b in rows)
            n,b=combination(rows,proof['dual']);assert n==objective
            assert b==rational(proof['value'])==sum(x*y for x,y in zip(objective,point))
            values.append(point[0])
        lo,hi=values;assert lo<=hi and pair(result['interval'])==(lo,hi)
        assert status==('FORCED_TRUE' if hi<=h else 'FORCED_FALSE' if lo>h else 'UNRESOLVED')
    return status

def main():
    cp=OUT/'two-free-tail-query-contract.json';c=json.loads(cp.read_text())
    report_path=OUT/'two-free-tail-query.json';report=json.loads(report_path.read_text())
    assert hashlib.sha256(cp.read_bytes()).hexdigest()==report['contract_sha256']
    paths={'backend_sha256':Path(__file__).with_name('two_free_tail_queries.py'),
           'lp_engine_sha256':Path(__file__).with_name('check_symbolic_tail_interface.py'),
           'source_sha256':OUT.parents[1]/'grothendieck/results/two-moment-tail-complexity.json'}
    for key,path in paths.items():assert hashlib.sha256(path.read_bytes()).hexdigest()==c[key]
    raw=(OUT/'two-free-tail-query-packet.json.gz').read_bytes();p=json.loads(gzip.decompress(raw))
    assert hashlib.sha256(raw).hexdigest()==report['packet_sha256']
    assert set(p)==set(c['requests'])
    for name,packet in p.items():
        expected=c['requests'][name];status=verify(expected['state'],expected['query'],packet)
        assert status==expected['status']
        if 'interval' in expected:assert pair(packet['result']['interval'])==pair(expected['interval'])
    # Resealing an altered response cannot replace the externally expected state.
    good=p['m3-worst-at'];expected=c['requests']['m3-worst-at'];attacks=[]
    for mutate in ('history','error','pins','free','binding','threshold','status','dual','witness'):
        bad=copy.deepcopy(good)
        if mutate=='history':bad['state']['evidence']=[]
        if mutate=='error':bad['state']['evidence'][0]['error'][1]='1'
        if mutate=='pins':bad['state']['pins'][0][1]='2'
        if mutate=='free':bad['state']['free']=[0,2]
        if mutate=='binding':bad['state']['source_binding']='foreign'
        if mutate=='threshold':bad['query']['threshold']='19'
        if mutate=='status':bad['result']['status']='FORCED_FALSE'
        if mutate=='dual':bad['result']['maximum']['dual']=[]
        if mutate=='witness':bad['result']['maximum']['point']=['0','0']
        bad['state_digest']=digest(bad['state']);bad['query_digest']=digest({'state_digest':bad['state_digest'],'query':bad['query']})
        attacks.append(bad)
    bad=copy.deepcopy(p['inconsistent']);bad['result']['farkas']=[]
    attacks.append(bad)
    for k,bad in enumerate(attacks):
        e=expected if k<9 else c['requests']['inconsistent']
        try:verify(e['state'],e['query'],bad)
        except (AssertionError,ValueError,KeyError,TypeError,IndexError,ZeroDivisionError):pass
        else:raise AssertionError('corruption accepted')
    # Valid old proofs must not migrate to refined precision or history.
    for old,new in [('wide','narrow'),('narrow','narrow-then-wide'),('wide','linear-refined')]:
        e=c['requests'][new]
        try:verify(e['state'],e['query'],p[old])
        except AssertionError:pass
        else:raise AssertionError('stale snapshot accepted')
    report={'passed':True,'report_sha256':hashlib.sha256(report_path.read_bytes()).hexdigest(),
            'certificates':len(p),'corruptions_rejected':len(attacks),'stale_snapshots_rejected':3,
            'scope':'Two free atoms, exact supplied pins, finite closed linear evidence; no measurement authentication or noisy pins.'}
    (OUT/'two-free-tail-query-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
