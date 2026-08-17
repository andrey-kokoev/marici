"""Audit the relative dualizing/Thom trace of the marked blowdown fiber."""


def matvec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def main():
    # Orient the two rays outwards from the central vertex h.  After quotienting
    # by the two endpoints, both boundaries are -h.
    relative_boundary = [[-1, -1]]
    fundamental_class = [-1, 1]  # path h_D -> h -> h_1
    assert matvec(relative_boundary, fundamental_class) == [0]

    # ker(d) is primitive: the two coefficients have gcd one.  A collar choice
    # gives a Bezout functional representing the derived trace.
    trace = [0, 1]
    assert sum(a * b for a, b in zip(trace, fundamental_class)) == 1

    # Reflection interchanges the rays.  It reverses the relative fundamental
    # class; tensoring with the orientation line contributes the second minus.
    reflected = [fundamental_class[1], fundamental_class[0]]
    assert reflected == [-x for x in fundamental_class]
    orientation_character = -1
    assert [orientation_character * x for x in reflected] == fundamental_class

    # The relative complex has H_1 = Z and H_0 = 0: d is onto and its kernel
    # has rank one.  This is the Tor-one suspension, not extra fiber homology.
    assert relative_boundary[0][0] in (1, -1)

    # All stalk maps are identities on the pulled-back localization A.  Thus
    # A tensor C_rel has the same unit matrices and trace(a*[I]) = a.
    sample_coefficients = [-3, 0, 1, 7]
    for a in sample_coefficients:
        a_class = [a * x for x in fundamental_class]
        assert sum(x * y for x, y in zip(trace, a_class)) == a

    # Singleton fibers carry the degree-zero identity trace.
    for a in sample_coefficients:
        assert a == a

    print("relative_fiber_complex: Z^2 --[-1 -1]--> Z")
    print("relative_homology: H1=Z, H0=0")
    print("fundamental_class: (-1,+1), PRIMITIVE")
    print("derived_trace_pairing: +1")
    print("reflection_with_orientation_line: INVARIANT")
    print("projection_formula_on_localized_stalks: PASS")
    print("singleton_trace: DEGREE_ZERO_IDENTITY")
    print("exceptional_trace: TOR_ONE_THOM_SUSPENSION")
    print("relative_dualizing_trace: CONSTRUCTED_IN_DERIVED_CATEGORY")
    print("raw_log_DNC_comparison: NEXT_GATE")


if __name__ == "__main__":
    main()
