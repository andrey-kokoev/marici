"""Exact infinity-jet audit for a generic bivalent source site."""

from itertools import permutations, product


def linear_extensions(vertex_count, relations):
    for order in permutations(range(vertex_count)):
        position = {vertex: index for index, vertex in enumerate(order)}
        if all(position[left] < position[right] for left, right in relations):
            yield order


def ordered_time_integral(energies, order):
    value = 1
    for start in range(len(order)):
        value /= sum(energies[order[index]] for index in range(start, len(order)))
    return value


def path_integrand(site_energies, edge_energies):
    answer = 0
    for states in product("FRB", repeat=len(edge_energies)):
        energies = list(site_energies)
        relations = []
        coefficient = 1
        for left, (state, edge_energy) in enumerate(zip(states, edge_energies)):
            right = left + 1
            if state == "F":
                relations.append((left, right))
                energies[left] -= edge_energy
                energies[right] += edge_energy
            elif state == "R":
                relations.append((right, left))
                energies[left] += edge_energy
                energies[right] -= edge_energy
            else:
                coefficient *= -1
                energies[left] += edge_energy
                energies[right] += edge_energy
        for order in linear_extensions(len(site_energies), relations):
            answer += coefficient * ordered_time_integral(energies, order)
    for edge_energy in edge_energies:
        answer /= 2 * edge_energy
    return answer


def leading_coefficient_at_infinity(value, variable):
    numerator = value.numerator()
    denominator = value.denominator()
    numerator_degree = numerator.degree(variable)
    denominator_degree = denominator.degree(variable)
    numerator_lead = numerator.coefficient({variable: numerator_degree})
    denominator_lead = denominator.coefficient({variable: denominator_degree})
    return numerator_lead / denominator_lead, denominator_degree - numerator_degree


def first_three_normalized_coefficients(integrand, variable, site_energy):
    normalized = site_energy**3 * integrand
    c0, gap0 = leading_coefficient_at_infinity(normalized, variable)
    assert gap0 == 0
    residual1 = normalized - c0
    c1, gap1 = leading_coefficient_at_infinity(residual1, variable)
    assert gap1 == 1
    residual2 = residual1 - c1/site_energy
    c2, gap2 = leading_coefficient_at_infinity(residual2, variable)
    assert gap2 == 2
    return c0, c1, c2


