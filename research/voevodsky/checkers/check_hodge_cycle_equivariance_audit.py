"""Finite-action coherence audit, not an all-cycle annihilation proof.

The geometric complete-intersection control uses the written Bertini argument;
its projective equations and derived category are not computed here.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/inputs/hodge-cycle-equivariance-audit-v1/contract.json'
NOTE=ROOT/'research/voevodsky/hodge-cycle-equivariance-audit-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-cycle-equivariance-audit-v1.json'
FORBIDDEN=['cycle_object_noninvariance_refutes_class_invariance','finite_group_rational_coherence_vanishing_kills_alpha',
 'formal_stable_module_is_a_constructed_algebraic_cycle_image','fixed_alpha_algebraicity_or_nonalgebraicity_decided',
 'general_higher_coherence_attack_refuted','main_net_or_pins_modified','positive_total_equivariant_cohomology_declared_zero']
SHORTCUTS=['centrality_and_cycle_functoriality_force_tau_equivariance_of_every_cycle_object',
 'positive_degree_additive_C4_group_cohomology_over_Q_can_detect_the_fixed_Hodge_class']
USED_SOURCES=[
 'research/conjecture_net/contracts/hodge-conjecture-net.v1.json',
 'research/conjecture_net/contracts/hodge-refutation-direction.v1.json',
 'research/voevodsky/hodge-cycle-packet-dictionary-v1.md',
 'research/voevodsky/hodge-middle-hodge-kernel-v1.md',
 'research/voevodsky/hodge-weil-projector-v1.md',
 'research/voevodsky/checkers/check_hodge_explicit_sixfold_candidate.py']


def require(condition,message):
    if not condition:raise ValueError(message)


def eye(n):return tuple(tuple(Q(j==k) for k in range(n)) for j in range(n))
def zero(n):return tuple(tuple(Q(0) for _ in range(n)) for _ in range(n))
def add(a,b):return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def scale(a,c):return tuple(tuple(Q(c)*x for x in r) for r in a)
def mul(a,b):return tuple(tuple(sum(a[j][r]*b[r][k] for r in range(len(b))) for k in range(len(b[0]))) for j in range(len(a)))
def diag(values):return tuple(tuple(Q(v) if j==k else Q(0) for k in range(len(values))) for j,v in enumerate(values))
def vec(a,v):return tuple(sum(x*y for x,y in zip(r,v)) for r in a)
def serial(a):return [[[Q(x).numerator,Q(x).denominator] for x in r] for r in a]


def contraction(t,denominator=4):
    n=len(t);i=eye(n);powers=[i]
    for _ in range(4):powers.append(mul(powers[-1],t))
    require(powers[4]==i,'C4 action must have fourth power identity')
    norm=zero(n);weighted=zero(n)
    for k in range(4):norm=add(norm,powers[k]);weighted=add(weighted,scale(powers[k],k))
    d=add(t,scale(i,-1));a=scale(norm,Q(1,4))
    b=scale(weighted,Q(1,denominator));h_even=scale(i,Q(1,denominator))
    require(mul(d,norm)==mul(norm,d)==zero(n),'periodic cochain differential')
    require(mul(a,a)==a and mul(t,a)==a,'Reynolds invariant projection')
    require(add(mul(d,b),mul(h_even,norm))==i and add(mul(norm,h_even),mul(b,d))==i,'periodic contraction in both positive-degree parities')
    require(mul(b,d)==add(i,scale(a,-1)),'degree-zero residual is invariants')
    return {'T':serial(t),'D':serial(d),'N':serial(norm),'averaging':serial(a),
        'h_odd':serial(b),'h_even':serial(h_even),'positive_group_cohomological_degree_over_Q':'zero',
        'all_degrees_basis':'two-periodic resolution and the written operator identities, not extrapolation from samples'}


def point_control(denominator=3):
    require(denominator>0,'positive torsion denominator')
    tau=tuple(tuple(Q(0) for _ in range(12)) for _ in range(12));tau=[list(r) for r in tau]
    for j in range(6):tau[2*j][2*j+1]=-1;tau[2*j+1][2*j]=1
    tau=tuple(map(tuple,tau));p=(Q(1,denominator),)+(Q(0),)*11
    orbit=[];v=p
    for _ in range(4):orbit.append(tuple(x%1 for x in v));v=vec(tau,v)
    require(tuple(x%1 for x in v)==orbit[0],'torsion orbit closes')
    require(len(set(orbit))==4,'Bertini control needs four distinct orbit points')
    return {'native_tau_matrix':serial(tau),'point_lattice_coordinates':[[x.numerator,x.denominator] for x in p],
        'orbit_length':4,'p_distinct_from_tau_p':True,
        'geometry':'Existence by very-ampleness/Bertini in the accompanying proof, not computed projective equations.',
        'cycle_object_tau_equivariance':False,'cycle_class_and_rational_Chow_class_tau_invariance':True}


def linear_models():
    t=diag([1,-1,-1]);f=((Q(125),Q(0),Q(0)),(Q(0),Q(-117),Q(44)),(Q(0),Q(-44),Q(-117)))
    p=diag([0,1,1]);a=diag([1,0,0]);theta=(Q(1),Q(0),Q(0));alpha=(Q(0),Q(1),Q(0))
    require(mul(t,f)==mul(f,t),'native endomorphisms commute')
    require(vec(t,theta)==theta and vec(f,theta)==(Q(125),Q(0),Q(0)) and vec(p,theta)==(0,0,0),'divisor line stable and killed by P')
    require(vec(p,alpha)==alpha and vec(a,alpha)!=(alpha),'averaging changes the selected Weil-direction class')
    require(add(a,p)==eye(3),'averaging complement equals known Hodge projector')
    return {'basis':['E^3','R','I'],'model_A0':'Q E^3','model_A1':'Q E^3 plus W',
        'both_stable_under_tau_F_and_P':True,'P_A0_zero':True,'P_A1_zero':False,
        'geometric_realizability_of_either_model_is_claimed':False,
        'meaning':'The extracted linear constraints alone do not decide the geometric algebraic-cycle image.'}


def torsion_controls():
    require(vec(diag([-2,-2]),(Q(-1,2),Q(0)))==(Q(1),Q(0)),'sign cocycle becomes rational coboundary')
    require(vec(diag([4]),(Q(1,4),))==(Q(1),),'trivial degree-two class becomes rational coboundary')
    return {'abstract_Z_sign_module_rank2_Hodd':'(Z/2)^2','abstract_Z_trivial_module_rank1_Hpositive_even':'Z/4',
        'after_tensor_Q':'zero','identification_with_actual_integral_Hodge_lattice_claimed':False,
        'warning':'Integral torsion tests do not establish rational Hodge nonalgebraicity.'}


def shifted_complex_control():
    # An abstract trivial Q coefficient complex in geometric degree2.
    # Its group-degree-zero invariant survives in total degree2.
    a=contraction(diag([1]))['averaging']
    require(a==serial(eye(1)),'shifted complex keeps its invariant coefficient')
    return {'abstract_coefficient_complex_degree':2,'positive_group_degree_vanishes':True,
        'total_equivariant_degree2_dimension':1,'positive_total_degree_vanishes':False,
        'identification_with_full_fixed_X_equivariant_cohomology_claimed':False}


def check_contract(c):
    require(c['schema']=='marici.hodge-cycle-equivariance-audit.v1' and c['net_node']=='all-algebraic-cycles-annihilation','audit binding')
    require(c['source']=={'complex_dimension':6,'codimension':3,'tau_order':4,'coefficients':'Q','fixed_point_denominator':3},'audit source changed')
    require(c['base_iteration']==52 and c['base_pins']=='v55','audit base changed')
    require(c['vanishing_degree_scope']=='positive_group_cohomological_degree_only_not_total_equivariant_degree','group degree confused with total degree')
    require(c['candidate_shortcuts']==SHORTCUTS and c['forbidden_promotions']==FORBIDDEN,'candidate/scope inventory')


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));check_contract(c)
    pins=ROOT/'research/voevodsky/inputs/hodge-net-source-pins.v55.json';frozen=json.loads(pins.read_text(encoding='utf-8'))['source_sha256']
    for name in USED_SOURCES:require(sha256((ROOT/name).read_bytes()).hexdigest()==frozen[name],'used source drift: '+name)
    net=json.loads((ROOT/USED_SOURCES[0]).read_text(encoding='utf-8'))
    gap=next(n for n in net['conjectures'] if n['id']==c['net_node'])
    require(gap['status']=='open' and gap['verdict']=='open' and gap['evidence']==[],'audit must not close fixed-X class-invariance gap')
    models={'fixed_Hodge_module':diag([1,-1,-1]),'Weil_sign_module':diag([-1,-1]),
        'rotation_module':((Q(0),Q(-1)),(Q(1),Q(0))),'trivial_module':diag([1])}
    certificates={name:contraction(t) for name,t in models.items()}
    paths=USED_SOURCES+[CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),
        Path(__file__).relative_to(ROOT).as_posix(),'research/voevodsky/checkers/test_hodge_cycle_equivariance_audit.py',pins.relative_to(ROOT).as_posix()]
    return {'schema':'marici.hodge-cycle-equivariance-audit-result.v1','passed':True,
        'disposition':'two_scoped_shortcuts_rejected_fixed_X_all_cycle_invariance_still_open',
        'classification':'scoped_necessity_shortcuts_rejected_not_Hodge_refuted',
        'residuals':['fixed_X_all_cycle_class_invariance_open','no_algebraic_specific_necessity_theorem_supplied'],
        'next_falsifier':'Any attempt to infer class noninvariance from object noninvariance, or to claim positive rational C4 cohomology despite the contraction.',
        'coherence_obligation':c['coherence_obligation'],'C4_contraction_certificates':certificates,
        'fixed_source_cycle_object_control':point_control(),'class_level_linear_constraints':linear_models(),
        'integral_torsion_controls':torsion_controls(),'shifted_complex_degree_control':shifted_complex_control(),'main_net_modified':False,'base_iteration':52,'base_pins':'v55',
        'first_missing_proof':'Every codimension-three algebraic cycle class on the fixed X is tau-invariant; additional source-specific algebraic necessity is required.',
        'finite_action_additive_rational_group_cohomology_detector_rejected':True,
        'cycle_object_equivariance_is_necessary_for_algebraicity':False,
        **dict.fromkeys(c['forbidden_promotions'],False),'Hodge_proved':False,'Hodge_refuted':False,
        'verification_level':'Exact rational operator identities and torsion-point arithmetic; geometric counterexample uses the written imported very-ampleness/Bertini argument. Not proof-assistant certification.',
        'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(set(paths))}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k not in ('source_sha256','C4_contraction_certificates','fixed_source_cycle_object_control')},indent=2))
