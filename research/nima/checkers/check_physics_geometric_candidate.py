"""Exact symmetric-power metric and routed cavity/detector geometry controls."""
import argparse
import itertools
import json
from fractions import Fraction as F
from hashlib import sha256
from math import factorial, prod
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/nima/contracts/physics-geometric-candidate.v1.json'
DIM=10
VAC=(0,)*DIM

def require(ok,why):
    if not ok:raise ValueError(why)

def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()
def eye():return [[F(i==j) for j in range(DIM)] for i in range(DIM)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(DIM)) for j in range(DIM)] for i in range(DIM)]
def occupation(indices):return tuple(indices.count(j) for j in range(DIM))
def basis(n):return [occupation(list(indices)) for indices in itertools.combinations_with_replacement(range(DIM),n)]
def weight(n):return prod(factorial(k) for k in n)
def inner(a,b):return sum(v*b.get(n,0)*weight(n) for n,v in a.items())

def round_map(k):
    require(type(k) is int and 0<=k<3,'round index')
    # Input slots (u,x,v2,w); keep x_next in returning slot zero.
    indices=(1+3*k,0,2+3*k,3+3*k);w=eye()
    for j,src in enumerate(indices):
        u,x,v,e=(F(i==j) for i in range(4))
        yr=-F(3,5)*u+F(4,5)*x;f=F(4,5)*u+F(3,5)*x
        yt=F(3,5)*f-F(4,5)*v;b=F(4,5)*f+F(3,5)*v
        xn=F(3,5)*b+F(4,5)*e;ye=-F(4,5)*b+F(3,5)*e
        for row,val in zip(indices,(yr,xn,yt,ye)):w[row][src]=val
    return w

def lift_column(w,n):
    p={VAC:F(1)}
    for j,multiplicity in enumerate(n):
        for _ in range(multiplicity):
            q={}
            for occupancy,coefficient in p.items():
                for i in range(DIM):
                    if not w[i][j]:continue
                    target=list(occupancy);target[i]+=1;target=tuple(target)
                    q[target]=q.get(target,F(0))+coefficient*w[i][j]
            p={key:value for key,value in q.items() if value}
    return p

def lift_state(w,state):
    out={}
    for n,a in state.items():
        for m,b in lift_column(w,n).items():out[m]=out.get(m,F(0))+a*b
    return {m:a for m,a in out.items() if a}

def evolve(w,branches):return [(memory,lift_state(w,state)) for memory,state in branches]

def instrument(port,outcome,branches):
    require(type(port) is int and 0<=port<DIM and outcome in ('C','N'),'instrument type')
    require(all(n[port]<=1 for _,s in branches for n,a in s.items() if a),'multiphoton input outside instrument domain')
    # Local Kraus labels (input number, input memory, output memory, amplitude).
    ks=[(1,'R','D',F(3,5))] if outcome=='C' else [
        (0,'R','R',F(1)),(1,'R','R',F(4,5)),
        (0,'D','R',F(3,5)),(0,'D','D',F(4,5)),
        (1,'D','R',F(3,5)),(1,'D','D',F(4,5))]
    out=[]
    for memory,state in branches:
        for n0,mi,mo,a in ks:
            if mi!=memory:continue
            s={}
            for n,c in state.items():
                if n[port]!=n0:continue
                target=list(n);target[port]=0;target=tuple(target)
                s[target]=s.get(target,F(0))+a*c
            s={n:c for n,c in s.items() if c}
            if s:out.append((mo,s))
    return out

