"""Frozen target-scope review, independent exact instruments and decision controls."""
import argparse
import copy
import itertools
import json
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/nima/contracts/physics-target-charter.v1.json'

def require(ok,why):
    if not ok:raise ValueError(why)

def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()
def digest(x):return sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def paths(c):return {CONTRACT,c['catalog'],c['catalog_predecessor'],c['source_register']}|set(c['source_evidence'])


def validate(c,pins,catalog):
    old=load(c['catalog_predecessor'])
    require(catalog['targets']==old['targets']+c['catalog_extensions'],'catalog inheritance/extension drift')
    require(catalog['deferred_expansions']==old['deferred_expansions'],'lost expansion gates')
    selected=c['selected_physical_targets']; ts={t['id']:t for t in c['targets']}
    require(len(selected)==len(set(selected))==2 and set(selected)==set(ts),'target coverage')
    cat={t['id']:t for t in catalog['targets']}
    require(all(k in cat and cat[k]['class']=='physical_target_candidate' for k in selected),'structural-as-physical')
    require(set(selected)=={t['id'] for t in c['catalog_extensions']},'unreviewed instance')
    require(c['common_source_witness_id'] is None and c['physical_realization_admitted'] is False
            and c['empirical_evidence_admitted'] is False,'charter promoted to realization')
    register=load(c['source_register']); sources={s['id']:s for s in register['sources']}
    specs={r[0]:r for r in register['ingredient_specs']}
    expected={'reciprocal-lossy-cavity-ordered-response':'instrument.reciprocal-lossy-cavity.v1',
              'finite-dead-time-detector-records':'instrument.dead-time-detector.v1'}
    require({k:t['source_id'] for k,t in ts.items()}==expected,'source identity mismatch')
    for k,t in ts.items():
        require(t['source_id'] in sources and all(t.get(f) for f in ('regime','nominal_fixture','ordered_law',
            'observation_law','recovery_contract','source_derivation_task','exact_success','independent_test_route',
            'falsifier','reference_predictions','rivals','excluded_extensions')),'untyped target contract')
        require(t['regime']['maximum_steps']==3,'unreviewed history extension')
        require('not measured' in t['nominal_fixture']['status'],'fixture promoted to calibration')
        require(set(t['ingredient_records'])==set(sources[t['source_id']]['ingredient_records']),'ingredient coverage')
        require(all(specs[r][1]==t['source_id'] and specs[r][2] in ('imported_physical_theory','instrument_specification')
                    for r in t['ingredient_records']),'ingredient role/source drift')
        require(cat[k]['required_bindings']==['instrument-common-source-binding'],'missing physical map gate')
    e=c['empirical_acceptance']
    require(e['acquired_dataset'] is None and F(e['epsilon'])==F(1,100),'unreviewed data/tolerance')
    require(len(e['protocol_gate'])==6 and e['normalization'] and e['rule'],'empirical protocol gate')
    require(2*(F(e['per_target_calibration_failure_budget'])+F(e['per_target_validation_failure_budget']))
            <=F(e['familywise_error_budget'])==F(1,100),'error budget overspent')
    o=c['overlap_obligation']
    require(o['status']=='missing_comparison' and len(o['routes'])==2 and len(o['required_maps'])==4,'unsupported overlap')
    require(set(pins['source_sha256'])==paths(c),'pin coverage')
    for p,h in pins['source_sha256'].items():require(sha(p)==h,'source drift: '+p)
    return ts


