"""Fixed Y2 Jacobian exclusion and necessary low-gonality Prym constraints.
Strong Torelli and Mumford are explicit theorem imports, not finite controls.
"""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import permutations
from math import comb
from pathlib import Path
import json
from check_hodge_indecomposable_principal_model import (
    gaussian_matrix, f_push, channels_new, report as model_report)
from check_hodge_secant_sheaf_transplant import gmatrix_product, gdet
from check_hodge_split_eightfold_stabilization import DS8, R_B, wedge, scale, full_pullback
from check_hodge_eightfold_weil_filter import generators

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-y2-curve-audit.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-y2-curve-audit-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-y2-curve-audit-v1.json'
SNAPSHOT = 'research/voevodsky/inputs/hodge-y2-curve-audit-v1/sources.json'
BASE = 'research/voevodsky/inputs/hodge-y2-curve-audit-v1/'
FILES = ('milne-JVs.pdf','milne-JVs.txt','milne.p37.txt','milne.p38.txt',
         'milne.p37.png','milne.p38.png','torelli-search.txt')


def require(condition,message):
    if not condition:
        raise ValueError(message)


def load(path):
    return json.loads((ROOT/path).read_text(encoding='utf-8'))


def validate_sources():
    d = load(SNAPSHOT)
    require(d['schema'] == 'marici.hodge-y2-curve-sources.v1' and d['author'] == 'J.S. Milne' and
        d['title'] == 'Jacobian Varieties' and d['version'] == 'June 12, 2021' and
        d['url'] == 'https://www.jmilne.org/math/xnotes/JVs.pdf','Torelli source identity')
    require(d['pdf'] == BASE+'milne-JVs.pdf' and d['text'] == BASE+'milne-JVs.txt' and
        d['rendered_pdf_pages'] == [37,38] and d['theorem_pdf_page'] == 38 and
        len(d['files']) == 7 and {r['path'] for r in d['files']} == {BASE+n for n in FILES}, 'Torelli source coverage')
    for row in d['files']:
        require(sha256((ROOT/row['path']).read_bytes()).hexdigest() == row['sha256'],'Torelli source drift')
    require((ROOT/d['pdf']).read_bytes().startswith(b'%PDF'),'Torelli PDF')
    text = ' '.join((ROOT/(BASE+'milne.p38.txt')).read_text(encoding='utf-8').split())
    require(all(s in text for s in ('THEOREM 12.1.','complete smooth curves','canonically polarized',
        'If C is not hyperelliptic','uniquely determined')), 'Torelli polarized/sign theorem anchors')


def hyperelliptic_elliptic_genus_bound(degree):
    # Independence is proved separately: a common factor of degree two would
    # factor the elliptic map through P1, impossible in characteristic zero.
    require(type(degree) is int and degree >= 1,'positive elliptic cover degree')
    return 2*degree-1


def trigonal_free_involution_obstruction(genus):
    require(type(genus) is int and genus >= 0,'curve genus')
    # Distinct degree-three pencils give a birational image in P1 x P1,
    # with arithmetic genus four; below this threshold uniqueness is not inferred.
    return genus > 4


def conditional_prym_gate(singularity_dimension):
    """Conditional on a smooth etale cyclic-quartic realization of this Y2."""
    if singularity_dimension is None:
        return 'undetermined_dimension_not_computed'
    require(type(singularity_dimension) is int and -1 <= singularity_dimension <= 7,'theta singularity dimension')
    if singularity_dimension > 4:
        return 'excluded_as_smooth_etale_Prym_by_Mumford'
    if singularity_dimension == 4:
        return 'cyclic_quartic_realization_requires_bielliptic_genus9_intermediate'
    return 'no_further_Mumford_restriction_beyond_nonhyperelliptic_nontrigonal_intermediate'


