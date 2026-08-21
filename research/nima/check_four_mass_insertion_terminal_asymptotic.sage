"""Exact univariate audit of the four-insertion terminal asymptotic."""

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


def path_integrand(site_energies, edge_energy):
    edge_count = len(site_energies) - 1
    answer = 0
    for states in product("FRB", repeat=edge_count):
        energies = list(site_energies)
        relations = []
        coefficient = 1
        for left, state in enumerate(states):
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
    answer /= (2 * edge_energy) ** edge_count
    return answer


def main():
    polynomial_ring = PolynomialRing(QQ, "w4")
    w4 = polynomial_ring.fraction_field().gen()
    # Distinct positive primes avoid accidental collisions among interval sums.
    integrand = path_integrand([3, 5, 7, 11, w4, 23], QQ(17))
    numerator_degree = integrand.numerator().degree()
    denominator_degree = integrand.denominator().degree()
    print("observed terminal degrees:", numerator_degree, denominator_degree)
    assert (numerator_degree, denominator_degree) == (7, 10)
    assert denominator_degree - numerator_degree == 3
    weighted = w4 * integrand
    assert weighted.denominator().degree() - weighted.numerator().degree() == 2
    print("four-insertion exact univariate derivation: PASS")
    print("terminal degrees:", numerator_degree, denominator_degree)
    print("unweighted terminal falloff: w4^-3")
    print("weighted terminal residue at infinity: zero")


main()
