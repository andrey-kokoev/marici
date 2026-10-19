"""Mixed factors in the commuting-lift stratum fail the fixed sixfold invariant."""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import json
from check_hodge_bielliptic_lift_audit import report as lift_report, norm, pullback
from check_hodge_secant_sheaf_transplant import pfaffian, valuation3

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-commuting-prym-audit.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-commuting-prym-audit-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-commuting-prym-audit-v1.json'
BASE = 'research/voevodsky/inputs/hodge-commuting-prym-audit-v1/'
SNAPSHOT = BASE+'sources.json'
PDF = 'research/voevodsky/inputs/hodge-principal-prym-membership-v1/mumford-prym-I.pdf'
POLICY = ['bielliptic_branch_is_unconditional','entire_commuting_stratum_excluded',
    'remaining_pulled_roots_are_target_realizations','nonlifting_half_excluded',
    'all_Prym_presentations_excluded','actual_cover_matching_Y2_constructed',
    'theta_dimension_computed','root_counts_are_unmarked_moduli_counts',
    'ramified_sixfold_principal_polarization_claimed','actual_target_reflection_identified_with_curve_lift',
    'ramified_top_covers_included','Hodge_proved','Hodge_refuted','alpha_nonalgebraic_proved',
    'algebraic_representative_of_alpha_constructed','all_cycle_annihilation_proved','global_witness_search_completed']


def require(condition,message):
    if not condition:
        raise ValueError(message)


def load(p):
    return json.loads((ROOT/p).read_text(encoding='utf-8'))


def source_paths():
    return {SNAPSHOT,PDF} | {BASE+f'mumford.p{i}.{ext}' for i in (7,8,9) for ext in ('txt','png')}


def validate_sources():
    d = load(SNAPSHOT)
    require(d['schema'] == 'marici.hodge-commuting-prym-sources.v1' and
        d['author'] == 'David Mumford' and d['title'] == 'Prym Varieties I' and
        d['url'] == 'https://www.dam.brown.edu/people/mumford/alg_geom/papers/1974a--PrymVar-I-NC.pdf' and
        d['rendered_pdf_pages'] == [7,8,9] and d['printed_pages'] == [331,332,333], 'ramified Prym source identity')
    require({r['path'] for r in d['files']} == source_paths()-{SNAPSHOT} and len(d['files']) == 7,'ramified Prym source coverage')
    for r in d['files']:
        require(sha256((ROOT/r['path']).read_bytes()).hexdigest() == r['sha256'],'ramified Prym source drift')
    text = ' '.join((ROOT/(BASE+'mumford.p8.txt')).read_text(encoding='utf-8').split())
    require(all(t in text for t in ('Corollary 1.', 'symplectic injection', 'polarization of P')), 'ramified Prym theorem anchors')


def quotient_case(a):
    require(type(a) is int and a in (0,2,4,6,8),'even inertia count required')
    g1,g2 = 9-a,1+a
    require(32 == 2*(2*g1-2)+4*a and 32 == 2*(2*g2-2)+4*(8-a),'quotient Hurwitz arithmetic')
    dims = sorted((g1-1,g2-1))
    kind = 'elliptic_four_isogeny_pullback_remains' if dims == [0,8] else (
        'excluded_by_simple_sixfold_dimension' if dims == [4,4] else 'excluded_by_ramified_sixfold_inert_three_parity')
    return {'inertia_sigma_branch_count':a,'quotient_genera':[g1,g2],
        'Prym_factor_dimensions':dims,'result':kind}


