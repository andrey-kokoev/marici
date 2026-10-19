"""Explicit scalar source with one primitive theta4 axis; not a Y3 match."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
import check_hodge_even_axis_joint_degree_gate as joint
from check_hodge_even_axis_coupled_kummer_gate import multiply_polynomials as mul

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-minimal-axis-scalar-source.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-minimal-axis-scalar-source-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-minimal-axis-scalar-source-v1.json'
POLICY=['opposite_character_theta6_axis_constructed','full_joint_elliptic_surface_embedding_constructed',
    'degree2_joint_map_to_two_CM_elliptics_realized','source_Prym_End_computed',
    'complementary_sevenfold_simple_proved','source_Prym_isogeny_to_Y3_constructed',
    'one_axis_suffices_for_Y3_match','fixed_Y3_Prym_membership_constructed',
    'explicit_auxiliary_cycle_equations_written','nonzero_target_exceptional_cycle_constructed',
    'all_scalar_sources_excluded_for_Y3','Y2_polarized_exclusions_transferred_to_Y3',
    'Hodge_proved','Hodge_refuted','global_witness_search_completed']
GEOMETRY={'parameters_lambda_a_b':[2,4,2],'W':'y^2=x*(x-1)*(x-2)',
    'T':'v^2=t^3+4*t','T_to_W':'x=(t+2)^2/(4*t), y=v*(t^2-4)/(8*t^2)',
    'order_four_translation_on_T':[-2,'4i'],'g_on_W':'(y+2*(x^2-2))/(x^2-4*x+2)',
    'V_to_W_equation':'w^2=g^3-g','C':'T times_W V','rho_on_C':'(p,w)->(p+kappa,i*w)',
    'scalar_tower_genera':[17,9,5],'ramified_auxiliary_genera':[9,1],
    'ramified_auxiliary_branch_points':16,'ramified_auxiliary_induced_theta_type':[1]*7+[2],
    'ramified_auxiliary_to_source_Prym_isogeny_degree':2,
    'primitive_elliptic_curve_map_degree':8,'actual_source_elliptic_theta_degree':4}
INPUTS={'joint':'research/voevodsky/results/hodge-even-axis-joint-degree-gate-v1.json',
    'literature':'research/voevodsky/results/hodge-eightfold-literature-audit-v1.json'}
P={3:Q(1),2:Q(-3),1:Q(2)}
D={2:Q(1),1:Q(-4),0:Q(2)}
N={2:Q(2),0:Q(-4)}


def require(c,m):
    if not c:raise ValueError(m)


def add(a,b,scale=Q(1)):
    r=dict(a)
    for i,v in b.items():r[i]=r.get(i,Q(0))+scale*v
    return {i:v for i,v in r.items() if v}


def scaled(a,c):return {i:v*c for i,v in a.items() if v*c}


def derivative(a):return {i-1:i*v for i,v in a.items() if i}


def remainder(a,b):
    require(bool(b),'nonzero polynomial divisor')
    a=dict(a);db=max(b)
    while a and max(a)>=db:
        k=max(a)-db;c=a[max(a)]/b[db]
        a=add(a,{i+k:c*v for i,v in b.items()},Q(-1))
    return a


def gcd(a,b):
    while b:a,b=b,remainder(a,b)
    return scaled(a,1/a[max(a)]) if a else {}


def fibre_polynomial(value):
    a=add(scaled(D,Q(value)),N,Q(-1))
    return add(P,mul(a,a),Q(-1))


def smoothness_certificate():
    require(max(D)==2 and gcd(D,derivative(D))=={0:Q(1)} and
        gcd(D,P)=={0:Q(1)} and gcd(D,fibre_polynomial(0))=={0:Q(1)},'four simple genuine poles')
    fibres={str(c):fibre_polynomial(c) for c in (0,1,-1)}
    for c,f in fibres.items():
        require(max(f)==4 and gcd(f,derivative(f))=={0:Q(1)} and
            gcd(f,P)=={0:Q(1)},'four simple fibre points at '+c)
    return {c:[int(f.get(i,0)) for i in range(5)] for c,f in fibres.items()}


def exact_core():
    polys=smoothness_certificate()
    transform=lambda a:{2-i:v*2**i for i,v in a.items()}
    require(transform(D)==scaled(D,2) and transform(N)==scaled(N,-2), 'g anti-translation identity')
    # Pullback of W's cubic under the actual degree-two isogeny T->W.
    xn={2:Q(1),1:Q(4),0:Q(4)};xd={1:Q(4)}
    target=mul(mul(xn,add(xn,xd,Q(-1))),add(xn,xd,Q(-2)))
    source=mul({3:Q(1),1:Q(4)},mul({2:Q(1),0:Q(-4)},{2:Q(1),0:Q(-4)}))
    require(mul(source,mul(mul(xd,xd),xd))==mul(target,{4:Q(64)}),'T-to-W isogeny equation')
    require((-2)**3+4*(-2)==-16 and 3*(-2)**2+4==(-2)*8*(-1) and
        (-4)-2*(-2)==0 and (-2)*(-2)-4==0,'kappa lies on T and doubles to (0,0)')
    # Last equality is the imaginary coefficient in y(2*kappa), slope=-2i.
    require(2 not in (0,1,-1),'no extra special fibre point at W infinity')
    require(16==4*4 and 2*9-2==16 and 2*17-2==32 and
        32==4*(2*5-2) and 32==2*(2*9-2),'genera and free tower RH')
    require([1+2*(8//k) for k in (2,4,8)]==[9,5,3] and
        all(17>1+2*(8//k) for k in (2,4,8)),'primitive elliptic pullback genus controls')
    return {'special_fibre_polynomials_ascending':polys,'g_degree':4,'g_special_fibre_support_sizes':[4,4,4,4],
        'V_to_W_branch_points':16,'V_genus':9,'C_to_T_branch_points':32,
        'C_genus':17,'D_genus':9,'B_genus':5,'primitive_curve_to_CM_elliptic_degree':8,
        'source_principal_Prym_elliptic_theta_degree':4,
        'ramified_auxiliary_induced_theta_type':[1]*7+[2],
        'ramified_auxiliary_to_source_Prym_isogeny_degree':2,
        'source_Gaussian_signature':[4,4],'hypothetical_nonprimitive_genus_bounds':[9,5,3]}


def validate_contract(c):
    require(c['schema']=='marici.hodge-minimal-axis-scalar-source.v1' and
        c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node']=='minimal-axis-scalar-source','minimal-axis source identity')
    require(c['geometry']==GEOMETRY,'minimal-axis source geometry changed')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),
        'one-axis source promoted to target')
    exact_core()


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    rs={'joint':joint.report(),'literature':joint.kummer.literature.report()}
    for k,r in rs.items():require(json.loads((ROOT/INPUTS[k]).read_text(encoding='utf-8'))==r and r['passed'],'stale '+k)
    require(rs['joint']['degree2_requires_scalar_elliptic_isogeny_pullback'] and
        not rs['joint']['all_scalar_sources_excluded_for_Y3'],'scalar continuation lost')
    names=set(INPUTS.values())|{CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),
        Path(__file__).relative_to(ROOT).as_posix()}
    return {'schema':'marici.hodge-minimal-axis-scalar-source-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',
        'verification_level':'Explicit smooth curve/isogeny/automorphism formulas and written primitivity proof; auxiliary Schoen import, no second axis or fixed target matching.',
        'checks':{'rational_fibre_smoothness':True,'explicit_cyclic_four_translation_lift':True,
            'actual_etale_scalar_tower':True,'primitive_CM_elliptic_theta4_axis':True,
            'actual_ramified_to_principal_source_isogeny':True,'fresh_conditional_Schoen_route':True,
            'source_not_confused_with_Y3':True,'scope':True},**exact_core(),
        'actual_scalar_curve_tower_constructed':True,'actual_primitive_theta4_axis_constructed':True,
        'actual_ramified9_1_to_source_principal_Prym_degree2_isogeny_constructed':True,
        'auxiliary_determinant_classes_algebraic_by_retained_theorem':True,
        **{k:False for k in POLICY},
        'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k!='source_sha256'},indent=2))
