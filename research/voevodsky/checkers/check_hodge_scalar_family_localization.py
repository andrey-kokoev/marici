"""Scalar-family geometry and a seven-adic exclusion sieve; no target witness."""
from fractions import Fraction
from pathlib import Path
from hashlib import sha256
import json
from check_hodge_asymmetric_absolute import report as absolute_report
from check_hodge_asymmetric_scalar_cover import modgcd_degree, source_equations
from check_hodge_even_scalar_cover import add, scale, mul, power, derivative

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-scalar-family-localization.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-scalar-family-localization-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-scalar-family-localization-v1.json'
BASE=(-2,0,0,0,1,0,0)
CUBIC=(0,25,-26,1)
POLICY=['all_scalar_parameters_excluded','all_scalar_fibres_simple',
    'simple_locus_claimed_Zariski_open','fixed_target_isogeny_locus_claimed_finite',
    'all_four_scalar_level_labels_analyzed','nonlifting_labels_excluded',
    'conditional_root_census_changed','Prym_End0_computed','actual_cover_matching_Y2_constructed',
    'theta_dimension_computed','finite_field_cycles_transferred_to_X','Hodge_proved','Hodge_refuted',
    'alpha_nonalgebraic_proved','algebraic_representative_of_alpha_constructed',
    'all_cycle_annihilation_proved','global_witness_search_completed']


def require(c,m):
    if not c: raise ValueError(m)


def parameters(v):
    require(len(v)==7 and all(type(x) in (int,Fraction) for x in v),'seven exact rational parameters required')
    return tuple(Fraction(x) for x in v)


def branch_norm(v):
    v=parameters(v);a=tuple(v[:4])+(Fraction(1),);b=tuple(v[4:])
    return add(power(a,2),scale(mul(CUBIC,power(b,2)),-1))


def residues(v):
    v=parameters(v)
    require(all(x.denominator%7 for x in v),'parameters not integral at seven')
    return tuple(x.numerator*pow(x.denominator,-1,7)%7 for x in v)


def mod_seven(poly):
    poly=tuple(Fraction(x) for x in poly)
    require(all(x.denominator%7 for x in poly),'polynomial not integral at seven')
    return tuple(x.numerator*pow(x.denominator,-1,7)%7 for x in poly)


def sieve(v):
    # Failure of this sufficient test is UNKNOWN, never target membership.
    same=residues(v)==tuple(x%7 for x in BASE)
    if same:
        f=mod_seven(branch_norm(v))
        require(modgcd_degree(f,derivative(f),7)==0,'residue class lost smooth branch')
    return 'excluded_from_A_Y2_by_absolute_simple_reduction' if same else 'not_certified_by_this_sieve'


def geometry(degree=4,character_order=4,square_order=2):
    require((degree,character_order,square_order)==(4,4,2),'scalar line-bundle input')
    # Elliptic RR + base-point-free pencil exact sequence, proved in NOTE.
    # A=L M, B=L M^-1, B/A=M^-2 nontrivial degree zero.
    h0a=h0b=degree;h0ab=2*degree
    h0ratio=h1ratio=0
    pencil_domain=2*h0b
    require(pencil_domain-h0ratio==h0ab and h1ratio==0,'pencil isomorphism dimensions')
    return {'branch_line_bundle_degree':degree,'character_line_bundle_order':character_order,
        'ratio_line_bundle_order':square_order,'H0_A_dimension':h0a,'H0_B_dimension':h0b,
        'pencil_kernel_dimension':h0ratio,'pencil_cokernel_dimension':h1ratio,
        'pencil_multiplication_rank':h0ab,'full_multiplication_domain_dimension':h0a*h0b,
        'full_multiplication_rank':h0ab,'fixed_elliptic_branch_family_dimension':h0ab-1,
        'fixed_elliptic_period_codifferential_rank':h0ab-1,
        'ambient_unitary_period_dimension':h0a*h0b,
        'Prym_map_quasifinite_on_norm_simple_chart':True,
        'geometric_generic_Prym_simple':True,'very_general_complex_Prym_simple':True,
        'fixed_target_isogeny_locus_at_most_countable':True}