def probability(branches):return sum(inner(s,s) for _,s in branches)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pin',action='store_true');args=parser.parse_args()
    c=load(CONTRACT);paths={CONTRACT,c['charter'],c['interface']}|set(c['source_evidence'])
    pins_path=ROOT/c['source_pins']
    if args.pin:
        require(not pins_path.exists(),'refusing implicit re-pin')
        pins_path.write_text(json.dumps({'source_sha256':{p:sha(p) for p in sorted(paths)}},indent=2)+'\n',encoding='utf-8')
    pins=load(c['source_pins']);require(set(pins['source_sha256'])==paths,'pin coverage')
    for p,h in pins['source_sha256'].items():require(sha(p)==h,'source drift: '+p)
    require(c['native_source_comparison'] is None and not c['physical_realization_admitted']
            and not c['source_law_independently_selected'],'scope promotion')
    require(load(c['interface'])['charter']==c['charter'],'interface/charter mismatch')
    ws=[round_map(k) for k in range(3)];gram_count=0;composition_count=0
    sector_dimensions={}
    for n in range(3):
        bs=basis(n);sector_dimensions[str(n)]=len(bs)
        for w in ws:
            cols=[lift_column(w,b) for b in bs]
            for i,j in itertools.product(range(len(bs)),repeat=2):
                require(inner(cols[i],cols[j])==(weight(bs[i]) if i==j else 0),'factorial metric square')
                gram_count+=1
        for b in bs:
            direct=lift_column(mm(ws[1],ws[0]),b)
            staged=lift_state(ws[1],lift_column(ws[0],b))
            require(direct==staged,'symmetric-power composition')
            require(all(sum(o)==n for o in direct),'number sector drift')
            composition_count+=1
    require(mm(ws[1],ws[0])!=mm(ws[0],ws[1]),'ordered-history hostile')
    col=lift_column(ws[0],occupation([0,0]))
    require(sum(x*x for x in col.values())!=1,'wrong Euclidean occupation metric not detected')
    initial={occupation([1]):F(4,5),occupation([0]):F(3,5)}
    opposite={occupation([1]):F(4,5),occupation([0]):F(-3,5)}
    first=lift_state(ws[0],initial);phase_other=lift_state(ws[0],opposite)
    require(first.get(occupation([1]),0)==0 and phase_other[occupation([1])]==F(-24,25),'phase-erasure hostile')
    require(inner(initial,initial)==inner(first,first)==1,'initial/source metric')
    joint={}
    for y,z in itertools.product('CN',repeat=2):
        b=instrument(2,y,[('R',first)]);b=evolve(ws[1],b);b=instrument(5,z,b)
        joint[y+z]=probability(b)
    require(sum(joint.values())==1,'joint record normalization')
    pfirst=probability(instrument(2,'C',[('R',first)]))
    reference=c['overlap']['two_step_predictions']
    require(pfirst==F(reference['first_click']) and joint['NC']==F(reference['first_N_second_C'])
            and joint['CC']==F(reference['first_C_second_C']),'routed prediction drift')
    # Independent amplitude route: retained x passes the second cavity then detector.
    transmitted_second=F(3,5)*F(3,5)*F(12,25)
    require(joint['NC']==F(9,25)*transmitted_second**2,'port-amplitude/joint-instrument square')
    # Fixed-number sectors have no adjacent-number coherence: <a_j>=0.
    lowered={VAC:initial.get(occupation([1]),0)}
    require(inner(initial,lowered)==0 and initial[occupation([1])]!=0,'wave coefficient/field-mean distinction')
    try:instrument(2,'N',[('R',{occupation([2,2]):F(1)})])
    except ValueError:guard=True
    else:raise AssertionError('silently truncated multiphoton input')
    # Distinct local Kraus labels must preserve spectator coherence, not dephase every mode.
    spectator={occupation([0]):F(3,5),occupation([1]):F(4,5)}
    branches=instrument(2,'N',[('R',spectator)])
    require(branches==[('R',spectator)],'spectator coherence erased')
    result={'schema':c['schema'],'status':'pass','source_id':c['source_id'],
        'sector_dimensions':sector_dimensions,'factorial_metric_entries':gram_count,
        'composition_columns':composition_count,'joint_record_probabilities':{k:str(v) for k,v in joint.items()},
        'first_click':str(pfirst),'spectator_coherence_preserved':True,'multiphoton_guard':guard,
        'hostiles_detected':['wrong occupation metric','relative-phase erasure','reversed rounds',
            'silent multiphoton projection','wave coefficient as field mean'],
        'verification':'Exact rational finite sectors N=0,1,2; analytic symmetric-power/coherent-state construction stated separately',
        'coherent_truncation_error_bound_supplied':False,'physical_realization_admitted':False,
        'native_carrier_identification_supplied':False,'source_sha256':pins['source_sha256'],
        'checker_sha256':sha(Path(__file__))}
    (ROOT/c['result']).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':main()
