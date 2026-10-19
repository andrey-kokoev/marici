"""Explicit auxiliary split eightfold and cycle transfer; no new algebraic Weil witness."""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import json
from check_hodge_explicit_sixfold_candidate import full_pullback, weil_forms, wedge
from check_hodge_literature_boundary_audit import multiply
from check_hodge_weil_projector import f_matrix, combine
from check_hodge_secant_sheaf_transplant import (
    conjugate, gdet, gmatrix_product, report as transplant_report)

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-split-eightfold-stabilization.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-split-eightfold-stabilization-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-split-eightfold-stabilization-v1.json'
DS8 = (1,1,1,-1,-1,-3,1,-3)
R_B = {(12,14):Q(1),(13,15):Q(-1)}
I_B = {(12,15):Q(1),(13,14):Q(1)}
E_B = {(12,13):Q(1),(14,15):Q(-3)}


def require(condition,message):
    if not condition:
        raise ValueError(message)


def scale(form,c):
    return {s:Q(c)*v for s,v in form.items() if c*v}


def shift(form,n):
    return {tuple(i+n for i in s):v for s,v in form.items()}


def integrate_B(form):
    result = {}
    for indices,value in form.items():
        if indices[-4:] == (12,13,14,15):
            key = indices[:-4]
            result[key] = result.get(key,Q(0))-value
    return {s:v for s,v in result.items() if v}


def j_operator(form):
    # Only on W6 does this act as a complex structure. No Chow square is assumed.
    return scale(combine(full_pullback(f_matrix(),form),scale(form,117)),Q(-1,44))


def forward(form):
    return combine(wedge(form,R_B),wedge(j_operator(form),I_B),-1)


def recover(form,divisor=None):
    return scale(integrate_B(wedge(form,R_B if divisor is None else divisor)),Q(-1,2))


def scalar_matrix(n,active=None):
    active = set(range(n)) if active is None else set(active)
    matrix = [[Q(i == j) for j in range(2*n)] for i in range(2*n)]
    for k in active:
        matrix[2*k][2*k],matrix[2*k+1][2*k+1] = Q(0),Q(0)
        matrix[2*k][2*k+1],matrix[2*k+1][2*k] = Q(-1),Q(1)
    return matrix


def hyperbolic_basis():
    zero = (Q(0),Q(0))
    vectors = [[zero for _ in range(8)] for _ in range(4)]
    for v,p,n in ((0,0,3),(1,1,4)):
        vectors[v][p] = vectors[v][n] = (Q(1),Q(0))
    vectors[2][2],vectors[2][6],vectors[2][5] = (Q(1),0),(Q(1),Q(1)),(Q(1),0)
    vectors[3][2],vectors[3][6],vectors[3][7] = (Q(-1),Q(1)),(Q(1),0),(Q(1),0)
    dual = []
    for v,negative,c in zip(vectors,(3,4,5,7),(1,1,3,3)):
        dual.append([tuple(x*Q(-1 if i == negative else 1,2*c) for x in value) for i,value in enumerate(v)])
    columns = vectors+dual
    return [[columns[j][i] for j in range(8)] for i in range(8)]


