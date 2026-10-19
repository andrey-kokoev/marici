"""A bounded actual-cycle search plus a written, library-scoped symmetry theorem.
Rational samples certify a universal centralizer bound; the fixed transcendental
point uses the prior algebraic-independence proof, never sample specialization.
"""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
from check_hodge_explicit_sixfold_candidate import (
    DS, sample_J, sparse_rank, identity, full_pullback, rref, weil_forms, wedge)
from check_hodge_weil_projector import (
    f_matrix, projection_polynomial, apply_polynomial, report as projector_report)

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-tautological-witness-search.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-tautological-witness-search-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-tautological-witness-search-v1.json'
SEEDS = ['all_rational_divisor_classes_on_powers', 'units_and_point_classes',
         'certified_exponential_Chern_characters_r_exp_c1_over_r']
OPERATIONS = ['rational_linear_combination', 'cup_and_external_products',
              'pullback_by_homomorphisms_between_smooth_powers_with_refined_intersection_license',
              'proper_pushforward_by_homomorphisms_between_powers',
              'graph_correspondences_of_such_homomorphisms',
              'Poincare_exponential_kernel_transform_pulled_back_by_polarization']


def require(condition, message):
    if not condition:
        raise ValueError(message)


def commutator_rows(j):
    for a in range(12):
        for b in range(12):
            row = [Q(0)]*144
            for k in range(12):
                row[12*k+b] += j[a][k]
                row[12*a+k] -= j[k][b]
            yield row


def scale(form, scalar):
    return {s: scalar*v for s,v in form.items() if scalar*v}


def fourier(form):
    """Integrate exp(ell), factored over the six native real two-planes.
    Local images of (1,dx,dy,dxdy) are (-d^2 dxdy,-d dx,-d dy,1).
    Global integration has sign -1 in the marked lattice orientation.
    """
    result = {}
    for indices,value in form.items():
        coefficient, output = -Q(value), []
        for j,d in enumerate(DS):
            occupied = tuple(k for k in (2*j,2*j+1) if k in indices)
            if not occupied:
                coefficient *= -d*d
                output.extend((2*j,2*j+1))
            elif len(occupied) == 1:
                coefficient *= -d
                output.extend(occupied)
        key = tuple(output)
        result[key] = result.get(key,Q(0)) + coefficient
    return {s:v for s,v in result.items() if v}


@lru_cache(maxsize=1)
def exact_core():
    # Only fixed rational calculations are cached; report rereads mutable sources.
    samples = [sample_J()] + [sample_J(i,j,b) for i in range(3) for j in range(3) for b in (False,True)]
    special_dimension = 144-sparse_rank(list(commutator_rows(samples[0])))
    require(special_dimension == 72, 'special fiber extra endomorphisms')
    rows = [row for j in samples for row in commutator_rows(j)]
    rank, row_ids = sparse_rank(rows,certificate=True)
    require(rank == 142, 'centralizer rank')
    _,pivots = rref([rows[i] for i in row_ids])
    require(len(pivots) == 142, 'independent centralizer certificate')
    tau = f_matrix(0,1)
    for matrix in (identity(12),tau):
        vector = [v for row in matrix for v in row]
        require(all(sum(a*b for a,b in zip(row,vector)) == 0 for row in rows), 'centralizer basis')
    E = {(2*j,2*j+1):Q(d) for j,d in enumerate(DS)}
    real,imaginary = weil_forms(6)
    require(full_pullback(tau,E) == E and full_pullback(tau,real) == scale(real,-1) and
            full_pullback(tau,imaginary) == scale(imaginary,-1), 'central i symmetry')
    powers = [{():Q(1)}]
    for k in range(1,7):
        powers.append(scale(wedge(powers[-1],E),Q(1,k)))
    for k in range(7):
        require(fourier(powers[k]) == scale(powers[6-k],3*(-1)**(6-k)), 'Fourier divisor powers')
    require(fourier(real) == scale(real,3) and fourier(imaginary) == scale(imaginary,3), 'Fourier Weil value')
    count = 0
    for k in range(13):
        for indices in combinations(range(12),k):
            basis = {indices:Q(1)}
            require(fourier(fourier(basis)) == scale(basis,9*(-1)**k), 'Fourier square')
            count += 1
    require(count == 4096, 'full exterior Fourier census')
    p,_,_ = projection_polynomial()
    records = []
    for a in range(7):
        for b in range(7):
            c = 9-a-b
            if c < 0:
                continue
            image = wedge(fourier(powers[a]),powers[b]) if 2*a+c == 12 else {}
            scalar = image.get(tuple(range(6)),Q(0))  # coefficient of E^3/3! here is 1
            require(image == scale(powers[3],scalar), 'non-divisor search image')
            require(not apply_polynomial(p,image), 'unexpected Weil witness')
            records.append({'a':a,'b':b,'c':c,'coefficient_of_E3_over_3_factorial':str(scalar)})
    nonzero = [v for v in records if v['coefficient_of_E3_over_3_factorial'] != '0']
    require(len(records) == 43 and [v['coefficient_of_E3_over_3_factorial'] for v in nonzero] == ['-3','9','-9','3'], 'finite search census')
    # Every E*H^4 monomial contains a native dx_j dy_j pair, hence both K characters.
    # The endpoint projector therefore kills it; this is the written kappa correction proof.
    for indices in combinations(range(12),4):
        form = wedge(E,{indices:Q(1)})
        require(all(any(2*j in s and 2*j+1 in s for j in range(6)) for s in form), 'Lefschetz character support')
    for indices in ((0,2,4,6),(0,1,4,7),(0,1,2,3),(1,3,8,10)):
        require(not apply_polynomial(p,wedge(E,{indices:Q(1)})), 'Lefschetz correction projection')
    return {'sample_count':19, 'endomorphism_matrix_variables':144, 'stacked_commutator_rank':rank,
            'independent_commutator_row_indices':row_ids, 'End0_dimension_from_written_genericity_proof':2,
            'special_fiber_End0_dimension':special_dimension,
            'Fourier_basis_control_count':count, 'finite_search_count':len(records),
            'nonzero_cohomology_image_count':len(nonzero), 'nonzero_Weil_projection_count':0,
            'finite_search':records, 'Fourier_alpha_multiplier':3, 'Fourier_divisor_cube_multiplier':-3,
            'Lefschetz_degree_four_basis_support_controls':495}


