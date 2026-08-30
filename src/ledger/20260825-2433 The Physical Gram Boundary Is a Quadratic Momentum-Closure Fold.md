---
author: marici.Benincasa
date: 2026-08-25
---

# 2433 — The Physical Gram Boundary Is a Quadratic Momentum-Closure Fold

## Why Entry 2430 is not yet a physical activation theorem

Entry 2430 finds a rank-one elliptic nearby-cycle channel transverse to each
Heron component in unconstrained magnitude space. Physical external momenta
do not vary freely in that space: they obey vector closure. The physical
relative cycle must therefore be transported in a source momentum chart
before assigning any meaning to the coefficient nearby cycle.

## Source momentum-closure chart

Choose

\[
\vec p_1=(P_1,0,0),
\qquad
\vec p_2=(P_2\cos\theta,P_2\sin\theta,0),
\]

and let

\[
P_3^2
=
P_1^2+P_2^2+2P_1P_2\cos\theta.
\]

The external Gram determinant and signed Heron product satisfy exactly

\[
\Lambda(P_1,P_2,P_3)
=
-4P_1^2P_2^2\sin^2\theta.
\]

At the physical component $f_3=P_1+P_2-P_3=0$,

\[
(P_1+P_2-P_3)(P_1+P_2+P_3)
=
4P_1P_2\sin^2\frac\theta2.
\]

Thus the resolved physical angle is linear, while the magnitude-space Heron
normal is quadratic:

\[
f_3=O(\theta^2).
\]

The other two labelled physical components are obtained by the corresponding
source orientation choices.

## Cancellation in the frozen measure

Equation (3.3) of Benincasa--Vazão, arXiv:2402.06558v3, rewrites the original
loop-vector measure as

\[
d^d\ell
\sim
G_{\rm ext}^{-1/2}
\left(\frac{G_{\rm full}}{G_{\rm ext}}\right)^{(d-n_e-1)/2}
\prod_e dy_e^2.
\]

For the physical three-site loop in three spatial dimensions,

\[
d=n_e=3.
\]

Therefore

\[
G_{\rm ext}^{-1/2}
\left(\frac{G_{\rm full}}{G_{\rm ext}}\right)^{-1/2}
=
G_{\rm full}^{-1/2}.
\]

The apparent external-Gram Jacobian pole cancels exactly. What fails at
$G_{\rm ext}=0$ is the scalar-product/distance coordinate chart, because
the chosen external momentum basis loses rank. The original loop contour

\[
\Gamma_\ell=\mathbb R^3
\]

does not collapse and is transported by the identity in the analytic
$\theta$-chart.

## Result

\[
\boxed{
M_{\rm Gram}^{\rm source\ cycle}=1.
}
\]

This is cycle monodromy, not a theorem that every renormalized period is
analytic. Combined with Entry 2430, the typed picture is

\[
\boxed{
\text{elliptic coefficient nearby cycle}
\quad+\quad
\text{trivial original-cycle transport}
\quad+\quad
\text{uncomputed pairing}.
}
\]

The external Gram wall is existing Cayley--Menger support and a quadratic
fold of the magnitude projection. It is not new Carrier support.

## Scope

The result certifies the source-cycle and Jacobian behavior at generic
nonsoft Gram kinematics. It does not by itself prove annihilation of the
elliptic vanishing-cycle covector at infinity, nor analyticity after every
UV subtraction. Those require the source-normalized Leray/readout pairing.

## Durable evidence

- `research/benincasa/check_physical_gram_vector_lift.py`;
- `research/benincasa/physical-gram-vector-lift.json`;
- frozen source arXiv:2402.06558v3, equations (3.3), (3.8), and (A.12);
- sequence claim `seqclaim-82185fce2b40faeda57858ab`.

## Next falsifier

Compute the source-normalized Leray covector of the original
$d^3\ell$-cycle against the rank-one elliptic vanishing cycle at infinity.
If it vanishes, the generic Gram coefficient monodromy is physically
invisible. If it does not, test whether the activated class is recovered by
the complete contact-normal score tower. No new Carrier cell is admissible.
