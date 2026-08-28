# The S1/Z2 hypermultiplet lies in the boundary-beta kernel: WP938

## Question

Does the known one-loop renormalization of five-dimensional orbifold gauge
theory derive WP937's completion-stable selector for the exchange-even
boundary coefficient?

## Imported theorem and exact domain

Groot Nibbelink and Hillenbach compute gauge-coupling renormalization for
supersymmetric gauge theories on orbifolds.  On the five-dimensional
`S1/Z2` orbifold, a bulk hypermultiplet does not induce renormalization of the
brane gauge couplings at one loop; its bosonic and fermionic cancellations
hold separately.  Their same analysis notes that a single complex bulk
scalar does require bulk and brane-localized gauge counterterms, while a
charged bulk fermion does not.

Primary source:
[Groot Nibbelink and Hillenbach, hep-th/0503153](https://arxiv.org/abs/hep-th/0503153).

This packet imports only the hypermultiplet contribution.  It does not claim
the complete non-Abelian `SU(4)` vector-multiplet beta function, higher-loop
closure, boundary-localized matter contributions, threshold matching, or a
UV completion.

## Kernel calculation

Write the common boundary coefficient as `tau` and decompose its one-loop
beta coefficient by source sector:

\[
\beta_\tau=\beta_{\mathrm{vector}}
+\beta_{\mathrm{boundary}}
+\sum_j\beta_{H_j}.
\]

For every admitted five-dimensional bulk hypermultiplet covered by the
theorem,

\[
\beta_{H_j}=0.
\]

Hence adding or removing those hypermultiplets leaves the one-loop boundary
beta coefficient unchanged.  This is a genuine completion-invariance result
for that contribution, but it is a kernel theorem, not a selector theorem.

If the remaining total beta vanishes, then on the RG scale coordinate

\[
\frac{d\tau}{dt}=0,
\qquad
\tau(t)=\tau(0).
\]

The hostile pair `tau(0) = 0, 1` therefore remains distinct at every scale.
If the remaining beta is a nonzero additive constant, WP937 already proves
that their separation is still preserved.  Neither case supplies an
attractive fixed point.

## Relation to the spectral completion

The same hypermultiplet content can change WP935's full-tower spectral index
while lying in the one-loop boundary-beta kernel.  Thus completion sensitivity
of the twist selector and completion sensitivity of the boundary beta are
independent axes.  One cannot use beta-invisibility to authorize the matter
completion or to restore the positive index.

This is a comparison among source sectors and scale-coordinate maps; it does
not introduce physical time or causal precedence.

## Classification

The imported hypermultiplet probe family identifies a nontrivial kernel in
the source-to-boundary-beta map.  It neither selects `tau` nor rigidifies a
texture presentation.  Its smallest exact falsifier of boundary selection is
the preserved pair `tau = 0, 1` under zero hypermultiplet beta.

The remaining source gate is the complete one-loop and higher-order boundary
beta system for the actual `SU(4)` vector, boundary matter, regulator, and
threshold packet.  Even a fully derived additive beta would transport rather
than select.  A selector requires a source-derived nonzero linear response or
another noninvertible boundary law, with completion stability and a typed
`physical16` instrument.

Reproduce with:

    uv run python research/flavor/checkers/wp938_s1z2_hypermultiplet_boundary_beta_kernel.py

Generated result:
`research/flavor/results/wp938_s1z2_hypermultiplet_boundary_beta_kernel.json`.
