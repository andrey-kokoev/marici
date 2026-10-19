"""Full-cohomology eightfold Weil filter and typed reverse cycle test.
No unknown quotient or presumed algebraic Weil representative enters construction.
"""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, combinations_with_replacement
from math import comb, lcm
from pathlib import Path
import json
from check_hodge_weil_projector import (
    pmul, padd, remainder, cmul, cpow, peval, combine, apply_polynomial,
    projection_polynomial as sixfold_polynomial)
from check_hodge_split_eightfold_stabilization import (
    weil_forms, wedge, full_pullback, f_matrix, DS8, R_B, I_B, E_B, scale,
    forward, recover, report as stabilization_report)

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-eightfold-weil-filter.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-eightfold-weil-filter-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-eightfold-weil-filter-v1.json'
MODULI8 = ((390625,1054,1),(390625,1170,1),(390625,350,1),(390625,-750,1),(-625,1))


def require(condition,message):
    if not condition:
        raise ValueError(message)


def projection_polynomial8():
    q = [Q(1)]
    for m in MODULI8[1:]:
        q = pmul(q,m)
    a,b = remainder(q,MODULI8[0])
    denominator = a*(a-1054*b)+390625*b*b
    inverse = [(a-1054*b)/denominator,-b/denominator]
    p = pmul(inverse,q)
    require(remainder(p,MODULI8[0]) == [1] and all(not remainder(p,m) for m in MODULI8[1:]),'eightfold CRT residues')
    return p,q,inverse


@lru_cache(maxsize=None)
def generators(n):
    return weil_forms(n)


