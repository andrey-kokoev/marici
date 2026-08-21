"""Derive the three-mass-insertion path and audit its first pushforward."""

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


def main():
    ring = PolynomialRing(QQ, names=("x1", "w1", "w2", "w3", "x2", "y"))
    field = ring.fraction_field()
    x1, w1, w2, w3, x2, y = map(field, ring.gens())

    integrand = path_integrand([x1, w1, w2, w3, x2], [y, y, y, y])
    weighted = w1 * w2 * w3 * integrand
    reversed_integrand = integrand.subs(
        {x1: x2, x2: x1, w1: w3, w3: w1}
    )
    assert reversed_integrand == integrand

    denominator = integrand.denominator()
    numerator = integrand.numerator()
    w3_polynomial = ring.gen(3)
    print("three-insertion derivation: PASS")
    print("path reversal: PASS")
    print("numerator total degree:", numerator.degree())
    print("denominator total degree:", denominator.degree())
    print("terminal numerator degree:", numerator.degree(w3_polynomial))
    print("terminal denominator degree:", denominator.degree(w3_polynomial))

    # Every denominator depending on the terminal white-site energy is monic
    # and linear. Extract its shift from the exact factored denominator.
    factors = denominator.factor()
    terminal_factors = []
    for factor_value, multiplicity in factors:
        if factor_value.degree(w3_polynomial) > 0:
            assert multiplicity == 1
            assert factor_value.degree(w3_polynomial) == 1
            terminal_factors.append(factor_value.subs(w3=0))
    assert len(terminal_factors) == len(set(terminal_factors))
    print("terminal pole count:", len(terminal_factors))
    for shift in sorted(terminal_factors, key=str):
        print("SHIFT", shift)

    residues = []
    for shift in terminal_factors:
        residue = ((w3 + shift) * weighted).subs(w3=-shift)
        residues.append(residue)
    assert sum(residues) == 0
    reconstructed = sum(
        residue / (w3 + shift)
        for residue, shift in zip(residues, terminal_factors)
    )
    assert reconstructed == weighted
    print("terminal first-pushforward reconstruction: PASS")


main()