def main():
    ring = PolynomialRing(QQ, names=("w", "x1", "x2", "y1", "y2"))
    field = ring.fraction_field()
    w, x1, x2, y1, y2 = map(field, ring.gens())
    w_polynomial = ring.gen(0)
    integrand = path_integrand([x1, w, x2], [y1, y2])

    c0, c1, c2 = first_three_normalized_coefficients(
        integrand, w_polynomial, w
    )

    print("C0", factor(c0))
    print("C1", factor(c1))
    print("C2", factor(c2))

    for excess, coefficient in enumerate((c0, c1, c2)):
        weighted = w**(2+excess) * integrand
        subtraction = sum(
            (c0, c1, c2)[index] * w**(excess-1-index)
            for index in range(excess)
        )
        remainder = weighted - subtraction
        residue_coefficient, residue_gap = leading_coefficient_at_infinity(
            remainder, w_polynomial
        )
        assert residue_gap == 1
    assert residue_coefficient == coefficient
    print("supercritical infinity jet through excess two: PASS")

    # First two grades of the edge-deletion jet recursion.  Deleting either
    # incident edge leaves a two-site component and one shifted singleton.
    common = 1 / ((x1+y1)*(x2+y2))
    a0_left = common
    a1_left = -(x2+y2) * common
    a0_right = common
    a1_right = -(x1+y1) * common
    other_site_sum = x1 + x2
    recursive_c0 = a0_left + a0_right
    recursive_c1 = (
        a1_left - (other_site_sum + 2*y1)*a0_left
        + a1_right - (other_site_sum + 2*y2)*a0_right
    )
    assert recursive_c0 == c0
    assert recursive_c1 == c1
    print("edge-deletion jet recursion through C1: PASS")

    diagonal_integrand = integrand.subs(y2=y1)
    diagonal_coefficients = first_three_normalized_coefficients(
        diagonal_integrand, w_polynomial, w
    )
    restricted_coefficients = tuple(
        coefficient.subs(y2=y1) for coefficient in (c0, c1, c2)
    )
    assert diagonal_coefficients == restricted_coefficients
    print("mass diagonal commutes with infinity jet through C2: PASS")

    expected_boundary_gate = (x1+y1)*(x2+y2)
    for coefficient in (c0, c1, c2):
        denominator_unit = coefficient.denominator() / expected_boundary_gate
        assert denominator_unit != 0
        assert all(denominator_unit.derivative(variable) == 0
                   for variable in (w, x1, x2, y1, y2))
    assert expected_boundary_gate.subs(y2=y1) != 0
    print("jet base-change gate is the neighboring total-energy boundary: PASS")

    left_boundary_residue = ((x1+y1)*integrand).subs(x1=-y1)
    left_boundary_lead, left_boundary_gap = leading_coefficient_at_infinity(
        left_boundary_residue, w_polynomial
    )
    assert left_boundary_gap == 3
    assert left_boundary_lead == 2/(x2+y2)
    left_residue_coefficients = first_three_normalized_coefficients(
        left_boundary_residue, w_polynomial, w
    )
    left_coefficient_residues = tuple(
        ((x1+y1)*coefficient).subs(x1=-y1)
        for coefficient in (c0, c1, c2)
    )
    assert left_residue_coefficients == left_coefficient_residues

    right_boundary_residue = ((x2+y2)*integrand).subs(x2=-y2)
    right_residue_coefficients = first_three_normalized_coefficients(
        right_boundary_residue, w_polynomial, w
    )
    right_coefficient_residues = tuple(
        ((x2+y2)*coefficient).subs(x2=-y2)
        for coefficient in (c0, c1, c2)
    )
    assert right_residue_coefficients == right_coefficient_residues
    print("total-energy Gysin commutes with infinity jet through C2: PASS")

    corner_residue = (
        (x1+y1)*(x2+y2)*integrand
    ).subs({x1: -y1, x2: -y2})
    corner_lead, corner_gap = leading_coefficient_at_infinity(
        corner_residue, w_polynomial
    )
    assert corner_gap == 3
    assert corner_lead == 2
    channel_plus = (y1+y2)**2
    channel_minus = (y1-y2)**2
    assert corner_residue == 2*w / (
        (w**2-channel_plus)*(w**2-channel_minus)
    )
    iterated_coefficient_residues = tuple(
        ((x1+y1)*(x2+y2)*coefficient).subs({x1: -y1, x2: -y2})
        for coefficient in (c0, c1, c2)
    )
    assert iterated_coefficient_residues == (2, 0, 4*y1**2 + 4*y2**2)
    corner_normalized_remainder = w**3*corner_residue - 2
    corner_c2, corner_c2_gap = leading_coefficient_at_infinity(
        corner_normalized_remainder, w_polynomial
    )
    assert corner_c2_gap == 2
    assert corner_c2 == 4*y1**2 + 4*y2**2
    expected_corner_c4 = 2*(
        channel_plus**2 + channel_plus*channel_minus + channel_minus**2
    )
    corner_c4_remainder = (
        w**3*corner_residue - 2 - corner_c2/w**2
    )
    corner_c4, corner_c4_gap = leading_coefficient_at_infinity(
        corner_c4_remainder, w_polynomial
    )
    assert corner_c4_gap == 4
    assert corner_c4 == expected_corner_c4
    print("iterated Gysin kills C1 and preserves C0,C2: PASS")
    print("corner even-jet recurrence through C4: PASS")

    mass_corner = corner_residue.subs(y2=y1)
    assert mass_corner == 2 / (w*(w**2-4*y1**2))
    mass_corner_normalized = w**3*mass_corner
    assert leading_coefficient_at_infinity(
        mass_corner_normalized-2, w_polynomial
    ) == (8*y1**2, 2)
    assert leading_coefficient_at_infinity(
        mass_corner_normalized-2-8*y1**2/w**2, w_polynomial
    ) == (32*y1**4, 4)
    print("mass diagonal collapses the corner jet to one quadratic channel: PASS")

    signed_mass_corner = corner_residue.subs(y2=-y1)
    assert signed_mass_corner == mass_corner
    assert channel_plus.subs(y2=-y2) == channel_minus
    assert channel_minus.subs(y2=-y2) == channel_plus
    assert corner_residue.subs(y2=-y2) == corner_residue
    print("edge-sign reversal exchanges the two corner channels: PASS")

    channel_sum = channel_plus + channel_minus
    channel_product = channel_plus * channel_minus
    channel_discriminant = channel_sum**2 - 4*channel_product
    assert channel_sum == 2*(y1**2+y2**2)
    assert channel_product == (y1**2-y2**2)**2
    assert channel_discriminant == 16*y1**2*y2**2
    assert channel_product.subs(y2=y1) == 0
    assert channel_discriminant.subs(y2=y1) == 16*y1**4
    print("scalar corner jet factors through the symmetric channel quotient: PASS")

    readout_c2 = 2*channel_sum
    readout_c4 = 2*(channel_sum**2-channel_product)
    reconstructed_sum = readout_c2/2
    reconstructed_product = reconstructed_sum**2-readout_c4/2
    assert reconstructed_sum == channel_sum
    assert reconstructed_product == channel_product
    print("C2 and C4 reconstruct the unordered channel pair: PASS")

    first_pair = (QQ(0), QQ(25))
    second_pair = (QQ(9), QQ(16))
    assert sum(first_pair) == sum(second_pair)
    assert 2*sum(first_pair) == 2*sum(second_pair) == 50
    first_c4 = 2*(sum(first_pair)**2-first_pair[0]*first_pair[1])
    second_c4 = 2*(sum(second_pair)**2-second_pair[0]*second_pair[1])
    assert first_c4 == 1250
    assert second_c4 == 962
    assert first_c4 != second_c4
    print("C2 alone is insufficient while C2,C4 are sufficient: PASS")

    quotient_jacobian = matrix([
        [1, 1],
        [channel_minus, channel_plus],
    ]).det()
    assert quotient_jacobian == channel_plus-channel_minus
    source_readout_jacobian = matrix([
        [diff(channel_sum, y1), diff(channel_sum, y2)],
        [diff(channel_product, y1), diff(channel_product, y2)],
    ]).det()
    assert source_readout_jacobian == (
        -32*y1*y2*(y1**2-y2**2)
    )
    assert quotient_jacobian.subs(y2=y1) == 4*y1**2
    assert source_readout_jacobian.subs(y2=y1) == 0
    print("lens quotient is smooth but source parametrization ramifies on mass diagonal: PASS")

    mean_edge = (y1+y2)/2
    edge_difference = y1-y2
    assert channel_sum == 4*mean_edge**2 + edge_difference**2
    assert channel_product == 4*mean_edge**2 * edge_difference**2
    assert readout_c2 == 8*mean_edge**2 + 2*edge_difference**2
    assert readout_c4 == (
        32*mean_edge**4
        + 8*mean_edge**2*edge_difference**2
        + 2*edge_difference**4
    )
    print("physical mass departure first appears at second normal grade: PASS")

    auxiliary_ring = PolynomialRing(QQ, names=("AA", "BB", "zz"))
    auxiliary_field = auxiliary_ring.fraction_field()
    AA, BB, zz = map(auxiliary_field, auxiliary_ring.gens())
    corner_generating_function = 2 / ((1-AA*zz**2)*(1-BB*zz**2))
    physical_generating_function = corner_generating_function.subs(BB=0)
    assert corner_generating_function.derivative(BB).subs(BB=0) == (
        zz**2 * physical_generating_function
    )
    print("second-normal deformation is the even-grade shift operator: PASS")
    for normal_order in range(9):
        derivative = corner_generating_function
        for _ in range(normal_order):
            derivative = derivative.derivative(BB)
        assert derivative.subs(BB=0) == (
            factorial(normal_order)
            * zz**(2*normal_order)
            * physical_generating_function
        )
    print("all normal derivatives are divided powers of the grade shift: PASS")

    connection_a = zz**2 / (1-AA*zz**2)
    connection_b = zz**2 / (1-BB*zz**2)
    assert corner_generating_function.derivative(AA) == (
        connection_a * corner_generating_function
    )
    assert corner_generating_function.derivative(BB) == (
        connection_b * corner_generating_function
    )
    mixed_curvature = (
        connection_b.derivative(AA)
        - connection_a.derivative(BB)
    )
    assert mixed_curvature == 0
    assert (
        corner_generating_function.derivative(AA).derivative(BB)
        == corner_generating_function.derivative(BB).derivative(AA)
    )
    print("mean-mass and unequal-mass jet transport is flat: PASS")

    trivializing_gauge = (1-AA*zz**2)*(1-BB*zz**2)
    assert trivializing_gauge * corner_generating_function == 2
    pole_a = 1/zz**2
    pole_b = 1/zz**2
    residue_a = ((AA-pole_a)*connection_a).subs(AA=pole_a)
    residue_b = ((BB-pole_b)*connection_b).subs(BB=pole_b)
    assert residue_a == -1
    assert residue_b == -1
    print("formal jet connection is pure gauge with integral residues: PASS")

    small_root = y1-y2
    large_root = y1+y2
    small_plus_residue = ((w-small_root)*corner_residue).subs(w=small_root)
    small_minus_residue = ((w+small_root)*corner_residue).subs(w=-small_root)
    large_plus_residue = ((w-large_root)*corner_residue).subs(w=large_root)
    large_minus_residue = ((w+large_root)*corner_residue).subs(w=-large_root)
    assert small_plus_residue == 1/(channel_minus-channel_plus)
    assert small_minus_residue == small_plus_residue
    assert large_plus_residue == 1/(channel_plus-channel_minus)
    assert large_minus_residue == large_plus_residue
    assert (
        small_plus_residue + small_minus_residue
        + large_plus_residue + large_minus_residue
    ) == 0
    physical_central_residue = (w*mass_corner).subs(w=0)
    assert physical_central_residue == -1/(2*y1**2)
    assert (
        (small_plus_residue+small_minus_residue).subs(y2=y1)
        == physical_central_residue
    )
    assert small_plus_residue-small_minus_residue == 0
    print("small-pole cycle trace survives while anti-trace is annihilated: PASS")

    deck_swap = matrix(QQ, [[0, 1], [1, 0]])
    cycle_transfer = matrix(QQ, [[1], [1]])
    cycle_specialization = matrix(QQ, [[1/2, 1/2]])
    invariant_projector = (identity_matrix(QQ, 2) + deck_swap)/2
    assert cycle_specialization * cycle_transfer == identity_matrix(QQ, 1)
    assert cycle_transfer * cycle_specialization == invariant_projector
    assert invariant_projector**2 == invariant_projector
    assert invariant_projector * matrix(QQ, [[1], [-1]]) == 0
    generic_residue_pairing = matrix(
        field, [[small_plus_residue, small_minus_residue]]
    )
    central_residue_pairing = matrix(
        field, [[2*small_plus_residue]]
    )
    assert (
        central_residue_pairing * cycle_specialization
        == generic_residue_pairing
    )
    print("cycle trace-transfer projector preserves the residue pairing: PASS")

    field_two = GF(2)
    deck_swap_two = matrix(field_two, [[0, 1], [1, 0]])
    deck_norm_two = identity_matrix(field_two, 2) + deck_swap_two
    transfer_two = matrix(field_two, [[1], [1]])
    trace_two = matrix(field_two, [[1, 1]])
    assert deck_norm_two.rank() == 1
    assert deck_norm_two**2 == zero_matrix(field_two, 2)
    assert trace_two * transfer_two == zero_matrix(field_two, 1)
    assert matrix(field_two, [[1], [-1]]) == transfer_two
    print("characteristic two destroys the normalized deck splitting: PASS")

    for deck_prime in (2, 3, 5, 7):
        rational_shift = matrix(QQ, deck_prime, deck_prime)
        for index in range(deck_prime):
            rational_shift[(index+1) % deck_prime, index] = 1
        rational_norm = sum(
            (rational_shift**power for power in range(deck_prime)),
            zero_matrix(QQ, deck_prime)
        )
        rational_projector = rational_norm/deck_prime
        assert rational_projector.rank() == 1
        assert rational_projector**2 == rational_projector

        residue_field = GF(deck_prime)
        modular_shift = rational_shift.change_ring(residue_field)
        modular_identity = identity_matrix(residue_field, deck_prime)
        modular_unipotent = modular_shift-modular_identity
        modular_norm = sum(
            (modular_shift**power for power in range(deck_prime)),
            zero_matrix(residue_field, deck_prime)
        )
        assert modular_unipotent**deck_prime == 0
        assert modular_norm == modular_unipotent**(deck_prime-1)
        assert modular_norm.rank() == 1
        assert modular_norm**2 == zero_matrix(residue_field, deck_prime)
        modular_transfer = matrix(
            residue_field, deck_prime, 1, [1]*deck_prime
        )
        modular_trace = matrix(
            residue_field, 1, deck_prime, [1]*deck_prime
        )
        assert (
            modular_trace*modular_transfer
            == zero_matrix(residue_field, 1)
        )
    print("prime cyclic deck traces split over Q and become nilpotent mod p: PASS")

    for deck_order in range(2, 13):
        rational_shift = matrix(QQ, deck_order, deck_order)
        for index in range(deck_order):
            rational_shift[(index+1) % deck_order, index] = 1
        rational_norm = sum(
            (rational_shift**power for power in range(deck_order)),
            zero_matrix(QQ, deck_order)
        )
        assert rational_norm**2 == deck_order*rational_norm
        assert (rational_norm/deck_order)**2 == rational_norm/deck_order
        for bad_prime in prime_divisors(deck_order):
            residue_field = GF(bad_prime)
            modular_norm = rational_norm.change_ring(residue_field)
            assert modular_norm.rank() == 1
            assert modular_norm**2 == zero_matrix(residue_field, deck_order)
    print("composite cyclic deck norms detect exactly their order primes: PASS")


main()
