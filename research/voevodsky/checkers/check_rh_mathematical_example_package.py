"""Export/check a bounded RH mathematical example; not branch proof import.
--record creates the immutable v1 package once. Normal runs validate wiring.
"""
import argparse
import copy
import json
import subprocess
import sys
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
HOME='research/conjecture_net/contracts/'
NET=HOME+'rh-realization-work-net.v1.json'
MATH=HOME+'mathematical-realization-conjecture-net.v1.json'
COMP=HOME+'same-source-compatibility-conjecture-net.v1.json'
DICT=HOME+'rh-stage-dictionary.v1.json'
PACKAGE=HOME+'rh-bounded-mathematical-example.v1.json'
NOTE='research/voevodsky/rh-bounded-mathematical-example-v1.md'
OUT='research/voevodsky/results/rh-bounded-mathematical-example-v1.json'
NODES=['rh-stage-dictionary','rh-operation-composition-squares','rh-identity-continuation-transport','rh-analytic-domain-completion-transport','rh-stagewise-interface']
BOUNDARIES={'RH_assumed_true':False,'RH_proved':False,'general_math_interface_discharged':False,
 'math_branch_example_automatically_resolved':False,'same_source_compatibility_discharged':False,
 'physical_realization_supplied':False,'Weil_form_pullback_supplied':False,'universal_coverage_supplied':False}


def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()
def require(ok,msg):
    if not ok:raise ValueError(msg)


def initial():
    c=load(NET);d=load(DICT);by={n['id']:n for n in c['conjectures']};art={a['id']:a for a in c['artifacts']};evidence={}
    for n in NODES:
        require(by[n]['verdict']=='constructed','unreviewed component '+n)
        aid=by[n]['evidence'][0];evidence[n]=dict(artifact_id=aid,**art[aid])
    reductions=[f'reduce-{a}-{b}' for a,b in zip((12,11,10,9,8,6),(11,10,9,8,6,4))]
    coeff=['coeff-'+str(n) for n in (12,11,10,9,8,6,4)]
    routes=[
      dict(id='carrier-generic',kind='linear',stages=coeff+['cyclic','comb','radial','mellin'],maps=reductions+['carrier-chart','comb-attachment','oriented-radial','spectral-mellin'],scope='Generic chosen shift; full source archive retained.'),
      dict(id='history-generic',kind='linear',stages=['history','endpoint','cyclic','comb','radial','mellin'],maps=['history-endpoint','endpoint-chart','comb-attachment','oriented-radial','spectral-mellin'],scope='Four actual stages n=10,16,26,42; continuous bridge plus distinct native continuation on finite generic image.'),
      dict(id='lattice-Fourier-square',kind='square_then_linear',stages=['lattice','torus','real-distribution','radial','mellin'],maps=['lattice-fourier','atom-lift','periodic-lift','real-radial','spectral-mellin'],scope='Independent additive lattice source, fixed mesh continuity; multichannel statements do not select a one-dimensional zeta source.'),
      dict(id='Riemann-completion',kind='linear',stages=coeff+['cyclic','riemann-boundary','theta','completed-zeta'],maps=reductions+['carrier-chart','unshifted-specialization','theta-pairing','theta-mellin-completion'],scope='Unit unshifted seed for ordinary Lambda/xi; arbitrary scalar coefficients scale the entire endpoint packet and readout.')]
    identity=load('research/voevodsky/results/rh-identity-continuation-audit-v1.json')
    analytic=load('research/voevodsky/results/rh-analytic-completion-audit-v1.json')
    assembly=load('research/voevodsky/results/rh-stagewise-interface-assembly-v1.json')
    return dict(schema='marici.rh-bounded-mathematical-example.v1',id='marici.rh-bounded-mathematical-example.v1',
      origin_net=NET,origin_node='rh-math-assembly',shared_example_id=c['shared_example_id'],baseline=c['baseline'],
      scope='Bounded mathematical realization under declared choices, not RH truth or a universal common-source theorem.',
      dictionary=DICT,dictionary_sha256=sha(DICT),
      stage_ids=[r['id'] for r in d['stages']],map_ids=[r['id'] for r in d['maps']],routes=routes,
      required_cells=assembly['required_cells'],excluded_boundary_cells=assembly['boundary_cells'],
      evidence=evidence,identity_contexts=identity['cells'],completion_contract=analytic['rigging'],
      operation_conventions=assembly['conventions'],
      normalization_contract=dict(unshifted_coefficient='c=sum cyclic coefficients; c=r12 x or ell O_n x on its respective route.',
        ordinary_zeta_seed_condition='c=1 with unit self-dual comb and declared Gaussian/measure.',
        arbitrary_state_output='c Lambda(s), c xi(s); polar packet and xi endpoint constant also scaled by c.',
        automatic_per_state_normalization=False,zero_coefficient_division_allowed=False,
        native_readout_prediction='Use Z=[ell;ell M], not scalar identity or free renormalization after extension.'),
      consumer_bindings=[dict(contract=MATH,node='rh-mathematical-realization-example',role='mathematical_realization',relation='scoped_contribution_pending_general_interface_review',proof_bearing=False,discharges_parent=False),
                         dict(contract=COMP,node='rh-same-source-compatibility-example',role='same_source_compatibility',relation='reuse_mathematical_witness_only',proof_bearing=False,discharges_parent=False)],
      remaining_gates=['math:stagewise-mathematical-interface','math:rh-mathematical-realization-example',
        'rh:channel-carrier-source-map','rh:one-dimensional-source-selection','rh:successor-form-candidate',
        'rh:weil-form-comparison','rh:same-source-continuation-comparison','rh:rh-cross-realization-assembly'],
      boundaries=BOUNDARIES)


