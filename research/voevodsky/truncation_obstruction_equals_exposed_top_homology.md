# Truncation obstruction equals exposed top homology

## Question

Does a concrete failure to preserve Carrier fillers produce exactly the positive-dimensional class exposed by a truncated observation?

## Claim boundary

The test uses skeletal truncations of the canonical six-dimensional relative attachment. These are mathematically defined observation maps, not source-derived physical sector maps. The result tests the algebraic mechanism of the descent-obstruction conjecture, not its physical sufficiency.

## Observation

Let \(C_\bullet\) be the acyclic six-cube relative chain complex and let \(P_{\leq r}\) retain chain groups through degree \(r\) while setting higher degrees to zero. As a graded projection, it need not commute with the differential. Its first defect is

\[
\Delta_r
=
P_{\leq r}d-dP_{\leq r},
\]

whose only nonzero block is

\[
\Delta_r|_{C_{r+1}}=d_{r+1}:C_{r+1}\to C_r.
\]

The truncated complex has no outgoing differential from degree \(r\), so

\[
H_r(C_{\leq r})
=
\ker d_r.
\]

Acyclicity of the full complex gives

\[
\ker d_r=
\operatorname{im}d_{r+1}.
\]

Therefore

\[
\dim H_r(C_{\leq r})
=
\operatorname{rank}\Delta_r.
\]

The apparent top class is exactly the boundary information discarded by truncation.

## Bold prediction

For every truncation degree \(r=0,\ldots,5\), the commutator-defect rank equals the exposed top Betti number. Restoring degree \(r+1\) removes precisely that class contribution. At \(r=6\), both defect and homology vanish.

## Rivals

1. Truncation creates classes unrelated to the omitted boundary block.
2. The defect is nonzero but its rank does not account for all exposed homology.
3. Full filler restoration leaves a residual class.

## Test

Construct the exact six-cube relative boundary matrices. For every skeletal cutoff, compute all truncated Betti numbers, the rank of \(P d-dP\), and the rank change when the next chain group is restored. Require exact equality over the integers/rationals.

## Computed result

For truncation degrees zero through five, the exposed top Betti numbers are

\[
(1,4,7,7,4,1),
\]

exactly equal to the ranks of the omitted boundary blocks \(d_1,\ldots,d_6\) and to the directly computed commutator ranks. Every lower retained Betti number vanishes. At full degree six, both homology and commutator defect vanish.

## Disposition

The algebraic mechanism survives exactly. Skeletal observation creates no unexplained class: every exposed class is the image of the first discarded filler boundary, and its dimension equals the failure of the projection to commute with \(d\). Restoring the filler removes it. This is a negative control for the descent-obstruction conjecture, not physical verification; a source-derived sector map remains required.
