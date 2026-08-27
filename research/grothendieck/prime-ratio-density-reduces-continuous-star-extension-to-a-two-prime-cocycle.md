# Prime-ratio density reduces continuous star extension to a two-prime cocycle

## Existing seam detector

For the continuous interval port

\[
B_\ell^+(z)=\int_0^\ell A(v)e^{izv}\,dv,
\]

define the reciprocal-versus-adjoint star defect

\[
\mathfrak S_\ell(z)
=
B_\ell^+(-z)-B_\ell^+(-\overline z).
\]

The staircase Green theorem already proves that if this defect vanishes for
every positive `ell` and `A` is nonzero on an interval, then `z` is real in
the centered coordinate, hence the spectral point lies on the critical seam.

The missing step was extension from discrete arithmetic boundary data to the
whole interval family.

## Density theorem

The set

\[
\{\log p-\log q:p,q\in\mathbb P\}
\]

is dense in the real line.

To see this, fix a positive target `r` and put `lambda=exp(r)`. Choose primes
`q` tending to infinity. The prime number theorem implies that for every
positive relative tolerance there is, for all sufficiently large `q`, a prime
`p` in the corresponding relative interval around `lambda q`. Hence
`p/q` tends to `lambda` and `log(p/q)` tends to `r`. Negative targets follow
by exchanging `p` and `q`, and zero is obtained along `p=q`.

## Continuous-extension consequence

For fixed `z`, the map

\[
\ell\longmapsto\mathfrak S_\ell(z)
\]

is continuous. Therefore

\[
\mathfrak S_{\log p-\log q}(z)=0
\quad\text{for every prime pair with }p>q
\]

implies

\[
\mathfrak S_\ell(z)=0
\quad\text{for every }\ell\ge0.
\]

The continuous staircase seam detector then forces the critical seam.

## What this changes

One does not need to reconstruct arbitrary interval values from isolated
prime-power samples by interpolation. It is enough to derive star compatibility
on the prime-ratio comparison cells already created by the two-prime moving
seam cocycle. Density and continuity perform the extension uniquely.

This moves the hard bridge down one categorical rung:

1. scalar zero supplies a completed two-prime comparison packet;
2. the shared-corner cocycle forces reciprocal--adjoint equality on each
   prime-ratio length;
3. prime-ratio density extends equality to the continuous interval port;
4. the staircase derivative forces the seam.

Only step 2 remains genuinely unproved.

## Quantitative form

If the star defect is locally Lipschitz with constant `L` and a finite
prime-ratio set is a `delta`-net on a compact scale interval, then

\[
\sup_\ell|\mathfrak S_\ell|
\le
\max_{r\text{ in the net}}|\mathfrak S_r|+L\delta.
\]

Thus approximate finite compatibility has a canonical error budget. Exact
compatibility on the growing dense family gives exact continuous closure.

## Hostile test

The positive two-atom source must fail step 2. It can satisfy every individual
moving-seam identity, but at its off-seam zero the continuous star-defect
derivative is nonzero on source-positive intervals. Hence it cannot have zero
star defect on a dense prime-ratio family.

This is the desired pre-scalar discriminator if—and only if—the zero-state
two-prime cocycle actually implies those discrete star equalities.

## Disposition

The next target is now finite and algebraic: express the shared `pq` moving
window in reciprocal and adjoint orders, and compute their difference on a
scalar-null constructor state. Equality on every prime pair would complete the
discrete-to-continuous bridge; one nonzero typed coefficient would falsify it.
