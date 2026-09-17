# Classical zero-free-region PNT cannot produce the required asymptotic threshold

Put `x=log N`.  After the `n^{-1/2}` edge weighting, a classical
zero-free-region remainder has scale

\[
R(N)=\sqrt N\,e^{-c\sqrt{\log N}}
     =\exp(x/2-c\sqrt x).
\]

For every fixed `c>0` and every polylogarithmic power `k>=0`,

\[
{R(N)\over(\log N)^k}
={\exp(x/2-c\sqrt x)\over x^k}\longrightarrow\infty.
\]

Indeed, its logarithm is

\[
x/2-c\sqrt x-k\log x,
\]

whose linear term dominates the square-root and logarithmic terms.  Therefore
no `N0` can make this remainder permanently smaller than an edge margin that
grows or decays only by powers of `log N`.

This excludes the standard zero-free-region PNT as an input to Gate 6; it does
not exclude cancellation in the signed weighted Hankel operator.  Such
cancellation is precisely the new RH-strength arithmetic theorem still
required.  The executable symbolic regression is
`check_zero_free_region_remainder_cannot_supply_asymptotic_N0.py`.