def cavity(t):
    r1,t1,r2,t2,a,ell=(F(t['nominal_fixture'][k]) for k in ('r1','t1','r2','t2','a','ell'))
    require(r1*r1+t1*t1==r2*r2+t2*t2==a*a+ell*ell==1,'component normalization')
    def step(v):
        u,x,v2,w=v;yr=-r1*u+t1*x;f=t1*u+r1*x
        yt=t2*f-r2*v2;b=r2*f+t2*v2
        return (yr,yt,a*b+ell*w,-ell*b+a*w)
    cols=[step(tuple(F(i==j) for i in range(4))) for j in range(4)]
    for i,j in itertools.product(range(4),repeat=2):
        require(sum(x*y for x,y in zip(cols[i],cols[j]))==int(i==j),'complete dilation square')
    A=a*r2*r1;B=a*r2*t1;count=0
    for x0,u0,u1 in itertools.product((F(0),F(1),F(-1,2)),repeat=3):
        one=step((u0,x0,F(0),F(0)));two=step((u1,one[2],F(0),F(0)))
        require(one[2]==A*x0+B*u0 and two[2]==A*A*x0+A*B*u0+B*u1,'two-step state square')
        require(sum(z*z for z in one)==x0*x0+u0*u0,'complete resource square')
        count+=1
    ref=t['reference_predictions'];dark=step(tuple(map(F,ref['dark_input'])))
    require(dark==tuple(map(F,ref['dark_output'])) and dark[0]==0 and dark[2]!=0,'dark-state fixture')
    nxt=step((F(0),dark[2],F(0),F(0)))
    require(nxt[0]==F(ref['next_zero_drive_reflected'])!=0,'retained continuation')
    require(sum(z*z for z in dark[:2])<1,'compressed-unitary hostile')
    # Input/return mixing and loss on the return slot do not commute.
    v=(F(1),F(1),F(0),F(0))
    mirror=lambda v:(-r1*v[0]+t1*v[1],t1*v[0]+r1*v[1],v[2],v[3])
    attenuation=lambda v:(v[0],a*v[1]+ell*v[3],v[2],-ell*v[1]+a*v[3])
    require(mirror(attenuation(v))!=attenuation(mirror(v)),'component order hostile')
    return {'orthogonality_entries':16,'composed_state_resource_cases':count,
            'dark_output':list(map(str,dark)),'next_zero_drive_reflected':str(nxt[0]),
            'hostiles':['state deletion after dark reflection','closed-unitary compression','unordered components']}


def sqrt_fraction(q):
    n,d=isqrt(q.numerator),isqrt(q.denominator)
    require(n*n==q.numerator and d*d==q.denominator,'nonrational fixture amplitude')
    return F(n,d)


def detector(t):
    # Joint basis: |0,R>,|1,R>,|0,D>,|1,D>. Each rank-one Kraus label is separate.
    def operators(eta,gamma):
        return {'C':[(2,1,sqrt_fraction(eta))],
                'N':[(0,0,F(1)),(0,1,sqrt_fraction(1-eta)),
                     (0,2,sqrt_fraction(gamma)),(2,2,sqrt_fraction(1-gamma)),
                     (0,3,sqrt_fraction(gamma)),(2,3,sqrt_fraction(1-gamma))]}
    def joint(inputs,word,initial,ops):
        state=[initial[0],F(0),initial[1],F(0)]
        for photon,outcome in zip(inputs,word):
            prepared=[F(0)]*4;prepared[photon]=state[0];prepared[2+photon]=state[2]
            state=[F(0)]*4
            for out,src,amp in ops[outcome]:state[out]+=amp*amp*prepared[src]
        return state[0],state[2]
    def memory(inputs,word,initial,eta,gamma):
        ready,dead=initial
        for photon,outcome in zip(inputs,word):
            if outcome=='C':ready,dead=F(0),eta*photon*ready
            else:ready,dead=(1-eta*photon)*ready+gamma*dead,(1-gamma)*dead
        return ready,dead
    count=0;normalizations=0;completeness=0
    for eta,gamma in itertools.product((F(9,25),F(16,25),F(1)),repeat=2):
        ops=operators(eta,gamma)
        for i in range(4):
            require(sum(amp*amp for entries in ops.values() for _,src,amp in entries if src==i)==1,'Kraus completeness')
            completeness+=1
        for initial in ((F(1),F(0)),(F(0),F(1)),(F(1,2),F(1,2))):
            for n in range(4):
                for inputs in itertools.product((0,1),repeat=n):
                    total=F(0)
                    for word in itertools.product('CN',repeat=n):
                        a=joint(inputs,word,initial,ops);b=memory(inputs,word,initial,eta,gamma)
                        require(a==b,'joint/memory history square');total+=sum(a);count+=1
                    require(total==1,'complete record normalization');normalizations+=1
    eta=F(t['nominal_fixture']['eta']);gamma=F(t['nominal_fixture']['gamma']);ops=operators(eta,gamma)
    prob=lambda inputs,word:sum(joint(inputs,word,(F(1),F(0)),ops))
    vals={'p_CC_given_inputs_11':prob((1,1),'CC'),'p_NC_given_inputs_11':prob((1,1),'NC'),
          'p_CNC_given_inputs_101':prob((1,0,1),'CNC'),
          'p_next_C_after_one_empty_gap_given_previous_C':prob((1,0,1),'CNC')/eta,
          'iid_reset_p_CC':eta*eta}
    require(vals=={k:F(v) for k,v in t['reference_predictions'].items()},'detector prediction drift')
    require(vals['p_CC_given_inputs_11']!=vals['iid_reset_p_CC'],'iid hostile lost')
    require(prob((1,1),'NN')>0 and sum(prob((1,1),w) for w in ('CC','CN','NC'))<1,
            'discarded no-click record hostile lost')
    return {'history_squares':count,'normalizations':normalizations,'completeness_entries':completeness,
            'predictions':{k:str(v) for k,v in vals.items()},'domain':'classical memory, sharp zero/one optical preparations',
            'hostiles':['iid memory reset','postselection removing no-click records']}


