# The affine-filler theorem stops at the source-decay map

## Result accepted

Voevodsky's conditional descent theorem closes the finite affine-homology branch. Given coefficients in

\[
B_\epsilon=\left\{c:\sum_r |c_r|H(r)^\epsilon<\infty\right\}
\]

and an orbit with \(|\operatorname{Re}w|<\epsilon\), cutoff evaluations converge uniformly and boundary-null relations pass to completion.

## Arithmetic applicability gate

Application to the theta/zeta construction requires a source-derived map

\[
\iota:\text{theta/Euler source}\longrightarrow B_\epsilon
\]

that identifies the labels `r`, the height `H(r)`, and the coefficients `c_r`. No such map is supplied by the abstract completion theorem.

The distinction between two expansions is decisive:

- Gaussian theta terms can decay rapidly for each fixed positive geometric parameter.
- The unsmoothed Dirichlet expansion of zeta has coefficients `c_n=1`. With `H(n)=n`, its proposed weighted norm contains \(\sum_n n^\epsilon\), which diverges for every positive \(\epsilon\).

Thus rapid decay of a theta kernel cannot be silently transferred to Euler or Dirichlet coefficients after Mellin transformation. Such a transfer requires an explicit transform theorem with its domain and norm estimate.

## Endpoint-width gate

Even when a weighted embedding exists, its exponent must satisfy \(\epsilon>|\operatorname{Re}w|\) for the intended reciprocal orbit. Existence of some narrow decay strip does not reach an independently prescribed modular endpoint.

## Disposition

The affine filler and its conditional completion are settled at source-typed strength. The next arithmetic task is to materialize `iota` and prove its weighted norm bound for the actual coefficients. Until then the theorem has no RH implication and does not provide a global spectral filler.
