"""Explicit two-primary successor; indecomposable is not Prym membership."""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from math import comb, factorial
from pathlib import Path
import json
from check_hodge_explicit_sixfold_candidate import inverse
from check_hodge_gaussian_principal_isogeny import T as T9, real_matrix, DY
from check_hodge_principal_prym_membership import report as membership_report
from check_hodge_secant_sheaf_transplant import cmul, gdet, valuation3
from check_hodge_split_eightfold_stabilization import DS8, full_pullback, scale, recover, wedge
from check_hodge_eightfold_weil_filter import forward_fast, generators
from check_hodge_eightfold_hodge_kernel import channels, exceptional_projector

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-indecomposable-principal-model.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-indecomposable-principal-model-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-indecomposable-principal-model-v1.json'
HADAMARD = (((Q(1),Q(0)),(Q(1),Q(0))),((Q(1),Q(0)),(Q(-1),Q(0))))
NEGATIVE = tuple(tuple(cmul((Q(1),Q(1)),x) for x in row) for row in T9)
BLOCKS = (((0,1,12,13),real_matrix(HADAMARD)),((10,11,14,15),real_matrix(NEGATIVE))) + tuple(
    ((2*k,2*k+1),[[Q(1),Q(-1)],[Q(1),Q(1)]]) for k in (1,2,3,4))


def require(condition,message):
    if not condition:
        raise ValueError(message)


def gaussian_matrix():
    out = [[(Q(0),Q(0)) for _ in range(8)] for _ in range(8)]
    for coords,m in (((0,6),HADAMARD),((5,7),NEGATIVE)):
        for i,a in enumerate(coords):
            for j,b in enumerate(coords):
                out[a][b] = m[i][j]
    for k in (1,2,3,4):
        out[k][k] = (Q(1),Q(1))
    return out


@lru_cache(maxsize=2)
def compounds(backward=False):
    result = []
    for coords,matrix in BLOCKS:
        m = inverse(matrix) if backward else matrix
        result.append({s:full_pullback(m,{s:Q(1)}) for k in range(len(coords)+1)
            for s in combinations(range(len(coords)),k)})
    return result


@lru_cache(maxsize=None)
def substitution(block,indices,backward=False):
    coords = BLOCKS[block][0]
    inside = tuple(i for i in indices if i in coords)
    outside = tuple(i for i in indices if i not in coords)
    sign_in = (-1)**sum(i > j for i in outside for j in inside)
    local = tuple(coords.index(i) for i in inside)
    result = {}
    for target,c in compounds(backward)[block][local].items():
        global_target = tuple(coords[i] for i in target)
        sign_out = (-1)**sum(i > j for i in outside for j in global_target)
        result[tuple(sorted(outside+global_target))] = c*sign_in*sign_out
    return result


def f_pull(form,backward=False):
    """Exterior cohomology pullback or its inverse, NOT an inverse Chow map."""
    require(all(tuple(sorted(set(s))) == s and all(0 <= i < 16 for i in s) for s in form),
        'invalid successor coordinates')
    for block in range(len(BLOCKS)):
        result = {}
        for indices,value in form.items():
            for target,c in substitution(block,indices,backward).items():
                result[target] = result.get(target,Q(0))+value*c
        form = {s:v for s,v in result.items() if v}
    return form


def f_push(form):
    return scale(f_pull(form,True),2304)


def forward_new(form):
    return scale(f_push(forward_fast(form)),Q(1,48))


def reverse_new(form):
    return scale(recover(f_pull(form)),Q(1,48))


def channels_new(form):
    return channels(f_pull(form))


def exceptional_new(form):
    return scale(f_push(exceptional_projector(f_pull(form))),Q(1,2304))


