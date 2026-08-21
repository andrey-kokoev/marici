"""Exhaustive exact site-energy falloff audit for small connected graphs."""

from itertools import permutations, product
import networkx as nx


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
    polynomial_ring = PolynomialRing(QQ, "z")
    z = polynomial_ring.fraction_field().gen()
    site_constants = [QQ(3), QQ(5), QQ(7), QQ(11)]
    edge_constants = [QQ(101), QQ(211), QQ(431), QQ(863), QQ(1733), QQ(3469)]

    graphs = [
        graph for graph in nx.graph_atlas_g()
        if 2 <= graph.number_of_nodes() <= 4 and nx.is_connected(graph)
    ]
    graph_count = 0
    vertex_count = 0
    for graph in graphs:
        graph = nx.convert_node_labels_to_integers(graph)
        edge_pairs = sorted(tuple(sorted(edge)) for edge in graph.edges())
        edges = [
            (left, right, edge_constants[index])
            for index, (left, right) in enumerate(edge_pairs)
        ]
        graph_count += 1
        for distinguished in graph.nodes():
            sites = list(site_constants[: graph.number_of_nodes()])
            sites[distinguished] = z
            integrand = graph_integrand(sites, edges)
            gap = integrand.denominator().degree() - integrand.numerator().degree()
            expected = graph.degree(distinguished) + 1
            assert gap == expected, (
                graph.number_of_nodes(),
                edge_pairs,
                distinguished,
                gap,
                expected,
            )
            vertex_count += 1
        print(
            "PASS graph",
            graph.number_of_nodes(),
            edge_pairs,
            "degrees",
            sorted(dict(graph.degree()).values()),
        )

    print("small-graph census: PASS")
    print("connected unlabeled graphs:", graph_count)
    print("distinguished vertices:", vertex_count)


main()