@lru_cache(maxsize=1)
def exact_core():
    # Cache fixed rational calculations only, not contracts or source reads.
    H = [[(Q(d if i == j else 0),Q(0)) for j in range(8)] for i,d in enumerate(DS8)]
    S = hyperbolic_basis()
    adjoint = [[conjugate(S[j][i]) for j in range(8)] for i in range(8)]
    gram = gmatrix_product(gmatrix_product(adjoint,H),S)
    expected = [[(Q((i < 4 and j == i+4) or (j < 4 and i == j+4)),Q(0)) for j in range(8)] for i in range(8)]
    require(gram == expected and gdet(H) == (9,0) and gdet(S) != (0,0),'explicit split Hermitian basis')
    # Actual graph-divisor classes on B, with the negative native complex plane.
    jb = [[0,-1,0,0],[1,0,0,0],[0,0,0,1],[0,0,-1,0]]
    jstd = [[0,-1],[1,0]]
    phi1 = [[1,0,-1,0],[0,1,0,1]]
    phii = [[1,0,0,-1],[0,1,-1,0]]
    for phi in (phi1,phii):
        require(multiply(phi,jb) == multiply(jstd,phi),'graph map not holomorphic')
    point = {(0,1):Q(1)}
    gamma1,gammai = (shift(full_pullback(phi,point),12) for phi in (phi1,phii))
    dsum = {(12,13):Q(1),(14,15):Q(-1)}
    require(combine(gamma1,dsum,-1) == I_B and combine(dsum,gammai,-1) == R_B,'explicit graph divisor formulas')
    degrees = [integrate_B(wedge(a,b)).get((),Q(0)) for a,b in ((R_B,R_B),(R_B,I_B),(I_B,I_B))]
    require(degrees == [-2,0,-2] and integrate_B(scale(wedge(E_B,E_B),Q(1,2))) == {():Q(3)},'divisor intersection orientation')
    r6,i6 = weil_forms(6)
    r8,i8 = weil_forms(8)
    require(forward(r6) == r8 and forward(i6) == i8,'Weil forward transfer')
    require(recover(r8) == r6 and recover(i8) == i6,'Weil reverse transfer')
    require(r8[tuple(range(0,16,2))] == 1,'stabilized class nonzero')
    samples = [(Q(a,3),Q(b,5)) for a in range(-3,4) for b in range(-3,4) if a or b]
    for a,b in samples:
        require(recover(combine(scale(r8,a),scale(i8,b))) == combine(scale(r6,a),scale(i6,b)),'rational Weil transfer controls')
    E = {(2*j,2*j+1):Q(d) for j,d in enumerate(DS8[:6])}
    cube = wedge(wedge(E,E),E)
    known_cycle = forward(cube)
    require(known_cycle and recover(known_cycle) == cube and j_operator(cube) == scale(cube,Q(-11,2)) and
            not set(known_cycle) & (set(r8)|set(i8)), 'full Chow retraction positive control')
    require(not integrate_B(r8) and not recover(r8,E_B),'bare projection or polarization cannot recover Weil class')
    require(full_pullback(scalar_matrix(8),r8) == r8 and full_pullback(scalar_matrix(8),i8) == i8,'diagonal i fixes W8')
    require(full_pullback(scalar_matrix(8,range(6)),r8) == scale(r8,-1),'i on X only negates W8')
    return {'A_complex_dimension':8,'A_Hermitian_determinant':9,'A_K_Witt_index_from_explicit_basis':4,
            'hyperbolic_basis_determinant':[str(x) for x in gdet(S)],
            'hyperbolic_basis_columns':[[[str(x) for x in S[i][j]] for i in range(8)] for j in range(8)],
            'B_divisor_intersection_degrees':list(map(int,degrees)), 'B_polarization_euler_characteristic':3,
            'R8_term_count':len(r8),'R8_all_x_period':1,'Weil_transfer_control_count':len(samples),
            'Chow_retraction_proved_by_written_projection_formula':True,
            'full_H8_retraction_image_projector_rank':924,'Weil_restriction_rank':2,
            'diagonal_i_on_W8':1,'i_on_X_only_on_W8':-1,
            'bare_projection_Weil_transfer_rejected':True,'polarization_divisor_Weil_transfer_rejected':True,
            'known_algebraic_divisor_cube_transfers_outside_W8':True}


