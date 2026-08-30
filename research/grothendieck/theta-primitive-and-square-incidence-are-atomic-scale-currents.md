# Theta primitive and square incidence are atomic scale currents

## Source-derived incidence map

The prime-Fock connected label is a pair `(p,k)`.  Its canonical scale is

\[
 q_{p,k}=k\log p.
\]

Before spectral evaluation, define the positive atomic scale current

\[
 \mu_k=\frac1k\sum_p p^{-k/2}\delta_{k\log p}.
\]

The oriented Tate boundary value is recovered by the odd character readout

\[
 C_k(t)=2i\int_0^\infty\sin(tq)\,d\mu_k(q)
 =\frac{2i}{k}\sum_pp^{-k/2}\sin(kt\log p).
\]

Thus the missing boundary incidence operation is not a fitted scalar phase.
It is the pushforward

\[
 I_k:(p,k)\longmapsto
 \frac1k p^{-k/2}\delta_{k\log p}
\]

from the prime-Fock occupation module to atomic currents on the common scale
axis.

The requested operations are

\[
 P=I_1,
 \qquad
 Q=I_2.
\]

## Finite-cutoff exactness

At prime cutoff `X`, put

\[
 \mu_{k,X}=\frac1k\sum_{p\le X}p^{-k/2}\delta_{k\log p}.
\]

Then the readouts of `mu_(1,X)` and `mu_(2,X)` are exactly the two
countercurrents in the finite Tate factorization.  No continuation or zero
data enters, and reassembly with the `k>=3` tail recovers every local
transition.

## Completion typing

The two incidence maps land in different current spaces.

For `P`, cumulative mass through scale `Q` is

\[
 \mu_1([0,Q])
 =\sum_{p\le e^Q}p^{-1/2}
 \asymp\frac{e^{Q/2}}{Q}.
\]

Hence `mu_1` has exponential growth and is not a tempered distribution on the
ordinary Schwartz scale line.  It acts absolutely on test functions with
decay

\[
 |\varphi(q)|\le C e^{-(1/2+\epsilon)q}.
\]

For `Q`,

\[
 \mu_2([0,Q])
 =\frac12\sum_{p\le e^{Q/2}}\frac1p
 =O(\log Q),
\]

so `mu_2` is a positive tempered measure, though not a finite measure.  This
recovers the distributional-versus-Hilbert distinction in a scale-local
form, and sharpens it: the primitive port requires an exponential/Laplace
rigging, not merely `S'(R_+)`.

## Spectral-readout obstruction

The function `sin(tq)` has no decay.  Therefore neither completed current may
be paired with it by naive absolute integration at the critical boundary.
The finite-cutoff readout is exact, but the infinite readout requires the
archimedean/modular relative completion.

This is precisely why `P,Q` must enter the boundary compiler before scalar
spectral compression.

## Compiler signature

### `P`

- `precedes`: archimedean completion `A` and completed doubled Green `D`;
- `domain_after`: exponential-type scale-current rigging;
- `boundary_delta`: the primitive atomic current `mu_1`;
- `completion_scope`: finite cutoffs and Laplace tests with real decay greater
  than `1/2`;
- `residual_capability`: carries the non-Hilbert primitive anomaly.

### `Q`

- `precedes`: scalar determinant/readout and completed `D`;
- `domain_after`: tempered positive scale measures, with a separate
  non-trace-class determinant type;
- `boundary_delta`: the prime-square atomic current `mu_2`;
- `completion_scope`: Schwartz tests, but not the undamped sine readout;
- `residual_capability`: carries the Hilbert/non-trace-class square anomaly.

The incidence maps commute at finite cutoff because they occupy disjoint Fock
grades and add independent typed currents.  Their completed scalar readouts
do not exist separately, so no infinite-level commutation with scalar
compression is asserted.

## New real obstacle

The earlier `2 x 3` Schwartz--Hilbert--distributional rigging is too small for
the primitive scale current.  The boundary object needs an additional
exponential test-space level, naturally supplied by the Mellin/Laplace
half-plane.  The next compiler braid is therefore `P A` versus `A P`: does
archimedean completion continuously transport `mu_1` from the exponential
rigging to the seam boundary without changing its finite-cutoff readout?
