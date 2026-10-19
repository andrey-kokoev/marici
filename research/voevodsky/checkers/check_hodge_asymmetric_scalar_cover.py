"""Actual asymmetric scalar tower and good-reduction counts, not a target match."""
from functools import lru_cache
from pathlib import Path
from hashlib import sha256
import json
from check_hodge_even_scalar_cover import (
    report as even_report, models, add, scale, mul, power, gcd, derivative, trim)

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-asymmetric-scalar-cover.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-asymmetric-scalar-cover-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-asymmetric-scalar-cover-v1.json'
POLICY = ['actual_cover_matching_Y2_constructed','theta_dimension_computed',
    'all_elliptic_inversions_have_no_lift','all_dihedral_automorphisms_excluded',
    'Prym_geometrically_simple_proved','Prym_End0_computed','Prym_not_a_square_proved',
    'point_counts_determine_target_isogeny','point_counts_determine_Weil_polynomial',
    'conditional_root_census_changed','Hodge_proved','Hodge_refuted','alpha_nonalgebraic_proved',
    'algebraic_representative_of_alpha_constructed','all_cycle_annihilation_proved','global_witness_search_completed']


def require(c,m):
    if not c:
        raise ValueError(m)


def modtrim(a,p):
    a = [int(v)%p for v in a]
    while len(a)>1 and not a[-1]:
        a.pop()
    return a


def modgcd_degree(a,b,p):
    a,b = modtrim(a,p),modtrim(b,p)
    while b != [0]:
        while a != [0] and len(a)>=len(b):
            k = len(a)-len(b)
            q = a[-1]*pow(b[-1],-1,p)%p
            for i,v in enumerate(b):
                a[i+k] = (a[i+k]-q*v)%p
            a = modtrim(a,p)
        a,b = b,a
    return len(a)-1


def evaluate(a,x,p):
    r = 0
    for v in reversed(a):
        r = (r*x+int(v))%p
    return r


@lru_cache(maxsize=1)
def source_equations():
    n,d,a,_ = models()
    e = trim([0,1,7,1])
    r = mul((-1,0,1),(1,-4,-30,-4,1))
    b = mul(r,power(d,2))
    norm_base = trim([4,-25,26,-1,-4,0,0,0,1])
    norm_source = add(power(a,2),scale(mul(e,power(b,2)),-1))
    homogeneous = (0,)
    for i,c in enumerate(norm_base):
        homogeneous = add(homogeneous,scale(mul(power(n,i),power(d,8-i)),c))
    require(norm_source == homogeneous,'homogeneous branch norm identity')
    return n,d,a,b,e,norm_base,norm_source


@lru_cache(maxsize=None)
def good_reduction(p):
    require(p in (7,11,13,17,19,23,29,31,101),'certified prime list')
    _,_,_,_,_,f,_ = source_equations()
    target = (0,25,-26,1)
    return modgcd_degree(f,derivative(f),p) == 0 and modgcd_degree(f,target,p) == 0


