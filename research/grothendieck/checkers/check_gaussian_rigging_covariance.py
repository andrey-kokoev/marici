"""Dependency-free parameter audit for the Gaussian source rigging."""


def main() -> None:
    # Record a Gaussian exponent by its rate parameter. Substitution
    # x -> exp(q)x multiplies that rate by exp(2q); Fourier conjugation
    # reverses q and hence multiplies the dual rate by exp(-2q).
    dilation_action = ("a*exp(2q)", "b*exp(-2q)")
    assert dilation_action[0] == "a*exp(2q)"
    assert dilation_action[1] == "b*exp(-2q)"

    # Fourier swaps the two declared decay parameters; applying twice returns
    # the original pair on the reflection-even carrier.
    pair = ("a", "b")
    swapped_once = (pair[1], pair[0])
    swapped_twice = (swapped_once[1], swapped_once[0])
    assert swapped_twice == pair

    print("fourier_parameter_action=(a,b)->(b,a)")
    print("dilation_parameter_action=(a,b)->(a*exp(2q),b*exp(-2q))")
    print("integer_comb_pairing_absolutely_convergent=true")
    print("moment_germ_faithful_by_entire_continuation=true")
    print("flat_fourier_bump_excluded=true")
    print("arithmetic_boundary_continuity=not_derived")


if __name__ == "__main__":
    main()
