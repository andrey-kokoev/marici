"""Independent direct-sum and exact primal/dual replay; no producer import."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,gzip,hashlib,copy
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
@lru_cache(None)
def model(m):
    # Independent verifier may enumerate generators, but never needs facets
    # for large m. The runtime engine instead uses closed geometric sums.
    caps=tuple(Q(100+2*j) for j in range(m));slopes=tuple(Q(1,128**j) for j in range(m))
    mass=[Q(0)];weighted=[Q(0)]
    for c,r in zip(caps,slopes):mass.append(mass[-1]+c);weighted.append(weighted[-1]+c*r)
    return caps,slopes,tuple(mass),tuple(weighted)
def support(m,s):
    caps,slopes,C,W=model(m);a=tuple(map(Q,s['normal']));lo,hi=s['positive_interval']
    assert 0<=lo<=hi<=m
    for j,r in enumerate(slopes):assert (a[0]+a[1]*r>0)==(lo<=j<hi)
    expected=sum(c*max(Q(0),a[0]+a[1]*r) for c,r in zip(caps,slopes))
    point=tuple(map(Q,s['point']));assert point==(C[hi]-C[lo],W[hi]-W[lo])
    assert Q(s['upper'])==expected==dot(a,point)
    return a,expected

def lift(m,point,l):
    caps,slopes,C,W=model(m);u,v=point
    k=l['high_prefix'];h=Q(l['high_partial']);j=l['complement_prefix'];r=Q(l['complement_partial']);theta=Q(l['theta'])
    for index,partial in ((k,h),(j,r)):
        assert type(index) is int and 0<=index<=m
        assert partial==0 if index==m else 0<=partial<caps[index]
    assert 0<=theta<=1 and C[k]+h==u and C[j]+r==C[-1]-u
    high=W[k]+(slopes[k]*h if k<m else 0);low=W[-1]-W[j]-(slopes[j]*r if j<m else 0)
    assert low<=high and (1-theta)*low+theta*high==v
    # Exact sparse-profile identities certify every source coordinate's cap
    # without storing a source vector. Small cases also replay every coordinate.
    if m<=16:
        x=[]
        for n in range(m):
            top=caps[n] if n<k else h if n==k else Q(0)
            comp=caps[n] if n<j else r if n==j else Q(0)
            x.append((1-theta)*(caps[n]-comp)+theta*top)
        assert all(0<=x[n]<=caps[n] for n in range(m))
        assert sum(x)==u and dot(x,slopes)==v
    return low,high

def check_lp(query,expected_frames):
    m=query['m'];objective=tuple(map(Q,query['objective']));result=query['result'];rows=[];frames=[]
    assert [(tuple(map(Q,f['a'])),Q(f['b'])) for f in query['frames']]==expected_frames
    for row in result['rows']:
        a,b=tuple(map(Q,row['a'])),Q(row['b']);rows.append((a,b))
        if row['kind']=='source':assert support(m,row['support'])==(a,b)
        else:assert row['kind']=='frame';frames.append((a,b))
    assert frames==expected_frames
    assert len(rows)<=4+len(frames)+2*m and len(result['cuts'])==result['source_facets_generated']<=2*m
    for i,cut in enumerate(result['cuts']):
        point=tuple(map(Q,cut['rejected_point']));a,b=support(m,cut['support'])
        assert rows[4+len(frames)+i]==(a,b)
        assert all(dot(n,point)<=c for n,c in rows[:4+len(frames)+i]) and dot(a,point)>b
    weights=result['dual'];assert len({i for i,v in weights})==len(weights)
    assert all(type(i) is int and 0<=i<len(rows) and Q(v)>=0 for i,v in weights)
    normal=tuple(sum(Q(v)*rows[i][0][j] for i,v in weights) for j in (0,1));upper=sum(Q(v)*rows[i][1] for i,v in weights)
    if result['status']=='OPTIMAL':
        assert len(weights)<=2 and normal==objective
        point=tuple(map(Q,result['point']));lift(m,point,result['lift'])
        assert all(dot(a,point)<=b for a,b in rows)
        assert upper==Q(result['value'])==dot(objective,point)
    else:
        assert result['status']=='INCONSISTENT' and len(weights)<=3 and normal==(0,0) and upper<0

def main():
    cp=OUT/'symbolic-tail-interface-contract.json';rp=OUT/'symbolic-tail-interface.json';pp=OUT/'symbolic-tail-interface-packet.json.gz'
    c,r=load(cp),load(rp)
    assert sha(cp)==r['contract_sha256'] and sha(pp)==r['packet_sha256']
    with gzip.open(pp,'rt') as f:p=json.load(f)
    source_path=ROOT/'grothendieck/results/two-moment-tail-complexity.json';assert sha(source_path)==c['source_sha256'];source=load(source_path)
    reference={f['m']:f for f in source['families']}
    for query in p['support_queries']:
        m=query['m'];a,b=support(m,query['result'])
        if m in reference:
            points={tuple(map(Q,x)) for f in reference[m]['facets'] for x in f['edge_endpoints']}
            assert max(dot(a,x) for x in points)==b
    for query in p['membership_queries']:
        m=query['m'];point=tuple(map(Q,query['point']));answer=query['result']
        if answer['admitted']:
            lo,hi=lift(m,point,answer['lift']);assert list(map(Q,answer['vertical_bounds']))==[lo,hi]
        else:
            a,b=support(m,answer['separator']);assert dot(a,point)>b
        if m in reference:
            actual=all(dot(tuple(map(Q,f['normal'])),point)<=Q(f['upper']) for f in reference[m]['facets'])
            assert actual==answer['admitted']
    traces={'source-dependent':[((Q(1),Q(0)),Q(50)),((Q(-1),Q(0)),Q(-25)),((Q(0),Q(-1)),Q(-75))],
      'coupled-refinement':[((Q(1),Q(0)),Q(50)),((-Q(1,2),Q(1)),Q(0)),((Q(0),Q(-1)),Q(-30))]}
    for query in p['refinement_queries']:
        check_lp(query,traces[query['trace']][:query['stage']])
        assert (query['result']['status']=='INCONSISTENT')==(query['stage']==3)
    for query in p['reset_controls']:
        check_lp(query,[traces[query['trace']][-1]]);assert query['result']['status']=='OPTIMAL'
    # Corruptions must fail arithmetic/admission, not merely a checksum check.
    bad=copy.deepcopy(p['support_queries'][0]['result']);bad['upper']=str(Q(bad['upper'])+1)
    try:support(p['support_queries'][0]['m'],bad)
    except AssertionError:pass
    else:raise AssertionError('bad support accepted')
    positive=next(q for q in p['membership_queries'] if q['result']['admitted'])
    bad=copy.deepcopy(positive['result']['lift']);bad['theta']='2'
    try:lift(positive['m'],tuple(map(Q,positive['point'])),bad)
    except AssertionError:pass
    else:raise AssertionError('bad source lift accepted')
    original=p['refinement_queries'][0];bad=copy.deepcopy(original);i,value=bad['result']['dual'][0];bad['result']['dual'][0]=[i,str(Q(value)+1)]
    try:check_lp(bad,traces[bad['trace']][:bad['stage']])
    except AssertionError:pass
    else:raise AssertionError('bad dual accepted')
    original=next(q for q in p['refinement_queries'] if q['stage']==3);bad=copy.deepcopy(original)
    del bad['result']['rows'][next(i for i,row in enumerate(bad['result']['rows']) if row['kind']=='frame')]
    try:check_lp(bad,traces[bad['trace']])
    except AssertionError:pass
    else:raise AssertionError('forgotten frame accepted')
    result={'passed':True,'report_sha256':sha(rp),'support_queries':len(p['support_queries']),
      'membership_queries':len(p['membership_queries']),'persistent_queries':len(p['refinement_queries']),
      'reset_controls':len(p['reset_controls']),'corruptions_rejected':4,'largest_m':1024,
      'qualification':'Source generators and all run-specific frames are retained. Certificates avoid full facet materialization, not arithmetic growth or evidence-dependent storage.',
      'scope':c['scope']}
    (OUT/'symbolic-tail-interface-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
