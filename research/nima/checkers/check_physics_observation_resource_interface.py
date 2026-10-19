"""Exact model interface, filtering and separately typed resource controls."""
import argparse
import itertools
import json
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/nima/contracts/physics-observation-resource-interface.v1.json'

def require(ok,message):
    if not ok:raise ValueError(message)

def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()

def step(n,outcome,state,eta=F(9,25),gamma=F(9,25)):
    require(type(n) is int and n in (0,1) and outcome in ('C','N'),'event type')
    require(0<=eta<=1 and 0<=gamma<=1 and min(state)>=0,'probability domain')
    r,d=state
    return (F(0),eta*n*r) if outcome=='C' else ((1-eta*n)*r+gamma*d,(1-gamma)*d)

def filter_step(n,outcome,r,eta=F(9,25),gamma=F(9,25)):
    require(0<=r<=1,'prior readiness')
    state=step(n,outcome,(r,1-r),eta,gamma);p=sum(state)
    require(p>0,'impossible record: posterior undefined')
    return state[0]/p,p

def interval_filter(n,outcome,bounds,eta=F(9,25),gamma=F(9,25)):
    lo,hi=bounds;require(0<=lo<=hi<=1,'readiness interval')
    a=filter_step(n,outcome,lo,eta,gamma)[0];b=filter_step(n,outcome,hi,eta,gamma)[0]
    require(a<=b,'interval order')
    return a,b

def cavity(u,x,v,w):
    yr=-F(3,5)*u+F(4,5)*x;f=F(4,5)*u+F(3,5)*x
    yt=F(3,5)*f-F(4,5)*v;b=F(4,5)*f+F(3,5)*v
    return yr,yt,F(3,5)*b+F(4,5)*w,-F(4,5)*b+F(3,5)*w

def check_records(records,c,mode='model'):
    require(mode=='model','physical execution lacks reviewed authorization/calibration')
    require(0<len(records)<=c['maximum_steps'],'history horizon')
    known={i['source_id'] for i in c['interfaces']};seen=set();previous=None
    source=records[0]['source_id'];trial=records[0]['trial_id']
    versions=records[0]['calibration_version'],records[0]['clock_version']
    for j,r in enumerate(records):
        require(all(k in r for k in c['record_schema']['required']),'record fields')
        require(r['source_id']==source and source in known and r['trial_id']==trial,'source/trial identity')
        require((r['calibration_version'],r['clock_version'])==versions,'within-trial version change')
        require(r['step']==j and r['previous_record_id']==previous,'history attachment')
        require(r['record_id'] and r['record_id'] not in seen,'occurrence identity')
        require(r['preparation']=='optical-only' if 'detector' in source else r['preparation']=='declared-port-input',
                'undeclared preparation or hidden reset')
        if 'detector' in source:require(type(r['input']) is int and r['input'] in (0,1) and r['outcome'] in ('C','N'),'detector record')
        seen.add(r['record_id']);previous=r['record_id']
    return True

