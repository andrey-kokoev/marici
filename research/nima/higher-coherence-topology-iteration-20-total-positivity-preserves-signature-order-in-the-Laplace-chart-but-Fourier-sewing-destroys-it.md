# Higher-coherence topology iteration 20: total positivity preserves signature order in the Laplace chart, but Fourier sewing destroys it

## Candidate topology

Use a totally positive or sign-regular kernel to transport source signatures.
Variation diminution then ensures that a source sequence with one sign
transition cannot acquire an alternating pattern. This would supply exactly
the ordered-signature hypothesis needed by the Wasserstein noncollision
mechanism.

## Laplace chart

The theta atom kernel is

\[
K_L(x,y)=e^{-xy},
\qquad x,y>0.
\]

For `x_1<x_2` and `y_1<y_2`, its second minor is

\[
\Delta_L
=e^{-x_1y_1-x_2y_2}
-e^{-x_1y_2-x_2y_1}<0.
\]

After reversing one coordinate order, the kernel is strictly sign-regular.
Classical variation diminution therefore preserves a one-transition source
signature in the radial/Laplace presentation.

This is an authentic source-side mechanism, not a topology chosen from zero
locations.

## Fourier quarter-turn

The self-adjoint translation carrier uses

\[
K_F(q,\xi)=e^{-i\xi q}.
\]

Its corresponding second minor factors into a unit phase times

\[
\sin\left(
\frac{(\xi_2-\xi_1)(q_2-q_1)}2
\right).
\]

The sign changes with rectangle size. No global ordering convention makes all
minors positive or gives them one fixed real phase.

Therefore ordinary total positivity is not preserved by the Fourier sewing
needed to reach the spectral carrier.

## Higher-coherence implication

A cone tower built entirely in the Laplace chart may preserve signature order,
but it no longer controls the self-adjoint spectral measure used by the Krein
and Wasserstein arguments. A tower built after Fourier sewing has lost the
variation-diminishing law.

Unitarity cannot transport total positivity: it preserves Hilbert norms, not
ordered minors.

## Possible two-polarization repair

A valid higher system would need to retain simultaneously:

\[
(\mathcal X_L,\mathcal X_F,\mathcal T,
\mathfrak f,\omega),
\]

where `X_L` carries the ordered cone, `X_F` carries spectral energy, `T` is the
actual Fourier/Tate sewing, and `omega` controls paired minors before scalar
projection.

The smallest finite test is:

1. use two arithmetic labels and two spectral samples;
2. compute the radial sign-regular minor;
3. apply the actual sewing map;
4. retain its conjugate sector;
5. test whether a Hermitian paired minor has fixed orientation.

A fixed orientation would be weaker than ordinary total positivity and could
still preserve one-transition signature. An oscillating paired orientation
would falsify the route.

## Completion conditions

Any finite orientation must survive dense spectral sampling, seam atoms,
primitive and square currents, and cutoff completion. A phase that oscillates
faster with cutoff does not define a completed order cone.

## Verdict for topology 20

Total-positive topology validates the source-side origin of ordered signature
but fails under the Fourier quarter-turn. It does not yet unlock the terminal
energy gate.

The next nonredundant topology is the proposed two-polarization Hermitian-minor
topology, testing whether conjugate Fourier sectors combine into a fixed real
orientation even though each sector separately oscillates.