def interval_decision(c,p,epsilon):
    require(len(c)==len(p)>0 and all(lo<=hi for lo,hi in c+p),'empty or invalid confidence/prediction box')
    low=max(max(F(0),a-d,b-e) for (a,e),(b,d) in zip(c,p))
    high=max(max(abs(a-d),abs(e-b)) for (a,e),(b,d) in zip(c,p))
    return 'reject' if low>epsilon else 'accept' if high<=epsilon else 'inconclusive'


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pin',action='store_true');args=parser.parse_args()
    c=load(CONTRACT)
    if args.pin:
        require(not (ROOT/c['source_pins']).exists() and not (ROOT/c['catalog']).exists(),'refusing implicit re-freeze')
        old=load(c['catalog_predecessor'])
        catalog=dict(old,schema='marici.physics-target-catalog.v3',id='physics-target-catalog.v3',
            predecessor=c['catalog_predecessor'],selection_status='reviewed_primary_instance_pair',
            targets=old['targets']+c['catalog_extensions'])
        (ROOT/c['catalog']).write_text(json.dumps(catalog,indent=2)+'\n',encoding='utf-8')
        (ROOT/c['source_pins']).write_text(json.dumps({'schema':'marici.physics-target-charter.pins.v1',
            'source_sha256':{p:sha(p) for p in sorted(paths(c))}},indent=2)+'\n',encoding='utf-8')
    catalog=load(c['catalog']);pins=load(c['source_pins']);ts=validate(c,pins,catalog)
    checks={'cavity':cavity(ts[c['selected_physical_targets'][0]]),'detector':detector(ts[c['selected_physical_targets'][1]])}
    prediction=[(F(358,1000),F(362,1000))];epsilon=F(c['empirical_acceptance']['epsilon'])
    decisions=[interval_decision([(F(a,1000),F(b,1000))],prediction,epsilon)
               for a,b in ((359,361),(480,520),(340,380))]
    require(decisions==['accept','reject','inconclusive'],'decision controls')
    rejected=[]
    for name in ('duplicate-target','missing-target','wrong-source','missing-map-gate','fixture-as-calibration',
                 'false-realization','false-empirical','expanded-history','lost-overlap','overspent-error','stale-pin'):
        b=copy.deepcopy(c);p=copy.deepcopy(pins);cat=copy.deepcopy(catalog)
        if name=='duplicate-target':b['selected_physical_targets'][1]=b['selected_physical_targets'][0]
        elif name=='missing-target':b['targets'].pop()
        elif name=='wrong-source':b['targets'][0]['source_id']='native-bool-square-pilot'
        elif name=='missing-map-gate':cat['targets'][-1]['required_bindings']=[];b['catalog_extensions'][-1]['required_bindings']=[]
        elif name=='fixture-as-calibration':b['targets'][0]['nominal_fixture']['status']='measured'
        elif name=='false-realization':b['physical_realization_admitted']=True
        elif name=='false-empirical':b['empirical_evidence_admitted']=True
        elif name=='expanded-history':b['targets'][0]['regime']['maximum_steps']=100
        elif name=='lost-overlap':b['overlap_obligation']['status']='constructed'
        elif name=='overspent-error':b['empirical_acceptance']['per_target_validation_failure_budget']='1/10'
        else:p['source_sha256'][CONTRACT]='0'*64
        try:validate(b,p,cat)
        except ValueError:rejected.append(name)
        else:raise AssertionError('corruption accepted: '+name)
    review={'id':'reviewed-physical-target-scope','type':'reviewed_target_selection',
            'targets':c['selected_physical_targets'],'evidence':['target-charter'],
            'review':'Nima bounded target charter: exact independent model controls, explicit imported inputs, missing common-source maps and frozen empirical decision requirements',
            'catalog_sha256':sha(c['catalog']),'charter':CONTRACT,'charter_sha256':sha(CONTRACT),
            'target_set_sha256':digest(sorted(c['selected_physical_targets']))}
    out={'schema':'marici.physics-target-charter.result.v1','status':'pass','interface_record':review,
         'exact_controls':checks,'interval_decision_controls':decisions,'rejected_corruptions':rejected,
         'source_sha256':pins['source_sha256'],'pins_sha256':sha(c['source_pins']),'checker_sha256':sha(Path(__file__)),
         'empirical_evidence_admitted':False,'physical_realization_admitted':False,'owner_suites_rerun':False}
    (ROOT/c['result']).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('source_sha256',)},indent=2))

if __name__=='__main__':main()
