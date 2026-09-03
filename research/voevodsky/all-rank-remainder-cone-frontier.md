# All-rank remainder-cone frontier

## Question

After closing the source bridge, what is the first genuinely unproved inequality rather than another equivalent reformulation?

## Claim boundary

The first scalar case and the first determinant case are identified exactly. Neither is proved here. Their failure would refute RH; proving only finitely many cases would not prove RH.

## Difference sequence

For fixed positive \(t,h\), define

\[
a_n
=
H_R(t+nh)-H_R(t+(n+1)h).
\]

The target is that \((a_n)\) is a Hausdorff moment sequence for every positive rational \(t,h\).

## First unknown scalar

Rank one requires

\[
a_0
=
H_R(t)-H_R(t+h)
\geq0.
\]

Thus the first unproved statement is monotonicity of the completed remainder kernel:

\[
H_R(t+h)
\leq
H_R(t).
\]

It must hold for every positive rational \(t,h\), not only for sampled values or zero truncations.

## First nonlinear obstruction

Rank two requires

\[
\begin{pmatrix}
a_0&a_1\\
a_1&a_2
\end{pmatrix}
\geq0.
\]

Besides \(a_0,a_2\geq0\), the new condition is

\[
a_0a_2-a_1^2\geq0.
\]

Explicitly,

\[
\begin{aligned}
&[H_R(t)-H_R(t+h)]
[H_R(t+2h)-H_R(t+3h)]\\
&\qquad\geq
[H_R(t+h)-H_R(t+2h)]^2.
\end{aligned}
\]

This is discrete log-convexity of the increment sequence. It is not implied by rank-one monotonicity.

## General polynomial probe

For

\[
p(z)=\sum_{j=0}^{N-1}c_jz^j,
\]

the all-rank assertion is

\[
Q_{t,h}(p)
=
\sum_{i,j=0}^{N-1}
\overline{c_i}c_j a_{i+j}
\geq0.
\]

Because \(H_R(t)=H(t)-e^{t/4}\), the endpoint contributes

\[
c_E|p(Y)|^2,
\qquad
c_E=e^{t/4}(e^{h/4}-1)>0,
\qquad
Y=e^{h/4}.
\]

Under RH, the full Gram formula is

\[
\begin{aligned}
Q_{t,h}(p)
={}&c_E|p(Y)|^2\\
&+\sum_{[\rho]}
 m_\rho e^{-t\gamma_\rho^2}
(1-e^{-h\gamma_\rho^2})
\left|p(e^{-h\gamma_\rho^2})\right|^2,
\end{aligned}
\]

which is manifestly nonnegative.

Without RH, the same expression has generally complex bases and cannot be used as a positive Gram decomposition. Replacing those bases by their moduli or by verified critical-line zeros would assume or truncate away the unresolved content.

## Strongest falsification attempt

The cheapest decisive falsifier is one explicit triple \((t,h,p)\) for which the fully completed arithmetic evaluation gives

\[
Q_{t,h}(p)<0.
\]

The evaluation must include certified bounds for all prime, gamma, endpoint, and truncation tails. A floating-point negative eigenvalue without those bounds is not a refutation.

Conversely, checking any finite collection of \((t,h,p)\) establishes only finite evidence. The theorem quantifies over every rank, polynomial, and positive rational mesh.

## Disposition

The research frontier is no longer a source-normalization problem. It is the direct sign problem for \(Q_{t,h}\). The rank-one monotonicity inequality is the first scalar target; the rank-two determinant is the first nonlinear target. No known argument in the current packets proves either uniformly from the arithmetic presentation.
