"""Test whether bivalent-site cubic falloff precedes the equal-edge diagonal."""

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
    ring = PolynomialRing(QQ, names=("x1", "w", "x2", "yL", "yR"))
    field = ring.fraction_field()
    x1, w, x2, yL, yR = map(field, ring.gens())
    w_polynomial = ring.gen(1)

    split = path_integrand([x1, w, x2], [yL, yR])
    split_num = split.numerator()
    split_den = split.denominator()
    split_degrees = (split_num.degree(w_polynomial), split_den.degree(w_polynomial))
    print("generic split-edge degrees:", split_degrees)

    leading_coefficient = split_num.coefficient({w_polynomial: split_degrees[0]})
    print("generic leading numerator coefficient:", factor(leading_coefficient))

    diagonal = split.subs(yR=yL)
    diagonal_degrees = (
        diagonal.numerator().degree(w_polynomial),
        diagonal.denominator().degree(w_polynomial),
    )
    print("equal-edge diagonal degrees:", diagonal_degrees)

    assert split_degrees == (1, 4)
    assert leading_coefficient != 0
    assert leading_coefficient.subs(yR=yL) != 0
    assert diagonal_degrees == (1, 4)
    assert split_den.degree(w_polynomial) - split_num.degree(w_polynomial) == 3
    print("intrinsic bivalent-site cubic falloff: PASS")
    print("equal-edge diagonal does not cause the improvement")


main()
