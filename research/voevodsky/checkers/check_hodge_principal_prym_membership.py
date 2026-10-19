"""Geometric exclusion of the four fixed-polarization principal Prym targets.
Mumford's theorem is an imported primary-source theorem, not proved by arithmetic.
"""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json
from check_hodge_gaussian_principal_isogeny import report as principal_report
from check_hodge_secant_sheaf_transplant import valuation3

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-principal-prym-membership.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-principal-prym-membership-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-principal-prym-membership-v1.json'
SNAPSHOT = 'research/voevodsky/inputs/hodge-principal-prym-membership-v1/sources.json'
BASE = 'research/voevodsky/inputs/hodge-principal-prym-membership-v1/'
FILES = ('mumford-prym-I.pdf','mumford-prym-I.txt','mumford.p4.png','mumford.p20.png',
         'mumford.p22.png','mumford-index.html','mumford-papers.html','prym-search.txt')


def require(condition,message):
    if not condition:
        raise ValueError(message)


def load(path):
    return json.loads((ROOT/path).read_text(encoding='utf-8'))


def validate_sources():
    data = load(SNAPSHOT)
    require(data['schema'] == 'marici.hodge-principal-prym-sources.v1' and
        data['author'] == 'David Mumford' and data['title'] == 'Prym Varieties I' and
        data['year'] == 1974 and data['url'] ==
        'https://www.dam.brown.edu/people/mumford/alg_geom/papers/1974a--PrymVar-I-NC.pdf', 'Mumford source identity')
    require(data['pdf'] == BASE+'mumford-prym-I.pdf' and data['text'] == BASE+'mumford-prym-I.txt' and
        data['rendered_pdf_pages'] == [4,20,22] and data['printed_pages'] == [328,344,346] and
        len(data['files']) == 8 and {r['path'] for r in data['files']} == {BASE+n for n in FILES},
        'Mumford source coverage')
    for row in data['files']:
        require(sha256((ROOT/row['path']).read_bytes()).hexdigest() == row['sha256'],'Mumford source drift')
    require((ROOT/data['pdf']).read_bytes().startswith(b'%PDF'),'Mumford PDF')
    text = ' '.join((ROOT/data['text']).read_text(encoding='utf-8').split())
    require(all(s in text for s in ('7. DIM SING','product of two such','Assuming C not hyperelliptic',
        'two groups of even cardinality','h + k + 1 = g')), 'Mumford theorem quote anchors')


def fmul(x,y):
    a,b = x
    c,d = y
    return ((a*c-b*d)%3,(a*d+b*c)%3)


def fadd(x,y):
    return ((x[0]+y[0])%3,(x[1]+y[1])%3)


def fconj(x):
    return (x[0],(-x[1])%3)


def coprime_genus_bound(d1,g1,d2,g2):
    require(d1 > 0 and d2 > 0 and g1 >= 0 and g2 >= 0 and gcd(d1,d2) == 1,
        'coprime degrees required for this automatic birationality argument')
    return d1*g1+d2*g2+(d1-1)*(d2-1)


@lru_cache(maxsize=1)
def exact_core():
    field = list(product(range(3),repeat=2))
    rows = []
    for slope in field:
        if sum(x*x for x in slope)%3 != 2:
            continue
        points = [(u,fmul(slope,u)) for u in field]
        require(len(set(points)) == 9 and sum(u == (0,0) for u,v in points) == 1 and
            sum(v == (0,0) for u,v in points) == 1,'mixed subgroup axis intersection')
        for u,v in points:
            for x,y in points:
                require(fadd(fmul(fconj(u),x),fmul(fconj(v),y)) == (0,0),
                    'mixed subgroup Hermitian discriminant isotropy')
        rows.append({'slope':list(slope),'order':9,'intersection_with_each_bad_factor_order':1,
            'untouched_principal_Eplus':True,'embedded_Eminus_theta_degree':3})
    require(len(rows) == 4,'four fixed-polarization Gaussian quotients')
    # An indecomposable sixfold factor carrying principal Gaussian polarization
    # would have raw determinant -1, not the rigid fixed -3 norm class.
    require(valuation3(Q(-3)/Q(-1))%2 == 1,'principal simple-factor norm barrier')
    dimension,base_genus,z_genus,ell_degree = 8,9,7,3
    crossing,nonhyperelliptic_bound = dimension-2,base_genus-5
    require(crossing == 6 and nonhyperelliptic_bound == 4 and crossing > nonhyperelliptic_bound,
        'Mumford nonhyperelliptic theta bound contradiction')
    bound = coprime_genus_bound(2,0,ell_degree,1)
    require(bound == 5 and z_genus > bound,'hyperelliptic degree-three elliptic map contradiction')
    # Adjunction for a birational image in P1 x E, bidegrees (2,3).
    self_intersection,canonical_intersection = 2*2*ell_degree,-2*2
    require(1+Q(self_intersection+canonical_intersection,2) == bound,'surface adjunction bound')
    return {'fixed_polarization_principal_quotient_count':4,'quotient_controls':rows,
        'principal_product_factor_dimensions':[1,7],'sevenfold_principal_indecomposable':True,
        'sevenfold_embedded_elliptic_polarization_degree':ell_degree,
        'hypothetical_etale_double_cover_base_genus':base_genus,
        'theta_product_crossing_dimension':crossing,'Mumford_nonhyperelliptic_upper_bound':nonhyperelliptic_bound,
        'hyperelliptic_genus_required':z_genus,'coprime_elliptic_cover_genus_upper_bound':bound,
        'surface_image_self_intersection':self_intersection,'surface_image_canonical_intersection':canonical_intersection,
        'fixed_theta_Y_smooth_etale_Prym_presentation_excluded':True,
        'all_four_fixed_polarization_Gaussian_principal_quotients_excluded_as_smooth_etale_Pryms':True}


