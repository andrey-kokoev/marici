"""Bounded common-witness definition + exact WG energy regression.
Physical realization remains pending; no shared RH/WG source is invented.
"""
import argparse
import copy
import json
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
SCHEMA='research/conjecture_net/contracts/common-witness-comparison-interface.v1.json'
NOTE='research/voevodsky/common-witness-comparison-interface-v1.md'
OUT='research/voevodsky/results/common-witness-comparison-interface-v1.json'
ENERGY='research/strominger/results/energy-task-reduction.json'
BRANCH='research/conjecture_net/contracts/same-source-compatibility-conjecture-net.v1.json'


def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()
def require(ok,msg):
    if not ok:raise ValueError(msg)


def fixture():
    s=load(SCHEMA)
    source=dict(id='Strominger.supplied.shared-leg-fixture',domain='real factored shared-leg 137-leaf field',
       constructor_digest=sha('research/strominger/checkers/check_energy_task_reduction.py'),
       parameters={'energy':'||A F||^2/4','gain':'supplied common primitive-leg family gain','clock':'supplied native drift'},
       archive={'policy':'full137 leaves, kernels, histories retained','certificate':sha(ENERGY)})
    context=dict(task='predict total coefficient energy',gain_domain='0<=q<=1',
                 nontrivial_gain_available=True,restoration_in_task=False,physical_energy_units=False)
    resources=dict(policy='ideal mathematical forward schedules, same known q; no physical budget attested',
                   independent_response_cell_writes=False)
    def route(target,map_name):
        return dict(source=copy.deepcopy(source),target_type=target,map=map_name,
          context=copy.deepcopy(context),resources=copy.deepcopy(resources),operations=['drift','family_gain'],
          retained=copy.deepcopy(source['archive']),evidence=[ENERGY])
    return dict(left=route('native coefficient field','identity'),right=route('complete retained T9','actual T, decoder L'),
      premises={name:dict(status='premise_unjustified',evidence=[]) for name in s['physical_premises']})


def validate_wg_binding(b):
    """Bounded WG instance validator; not a universal source compiler."""
    s=load(SCHEMA);l,r=b['left'],b['right']
    for route in (l,r):
        require(set(route)==set(s['route_contract']['required']),'route fields')
        require(set(route['source'])==set(s['source_binding']['required']),'source fields')
        require(route['target_type'] and route['map'] and route['evidence'],'untyped/unwitnessed route')
        require(route['retained']==route['source']['archive'],'lost archive')
        require(route['operations']==['drift','family_gain'],'extra source operations')
        require(not route['resources']['independent_response_cell_writes'],'new actuator')
        require(route['context']['gain_domain']=='0<=q<=1' and not route['context']['restoration_in_task'],'changed task; needs new quotient review')
        for p in route['evidence']:require((ROOT/p).is_file(),'missing route evidence')
    require(l['source']==r['source'],'not the same source record/hidden choices')
    require(l['context']==r['context'] and l['resources']==r['resources'],'context/resource mismatch')
    require(set(b['premises'])==set(s['physical_premises']),'missing physical premise')
    for v in b['premises'].values():
        require(v['status'] in s['premise_statuses'],'invalid physical premise status')
        if v['status']=='independently_justified':require(v['evidence'],'physical claim without evidence')
    # This validator checks declarations, not the truth of external physical evidence.
    return 'pending_independent_physical_review'


def step(a,b,q):
    require(0<=q<=1,'gain outside declared domain')
    require(a>=0 and b>=0,'negative coefficient energies')
    return a*q*q,b*q**4


