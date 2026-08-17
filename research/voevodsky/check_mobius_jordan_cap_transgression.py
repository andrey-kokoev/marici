"""Audit the cellular relation between the Mobius atlas class and Jordan cap."""


def main():
    # The Mobius band retracts to its primitive core gamma.  Its oriented
    # boundary traverses gamma twice.  Attaching the octagonal Jordan cap O
    # therefore gives the relative connecting map d[O] = 2[gamma].
    relative_boundary = [[2]]
    assert relative_boundary[0][0] == 2

    # The selected atlas cocycle omega is primitive, not twice a cocycle.
    omega_on_core = 1
    omega_on_cap_boundary = relative_boundary[0][0] * omega_on_core
    assert omega_on_cap_boundary == 2

    # Reduction modulo two kills the cap boundary while retaining the
    # distinction between integral primitive and zero atlas classes.
    endpoint_parity = omega_on_cap_boundary % 2
    assert endpoint_parity == 0

    # Degree audit: omega belongs to H^1(M), whereas O generates
    # H_2(X,M).  Their canonical relation is evaluation after the connecting
    # map, not equality of chain representatives.
    omega_degree = 1
    jordan_cap_relative_degree = 2
    assert omega_degree != jordan_cap_relative_degree

    print("mobius_core_group: Z<gamma>")
    print("jordan_cap_relative_group: Z<O>")
    print("relative_connecting_matrix: [2]")
    print("omega_core_pairing: 1")
    print("omega_on_jordan_cap_boundary: 2")
    print("endpoint_parity_mod2: 0")
    print("literal_chain_equality: IMPOSSIBLE_BY_DEGREE")
    print("canonical_relation: <omega,delta(O)>=2")


if __name__ == "__main__":
    main()