def add_resource(a,b):
    require(a[0]==b[0],'resource dimensions differ')
    return a[0],a[1]+b[1]

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pin',action='store_true');args=parser.parse_args()
    c=load(CONTRACT);paths={CONTRACT,c['charter']}|set(c['source_evidence']);pin=ROOT/c['source_pins']
    if args.pin:
        require(not pin.exists(),'refusing implicit re-pin')
        pin.write_text(json.dumps({'source_sha256':{p:sha(p) for p in sorted(paths)}},indent=2)+'\n',encoding='utf-8')
    pins=load(c['source_pins']);require(set(pins['source_sha256'])==paths,'pin coverage')
    for p,h in pins['source_sha256'].items():require(sha(p)==h,'source drift: '+p)
    charter=load(c['charter'])
    require({i['target'] for i in c['interfaces']}==set(charter['selected_physical_targets']),'target coverage')
    require(c['physical_authorization'] is None and c['calibration_certificate'] is None and c['common_source_map'] is None,'scope promotion')
    cases=0;word_cases=0;interval_cases=0
    for u,x,v,w in itertools.product((F(-1,2),F(0),F(1)),repeat=4):
        yr,yt,xn,ye=cavity(u,x,v,w)
        require(xn*xn-x*x==u*u+v*v+w*w-yr*yr-yt*yt-ye*ye,'energy balance')
        require((yr+F(3,5)*u)/F(4,5)==x,'known-input state reconstruction')
        require(xn==F(36,125)*x+F(48,125)*u+F(9,25)*v+F(4,5)*w,'complete input state map');cases+=1
    for initial in (F(0),F(1,2),F(1)):
        for nsteps in range(1,4):
            for inputs in itertools.product((0,1),repeat=nsteps):
                total=F(0)
                for word in itertools.product('CN',repeat=nsteps):
                    state=(initial,1-initial);r=initial;likelihood=F(1)
                    for n,y in zip(inputs,word):
                        state=step(n,y,state)
                        if sum(state)==0:likelihood=0;break
                        r,p=filter_step(n,y,r);likelihood*=p
                        require(n==int(y=='C')+(n-int(y=='C')) and n-int(y=='C')>=0,'photon resource balance')
                    require(sum(state)==likelihood,'conditional product likelihood')
                    if likelihood:require(r==state[0]/likelihood,'belief/unnormalized square')
                    total+=likelihood;word_cases+=1
                require(total==1,'complete word law')
    bounds=interval_filter(1,'N',(F(1,4),F(3,4)))
    require(bounds==(F(43,91),F(57,73)) and filter_step(1,'N',F(1,2))[0]==F(25,41),'reference filter')
    for eta,gamma in itertools.product((F(1,4),F(9,25),F(3,4)),repeat=2):
        lo,hi=interval_filter(1,'N',(F(1,4),F(3,4)),eta,gamma)
        for k in range(101):
            r=F(1,4)+F(k,200);p=filter_step(1,'N',r,eta,gamma)[0]
            require(lo<=p<=hi,'interval enclosure');interval_cases+=1
    d=F(1)
    for k in range(4):
        require(d==F(16,25)**k,'readiness recovery law');d=step(0,'N',(1-d,d))[1]
    records=[dict(source_id='instrument.dead-time-detector.v1',trial_id='fixture',step=j,
        preparation='optical-only',input=n,outcome=y,calibration_version='nominal-model',clock_version='bin-model',
        previous_record_id=None if j==0 else str(j-1),record_id=str(j))
        for j,(n,y) in enumerate(zip((1,0,1),'CNC'))]
    require(check_records(records,c),'valid record rejected');rejected=[]
    import copy
    bad=copy.deepcopy(records);bad[1]['preparation']='reset-ready'
    missing=copy.deepcopy(records);missing.pop(1)
    retag=copy.deepcopy(records);retag[1]['source_id']='instrument.reciprocal-lossy-cavity.v1'
    for name,action in (
        ('hidden-memory-reset',lambda:check_records(bad,c)),
        ('dropped-no-click',lambda:check_records(missing,c)),
        ('mixed-source-records',lambda:check_records(retag,c)),
        ('unlicensed-physical-execution',lambda:check_records(records,c,'physical')),
        ('impossible-click',lambda:filter_step(0,'C',F(1,2))),
        ('zero-likelihood-no-click',lambda:filter_step(1,'N',F(1),F(1))),
        ('interval-support-restriction',lambda:interval_filter(1,'C',(F(0),F(1)))),
        ('readiness-as-energy',lambda:add_resource(('photon-number',F(1)),('readiness',F(1))))):
        try:action()
        except ValueError:rejected.append(name)
        else:raise AssertionError('hostile admitted: '+name)
    result={'status':'pass','schema':c['schema'],'scope':c['status'],'cavity_cases':cases,
        'detector_word_cases':word_cases,'interval_enclosure_cases':interval_cases,
        'no_click_posterior_interval':list(map(str,bounds)),'rejected_hostiles':rejected,
        'source_sha256':pins['source_sha256'],'checker_sha256':sha(Path(__file__)),
        'physical_execution_authorized':False,'common_source_constructed':False}
    (ROOT/c['result']).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':main()
