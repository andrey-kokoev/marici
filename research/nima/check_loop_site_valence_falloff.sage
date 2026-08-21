"""Exact site-energy falloff audits for the first loop graphs."""

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


def degree_gap(rational_function, polynomial_generator):
    return (
        rational_function.denominator().degree(polynomial_generator)
        - rational_function.numerator().degree(polynomial_generator)
    )


def main():
    ring = PolynomialRing(QQ, names=("x1", "x2", "x3", "ya", "yb", "yc"))
    field = ring.fraction_field()
    x1, x2, x3, ya, yb, yc = map(field, ring.gens())

    bubble = graph_integrand([x1, x2], [(0, 1, ya), (0, 1, yb)])
    published_bubble = (
        1 / ((x1+x2)*(x1+ya+yb)*(x2+ya+yb))
        * (1/(x1+x2+2*ya) + 1/(x1+x2+2*yb))
    )
    assert bubble == published_bubble
    assert degree_gap(bubble, ring.gen(0)) == 3
    assert degree_gap(bubble, ring.gen(1)) == 3
    print("parallel-edge source formula match: PASS")
    print("parallel-edge vertex falloff: x^-3")

    triangle = graph_integrand(
        [x1, x2, x3],
        [(0, 1, ya), (1, 2, yb), (2, 0, yc)],
    )
    triangle_gaps = [degree_gap(triangle, ring.gen(index)) for index in range(3)]
    assert triangle_gaps == [3, 3, 3]
    print("triangle vertex degree gaps:", triangle_gaps)
    print("triangle valence falloff: PASS")


main()
