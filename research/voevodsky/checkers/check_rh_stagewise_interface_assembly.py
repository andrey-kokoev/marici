# /// script
# dependencies = ["sympy"]
# ///
"""Review scoped RH child overlaps; --replay builds extra exact diagrams.
This does not discharge the general mathematical interface or prove RH.
"""
import argparse
import copy
import json
import subprocess
import sys
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
NET='research/conjecture_net/contracts/rh-realization-work-net.v1.json'
MATH='research/conjecture_net/contracts/mathematical-realization-conjecture-net.v1.json'
DICT='research/conjecture_net/contracts/rh-stage-dictionary.v1.json'
NOTE='research/voevodsky/rh-stagewise-interface-assembly-v1.md'
OUT='research/voevodsky/results/rh-stagewise-interface-assembly-v1.json'
CHILDREN={
 'rh-stage-dictionary':('stage-dictionary','check_rh_stage_dictionary.py','rh-stage-dictionary-v1.json'),
 'rh-operation-composition-squares':('operation-composition-audit','check_rh_operation_composition_audit.py','rh-operation-composition-audit-v1.json'),
 'rh-identity-continuation-transport':('identity-continuation-audit','check_rh_identity_continuation_audit.py','rh-identity-continuation-audit-v1.json'),
 'rh-analytic-domain-completion-transport':('analytic-completion-audit','check_rh_analytic_completion_audit.py','rh-analytic-completion-audit-v1.json')}
CONVENTIONS={
 'additive_Fourier':'exp(-2pi ixy), self-dual measure',
 'history_angular_generator':'A=sqrt(3)*[[0,2/3],[-2,0]]',
 'half_density':'(U f)_epsilon(u)=exp(u/2)f(epsilon exp(u))',
 'log_Fourier':'V=(2pi)^(-1/2) M_log; scalar normalization cancels in gamma square',
 'radial_test_topology':'E_r=U S(R), transported Schwartz Frechet',
 'spectral_test_topology':'E_s=V E_r, transported Frechet',
 'dual_pairing':'continuous anti-duals; <A^times T,A phi>=<T,phi>',
 'generic_shift':'0<a<1, a!=1/2; seed/shift supplied',
 'specialization':'Rank-one unshifted comb readout; hidden records retained',
 'native_analytic_continuation':'J M J^-1 on cyclic coefficients, transported to finite generic comb image; not Fourier or an operator on arbitrary ambient states'}
BOUNDARIES={
 'general_mathematical_interface_discharged':False,
 'universal_dependent_transport_supplied':False,
 'source_channel_carrier_identified':False,
 'one_dimensional_channel_selected':False,
 'native_tick_identified_with_Fourier':False,
 'ordinary_log_tempered_comb_extension':False,
 'positive_Weil_pullback_constructed':False,
 'physical_realization_admitted':False,'RH_proved':False}


def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()
def require(ok,msg):
    if not ok:raise ValueError(msg)


