"""Exact countermodels to weak optical and classical-record law selection."""
import argparse
import itertools
import json
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import check_physics_geometric_candidate as G

ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/nima/contracts/physics-dynamics-selection-audit.v1.json'

def require(ok,why):
    if not ok:raise ValueError(why)

def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()

def clean(s):return {n:a for n,a in s.items() if a}
def add(a,b):return clean({n:a.get(n,0)+b.get(n,0) for n in a.keys()|b.keys()})
def scale(q,s):return clean({n:q*a for n,a in s.items()})
def twist(s,t=1):return clean({n:(-1)**(t*sum(n)*(sum(n)-1)//2)*a for n,a in s.items()})
def rival(w,s,t=1):return twist(G.lift_state(w,s),t)

def local_rival(w,s,active=(0,1,2,3),t=1):
    # Local Kerr completion preserves every spectator mode, including future inputs.
    out=G.lift_state(w,s)
    return {n:(-1)**(t*sum(n[i] for i in active)*(sum(n[i] for i in active)-1)//2)*a
            for n,a in out.items()}

def create(j,s):
    out={}
    for n,a in s.items():
        m=list(n);m[j]+=1;m=tuple(m);out[m]=a
    return out

def annihilate(j,s):
    out={}
    for n,a in s.items():
        if n[j]:
            m=list(n);m[j]-=1;m=tuple(m);out[m]=n[j]*a
    return out

def linear_create(w,j,s):
    out={}
    for i in range(G.DIM):out=add(out,scale(w[i][j],create(i,s)))
    return out

def optical(c):
    w,v=G.round_map(0),G.round_map(1);composed=G.mm(v,w);compositions=0;covariances=0;rival_failures=0
    for n in range(3):
        for b in G.basis(n):
            s={b:F(1)};r=rival(w,s)
            require(G.inner(r,r)==G.weight(b),'rival metric preservation')
            require(all(sum(k)==n for k in r),'rival number preservation')
            require(rival(v,r)==rival(composed,s,2),'additive-duration composition')
            require(rival(G.eye(),s,0)==s,'identity event')
            if n<=1:require(r==G.lift_state(w,s),'vacuum/one-particle agreement')
            compositions+=1
            if n<=1:
                for j in range(G.DIM):
                    require(G.lift_state(w,create(j,s))==linear_create(w,j,G.lift_state(w,s)),'reference creation covariance')
                    covariances+=1
                    if rival(w,create(j,s))!=linear_create(w,j,r):rival_failures+=1
    psi={G.VAC:F(1,2),G.occupation([0]):F(1,2),G.occupation([0,0]):F(1,2)}
    reference=G.lift_state(w,psi);alternative=rival(w,psi)
    require(G.inner(psi,psi)==G.inner(reference,reference)==G.inner(alternative,alternative)==1,'witness norm')
    number=lambda s:sum(sum(n)*a*a*G.weight(n) for n,a in s.items())
    require(number(reference)==number(alternative)==F(5,4),'number witness')
    mean=lambda s:G.inner(s,annihilate(1,s))
    expected=c['optical_rival']['finite_witness']
    require(mean(reference)==F(expected['reference_reflected_field_mean']) and
            mean(alternative)==F(expected['rival_reflected_field_mean']),'field-mean discriminator')
    s={G.occupation([0]):F(1)}
    residual=add(rival(w,create(0,s)),scale(-1,linear_create(w,0,rival(w,s))))
    require(G.inner(residual,residual)==F(expected['creation_square_residual_norm_squared']),'creation residual')
    # Existing routed preparation never leaves N<=1, including outcome updates.
    initial={G.occupation([1]):F(4,5),G.occupation([0]):F(3,5)}
    joint={}
    for y,z in itertools.product('CN',repeat=2):
        reference_b=G.instrument(2,y,[('R',G.lift_state(w,initial))])
        rival_b=G.instrument(2,y,[('R',rival(w,initial))])
        reference_b=G.instrument(5,z,G.evolve(v,reference_b))
        rival_b=G.instrument(5,z,[(m,rival(v,s)) for m,s in rival_b])
        require(reference_b==rival_b,'one-photon history changed')
        joint[y+z]=str(G.probability(rival_b))
    require(rival_failures==100,'creation hostile coverage')
    local=local_rival(w,psi)
    require(mean(local)==mean(alternative) and number(local)==number(reference),'local phase witness')
    local_failures=0;spectator_squares=0
    for n in range(3):
        for b in G.basis(n):
            s={b:F(1)};ls=local_rival(w,s)
            require(G.inner(ls,ls)==G.weight(b),'local rival metric')
            if n<=1:
                for j in range(G.DIM):
                    lhs=local_rival(w,create(j,s));rhs=linear_create(w,j,ls)
                    if j>=4:
                        require(lhs==rhs,'spectator operation changed');spectator_squares+=1
                    elif lhs!=rhs:local_failures+=1
    require(local_failures==16 and spectator_squares==66,'local support controls')
    return {'local_rival_field_mean':str(mean(local)),
            'local_rival_failed_creation_squares':local_failures,
            'preserved_spectator_creation_squares':spectator_squares,
            'composition_columns':compositions,'reference_creation_squares':covariances,
            'rival_failed_creation_squares':rival_failures,'reference_field_mean':str(mean(reference)),
            'rival_field_mean':str(mean(alternative)),'common_mean_number':'5/4',
            'creation_residual_norm_squared':str(G.inner(residual,residual)),
            'unchanged_routed_records':joint}


def zero():return [[F(0) for _ in range(4)] for _ in range(4)]
def matadd(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def tr(a):return list(map(list,zip(*a)))
def trace(a):return sum(a[i][i] for i in range(4))
def transition(o,i,a):
    m=zero();m[o][i]=a;return m

def apply(ks,rho):
    out=zero()
    for k in ks:out=matadd(out,mm(mm(k,rho),tr(k)))
    return out

def detector():
    vr=transition(0,0,F(1));ds=transition(2,2,F(4,5))
    click=[transition(2,1,F(3,5))]
    rest=[transition(0,1,F(4,5)),transition(0,2,F(3,5)),
          transition(0,3,F(3,5)),transition(2,3,F(4,5))]
    reference={'C':click,'N':[vr,ds]+rest};rival_ops={'C':click,'N':[matadd(vr,ds)]+rest}
    for ops in (reference,rival_ops):
        completeness=zero()
        for ks in ops.values():
            for k in ks:completeness=matadd(completeness,mm(tr(k),k))
        require(completeness==[[F(i==j) for j in range(4)] for i in range(4)],'CP completeness')
    for i,y in itertools.product(range(4),'CN'):
        rho=transition(i,i,F(1))
        require(apply(reference[y],rho)==apply(rival_ops[y],rho),'diagonal action difference')
    coherent=zero()
    for i,j in itertools.product((0,2),repeat=2):coherent[i][j]=F(1,2)
    a=apply(reference['N'],coherent);b=apply(rival_ops['N'],coherent)
    require(trace(a)==trace(b)==1 and a[0][2]==0 and b[0][2]==F(2,5),'coherent-memory hostile')
    require(a[0][0]==b[0][0]==F(17,25) and a[2][2]==b[2][2]==F(8,25),'same classical memory')
    cases=0
    for ready in (F(0),F(1,2),F(1)):
        for length in range(1,4):
            for inputs,word in itertools.product(itertools.product((0,1),repeat=length),itertools.product('CN',repeat=length)):
                a=zero();a[0][0]=ready;a[2][2]=1-ready;b=[r[:] for r in a]
                for n,y in zip(inputs,word):
                    def prepare(rho):
                        p=zero();p[n][n]=rho[0][0];p[2+n][2+n]=rho[2][2];return p
                    a=apply(reference[y],prepare(a));b=apply(rival_ops[y],prepare(b))
                require(a==b,'classical history distinction');cases+=1
    return {'completeness_entries':32,'diagonal_outcome_maps':8,'identical_classical_histories':cases,
            'reference_coherent_memory_X':'0','rival_coherent_memory_X':'4/5',
            'coherent_memory_intervention_in_current_charter':False}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pin',action='store_true');args=parser.parse_args()
    c=load(CONTRACT);paths={CONTRACT,c['geometry'],c['interface']}|set(c['source_evidence'])
    p=ROOT/c['source_pins']
    if args.pin:
        require(not p.exists(),'refusing implicit re-pin')
        p.write_text(json.dumps({'source_sha256':{s:sha(s) for s in sorted(paths)}},indent=2)+'\n',encoding='utf-8')
    pins=load(c['source_pins']);require(set(pins['source_sha256'])==paths,'pin coverage')
    for s,h in pins['source_sha256'].items():require(sha(s)==h,'source drift: '+s)
    require(load(c['geometry'])['source_id']==c['source_id'],'candidate identity')
    require(c['conditional_uniqueness']['independent_source_justification_supplied'] is False and
            c['disposition']['native_relational_source_law_selected'] is False and
            c['disposition']['physical_realization_admitted'] is False,'unsupported selection')
    result={'schema':c['schema'],'status':'pass','disposition':c['disposition'],
            'optical':optical(c),'detector':detector(),
            'source_sha256':pins['source_sha256'],'checker_sha256':sha(Path(__file__)),
            'compiler_rerun':False,'owner_suites_rerun':False}
    (ROOT/c['result']).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':main()