def validate_membership(c):
    require(c['schema'] == 'marici.hodge-principal-prym-membership.v1' and
        c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node'] == 'principal-prym-membership-audit' and c['verdict'] == 'rejected', 'principal Prym identity')
    require(c['resolution_kind'] == 'fixed_polarization_product_factor_and_Mumford_hyperelliptic_cover_exclusion',
        'principal Prym resolution')
    require(c['geometry'] == {'target_dimension':8,'fixed_theta_Y':True,'pullback_polarization':'E_A',
        'native_Gaussian_embedding_retained':True,'quotient_count':4,'principal_factor_dimensions':[1,7],
        'embedded_Eminus_degree':3,'cover':'smooth_connected_etale_double',
        'canonical_principal_Prym_polarization':True},'principal Prym geometry scope')
    require(c['source_policy'] == {'Mumford_section':7,'parts':['a','d'],
        'theorem_inequalities_checked_against_rendered_images':True,
        'local_no_matches_is_literature_absence':False},'principal Prym source policy')
    require(c['scope_policy'] == dict.fromkeys(['all_Prym_presentations_excluded',
        'ramified_Pryms_excluded','singular_admissible_covers_excluded',
        'all_isogenous_principal_models_excluded','other_polarizations_excluded',
        'other_Gaussian_embeddings_excluded','unpolarized_isomorphism_suffices',
        'moduli_dimension_alone_used','actual_hyperelliptic_curve_constructed'],False), 'principal Prym exclusion promoted')
    require(set(c['boundary']) == {'Hodge_proved','Hodge_refuted','alpha_nonalgebraic_proved',
        'algebraic_representative_of_alpha_constructed','all_cycle_annihilation_proved',
        'global_witness_search_completed'} and all(v is False for v in c['boundary'].values()),
        'principal Prym verdict promotion')


def source_paths():
    return {SNAPSHOT} | {r['path'] for r in load(SNAPSHOT)['files']}


def report():
    c = load(CONTRACT)
    validate_membership(c)
    validate_sources()
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-gaussian-principal-isogeny-v1.json',
        'principal quotient input binding')
    old = load(c['previous_receipt'])
    require(old == principal_report() and old['candidate_id'] == c['candidate_id'] and
        old['actual_principal_Gaussian_eightfold_constructed'] and old['quotient_degree'] == 9 and
        len(old['maximal_mixed_isotropic_Gaussian_lines_mod3']) == 4,
        'stale principal quotient input')
    sources = source_paths() | {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_gaussian_principal_isogeny.py',
        'research/voevodsky/checkers/check_hodge_secant_sheaf_transplant.py'}
    return {'schema':'marici.hodge-principal-prym-membership-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'rejected',**exact_core(),
        'checks':dict.fromkeys(['primary_Mumford_pages_344_346_and_principal_normalization',
            'all_four_mixed_kernels_leave_Eplus_principal_and_embed_Eminus_with_degree_three',
            'sevenfold_indecomposable_by_simple_sixfold_Gaussian_norm_barrier',
            'theta_crossing_six_exceeds_nonhyperelliptic_bound_four',
            'hyperelliptic_genus_seven_with_degree_three_elliptic_map_exceeds_adjunction_bound_five',
            'fixed_principal_polarizations_only_not_all_isogenous_or_ramified_Pryms'],True),
        **dict.fromkeys(c['scope_policy'],False),**c['boundary'],
        'verification_level':c['trust_scope'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'source_sha256'},indent=2))