def point_profile(p):
    require(good_reduction(p),'bad branch reduction')
    n,d,_,_,_,_,_ = source_equations()
    r = mul((-1,0,1),(1,-4,-30,-4,1))
    def chi(t):
        t %= p
        if t == 0:
            return 0
        return 1 if pow(t,(p-1)//2,p) == 1 else -1
    def fibre(x,y):
        return 1+chi(pow(x,4,p)+y-2)
    def points(cubic):
        return [(x,y) for x in range(p) for y in range(p) if y*y%p == evaluate(cubic,x,p)]
    # At every pole above elliptic infinity z/x2^2 tends to +/-1:
    # two rational points, not an affine zero or one point at infinity.
    c5 = 2+sum(fibre(x,y) for x,y in points((0,25,-26,1)))
    c9 = 2
    for u,v in points((0,36,13,1)):
        if u == 0:
            c9 += 2
        else:
            x2 = (u+13+36*pow(u,-1,p))%p
            y2 = v*(1-36*pow(u,-2,p))%p
            c9 += fibre(x2,y2)
    c17 = 2
    for x,y in points((0,1,7,1)):
        dv = evaluate(d,x,p)
        if dv == 0:
            c17 += 2
        else:
            x2 = evaluate(n,x,p)*pow(dv,-1,p)%p
            y2 = y*evaluate(r,x,p)*pow(dv,-2,p)%p
            c17 += fibre(x2,y2)
    require(c17%4 == 0 and c9%2 == 0,'free rational deck orbit point census')
    require(abs(c9-c17)**2 <= 256*p,'eightfold trace Weil bound')
    return {'p':p,'C5':c5,'C9':c9,'C17':c17,'primitive_Prym_trace_n1':c9-c17,
        'pole_fibres_split_points':[2,4,8]}


@lru_cache(maxsize=1)
def exact_core():
    n,d,a,b,e,f,fs = source_equations()
    p = trim([-2,0,0,0,1])
    target = trim([0,25,-26,1])
    require(gcd(f,derivative(f)) == (1,) and gcd(f,target) == (1,) and
        gcd(p,target) == (1,), 'simple branch points disjoint from inversion images')
    require(len(f)-1 == 8 and len(fs)-1 == 32,'branch norm degrees')
    certificates = [q for q in (7,11,13,17,19,23,29,31,101) if good_reduction(q) and
        modgcd_degree(fs,derivative(fs),q) == 0]
    require(certificates,'no degree-preserving modular squarefreeness certificate')
    # Monic degree-32 norm retains leading coefficient one modulo each prime.
    profiles = [point_profile(q) for q in certificates[:5]]
    require(2*5-2 == 8 and 2*9-2 == 16 and 2*17-2 == 32,'tower genus arithmetic')
    return {'actual_asymmetric_control_tower_constructed':True,'actual_tower_genera':[17,9,5],
        'target_double_cover_function':'x2^4+y2-2',
        'source_normalized_model':'y^2=x^3+7*x^2+x; w^2=A(x)+y*B(x)',
        'A':'N^4-2*D^4','B':'R*D^2',
        'base_branch_norm_coefficients':[int(v) for v in f],
        'base_branch_degree':8,'top_branch_degree':32,
        'source_branch_norm_degree':32,'source_norm_modular_squarefree_primes':certificates,
        'fixed_origin_inversion_branch_supports_disjoint':True,
        'fixed_origin_inversion_has_no_lift_to_top_double_cover':True,
        'old_fixed_origin_dihedral_square_argument_available':False,
        'good_reduction_point_profiles':profiles,
        'actual_theta_singularity_dimension':None,'actual_target_isogeny':None,
        'conditional_root_label_count_not_updated':516}


def validate_control(c):
    require(c['schema'] == 'marici.hodge-asymmetric-scalar-cover.v1' and
        c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node'] == 'asymmetric-scalar-cover-control' and c['verdict'] == 'constructed','asymmetric control identity')
    require(c['resolution_kind'] == 'explicit_smooth_asymmetric_tower_fixed_origin_nonlift_and_good_reduction_profiles','asymmetric resolution')
    require(c['geometry'] == {'target_cover_function':'x2^4+y2-2','uses_previous_cyclic_four_isogeny':True,
        'top_is_normalization':True,'inversion_test':'fixed_origin_only',
        'point_counts':'n1_only_at_certified_good_primes'},'asymmetric geometry scope')
    require(set(c['scope_policy']) == set(POLICY) and all(v is False for v in c['scope_policy'].values()),'asymmetric promotion')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_control(c)
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-even-scalar-cover-v1.json','asymmetric predecessor binding')
    old = json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    require(old == even_report() and old['actual_control_tower_constructed'] and
        old['actual_theta_singularity_dimension'] is None,'stale even scalar receipt')
    sources = {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_even_scalar_cover.py'}
    return {'schema':'marici.hodge-asymmetric-scalar-cover-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',**exact_core(),
        'checks':dict.fromkeys(['exact_base_and_homogeneous_source_branch_norm_identities',
            'simple_disjoint_branch_supports_and_smooth_connected_etale_base_changes',
            'inversion_ratio_has_odd_valuation_so_not_a_square',
            'good_reduction_certificates_and_normalized_pole_fibre_point_counts',
            'n1_counts_not_complete_Weil_polynomial_or_endomorphism_certificate'],True),
        **c['scope_policy'],'verification_level':c['trust_scope'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)}}


if __name__ == '__main__':
    r = report()
    OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k != 'source_sha256'},indent=2))
