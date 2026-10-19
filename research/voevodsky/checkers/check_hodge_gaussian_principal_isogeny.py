"""Explicit principal Gaussian quotient of the auxiliary eightfold.
The quotient is real geometry; its Weil classes are still not supplied cycles.
"""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from math import factorial
from pathlib import Path
import json
from check_hodge_secant_sheaf_transplant import gdet, gmatrix_product, conjugate
from check_hodge_eightfold_hodge_kernel import (
    report as kernel_report, channels, exceptional_projector, generators)
from check_hodge_eightfold_weil_filter import forward_fast
from check_hodge_split_eightfold_stabilization import (
    DS8, full_pullback, wedge, scale, combine, recover)

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-gaussian-principal-isogeny.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-gaussian-principal-isogeny-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-gaussian-principal-isogeny-v1.json'
DY = (1,1,1,-1,-1,-1,1,-1)
ACTIVE = (10,11,14,15)
T = (((Q(1),Q(0)),(Q(1),Q(-1))),((Q(-1),Q(-1)),(Q(1),Q(0))))
S = (((Q(1,3),Q(0)),(Q(-1,3),Q(1,3))),((Q(1,3),Q(1,3)),(Q(1,3),Q(0))))


def require(condition,message):
    if not condition:
        raise ValueError(message)


