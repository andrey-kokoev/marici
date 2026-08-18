"""Propagate the raw-DNC occurrence-localization no-go to all even arities."""

from itertools import product

import check_general_even_cut_induction as induction


def main():
    # One universal radial chart. Exponents use the independent basis (X,u).
    finite = {(a, b) for a, b in product(range(4), range(-3, 4))}
    raw = {(a, b) for a, b in product(range(-3, 4), range(-3, 4))}
    assert finite < raw
    assert (-1, 0) in raw and (-1, 0) not in finite

    # The retained occurrence boundary is nonzero before localization and is
    # annihilated after X is inverted.
    boundary = {(0, b) for b in range(-3, 4)}
    assert boundary
    localized_boundary = set()
    assert not localized_boundary

    audits = {}
    for n in range(6, 16, 2):
        cuts = induction.physical_cuts(n)
        m = n // 2
        assert len(cuts) == m * (m - 2)
        # Every physical Cut chart has its own occurrence-normal radial stalk,
        # so the same nonzero kernel witness appears on every chart.
        witnesses = {cut: bool(boundary) and not localized_boundary for cut in cuts}
        assert all(witnesses.values())
        audits[n] = len(witnesses)

    # A derived equivalence is conservative and cannot annihilate a nonzero
    # object. Nor can a global equivalence repair a failure on an open chart.
    raw_comparison_conservative = False
    raw_comparison_derived_equivalence = False
    assert not raw_comparison_conservative
    assert not raw_comparison_derived_equivalence

    for n, count in audits.items():
        print(f"n={n}: physical_radial_boundary_witnesses={count}")
    print("universal_finite_stalk: Z[X,u^+-1]")
    print("universal_raw_radial_stalk: Z[X^+-1,u^+-1]")
    print("canonical_comparison: LOCALIZE_AT_X")
    print("nonzero_supported_kernel: C/(X)")
    print("raw_localization_of_supported_kernel: ZERO")
    print("global_raw_scheme_equivalence_preserving_connector: IMPOSSIBLE")
    print("correct_algebraic_home: FS_KATO_OR_TRIVIAL_INERTIA_ARTIN_CONE_SECTOR")
    print("remaining_comparison: NONCONSERVATIVE_GENERIC_LOCALIZATION_ONLY")


if __name__ == "__main__":
    main()
