"""Retained higher-Chern theorem applicability, not an all-sheaf impossibility claim."""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import json
from check_hodge_weil_projector import cmul
from check_hodge_middle_hodge_kernel import report as kernel_report

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-secant-sheaf-transplant.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-secant-sheaf-transplant-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-secant-sheaf-transplant-v1.json'
SNAPSHOT = 'research/voevodsky/inputs/hodge-secant-transplant-v1/sources.json'


def require(condition,message):
    if not condition:
        raise ValueError(message)


def load(name):
    return json.loads((ROOT/name).read_text(encoding='utf-8'))


def norm(z):
    return z[0]*z[0]+z[1]*z[1]


def conjugate(z):
    return z[0],-z[1]


def pfaffian(a):
    """Usual alternating Pfaffian; paper's normalized six-by-six Pf is its negative."""
    if not a:
        return Q(1)
    result = Q(0)
    for j in range(1,len(a)):
        indices = [k for k in range(len(a)) if k not in (0,j)]
        minor = [[a[r][s] for s in indices] for r in indices]
        result += (-1)**(j+1)*a[0][j]*pfaffian(minor)
    return result


def igusa_rank_two(d):
    y = [[Q(0)]*6 for _ in range(6)]
    for j in range(3):
        y[j][j+3],y[j+3][j] = 2*Q(d),-2*Q(d)
    return -2*pfaffian(y)


def valuation3(x):
    x = Q(x)
    require(x != 0,'valuation of zero')
    def power(n):
        n,exponent = abs(n),0
        while n%3 == 0:
            n //= 3
            exponent += 1
        return exponent
    return power(x.numerator)-power(x.denominator)


def gadd(a,b):
    return a[0]+b[0],a[1]+b[1]


def gdet(matrix):
    a = [[tuple(map(Q,x)) for x in row] for row in matrix]
    det = (Q(1),Q(0))
    for k in range(len(a)):
        pivot = next((i for i in range(k,len(a)) if a[i][k] != (0,0)),None)
        if pivot is None:
            return Q(0),Q(0)
        if pivot != k:
            a[k],a[pivot] = a[pivot],a[k]
            det = (-det[0],-det[1])
        value = a[k][k]
        det = cmul(det,value)
        inverse = tuple(x/norm(value) for x in conjugate(value))
        for i in range(k+1,len(a)):
            factor = cmul(a[i][k],inverse)
            for j in range(k,len(a)):
                product = cmul(factor,a[k][j])
                a[i][j] = gadd(a[i][j],(-product[0],-product[1]))
    return det


def gmatrix_product(a,b):
    return [[tuple(sum(cmul(a[i][k],b[k][j])[part] for k in range(len(b))) for part in (0,1))
             for j in range(len(b[0]))] for i in range(len(a))]


def validate_sources(c):
    require(c['source_snapshot'] == SNAPSHOT,'source snapshot binding')
    data = load(SNAPSHOT)
    require(data['schema'] == 'marici.hodge-secant-source-snapshot.v1' and
            data['pdf'] == 'research/voevodsky/inputs/hodge-literature-v1/markman-2502.03415v2.pdf','retained PDF identity')
    require(sha256((ROOT/data['pdf']).read_bytes()).hexdigest() == data['pdf_sha256'],'retained PDF drift')
    pages = {x['pdf_page']:x for x in data['pages']}
    require(set(pages) == {7,9,23,24,88,89,90,91} and len(data['pages']) == 8,'page inventory')
    for p,record in pages.items():
        expected = ('research/voevodsky/inputs/hodge-literature-v1/markman-2502.03415v2.p9.txt' if p == 9 else
                    f'research/voevodsky/inputs/hodge-secant-transplant-v1/markman.p{p}.txt')
        require(record['path'] == expected and sha256((ROOT/expected).read_bytes()).hexdigest() == record['sha256'],'retained page drift')
    require([r['page'] for r in c['citations']] == [7,9,23,24,88,90,91],'citation inventory')
    for quote in c['citations']:
        text = ' '.join((ROOT/pages[quote['page']]['path']).read_text(encoding='utf-8').split())
        require(quote['quote'] and quote['quote'] in text,'source quote absent on page '+str(quote['page']))