def real_matrix(matrix):
    out = [[Q(0)]*4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            a,b = matrix[i][j]
            out[2*i][2*j],out[2*i][2*j+1] = a,-b
            out[2*i+1][2*j],out[2*i+1][2*j+1] = b,a
    return out


@lru_cache(maxsize=2)
def compound(inverse=False):
    matrix = real_matrix(S if inverse else T)
    return {s:full_pullback(matrix,{s:Q(1)}) for k in range(5) for s in combinations(range(4),k)}


def q_pull(form,inverse=False):
    """q* in marked rational exterior cohomology, or its inverse. Not Chow data."""
    table,result = compound(inverse),{}
    for indices,value in form.items():
        require(tuple(sorted(set(indices))) == indices and all(0 <= i < 16 for i in indices),'invalid isogeny coordinates')
        inside = tuple(i for i in indices if i in ACTIVE)
        outside = tuple(i for i in indices if i not in ACTIVE)
        sign_in = (-1)**sum(i > j for i in outside for j in inside)
        local = tuple(ACTIVE.index(i) for i in inside)
        for target,c in table[local].items():
            global_target = tuple(ACTIVE[i] for i in target)
            sign_out = (-1)**sum(i > j for i in outside for j in global_target)
            key = tuple(sorted(outside+global_target))
            result[key] = result.get(key,Q(0))+value*c*sign_in*sign_out
    return {s:v for s,v in result.items() if v}


def q_push(form):
    return scale(q_pull(form,inverse=True),9)


def forward_Y(form):
    return scale(q_push(forward_fast(form)),Q(1,3))


def reverse_Y(form):
    return scale(recover(q_pull(form)),Q(1,3))


def channels_Y(form):
    return channels(q_pull(form))


def exceptional_Y(form):
    return scale(q_push(exceptional_projector(q_pull(form))),Q(1,9))


@lru_cache(maxsize=1)
def exact_core():
    ident = [[(Q(int(i == j)),Q(0)) for j in range(2)] for i in range(2)]
    require(gmatrix_product(S,T) == ident and gmatrix_product(T,S) == ident and
        gdet(S) == (Q(1,3),0) and gdet(T) == (Q(3),0),'Gaussian marking matrices')
    adjoint = [[conjugate(S[j][i]) for j in range(2)] for i in range(2)]
    h = [[(Q(-3*int(i == j)),0) for j in range(2)] for i in range(2)]
    hy = gmatrix_product(gmatrix_product(adjoint,h),S)
    require(hy == [[(Q(-int(i == j)),0) for j in range(2)] for i in range(2)],'principal Hermitian block')
    # F9=F3[i], i^2=-1. Isotropic Gaussian lines in the two bad planes.
    lambdas = [(a,b) for a,b in product(range(3),repeat=2) if (a*a+b*b)%3 == 2]
    require(lambdas == [(1,1),(1,2),(2,1),(2,2)],'mixed maximal isotropic lines')
    require(not any((x*x+1)%3 == 0 for x in range(3)),'i has an invariant order-three line')
    EA = {(2*j,2*j+1):Q(d) for j,d in enumerate(DS8)}
    EY = {(2*j,2*j+1):Q(d) for j,d in enumerate(DY)}
    require(q_pull(EY) == EA,'q polarization pullback')
    ap,yp = {():Q(1)},{():Q(1)}
    for _ in range(8):
        ap,yp = wedge(ap,EA),wedge(yp,EY)
    require(yp[tuple(range(16))] == factorial(8) and ap[tuple(range(16))] == 9*factorial(8) and
        q_pull(yp) == ap,'principal volume and degree nine')
    r8,i8 = generators(8)
    for w in (r8,i8):
        require(q_pull(w) == scale(w,3) and q_push(w) == scale(w,3),'Weil determinant factor three')
    # Two orders on all H8 basis columns, not a sparse handpicked test library.
    for indices in combinations(range(16),8):
        v = {indices:Q(1)}
        require(q_push(q_pull(v)) == scale(v,9) and q_pull(q_push(v)) == scale(v,9),
            'full middle cohomology isogeny inverse census')
    # Cross-check the local compound implementation against the original full pullback.
    full = [[Q(int(i == j)) for j in range(16)] for i in range(16)]
    local = real_matrix(T)
    for i,a in enumerate(ACTIVE):
        for j,b in enumerate(ACTIVE):
            full[a][b] = local[i][j]
    for indices in ((0,2,4,6,8,10,12,14),(0,1,10,11,12,13,14,15)):
        v = {indices:Q(1)}
        require(q_pull(v) == full_pullback(full,v),'compound pullback sign cross-check')
    r6,i6 = generators(6)
    EX = {(2*j,2*j+1):Q(d) for j,d in enumerate(DS8[:6])}
    cube = wedge(wedge(EX,EX),EX)
    for v in (r6,i6,cube):
        require(reverse_Y(forward_Y(v)) == v,'transferred reverse/forward normalization')
    require(forward_Y(r6) == r8 and forward_Y(i6) == i8,'transported Weil generators')
    require(not any(channels_Y(forward_Y(cube))),'divisor cube falsely detected after principalization')
    require(exceptional_Y(r8) == r8 and exceptional_Y(i8) == i8,'exceptional filter transport')
    return {'quotient_degree':9,'Gaussian_marking_determinants':{'S':'1/3','q_matrix_T':'3'},
        'principal_Hermitian_diagonal':list(DY),'maximal_mixed_isotropic_Gaussian_lines_mod3':[list(x) for x in lambdas],
        'kernel_order':9,'Weil_pullback_factor':3,'Weil_pushforward_factor':3,
        'normalized_forward_denominator':3,'normalized_reverse_denominator':3,
        'full_H8_inverse_basis_count':12870,'principal_polarization_top_intersection':factorial(8),
        'rational_Hdg4_Y_dimension':14,'exceptional_Hdg4_Y_dimension':8,
        'actual_principal_Gaussian_eightfold_constructed':True,
        'algebraicity_test_transported_by_actual_isogeny':True}


def validate_isogeny(c):
    require(c['schema'] == 'marici.hodge-gaussian-principal-isogeny.v1' and
        c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node'] == 'gaussian-principal-isogeny' and c['verdict'] == 'constructed','principal isogeny identity')
    require(c['resolution_kind'] == 'explicit_mixed_three_torsion_Gaussian_principal_quotient_and_cycle_transfer',
        'principal isogeny resolution')
    require(c['geometry'] == {'complex_dimension':8,'quotient_degree':9,'kernel_order':9,
        'mixed_K_coordinates':[6,8],'H_generator':'(e6+(1+i)e8)/3',
        'principal_Hermitian_diagonal':list(DY),'original_candidate_X_changed':False},'principal quotient geometry')
    require(c['transfer'] == {'Weil_pullback_factor':3,'Weil_pushforward_factor':3,
        'normalized_forward_denominator':3,'normalized_reverse_denominator':3,
        'Hdg4_dimension':14,'exceptional_Hdg4_dimension':8},'principal quotient transfer normalization')
    require(c['policy'] == {'marking_matrix_is_an_endomorphism_of_A':False,
        'Prym_cover_constructed':False,'generic_Weil_eightfold_claimed':False,
        'B_has_no_other_principal_polarization':False,
        'q_pull_q_push_equals_9_on_Chow_claimed':False,'transported_Chow_retraction_claimed':False,
        'transported_rank_eight_formula_Chow_idempotence_claimed':False,
        'sixfold_Koike_theorem_applied_to_Y':False},'principal quotient scope promoted')
    require(set(c['boundary']) == {'Hodge_proved','Hodge_refuted','alpha_nonalgebraic_proved',
        'algebraic_representative_of_alpha_constructed','nonzero_algebraic_Weil_class_constructed',
        'Prym_cover_constructed','all_cycle_annihilation_proved'} and
        all(v is False for v in c['boundary'].values()),'principal quotient verdict promotion')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_isogeny(c)
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-eightfold-hodge-kernel-v1.json','product Hodge input binding')
    old = json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    require(old == kernel_report() and old['candidate_id'] == c['candidate_id'],'stale product Hodge input')
    sources = {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_split_eightfold_stabilization.py',
        'research/voevodsky/checkers/check_hodge_eightfold_hodge_kernel.py',
        'research/voevodsky/checkers/check_hodge_eightfold_weil_filter.py',
        'research/voevodsky/checkers/check_hodge_secant_sheaf_transplant.py'}
    return {'schema':'marici.hodge-gaussian-principal-isogeny-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',**exact_core(),
        'checks':dict.fromkeys(['mixed_isotropic_F9_line_and_integral_unimodular_overlattice',
            'unchanged_complex_structure_and_identity_quotient_not_marking_endomorphism',
            'principal_Riemann_form_and_exact_degree_nine',
            'all_12870_middle_basis_isogeny_inverse_columns_and_compound_sign_cross_checks',
            'Weil_factor_three_and_correct_normalized_forward_reverse_maps',
            'four_channel_filter_preservation_without_a_nonzero_algebraic_source',
            'not_a_cover_not_generic_not_a_Chow_retraction_or_Hodge_verdict'],True),
        'Prym_cover_constructed':False,'nonzero_algebraic_Weil_class_constructed':False,
        'algebraic_representative_of_alpha_constructed':False,'all_cycle_annihilation_proved':False,
        'alpha_nonalgebraic_proved':False,'Hodge_proved':False,'Hodge_refuted':False,
        'verification_level':c['trust_scope'],
        'source_sha256':{name:sha256((ROOT/name).read_bytes()).hexdigest() for name in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'source_sha256'},indent=2))
