# The two-channel positive completion is matrix/Clifford-like but becomes quaternionic only with an additional symplectic sewing symmetry

## The superficial resemblance

The regulated feature has two complex channels,

\[
\mathcal H\oplus\mathcal H,
\]

and a positive `2x2` Gram operator. Since

\[
M_2(\mathbb C)
\]

contains the standard real quaternion algebra, it is natural to ask whether the two-channel completion is quaternionic.

The answer is: **not from the Gram structure alone**.

## Canonical quaternionic structure on two complex channels

Define the antiunitary

\[
\boxed{
\Theta
\begin{pmatrix}\xi\\\eta\end{pmatrix}
=
\begin{pmatrix}-\overline\eta\\\overline\xi\end{pmatrix}.
}
\]

Then

\[
\Theta^2=-I.
\]

Together with ordinary multiplication by `i`, this gives quaternion generators

\[
i^2=\Theta^2=-1,
\qquad
i\Theta=-\Theta i.
\]

Thus every doubled complex Hilbert space can be *equipped* with a quaternionic structure. The substantive question is whether the semilocal operators commute with `Theta`.

## Quaternionic-linearity test

A complex-linear two-channel operator `G` is quaternionic-linear precisely when

\[
\boxed{
G\Theta=\Theta G.
}
\]

For a scalar Hermitian Gram matrix

\[
G=
\begin{pmatrix}
a&z\\
\overline z&d
\end{pmatrix},
\]

the commutation equation forces

\[
a=d,
\qquad
z=0.
\]

Hence a generic positive two-channel Gram matrix is not quaternionic-linear. Doubling alone supplies only `M_2(C)` bookkeeping.

## Test of the channelwise bulk counterterm

The positive bulk counterterm is

\[
\mathcal C_{\Lambda,R}
=
\begin{pmatrix}
V_{in}&0\\
0&V_{ann}
\end{pmatrix}h(1).
\]

It commutes with the canonical quaternionic structure exactly when

\[
\boxed{
V_{in}=V_{ann}.
}
\]

Since

\[
V_{in}=2\log\Lambda,
\qquad
V_{ann}=2\log R-2\log\Lambda
\]

under the symmetric logarithmic-volume normalization, balance requires

\[
2\log\Lambda
=
2\log R-2\log\Lambda,
\]

so

\[
\boxed{
R=\Lambda^2.
}
\]

Thus the correlated cutoff `R=Lambda^2` is distinguished by quaternionic compatibility of the **bulk counterterm**.

This does not prove quaternionic symmetry of the boundary feature.

## Test of a Halmos mode

A generic Halmos/prolate mode has positive rank-one matrix

\[
G_\lambda
=
\begin{pmatrix}
\lambda&
\sqrt{\lambda(1-\lambda)}\\
\sqrt{\lambda(1-\lambda)}&
1-\lambda
\end{pmatrix}.
\]

It does not commute with `Theta` except in degenerate cases, and no nonzero rank-one operator can be a quaternionic scalar on one quaternionic line.

Therefore an individual prolate mode is not quaternionic. Quaternionic symmetry could arise only after adjoining its opposite-polarity partner.

## Opposite-polarity completion

The two semilocal orientations exchange

\[
P_\Lambda Q_\Lambda
\longleftrightarrow
Q_\Lambda P_\Lambda,
\]

\[
J_S
\longleftrightarrow
J_S^{-1},
\]

and inside/outside channels under inversion.

If the missing sewing antiunitary identifies these operations with `Theta`, then the doubled primal/contra system could carry a genuine quaternionic action.

The required identities are of the form

\[
\boxed{
\ThetaP\Theta^{-1}=I-P,
\qquad
\ThetaQ\Theta^{-1}=I-Q,
}
\]

or the corresponding exchanged-orientation formulas, together with

\[
\ThetaU_S(g)\Theta^{-1}
=U_S(g^*)
\]

and compatibility with the boundary quotient.

None of these identities follows merely from positivity of the Gram block.

## Clifford interpretation

Two projections naturally produce centered involutions

\[
\epsilon_P=2P-I,
\qquad
\epsilon_Q=2Q-I.
\]

They satisfy

\[
\epsilon_P^2=
\epsilon_Q^2=I.
\]

Their product and commutator encode the Halmos angle operator. This is more naturally a two-generator reflection/Clifford structure than a quaternionic one.

A quaternionic structure appears only if an additional complex or antiunitary generator converts the two reflections into anticommuting square-minus-one operators.

## Exact acceptance test

The positive completion is genuinely quaternionic only after constructing an antiunitary `Theta_S` such that:

1. `Theta_S^2=-I`;
2. it exchanges the two cutoff polarities;
3. it preserves the regulated two-copy bulk module;
4. it descends through the Eisenstein/radical quotient;
5. the residual boundary Gram operator commutes with `Theta_S`;
6. it transports the Euler phase `J_S` to `J_S^(-1)`.

Without these checks, “quaternionic” is only a useful analogy for the doubled matrix organization.

## Disposition

The present structure is intrinsically

\[
\boxed{
\text{two-projection/Halmos and hence matrix--Clifford-like}.}
\]

It becomes quaternionic only if the missing opposite-polarity sewing supplies a compatible antiunitary square root of `-1`.

The balanced scale

\[
\boxed{R=\Lambda^2}
\]

is a concrete candidate because it makes the two-copy bulk counterterm quaternionically symmetric. Testing the boundary residual at this scale is the next executable quaternionic check.
