# Suzuki squared is the Hardy block decomposition, and its defect has the wrong role

## Objective

Starting only from Suzuki's unconditional boundary operator, attempt to construct an abstract second-stage Hilbert factorization rather than test sampled kernels.

Let

\[
\Theta=E^\#/E,
\qquad |\Theta(x)|=1\quad\text{for a.e. }x\in\mathbb R,
\]

and let `P_+` and `P_-` be the Hardy projections of `L^2(R)` onto the upper and lower Hardy boundary spaces. Multiplication

\[
U=M_\Theta
\]

is unitary on boundary `L^2` without RH.

## The exact abstract Suzuki-squared decomposition

Relative to

\[
L^2=H^2_+\oplus H^2_-,
\]

write the unitary multiplication operator in blocks:

\[
U=
\begin{pmatrix}
T_\Theta & C_\Theta\\
H_\Theta & D_\Theta
\end{pmatrix},
\]

where

\[
T_\Theta=P_+M_\Theta|_{H^2_+},
\qquad
H_\Theta=P_-M_\Theta|_{H^2_+}.
\]

The first column of `U^*U=I` gives the unconditional identity

\[
\boxed{
T_\Theta^*T_\Theta+H_\Theta^*H_\Theta=I_{H^2_+}.
}
\]

Equivalently,

\[
\|f\|_2^2
=
\|T_\Theta f\|_2^2+
\|H_\Theta f\|_2^2.
\]

This is the genuine operator-theoretic meaning of applying Suzuki's unitary construction twice: it produces a positive Pythagorean decomposition into the Hardy-preserving channel and the leaked channel.

## The leakage is a positive square, but cannot repair the Weil form

The commutator with the Hardy projection is

\[
[P_+,M_\Theta]|_{H^2_+}=-H_\Theta.
\]

Thus

\[
H_\Theta^*H_\Theta
\]

is an unconditional positive operator measuring failure of the boundary multiplier to preserve the analytic half-space.

This initially resembles the desired remainder. Its logical role is opposite, however. The model-space/de Branges argument needs the analytic channel to close. In the ideal inner case,

\[
M_\Theta H^2_+\subseteq H^2_+,
\qquad H_\Theta=0.
\]

Hence the positive square supplied by the second stage is an **error norm whose vanishing is required**, not a positive term that can be added to the Weil form. The identity proves contractivity of `T_Theta`; it does not prove positivity of the de Branges kernel or identify Suzuki's ambient norm with the Weil pairing.

## Why quotienting by the leakage is circular

One might define

\[
\mathcal N=\overline{\operatorname{ran}H_\Theta^*}
\]

and pass to `H^2_+ \ominus N`, where the leakage vanishes. This always creates a maximal subspace on which the chosen defect is invisible, but it is not the required arithmetic quotient:

1. it discards precisely the vectors detecting nonanalytic upper-half-plane poles;
2. no source theorem says the Gaussian/Weil test image lies in `ker H_Theta`;
3. proving that the full test image lies in `ker H_Theta` is the missing innerness statement;
4. an off-axis zero produces a nontrivial negative Krein orbit even if one formally kills its boundary leakage.

Therefore the quotient cannot be declared before proving that it preserves every Weil evaluation and polarization.

## Generalized Schur/Pontryagin completion

There is a canonical abstract home for the obstruction. A unimodular meromorphic boundary function with upper-half-plane poles belongs, when the pole index is finite, to a generalized Schur class rather than the ordinary Schur class. Its kernel

\[
k_\Theta(z,w)
=
\frac{1-\Theta(z)\overline{\Theta(w)}}{-i(z-\bar w)}
\]

then has a finite number of negative squares, and its reproducing space is Pontryagin rather than Hilbert. In a Krein--Langer factorization one writes schematically

\[
\Theta=B^{-1}\Theta_0,
\]

where `B` is the Blaschke product formed from the upper-half-plane pole divisor and `Theta_0` is Schur after cancellation.

For the completed-zeta specialization, this gives an exact conceptual factorization:

\[
\boxed{
\text{Suzuki positive bulk}
\oplus
\text{pole-divisor Pontryagin defect}.
}
\]

Each off-axis conjugate zero orbit contributes the previously identified `(1,1)` arithmetic block. The ordinary Hilbert case is exactly `B=1`, namely absence of the forbidden pole divisor.

## Why the Blaschke repair is not source-derived in the required sense

Multiplying by `B` would indeed repair `Theta` into an ordinary Schur candidate and produce a positive model kernel. But `B` is constructed from the forbidden spectral divisor itself. Moreover, the repaired terminal function is `B Theta`, not the original completed Weil boundary function. To descend its positive norm back to the original form one must restore the inverse Blaschke factors, reintroducing the negative Pontryagin directions.

Thus divisor cancellation is the exact analogue of deleting off-critical zeros by hand. It is a valid conditional classification, not a noncircular source construction.

## Result of the construction attempt

The strongest unconditional abstract identity obtainable from Suzuki's existing operator is

\[
\boxed{
I-T_\Theta^*T_\Theta=H_\Theta^*H_\Theta\succeq0.
}
\]

It supplies a canonical positive defect operator. But the desired implication requires

\[
H_\Theta=0
\]

on the full arithmetic test image, not merely positivity of its square. Applying another norm cannot prove this vanishing.

The remaining genuinely constructive question is consequently narrower:

> Does the endpoint--gamma--prime source provide an independent intertwining law forcing `P_D(C_c^infty)` into `ker H_Theta`?

Suzuki's norm equality shows that universal such inclusion is RH-equivalent. Any useful weaker theorem must exploit the special rung-four Gaussian image and prove its inclusion or a coercive leakage bound without extending to all tests.

## Disposition

`Suzuki squared` is not empty: it canonically exposes the Hardy leakage as a positive square. It nevertheless does not turn the Weil form into a Hilbert norm. The exact abstract obstruction is

\[
\boxed{
\text{positive leakage magnitude}
\neq
\text{vanishing of analytic leakage}.
}
\]

The universal vanishing condition is the innerness/RH gate; the non-Hilbert completion is the generalized-Schur Pontryagin space indexed by the forbidden divisor.
