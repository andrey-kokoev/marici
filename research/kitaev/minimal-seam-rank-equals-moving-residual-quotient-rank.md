# Minimal Seam Rank Equals Moving-Residual Quotient Rank

Let (Q\succeq0), (R) be a frame residual, and (H) an authorized seam
port. Put (K=\ker Q). A necessary finite gate for

\[
R^*R\le C(Q+H^*H)
\]

is

\[
K\cap\ker H\subseteq\ker R.
\]

Equivalently, (R|_K) factors through (H|_K). Therefore

\[
\operatorname{rank}(H|_K)\ge\operatorname{rank}(R|_K).
\]

This is the minimal seam-port theorem: one scalar seam row repairs a moving
frame only when the operative residual on the analytic nullspace has rank at
most one and that row separates its quotient. Scalar domination on one chosen
witness does not establish the joint-kernel law.

The smallest hostile uses (Q=\operatorname{diag}(1,0,0)), with (R) reading
the last two coordinates. A single seam row (H=(0,1,1)) sees both coordinate
basis witnesses but kills their difference, while (R(0,1,-1)\ne0). Two
independent rows are necessary and sufficient. If (R) reads only the second
coordinate, one aligned seam row is minimal.

Uniform completion additionally requires the factorization norms to remain
bounded. Rank and kernel inclusion decide finite possibility, not uniform
conditioning. The seam rows must be source-authorized before optimization.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
9/10. Nullspace, residual rank, seam rank, and joint-kernel witness were frozen.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The apparent same-direction repair became an exact quotient-rank law.
One scalar seam cannot repair two independent moving residual directions even
when it is nonzero on each coordinate witness separately.
