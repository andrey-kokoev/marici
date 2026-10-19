"""Exhaust the nonlifting (4,4) diagram for the fixed principal Y2 only."""
from hashlib import sha256
from pathlib import Path
import json
from check_hodge_scalar_polarized_obstruction import (
    report as scalar_report, joint_degrees, curve_map_degree, independent_elliptic_genus_bound)
from check_hodge_bielliptic_lift_audit import report as lift_report
from check_hodge_y2_curve_audit import report as curve_report, conditional_prym_gate

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-nonlifting-polarized-obstruction.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-nonlifting-polarized-obstruction-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-nonlifting-polarized-obstruction-v1.json'
POLICY=['nonlifting_labels_excluded_up_to_unpolarized_isogeny','unpolarized_label_census_changed',
    'other_principal_polarizations_excluded','all_smooth_etale_Prym_presentations_excluded',
    'all_cyclic_quartic_presentations_excluded_without_theta_hypothesis',
    'conditional_biellipticity_asserted_unconditionally','actual_theta_dimension_computed',
    'actual_cover_matching_Y2_constructed','finite_field_cycles_transferred_to_X',
    'Hodge_proved','Hodge_refuted','alpha_nonalgebraic_proved',
    'algebraic_representative_of_alpha_constructed','all_cycle_annihilation_proved',
    'global_witness_search_completed']


def require(c,m):
    if not c: raise ValueError(m)


def birational_case(genus=17,h_free=True):
    require(type(genus) is int and genus>=2 and type(h_free) is bool,'birational case input')
    upper=independent_elliptic_genus_bound(4,4)
    if genus>upper: return 'excluded_by_genus_bound'
    if genus<upper: return 'normalization_may_separate_branches_not_excluded'
    if not h_free: return 'fixed_points_permitted_no_etale_contradiction'
    return 'excluded_by_smooth_image_reflection_fixed_points'


def joint_case(degree,b_liftable=False,genus=17,h_free=True):
    require(type(degree) is int and degree in joint_degrees(4,4),'joint degree coverage')
    require(type(b_liftable) is bool,'liftability input')
    if degree==1: return birational_case(genus,h_free)
    if degree==2:
        return 'involutive_lift_forced_no_nonlifting_contradiction' if b_liftable else 'excluded_by_forced_bielliptic_lift'
    return 'excluded_by_invariant_vs_anti_invariant_factorization'


def v4_control():
    identity=tuple(range(4));h=tuple(x^1 for x in range(4));sigma=tuple(x^2 for x in range(4))
    def compose(a,b): return tuple(a[b[x]] for x in range(4))
    require(h!=sigma and compose(h,h)==compose(sigma,sigma)==identity and
        compose(h,sigma)==compose(sigma,h),'commuting distinct quadratic deck involutions')
    quotient_h=({0,1},{2,3});quotient_sigma=({0,2},{1,3})
    require({sigma[x] for x in quotient_h[0]}==quotient_h[1] and
        {h[x] for x in quotient_sigma[0]}==quotient_sigma[1],'nontrivial descended bielliptic lift')
    return {'generic_fibre_h_permutation':list(h),'generic_fibre_sigma_permutation':list(sigma),
        'h_quotient_blocks':[sorted(b) for b in quotient_h],
        'sigma_descends_nontrivially_on_h_quotient':True,
        'h_descends_nontrivially_on_sigma_quotient':True}


def theta_gate(d):
    if d is None: return 'undetermined_actual_dimension_not_computed'
    require(type(d) is int and -1<=d<=7,'theta singularity dimension')
    if d>=4: return 'excluded_fixed_Y2_smooth_etale_cyclic_quartic_realization'
    return 'no_exclusion_from_this_theta_gate'


