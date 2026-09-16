# Noncommuting near-null modes are the exact obstruction to global common-edge removal

## Question

Does exact positive alignment

\[
G^T\succeq0,
\qquad
G^0\succeq0,
\qquad
D=G^T-G^0
\]

automatically imply the Douglas domination

\[
D_+\preceq G^T?
\]

It does not. The failure already occurs in dimension two and identifies the global obstruction left hidden by finite-packet Widom coercivity.

## Two-dimensional hostile

On \(\mathbb C^2\), let

\[
A=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}
\]

and let \(B\) be the projection onto \((1,1)/\sqrt2\):

\[
B=\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}.
\]

Set

\[
G^T=A,
\qquad
G^0=B,
\qquad
D=A-B
=\frac12
\begin{pmatrix}
1&-1\\
-1&-1
\end{pmatrix}.
\]

Both regulator Grams are positive and their difference is exactly the centered Hermitian form.

A direct multiplication gives

\[
D^2=\frac12I,
\qquad
|D|=\frac1{\sqrt2}I.
\]

Hence

\[
D_+
=\frac12
\left(
D+\frac1{\sqrt2}I
\right).
\]

This positive operator has rank one, but its range is not contained in \(\operatorname{ran}A=\mathbb Ce_1\). Therefore

\[
\boxed{D_+\npreceq A.}
\]

Equivalently, the candidate common edge

\[
C=A-D_+
=B-D_-
\]

is not positive.

Thus exact signed alignment alone does not produce a common positive subfeature.

## Range form of the obstruction

For bounded positive operators, Douglas domination

\[
D_+\preceq cA
\]

for some finite \(c\) is equivalent to

\[
\operatorname{ran}D_+^{1/2}
\subseteq
\operatorname{ran}A^{1/2}
\]

with the appropriate closure qualification. The sharp common-edge condition asks for the constant \(c=1\).

The hostile fails before the constant is considered: the positive spectral direction of \(A-B\) escapes the support of \(A\).

For the aligned regulators, the exact support gate is therefore

\[
\boxed{
\operatorname{ran}(D_{\alpha,+}^{1/2})
\subseteq
\operatorname{ran}((G_\alpha^T)^{1/2}),
}
\]

and similarly for the negative orientation. Near-null prolate modes can violate this inclusion even when every fixed coercive packet eventually satisfies it.

## Why finite-packet coercivity repairs the hostile

Add a common scalar edge \(tI\):

\[
G_t^T=tI+A,
\qquad
G_t^0=tI+B.
\]

Their difference remains \(D\). Since

\[
\|D_+\|=\frac1{\sqrt2},
\]

one has

\[
D_+\preceq tI\preceq G_t^T
\]

for \(t\ge1/\sqrt2\), and likewise

\[
D_-\preceq G_t^0.
\]

This is exactly the finite-packet Widom argument: a coercive common edge dominates every bounded angular mismatch.

On the completed observer space, the smallest edge eigenvalue can approach zero along increasing packets. No uniform \(t\) survives, so the two-dimensional hostile can recur along a sequence of near-null modes.

## Quantitative leakage ratio

When \(G^T\) is injective on the relevant support, define

\[
\boxed{
\kappa_+(G^T,D)
=
\left\|
(G^T)^{-1/2}D_+^{1/2}
\right\|^2,
}
\]

using the reduced inverse. Douglas's lemma gives

\[
D_+\preceq G^T
\quad\Longleftrightarrow\quad
\kappa_+(G^T,D)\le1.
\]

Similarly,

\[
\kappa_-(G^0,D)
=
\left\|
(G^0)^{-1/2}D_-^{1/2}
\right\|^2.
\]

These quantities measure residual spectral leakage relative to the physical positive legs. They are invariant under isometric changes of feature carrier.

The packetwise theorem proves

\[
\kappa_{\alpha,\pm}(E)<1
\]

for every fixed coercive packet and sufficiently large regulator. Global common-edge removal requires

\[
\boxed{
\sup_\alpha\kappa_{\alpha,+}\le1,
\qquad
\sup_\alpha\kappa_{\alpha,-}\le1
}
\]

on the completed graph domain, not merely pointwise packet bounds.

## Asymptotic rather than exact removal

If exact domination fails but

\[
\kappa_{\alpha,\pm}\le1+\varepsilon_\alpha,
\qquad
\varepsilon_\alpha\to0,
\]

then the rescaled Jordan legs

\[
\widetilde D_{\alpha,\pm}
=(1+\varepsilon_\alpha)^{-1}D_{\alpha,\pm}
\]

are physically extractable. The residual signed form differs from \(D_\alpha\) by

\[
\frac{\varepsilon_\alpha}{1+\varepsilon_\alpha}D_\alpha,
\]

which vanishes on every graph-bounded vector if \(D_\alpha\) is uniformly graph bounded.

Thus Mosco convergence does not require exact finite-regulator extraction. It is enough to prove asymptotic Douglas bounds with constants tending to one.

## Spectrally adapted filtration target

Let \(P_n\) be the filtration adapted to the bounded phase-energy target \(\mathcal A_S\). The exact two-parameter estimate needed is

\[
\boxed{
\lim_{n\to\infty}
\limsup_{\alpha\to\infty}
\kappa_{\alpha,\pm}
\left|
_{P_n\mathscr E_S}
\right.
\le1
}
\]

together with graph-tail control preventing escaping positive spectral vectors in \((I-P_n)\mathscr E_S\).

The first statement is supplied packetwise by Widom coercivity. The second is the genuinely global estimate.

A concrete sufficient tail condition is

\[
\boxed{
\left\|
(G_\alpha^T)^{-1/2}
(I-P_n)D_{\alpha,+}^{1/2}
\right\|
+
\left\|
(G_\alpha^0)^{-1/2}
(I-P_n)D_{\alpha,-}^{1/2}
\right\|
\le\eta_n,
}
\]

uniformly over a regulator tail, with \(\eta_n\to0\). This is the range-sensitive version of the previously proposed residual commutator estimate.

## Consequence for the eight-leg transport

The fixed Krein splitting proves

\[
D_\alpha=G_\alpha^T-G_\alpha^0
\]

globally and packet-naturally. The hostile shows that no purely algebraic manipulation of this identity can prove global common-edge removal.

The transported rows must additionally control the angle between:

1. the positive spectral subspace of \(D_\alpha\); and
2. the support of the Tate positive Gram \(G_\alpha^T\),

with the conjugate condition for the negative/reference pair.

That angle control is exactly the asymptotic Douglas leakage estimate above.

## Disposition

Global common-edge removal is obstructed by noncommuting near-null modes, not by a missing Jordan identity. The finite-dimensional counterexample proves that exact alignment alone is insufficient.

The next analytic theorem has the sharp form

\[
\boxed{
\kappa_{\alpha,+},\kappa_{\alpha,-}
\le1+o(1)
}
\]

in the phase-energy graph norm, together with uniform filtration-tail control. This is both source-sensitive and strong enough for asymptotic physical extraction and Mosco convergence.
