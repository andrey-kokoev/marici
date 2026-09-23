"""Independent joint cuts, statement translation and precision-answer replay."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,copy
from verify_two_free_tail_queries import reconstruct,verify
from verify_two_free_schema_bridge import expected_translation,check as check_source
if not __debug__:raise RuntimeError('Assertions required')
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def expected(origin):
    reconstruct(origin);m=origin['m'];i,j=origin['free'];A=[k for k,h in origin['pins']]
    slopes=[Q(1,128**k) for k in range(m)];r,s=slopes[i],slopes[j];gap=r-s;d=2+len(A)
    x=tuple([-s/gap,1/gap]+[(s-slopes[k])/gap for k in A])
    y=tuple([r/gap,-1/gap]+[(slopes[k]-r)/gap for k in A])
    def pull(a):return tuple(a[0]+a[1]*slopes[k]+(a[2+A.index(k)] if k in A else 0) for k in range(m))
    assert pull(x)==tuple(Q(int(k==i)) for k in range(m))
    assert pull(y)==tuple(Q(int(k==j)) for k in range(m))
    frames=[]
    for pos,(k,h) in enumerate(origin['pins']):
        for sign in (1,-1):frames.append((tuple(Q(sign if n==pos+2 else 0) for n in range(d)),sign*Q(h)))
    for e in origin['evidence']:
        if e['kind']=='free_halfspace':
            a,b=map(Q,e['normal']);frames.append((tuple(a*v+b*w for v,w in zip(x,y)),Q(e['upper'])))
        else:
            for k in range(2):
                for sign in (1,-1):frames.append((tuple(Q(sign if n==k else 0) for n in range(d)),sign*Q(e['center'][k])+Q(e['error'][k])))
    def bound(a):return sum(Q(100+2*k)*max(Q(0),v) for k,v in enumerate(pull(a)))
    D={}
    for pos,k in enumerate(A):
        for sign in (-1,1):
            a=tuple(Q(sign if n==pos+2 else 0) for n in range(d));D[f'audit:{k}:{sign}']=(a,bound(a))
    for k in (i,j):
        for sign in (-1,1):
            a=tuple([-sign*slopes[k],Q(sign)]+[sign*(slopes[k]-slopes[v]) for v in A])
            D[f'edge:{k}:{sign}']=(a,bound(a))
    for sign in (-1,1):
        a=tuple([Q(sign),Q(0)]+[Q(-sign)]*len(A));D[f'mass:{sign}']=(a,bound(a))
    assert len(D)==2*m+2
    return A,frames,x,slopes,bound,D

def check_answer(origin,frames,obj,answer,context):
    A,_,_,slopes,bound,D=context;m=origin['m'];d=len(obj);rows=[]
    for j in range(d):
        for sign in (-1,1):
            a=tuple(Q(sign if k==j else 0) for k in range(d));rows.append((a,bound(a),f'box:{j}:{sign}'))
    rows.extend((a,b,f'frame:{k}') for k,(a,b) in enumerate(frames));used=set()
    for step in answer['trace']:
        p=tuple(map(Q,step['candidate']));key=step['cut']
        assert len(p)==d and min(p)>=0 and all(dot(a,p)<=b for a,b,label in rows)
        assert key in D and key not in used;used.add(key);a,b=D[key]
        assert dot(a,p)>b;rows.append((a,b,key))
    if answer['rows'][-1]['label']=='support:objective':rows.append((obj,bound(obj),'support:objective'))
    actual=[(tuple(map(Q,r['normal'])),Q(r['upper']),r['label']) for r in answer['rows']]
    assert actual==rows and answer['dictionary_size']==len(D) and len(used)<=len(D)
    w=list(map(Q,answer['multipliers']));assert len(w)==len(rows) and min(w)>=0
    normal=tuple(sum(v*row[0][k] for v,row in zip(w,rows)) for k in range(d));upper=sum(v*row[1] for v,row in zip(w,rows))
    if answer['status']=='INCONSISTENT':assert min(normal)>=0 and upper<0
    else:
        assert answer['status']=='OPTIMUM';p=tuple(map(Q,answer['point']));t=tuple(map(Q,answer['source_lift']))
        assert len(p)==d and len(t)==m and all(0<=v<=100+2*k for k,v in enumerate(t))
        assert p==(sum(t),dot(slopes,t),*[t[k] for k in A])
        assert all(dot(a,p)<=b for a,b,label in rows) and all(a>=b for a,b in zip(normal,obj))
        assert upper==dot(obj,p)==Q(answer['value'])

def check_case(request,packet):
    origin=request['state'];query=request['query'];context=expected(origin);A,frames,obj,_,_,_=context
    assert packet['origin']==origin and packet['query']==query and packet['audits']==A
    assert packet['frames']==[{'normal':list(map(str,a)),'upper':str(b)} for a,b in frames]
    assert packet['objective']==list(map(str,obj))
    status=verify(origin,query,packet['specialized']);assert len(packet['joint'])==2
    for side,sign,proposal in zip(('minimum','maximum'),(-1,1),packet['joint']):
        if proposal['status']=='PROPOSAL_FAILED':
            assert set(proposal)=={'status','error_type','message'};continue
        if proposal['status']=='SOURCE_FARKAS_FALLBACK':
            assert set(proposal)=={'status','primary_failure','certificate'}
            assert set(proposal['primary_failure'])=={'error_type','message'}
            target=expected_translation(origin);objective=['0']*(origin['m']+2)
            objective[origin['free'][0]+2]=str(sign)
            check_source(target,{'kind':'maximize','objective':objective},proposal['certificate'])
            assert proposal['certificate']['status']=='EMPTY' and status=='INCONSISTENT'
            continue
        assert proposal['status']=='PROPOSED';a=proposal['answer'];check_answer(origin,frames,tuple(sign*v for v in obj),a,context)
        assert (a['status']=='INCONSISTENT')==(status=='INCONSISTENT')
        if status!='INCONSISTENT':assert Q(a['value'])==Q(packet['specialized']['result'][side]['value'])
    return all(a['status'] in ('PROPOSED','SOURCE_FARKAS_FALLBACK') for a in packet['joint'])

def main():
    c=json.loads((OUT/'precision-joint-bridge-contract.json').read_text())
    for path,h in c['bindings'].items():assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==h
    original=json.loads((OUT/'two-free-tail-query-contract.json').read_text())['requests']
    names=[n for n,r in original.items() if r['state']['m']<=8];assert c['cases']==names
    raw=(OUT/'precision-joint-bridge-packet.json.gz').read_bytes();report_path=OUT/'precision-joint-bridge.json';report=json.loads(report_path.read_text())
    assert hashlib.sha256(raw).hexdigest()==report['packet_sha256'];packets=json.loads(gzip.decompress(raw));assert set(packets)==set(names)
    complete=sum(check_case(original[n],packets[n]) for n in names)
    checked=[a['answer'] for p in packets.values() for a in p['joint'] if a['status']=='PROPOSED']
    n=next(n for n in names if all(a['status']=='PROPOSED' for a in packets[n]['joint']) and packets[n]['joint'][0]['answer']['status']=='OPTIMUM')
    attacks=[]
    for defect in ('history','precision','schema','objective','multiplier','lift'):
        bad=copy.deepcopy(packets[n])
        if defect=='history':bad['frames'].pop()
        if defect=='precision':bad['origin']['evidence'][0]['error'][1]='1'
        if defect=='schema':bad['audits']=[]
        if defect=='objective':bad['objective'][0]='999'
        if defect=='multiplier':bad['joint'][0]['answer']['multipliers'][0]='-1'
        if defect=='lift':bad['joint'][0]['answer']['source_lift'][0]='-1'
        try:check_case(original[n],bad)
        except (AssertionError,ValueError,KeyError,IndexError):attacks.append(defect)
        else:raise AssertionError('accepted '+defect)
    cut_name=next(n for n in names if any(a['status']=='PROPOSED' and a['answer']['trace'] for a in packets[n]['joint']))
    for defect in ('cut-row','cut-identity'):
        bad=copy.deepcopy(packets[cut_name]);a=next(a['answer'] for a in bad['joint'] if a['status']=='PROPOSED' and a['answer']['trace'])
        if defect=='cut-row':a['rows'][-1]['upper']=str(Q(a['rows'][-1]['upper'])+1)
        else:a['trace'][0]['cut']='not-in-dictionary'
        try:check_case(original[cut_name],bad)
        except (AssertionError,KeyError):attacks.append(defect)
        else:raise AssertionError('accepted cut corruption')
    for old,new in [('wide','narrow'),('narrow','narrow-then-wide'),('wide','linear-refined')]:
        bad=copy.deepcopy(packets[new]);bad['joint']=packets[old]['joint']
        try:check_case(original[new],bad)
        except (AssertionError,KeyError):attacks.append(old+'->'+new)
        else:raise AssertionError('stale packet accepted')
    for defect in ('negative-ray','zero-ray','missing-pin','wrong-objective','foreign-binding','feasible-replay'):
        name='inconsistent';bad=copy.deepcopy(packets[name]);fallback=bad['joint'][0]
        assert fallback['status']=='SOURCE_FARKAS_FALLBACK'
        proof=fallback['certificate']
        if defect=='negative-ray':proof['weights'][0][1]='-1'
        if defect=='zero-ray':proof['weights']=[]
        if defect=='missing-pin':del proof['state']['frames'][0]
        if defect=='wrong-objective':proof['query']['objective']=['0']*len(proof['query']['objective'])
        if defect=='foreign-binding':bad['origin']['source_binding']='foreign'
        if defect=='feasible-replay':
            name='narrow';other=copy.deepcopy(packets[name]);other['joint'][0]=fallback;bad=other
        try:check_case(original[name],bad)
        except (AssertionError,KeyError,IndexError,ValueError):attacks.append('fallback:'+defect)
        else:raise AssertionError('invalid fallback accepted')
    recovered=sum(a['status']=='SOURCE_FARKAS_FALLBACK' for p in packets.values() for a in p['joint'])
    assert complete==len(names)==46 and len(checked)+recovered==92 and recovered==4
    def bits(value):
        if isinstance(value,dict):return max([0]+[bits(v) for v in value.values()])
        if isinstance(value,list):return max([0]+[bits(v) for v in value])
        try:q=Q(value);return max(abs(q.numerator).bit_length(),q.denominator.bit_length())
        except (ValueError,TypeError):return 0
    result={'passed':True,'report_sha256':hashlib.sha256(report_path.read_bytes()).hexdigest(),
      'cases':len(names),'joint_certificates_verified':len(checked),'complete_answer_comparisons':complete,
      'source_farkas_certificates_verified':recovered,'total_certificates_verified':len(checked)+recovered,
      'primary_proposal_failures':2*len(names)-len(checked),
      'unresolved_proposal_failures':2*len(names)-len(checked)-recovered,'attacks_rejected':attacks,
      'observed_max_cuts':max(len(a['trace']) for a in checked),'observed_max_rows':max(len(a['rows']) for a in checked),
      'observed_max_dimension':max(len(a['rows'][0]['normal']) for a in checked),'observed_max_rational_bits':bits(checked),
      'cost_scope':'Observed maxima cover native joint packets; fallback source-space proofs are counted separately.',
      'scope':'Finite-workload measurements; no uniform efficiency or solver-totality claim.'}
    (OUT/'precision-joint-bridge-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