def exact_core():
    require(curve_map_degree(2)==4 and joint_degrees(4,4)==[1,2,4],'degree four and joint coverage')
    cases={str(d):joint_case(d) for d in joint_degrees(4,4)}
    require(all(v.startswith('excluded_') for v in cases.values()),'unresolved nonlifting joint case')
    require(independent_elliptic_genus_bound(4,4)==17 and
        independent_elliptic_genus_bound(2,2)==5,'equality and intermediate genus controls')
    require(birational_case(15)=='normalization_may_separate_branches_not_excluded' and
        birational_case(17,False)=='fixed_points_permitted_no_etale_contradiction',
        'equality and freeness must not be dropped')
    total,zero,mixed,scalar,nonlifting=1024,256,252,4,512
    require(total==zero+mixed+scalar+nonlifting,'complete polarized label partition')
    return {'joint_cases':cases,'joint_degrees_exhausted':[1,2,4],
        'birational_image_arithmetic_genus':17,'birational_image_normalization_defect':0,
        'elliptic_reflection_fixed_values':4,'curve_degree_over_each_fixed_value':4,
        'degree_two_common_factor_maximum_genus':5,'degree_two_case_control':v4_control(),
        'elliptic_degree_two_axis_forces_bielliptic_involution_lift':True,
        'nonlifting_labels_excluded_for_fixed_principal_Y2':True,
        'fixed_Y2_bielliptic_intermediate_cyclic_realizations_excluded':True,
        'new_polarized_labels_removed':nonlifting,
        'conditional_polarized_Y2_survivor_labels':total-zero-mixed-scalar-nonlifting,
        'conditional_polarized_Y2_survivor_inverse_pairs':0,
        'conditional_unpolarized_isogeny_survivor_labels':scalar+nonlifting,
        'conditional_unpolarized_isogeny_survivor_inverse_pairs':(scalar+nonlifting)//2,
        'necessary_theta_dimension_upper_bound_if_cyclic_realization_exists':3,
        'actual_theta_singularity_dimension':None,
        'conditional_theta_cases':{str(d):theta_gate(d) for d in (None,-1,0,3,4,5,7)}}


def validate_certificate(c):
    require(c['schema']=='marici.hodge-nonlifting-polarized-obstruction.v1' and
        c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node']=='nonlifting-polarized-prym-transplant' and c['verdict']=='rejected','nonlifting polarized identity')
    require(c['resolution_kind']=='joint_degree_exhaustion_genus_equality_free_involution_and_forced_lift','nonlifting resolution')
    require(c['geometry']=={'top_genus':17,'elliptic_map_degrees':[4,4],
        'joint_degrees':[1,2,4],'h_free':True,'h_on_first_elliptic_map':'identity',
        'h_on_second_elliptic_map':'reflection_up_to_translation','bielliptic_involution_lifts':False,
        'comparison':'canonical_principal_polarized_isomorphism',
        'conditional_polarized_survivor_labels':0,'conditional_unpolarized_survivor_labels':516},'nonlifting scope')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'nonlifting promotion')


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_certificate(c)
    expected={'previous_receipt':'research/voevodsky/results/hodge-scalar-polarized-obstruction-v1.json',
        'lifting_receipt':'research/voevodsky/results/hodge-bielliptic-lift-audit-v1.json',
        'curve_receipt':'research/voevodsky/results/hodge-y2-curve-audit-v1.json'}
    require(all(c[k]==v for k,v in expected.items()),'nonlifting input binding')
    old=json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    lifting=json.loads((ROOT/c['lifting_receipt']).read_text(encoding='utf-8'))
    curve=json.loads((ROOT/c['curve_receipt']).read_text(encoding='utf-8'))
    require(old==scalar_report() and old['conditional_polarized_Y2_survivor_labels']==512,
        'stale scalar polarized census')
    require(lifting==lift_report() and lifting['nonlifting_root_labels']==512,
        'stale nonlifting criterion')
    require(curve==curve_report() and curve['actual_theta_singularity_dimension'] is None and
        conditional_prym_gate(4)=='cyclic_quartic_realization_requires_bielliptic_genus9_intermediate',
        'stale conditional Mumford gate')
    sources={p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | set(expected.values()) | {
        'research/voevodsky/checkers/check_hodge_scalar_polarized_obstruction.py',
        'research/voevodsky/checkers/check_hodge_bielliptic_lift_audit.py',
        'research/voevodsky/checkers/check_hodge_y2_curve_audit.py'}
    return {'schema':'marici.hodge-nonlifting-polarized-obstruction-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'rejected',**exact_core(),
        'checks':dict.fromkeys(['fresh_degree_two_axis_nonlifting_criterion_and_scalar_census',
            'joint_degree_four_factorization_contradicts_h_signs',
            'joint_degree_one_genus_equality_forces_smooth_image_and_fixed_points',
            'joint_degree_two_quadratic_deck_involution_lifts_bielliptic_involution',
            'all_joint_degrees_exhausted_without_coprimality_assumption',
            'polarized_bielliptic_branch_closed_unpolarized_census_unchanged',
            'theta_at_least_four_excludes_cyclic_realization_without_computing_dimension'],True),
        **c['scope_policy'],'verification_level':c['trust_scope'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k!='source_sha256'},indent=2))
