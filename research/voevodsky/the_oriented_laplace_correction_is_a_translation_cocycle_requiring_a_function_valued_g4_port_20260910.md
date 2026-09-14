# The oriented Laplace correction is a translation cocycle requiring a function-valued G4 port

## Question

What is the minimal target structure needed to compare the rapid radial Laplace probe with a future G4 port while preserving ordered ratio translations?

## Claim boundary

The one-sided Laplace readout transforms by a nontrivial translation cocycle. A target retaining only the Mellin character cannot receive the source action. The minimal comparison target must retain the function-valued radial kernel or an equivalent complete family of oriented segment functionals. This constructs the required interface shape but does not authorize a G4 contract mutation.

## Problem

For a rapid radial kernel \(K\), define

\[
H_K(z)=\int_0^\infty e^{-zw}K(w)\,dw
\]

and translation

\[
(T_dK)(w)=K(w+d).
\]

One-sided integration is not translation invariant because the lower endpoint stays fixed.

## Bold conjecture

Translation acts on the Laplace readout only by the character \(e^{zd}\):

\[
H_{T_dK}(z)=e^{zd}H_K(z).
\]

## Named rivals

1. Translation produces an oriented finite-segment cocycle.
2. The finite correction can be absorbed into one fixed scalar boundary coordinate.
3. Retaining the rapid kernel makes the cocycle functorial under composition.

## Exact translation law

Define the oriented segment functional

\[
J_K(z;d)=\int_0^d e^{-zw}K(w)\,dw,
\]

using the oriented-integral convention for \(d<0\). Change of variables gives

\[
H_{T_dK}(z)
=e^{zd}\bigl(H_K(z)-J_K(z;d)\bigr).
\]

The bold conjecture fails whenever \(J_K(z;d)\ne0\).

For ordered labels \((n,m)\), the displacement is

\[
d_{nm}=\log\frac mn,
\]

so the character is \((m/n)^z\), while swapping labels reverses the oriented interval.

## Cocycle composition

For two displacements \(d_1,d_2\), splitting the oriented interval at \(d_1\) gives

\[
J_K(z;d_1+d_2)
=
J_K(z;d_1)
+
e^{-zd_1}J_{T_{d_1}K}(z;d_2).
\]

This is the exact cocycle identity required for constructor composition. Substituting it into the translation law yields

\[
H_{T_{d_2}T_{d_1}K}
=
H_{T_{d_1+d_2}K}
\]

with no fitted correction or associativity residual.

## Why one extra scalar is insufficient

For fixed \(z,d\), \(J_K(z;d)\) is scalar. But constructor closure requires all admitted \(d\), every parameter jet, and translated inputs \(T_{d_1}K\). A fixed scalar value does not determine

\[
J_{T_{d_1}K}(z;d_2).
\]

The correction family is therefore function-valued. It can be represented in either of two equivalent ways:

1. retain \(K\) in the rapid radial source and derive every \(J_K(z;d)\);
2. retain the complete compatible family \((J_K(z;d))_{z,d}\) satisfying the cocycle identity.

No finite scalar port is shown to be a coalgebra quotient of this family.

## Jet compatibility

Differentiation gives

\[
\partial_z^jJ_K(z;d)
=(-1)^j\int_0^d w^je^{-zw}K(w)\,dw.
\]

Rapid radial seminorms control these derivatives locally uniformly. Differentiating the cocycle identity therefore supplies coherent composition laws for every parameter jet.

## Minimal G4 comparison target

A compatible successor interface needs a radial response object

\[
\mathcal R_{m G4}
=
\bigl(K,H_K,(J_K(\cdot;d))_d\bigr)
\]

or a proved equivalent quotient. Its translation arrow is triangular:

\[
(K,H_K)
\longmapsto
\bigl(T_dK,
 e^{zd}(H_K-J_K(z;d))\bigr).
\]

The four scalar boundary traces \((P,Q,M,J)\) remain the joint Green trace of the history state. The rapid kernel and oriented Laplace cocycle are continuation/response coordinates, not a fifth instantaneous boundary trace.

## Strongest falsification attempt

Rival 2 would require a fixed scalar statistic \(s(K)\) determining every translated segment integral. Kernels with the same \(s(K)\) but different restrictions to an interval \([d_1,d_1+d_2]\) violate that requirement. Thus no unspecified scalar correction can implement the composition law.

Rival 3 survives exactly: retaining the function-valued kernel makes the action strict through the cocycle identity.

## Disposition

The missing rapid-probe-to-G4 comparison is now typed. G4 must expose a function-valued radial response port carrying the oriented translation cocycle; a Mellin character or one additional scalar is insufficient. This requirement is independent of the still-missing arithmetic loading arrow. A successor contract can compare the retained rapid graph to this target, but the current three-port v2 contract does not declare it.
