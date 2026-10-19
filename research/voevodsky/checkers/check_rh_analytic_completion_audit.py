# /// script
# dependencies = ["sympy"]
# ///
"""RH completed-domain ledger; proofs are in the note, not finite checks.
--replay runs exact controls and source suites. Default checks retained provenance.
"""
import argparse
import copy
import json
import subprocess
import sys
from pathlib import Path
from hashlib import sha256
ROOT=Path(__file__).resolve().parents[3]
DICT='research/conjecture_net/contracts/rh-stage-dictionary.v1.json'
NOTE='research/voevodsky/rh-analytic-completion-audit-v1.md'
OUT='research/voevodsky/results/rh-analytic-completion-audit-v1.json'
REPLAY={'lattice':('check_additive_lattice_fourier_bridge.py','additive-lattice-fourier-bridge-v1.json'),
        'riemann':('check_riemann_comb_specialization.py','riemann-comb-specialization-v1.json')}
CELLS={
 'generic-domain':dict(status='constructed_at_declared_scope',source='R^4 at generic a',target='V_a subset S\'(R)_beta',topology='Finite-dimensional coefficient topology and strong tempered-distribution topology.',witness='Lattice sampling bound, independent local atom probes and finite-dimensional closed-subspace theorem.',restriction='No uniform coordinate inverse at a=0 or a=1/2; no comb L2 norm.'),
 'radial-endpoint-domain':dict(status='constructed_at_declared_scope',source='S(R) and its strong anti-dual',target='E_r=U S(R), E_r^times',topology='Transported Schwartz Frechet topology, not ordinary log-Schwartz inherited topology.',witness='U is unitary on L2 and a topological isomorphism onto E_r; inverse test has matching smooth jets at zero; Fourier conjugation extends by anti-duality.',restriction='Endpoint values are source-induced, not independently completed coordinates.'),
 'mellin-domain':dict(status='constructed_at_declared_scope',source='E_r and E_r^times',target='E_s=V E_r, E_s^times; V=(2pi)^(-1/2) M_log',topology='Induced complete Frechet test space and strong anti-dual, continuously/densely embedded test space in L2.',witness='Dense-core Abel gamma identity, uniformly bounded regulated multipliers, Plancherel extension, and H=V U F U^-1 V^-1 on E_s.',restriction='Spectral anti-duals are not claimed to be ordinary S\'(t), Hilbert vectors or pointwise Mellin functions.'),
 'lattice-continuity':dict(status='constructed_at_declared_scope',source='l2(Z), L2(T), fixed mesh h>0',target='S\'(R)_beta and transported induced strong anti-duals',topology='Strong dual convergence, uniformly on bounded Schwartz test sets.',witness='Cauchy-Schwarz sampling and periodized-test bounds; density extends Fourier square; dyadic isometry; Gaussian error <=h(2||phi||_infinity+t^-1/2||phi_prime||_infinity).',restriction='No h-uniform unweighted sampling constant or l2 convolution-algebra claim.'),
 'theta-completion':dict(status='constructed_at_declared_scope',source='Theta Gaussian pairing at t>0 and Re(s)>1 initially',target='Meromorphic Lambda and entire xi',topology='Uniform convergence of tail integral and derivatives on compact s-sets.',witness='Poisson under supplied self-dual convention, tail <=2e^-pi t/(1-e^-pi), parameter-integral theorem, exact endpoint pole cancellation.',restriction='No critical-line zero theorem or arithmetic form positivity.')}
RIGGING=dict(test_pairing='Continuous anti-dual: <T,phi>=T(conjugate phi); <A^times T,A phi>=<T,phi>.',
 radial='E_r=U S(R), p_Nk^r(g)=p_Nk(U^-1 g), smooth inverse at zero.',
 spectral='E_s=V E_r with transported topology, V normalized log Fourier.',
 ordinary_log_tempered_extension=False,raw_combs_are_Hilbert_states=False,
 all_l2_packets_have_pointwise_continued_Mellin_functions=False,
 zero_endpoint_retained=True,independent_endpoint_completion=False)


def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()
def require(ok,msg):
    if not ok:raise ValueError(msg)


def validate_ledger(cells,rigging):
    d=load(DICT);required={c['id'] for c in d['cells'] if c['owner']=='rh-analytic-domain-completion-transport' and c['required_for_interface']}
    require(set(cells)==required and cells==CELLS,'missing/changed completed-domain cell')
    require(rigging==RIGGING,'unlicensed ambient-space, endpoint or pairing promotion')