def source_paths():
    return [SCHEMA,NOTE,Path(__file__).relative_to(ROOT).as_posix(),ENERGY,
      'research/strominger/energy-task-reduction.md',
      'research/strominger/checkers/check_energy_task_reduction.py',
      'research/strominger/checkers/energy_task_reduction.py',
      'research/strominger/checkers/check_shared_leg_controllability.py',
      'research/strominger/checkers/shared_leg_control_ports.py',
      'research/strominger/checkers/hamiltonian_descent_wg.py',
      'research/strominger/results/shared-leg-controllability.json',
      'research/strominger/results/retained-hamiltonian-observer.json']


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--record',action='store_true');args=parser.parse_args()
    s=load(SCHEMA);e=load(ENERGY)
    require(not any(s['boundaries'].values()),'schema promotion')
    require(e['verification_status']=='pass' and len(e['checks'])==38,'upstream regression missing')
    for p,digest in e['input_sha256'].items():require(sha('research/'+p)==digest,'energy source drift')
    for key in ('retained-rung4-task-reader','hostile-all-shared-legs-invertible','hostile-same-all-family-means','current-energy-and-means-insufficient-for-next-energy'):
        require(key in e['checks'],'missing actual source witness')
    require(not e['physical_selection_or_calibration'] and not e['new_actuators_added'],'upstream scope drift')
    binding=fixture();require(validate_wg_binding(binding)=='pending_independent_physical_review','physical auto admission')
    a=Q(e['sufficient_statistics']['one_leg']);b=Q(e['sufficient_statistics']['two_leg']);q=Q(1,2)
    H=Q(e['equal_energy_hostile']['current']);one=step(H,Q(0),q);two=step(Q(0),H,q)
    require(sum(one)==Q(e['equal_energy_hostile']['next_one_leg']) and sum(two)==Q(e['equal_energy_hostile']['next_two_leg']),'hostile source mismatch')
    require(sum(one)!=sum(two),'scalar quotient incorrectly predictive')
    checks=['actual-source hostile: equal H and means, unequal next H','pending physical premises preserved']
    for gain in (Q(0),Q(1),Q(1,2),Q(2,3)):
        direct=step(a,b,gain)
        require(direct==(a*gain**2,b*gain**4),'reader contract')
        checks.append('reader gain contract/'+str(gain))
    require(step(*step(a,b,Q(2,3)),Q(3,5))==step(a,b,Q(2,5)),'schedule composition')
    checks.append('composition of forward schedules')
    det=q**4-q*q;require(det!=0,'nontrivial gain not informative')
    total=a+b;after=sum(step(a,b,q))
    inferred_a=(total*q**4-after)/det;inferred_b=(after-total*q*q)/det
    require((inferred_a,inferred_b)==(a,b),'predictive reader inversion')
    checks.append('two readings identify both task coordinates')
    require(all(g**4-g*g==0 for g in (Q(0),Q(1))),'endpoint gain control')
    checks.append('endpoint gains not identification witnesses')
    hostiles=[]
    for name in ('different-source','hidden-normalization','resource-mismatch','context-mismatch','lost-archive','extra-actuator','mathematics-as-physical-evidence'):
        bad=copy.deepcopy(binding)
        if name=='different-source':bad['right']['source']['id']='RH.source'
        elif name=='hidden-normalization':bad['right']['source']['parameters']['energy']='fitted energy'
        elif name=='resource-mismatch':bad['right']['resources']['policy']='different budget'
        elif name=='context-mismatch':bad['right']['context']['nontrivial_gain_available']=False
        elif name=='lost-archive':bad['right']['retained']={}
        elif name=='extra-actuator':bad['right']['operations'].append('response_cell_write')
        else:bad['premises'][s['physical_premises'][0]]={'status':'independently_justified','evidence':[]}
        try:validate_wg_binding(bad)
        except ValueError:hostiles.append(name)
        else:raise AssertionError('hostile admitted '+name)
    try:step(a,b,Q(2))
    except ValueError:hostiles.append('undeclared amplification')
    else:raise AssertionError('extra gain')
    require(step(a,b,Q(0))==(Q(0),Q(0)) and binding['left']['retained']==binding['left']['source']['archive'],'zero gain archive loss')
    checks.append('zero forward readout does not discard archive')
    result=dict(schema='marici.common-witness-comparison-interface-validation.v1',passed=True,
      resolution_kind='bounded_interface_definition',definition=SCHEMA,
      source_validation='38-check actual WG energy suite freshly run for the initial interface review; normal validation pins and reuses it.',
      binding=binding,checks=checks,corruptions_rejected=hostiles,
      physical_realization_admitted=False,universal_compatibility_proved=False,
      WG_and_RH_sources_identified=False,source_suites_rerun_this_checker=False,
      source_sha256={p:sha(p) for p in source_paths()})
    if args.record:
        require(not (ROOT/OUT).exists(),'refusing implicit interface receipt overwrite')
        (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    else:
        require(load(OUT)==result,'interface evidence drift; review a successor version')
        branch=load(BRANCH);n=next(n for n in branch['conjectures'] if n['id']=='common-witness-comparison-interface')
        require(n['status']=='resolved' and n['verdict']=='constructed' and n['resolution_kind']=='bounded_interface_definition' and branch['comparison_interface']==SCHEMA,'missing scoped registration')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_sha256','binding')},indent=2))


if __name__=='__main__':main()
