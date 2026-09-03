# Source Krein channels for the meta-contraction

## Question

Can the abstract positive and negative feature maps `A` and `B` be obtained from the completed explicit formula without using zero locations?

## Endpoint channel

For an analytic spectral test `h`, the centered endpoint contribution is the symmetric polar evaluation

\[
Q_{\rm end}(h)
=
\frac12\left(h(i/2)+h(-i/2)\right).
\]

After polarization, write the two endpoint evaluations as `e_+(f)` and `e_-(f)`. Their cross-pairing diagonalizes by

\[
a_{\rm end}(f)=\frac{e_+(f)+e_-(f)}2,
\qquad
b_{\rm end}(f)=\frac{e_+(f)-e_-(f)}2.
\]

Up to the fixed convention factor, the endpoint form is

\[
|a_{\rm end}(f)|^2-|b_{\rm end}(f)|^2.
\]

This recovers the endpoint's exact one-positive/one-negative Krein signature and explains its rank-two Toeplitz failure.

## Gamma channel

The archimedean term is a real weighted integral on the spectral line. After retaining its normalization constant, split its real weight into positive and negative parts

\[
w_\Gamma=w_\Gamma^+-w_\Gamma^-.
\]

This gives multiplication feature maps

\[
A_\Gamma f=\sqrt{w_\Gamma^+}\,f,
\qquad
B_\Gamma f=\sqrt{w_\Gamma^-}\,f.
\]

The split is source-derived from the digamma weight; it does not assert that either part separately respects completion identities.

## Prime-derived channel

Each paired prime displacement acts through a self-adjoint translation adjacency

\[
J_n=\frac{U_{\log n}+U_{-\log n}}2.
\]

Although all `J_n` commute, taking positive and negative parts after forming a cutoff sum is not functorial in the cutoff: adding one adjacency can move the zero set of the total multiplier and transfer directions between its positive and negative spectral subspaces.

The cutoff-compatible construction instead splits every labelled adjacency before summation:

\[
J_n=J_n^+-J_n^-.
\]

The prime feature rows are the direct sums of

\[
\sqrt{q_n}\,(J_n^+)^{1/2}
\quad\text{and}\quad
\sqrt{q_n}\,(J_n^-)^{1/2}.
\]

Adding a prime label appends feature coordinates and therefore gives honest nested cutoff spaces. At fixed Gaussian width, the log-Gaussian weights make the relevant labelled sums convergent. This termwise split preserves provenance and cutoff conformance; it does not assert positivity of the total prime channel.

## Global row operators

Collect every positive feature into one row operator `A_N` and every negative feature into `B_N`. Then the finite completed form is exactly

\[
Q_N(f)=\|A_Nf\|^2-\|B_Nf\|^2.
\]

Arithmetic cutoff is used only to construct the convergent labelled feature rows. It is not a positivity index: the partial completed forms need not be positive. After completing the prime rows, combine them with the endpoint and gamma channels into global operators `A` and `B`.

The lower-pyramid identities now have one concrete target:

\[
CA=B,
\qquad
\|C\|\le1.
\]

Finite contractions are restrictions of this global relation to finite observer packets, not to finite prime cutoffs. Mixed cutoff-and-observer computations must carry a rigorous tail bound.

## Obstruction localized

The endpoint, gamma, and prime Jordan decompositions exist at each finite cutoff, but this does not prove positivity. The missing content is simultaneous domination of the assembled negative row by the positive row. Separate sector contractions are impossible because the endpoint negative direction requires cross-sector cancellation.

The infinite conformance identities can now be asked to determine `C_N` on generators. A failure of compatibility under one cutoff inclusion is a finite coherence obstruction; a compatible family with norms approaching a value above one is an order obstruction.

## Disposition

The abstract Krein presentation can be sourced without zeros at finite cutoff. The next executable object is a cutoff-compatible contraction candidate coupling endpoint-negative, gamma-negative, and prime-negative features to the assembled positive row. Do not take Jordan limits or claim an infinite contraction before graph convergence and uniform norm control are proved.