def review_inputs():
    c=load(NET);by={n['id']:n for n in c['conjectures']};art={a['id']:a for a in c['artifacts']}
    p=by['rh-stagewise-interface']
    require(set(p['depends_on'])==set(CHILDREN) and p['required_verdicts']==dict.fromkeys(CHILDREN,'constructed'),'assembly gate changed')
    for node,(aid,script,receipt) in CHILDREN.items():
        require(by[node]['status']=='resolved' and by[node]['verdict']=='constructed' and by[node]['evidence']==[aid],'unconstructed child '+node)
        require(art[aid]['checker']=='research/voevodsky/checkers/'+script and art[aid]['receipt']=='research/voevodsky/results/'+receipt,'child evidence mismatch')
        r=load(art[aid]['receipt']);require(r['passed'] is True,'failed child receipt')
    d=load(DICT);op=load('research/voevodsky/results/rh-operation-composition-audit-v1.json');identity=load('research/voevodsky/results/rh-identity-continuation-audit-v1.json');analytic=load('research/voevodsky/results/rh-analytic-completion-audit-v1.json')
    owner_packets={'rh-operation-composition-squares':op,'rh-identity-continuation-transport':identity,'rh-analytic-domain-completion-transport':analytic}
    cells=[]
    for cell in d['cells']:
        if cell['required_for_interface']:
            packet=owner_packets[cell['owner']]
            require(cell['id'] in packet['cells'],'unaccounted required cell')
            entry=packet['cells'][cell['id']]
            state=entry.get('disposition',entry.get('status'))
            cells.append(dict(id=cell['id'],owner=cell['owner'],witness_state=state,
                              claim_scope=entry.get('equivalence',entry.get('restriction',entry.get('boundary',''))),
                              positive_identity_asserted=state!='rejected_identification_retained',
                              rejected_original_identification_promoted=False))
    require(len(cells)==14,'required cell coverage changed')
    require(op['cells']['native-tick-no-go']['disposition']=='rejected_identification_retained' and op['cells']['generator-quarter-turn-no-go']['disposition']=='rejected_identification_retained','lost exclusion')
    rig=analytic['rigging']
    require(not rig['ordinary_log_tempered_extension'] and rig['zero_endpoint_retained'] and not rig['raw_combs_are_Hilbert_states'],'incompatible completion')
    w=identity['witnesses']
    require(w['endpoint_readout']==[['2','2','0','0']] and w['predictive_update']==[['0','1'],['1','1']],'identity convention changed')
    require(not w['complete_state_identity_inferred_from_task_readout'],'task readout promoted')
    general=next(n for n in load(MATH)['conjectures'] if n['id']=='stagewise-mathematical-interface')
    branch_snapshot={k:general[k] for k in ('statement','acceptance','falsifier')}
    return cells,branch_snapshot


def validate_review(c,b):
    require(c==CONVENTIONS and b==BOUNDARIES,'normalization/source/domain/claim drift')


def exact_overlaps():
    import sympy as S
    def rows(x):return [[str(v) for v in x.row(i)] for i in range(x.rows)]
    ep=load('research/voevodsky/results/full-endpoint-fourier-bridge-v1.json');J=S.Matrix(ep['full_analytic_attachment']);M=S.Matrix(ep['endpoint_matrix']);Q=S.Matrix(ep['endpoint_basis'])
    F=S.zeros(4)
    for j in range(4):F[(j+1)%4,j]=1
    D=F-F.T;A0=S.Matrix([[0,S.Rational(2,3)],[-2,0]])
    Aep0=Q*S.diag(A0,S.zeros(2))*Q.inv();Aep=S.sqrt(3)*Aep0
    require(S.simplify(D*J-J*Aep)==S.zeros(4),'angular overlap')
    require(S.simplify(D*J-J*Aep0)!=S.zeros(4),'lost sqrt(3) normalization control')
    native=S.simplify(J*M*J.inv())
    require(S.simplify(native*J-J*M)==S.zeros(4),'native finite analytic route')
    require(S.simplify(native-F)!=S.zeros(4),'native replaced by Fourier')
    require(S.simplify(native*F-F*native)!=S.zeros(4),'native/Fourier noncommutativity erased')
    ell=S.simplify(S.ones(1,4)*J);Z=ell.col_join(ell*M);T=S.Matrix([[0,1],[1,1]])
    require(Z*M==T*Z and Z*Aep==S.zeros(2,4),'predictive/operation overlap')
    analytic_reader=S.simplify(Z*J.inv())
    require(S.simplify(analytic_reader*native-T*analytic_reader)==S.zeros(2,4),'predictive task on analytic image')
    require(S.simplify(S.ones(1,4)*native-S.ones(1,4))!=S.zeros(1,4),'unsafe scalar specialization concealed')
    carrier=load('research/voevodsky/results/carrier-fourier-orbit-bridge-v1.json');K=S.Matrix(carrier['projection_then_attachment'])
    prior=load('research/strominger/results/source-arrow-hamiltonian-descent.json')
    sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
    from source_arrow_hamiltonian import construct
    source,C,edges=construct(tuple('ABCD'),prior['vertex_permutation'],{'A':0,'C':1,'D':2,'B':3},S.Rational(1,2))
    require(K*C==F*K and K*source.D==D*K,'carrier/analytic overlap')
    require(S.ones(1,4)*K*C==S.ones(1,4)*K,'safe carrier specialization')
    boundary=S.Matrix([[1,0,0],[0,0,1],[0,1,0]])
    require(boundary*S.Matrix([1,-1,0])==S.Matrix([1,0,-1]),'zero-atom boundary erased')
    return dict(native_cyclic_continuation=rows(native),native_operator_scope='Finite generic analytic image only, via existing injective B_a. No independently admitted ambient operator.',
      predictive_reader_in_cyclic_coordinates=rows(analytic_reader),
      checks=['sqrt(3) angular normalization','native analytic continuation square',
              'native/Fourier inequality and noncommutativity','predictive quotient/analytic-image overlap',
              'unsafe native versus safe carrier scalar specialization','carrier Fourier/generator squares','zero-atom exchange'])