def weil_coordinates(form,n):
    """Coordinates of endpoint projection, derived by dx=(u+ubar)/2,
    dy=(u-ubar)/(2i). Not a fitted reader and not the coordinates of an arbitrary class.
    """
    a,b = Q(0),Q(0)
    for indices,value in form.items():
        require(len(indices) == n and tuple(sorted(set(indices))) == indices and
                all(0 <= i < 2*n for i in indices),'wrong degree or coordinates for Weil filter')
        if tuple(i//2 for i in indices) != tuple(range(n)):
            continue
        k = sum(i%2 for i in indices)
        if k%2 == 0:
            a += value*(-1)**(k//2)
        else:
            b += value*(-1)**((k-1)//2)
    return a/Q(2**(n-1)),b/Q(2**(n-1))


def weil_filter(form,n=8):
    a,b = weil_coordinates(form,n)
    if not (a or b):
        return {}
    real,imaginary = generators(n)
    return combine(scale(real,a),scale(imaginary,b))


@lru_cache(maxsize=None)
def monomial_pullback(indices,n):
    """Tensorized native (2+i) pullback; complete pairs contribute determinant 5."""
    result = {():1}
    for j in range(n):
        occupied = tuple(i for i in (2*j,2*j+1) if i in indices)
        if not occupied:
            continue
        if len(occupied) == 2:
            result = {s+occupied:5*v for s,v in result.items()}
        else:
            x,y = (2,-1) if occupied[0] == 2*j else (1,2)
            result = {s+(i,):v*c for s,v in result.items() for i,c in ((2*j,x),(2*j+1,y))}
    return tuple(result.items())


def native_pullback(form,n):
    result = {}
    for indices,value in form.items():
        for target,c in monomial_pullback(indices,n):
            result[target] = result.get(target,Q(0))+value*c
    return {s:v for s,v in result.items() if v}


def forward_fast(form):
    jform = scale(combine(native_pullback(form,6),scale(form,117)),Q(-1,44))
    return combine(wedge(form,R_B),wedge(jform,I_B),-1)


def filtered_reverse(form):
    return recover(weil_filter(form,8))


@lru_cache(maxsize=1)
def exact_core():
    # Cache fixed rational algebra only, never mutable source reads.
    p,q,inverse = projection_polynomial8()
    minimal = [Q(1)]
    for m in MODULI8:
        minimal = pmul(minimal,m)
    require(not remainder(padd(pmul(p,p),p,-1),minimal),'eightfold cohomological idempotence')
    values = [cmul(cpow((Q(2),Q(1)),a),cpow((Q(2),Q(-1)),8-a)) for a in range(9)]
    multiplicities = [comb(8,a)**2 for a in range(9)]
    require(len(set(values)) == 9 and sum(multiplicities) == 12870,'full eightfold character census')
    for a,value in enumerate(values):
        require(peval(MODULI8[min(a,8-a)],value) == (0,0),'eightfold minimal factors')
        require(peval(p,value) == (Q(int(a in (0,8))),0),'eightfold CRT character selector')
    r8,i8 = generators(8)
    r6,i6 = generators(6)
    require(native_pullback(r8,8) == combine(scale(r8,-527),scale(i8,336)) and
            native_pullback(i8,8) == combine(scale(r8,-336),scale(i8,-527)),'F8 on Weil generators')
    require(weil_filter(r8) == r8 and weil_filter(i8) == i8,'coordinate projector normalization')
    trace,nonzero = Q(0),0
    for indices in combinations(range(16),8):
        a,b = weil_coordinates({indices:Q(1)},8)
        trace += a*r8.get(indices,0)+b*i8.get(indices,0)
        nonzero += bool(a or b)
    require(trace == 2 and nonzero == 256,'complete real basis projection census')
    for indices in ((0,1,2,4,6,8),(0,2,4,6,8,10),(1,3,5,7,9,11)):
        form = {indices:Q(1)}
        require(native_pullback(form,6) == full_pullback(f_matrix(),form),'tensorized pullback cross-check')
        require(forward_fast(form) == forward(form),'forward implementation cross-check')
        require(weil_filter(form,6) == apply_polynomial(sixfold_polynomial()[0],form),'sixfold coordinate/poly cross-check')
    # All 924 source basis vectors: P8 S = S P6, hence D P8 S=P6.
    for indices in combinations(range(12),6):
        v = {indices:Q(1)}
        left = weil_filter(forward_fast(v),8)
        a,b = weil_coordinates(v,6)
        right = combine(scale(r8,a),scale(i8,b))
        require(left == right and recover(left) == weil_filter(v,6),'full source transfer intertwiner')
    E = {(2*j,2*j+1):Q(d) for j,d in enumerate(DS8[:6])}
    powers = [{():Q(1)}]
    for k in range(1,5):
        powers.append(wedge(powers[-1],E))
    d1,d2 = {(12,13):Q(1)},{(14,15):Q(-1)}
    divs = [d1,d2,R_B,I_B]
    records = []
    for k in range(3):
        for indices in combinations_with_replacement(range(4),k):
            form = powers[4-k]
            for j in indices:
                form = wedge(form,divs[j])
            require(not weil_filter(form),'factor-divisor search found a Weil witness')
            records.append({'X_divisor_power':4-k,'B_divisor_indices':list(indices),'class_nonzero':bool(form)})
    require(len(records) == 15 and sum(x['class_nonzero'] for x in records) == 8,'factor-divisor search census')
    E_A = combine(E,E_B)
    fourth = wedge(wedge(E_A,E_A),wedge(E_A,E_A))
    require(fourth and native_pullback(fourth,8) == scale(fourth,625) and not weil_filter(fourth),'divisor fourth-power control')
    require(not filtered_reverse(forward_fast(powers[3])),'nonzero reverse divisor cube is not a filtered witness')
    opposite_real = combine(wedge(r6,R_B),wedge(i6,I_B))
    opposite_imag = combine(wedge(i6,R_B),wedge(r6,I_B),-1)
    require(not weil_filter(opposite_real) and not weil_filter(opposite_imag),'opposite-character Hodge plane not excluded')
    require(recover(opposite_real) == r6 and recover(opposite_imag) == i6 and
            weil_filter(recover(opposite_real),6) == r6,'D P8 not equal to P6 D on arbitrary target')
    require(weil_filter(forward_fast(recover(opposite_real))) == r8 and
            not forward_fast(recover(weil_filter(opposite_real))),'P8 and S D do not commute')
    coarse_rank = sum(multiplicities[a] for a in (0,4,8))
    diagonal_i_rank = sum(multiplicities[a] for a in (0,2,4,6,8))
    require(coarse_rank == 4902 and diagonal_i_rank == 6470,'coarse eightfold projectors')
    coarse = [Q(1,4),Q(1,64),Q(1,1024),Q(1,16384)]
    for a in range(9):
        value = cmul(cpow((Q(1),Q(1)),a),cpow((Q(1),Q(-1)),8-a))
        require(peval(coarse,value) == (Q(int(a in (0,4,8))),0),'coarse 1+i projector aliasing')
    denominator = lcm(*(x.denominator for x in inverse))
    return {'H8_dimension':12870,'character_multiplicities':multiplicities,'rational_Weil_projector_rank':2,
            'polynomial_coefficients_ascending':[str(x) for x in p],
            'factored_inverse_numerators':[int(x*denominator) for x in inverse],
            'factored_inverse_denominator':denominator,'factor_q_coefficients_ascending':[str(x) for x in q],
            'full_coordinate_basis_count':12870,'nonzero_basis_images':256,'coordinate_projector_trace':str(trace),
            'source_intertwiner_basis_count':924,'factor_divisor_cycle_count':15,'nonzero_factor_divisor_classes':8,
            'factor_divisor_controls':records,'nonzero_factor_divisor_Weil_projections':0,
            'coarse_1_plus_i_projector_rank':coarse_rank,'diagonal_i_invariant_projector_rank':diagonal_i_rank,
            'reverse_filter_order_commutation_claim_rejected':True,'P8_and_SD_commutation_claim_rejected':True}


def validate_filter(c):
    require(c['schema'] == 'marici.hodge-eightfold-weil-filter.v1' and
            c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1','eightfold filter candidate binding')
    require(c['node'] == 'eightfold-weil-filter' and c['verdict'] == 'constructed' and
            c['resolution_kind'] == 'rank_two_eightfold_CRT_projector_and_typed_cycle_filter','eightfold filter node binding')
    d = c['definition']
    require(d['complex_dimension'] == 8 and d['cohomological_degree'] == 8 and
            d['endomorphism'] == '2+i on A=X times B' and
            tuple(tuple(x) for x in d['minimal_factors_ascending']) == MODULI8 and
            d['full_cohomology_rank'] == 2,'eightfold filter spectral binding')
    _,_,inverse = projection_polynomial8()
    denominator = lcm(*(x.denominator for x in inverse))
    require(d['factored_inverse_numerators'] == [int(x*denominator) for x in inverse] and
            d['factored_inverse_denominator'] == denominator,'displayed eightfold CRT coefficients')
    require(c['finite_controls'] == {'full_H8_basis_count':12870,'source_intertwiner_basis_count':924,
            'actual_factor_divisor_cycles':15,'nonzero_factor_divisor_classes':8,'nonzero_factor_divisor_Weil_projections':0,
            'coarse_1_plus_i_projector_rank':4902,'diagonal_i_invariant_projector_rank':6470},'eightfold control scope')
    require(c['transfer']['P8_S_equals_S_P6'] is True and c['transfer']['D_P8_S_equals_P6'] is True and
            c['transfer']['D_P8_equals_P6_D_on_all_H8'] is False and
            c['transfer']['P8_commutes_with_SD_on_all_H8'] is False,'eightfold transfer scope')
    require(c['cycle_policy'] == {'preserves_algebraic_cycle_classes':True,'Chow_idempotence_claimed':False,
            'annihilates_all_algebraic_cycles_proved':False,'nonzero_algebraic_W8_class_constructed':False},'eightfold projector promoted')
    require(len(c['boundary']) == 6 and all(x is False for x in c['boundary'].values()),'eightfold filter promoted to Hodge verdict')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_filter(c)
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-split-eightfold-stabilization-v1.json','stabilization source binding')
    old = json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    require(old == stabilization_report() and old['candidate_id'] == c['candidate_id'],'stale stabilization source')
    core = exact_core()
    require(c['definition']['factored_inverse_numerators'] == core['factored_inverse_numerators'] and
            c['definition']['factored_inverse_denominator'] == core['factored_inverse_denominator'],'displayed eightfold CRT coefficients')
    checks = dict.fromkeys(['nine_character_full_H8_spectrum_and_exact_CRT_idempotence',
        'coordinate_formula_derived_from_K_eigenforms_and_all_12870_real_basis_columns',
        'tensor_pullback_and_original_sixfold_polynomial_cross_checks',
        'P8_S_and_D_P8_S_intertwiners_verified_on_all_924_source_basis_vectors',
        '15_actual_factor_divisor_cycles_filtered_without_false_Weil_witness',
        'opposite_Hodge_plane_refutes_D_P8_equals_P6_D_and_P8_SD_commutation',
        'coarse_1_plus_i_and_diagonal_i_projectors_rejected_by_ranks_and_divisor_control',
        'algebraic_correspondence_preservation_not_Chow_idempotence_or_all_cycle_vanishing',
        'fixed_X_alpha_and_unrestricted_research_gates_retained'],True)
    sources = {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_split_eightfold_stabilization.py',
        'research/voevodsky/checkers/check_hodge_weil_projector.py',
        'research/voevodsky/checkers/check_hodge_explicit_sixfold_candidate.py'}
    return {'schema':'marici.hodge-eightfold-weil-filter-result.v1','passed':True,'checks':checks,
            'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',**core,
            'cycle_preserving_filtered_reverse_constructed':True,'nonzero_algebraic_W8_class_constructed':False,
            'algebraic_representative_of_alpha_constructed':False,'all_cycle_annihilation_proved':False,
            'alpha_nonalgebraic_proved':False,'Chow_idempotence_claimed':False,'Hodge_proved':False,'Hodge_refuted':False,
            'verification_level':c['trust_scope'],
            'source_sha256':{name:sha256((ROOT/name).read_bytes()).hexdigest() for name in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_sha256','factor_divisor_controls','polynomial_coefficients_ascending','factor_q_coefficients_ascending')},indent=2))
