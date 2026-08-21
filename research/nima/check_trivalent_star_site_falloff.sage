"""Exact time-order audit of the central-energy falloff of a trivalent star."""

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
    ring = PolynomialRing(QQ, names=("w", "x1", "x2", "x3", "y1", "y2", "y3"))
    field = ring.fraction_field()
    w, x1, x2, x3, y1, y2, y3 = map(field, ring.gens())
    integrand = graph_integrand(
        [w, x1, x2, x3],
        [(0, 1, y1), (0, 2, y2), (0, 3, y3)],
    )
    w_polynomial = ring.gen(0)
    degrees = (
        integrand.numerator().degree(w_polynomial),
        integrand.denominator().degree(w_polynomial),
    )
    print("trivalent-star central degrees:", degrees)
    assert degrees[1] - degrees[0] == 4
    print("trivalent-star valence falloff: PASS")
    print("central falloff: w^-4")


main()
