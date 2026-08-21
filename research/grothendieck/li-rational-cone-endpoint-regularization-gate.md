# The Möbius Li cone requires canonical endpoint regularization

## Pole theorem

Let `p` be a degree-`d` polynomial with nonzero constant and leading
coefficients, and put

`R_p(s)=p(u(s))p(u(s)^(-1))/[s(1-s)]`,

where `u(s)=(s-1)/s`.

Then `R_p` has a pole of order `d+1` at each endpoint `s=0` and `s=1`.

At zero, `u` has a simple pole while `u^(-1)` has a simple zero. Thus the
first polynomial factor has pole order `d`, the second tends to `p(0)`, and
the coboundary weight adds one pole. Reflection gives the same order at one.

## Consequence

The notation `W(R_p)` cannot silently mean evaluation by an ordinary
holomorphic Weil test-function functional. The entire rational-square cone
lies in a growing meromorphic endpoint class. A source-side positivity proof
must first construct a canonical extension of the explicit formula to that
class.

For each degree this extension must specify:

1. which endpoint principal parts are subtracted;
2. how the pole and gamma-factor terms participate in the finite part;
3. why reflection symmetry is preserved;
4. why the result agrees with the Li derivative definition;
5. why multiplication/polarization of polynomial tests is compatible with
   the regularization.

## Hard-to-vary requirement

The regularization may not be chosen separately for each polynomial or rank.
It must be one degree-compatible endpoint distribution on the full rational
test algebra. Otherwise any desired finite Toeplitz form could be installed
through counterterms.

## Falsifiers

- Dependence on a cutoff or subtraction coordinate.
- A reflection anomaly between `s=0` and `s=1`.
- Failure to reproduce a known Li coefficient or its second difference.
- Counterterms that are not compatible with polarization.
- A degree-dependent rule with no common extension.

This gate precedes arithmetic positivity. Until it is crossed, the claim that
the prime/gamma explicit formula is positive on `R_p` is not well-defined.

It is algebraically separate from any unavailable physical relative-chain
pushforward: the issue here is meromorphic endpoint extension of a scalar
arithmetic functional.
