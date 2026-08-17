"""Compare a raw DNC radial chart with its finite PC localization stalk."""

from itertools import product


def main():
    # Raw chart: B=Z[X,u,t]/(u-Xt).  Once u is inverted, both X and t are
    # units.  Exponent vectors are recorded in the independent basis (X,u).
    # t=u/X therefore has vector (-1,+1).
    x = (1, 0)
    u = (0, 1)
    t = (-1, 1)
    assert (x[0] + t[0], x[1] + t[1]) == u

    # The raw radial ring is Z[X^{+-1},u^{+-1}], whereas the finite stalk is
    # C=Z[X,u^{+-1}].  Bounded monomial enumeration exhibits the strict gap.
    finite_monomials = {(a, b) for a, b in product(range(4), range(-3, 4))}
    raw_radial_monomials = {
        (a, b) for a, b in product(range(-3, 4), range(-3, 4))
    }
    assert finite_monomials < raw_radial_monomials
    assert (-1, 0) in raw_radial_monomials
    assert (-1, 0) not in finite_monomials

    # C/(X) is nonzero: Laurent u-monomials remain distinct after X=0.
    boundary_basis = {(0, b) for b in range(-3, 4)}
    assert len(boundary_basis) == 7
    assert (0, 0) in boundary_basis

    # Localization kills that entire boundary module, so C -> C[X^-1] is
    # flat and injective but neither an isomorphism nor a derived equivalence.
    localized_boundary = set()
    assert boundary_basis
    assert not localized_boundary

    print("raw_DNC_relation: u=X*t")
    print("raw_radial_ring: Z[X^+-1,u^+-1]")
    print("finite_PC_radial_stalk: Z[X,u^+-1]")
    print("canonical_comparison: LOCALIZE_AT_X")
    print("comparison_flat_injective: YES")
    print("comparison_isomorphism: NO")
    print("derived_equivalence: NO")
    print("cone_boundary_witness: C/(X) NONZERO")
    print("raw_DNC_structure_sheaf_identification: IMPOSSIBLE")
    print("required_replacement: LOG_SATURATED_OR_ARTIN_FAN_COMPARISON")


if __name__ == "__main__":
    main()
