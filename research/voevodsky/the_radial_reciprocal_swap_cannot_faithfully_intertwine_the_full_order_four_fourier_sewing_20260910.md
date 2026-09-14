# The radial reciprocal swap cannot faithfully intertwine the full order-four Fourier sewing

## Question

Can the phase-decorated radial involution \(W_u\) be directly identified with the full retained Fourier--Poisson sewing operator by an injective comparison map?

## Claim boundary

Not on the complete four-character Fourier packet. The radial swap is an involution with eigenvalues \(\pm1\), while the full Fourier action has nonzero \(\pm i\) character sectors. Any direct intertwiner kills those sectors. A faithful comparison must instead identify the radial swap with the square/reflection part of Fourier sewing or lift the radial target by a metaplectic line carrying the missing order-four phase.

## Problem

Prior radial work forces

\[
W_u=
\begin{pmatrix}0&u^{-1}\\u&0\end{pmatrix},
\qquad
W_u^2=I.
\]

The retained Fourier boundary packet decomposes as

\[
X_{m FP}
=X_1\oplus X_{-1}\oplus X_i\oplus X_{-i},
\]

with

\[
W_{m FP}x_\lambda=\lambda x_\lambda.
\]

## Bold conjecture

There is an injective comparison \(C\) on the full packet satisfying

\[
CW_{m FP}=W_uC.
\]

## Named rivals

1. A direct intertwiner necessarily annihilates the \(\pm i\) sectors.
2. The radial involution represents \(W_{m FP}^2\), not \(W_{m FP}\).
3. A metaplectic or line-valued lift gives the radial target an order-four action.
4. The odd Fourier sectors may be quotiented away without changing the four-port observer.

## Strongest falsification attempt

Take \(x_i\in X_i\). Intertwining gives

\[
W_uCx_i=CW_{m FP}x_i=iCx_i.
\]

Applying \(W_u\) again yields

\[
Cx_i=W_u^2Cx_i=i^2Cx_i=-Cx_i.
\]

Therefore

\[
Cx_i=0.
\]

The same argument gives \(Cx_{-i}=0\). Hence

\[
X_i\oplus X_{-i}\subseteq\ker C.
\]

No injective direct intertwiner exists when either odd character sector is nonzero. Both are required by the cyclic four-port observer, so rival 4 is prohibited unless a separately proved quotient changes the observer claim.

## Corrected comparison alternatives

### Fourier-square comparison

Since \(W_{m FP}^2\) has eigenvalues \(\pm1\), the radial reciprocal swap can represent the reflection or half-turn action:

\[
CW_{m FP}^2=W_uC.
\]

This preserves the even/odd reciprocal split but does not identify one quarter-turn Fourier generator.

### Metaplectic lift

Alternatively enlarge the radial target by a line or double-cover coordinate and define an operator \(\widetilde W_u\) with

\[
\widetilde W_u^2=Z,
\qquad
Z^2=I,
\]

where the central action \(Z\) is \(-I\) on the lifted odd plane. Then \(\widetilde W_u\) can carry eigenvalues \(\pm i\) and admit an order-four comparison

\[
CW_{m FP}=\widetilde W_uC.
\]

The lift must come from the already retained metaplectic or determinant line; an arbitrary square root is not source-authorized.

## Boundary-form compatibility

The radial involution satisfies

\[
W_u^*J_\partial W_u=-J_\partial.
\]

This anti-isometry is compatible with a reciprocal half-turn. A quarter-turn lift must specify how the line-valued boundary form transforms at each step so that its square reproduces this sign. This is exactly where the metaplectic line belongs in the morphism type.

## Dagger consequence

The Real comparison between analytic transpose and Hermitian adjoint should be tested against the corrected generator:

- against \(W_{m FP}^2\) for the unlifted radial double; or
- against \(\widetilde W_u\) for the metaplectic lift.

Testing it against \(W_u\) as though \(W_u=W_{m FP}\) is spectrally inconsistent before any domain question arises.

## Disposition

The direct full-order sewing comparison proposed previously is rejected. The radial swap is at most the reciprocal half-turn of the Fourier action. A faithful G4 interface must either compare \(W_u\) with \(W_{m FP}^2\) or declare a source-derived metaplectic lift \(\widetilde W_u\) carrying all four Fourier characters. The next source question is which of these two roles the intended G4 sewing assigns to its reciprocal operator.
