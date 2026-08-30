# A seam Green current is a boundary-metric mismatch

## Question

How can a nonzero Green seam current survive when the sewn theta source has a
smooth oriented germ across the seam?

## Two chart Green identities

Let the positive and negative chart states have a common trace (u) in a
trace space (R). Let their boundary flux forms, after transport to (R),
be represented by Hermitian or sesquilinear operators (M_+) and (M_-).

Integration by parts on the two half-lines gives oppositely oriented endpoint
terms. Their total seam contribution is

\[
j_{\rm seam}(u,v)
=
\langle u,M_-v\rangle
-\langle u,M_+v\rangle.
\]

Therefore

\[
j_{\rm seam}(u,v)
=
\langle u,\Delta_Mv\rangle,
\qquad
\Delta_M=M_--M_+.
\]

The source state may be perfectly continuous while its two chart Green
metrics fail to match.

## General pullback form

If the common trace embeds into chart boundary spaces through maps

\[
B_+:R\to E_+,
\qquad
B_-:R\to E_-,
\]

and the chart boundary forms are (J_+) and (J_-), the actual mismatch is

\[
\Delta_R
=
B_-^*J_-B_-
-B_+^*J_+B_+.
\]

The seam Green current cancels for every sewn state if and only if

\[
\Delta_R=0.
\]

Ambient equality of (J_+) and (J_-) is unnecessary. Only their pullbacks
to the source-authorized common trace range must agree.

## Rank theorem

The minimal number of independent complex seam channels required to carry
the mismatch is

\[
\operatorname{rank}\Delta_R.
\]

Indeed, the seam form factors through the image of (Delta_R), and no
smaller target can represent a form of that rank.

For a one-dimensional common trace, the possibilities are exact:

- (Delta_R=0): no seam channel;
- (Delta_R\ne0): exactly one complex seam line.

This recovers Grothendieck's surviving one-line defect count without
attributing it to a discontinuous source state.

## Theta interpretation

The canonical theta tail and reflected seam atoms have a common oriented
source jet. Consequently a surviving primitive Clark seam term must arise
from a mismatch among the transported boundary forms, such as:

1. different Clark operators on the two charts;
2. a sign in the reflected Green metric;
3. a chart-dependent spectral normalization;
4. an arithmetic aggregation applied after the common trace;
5. a cut-domain convention that retains one flux instead of summing both.

The exact finite audit is now

\[
\Delta_{R,X}
=
B_{-,X}^*J_{-,X}B_{-,X}
-B_{+,X}^*J_{+,X}B_{+,X}.
\]

It should be evaluated before scalar aggregation. Its rank, sign, sheet
character, and cutoff naturality identify the seam port completely.

## Control-theoretic reading

The common trace is continuity of the interface state. The pulled-back Green
form is the interface supply rate. Equal state alone does not guarantee zero
net power; the two sides must also expose the same port metric. The residual
(Delta_R) is an impedance mismatch.

This distinguishes state sewing from power-conserving interconnection.

## Relation to relational descent

The seam current is bilinear and the trace quotient is linear. Therefore the
slotwise kernel-annihilation theorem applies completely here. Aspect's warning
about nonlinear fibers and irreducible higher-order correlations remains
essential for other targets, but it does not weaken this bilinear criterion.

If a later theta construction uses nonlinear normalization or a genuine
three-source cumulant, fiberwise constancy or the full higher-arity relation
must replace pairwise kernel tests.

## Falsifier certificate

    {
      "code": "seam_boundary_metric_mismatch",
      "state_trace_jump": 0,
      "pulled_back_metric_difference": "Delta_R",
      "seam_channel_rank": "rank(Delta_R)",
      "source_germ_discontinuous": false
    }

## Disposition

A Green seam current on a smoothly sewn source is exactly a mismatch of the
two chart boundary forms on their common trace range. Its minimal port count
is the rank of that mismatch. The theta programme should compute this matrix
before invoking primitive-current domination.

## Claim boundary

This theorem classifies bilinear boundary fluxes of linearly sewn chart
states. It does not identify the actual theta chart metrics, prove positivity,
or extend unchanged to nonlinear quotient maps or irreducible higher-order
source relations.
