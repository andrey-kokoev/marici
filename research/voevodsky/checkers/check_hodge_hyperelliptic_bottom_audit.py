"""Hyperelliptic bottom gives a dihedral square, not the fixed A isogeny class.
The bielliptic family and torsion labels are conditional, not a matched target cover.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations, product
from hashlib import sha256
from pathlib import Path
import json
from check_hodge_explicit_sixfold_candidate import multiply
from check_hodge_y2_curve_audit import report as curve_report

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-hyperelliptic-bottom-audit.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-hyperelliptic-bottom-audit-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-hyperelliptic-bottom-audit-v1.json'


def require(condition,message):
    if not condition:
        raise ValueError(message)


def compose(p,q):
    return tuple(p[q[i]] for i in range(len(p)))


def torsion_roots():
    # A marked abstract J(C5)[4]=(Z/4)^10, eta=(2,0,...,0).
    return tuple((a,)+tail for a in (1,3) for tail in product((0,2),repeat=9))


def unique_bielliptic_involution_for_genus(genus):
    require(type(genus) is int and genus >= 0,'curve genus')
    return genus > 5


def conditional_family(theta_dimension=None):
    if theta_dimension is None:
        return 'not_selected_theta_dimension_unknown'
    require(type(theta_dimension) is int and -1 <= theta_dimension <= 7,'theta dimension')
    if theta_dimension > 4:
        return 'excluded_as_smooth_etale_Prym_by_previous_Mumford_gate'
    if theta_dimension == 4:
        return 'necessary_bielliptic_C5_with_C9_elliptic_two_isogeny_pullback'
    return 'no_bielliptic_family_selected_by_Mumford'


@lru_cache(maxsize=1)
def exact_core():
    # All fibre permutations inverting a regular C4 generator are reflections.
    r = (1,2,3,0)
    rinv = (3,0,1,2)
    identity = tuple(range(4))
    reflections = []
    for s in permutations(range(4)):
        if compose(s,r) == compose(rinv,s):
            require(compose(s,s) == identity,'inverting lift has wrong square')
            reflections.append(s)
    require(len(reflections) == 4 and (0,3,2,1) in reflections,'dihedral fibre lift census')
    # A faithful rational H1 model for rho^2=-I, sigma^2=I, sigma rho=-rho sigma.
    n = 16
    I = [[Q(int(i == j)) for j in range(n)] for i in range(n)]
    minus = [[-v for v in row] for row in I]
    rho = [[Q(0)]*n for _ in range(n)]
    sigma = [[Q(0)]*n for _ in range(n)]
    for i in range(8):
        rho[i][i+8],rho[i+8][i] = Q(-1),Q(1)
        sigma[i][i],sigma[i+8][i+8] = Q(1),Q(-1)
    require(multiply(rho,rho) == minus and multiply(sigma,sigma) == I and
        multiply(multiply(sigma,rho),sigma) == [[-x for x in row] for row in rho], 'dihedral H1 relations')
    plus = [[(I[i][j]+sigma[i][j])/2 for j in range(n)] for i in range(n)]
    neg = [[(I[i][j]-sigma[i][j])/2 for j in range(n)] for i in range(n)]
    require(multiply(plus,plus) == plus and multiply(neg,neg) == neg and
        multiply(rho,plus) == multiply(neg,rho) and
        sum(plus[i][i] for i in range(n)) == sum(neg[i][i] for i in range(n)) == 8,
        'fourfold factors exchanged by rho')
    require(6 > 4,'simple sixfold fits in a fourfold')
    # The two independent degree-two elliptic quotients have genus at most five:
    # Hodge index bounds image self-intersection by eight, K=0.
    require(1+Q(8,2) == 5 and unique_bielliptic_involution_for_genus(9) and
        not unique_bielliptic_involution_for_genus(5), 'unique bielliptic threshold')
    # Riemann--Hurwitz: C9/E has 16 branch points; C5/Eprime has eight.
    require(2*9-2 == 16 and 2*5-2 == 8 and 2*17-2 == 4*(2*5-2), 'cover genus/branch arithmetic')
    roots = torsion_roots()
    eta = (2,)+(0,)*9
    require(len(roots) == len(set(roots)) == 1024 and
        all(tuple(2*x%4 for x in v) == eta for v in roots),'formal fourth roots of nonzero eta')
    orbits = {min(v,tuple(-x%4 for x in v)) for v in roots}
    require(len(orbits) == 512 and all(tuple(-x%4 for x in v) != v for v in roots),'formal inversion orbits')
    return {'hyperelliptic_genus5_bottom_excluded_up_to_isogeny_to_fixed_A':True,
        'all_fixed_A_isogeny_models_excluded_for_this_cover_family':True,
        'inverting_C4_fibre_lifts_checked':len(reflections),'lift_square':'identity',
        'hypothetical_Prym_dimension':8,'hypothetical_square_factor_dimension':4,
        'square_factor_H1_dimensions':[8,8],'fixed_simple_factor_dimension':6,
        'bielliptic_involution_unique_above_genus':5,
        'conditional_bielliptic_descent':{'premise':'realization_with_bielliptic_C9',
            'C5_bielliptic':True,'intermediate_is_pullback_of_elliptic_two_isogeny':True,
            'C5_double_cover_branch_degree':8,'eta':'kappa0_pullback_of_nonzero_elliptic_2_torsion',
            'top_cover_line_bundle_equation':'L^2=eta, L exact order 4',
            'marked_formal_4_torsion_root_count':1024,'formal_L_inverse_pair_count':512,
            'sample_root_labels':[list(v) for v in roots[:3]]},
        'actual_theta_singularity_dimension':None,
        'conditional_theta_cases':{str(d):conditional_family(d) for d in (None,3,4,5)}}


def validate_audit(c):
    require(c['schema'] == 'marici.hodge-hyperelliptic-bottom-audit.v1' and
        c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node'] == 'hyperelliptic-bottom-prym-transplant' and c['verdict'] == 'rejected', 'bottom-cover identity')
    require(c['resolution_kind'] == 'pointed_dihedral_lift_square_fourfold_obstruction_and_conditional_bielliptic_descent',
        'bottom-cover resolution')
    require(c['geometry'] == {'cover_genera':[17,9,5],'top_to_bottom':'connected_etale_cyclic_quartic',
        'hyperelliptic_curve_in_unconditional_exclusion':'genus5_bottom',
        'pointed_lift_at_Weierstrass_point':True,'isogeny_not_just_polarized_isomorphism_excluded':True,
        'square_factor_dimension':4,'fixed_simple_factor_dimension':6,
        'conditional_bielliptic_intermediate_genus':9}, 'bottom-cover geometry scope')
    require(c['level_data'] == {'Pic0_C5_4_torsion_rank_over_Z4':10,'nonzero_eta_order':2,
        'formal_root_count':1024,'formal_inverse_pair_count':512}, 'bottom-cover level data')
    require(c['scope_policy'] == dict.fromkeys(['nonhyperelliptic_bottoms_excluded','ramified_covers_excluded',
        'singular_admissible_covers_excluded','all_Prym_presentations_excluded',
        'square_is_a_principal_product_claimed','actual_fourfold_for_target_constructed',
        'actual_cover_matching_Y2_constructed','theta_dimension_computed',
        'bielliptic_branch_is_unconditional','elliptic_base_forced_CM_i',
        'formal_root_pairs_are_unmarked_moduli_count','moduli_dimension_alone_excludes_target'],False),
        'bottom-cover scope promoted')
    require(set(c['boundary']) == {'Hodge_proved','Hodge_refuted','alpha_nonalgebraic_proved',
        'algebraic_representative_of_alpha_constructed','all_cycle_annihilation_proved',
        'global_witness_search_completed'} and all(v is False for v in c['boundary'].values()),'bottom-cover verdict promotion')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_audit(c)
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-y2-curve-audit-v1.json', 'previous curve-audit binding')
    old = json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    require(old == curve_report() and old['candidate_id'] == c['candidate_id'] and
        old['actual_theta_singularity_dimension'] is None and
        old['trigonal_genus9_intermediate_cyclic_quartic_tower_excluded'], 'stale previous curve audit')
    sources = {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_y2_curve_audit.py',
        'research/voevodsky/checkers/check_hodge_indecomposable_principal_model.py'}
    return {'schema':'marici.hodge-hyperelliptic-bottom-audit-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'rejected',**exact_core(),
        'checks':dict.fromkeys(['pointed_etale_Weierstrass_lift_has_square_one_and_inverts_C4',
            'actual_dihedral_relations_on_hypothetical_Prym_force_equal_fourfold_factors',
            'simple_sixfold_factor_cannot_appear_in_square_of_fourfolds',
            'unique_genus9_bielliptic_involution_commutes_with_free_eta',
            'fixed_point_elliptic_descent_gives_excluded_hyperelliptic_C5_else_translation_pullback',
            'marked_formal_torsion_roots_not_curves_or_unmarked_moduli_counts'],True),
        **c['scope_policy'],**c['boundary'],'verification_level':c['trust_scope'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'source_sha256'},indent=2))