@lru_cache(maxsize=1)
def exact_core():
    k_matrix = gaussian_matrix()
    require(gdet(k_matrix) == (Q(0),Q(48)),'successor Gaussian determinant phase')
    require(sorted(i for coords,m in BLOCKS for i in coords) == list(range(16)), 'real direct-sum block coverage')
    columns = 0
    for coords,m in BLOCKS:
        inv = inverse(m)
        for k in range(len(coords)+1):
            for s in combinations(range(len(coords)),k):
                v = {s:Q(1)}
                require(full_pullback(inv,full_pullback(m,v)) == v and
                    full_pullback(m,full_pullback(inv,v)) == v,'local compound inverse certificate')
                columns += 1
    require(columns == 48 and comb(16,8) == 12870,'factorized exterior certificate dimensions')
    # Cross-check tensor/sign implementation with full native pullback on four H8 columns.
    full = [[Q(int(i == j)) for j in range(16)] for i in range(16)]
    for coords,m in BLOCKS:
        for i,a in enumerate(coords):
            for j,b in enumerate(coords):
                full[a][b] = m[i][j]
    samples = (tuple(range(8)),tuple(range(0,16,2)),(0,1,3,6,10,12,14,15),(1,2,5,7,9,11,12,15))
    for s in samples:
        v = {s:Q(1)}
        require(f_pull(v) == full_pullback(full,v) and f_push(f_pull(v)) == scale(v,2304) and
            f_pull(f_push(v)) == scale(v,2304),'global tensor sign/inverse cross-check')
    EA = {(2*k,2*k+1):Q(d) for k,d in enumerate(DS8)}
    Enew = {(2*k,2*k+1):Q(d) for k,d in enumerate(DY)}
    require(f_pull(Enew) == scale(EA,2),'changed pullback polarization is 2 E_A')
    require(f_pull({tuple(range(16)):Q(1)}) == {tuple(range(16)):Q(2304)},'isogeny degree')
    kernel_orders = []
    for axis in (6,7):
        col = [k_matrix[i][axis] for i in range(8)]
        residues = []
        for a,b in product(range(2),repeat=2):
            values = [cmul(c,(Q(a,2),Q(b,2))) for c in col]
            if all(x.denominator == 1 and y.denominator == 1 for x,y in values):
                residues.append([a,b])
        kernel_orders.append(len(residues))
    require(kernel_orders == [1,2],'elliptic axis kernel orders')
    # The plus column contains a unit; the minus column contains 1+i.
    # These bound all denominators by two, so the preceding residue enumeration is complete.
    require((Q(1),Q(0)) in [k_matrix[i][6] for i in range(8)] and
        (Q(1),Q(1)) in [k_matrix[i][7] for i in range(8)],'axis denominator bounds')
    elliptic_degrees = [Q(2,1)/kernel_orders[0],Q(6,1)/kernel_orders[1]]
    require(elliptic_degrees == [2,3] and valuation3(Q(3))%2 == 1,'indecomposable factor exclusions')
    r8,i8 = generators(8)
    require(f_pull(r8) == scale(i8,-48) and f_pull(i8) == scale(r8,48) and
        f_push(r8) == scale(i8,48) and f_push(i8) == scale(r8,-48),'Weil quarter-turn, not real scalar')
    r6,i6 = generators(6)
    EX = {(2*k,2*k+1):Q(d) for k,d in enumerate(DS8[:6])}
    cube = wedge(wedge(EX,EX),EX)
    for v in (r6,i6,cube):
        require(reverse_new(forward_new(v)) == v,'normalized successor retraction control')
    require(forward_new(r6) == i8 and forward_new(i6) == scale(r8,-1), 'original alpha transfer phase')
    require(not any(channels_new(forward_new(cube))),'divisor cube promoted to exceptional cycle')
    require(exceptional_new(r8) == r8 and exceptional_new(i8) == i8,'full exceptional filter transport')
    return {'actual_principal_Gaussian_model_constructed':True,'principal_polarization_indecomposable':True,
        'successor_step_degree':256,'composite_isogeny_degree':2304,'pullback_polarization_multiplier':2,
        'Gaussian_composite_determinant':[0,48],'native_Weil_pullback':{'Rnew':'-48 I_A','Inew':'48 R_A'},
        'normalized_transfer_denominator':48,'alpha_R6_forward_image':'Inew',
        'elliptic_axis_isogeny_degrees':kernel_orders,'elliptic_axis_polarization_degrees':[2,3],
        'excluded_principal_product_factor_dimensions':[[6,2],[6,1,1],[7,1]],
        'factorized_inverse_local_exterior_columns':columns,'factorized_certificate_H8_dimension':12870,
        'explicit_global_H8_sample_columns':len(samples),'principal_theta_top_intersection':factorial(8),
        'rational_Hdg4_dimension':14,'divisor_Hdg4_dimension':6,'exceptional_Hdg4_dimension':8,
        'four_channel_cycle_test_transported':True}


