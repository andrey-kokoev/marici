"""Exact generic middle Hodge kernel: modular minor bound + rational generators.
The genericity implication is proved in the note, not inferred from samples.
"""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
from math import isqrt, comb
from pathlib import Path
import json
from check_hodge_explicit_sixfold_candidate import sample_J, lie_action, full_pullback, DS, weil_forms, wedge
from check_hodge_weil_projector import f_matrix, projection_polynomial, apply_polynomial, combine
from check_hodge_tautological_witness_search import report as search_report

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-middle-hodge-kernel.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-middle-hodge-kernel-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-middle-hodge-kernel-v1.json'
BASIS = tuple(combinations(range(12),6))
PRIME = 1000003


def require(condition, message):
    if not condition:
        raise ValueError(message)


def is_prime(p):
    return p >= 2 and all(p%d for d in range(2,isqrt(p)+1))


def residue(value,p):
    value = Q(value)
    require(value.denominator % p != 0, 'noninvertible rational denominator')
    return value.numerator*pow(value.denominator,-1,p)%p


def modular_rank(rows,p):
    require(is_prime(p),'rank modulus must be prime')
    pivots, ids, columns, scales = {}, [], [], []
    for row_id,row in enumerate(rows):
        v = {k:x%p for k,x in row.items() if x%p}
        while v:
            col = min(v)
            value = v[col]
            if col not in pivots:
                inv = pow(value,-1,p)
                pivots[col] = {k:x*inv%p for k,x in v.items()}
                ids.append(row_id); columns.append(col); scales.append(value)
                break
            for k,x in pivots[col].items():
                changed = (v.get(k,0)-value*x)%p
                if changed:
                    v[k] = changed
                else:
                    v.pop(k,None)
    # For a square full-rank matrix, sorting the admitted pivot rows makes the
    # normalized matrix upper triangular. Row-normalization factors recover det.
    det = (-1)**sum(a>b for i,a in enumerate(columns) for b in columns[i+1:])
    for value in scales:
        det = det*value%p
    return len(pivots),ids,columns,det%p


def exterior_rows(j):
    positions = {indices:k for k,indices in enumerate(BASIS)}
    rows = [{} for _ in BASIS]
    for col,indices in enumerate(BASIS):
        for target,value in lie_action(j,{indices:Q(1)}).items():
            rows[positions[target]][col] = value
    return rows


def cyclic_product(a,b):
    result = [Q(0)]*4
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            result[(i+j)%4] += x*y
    return result


def anti_projector(form):
    return {s:v/2 for s,v in combine(form,full_pullback(f_matrix(0,1),form),-1).items()}


@lru_cache(maxsize=1)
def exact_core():
    # Fixed rational mathematics only. Mutable contracts and receipts are reread.
    samples = [sample_J()] + [sample_J(i,j,b) for i in range(3) for j in range(3) for b in (False,True)]
    E = {(2*j,2*j+1):Q(d) for j,d in enumerate(DS)}
    cube = wedge(wedge(E,E),E)
    real,imaginary = weil_forms(6)
    rows = []
    for j in samples:
        require(all(not lie_action(j,v) for v in (cube,real,imaginary)), 'rational Hodge generators at samples')
        rows.extend({col:residue(value,PRIME) for col,value in row.items()} for row in exterior_rows(j))
    rank,ids,columns,_ = modular_rank(rows,PRIME)
    require(rank == 921, 'middle Hodge constraint rank')
    cols = sorted(columns)
    # Independently re-eliminate the transpose of the selected 921-square minor.
    transpose_minor = [{k:rows[r].get(col,0) for k,r in enumerate(ids) if rows[r].get(col,0)} for col in cols]
    minor_rank,_,_,det = modular_rank(transpose_minor,PRIME)
    require(minor_rank == 921 and det != 0, 'selected minor certificate')
    require(cube.get(tuple(range(6))) != 0 and real.get(tuple(range(0,12,2))) == 1 and
            imaginary.get((1,2,4,6,8,10)) == 1 and not cube.get(tuple(range(0,12,2))), 'independent rational generators')
    p,_,_ = projection_polynomial()
    for v in (cube,real,imaginary):
        require(anti_projector(v) == apply_polynomial(p,v), 'two projectors agree on Hodge generators')
    # Agreement is intentionally not asserted on the full 924-dimensional space.
    anti_rank = sum(comb(6,a)**2 for a in (0,2,4,6))
    require(anti_rank == 452, 'full cohomology anti-i rank')
    e = [Q(1,4),Q(-1,4),Q(1,4),Q(-1,4)]
    require(cyclic_product(e,e) == e and cyclic_product([0,1,0,0],e) == [-x for x in e], 'cyclic Chow idempotent')
    half = [Q(1,2),Q(-1,2),Q(0),Q(0)]
    half_squared = cyclic_product(half,half)
    require([a-b for a,b in zip(half_squared,half)] == [Q(-1,4),0,Q(1,4),0], 'half difference is not a cyclic-group-algebra idempotent')
    return {'sample_count':len(samples),'exterior_basis_size':len(BASIS),'stacked_row_count':len(rows),
            'prime':PRIME,'rank_mod_prime':rank,'selected_minor_rank':minor_rank,'selected_minor_determinant_mod_prime':det,
            'independent_row_indices':ids,'minor_column_indices':cols,
            'rational_Hodge_dimension_from_written_genericity_proof':3,
            'Hodge_basis':['E^3','R','I'],'tau_invariant_Hodge_dimension':1,'tau_anti_invariant_Hodge_dimension':2,
            'full_H6_anti_i_projector_rank':anti_rank,'restricted_anti_i_projector_rank':2,
            'genuine_Chow_idempotent_coefficients':[str(x) for x in e],
            'half_difference_Chow_idempotence_claim_rejected':True}


