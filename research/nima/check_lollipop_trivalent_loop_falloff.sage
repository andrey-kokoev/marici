"""Exact trivalent-site falloff audit on a triangle with an attached leaf."""

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


def main():
    polynomial_ring = PolynomialRing(QQ, "w")
    w = polynomial_ring.fraction_field().gen()
    # Vertex 0 lies on the triangle and carries the attached leaf: valence 3.
    integrand = graph_integrand(
        [w, QQ(3), QQ(5), QQ(7)],
        [
            (0, 1, QQ(101)),
            (1, 2, QQ(211)),
            (2, 0, QQ(431)),
            (0, 3, QQ(863)),
        ],
    )
    numerator_degree = integrand.numerator().degree()
    denominator_degree = integrand.denominator().degree()
    print("loop-trivalent central degrees:", numerator_degree, denominator_degree)
    assert denominator_degree - numerator_degree == 4
    print("loop-trivalent falloff: PASS")
    print("central falloff: w^-4")


main()