def source_paths():
    d=load(DICT);paths=[DICT,NOTE,Path(__file__).relative_to(ROOT).as_posix(),
      'research/voevodsky/results/carrier-fourier-orbit-bridge-v1.json',
      'research/voevodsky/results/full-endpoint-fourier-bridge-v1.json',
      'research/strominger/results/source-arrow-hamiltonian-descent.json',
      'research/strominger/checkers/source_arrow_hamiltonian.py']
    for aid,script,receipt in CHILDREN.values():
        paths+=['research/voevodsky/checkers/'+script,'research/voevodsky/results/'+receipt]
    paths+=['research/voevodsky/'+x for x in ('rh-stage-dictionary-v1.md','rh-operation-composition-audit-v1.md','rh-identity-continuation-audit-v1.md','rh-analytic-completion-audit-v1.md')]
    return sorted(set(paths))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--replay',action='store_true');args=parser.parse_args()
    cells,branch=review_inputs();validate_review(CONVENTIONS,BOUNDARIES);hostiles=[]
    for mode in ('angular-factor-loss','ambient-native-operator','log-tempered-substitution','branch-auto-discharge','Weil-promotion'):
        c=copy.deepcopy(CONVENTIONS);b=copy.deepcopy(BOUNDARIES)
        if mode=='angular-factor-loss':c['history_angular_generator']='A=A0'
        elif mode=='ambient-native-operator':c['native_analytic_continuation']='native M is ambient Fourier'
        elif mode=='log-tempered-substitution':b['ordinary_log_tempered_comb_extension']=True
        elif mode=='branch-auto-discharge':b['general_mathematical_interface_discharged']=True
        else:b['positive_Weil_pullback_constructed']=True
        try:validate_review(c,b)
        except ValueError:hostiles.append(mode)
        else:raise AssertionError('hostile accepted '+mode)
    runs=[]
    for node,(aid,script,receipt) in CHILDREN.items():
        r=subprocess.run([sys.executable,str(ROOT/'research/voevodsky/checkers'/script)],cwd=ROOT,capture_output=True,text=True,timeout=120)
        require(r.returncode==0,'child validation failed '+node+'\n'+r.stderr+'\n'+r.stdout[-2000:])
        runs.append(dict(node=node,checker=script,returncode=0))
    if args.replay:
        overlaps=exact_overlaps()
        result=dict(schema='marici.rh-stagewise-interface-assembly.v1',passed=True,
          child_witnesses={n:aid for n,(aid,script,receipt) in CHILDREN.items()},
          required_cells=cells,boundary_cells=['channel-source-binding','one-dimensional-binding'],
          conventions=CONVENTIONS,boundaries=BOUNDARIES,exact_overlaps=overlaps,
          branch_interface_acceptance_snapshot=branch,
          child_validations=runs,scientific_source_suites_rerun=False,
          fresh_overlap_checks=True,formal_compiler_closure=False,
          corruptions_rejected=hostiles,source_sha256={p:sha(p) for p in source_paths()})
        (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    else:
        result=load(OUT)
        require(result['passed'] and result['required_cells']==cells and result['branch_interface_acceptance_snapshot']==branch,'assembly input or branch-review drift')
        validate_review(result['conventions'],result['boundaries'])
        require(result['source_sha256']=={p:sha(p) for p in source_paths()},'assembly source drift')
    print(json.dumps(dict(passed=True,required_cells_covered=len(cells),children_validated=len(runs),
       fresh_overlap_checks_this_run=args.replay,general_mathematical_interface_discharged=False,
       corruptions_rejected=hostiles),indent=2))


if __name__=='__main__':main()