def reflection_matrix():
    m = [[Q(int(i == j)) for j in range(16)] for i in range(16)]
    for a,b in ((0,12),(1,13)):
        m[a][a] = m[b][b] = Q(0)
        m[a][b] = m[b][a] = Q(1)
    return m


@lru_cache(maxsize=1)
def exact_core():
    # The reflection is an actual descended old Eplus sign, not an arbitrary
    # unitary lattice isometry which might fail to commute with complex structure.
    T = gaussian_matrix()
    z = (Q(0),Q(0))
    old = [[(Q(int(i == j)*(-1 if i == 6 else 1)),Q(0)) for j in range(8)] for i in range(8)]
    new = [[(Q(int(i == j)),Q(0)) for j in range(8)] for i in range(8)]
    new[0][0] = new[6][6] = z
    new[0][6] = new[6][0] = (Q(1),Q(0))
    require(gmatrix_product(new,T) == gmatrix_product(T,old) and
        gdet(new) == (Q(-1),Q(0)),'actual elliptic reflection descent')
    real = reflection_matrix()
    rho = [[Q(0)]*16 for _ in range(16)]
    for k in range(8):
        rho[2*k][2*k+1],rho[2*k+1][2*k] = Q(-1),Q(1)
    for k in range(16):
        v = {(k,):Q(1)}
        require(full_pullback(real,full_pullback(real,v)) == v,'reflection square')
        require(full_pullback(rho,full_pullback(rho,v)) == scale(v,-1),'Gaussian square minus identity')
    r8,i8 = generators(8)
    for v in (r8,i8):
        require(full_pullback(real,v) == scale(v,-1),'reflection Weil sign')
    EX = {(2*k,2*k+1):Q(d) for k,d in enumerate(DS8[:6])}
    cube = wedge(wedge(EX,EX),EX)
    algebraic_control = f_push(wedge(cube,R_B))
    require(algebraic_control and full_pullback(real,algebraic_control) == scale(algebraic_control,-1) and
        not any(channels_new(algebraic_control)),'reflection anti-divisor control')
    # Weighted degree-three fibres exhaust possible branch multiplicities.
    fibre_cases = []
    for weights in ((3,),(1,2),(1,1,1)):
        count = 0
        for p in permutations(range(len(weights))):
            if all(p[p[i]] == i and weights[p[i]] == weights[i] for i in range(len(weights))):
                fixed_weight = sum(weights[i] for i in range(len(weights)) if p[i] == i)
                require(fixed_weight%2 == 1,'odd invariant fibre without fixed support')
                count += 1
        fibre_cases.append({'multiplicities':list(weights),'involutions_checked':count})
    require(sum(r['involutions_checked'] for r in fibre_cases) == 6,'weighted fibre completeness')
    require(hyperelliptic_elliptic_genus_bound(2) == 3 and 8 > 3 and
        trigonal_free_involution_obstruction(9) and not trigonal_free_involution_obstruction(4),
        'Jacobian genus and unique-trigonal thresholds')
    require(1+Q(2*2*2-2*2,2) == 3 and 1+Q(2*3*3-2*3-2*3,2) == 4,'surface adjunction controls')
    return {'actual_elliptic_reflection_constructed':True,'reflection_H1_minus_rank':2,
        'reflection_anti_full_H8_rank':2*comb(14,7),'reflection_anti_algebraic_divisor_control_nonzero':True,
        'reflection_anti_control_all_four_exceptional_channels_zero':True,
        'fixed_principal_Y2_Jacobian_presentation_excluded':True,
        'hypothetical_Jacobian_genus':8,'hyperelliptic_elliptic_degree':2,'hyperelliptic_genus_upper_bound':3,
        'hyperelliptic_genus9_smooth_etale_Prym_base_excluded':True,
        'trigonal_genus9_intermediate_cyclic_quartic_tower_excluded':True,
        'distinct_trigonal_pencil_genus_upper_bound':4,'weighted_odd_fibre_controls':fibre_cases,
        'minimum_genus9_intermediate_gonality_for_cyclic_realization':4,
        'actual_theta_singularity_dimension':None,
        'conditional_singularity_cases':{str(d):conditional_prym_gate(d) for d in (None,-1,0,3,4,5)}}


