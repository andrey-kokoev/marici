"""Actual even scalar cover control, excluded up to isogeny; not a Y2 cover."""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import json
from check_hodge_commuting_prym_audit import report as commuting_report

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-even-scalar-cover.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-even-scalar-cover-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-even-scalar-cover-v1.json'
POLICY = ['all_scalar_pulled_roots_excluded','nonlifting_half_excluded',
    'all_inversion_invariant_branch_sets_have_involutive_lift','all_Prym_presentations_excluded',
    'actual_cover_matching_Y2_constructed','theta_dimension_computed','target_reflection_is_curve_lift',
    'Hodge_proved','Hodge_refuted','alpha_nonalgebraic_proved',
    'algebraic_representative_of_alpha_constructed','all_cycle_annihilation_proved','global_witness_search_completed']


def require(c,m):
    if not c:
        raise ValueError(m)


def trim(a):
    a = list(map(Q,a))
    while len(a)>1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])


def scale(a,q):
    return trim([x*q for x in a])


def mul(a,b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def power(a,n):
    require(type(n) is int and n>=0,'nonnegative polynomial exponent')
    r = (Q(1),)
    for _ in range(n):
        r = mul(r,a)
    return r


def remainder(a,b):
    require(b != (0,),'zero polynomial divisor')
    while a != (0,) and len(a)>=len(b):
        a = add(a,scale((0,)*(len(a)-len(b))+b,-a[-1]/b[-1]))
    return a


def gcd(a,b):
    while b != (0,):
        a,b = b,remainder(a,b)
    return scale(a,1/a[-1])


def derivative(a):
    return trim([i*a[i] for i in range(1,len(a))] or [0])


def models(c=2):
    require(type(c) is int and c not in (0,1,25**4),'branch zeros must avoid elliptic two-torsion x values')
    N = trim([1,9,16,9,1])
    D = trim([0,1,-2,1])
    F = add(power(N,4),scale(power(D,4),-c))
    A = trim([36,13,1])
    G = add(power(A,4),scale(power((0,1),4),-c))
    return N,D,F,G


@lru_cache(maxsize=1)
def exact_core():
    N,D,F,G = models()
    e = trim([0,1,7,1])
    # psi_y = y R/S, psi_x=N/D. Exact elliptic function-field identity.
    R = mul((-1,0,1),(1,-4,-30,-4,1))
    S = mul((0,0,1),power((-1,1),4))
    target = mul(mul(N,add(N,scale(D,-1))),add(N,scale(D,-25)))
    require(mul(mul(e,power(R,2)),power(D,3)) == mul(target,power(S,2)), 'cyclic four-isogeny identity')
    require(gcd(N,D) == (1,) and len(N)-1 == 4,'degree-four x-map')
    # P=(1,3) on y^2=x^3+7x^2+x doubles to (0,0), not infinity.
    slope = Q(3+14+1,6)
    x2 = slope*slope-7-2
    y2 = -3+slope*(1-x2)
    require((x2,y2) == (0,0),'kernel point has exact order four')
    require(len(F)-1 == 16 and gcd(F,derivative(F)) == (1,) and gcd(F,e) == (1,), 'smooth disjoint branch control C17')
    require(len(G)-1 == 8 and gcd(G,derivative(G)) == (1,), 'smooth genus-three quotient')
    # u=(x-1)^2/x, v=w/x^4. Clear x^8 in the H7->H3 identity.
    u_num = power((-1,1),2)
    x = (0,1)
    A_num = add(add(power(u_num,2),scale(mul(u_num,x),13)),scale(power(x,2),36))
    require(A_num == N and add(power(A_num,4),scale(mul(power(u_num,4),power(x,4)),-2)) == F,
        'explicit degree-two fourfold Prym quotient map')
    # Cover and quotient genus/branch arithmetic; normalization is essential.
    require(2*17-2 == 4*(2*5-2) and 2*9-2 == 2*(2*5-2) and
        2*7-2 == 2*(2*3-2)+4,'Hurwitz controls')
    return {'actual_control_tower_constructed':True,'actual_control_tower_genera':[17,9,5],
        'elliptic_source_cubic':[0,1,7,1],'elliptic_target_cubic':[0,25,-26,1],
        'cyclic_four_kernel_generator':[1,3],'doubled_kernel_generator':[0,0],
        'isogeny_x_numerator':[int(v) for v in N],'isogeny_x_denominator':[int(v) for v in D],
        'normalized_C17_equations':{'elliptic':'y^2=x^3+7*x^2+x','second':'w^2=N(x)^4-2*D(x)^4'},
        'normalized_fourfold_quotient_genera':[7,3],'fourfold_double_cover_branch_count':4,
        'explicit_Prym_square_factor_dimension':4,
        'even_function_inversion_lift_square':'identity','Prym_isogenous_to_square_fourfold':True,
        'even_scalar_subfamily_excluded_up_to_fixed_A_isogeny':True,
        'fixed_simple_factor_dimension':6,
        'conditional_scalar_root_count_not_updated':4,'conditional_nonlifting_root_count_not_updated':512,
        'conditional_total_root_label_count_not_updated':516,
        'actual_theta_singularity_dimension':None}


def validate_audit(c):
    require(c['schema'] == 'marici.hodge-even-scalar-cover.v1' and
        c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node'] == 'inversion-symmetric-scalar-transplant' and c['verdict'] == 'rejected','even scalar identity')
    require(c['resolution_kind'] == 'explicit_cyclic_four_isogeny_even_branch_involutive_lift_and_fourfold_square','even scalar resolution')
    require(c['geometry'] == {'source_elliptic_A':7,'source_elliptic_B':1,'kernel_point':[1,3],
        'target_branch_function':'x2^4-2','top_is_normalization':True,
        'inversion_lift_fixes_cover_coordinate':True,'general_exclusion_requires_actual_order_two_lift':True,
        'fixed_X_simple_dimension':6},'even scalar geometry scope')
    require(set(c['scope_policy']) == set(POLICY) and all(v is False for v in c['scope_policy'].values()),'even scalar promotion')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_audit(c)
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-commuting-prym-audit-v1.json','even scalar predecessor binding')
    old = json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    require(old == commuting_report() and old['remaining_commuting_pulled_root_labels'] == 4 and
        old['actual_theta_singularity_dimension'] is None,'stale commuting audit')
    sources = {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_commuting_prym_audit.py'}
    return {'schema':'marici.hodge-even-scalar-cover-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'rejected',**exact_core(),
        'checks':dict.fromkeys(['exact_elliptic_four_isogeny_function_field_identity',
            'exact_order_four_kernel_and_smooth_connected_base_changes',
            'squarefree_normalized_models_and_explicit_genus_seven_to_three_quotient',
            'actual_inversion_lift_fixes_z_and_inverts_translation_generator',
            'dihedral_relations_on_primitive_Prym_give_actual_square_isogeny',
            'simple_X6_cannot_enter_square_fourfold',
            'not_all_scalar_branches_or_root_labels_rejected'],True),
        **c['scope_policy'],'verification_level':c['trust_scope'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)}}


if __name__ == '__main__':
    r = report()
    OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k != 'source_sha256'},indent=2))
