# 2100 — Gaussian Collision Frame Holonomy Disappears in the Boundary Coefficient

## Question

Entry 2098 identified an unsplit rank-two boundary coefficient at coincident
zero modes.  Test whether transport around a genuine frequency-collision point
gives this coefficient nontrivial holonomy.

## Frozen collision family

Use the real symmetric conical family

\[
A(\theta)=
\begin{pmatrix}
\cos\theta&\sin\theta\\
\sin\theta&-\cos\theta
\end{pmatrix},
\]

inside the positive frequency matrix

\[
F_{\epsilon,\theta}
=\epsilon(I+\delta A(\theta)),
\qquad 0<\delta<1.
\]

The two frequencies remain positive for \(\epsilon>0\), coalesce at the
central collision, and share the zero-mode limit as \(\epsilon\to0\).

## Exact transport

A continuous real eigenframe is parametrized by the half-angle.  After one
loop,

\[
v_\pm(2\pi)=-v_\pm(0).
\]

Thus the eigenframe double cover has the familiar real Berry sign:

\[
T_{\rm frame}=-I.
\]

The covariance boundary coefficients, however, depend on the quadratic
projectors

\[
P_\pm=v_\pm v_\pm^T.
\]

Consequently

\[
P_\pm(2\pi)=P_\pm(0),
\qquad
T_{\rm coeff}=I.
\]

Their rank-two sum is also fixed.

## Narrow result

\[
\boxed{
\text{frequency collision carries a nontrivial frame double cover but
trivial Gaussian boundary-coefficient holonomy.}
}
\]

The Berry sign is presentation/frame memory.  It disappears under the
quadratic covariance lens.  Therefore this real two-mode collision creates
neither a coefficient obstruction nor a new Carrier cell.

This provides another typed warning:

\[
\text{monodromy of a primitive frame}
\not\Rightarrow
\text{monodromy of the physical coefficient object}.
\]

## Next falsifier

Test a complex Bogoliubov family whose source transport is not reduced to a
real sign.  Determine whether the covariance coefficient still factors
through projectors with trivial holonomy or retains a genuine symplectic
phase/extension.  The source family and physical covariance pairing must be
frozen before inspecting the loop.

## Durable evidence

- `research/benincasa/checkers/two_mode_gaussian_collision_holonomy.py`
- `research/benincasa/checkers/results/two-mode-gaussian-collision-holonomy.json`
- Ledger allocation: `seqclaim-1259cebca9c597fadf0a3866`

