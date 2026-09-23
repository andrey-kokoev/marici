"""Reuse only independent certificate replay, not the query engine."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
import json,gzip,hashlib
from verify_symbolic_tail_interface import check_lp,support,lift,model
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def image(t):return sum(t),sum(x*Q(1,128**j) for j,x in enumerate(t))
def main():
    cp=OUT/'symbolic-interface-coherence-levels-contract.json';pp=OUT/'symbolic-interface-coherence-levels-packet.json.gz';rp=OUT/'symbolic-interface-coherence-levels.json'
    c,r=load(cp),load(rp)
    assert sha(cp)==r['contract_sha256'] and sha(pp)==r['packet_sha256']
    assert sha(Path(__file__).with_name('check_symbolic_tail_interface.py'))==c['engine_sha256']
    assert sha(OUT/'symbolic-tail-interface.json')==c['owning_report_sha256']
    with gzip.open(pp,'rt') as f:p=json.load(f)
    frames=[((Q(1),Q(0)),Q(50)),((Q(-1),Q(0)),Q(-25)),((-Q(1,2),Q(1)),Q(0))]
    for query in p['queries']:
        assert sorted(query['order'])==[0,1,2]
        check_lp(query,[frames[i] for i in query['order']])
        last=Q(1,128**(query['m']-1));objective=tuple(map(Q,query['objective']))
        if objective==(0,1):expected=(Q(50),Q(25))
        elif objective==(-1,0):expected=(Q(25),25*last)
        else:assert objective in ((1,0),(1,-1));expected=(Q(50),50*last)
        assert tuple(map(Q,query['result']['point']))==expected
        assert Q(query['result']['value'])==sum(a*b for a,b in zip(objective,expected))
    for group in p['order_groups']:
        assert len(group)==6
        queries=[p['queries'][i] for i in group]
        assert {tuple(q['order']) for q in queries}==set(permutations(range(3)))
        assert len({(q['m'],tuple(q['objective'])) for q in queries})==1
        baseline=queries[0]['result']
        assert all(all(q['result'][key]==baseline[key] for key in ('point','value','lift')) for q in queries)
    d=p['saturation_diamond'];start,mid,end=[tuple(map(Q,d[name])) for name in ('start','middle','end')]
    for x in (start,mid,end):assert all(0<=v<=100+2*j for j,v in enumerate(x))
    assert image(start)[0]==image(mid)[0] and image(mid)[1]==image(end)[1]
    target=tuple(map(Q,d['reverse_middle_observables']));assert target==(image(end)[0],image(start)[1])
    answer=d['reverse_membership'];assert not answer['admitted'];a,b=support(3,answer['separator'])
    assert sum(x*y for x,y in zip(a,target))>b
    # Independent universal lower slope bound also proves the reverse fiber empty.
    smallest=Q(1,128**2);assert target[1]<smallest*target[0]
    witness=p['lift_routes'];point=tuple(map(Q,witness['observable_midpoint']))
    certificate=witness['direct_certificate'];assert certificate['admitted'];lift(3,point,certificate['lift'])
    direct=tuple(map(Q,witness['direct_source_lift']));other=tuple(map(Q,witness['interpolated_source_lift']))
    left,right=[tuple(map(Q,witness[k])) for k in ('left','right')]
    for t in (direct,other,left,right):assert all(0<=v<=100+2*j for j,v in enumerate(t))
    assert other==tuple((a+b)/2 for a,b in zip(left,right))
    assert image(direct)==image(other)==point
    assert point==tuple((a+b)/2 for a,b in zip(image(left),image(right)))
    assert direct[2]>0 and other[2]==0 and direct!=other
    result={'passed':True,'report_sha256':sha(rp),'refinement_certificates':len(p['queries']),
      'order_groups':len(p['order_groups']),'reverse_saturation_fiber_empty':True,'valid_but_distinct_source_lifts':True,
      'scope':'Set-valued query correctness and a fixed selector, not proof-relevant interchange or braid coherence.'}
    (OUT/'symbolic-interface-coherence-levels-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
