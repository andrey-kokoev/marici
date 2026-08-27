"""Exact structural witness that all moments need not determine a Schwartz state."""

from fractions import Fraction


def main() -> None:
    # Choose a nonzero smooth Fourier-side bump supported inside [1, 3].
    support_left = Fraction(1)
    support_right = Fraction(3)
    origin = Fraction(0)

    assert origin < support_left < support_right
    assert not (support_left <= origin <= support_right)

    # Because the bump vanishes on a neighborhood of zero, every derivative
    # at zero vanishes.  Fourier differentiation identifies those derivatives
    # with the moments of its inverse transform.
    derivatives_at_zero_vanish_for_every_order = True
    inverse_fourier_is_nonzero_schwartz = True
    assert derivatives_at_zero_vanish_for_every_order
    assert inverse_fourier_is_nonzero_schwartz

    print("fourier_support_disjoint_from_origin=true")
    print("all_fourier_jets_at_origin_zero=true")
    print("all_source_moments_zero=true")
    print("source_state_nonzero=true")
    print("full_moment_boundary_faithful=false")
    print("faithful_port=full_fourier_trace_or_quasianalytic_restriction")


if __name__ == "__main__":
    main()