def validate_package(p):
    require(p==initial(),'package differs from scoped source/evidence/interface inventory')
    d=load(DICT);maps={x['id']:x for x in d['maps']};covered=set()
    for r in p['routes']:
        require(set(r['stages']) <= set(p['stage_ids']) and set(r['maps']) <= set(maps),'untyped route reference')
        for mid in r['maps']:
            require(maps[mid]['source'] in r['stages'] and maps[mid]['target'] in r['stages'],'route map crosses wrong stage')
        if r['kind']=='linear':
            require(len(r['maps'])==len(r['stages'])-1,'linear route size')
            for mid,s,t in zip(r['maps'],r['stages'],r['stages'][1:]):
                require(maps[mid]['source']==s and maps[mid]['target']==t,'noncomposable route')
        covered.update(r['maps'])
    require(covered==set(p['map_ids']),'map not exported')
    require(not any(p['boundaries'].values()),'claim promotion')
    require(not p['normalization_contract']['automatic_per_state_normalization'] and not p['normalization_contract']['zero_coefficient_division_allowed'],'answer-fitted normalization')
    return len(covered)


def validate_wiring(p):
    c=load(NET);by={n['id']:n for n in c['conjectures']}
    require(by['rh-math-assembly']['status']=='resolved' and by['rh-math-assembly']['verdict']=='constructed','package not registered as scoped result')
    require(by['rh-math-assembly']['required_verdicts']=={'rh-stagewise-interface':'constructed'},'math assembly gate changed')
    for b in p['consumer_bindings']:
        branch=load(b['contract']);w=next(w for w in branch['work_nets'] if w['node']==b['node'])
        field='assembled_package' if b['role']=='mathematical_realization' else 'reuses_mathematical_package'
        require(w[field]==PACKAGE and w['shared_example_id']==p['shared_example_id'],'consumer package/identity mismatch')
        a=next(a for a in branch['example_attachments'] if a['id']==p['shared_example_id'])
        require(a['contract']==p['baseline'] and a['proof_bearing'] is False and a['discharges_parent'] is False,'source or role promotion')
        projection=next(x for x in c['branch_projections'] if x['role']==b['role'])
        require(projection[field]==PACKAGE,'missing reciprocal package projection')
    require(load(MATH)['imports']==load(COMP)['imports']==[],'proof import introduced')


def source_paths(p):
    paths=[PACKAGE,DICT,NOTE,Path(__file__).relative_to(ROOT).as_posix()]
    for e in p['evidence'].values():paths += [e[k] for k in ('note','checker','receipt')]
    return sorted(set(paths))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--record',action='store_true');args=parser.parse_args()
    if args.record:
        require(not (ROOT/PACKAGE).exists(),'refusing implicit package overwrite')
        (ROOT/PACKAGE).write_text(json.dumps(initial(),indent=2)+'\n',encoding='utf-8')
    p=load(PACKAGE);count=validate_package(p)
    if not args.record:validate_wiring(p)
    r=subprocess.run([sys.executable,str(ROOT/'research/voevodsky/checkers/check_rh_stagewise_interface_assembly.py')],cwd=ROOT,capture_output=True,text=True,timeout=180)
    require(r.returncode==0,'upstream interface review failed\n'+r.stderr+'\n'+r.stdout[-2000:])
    hostiles=[]
    for mode in ('missing-route-map','wrong-type','RH-import','same-source-promotion','automatic-normalization','wrong-shared-source'):
        bad=copy.deepcopy(p)
        if mode=='missing-route-map':bad['routes'][0]['maps'].pop()
        elif mode=='wrong-type':bad['routes'][0]['stages'][0]='endpoint'
        elif mode=='RH-import':bad['boundaries']['RH_assumed_true']=True
        elif mode=='same-source-promotion':bad['consumer_bindings'][1]['discharges_parent']=True
        elif mode=='automatic-normalization':bad['normalization_contract']['automatic_per_state_normalization']=True
        else:bad['baseline']='another-RH-source'
        try:validate_package(bad)
        except ValueError:hostiles.append(mode)
        else:raise AssertionError('hostile accepted '+mode)
    # Scalar readout normalization is linear, including the endpoint term.
    identity=load('research/voevodsky/results/rh-identity-continuation-audit-v1.json')
    source_row=[Fraction(v) for v in identity['witnesses']['carrier_riemann_row'][0]]
    require(len(source_row)==12 and source_row[0]==1,'unit AD seed binding changed')
    scale_controls=[]
    for c in (Fraction(0),Fraction(1),Fraction(2),Fraction(-1),Fraction(2,7)):
        require(c*Fraction(1,2)==c/2,'scaled xi endpoint')
        scale_controls.append(dict(coefficient=str(c),xi_endpoint_constant=str(c/2),ordinary_unit_seed=c==1))
    result=dict(schema='marici.rh-bounded-mathematical-example-validation.v1',passed=True,
      routes=len(p['routes']),stage_families=len(p['stage_ids']),maps_exported=count,required_cells=len(p['required_cells']),
      general_math_interface_discharged=False,same_source_compatibility_discharged=False,
      normalization_controls=scale_controls,corruptions_rejected=hostiles,
      wiring_validated=not args.record,source_suites_rerun=False,
      source_sha256={path:sha(path) for path in source_paths(p)})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_sha256','normalization_controls')},indent=2))


if __name__=='__main__':main()
