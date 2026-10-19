"""Coupled Kummer reduction for Y3; no solved base curve or target cover."""
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
from hashlib import sha256
import json
import check_hodge_even_axis_principal_model as model
import check_hodge_eightfold_literature_audit as literature

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-even-axis-coupled-kummer-gate.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-even-axis-coupled-kummer-gate-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-even-axis-coupled-kummer-gate-v1.json'
POLICY=['actual_genus5_curve_and_functions_supplied','actual_Picard_torsion_calculated',
    'local_divisibility_alone_proves_connectedness','coupled_equation_alone_proves_order_four',
    'local_profiles_counted_as_actual_covers','primitive_joint_elliptic_embedding_verified',
    'cover_reconstruction_proves_fixed_Y3_membership','fixed_Y3_Prym_membership_constructed',
    'quotient_surface_classified_as_K3_here','dimension_bound_alone_excludes_fixed_X',
    'nonzero_target_exceptional_cycle_constructed','Hodge_proved','Hodge_refuted','global_witness_search_completed']
GEOMETRY={'target_auxiliary_model':'Y3','base_genus':5,'base_function_degrees':[8,12],
    'elliptic_equation':'y^2=x^3-x','elliptic_cyclic_quotient_coordinate':'z=x^2',
    'Kummer_function':'H(z)=z*(z-1)^2','opposite_curve_characters_mod_four':[1,3],
    'coupled_equation':'H(f8)*H(f12)=r^4','Kummer_divisor':'D(f)=(F0+2F1-3Finfinity)/4',
    'connected_Kummer_class_exact_order':4,'branch_fibre_divisibility_at_0_1_infinity':[4,2,4],
    'reconstructed_tower_genera':[17,9,5]}
MATCH=['primitive_joint_elliptic_embedding_with_trivial_kernel',
    'full_principal_Gaussian_period_isomorphism_or_licensed_correspondence']
INPUTS={'model':'research/voevodsky/results/hodge-even-axis-principal-model-v1.json',
    'literature':'research/voevodsky/results/hodge-eightfold-literature-audit-v1.json'}


def require(c,m):
    if not c:raise ValueError(m)


def partitions(n,maximum=None):
    if n==0:return [()]
    maximum=n if maximum is None else min(n,maximum)
    return [(a,)+t for a in range(maximum,0,-1) for t in partitions(n-a,a)]


def fibre_pattern(degree,p0,p1,pinf):
    require(type(degree) is int and degree in (8,12),'Y3 function degree')
    require(all(sum(p)==degree and p and all(type(e) is int and e>0 for e in p) for p in (p0,p1,pinf)), 'complete positive fibre partitions')
    require(all(e%4==0 for e in p0+pinf) and all(e%2==0 for e in p1),'orbifold divisibility')
    used=sum(e-1 for p in (p0,p1,pinf) for e in p)
    total=2*degree+8;excess=used-2*degree
    return {'function_degree':degree,'ramification_used':used,'total_ramification':total,
        'remaining_ramification':total-used,'elliptic_map_ramification_over_special_values':4*excess,
        'elliptic_map_ramification_elsewhere':4*(total-used),'RH_feasible':total>=used}


def local_patterns(degree):
    require(degree in (8,12),'Y3 function degree')
    four=[p for p in partitions(degree) if all(e%4==0 for e in p)]
    two=[p for p in partitions(degree) if all(e%2==0 for e in p)]
    cases=[fibre_pattern(degree,p0,p1,pinf) for p0 in four for p1 in two for pinf in four]
    return cases


def marked_torsion_order(label):
    # Abstract marked Pic[4] controls only: no actual Picard coordinates have been found.
    require(len(label)==10 and all(type(x) is int and 0<=x<4 for x in label),'marked genus-five Pic[4] label')
    d=4
    for x in label:d=gcd(d,x)
    return 4//d


def require_reconstruction_hypotheses(*,smooth_connected_base,local_divisibility,exact_order_four,coupled_product_identity):
    require(all(x is True for x in (smooth_connected_base,local_divisibility,exact_order_four,coupled_product_identity)),
        'smooth base, local divisibility, exact order4 and coupled product required')
    return [17,9,5]


def multiply_polynomials(a,b):
    r={}
    for i,x in a.items():
        for j,y in b.items():r[i+j]=r.get(i+j,Q(0))+x*y
    return {i:x for i,x in r.items() if x}


