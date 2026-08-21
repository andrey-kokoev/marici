"""Exact univariate central-energy audit for a valence-four star."""

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


def star_integrand(center_energy, leaf_energies, edge_energies):
    site_energies = [center_energy] + list(leaf_energies)
    answer = 0
    for states in product("FRB", repeat=len(edge_energies)):
        energies = list(site_energies)
        relations = []
        coefficient = 1
        for leaf, (state, edge_energy) in enumerate(zip(states, edge_energies), 1):
            if state == "F":
                relations.append((0, leaf))
                energies[0] -= edge_energy
                energies[leaf] += edge_energy
            elif state == "R":
                relations.append((leaf, 0))
                energies[0] += edge_energy
                energies[leaf] -= edge_energy
            else:
                coefficient *= -1
                energies[0] += edge_energy
                energies[leaf] += edge_energy
        for order in linear_extensions(len(site_energies), relations):
            answer += coefficient * ordered_time_integral(energies, order)
    for edge_energy in edge_energies:
        answer /= 2 * edge_energy
    return answer


def main():
    polynomial_ring = PolynomialRing(QQ, "w")
    w = polynomial_ring.fraction_field().gen()
    # Pairwise-distinct primes avoid accidental connected-energy collisions.
    integrand = star_integrand(
        w,
        [QQ(3), QQ(5), QQ(7), QQ(11)],
        [QQ(101), QQ(211), QQ(431), QQ(863)],
    )
    numerator_degree = integrand.numerator().degree()
    denominator_degree = integrand.denominator().degree()
    print("valence-four central degrees:", numerator_degree, denominator_degree)
    assert denominator_degree - numerator_degree == 5
    print("valence-four star falloff: PASS")
    print("central falloff: w^-5")


main()