def validate_model(c):
    require(c['schema'] == 'marici.hodge-indecomposable-principal-model.v1' and
        c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node'] == 'indecomposable-principal-model' and c['verdict'] == 'constructed','successor model identity')
    require(c['resolution_kind'] == 'two_primary_repolarized_Gaussian_gluing_indecomposable_model_with_phase_correct_transfer',
        'successor model resolution')
    require(c['geometry'] == {'complex_dimension':8,'step_degree':256,'composite_degree':2304,
        'pullback_polarization_multiplier':2,'principal_Hermitian_diagonal':list(DY),
        'elliptic_axis_polarization_degrees':[2,3],'original_candidate_X_changed':False},'successor model geometry')
    require(c['transfer'] == {'Gaussian_composite_determinant':[0,48],'normalized_denominator':48,
        'R6_forward_image':'Inew','I6_forward_image':'-Rnew',
        'certificate':'48_local_exterior_columns_tensor_cover_H8_not_12870_explicit_columns'},'successor transfer phase or certificate scope')
    require(c['policy'] == dict.fromkeys(['marking_change_is_endomorphism_of_A','Prym_cover_constructed',
        'Prym_presentation_excluded','Mumford_product_crossing_argument_reused','theta_singular_locus_dimension_computed',
        'generic_Weil_eightfold_claimed','native_Weil_generators_identified_without_rotation',
        'Chow_retraction_claimed','transported_filter_Chow_idempotence_claimed'],False),'successor scope promoted')
    require(set(c['boundary']) == {'Hodge_proved','Hodge_refuted','alpha_nonalgebraic_proved',
        'algebraic_representative_of_alpha_constructed','nonzero_algebraic_Weil_class_constructed',
        'all_cycle_annihilation_proved'} and all(v is False for v in c['boundary'].values()),'successor verdict promotion')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_model(c)
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-principal-prym-membership-v1.json', 'old-model audit binding')
    old = json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    require(old == membership_report() and old['candidate_id'] == c['candidate_id'] and
        old['fixed_theta_Y_smooth_etale_Prym_presentation_excluded'] and not old['other_polarizations_excluded'],
        'stale old-model audit or scope expanded')
    sources = {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_principal_prym_membership.py',
        'research/voevodsky/checkers/check_hodge_gaussian_principal_isogeny.py',
        'research/voevodsky/checkers/check_hodge_eightfold_hodge_kernel.py',
        'research/voevodsky/checkers/check_hodge_eightfold_weil_filter.py'}
    return {'schema':'marici.hodge-indecomposable-principal-model-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',**exact_core(),
        'checks':dict.fromkeys(['integral_Gaussian_lattice_inclusion_and_unimodular_2EA_Riemann_form',
            'elliptic_axis_degrees_two_three_and_complete_principal_factor_case_analysis',
            'factorized_all_degree_inverse_certificate_and_native_sample_cross_checks',
            'imaginary_48i_Weil_factor_and_normalized_full_cohomology_retraction',
            'four_channels_and_divisor_control_do_not_supply_exceptional_cycle',
            'indecomposable_not_a_cover_membership_or_Hodge_verdict'],True),
        **c['policy'],**c['boundary'],'verification_level':c['trust_scope'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'source_sha256'},indent=2))
