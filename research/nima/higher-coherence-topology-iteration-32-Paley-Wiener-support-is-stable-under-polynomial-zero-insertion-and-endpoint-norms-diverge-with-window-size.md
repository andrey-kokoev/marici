# Higher-coherence topology iteration 32: Paley--Wiener support is stable under polynomial zero insertion, and endpoint norms diverge with window size

## Candidate topology

Use Paley--Wiener spaces `PW_L`, identifying entire functions of exponential
type `L` with Fourier transforms of `L2` functions supported in `[-L,L]`.
Support, causal orientation, endpoint evaluation, and affine crossing operators
are then explicit at every finite window.

## Support does not fix zero location

If

\[
F(z)=\int_{-L}^Le^{-izt}f(t)\,dt,
\]

then multiplication by a polynomial corresponds distributionally to applying
a differential operator to `f`. In particular,

\[
(1-z^2)F(z)
\]

has the same exponential type and the same compact support after replacing `f`
by the corresponding derivative combination.

Thus finite reciprocal zero insertion does not violate the Paley--Wiener
support constraint. Exponential type controls density and support provenance,
not critical-line placement.

## Finite-window success

Every evaluation functional is continuous on `PW_L`; endpoint vectors and
rank-two crossing/clutching operators are explicit and trace class. Therefore
finite higher-cone comparisons can be realized exactly on each window.

This topology is particularly effective for:

- causal Hardy orientation;
- endpoint Green identities;
- finite affine spectral-flow clutching;
- exact finite-rank Schur complements.

## Completion failure

The norm of off-axis endpoint evaluation grows exponentially with `L`, and the
trace norm of the affine crossing operator grows at least linearly with the
window. Hence the finite clutching family need not define a bounded operator on
one fixed completed Paley--Wiener carrier.

Rescaling by `1/L` can bound the trace but destroys source-faithful evaluation
on fixed packets. The correct limit is pro/relative rather than one ordinary
Hilbert space.

## Phase monotonicity

A de Branges phase monotonicity theorem would add genuine zero-location force,
but it is equivalent to positivity of the associated de Branges kernel. The
support theorem alone does not provide that positivity. Likewise, causal
one-sided support fixes poles and propagation direction but does not exclude
inner zeros of the reciprocal feedback.

## Higher-coherence interpretation

Repeated cones close exactly at each finite bandwidth, while their operator
norms diverge as bandwidth grows. This is a clear example where finite higher
coherence exists but no uniform Hilbert totalization follows. A pro-window
object retains the cells, yet—as shown in iteration 1—faithful finite readouts
retain the terminal residual.

## Verdict for topology 32

Paley--Wiener topology gives excellent finite boundary control and exact
support provenance. It cannot prevent polynomial off-seam zero insertion, and
its endpoint/clutching norms diverge under window completion.

The next nonredundant topology to test is a quasianalytic or Denjoy--Carleman
topology, where an infinite jet at the seam determines the whole section and
might make repeated higher-jet coherence globally rigid.