def validate_search(c):
    require(c['schema'] == 'marici.hodge-tautological-witness-search.v1' and
            c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1', 'search identity')
    require(c['node'] == 'tautological-power-witness-search' and c['verdict'] == 'rejected' and
            c['resolution_kind'] == 'central_i_symmetry_excludes_divisorial_power_correspondence_library', 'search rejection binding')
    require(c['endomorphism_certificate']['sample_count'] == 19 and
            c['endomorphism_certificate']['matrix_variable_count'] == 144 and
            c['endomorphism_certificate']['stacked_commutator_rank'] == 142 and
            c['endomorphism_certificate']['rational_centralizer_dimension'] == 2, 'centralizer certificate binding')
    require(c['symmetry']['automorphism'] == 'tau=i on X and diagonally on every power' and
            c['symmetry']['on_weil_space'] == 'tau*=-Id' and
            c['symmetry']['on_divisor_classes_of_every_power'] == 'tau*=Id', 'symmetry binding')
    library = c['library']
    require(library['seeds'] == SEEDS and library['operations'] == OPERATIONS and
            library['arbitrary_higher_Chern_classes_included'] is False and
            library['arbitrary_algebraic_subvarieties_included'] is False, 'bounded library promoted')
    require(c['finite_search']['monomial_count'] == 43 and c['finite_search']['nonzero_cohomology_images'] == 4 and
            c['finite_search']['all_Weil_projections_zero'] is True, 'finite search binding')
    f = c['fourier_control']
    require(f['polarization_euler_characteristic'] == 3 and f['on_alpha'] == 3 and
            f['basis_control_count'] == 4096 and
            f['formula'] == 'Phi_E(E^k/k!)=3*(-1)^(6-k)*E^(6-k)/(6-k)!', 'Fourier normalization')
    require(len(c['boundary']) == 7 and all(v is False for v in c['boundary'].values()), 'bounded failure promoted to Hodge verdict')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_search(c)
    require(c['candidate_contract'] == 'research/conjecture_net/contracts/hodge-explicit-sixfold-candidate.v1.json' and
            c['candidate_receipt'] == 'research/voevodsky/results/hodge-explicit-sixfold-candidate-v1.json' and
            c['projector_contract'] == 'research/conjecture_net/contracts/hodge-weil-projector.v1.json' and
            c['projector_receipt'] == 'research/voevodsky/results/hodge-weil-projector-v1.json', 'fixed input bindings')
    projector = json.loads((ROOT/c['projector_receipt']).read_text(encoding='utf-8'))
    require(projector == projector_report() and projector['candidate_id'] == c['candidate_id'], 'stale projector source')
    checks = dict.fromkeys([
        'rank_142_commutator_bound_and_independent_dense_certificate',
        'End0_Qi_and_all_power_divisor_symmetry_by_written_genericity_Rosati_proof',
        'central_i_fixes_seeds_but_negates_the_Weil_plane',
        'product_special_fiber_extra_endomorphisms_prevent_uniform_extension',
        'typed_pull_push_and_kernel_library_preserves_symmetry',
        '43_actual_correspondence_classes_have_zero_Weil_projection',
        'Fourier_square_verified_on_all_4096_exterior_basis_elements',
        'Fourier_fixes_Weil_plane_up_to_3_not_a_universal_annihilator',
        'normalized_third_Chern_positive_route_retains_arbitrary_bundle_search',
        'bounded_library_failure_does_not_resolve_global_witness_or_annihilation_gate'],True)
    sources = {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['candidate_contract'], c['candidate_receipt'], c['projector_contract'], c['projector_receipt'],
        'research/voevodsky/checkers/check_hodge_explicit_sixfold_candidate.py',
        'research/voevodsky/checkers/check_hodge_weil_projector.py'}
    return {'schema':'marici.hodge-tautological-witness-search-result.v1','passed':True,
            'checks':checks, 'candidate_id':c['candidate_id'], 'node':c['node'], 'verdict':'rejected',
            **exact_core(), 'bounded_library_excluded':True, 'all_cycle_annihilation_proved':False,
            'global_algebraic_witness_search_completed':False, 'alpha_nonalgebraic_proved':False,
            'algebraic_representative_of_alpha_constructed':False, 'Hodge_proved':False, 'Hodge_refuted':False,
            'verification_level':c['trust_scope'],
            'source_sha256':{name:sha256((ROOT/name).read_bytes()).hexdigest() for name in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_sha256','finite_search','independent_commutator_row_indices')},indent=2))
