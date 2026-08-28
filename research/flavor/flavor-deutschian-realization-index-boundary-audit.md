# Deutschian realization-index-boundary audit: WP935

## Question

Does the strongest declared flavor source make the realization stratum,
positive full-tower index, and physical normalization consequences of one
hard-to-vary constructor?

## Admitted comparison

The strongest existing candidate is the five-dimensional `SU(4)` gauge-Higgs
packet of WP772.  With parity

\[
P=\operatorname{diag}(1,1,-1,-1),
\]

the adjoint splits as `15 = 7 + 8`.  Opposite parity for the fifth gauge
component realizes the eight-dimensional odd sector as a complex
`(2,2)` link.  This is source progress: the link is no longer an arbitrary
scalar presentation.

For the pure vector realization,

\[
\kappa_{\mathrm{vector}}=2+15=17>0,
\]

so the complete KK potential of WP753 selects the half twist.  The
representation realization and spectral sign are therefore joined inside
this restricted source packet.

## Two exact hostile extensions

The complete residual-symmetry boundary operator ring admits an exchange-even
kinetic coefficient `tau`.  With bulk contribution `C = 1`, both `tau = 0`
and `tau = 1` preserve the same parent, parity, link realization, exchange
symmetry, and positive index, while changing the portal contrast:

\[
\Delta(0)=\frac{1}{10},
\qquad
\Delta(1)=\frac{1}{20}.
\]

Thus the parent rigidifies the realization and selects the twist, but does
not select the physical normalization.

The second hostile extension admits the required 32-degree portal operand
packet in the bulk.  It retains the parent and boundary operator grammar but
changes

\[
\kappa=2+15-32=-15.
\]

The same minimal parent then selects the zero-twist branch.  Adding the
48-degree mediator packet gives `kappa = -63`.  Hence positivity is not stable
under completion by the already required flavor content.

These are logical comparisons between admitted objects, not a temporal or
causal sequence.

## Classification

The `SU(4)` gauge-Higgs packet is both a realization selector and a
conditional half-twist selector on the pure-vector subdomain.  It is neither
a complete flavor selector nor a distinguished-point selector on
`physical16`.

The first missing arrow is a source law selecting the complete realization
and operator ring together.  It must both control the exchange-even boundary
coefficient and keep the full required matter spectrum in the positive-index
class.  Two-momentum tomography from WP770 could identify the surviving
boundary coefficients, but identification is not selection.

The smallest exact falsifier of the current Deutschian conjecture is already
the pair `tau = 0, 1`: the conjecture fails if it asserts that the declared
parent alone fixes the numerical portal.  A stronger future conjecture is
falsified by any source-compatible complete realization with nonpositive
index or a free exchange-even boundary modulus.

## Result

No declared constructor currently makes realization, positive index,
boundary normalization, and `physical16` restriction vary together.  The
frontier is narrower than total source absence: a partial realization-plus-
twist constructor exists, and the unresolved defect is completion-stable
boundary selection.

Reproduce with:

    uv run python research/flavor/checkers/wp935_deutschian_realization_index_boundary_audit.py

Generated result:
`research/flavor/results/wp935_deutschian_realization_index_boundary_audit.json`.