def exact_controls():
    import sympy as S
    from check_rh_operation_composition_audit import symbolic_checks
    controls=symbolic_checks()
    x,t=S.symbols('x t',positive=True);u=S.symbols('u',real=True);g=S.Function('g')
    inv=x**(-S.Rational(1,2))*g(S.log(x))
    expected=x**(-S.Rational(3,2))*(S.Subs(S.diff(g(u),u),u,S.log(x))-g(S.log(x))/2)
    require(S.simplify(S.diff(inv,x)-expected)==0,'inverse half-density derivative')
    expected2=x**(-S.Rational(5,2))*(S.Subs(S.diff(g(u),u,2),u,S.log(x))-2*S.Subs(S.diff(g(u),u),u,S.log(x))+3*g(S.log(x))/4)
    require(S.simplify(S.diff(inv,x,2)-expected2)==0,'inverse half-density second derivative')
    gaussian=S.exp(-S.pi*t*x*x)
    require(S.simplify(2*S.integrate(gaussian,(x,0,S.oo))-t**(-S.Rational(1,2)))==0,'Gaussian L1 mass')
    require(S.simplify(2*S.integrate(2*S.pi*t*x*gaussian,(x,0,S.oo))-2)==0,'Gaussian derivative L1 variation')
    radial_gaussian=S.exp(u/2)*S.exp(-S.pi*t*S.exp(2*u))
    require(S.limit(S.exp(-u/2)*radial_gaussian,u,-S.oo)==1,'zero-atom endpoint evaluation')
    odd_positive=S.exp(3*u/2)*S.exp(-S.exp(2*u))
    require(S.limit(S.exp(-3*u/2)*odd_positive,u,-S.oo)==1,'positive endpoint derivative jet')
    require(S.limit(-S.exp(-3*u/2)*odd_positive,u,-S.oo)==-1,'negative endpoint derivative jet')
    # Finite-dimensional control for the anti-dual convention, not a Fourier theorem.
    D=S.Matrix(4,4,lambda i,j:(-S.I)**(i*j)/2)
    require(D.H*D==S.eye(4) and D.inv()==D.H and D!=D.inv(),'adjoint Fourier convention')
    a=S.Matrix([1,S.I,2,0]);b=S.Matrix([0,1,S.I,3])
    require(S.simplify((D*a).H*(D*b)-a.H*b)==S.zeros(1,1),'transported anti-dual pairing')
    s=S.symbols('s');polar=1/(s*(s-1))
    require(S.simplify(s*(s-1)*polar/2)==S.Rational(1,2),'xi endpoint constant')
    require(S.residue(polar,s,0)==-1 and S.residue(polar,s,1)==1,'polar endpoint residues')
    # m+1 integers in [m,2m], each carrying at least (2m)^-1/2.
    m=S.symbols('m',positive=True)
    require(S.simplify((m+1)/S.sqrt(2*m)-S.sqrt(m/2))==1/S.sqrt(2*m),'non-tempered comb lower bound')
    controls+=['inverse half-density derivatives','zero value and signed derivative jets',
               'Gaussian L1 error constants','anti-dual adjoint convention control',
               'endpoint poles and constant','comb translated-bump lower bound']
    return controls


def source_paths():
    d=load(DICT)
    paths=[DICT,NOTE,Path(__file__).relative_to(ROOT).as_posix(),
      'research/voevodsky/checkers/check_rh_operation_composition_audit.py',
      'research/voevodsky/rh-operation-composition-audit-v1.md',
      'research/voevodsky/results/rh-operation-composition-audit-v1.json']
    paths+=list(d['evidence_sources'].values())
    for script,receipt in REPLAY.values():paths+=['research/voevodsky/checkers/'+script,'research/voevodsky/results/'+receipt]
    return sorted(set(paths))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--replay',action='store_true');args=parser.parse_args()
    validate_ledger(CELLS,RIGGING);hostiles=[]
    for mode in ('missing-cell','ordinary-log-tempered-substitution','comb-Hilbert-substitution','endpoint-loss','pointwise-Mellin-for-all-packets','independent-endpoint-completion'):
        cells=copy.deepcopy(CELLS);rig=copy.deepcopy(RIGGING)
        if mode=='missing-cell':cells.pop('mellin-domain')
        elif mode=='ordinary-log-tempered-substitution':rig['ordinary_log_tempered_extension']=True
        elif mode=='comb-Hilbert-substitution':rig['raw_combs_are_Hilbert_states']=True
        elif mode=='endpoint-loss':rig['zero_endpoint_retained']=False
        elif mode=='pointwise-Mellin-for-all-packets':rig['all_l2_packets_have_pointwise_continued_Mellin_functions']=True
        else:rig['independent_endpoint_completion']=True
        try:validate_ledger(cells,rig)
        except ValueError:hostiles.append(mode)
        else:raise AssertionError('hostile accepted '+mode)
    if args.replay:
        executions=[]
        for key,(script,receipt) in REPLAY.items():
            p='research/voevodsky/checkers/'+script;rp='research/voevodsky/results/'+receipt;before=sha(rp)
            r=subprocess.run([sys.executable,str(ROOT/p)],cwd=ROOT,capture_output=True,text=True,timeout=240)
            require(r.returncode==0,'source replay failed '+key+'\n'+r.stderr+'\n'+r.stdout[-3000:])
            require(sha(rp)==before,'pinned source receipt changed '+key)
            executions.append(dict(id=key,checker=p,returncode=0,receipt_unchanged=True))
        controls=exact_controls()
        result=dict(schema='marici.rh-analytic-completion-audit.v1',passed=True,required_cells_covered=5,cells=CELLS,rigging=RIGGING,
          ordinary_log_tempered_candidate='rejected by translated-bump exponential growth; induced rigging used instead',
          source_suites_freshly_replayed=executions,exact_controls=controls,corruptions_rejected=hostiles,
          proof_status='Analytic arguments in note, using Plancherel, gamma reflection, Schwartz Fourier continuity, Poisson and standard parameter-integral theorem; not a formal compiler certificate.',
          stagewise_assembly_closed=False,RH_proved=False,physical_realization_admitted=False,
          source_sha256={p:sha(p) for p in source_paths()})
        (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    else:
        result=load(OUT);require(result['passed'] and result['cells']==CELLS and result['rigging']==RIGGING,'ledger receipt drift')
        require(result['source_sha256']=={p:sha(p) for p in source_paths()},'analytic source drift')
        require(not result['stagewise_assembly_closed'] and not result['RH_proved'] and not result['physical_realization_admitted'],'scope promotion')
    print(json.dumps(dict(passed=True,required_cells_covered=5,fresh_replay_this_run=args.replay,
      ordinary_log_tempered_extension=False,zero_endpoint_retained=True,
      exact_control_count=len(result['exact_controls']),corruptions_rejected=hostiles),indent=2))


if __name__=='__main__':main()