@lru_cache(maxsize=1)
def exact_core():
    # Fixed rational mathematics only; no mutable source reads in this cache.
    norms = 0
    for a in range(-4,5):
        for b in range(-4,5):
            if a == b == 0:
                continue
            for denominator in (1,2,3,5):
                n = norm((Q(a,denominator),Q(b,denominator)))
                require(valuation3(n)%2 == 0 and valuation3(3*n)%2 == 1,'local Gaussian norm parity')
                norms += 1
    controls = []
    for q in (Q(1,3),Q(1,2),Q(1),Q(2),Q(3),Q(5,2)):
        h = [[(q*d if i == j else Q(0),Q(0)) for j in range(6)] for i,d in enumerate((1,1,1,-1,-1,-3))]
        for z in ((1,1),(2,1),(1,2),(-1,1)):
            S = [[(Q(i == j),Q(0)) for j in range(6)] for i in range(6)]
            S[0][0],S[0][1],S[3][5] = tuple(map(Q,z)),(Q(1),Q(1)),(Q(1,2),Q(-2))
            adjoint = [[conjugate(S[j][i]) for j in range(6)] for i in range(6)]
            transformed = gmatrix_product(gmatrix_product(adjoint,h),S)
            determinant = gdet(transformed)
            detS = gdet(S)
            require(determinant == (-3*q**6*norm(detS),0),'Gaussian basis determinant law')
            require(valuation3(-determinant[0])%2 == 1,'repolarization/basis mismatch lost')
            controls.append({'q':str(q),'basis_determinant':[str(x) for x in detS],
                             'new_Hermitian_determinant':str(determinant[0])})
    # d in this source controls the field, not the Hermitian discriminant.
    igusa = [{'d':d,'reflexive_secant_rank':8*d,'Igusa_rank_two_source_value':int(igusa_rank_two(d)),
              'same_field_as_Qi':True,'theorem_discriminant':-1} for d in (4,9,16)]
    require([x['Igusa_rank_two_source_value'] for x in igusa] == [1024,11664,65536],'Igusa normalization')
    return {'selected_discriminant':-3,'required_discriminant':-1,'ratio':3,
            'v3_ratio':1,'Gaussian_norm_parity_control_count':norms,
            'polarization_and_Gaussian_basis_control_count':len(controls),'controls':controls,
            'same_field_Igusa_parameter_controls':igusa,
            'retained_split_theorem_excluded_on_all_repolarized_Qi_isogeny_models':True}


def validate_transplant(c):
    require(c['schema'] == 'marici.hodge-secant-sheaf-transplant.v1' and
            c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1','transplant candidate binding')
    require(c['node'] == 'secant-sheaf-transplant' and c['verdict'] == 'rejected' and
            c['resolution_kind'] == 'fixed_isogeny_class_discriminant_rigidity_blocks_retained_split_secant_theorem','transplant rejection binding')
    require(c['hypotheses'] == {'End0':'Q(i)','NS_Q_rank':1,'complex_dimension':6,
            'selected_determinant':-3,'required_determinant_representative':-1},'transplant hypothesis binding')
    require(c['rigidity']['ratio_to_required'] == 3,'wrong norm obstruction')
    require(len(c['boundary']) == 8 and all(x is False for x in c['boundary'].values()),'scoped transplant failure promoted')


def source_paths():
    data = load(SNAPSHOT)
    return {SNAPSHOT,data['pdf']} | {p['path'] for p in data['pages']}


def report():
    c = load(CONTRACT.relative_to(ROOT))
    validate_transplant(c)
    validate_sources(c)
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-middle-hodge-kernel-v1.json','kernel source binding')
    previous = load(c['previous_receipt'])
    require(previous == kernel_report() and previous['candidate_id'] == c['candidate_id'],'stale Hodge-kernel source')
    endo = load('research/voevodsky/results/hodge-tautological-witness-search-v1.json')
    candidate = load('research/voevodsky/results/hodge-explicit-sixfold-candidate-v1.json')
    require(endo['End0_dimension_from_written_genericity_proof'] == 2 and
            candidate['rational_Neron_Severi_rank_from_written_genericity_proof'] == 1,'rigidity inputs unavailable')
    checks = dict.fromkeys(['retained_secant_sheaf_and_Igusa_pages_bound_to_fixed_PDF',
        'published_positive_kappa_route_retained_with_its_split_discriminant_hypothesis',
        'rank_one_NS_makes_every_polarization_change_a_norm_multiplier',
        'End0_Qi_excludes_alternative_quadratic_fields_and_extra_embeddings',
        'arbitrary_isogeny_model_reduces_to_same_polarization_and_K_action',
        'exact_Gaussian_basis_and_local_norm_parity_controls',
        'Igusa_field_parameter_not_confused_with_Hermitian_discriminant',
        'special_nonsplit_algebraic_control_retains_no_nonalgebraicity_inference',
        'unrestricted_higher_Chern_and_witness_search_remain_open'],True)
    sources = source_paths() | {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/results/hodge-tautological-witness-search-v1.json',
        'research/voevodsky/results/hodge-explicit-sixfold-candidate-v1.json',
        'research/voevodsky/checkers/check_hodge_middle_hodge_kernel.py',
        'research/voevodsky/checkers/check_hodge_weil_projector.py'}
    return {'schema':'marici.hodge-secant-sheaf-transplant-result.v1','passed':True,'checks':checks,
            'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'rejected',**exact_core(),
            'retained_theorem_applicable_to_fixed_isogeny_class':False,
            'algebraic_representative_of_alpha_constructed':False,'alpha_nonalgebraic_proved':False,
            'all_cycle_annihilation_proved':False,'all_sheaf_routes_excluded':False,
            'global_witness_search_completed':False,'Hodge_proved':False,'Hodge_refuted':False,
            'verification_level':c['trust_scope'],
            'source_sha256':{name:sha256((ROOT/name).read_bytes()).hexdigest() for name in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_sha256','controls')},indent=2))