@lru_cache(maxsize=1)
def exact_core():
    cases = [quotient_case(a) for a in (0,2,4,6,8)]
    # Restricted Jacobian polarization of a ramified D7->E1 cover:
    # Mumford ker(lambda)=E[2], hence type (1,1,1,1,1,2), NOT principal.
    diagonal = [1,1,1,-1,-1,-2]
    e = [[Q(0)]*12 for _ in range(12)]
    for i,d in enumerate(diagonal):
        e[i][i+6],e[i+6][i] = Q(d),Q(-d)
    require(abs(pfaffian(e)) == 2 and valuation3(Q(3,2)) == 1,'ramified determinant certificate')
    require(all((valuation3(Q(2)*Q(3)**(6*k))%2) == 0 for k in range(-3,4)), 'even rank polarization scaling parity')
    # Elliptic [4] has four roots of a fixed nonzero zeta, and pullback is injective.
    zeta = (2,0)
    m = [(a,b) for a in range(4) for b in range(4) if (2*a%4,2*b%4) == zeta]
    pulled = {pullback(v) for v in m}
    require(len(m) == len(pulled) == 4 and all(norm(v) == zeta for v in pulled),'scalar branch four pulled roots')
    require(len({min(v,tuple(-x%4 for x in v)) for v in pulled}) == 2,'pulled inverse pairs')
    return {'conditional_on_bielliptic_intermediate':True,'quotient_cases':cases,
        'mixed_commuting_factor_presentations_excluded_up_to_A_isogeny':True,
        'ramified_sixfold_cover_genera':[7,1],'ramified_sixfold_branch_count':12,
        'ramified_sixfold_polarization_type':[1,1,1,1,1,2],
        'ramified_sixfold_polarization_kernel_order':4,'ramified_sixfold_Hermitian_determinant_absolute_value':2,
        'ramified_sixfold_v3_parity':0,'fixed_X_v3_parity':1,
        'commuting_root_labels_before':256,'mixed_commuting_root_labels_excluded':252,
        'remaining_commuting_pulled_root_labels':4,'remaining_commuting_inverse_pairs':2,
        'pulled_formal_root_labels':[list(v) for v in sorted(pulled)],
        'nonlifting_root_labels_not_tested_here':512,
        'conditional_total_remaining_root_labels':516,'conditional_total_remaining_inverse_pairs':258,
        'actual_theta_singularity_dimension':None,'actual_matching_root_label':None}


def validate_audit(c):
    require(c['schema'] == 'marici.hodge-commuting-prym-audit.v1' and
        c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node'] == 'commuting-prym-factor-transplant' and c['verdict'] == 'rejected','commuting Prym identity')
    require(c['resolution_kind'] == 'commuting_quotient_genus_ramified_polarization_and_inert_three_parity_exclusion','commuting Prym resolution')
    require(c['geometry'] == {'conditional_intermediate_genus':9,'bottom_genus':5,
        'norm_L':'zeta','top_cover':'connected_etale_cyclic_quartic','lift_commutes_with_rho':True,
        'lift_is_involution':True,'inertia_count_even':True,'fixed_X_simple':True,
        'fixed_X_End0':'Q(i)','fixed_X_rational_NS_rank':1},'commuting Prym geometry scope')
    require(c['source_policy'] == {'Mumford_section':3,'corollary':1,'printed_page':332,
        'polarization':'restriction_of_Jacobian_theta_not_principal_halving'},'commuting Prym source scope')
    require(c['level_data'] == {'commuting_roots_before':256,'mixed_roots_excluded':252,
        'pulled_roots_remaining':4,'all_conditional_roots_remaining':516,
        'all_conditional_inverse_pairs_remaining':258},'commuting Prym census scope')
    require(set(c['scope_policy']) == set(POLICY) and all(v is False for v in c['scope_policy'].values()),'commuting Prym promotion')


def report():
    c = load(CONTRACT.relative_to(ROOT).as_posix())
    validate_audit(c)
    validate_sources()
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-bielliptic-lift-audit-v1.json','commuting Prym predecessor binding')
    old = load(c['previous_receipt'])
    require(old == lift_report() and old['commuting_lift_root_labels'] == 256 and
        old['nonlifting_root_labels'] == 512 and old['actual_theta_singularity_dimension'] is None,'stale lift audit')
    sources = source_paths() | {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_bielliptic_lift_audit.py',
        'research/voevodsky/checkers/check_hodge_secant_sheaf_transplant.py'}
    return {'schema':'marici.hodge-commuting-prym-audit-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'rejected',**exact_core(),
        'checks':dict.fromkeys(['primary_ramified_polarization_kernel_not_etale_principal_normalization',
            'abelian_inertia_relation_forces_even_branch_split',
            'quotient_genus_and_actual_Prym_factor_isogenies',
            'fourfold_pair_cannot_contain_simple_X6',
            'six_plus_two_case_fails_inert_three_parity_even_after_K_conjugation',
            'scalar_lift_cases_exactly_elliptic_four_isogeny_pullbacks',
            'conditional_root_reduction_not_actual_target_geometry'],True),
        **c['scope_policy'],'verification_level':c['trust_scope'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'source_sha256'},indent=2))