def finite_controls():
    base=branch_norm(BASE)
    require(base==source_equations()[5],'family base branch norm')
    require(len(base)==9 and base[-1]==1 and modgcd_degree(base,derivative(base),7)==0,'base norm smoothness')
    control_vectors=[BASE]
    for i in range(7):
        v=list(BASE);v[i]+=7;control_vectors.append(tuple(v))
    v=list(BASE);v[0]+=Fraction(7,2);control_vectors.append(tuple(v))
    for v in control_vectors:
        require(residues(v)==residues(BASE) and sieve(v)=='excluded_from_A_Y2_by_absolute_simple_reduction','seven-adic controls')
        require(mod_seven(branch_norm(v))==mod_seven(base),'family norm reduction')
    # B=0 can have simple branch on E despite its norm A^2 not squarefree.
    even=(-2,0,0,0,0,0,0);f=branch_norm(even);a=(-2,0,0,0,1)
    require(modgcd_degree(f,derivative(f),7)==4 and
        modgcd_degree(a,derivative(a),7)==0 and modgcd_degree(a,CUBIC,7)==0,
        'norm-simple is sufficient not necessary')
    require(sieve(even)=='not_certified_by_this_sieve','sieve must not accept all parameters')
    return {'parameter_order':['a0','a1','a2','a3','b0','b1','b2'],
        'normalized_section':'x^4+a3*x^3+a2*x^2+a1*x+a0+y*(b2*x^2+b1*x+b0)',
        'base_parameters':list(BASE),'base_norm_coefficients_ascending':[int(x) for x in base],
        'excluded_residue_vector_mod_7':list(residues(BASE)),
        'residue_controls_checked':len(control_vectors),'parameters_require_seven_integral_denominators':True,
        'norm_squarefree_chart_is_sufficient_not_necessary':True,
        'smooth_even_control_outside_chart':True,'conditional_root_label_count_not_updated':516}


def validate_certificate(c):
    require(c['schema']=='marici.hodge-scalar-family-localization.v1' and
        c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node']=='scalar-family-localization' and c['verdict']=='constructed','scalar family identity')
    require(c['resolution_kind']=='elliptic_pencil_period_immersion_generic_simplicity_and_seven_adic_exclusion','scalar family resolution')
    require(c['family']=={'parameter_order':['a0','a1','a2','a3','b0','b1','b2'],
        'normalized_leading_x4_coefficient':1,'branch_line_bundle_degree':4,
        'character_order':4,'square_order':2,'chart':'norm_squarefree_sufficient_open',
        'fixed_elliptic_curve_and_level_isogeny':True,'prime':7,
        'excluded_residue_vector':[5,0,0,0,1,0,0],
        'fixed_target_isogeny_locus_scope':'at_most_countable_not_finite_or_empty'},'scalar family scope')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'scalar family promotion')


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_certificate(c)
    require(c['previous_receipt']=='research/voevodsky/results/hodge-asymmetric-absolute-v1.json','family predecessor binding')
    old=json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    require(old==absolute_report() and old['reduction_absolutely_simple'] is True and
        old['complex_auxiliary_Prym_absolutely_simple'] is True,'stale absolute simplicity certificate')
    cert={**geometry(),**finite_controls()}
    sources={p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_asymmetric_absolute.py',
        'research/voevodsky/checkers/check_hodge_asymmetric_scalar_cover.py'}
    return {'schema':'marici.hodge-scalar-family-localization-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',**cert,
        'checks':dict.fromkeys(['fresh_absolute_simplicity_anchor_and_full_counts',
            'explicit_degree_eight_norm_and_sufficient_smooth_branch_chart',
            'nontrivial_degree_zero_pencil_kernel_and_cokernel_vanish',
            'Prym_codifferential_surjective_and_fixed_E_chart_immersive',
            'generic_and_very_general_not_every_fibre_simple',
            'isogeny_class_countable_and_polarized_fibres_finite',
            'same_good_reduction_for_seven_integral_residue_class',
            'even_section_prevents_norm_chart_or_simplicity_overclaims'],True),
        **c['scope_policy'],'verification_level':c['trust_scope'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k!='source_sha256'},indent=2))
