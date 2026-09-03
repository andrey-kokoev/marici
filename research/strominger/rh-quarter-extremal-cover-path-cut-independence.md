# The collective path cut is the independent extremal constraint

## Question

Is the two-demand Hall inequality implied by the two singleton inequalities on the five-vertex path?

## Claim boundary

No. In common-scale coordinates, the exact slacks are

\[
s_0=1446502276281209062102946365025805852465952053,
\]
\[
s_1=1972986212379857413044470885873388491416102070,
\]
\[
s_{01}=98228145156170453429479348620499761647718440.
\]

All are positive, but \(s_{01}\) is strictly smaller than both singleton slacks. The collective constraint is therefore independent and controls the global minimum.

## Disposition

The branching is both topological and inequality-theoretic. If \(x\) denotes central-supply mass sent left, path feasibility requires

\[
d_0-p_0\leq x\leq p_1+p_2-d_1.
\]

The width of this admissible interval is exactly the collective slack. The next leaf should verify this allocation-interval identity and extract a canonical interior split; this converts the opaque min-cut into an explicit local transport certificate.