def validate_kernel(c):
    require(c['schema'] == 'marici.hodge-middle-hodge-kernel.v1' and
            c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1', 'kernel fixed candidate binding')
    require(c['node'] == 'generic-middle-hodge-kernel' and c['verdict'] == 'constructed' and
            c['resolution_kind'] == 'generic_degree_six_Hodge_kernel_and_finite_order_cycle_projector', 'kernel node binding')
    require(c['certificate'] == {'prime':PRIME,'sample_count':19,'exterior_dimension':924,'rank':921,
            'rational_kernel_dimension':3,'kernel_basis':['E^3','R','I']}, 'kernel certificate binding')
    require(c['projectors']['agreement_scope'] == 'Hdg^3(X,Q) only, not full H^6' and
            c['projectors']['anti_i_full_H6_rank'] == 452 and c['projectors']['anti_i_Hodge_rank'] == 2 and
            c['projectors']['Chow_coefficients_ascending_tau'] == ['1/4','-1/4','1/4','-1/4'] and
            c['projectors']['half_difference_Chow_idempotence_claimed'] is False and
            c['projectors']['P_CH_equals_four_term_projector_on_Chow_claimed'] is False, 'projector scope or Chow idempotence error')
    require(len(c['boundary']) == 7 and all(x is False for x in c['boundary'].values()), 'Hodge kernel promoted to algebraicity verdict')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_kernel(c)
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-tautological-witness-search-v1.json', 'previous artifact binding')
    old = json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    require(old == search_report() and old['candidate_id'] == c['candidate_id'], 'stale witness-library source')
    checks = dict.fromkeys([
        '921_square_minor_nonsingular_mod_prime_with_all_rational_denominators_invertible',
        'selected_minor_transpose_replay_and_explicit_row_column_certificate',
        'three_independent_universal_rational_generators_and_written_genericity_argument',
        'full_fixed_point_Hodge_space_not_inferred_from_rational_specialization',
        'anti_i_equals_Weil_projector_on_Hodge_space_but_rank_452_on_full_H6',
        'four_term_finite_order_Chow_projector_is_genuinely_idempotent',
        'two_term_cohomology_projector_not_promoted_to_Chow_idempotence',
        'nonzero_Chow_class_without_nonzero_cycle_class_not_accepted_as_witness',
        'algebraic_image_dimensions_one_or_three_not_a_Hodge_verdict'],True)
    sources = {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'], 'research/conjecture_net/contracts/hodge-tautological-witness-search.v1.json',
        'research/voevodsky/checkers/check_hodge_tautological_witness_search.py',
        'research/voevodsky/checkers/check_hodge_explicit_sixfold_candidate.py',
        'research/voevodsky/checkers/check_hodge_weil_projector.py'}
    return {'schema':'marici.hodge-middle-hodge-kernel-result.v1','passed':True,'checks':checks,
            'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',**exact_core(),
            'possible_algebraic_image_dimensions':[1,3], 'Chow_idempotent_constructed':True,
            'nonzero_homological_anti_i_cycle_constructed':False,
            'algebraic_representative_of_alpha_constructed':False,'all_cycle_annihilation_proved':False,
            'alpha_nonalgebraic_proved':False,'Hodge_proved':False,'Hodge_refuted':False,
            'verification_level':c['trust_scope'],
            'source_sha256':{name:sha256((ROOT/name).read_bytes()).hexdigest() for name in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_sha256','independent_row_indices','minor_column_indices')},indent=2))
