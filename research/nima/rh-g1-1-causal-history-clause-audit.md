# RH G1.1 causal-history clause audit

## Ledger clause

Gate G1.1 requires one source-typed theorem containing all three parts:

1. the causal-history auxiliary block;
2. cutoff- and prime-uniform lower bounds for \(I\pm iH\);
3. incidence compression to the finite coefficient \(\tau\).

The repository contains substantial results for each part, but they do not yet compose into that theorem.

## Auxiliary block

The analytic factorization is exact:

\[
D_\pm
=\frac12(I\pm iH)^*(I\pm iH).
\]

The finite wall polarization is also exact: reciprocal chain reversal gives

\[
-JM=I.
\]

What remains is not positivity algebra. It is the typed wall--graph identity

\[
S=\frac12(I_{\mathrm{wall}}+H^*H)
\]

on one declared reduced history carrier, with the coefficient wall and history output carrying the source normalization used by the Adams edge. The finite identity wall cannot be inserted into the completed history graph merely because it yields a positive factorization.

## Uniform shifted-history bound

For a nonnegative history kernel \(\Phi\), every half-line cutoff satisfies

\[
\|H_L\|\le M_\Phi,
\qquad
M_\Phi=\int_0^\infty\Phi(r)\,dr.
\]

Once the source normalization identifies \(M_\Phi=\xi(1/2)\), the theta fixed-point integral proves exactly

\[
M_\Phi<\frac12.
\]

Therefore

\[
\|(I\pm iH_L)x\|>\frac12\|x\|
\]

uniformly in the cutoff, and the reciprocal shifted squares have the rational lower bound

\[
D_{L,\pm}\ge\frac18I.
\]

This settles the operator estimate conditional on the normalization diagram. It does not settle that diagram. In particular, bilateral/half-line factors, prime amplitudes, differentiated kernels, or coefficient placement can change the effective mass.

## Incidence compression

On the rapid relative core, Volterra history gives both reciprocal channels explicitly:

\[
c_+=\frac{m^2}{2},
\qquad
c_-=-\|\Phi\|_2^2.
\]

Thus the odd channel is nonzero and its sign is fixed. However, the calculation is a relative Green pairing: the even history is a constant wall and the odd primitive approaches nonzero endpoint values. The missing theorem must place both in the wall-extended Sobolev history space, pass the identities through closure and Mellin transport, and then identify the compressed operator with the ledger's \(\tau\), including its Euler/Wronskian orientation.

## Earliest residual

The first unresolved implication in G1.1 is the relative common-carrier theorem. The coefficient wall does represent as the full analytic identity under multiplication; there is no rank obstruction. However, completion annihilates the zero-mode wall, so the identity cannot be transported as an ordinary completed-image coordinate.

One must construct a relative Green or mapping-cone block retaining the wall in kernel data and the causal history in the completed image, then prove that its Schur return is

\[
\frac12(I\pm iH)^*(I\pm iH)
\]

with the same kernel amplitude and prime coefficient convention used by the incidence map. Once this is proved, the existing theta-mass estimate supplies the uniform shifted-resolvent margin. The next residual is closure and orientation of the two-channel compression to \(\tau\).

G1.1 therefore remains open. No RH conclusion is promoted.

## Evidence

- `publication/rh-proof-ledger.json`
- `research/nima/oriented-reciprocal-sewing-polarizes-the-real-wall-krein-form-to-the-identity-metric.md`
- `research/nima/the-history-graph-energy-canonically-dominates-causal-oddness.md`
- `research/nima/the-graph-energy-reciprocal-blocks-are-exact-shifted-history-squares.md`
- `research/nima/the-theta-mass-may-close-the-half-line-shifted-resolvent-gate.md`
- `research/nima/the-theta-integral-proves-xi-one-half-is-strictly-below-one-half-without-numerics.md`
- `research/nima/volterra-history-couples-both-reciprocal-theta-channels-exactly.md`