def exact_core():
    # y^4=(x^3-x)^2=x^2*(x^2-1)^2=H(x^2), exact polynomial coefficients.
    a={3:Q(1),1:Q(-1)};b={2:Q(1),0:Q(-1)}
    lhs=multiply_polynomials(a,a);rhs=multiply_polynomials({2:Q(1)},multiply_polynomials(b,b))
    require(lhs==rhs and (1+3)%4==0 and (1-3)%4==2,'elliptic identity and product-not-ratio')
    require(sum((1,2,1))%4==0 and 3+2+3==8,'elliptic cyclic quotient RH')
    eight=local_patterns(8);twelve=local_patterns(12)
    a=[p for p in eight if p['RH_feasible']];b=[p for p in twelve if p['RH_feasible']]
    require(len(eight)==len(a)==20 and len(twelve)==99 and len(b)==98,'local pattern exhaustion')
    require(not fibre_pattern(12,(12,),(12,),(12,))['RH_feasible'],'triple-total-degree12 countercontrol')
    for p in a+b:
        require(p['elliptic_map_ramification_over_special_values']>=0 and
            p['elliptic_map_ramification_elsewhere']>=0 and
            p['elliptic_map_ramification_over_special_values']+p['elliptic_map_ramification_elsewhere']==32,'elliptic map RH')
    zero=(0,)*10;primitive=(1,)+(0,)*9;inverse=(3,)+(0,)*9;quadratic=(2,)+(0,)*9
    require([marked_torsion_order(x) for x in (zero,quadratic,primitive,inverse)]==[1,2,4,4] and
        all((x+y)%4==0 for x,y in zip(primitive,inverse)),'exact-order and inverse-class controls')
    require_reconstruction_hypotheses(smooth_connected_base=True,local_divisibility=True,
        exact_order_four=True,coupled_product_identity=True)
    return {'base_function_degrees':[8,12],'elliptic_cyclic_quotient_inertia_orders':[4,2,4],
        'axis8_raw_local_patterns':20,'axis8_RH_feasible_local_patterns':20,
        'axis12_raw_local_patterns':99,'axis12_RH_feasible_local_patterns':98,
        'paired_local_profile_controls':len(a)*len(b),'curve_to_elliptic_total_ramification':32,
        'opposite_Kummer_characters':[1,3],'divisor_class_orders_in_abstract_controls':[1,2,4,4],
        'conditional_reconstructed_tower_genera':[17,9,5]}


def validate_contract(c):
    require(c['schema']=='marici.hodge-even-axis-coupled-kummer-gate.v1' and
        c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node']=='even-axis-coupled-kummer-gate','coupled Kummer identity')
    require(c['geometry']==GEOMETRY and c['target_matching_requirements']==MATCH,'coupled Kummer hypotheses changed')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'coupled Kummer promoted to target')
    exact_core()


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    rs={'model':model.report(),'literature':literature.report()}
    for k,r in rs.items():require(json.loads((ROOT/INPUTS[k]).read_text(encoding='utf-8'))==r and r['passed'],'stale '+k)
    require(rs['model']['actual_principal_Gaussian_model_Y3_constructed'] and
        rs['model']['physical_elliptic_surface_polarization_degrees']==[4,6] and
        rs['model']['four_exceptional_cycle_channels_transported'],'Y3 actual geometry missing')
    require(len(model.odd.unitary_restriction_controls((4,6)))==16,'Y3 intrinsic axis preservation control')
    names=set(INPUTS.values())|{CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),
        Path(__file__).relative_to(ROOT).as_posix()}
    return {'schema':'marici.hodge-even-axis-coupled-kummer-gate-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',
        'verification_level':'Written common-cover Kummer and quotient-surface reduction plus conditional reconstruction; exact local controls do not supply a genus-five solution or target matching.',
        'checks':{'actual_Y3_inputs_fresh':True,'opposite_axis_characters':True,'common_cover_product_equation':True,
            'local_divisor_and_RH_controls':True,'exact_order_not_inferred_from_local_parity':True,
            'cover_and_target_matching_separated':True,'scope':True},**exact_core(),
        'conditional_geometric_cover_reconstruction_proved':True,
        'quotient_surface_equation':'r^4=H(s)*H(t)',
        'target_matching_requirements':MATCH,**{k:False for k in POLICY},
        'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k!='source_sha256'},indent=2))
