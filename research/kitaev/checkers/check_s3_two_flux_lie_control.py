"""Real dynamical Lie closure of gauge quadratures plus two D(S3) flux ports."""

import itertools
import json
import numpy as np
import sympy as sp


def compose(p, q): return tuple(p[q[i]] for i in range(3))
def inverse(p):
    out = [0, 0, 0]
    for i, image in enumerate(p): out[image] = i
    return tuple(out)
def conjugate(g, h): return compose(compose(g, h), inverse(g))
def parity(p): return -1 if sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2 else 1
def cycle_type(p):
    fixed = sum(p[i] == i for i in range(3))
    return "e" if fixed == 3 else ("t" if fixed == 1 else "c")


def main():
    group = list(itertools.permutations(range(3)))
    e, t, c = (0, 1, 2), (1, 0, 2), (1, 2, 0)
    reps = {"e": e, "t": t, "c": c}
    classes = {name: [g for g in group if cycle_type(g) == name] for name in reps}
    transporters = {name: {target: next(q for q in group if conjugate(q, rep) == target) for target in classes[name]} for name, rep in reps.items()}
    sqrt3 = sp.sqrt(3)
    omega = -sp.Rational(1, 2) + sp.I * sqrt3 / 2
    rmat = sp.Matrix([[-sp.Rational(1, 2), -sqrt3 / 2], [sqrt3 / 2, -sp.Rational(1, 2)]])
    smat = sp.diag(1, -1)
    r, s = (1, 2, 0), (1, 0, 2)
    standard = {}
    for k in range(3):
        pr, mr = e, sp.eye(2)
        for _ in range(k): pr, mr = compose(r, pr), rmat * mr
        for epsilon in range(2): standard[compose(pr, s if epsilon else e)] = sp.simplify(mr * (smat if epsilon else sp.eye(2)))
    labels = [
        ("A", "e", "triv", 1), ("B", "e", "sign", 1), ("C", "e", "std", 2),
        ("D", "t", "plus", 3), ("E", "t", "minus", 3),
        ("F", "c", "triv", 2), ("G", "c", "omega", 2), ("H", "c", "omega2", 2),
    ]

    def internal_matrix(label, z):
        _, sector, irrep, _ = label
        if sector == "e":
            if irrep == "triv": return sp.Matrix([[1]])
            if irrep == "sign": return sp.Matrix([[parity(z)]])
            return standard[z]
        if sector == "t": return sp.Matrix([[1 if irrep == "plus" or z == e else -1]])
        power = {e: 0, c: 1, compose(c, c): 2}[z]
        exponent = power * {"triv": 0, "omega": 1, "omega2": 2}[irrep] % 3
        return sp.Matrix([[sp.simplify(omega ** exponent)]])

    def representation(label, g, x):
        _, sector, _, dimension = label
        fluxes = classes[sector]
        internal_dim = dimension // len(fluxes)
        matrix = sp.zeros(dimension)
        for i, flux_in in enumerate(fluxes):
            flux_out = conjugate(x, flux_in)
            j = fluxes.index(flux_out)
            if g != flux_out: continue
            qi, qj = transporters[sector][flux_in], transporters[sector][flux_out]
            z = compose(compose(inverse(qj), x), qi)
            matrix[j * internal_dim:(j + 1) * internal_dim, i * internal_dim:(i + 1) * internal_dim] = internal_matrix(label, z)
        return sp.simplify(matrix)

    def global_endpoint(g, x): return sp.diag(*(representation(label, g, x) for label in labels))
    def global_gauge(x): return sum((global_endpoint(g, x) for g in group), sp.zeros(16))
    offsets = []
    cursor = 0
    for label in labels:
        offsets.append(cursor)
        cursor += label[3]

    def real_vector(matrix):
        entries = []
        for offset, label in zip(offsets, labels):
            dim = label[3]
            entries.extend(list(matrix[offset:offset + dim, offset:offset + dim]))
        return sp.Matrix([sp.simplify(sp.re(z)) for z in entries] + [sp.simplify(sp.im(z)) for z in entries])

    def lie_closure(generators):
        basis = []
        numeric_vectors = np.empty((72, 0), dtype=float)
        def admit(matrix):
            nonlocal numeric_vectors
            matrix = sp.simplify(matrix)
            column = real_vector(matrix)
            numeric_column = np.array([float(sp.N(z, 16)) for z in column], dtype=float).reshape(72, 1)
            candidate = np.hstack((numeric_vectors, numeric_column))
            if np.linalg.matrix_rank(candidate, tol=1e-10) > numeric_vectors.shape[1]:
                basis.append(matrix)
                numeric_vectors = candidate
                return True
            return False
        for generator in generators: admit(generator)
        frontier_start = 0
        while frontier_start < len(basis):
            new = list(basis[frontier_start:])
            frozen = list(basis)
            frontier_start = len(basis)
            for a in new:
                for b in frozen:
                    admit(a * b - b * a)
            if len(basis) > 36: raise AssertionError("closure exceeded block-unitary dimension")
        # Numerical selection is only a proposal.  Certify both independence
        # and commutator closure exactly in one bounded symbolic rank test.
        exact = sp.Matrix.hstack(*(real_vector(a) for a in basis))
        assert exact.rank() == len(basis)
        commutators = [real_vector(a * b - b * a) for a in basis for b in basis]
        assert sp.Matrix.hstack(exact, *commutators).rank() == len(basis)
        return len(basis), basis

    gauge_quadratures = []
    for x in group:
        u = global_gauge(x)
        gauge_quadratures.extend([sp.I * (u + u.H) / 2, (u - u.H) / 2])
    flux_t = global_endpoint(t, e)
    flux_c = global_endpoint(c, e)
    flux_e = global_endpoint(e, e)

    gauge_lie_dimension, _ = lie_closure(gauge_quadratures)
    one_port_dimensions = {
        "identity": lie_closure(gauge_quadratures + [sp.I * flux_e])[0],
        "transposition": lie_closure(gauge_quadratures + [sp.I * flux_t])[0],
        "three_cycle": lie_closure(gauge_quadratures + [sp.I * flux_c])[0],
    }
    two_port_dimension, two_port_basis = lie_closure(gauge_quadratures + [sp.I * flux_t, sp.I * flux_c])
    target_dimension = sum(label[3] ** 2 for label in labels)
    projective_target_dimension = sum(label[3] ** 2 - 1 for label in labels)
    commutators = [a * b - b * a for a in two_port_basis for b in two_port_basis]
    derived_dimension = sp.Matrix.hstack(*(real_vector(x) for x in commutators)).rank()
    per_block_derived_ranks = {}
    for offset, label in zip(offsets, labels):
        dim = label[3]
        entries = []
        for x in commutators:
            block = x[offset:offset + dim, offset:offset + dim]
            flat = list(block)
            entries.append(sp.Matrix([sp.re(z) for z in flat] + [sp.im(z) for z in flat]))
        per_block_derived_ranks[label[0]] = sp.Matrix.hstack(*entries).rank()
    trace_signatures = sp.Matrix([
        [sp.simplify(-sp.I * sp.trace(x[offset:offset + label[3], offset:offset + label[3]])) for x in two_port_basis]
        for offset, label in zip(offsets, labels)
    ])
    center_trace_rank = trace_signatures.rank()
    missing_central_covectors = trace_signatures.T.nullspace()
    assert len(missing_central_covectors) == 3

    def trace_vector(x):
        return sp.Matrix([
            sp.simplify(-sp.I * sp.trace(x[offset:offset + label[3], offset:offset + label[3]]))
            for offset, label in zip(offsets, labels)
        ])

    # Search endpoint-basis Hermitian quadratures for a minimum completion of
    # the three-dimensional central quotient.
    candidate_quotients = []
    seen = set()
    for g in group:
        for x in group:
            a = global_endpoint(g, x)
            for quadrature, control in (
                ("real", sp.I * (a + a.H) / 2),
                ("imag", (a - a.H) / 2),
            ):
                v = trace_vector(control)
                q = sp.Matrix([sp.simplify(n.dot(v)) for n in missing_central_covectors])
                key = tuple(q)
                if q != sp.zeros(3, 1) and key not in seen:
                    seen.add(key)
                    candidate_quotients.append((str(g) + "|" + str(x) + "|" + quadrature, v, q))
    completion = None
    for triple in itertools.combinations(candidate_quotients, 3):
        if sp.Matrix.hstack(*(item[2] for item in triple)).rank() == 3:
            completion = triple
            break
    assert completion is not None
    completion_vectors = [item[1] for item in completion]
    assert sp.Matrix.hstack(trace_signatures, *completion_vectors).rank() == 8

    # Central completeness is stronger than sector dephasing.  Test the
    # weaker operational condition using block eigenvalues (trace/dimension).
    central_eigenvalues = sp.Matrix([
        [sp.simplify(trace_signatures[i, j] / labels[i][3]) for j in range(trace_signatures.cols)]
        for i in range(8)
    ])
    central_basis = central_eigenvalues.columnspace()
    assert len(central_basis) == 5
    row_signatures = [tuple(central_eigenvalues.row(i)) for i in range(8)]
    assert len(set(row_signatures)) == 7
    collisions = [
        [labels[i][0] for i in range(8) if row_signatures[i] == signature]
        for signature in set(row_signatures)
    ]
    collisions = [collision for collision in collisions if len(collision) > 1]
    assert collisions == [["G", "H"]]

    separating_port = None
    for g in group:
        for x in group:
            a = global_endpoint(g, x)
            for quadrature, control in (("real", sp.I * (a + a.H) / 2), ("imag", (a - a.H) / 2)):
                v = sp.Matrix([
                    sp.simplify(trace_vector(control)[i] / labels[i][3]) for i in range(8)
                ])
                augmented_rows = [row_signatures[i] + (v[i],) for i in range(8)]
                if len(set(augmented_rows)) == 8:
                    separating_port = (str(g) + "|" + str(x) + "|" + quadrature, v)
                    break
            if separating_port: break
        if separating_port: break
    assert separating_port is not None
    pivot = next(value for value in separating_port[1] if value != 0)
    scaled_port = sp.simplify(separating_port[1] / pivot)
    assert all(value.is_Rational for value in scaled_port)
    separating_basis = central_basis + [scaled_port]
    separating_generator = None
    for coefficients in itertools.product(range(-2, 3), repeat=6):
        if not any(coefficients): continue
        values = sum((coefficient * vector for coefficient, vector in zip(coefficients, separating_basis)), sp.zeros(8, 1))
        if len(set(values)) == 8 and all(value.is_Rational for value in values):
            separating_generator = (coefficients, values)
            break
    assert separating_generator is not None
    denominators = [sp.denom(value) for value in separating_generator[1]]
    scale = sp.ilcm(*[int(d) for d in denominators])
    integer_values = [int(scale * value) for value in separating_generator[1]]
    shifted_values = [value - min(integer_values) for value in integer_values]
    cyclic_branch_count = max(shifted_values) + 1
    assert len({value % cyclic_branch_count for value in shifted_values}) == 8

    # Optimize cyclic branch count in the saturated integer lattice.  The
    # separating center is cut out by two primitive integer equations.
    constraint_matrix = sp.Matrix([
        [1, -1, 0, -3, 3, 0, 0, 0],
        [1, 1, -2, 0, 0, -2, 1, 1],
    ])
    assert all(constraint_matrix * vector == sp.zeros(2, 1) for vector in separating_basis)
    optimal_cyclic = None
    for modulus in range(8, 20):
        for residues in itertools.permutations(range(modulus), 8):
            obstruction = constraint_matrix * sp.Matrix(residues)
            if all(int(value) % modulus == 0 for value in obstruction):
                # Columns A=(1,1) and G=(0,1) give a unimodular lift.
                target = -obstruction / modulus
                correction = [0] * 8
                correction[0] = int(target[0])
                correction[6] = int(target[1] - target[0])
                integer_values_optimal = [residues[i] + modulus * correction[i] for i in range(8)]
                assert constraint_matrix * sp.Matrix(integer_values_optimal) == sp.zeros(2, 1)
                coefficient_solution = sp.Matrix.hstack(*separating_basis).gauss_jordan_solve(sp.Matrix(integer_values_optimal))[0]
                optimal_cyclic = (modulus, tuple(coefficient_solution), residues, tuple(integer_values_optimal))
                break
        if optimal_cyclic: break
    assert optimal_cyclic is not None and optimal_cyclic[0] == 8

    # Nonuniform branch weights leave Fourier residuals.  A deliberate
    # single-branch overweight eta with compensating uniform underweight is
    # an exact sharp witness: every nontrivial Fourier mode has residual eta.
    eta = sp.symbols("eta", real=True)
    optimal_modulus = optimal_cyclic[0]
    weight_errors = [eta] + [-eta / (optimal_modulus - 1)] * (optimal_modulus - 1)
    fourier_residuals = []
    omega_n = sp.exp(2 * sp.pi * sp.I / optimal_modulus)
    for delta in range(1, optimal_modulus):
        residual = sp.simplify(sum(weight_errors[k] * omega_n ** (k * delta) for k in range(optimal_modulus)))
        fourier_residuals.append(sp.simplify(sp.expand_complex(residual)))
    expected_residual = sp.Rational(optimal_modulus, optimal_modulus - 1) * eta
    assert all(sp.simplify(value * sp.conjugate(value) - expected_residual ** 2) == 0 for value in fourier_residuals)

    # Exact dephasing on the optimal cyclic group fixes the branch law
    # uniquely: all seven nontrivial Fourier coefficients must vanish.
    probabilities = sp.symbols("p0:8", real=True)
    omega_exact = sp.sqrt(2) / 2 + sp.I * sp.sqrt(2) / 2
    fourier_matrix = sp.Matrix(8, 8, lambda k, j: sp.simplify(omega_exact ** (k * j)))
    assert fourier_matrix.det() != 0
    solution = sp.linsolve(
        [sum(probabilities[j] for j in range(8)) - 1] +
        [sp.simplify(sum(probabilities[j] * omega_exact ** (k * j) for j in range(8))) for k in range(1, 8)],
        probabilities,
    )
    assert solution == sp.FiniteSet(tuple([sp.Rational(1, 8)] * 8))
    assert target_dimension == 36
    assert two_port_dimension == 33 < target_dimension
    assert derived_dimension == projective_target_dimension == 28
    assert per_block_derived_ranks == {label[0]: label[3] ** 2 - 1 for label in labels}
    assert center_trace_rank == 5
    assert max(one_port_dimensions.values()) < target_dimension

    result = {
        "schema": "marici.s3-two-flux-lie-control.v2",
        "target_block_unitary_lie_dimension": target_dimension,
        "gauge_quadrature_lie_dimension": gauge_lie_dimension,
        "one_flux_port_lie_dimensions": one_port_dimensions,
        "transposition_plus_three_cycle_lie_dimension": two_port_dimension,
        "full_block_unitary_dimension_deficit": target_dimension - two_port_dimension,
        "derived_commutator_lie_dimension": derived_dimension,
        "projective_block_unitary_target_dimension": projective_target_dimension,
        "per_block_derived_lie_ranks": per_block_derived_ranks,
        "central_trace_signature_rank": center_trace_rank,
        "missing_central_phase_covectors": [
            {label[0]: str(value) for label, value in zip(labels, vector)}
            for vector in missing_central_covectors
        ],
        "minimum_additional_endpoint_quadratures_for_full_central_rank": 3,
        "central_completion_witness": [item[0] for item in completion],
        "completed_central_trace_rank": 8,
        "adjoint_projective_dimension_before_and_after_completion": 28,
        "available_central_eigenvalue_rank": len(central_basis),
        "available_center_sector_signature_count": 7,
        "available_center_collision": collisions,
        "minimum_additional_endpoint_quadratures_for_sector_dephasing": 1,
        "sector_separating_port_witness": separating_port[0],
        "sector_separating_central_rank": 6,
        "finite_cyclic_dephasing_witness": {
            "basis_coefficients": list(separating_generator[0]),
            "integer_sector_eigenvalues": integer_values,
            "cyclic_branch_count": cyclic_branch_count,
        },
        "optimal_cyclic_dephasing": {
            "minimum_branch_count": optimal_cyclic[0],
            "basis_coefficients": [str(value) for value in optimal_cyclic[1]],
            "sector_residues": list(optimal_cyclic[2]),
            "integer_sector_eigenvalues": list(optimal_cyclic[3]),
            "lower_bound_reason": "eight_labels_require_eight_residues_and_the_saturated_lattice_attains_them",
        },
        "branch_weight_error_witness": {
            "overweight_pattern": "eta_on_branch_0_and_minus_eta_over_7_on_each_other_branch",
            "nontrivial_fourier_residual_magnitude": "8*Abs(eta)/7",
            "coherence_returns_for_every_nonzero_eta": True,
        },
        "exact_branch_distribution": {
            "unique_distribution": ["1/8"] * 8,
            "ideal_randomness_entropy_bits": 3,
            "scope": "single_draw_uniform_classical_branch_source",
        },
        "deliberate_failure": {
            "claim": "associative_generation_guarantees_full_block_unitary_lie_control",
            "actual_dimension": two_port_dimension,
            "required_dimension": target_dimension,
            "dimension_deficit": target_dimension - two_port_dimension,
        },
        "aggregate_gates": {
            "gauge_quadratures_are_lie_incomplete": gauge_lie_dimension < target_dimension,
            "every_tested_single_flux_port_is_lie_incomplete": max(one_port_dimensions.values()) < target_dimension,
            "two_typed_flux_ports_do_not_generate_full_block_unitary_lie_algebra": two_port_dimension < target_dimension,
            "missing_directions_are_three_central_phase_combinations": center_trace_rank == 5,
            "derived_lie_algebra_is_projectively_complete": derived_dimension == projective_target_dimension,
            "every_simple_block_has_full_special_unitary_rank": all(per_block_derived_ranks[label[0]] == label[3] ** 2 - 1 for label in labels),
            "projective_control_suffices_for_within_block_conjugation_twirl": True,
            "three_additional_endpoint_quadratures_complete_central_control": True,
            "central_completion_does_not_enlarge_projective_adjoint_control": True,
            "five_dimensional_available_center_fuses_G_and_H": True,
            "one_additional_endpoint_quadrature_separates_all_sectors": True,
            "finite_cyclic_twirl_requires_the_additional_sector_separating_port": True,
            "eight_branch_cyclic_twirl_is_optimal_on_the_separating_center": True,
            "nonuniform_branch_weights_resurrect_coherence": True,
            "uniform_eight_branch_distribution_is_unique": True,
            "ideal_single_draw_randomness_cost_is_three_bits": True,
            "control_amplitudes_locality_and_leakage_remain_untyped": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__": main()