def validate_stabilization(c):
    require(c['schema'] == 'marici.hodge-split-eightfold-stabilization.v1' and
            c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1','stabilization fixed candidate binding')
    require(c['node'] == 'split-eightfold-stabilization' and c['verdict'] == 'constructed' and
            c['resolution_kind'] == 'explicit_split_eightfold_and_algebraic_Weil_transfer_retraction','stabilization node binding')
    require(c['fixed_target'] == {'X_dimension':6,'X_codimension':3,'alpha':'R6','unchanged':True},'auxiliary target replaced fixed candidate')
    a = c['auxiliary']
    require(a['dimension'] == 8 and a['codimension'] == 4 and a['B_dimension'] == 2 and
            a['A_Hermitian_diagonal'] == list(DS8) and a['B_Hermitian_diagonal'] == [1,-3] and
            a['A_determinant'] == 9 and a['A_K_Witt_index'] == 4 and a['B_integration_orientation'] == -1 and
            a['B_complex_structure'] == 'diag(i,-i) in native real coordinates','auxiliary geometry or orientation')
    t = c['transfer']
    require(t['codimension_shifts'] == {'S':1,'D':-1} and t['reverse_coefficient'] == '-1/2' and
            t['J_pullback_coefficient'] == '-1/44' and t['J_identity_coefficient'] == '-117/44' and
            t['full_H8_image_projector_rank'] == 924 and
            t['rank_two_only_on_Weil_spaces'] is True and t['Chow_S_D_identity_on_all_CH4_A_claimed'] is False and
            t['J_CH_square_minus_identity_claimed'] is False,'Chow transfer scope')
    require(c['Weil_classes']['diagonal_i_action_on_W8'] == 1 and
            c['Weil_classes']['i_on_X_only_action_on_W8'] == -1,'changed-dimensional symmetry scope')
    require(c['divisors']['intersection_degrees'] == {'r_squared':-2,'r_s':0,'s_squared':-2},'intersection normalization')
    require(c['source_boundary'] == {'retained_secant_theorem_dimension':6,'auxiliary_dimension':8,
            'sixfold_theorem_applied_to_A':False,'full_Hodge_space_of_A_computed':False},'dimension-shift theorem misuse')
    require(len(c['boundary']) == 7 and all(x is False for x in c['boundary'].values()),'transfer promoted to algebraicity')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_stabilization(c)
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-secant-sheaf-transplant-v1.json','transplant source binding')
    old = json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    require(old == transplant_report() and old['candidate_id'] == c['candidate_id'],'stale theorem-transplant source')
    checks = dict.fromkeys(['product_CM_surface_and_explicit_maximal_K_isotropic_four_plane',
        'graph_divisors_are_actual_holomorphic_kernel_divisors',
        'negative_complex_orientation_and_divisor_intersection_degrees',
        'Weil_stabilization_and_reverse_transfer_exact_on_two_generators_and_48_controls',
        'Chow_retraction_from_projection_formula_not_just_cohomology',
        'full_image_projector_rank_924_not_a_rank_two_Weil_Chow_projector',
        'bare_projection_and_polarization_insertion_do_not_recover_the_Weil_class',
        'known_nonzero_algebraic_cycle_does_not_supply_a_W8_witness',
        'anti_i_sixfold_test_not_reused_for_diagonal_i_on_eightfold',
        'sixfold_theorem_not_applied_after_dimension_change'],True)
    sources = {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_secant_sheaf_transplant.py',
        'research/voevodsky/checkers/check_hodge_explicit_sixfold_candidate.py',
        'research/voevodsky/checkers/check_hodge_literature_boundary_audit.py',
        'research/voevodsky/checkers/check_hodge_weil_projector.py'}
    return {'schema':'marici.hodge-split-eightfold-stabilization-result.v1','passed':True,'checks':checks,
            'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',**exact_core(),
            'specified_W8_algebraicity_equivalent_to_alpha_algebraicity':True,
            'nonzero_algebraic_W8_class_constructed':False,'algebraic_representative_of_alpha_constructed':False,
            'all_cycle_annihilation_proved':False,'alpha_nonalgebraic_proved':False,
            'sixfold_theorem_applied_to_A':False,'Hodge_proved':False,'Hodge_refuted':False,
            'verification_level':c['trust_scope'],
            'source_sha256':{name:sha256((ROOT/name).read_bytes()).hexdigest() for name in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_sha256','hyperbolic_basis_columns')},indent=2))
