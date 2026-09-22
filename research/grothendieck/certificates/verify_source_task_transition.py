"""Standalone exact verifier for fixed-data gamma=1 source-task refinements.

No solver, recorder, integration package or repository imports. Analytical
calibration/source-domain assumptions remain external; hashes bind, not prove,
the owning evidence. Reference edges are ALWAYS conditional, not Arb proofs.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json,sys

N=('positive','crossed','vacuum')
ASSUMPTIONS=['real_integer_background_271_direction_source_family',
             'order16_disjoint_path_cost_32_features_8_vacuum',
             'actual_gains_and_source_functionals_in_declared_enclosures',
             'uniform_residual_bound_and_decreasing_order16_tail_ratio',
             'declared_source_budget_is_valid']

def require(ok,message):
    if not ok:raise ValueError(message)
def fields(x,keys):require(type(x) is dict and set(x)==set(keys),'Missing or unknown fields')
def q(x):
    require(type(x) is str,'Rationals must be strings')
    return Q(x)
def box(x):
    require(type(x) is list and len(x)==2,'Expected interval')
    a,b=map(q,x);require(a<=b,'Reversed interval');return a,b
def sha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def hash_value(x):require(type(x) is str and len(x)==64 and all(c in '0123456789abcdef' for c in x),'Bad evidence digest')
def load(path):
    def pairs(items):
        result={}
        for k,v in items:
            require(k not in result,'Duplicate JSON key');result[k]=v
        return result
    def reject(x):raise ValueError('Floating/nonfinite JSON forbidden')
    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=pairs,parse_float=reject,parse_constant=reject)
def subset(old,new):return old[0]<=new[0]<=new[1]<=old[1]
def mul(a,b):
    values=[x*y for x in a for y in b];return min(values),max(values)
def minimum(a):return Q(0) if a[0]<=0<=a[1] else min(abs(x) for x in a)

def problem(p):
    fields(p,('model','mode','raw','gains','sigma','tail_multiplier','budget','assumptions','evidence'))
    require(p['model']=='gamma1-real-cubic-order16-v1','Unsupported source model')
    require(p['mode'] in ('private','reuse'),'Unsupported mode')
    require(p['assumptions']==ASSUMPTIONS,'Changed assumption boundary')
    fields(p['raw'],N);fields(p['gains'],N);fields(p['sigma'],('positive','crossed'))
    fields(p['evidence'],('protocol','filters','calibration'))
    for h in p['evidence'].values():hash_value(h)
    raw={n:box(p['raw'][n]) for n in N};gains={n:box(p['gains'][n]) for n in N}
    require(all(gains[n][0]>0 for n in N),'Nonpositive gain')
    require(gains['vacuum']==(Q(1),Q(1)),'Vacuum coordinate must be unscaled')
    sigma={n:box(p['sigma'][n]) for n in p['sigma']}
    D=q(p['tail_multiplier']);B=q(p['budget'])
    require(D>0 and B>=0,'Invalid tail bound/budget')
    outer={n:mul(raw[n],(1/gains[n][1],1/gains[n][0])) for n in N}
    weights={'positive':32*2**16,'crossed':32*2**16,'vacuum':8*2**16}
    lower=sum(weights[n]*minimum(outer[n]) for n in N)
    return raw,gains,sigma,D,B,outer,weights,lower

def node(p,c):
    raw,gains,sigma,D,B,outer,weights,lower=problem(p)
    common={'version','problem_sha256','status','necessary_cost'}
    status=c.get('status') if type(c) is dict else None
    require(status in ('UNRESOLVED','CERTIFIED_FEASIBLE','CERTIFIED_INFEASIBLE'),'Unknown status')
    extra=set() if status=='CERTIFIED_INFEASIBLE' else {'aggregate_bounds','positive_task'}
    if status=='CERTIFIED_FEASIBLE':extra.add('witness')
    fields(c,common|extra)
    require(type(c['version']) is int and c['version']==1,'Bad version')
    require(c['problem_sha256']==sha(p),'Node digest mismatch')
    require(q(c['necessary_cost'])==lower,'Incorrect necessary cost')
    if status=='CERTIFIED_INFEASIBLE':
        require(lower>B,'No budget contradiction');return
    require(lower<=B,'Contradictory non-infeasible certificate')
    R=B-lower;tv=R/(8*3**16);tr=R*D/(32*3**16)
    x=mul(sigma['positive'],outer['positive']);y=mul(sigma['crossed'],outer['crossed'])
    expected={'vacuum':(outer['vacuum'][0]-tv,outer['vacuum'][1]+tv),
              'residual':(x[0]+y[0]-tr,x[1]+y[1]+tr)}
    fields(c['aggregate_bounds'],expected)
    require(all(box(c['aggregate_bounds'][n])==v for n,v in expected.items()),'Incorrect universal task bounds')
    if status=='CERTIFIED_FEASIBLE':
        fields(c['witness'],N);w={n:q(c['witness'][n]) for n in N}
        require(sum(weights[n]*abs(w[n]) for n in N)<=B,'Witness over budget')
        for n in N:require(subset(raw[n],mul(gains[n],(w[n],w[n]))),'Witness fails gain endpoint')
        # This certificate convention sets every other source coefficient to zero.
    require(type(c['positive_task']) is bool,'Invalid task flag')
    require(c['positive_task']==(status=='CERTIFIED_FEASIBLE' and all(v[0]>0 for v in expected.values())),
            'Vacuous or incorrect task claim')

def edge(old,new,e):
    common={'version','kind','old_sha256','new_sha256'}
    kind=e.get('kind') if type(e) is dict else None
    require(kind in ('identity-calibration-refinement','controlled-reference-restriction'),'Unsupported transition type')
    fields(e,common|({'reference'} if kind=='controlled-reference-restriction' else set()))
    require(type(e['version']) is int and e['version']==1,'Bad edge version')
    require(e['old_sha256']==sha(old) and e['new_sha256']==sha(new),'Edge digest mismatch')
    problem(old);problem(new)
    # No stronger prior, changed target, new channel, frame, or source action is admitted.
    for key in ('model','mode','raw','sigma','tail_multiplier','budget','assumptions'):
        require(old[key]==new[key],'Identity edge changes data, prior, source model or task')
    for key in ('protocol','filters'):
        require(old['evidence'][key]==new['evidence'][key],'Changed deployed protocol')
    for n in N:require(subset(box(old['gains'][n]),box(new['gains'][n])),'Calibration is not nested')
    if kind=='identity-calibration-refinement':
        if old['gains']!=new['gains']:
            require(old['evidence']['calibration']!=new['evidence']['calibration'],
                    'Narrower analytical enclosure requires distinct owning evidence')
        return False
    r=e['reference']
    fields(r,('kind','channel','source_coefficients','interval','premise'))
    require(r['kind']=='hypothetical-known-source-reference-v1','Reference is not an analytical proof')
    require(r['channel']=='positive','Unsupported reference channel')
    require(r['source_coefficients']=={'positive':'1','crossed':'0','vacuum':'0'},'Unknown reference source')
    require(r['premise']=='valid_total_reference_error_including_preparation_and_acquisition','Missing external reference premise')
    observation=box(r['interval']);prior=box(old['gains']['positive'])
    intersection=max(prior[0],observation[0]),min(prior[1],observation[1])
    require(intersection[0]<=intersection[1],'Reference contradicts calibration')
    require(box(new['gains']['positive'])==intersection,'Incorrect reference intersection')
    for n in ('crossed','vacuum'):require(old['gains'][n]==new['gains'][n],'Reference changes unrelated channel')
    require(old['evidence']==new['evidence'],'Reference cannot manufacture analytical evidence')
    return True

def verify(bundle):
    fields(bundle,('version','kind','nodes','certificates','edges','conditional_on_reference'))
    require(type(bundle['version']) is int and bundle['version']==1,'Bad bundle version')
    require(bundle['kind']=='fixed-data-task-transition-chain-v1','Unsupported bundle')
    nodes=bundle['nodes'];certs=bundle['certificates'];edges=bundle['edges']
    require(type(nodes) is list and 2<=len(nodes)<=16,'Invalid chain length')
    require(type(certs) is list and len(certs)==len(nodes),'Missing node certificates')
    require(type(edges) is list and len(edges)==len(nodes)-1,'Missing edges')
    for p,c in zip(nodes,certs):node(p,c)
    conditional=False
    for a,b,e in zip(nodes,nodes[1:],edges):conditional=edge(a,b,e) or conditional
    require(type(bundle['conditional_on_reference']) is bool and bundle['conditional_on_reference']==conditional,
            'Reference premise erased or invented')
    # Identity maps compose to identity; check endpoint nesting independently.
    for n in N:require(subset(box(nodes[0]['gains'][n]),box(nodes[-1]['gains'][n])),'Composite nesting fails')
    return conditional

if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('Usage: python verify_source_task_transition.py bundle.json')
    conditional=verify(load(sys.argv[1]))
    print('VALID exact task transitions; analytical/source assumptions remain external'+
          ('; ALSO CONDITIONAL ON A VALID HYPOTHETICAL REFERENCE' if conditional else ''))
