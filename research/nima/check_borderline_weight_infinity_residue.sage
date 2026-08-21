"""Exact normalization checks for the borderline infinity coefficient."""

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


def graph_integrand(site_energies, edges):
    answer = 0
    for states in product("FRB", repeat=len(edges)):
        energies = list(site_energies)
        relations = []
        coefficient = 1
        for state, (left, right, edge_energy) in zip(states, edges):
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
    for _, _, edge_energy in edges:
        answer /= 2 * edge_energy
    return answer


def coefficient_at_infinity(rational_function, variable, power):
    numerator = rational_function.numerator()
    denominator = rational_function.denominator()
    assert denominator.degree(variable) - numerator.degree(variable) == power
    numerator_lead = numerator.coefficient({variable: numerator.degree(variable)})
    denominator_lead = denominator.coefficient({variable: denominator.degree(variable)})
    return numerator_lead / denominator_lead


def main():
    ring = PolynomialRing(QQ, names=("w", "x1", "x2", "x3", "y1", "y2", "y3"))
    field = ring.fraction_field()
    w, x1, x2, x3, y1, y2, y3 = map(field, ring.gens())
    w_polynomial = ring.gen(0)

    bivalent = graph_integrand(
        [w, x1, x2],
        [(0, 1, y1), (0, 2, y2)],
    )
    bivalent_coefficient = coefficient_at_infinity(bivalent, w_polynomial, 3)
    bivalent_expected = 2 / ((x1+y1)*(x2+y2))
    assert bivalent_coefficient == bivalent_expected
    print("bivalent borderline coefficient:", factor(bivalent_coefficient))

    trivalent = graph_integrand(
        [w, x1, x2, x3],
        [(0, 1, y1), (0, 2, y2), (0, 3, y3)],
    )
    trivalent_coefficient = coefficient_at_infinity(trivalent, w_polynomial, 4)
    trivalent_expected = 6 / ((x1+y1)*(x2+y2)*(x3+y3))
    assert trivalent_coefficient == trivalent_expected
    print("trivalent borderline coefficient:", factor(trivalent_coefficient))
    print("borderline infinity normalization: PASS")


main()