def validate_audit(c):
    require(c['schema'] == 'marici.hodge-y2-curve-audit.v1' and
        c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node'] == 'y2-jacobian-low-gonality-transplant' and c['verdict'] == 'rejected','Y2 curve identity')
    require(c['resolution_kind'] == 'polarized_Torelli_elliptic_degree_two_and_free_involution_low_gonality_exclusion',
        'Y2 curve resolution')
    require(c['geometry'] == {'fixed_principal_Y2':True,'complex_dimension':8,
        'Gaussian_automorphism_square':'minus_identity','elliptic_polarization_degree':2,
        'etale_double_cover_base_genus':9,'cyclic_quartic_base_genus':5,
        'free_intermediate_involution_required_for_trigonal_exclusion':True},'Y2 curve geometry scope')
    require(c['imports'] == {'strong_polarized_Torelli':'Milne 12.1(a,b)',
        'Mumford':'Prym Varieties I section 7(a,d)',
        'noncoprime_map_independence':'no nonconstant morphism P1 to an elliptic curve'},'Y2 curve theorem imports')
    require(c['scope_policy'] == dict.fromkeys(['all_smooth_etale_Prym_presentations_of_Y2_excluded',
        'all_isogenous_Jacobians_excluded','other_polarizations_excluded','ramified_Pryms_excluded',
        'singular_admissible_covers_excluded','genus5_base_excluded_by_this_argument',
        'trigonal_base_excluded_for_arbitrary_etale_double_Prym_without_free_involution',
        'theta_singularity_dimension_computed','all_cycles_reflection_invariant',
        'reflection_anti_invariance_is_exceptional_test','conditional_biellipticity_is_unconditional'],False),
        'Y2 curve exclusion promoted')
    require(set(c['boundary']) == {'Hodge_proved','Hodge_refuted','alpha_nonalgebraic_proved',
        'algebraic_representative_of_alpha_constructed','all_cycle_annihilation_proved',
        'global_witness_search_completed'} and all(v is False for v in c['boundary'].values()),'Y2 curve verdict promotion')


def source_paths():
    return {SNAPSHOT} | {r['path'] for r in load(SNAPSHOT)['files']}


def report():
    c = load(CONTRACT)
    validate_audit(c)
    validate_sources()
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-indecomposable-principal-model-v1.json',
        'Y2 model input binding')
    old = load(c['previous_receipt'])
    require(old == model_report() and old['candidate_id'] == c['candidate_id'] and
        old['principal_polarization_indecomposable'] and old['elliptic_axis_polarization_degrees'] == [2,3],
        'stale Y2 model input')
    sources = source_paths() | {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_indecomposable_principal_model.py',
        'research/voevodsky/checkers/check_hodge_eightfold_hodge_kernel.py'}
    return {'schema':'marici.hodge-y2-curve-audit-result.v1','passed':True,'candidate_id':c['candidate_id'],
        'node':c['node'],'verdict':'rejected',**exact_core(),
        'checks':dict.fromkeys(['fresh_polarized_Torelli_statement_and_sign_uniqueness',
            'Gaussian_square_minus_one_forces_hyperelliptic_hypothetical_Jacobian',
            'independent_degree_two_maps_to_P1_and_elliptic_curve_genus_bound_three',
            'actual_reflection_descent_and_nonzero_anti_divisor_control',
            'genus9_unique_trigonal_pencil_and_weighted_odd_fibre_fixed_point',
            'Mumford_hyperelliptic_exclusion_and_only_conditional_biellipticity'],True),
        **c['scope_policy'],**c['boundary'],'verification_level':c['trust_scope'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'source_sha256'},indent=2))
