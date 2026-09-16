# The moving real-boundary rotor decouples from the fixed completed endpoint graph at the crossing limit

## Objective

Determine the interaction between:

1. the moving hostile rotor supported at real spectral points \(\pm\gamma\);
2. the fixed completed endpoint evaluations at \(z=\pm i/2\).

The channels are not orthogonal at finite crossing width, but their coupling vanishes as the divisor reaches the real boundary, provided no finite-width pole collides with a fixed endpoint.

## Elementary model vector

For \(b>0\), the normalized model-space vector at the crossing center \(\gamma\in\mathbb R\) is

\[
e_{\gamma,b}(z)
=
\sqrt{
\frac b\pi
}
\frac1{
z-\gamma+ib
}.
\]

Its boundary norm is one, and its squared boundary modulus is the Poisson phase-energy density.

## Fixed endpoint evaluations

At the completed endpoints,

\[
e_{\gamma,b}(i/2)
=
\sqrt{
\frac b\pi
}
\frac1{
-
\gamma+i(b+1/2)
},
\]

and

\[
e_{\gamma,b}(-i/2)
=
\sqrt{
\frac b\pi
}
\frac1{
-
\gamma+i(b-1/2)
}.
\]

Therefore

\[
|e_{\gamma,b}(i/2)|^2
=
\frac{b/\pi}
{
\gamma^2+(b+1/2)^2
},
\]

\[
|e_{\gamma,b}(-i/2)|^2
=
\frac{b/\pi}
{
\gamma^2+(b-1/2)^2
}.
\]

## Crossing limit

For every fixed real \(\gamma\), away from the isolated finite-width collision discussed below,

\[
e_{\gamma,b}(i/2)
=
O(
\sqrt b
),
\]

\[
e_{\gamma,b}(-i/2)
=
O(
\sqrt b
)
\]

as \(b\downarrow0\).

Hence

\[
\boxed{
\lim_{b\downarrow0}
e_{\gamma,b}(
\pm i/2
)
=0.
}
\]

The normalized rotor retains unit real-boundary phase energy while its fixed endpoint evaluations vanish.

## Symmetry-completed rotor plane

For

\[
B_{b,\gamma}
=
b_{\gamma,b}
b_{-
\gamma,b},
\]

use the ordered Takenaka basis

\[
e_{+,b}
=
e_{\gamma,b},
\qquad

e_{-,b}
=
b_{
\gamma,b}
e_{-
\gamma,b}.
\]

At either fixed endpoint, the Blaschke prefactor remains bounded as \(b\downarrow0\) for \(\gamma\ne0\). Therefore

\[
e_{+,b}(
\pm i/2
)
	o0,
\qquad

e_{-,b}(
\pm i/2
)
	o0.
\]

Define the endpoint-coupling matrix

\[
C_{end\leftarrow rot}(b,\gamma)
=
\begin{pmatrix}
e_{+,b}(i/2)&e_{-,b}(i/2)\\
e_{+,b}(-i/2)&e_{-,b}(-i/2)
\end{pmatrix}.
\]

Then

\[
\boxed{
\|C_{end\leftarrow rot}(b,\gamma)
\|
=
O(
\sqrt b
)
}
\]

for every fixed \(\gamma>0\).

Thus the moving rotor and fixed endpoint graph become asymptotically decoupled at the boundary crossing.

## Endpoint swap metric

The fixed endpoint sector carries the swap form

\[
J_{end}
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

Pulling this form back to the rotor plane gives

\[
C_{end\leftarrow rot}^*
J_{end}
C_{end\leftarrow rot}.
\]

Its norm satisfies

\[
\left\|
C_{end\leftarrow rot}^*
J_{end}
C_{end\leftarrow rot}
\right\|
=
O(b).
\]

Therefore no nonzero endpoint odd-parity square survives on the limiting moving rotor.

This proves quantitatively that the real-boundary crossing cycle does not transfer into the fixed endpoint negative line.

## Finite-width interaction

At \(b>0\), the coupling is generally nonzero. Hence the three-channel Green object

\[
\text{regular bulk}
\oplus
\text{moving rotor}
\oplus
\text{fixed endpoint graph}
\]

is not an orthogonal direct sum before taking the crossing limit.

The exact coupled Green matrix contains blocks

\[
\begin{pmatrix}
G_{bulk}&B_{bulk,rot}^*&B_{bulk,end}^*\\
B_{bulk,rot}&G_{rot}&C_{end\leftarrow rot}^*\\
B_{bulk,end}&C_{end\leftarrow rot}&J_{end}
\end{pmatrix}.
\]

The rotor--endpoint block vanishes at rate \(O(\sqrt b)\), and its Schur contribution vanishes at rate \(O(b)\).

## Exceptional finite-width collision

The lower endpoint evaluation has denominator

\[
-
\gamma+i(b-1/2).
\]

It becomes singular only if

\[
\gamma=0,
\qquad
b=1/2.
\]

This is a genuine collision of the elementary model-space pole with the fixed point \(-i/2\). It is not the hostile boundary crossing \(b\downarrow0\).

Such a collision must be treated in a merged divisor/endpoint chart; the separate rotor and endpoint coordinates cease to be valid there.

For every crossing packet with either \(\gamma>0\) or sufficiently small \(b\), this exceptional locus is avoided.

## Dagger

Centered dagger exchanges \(\gamma\) and \(-\gamma\) and swaps the two fixed endpoints. Consequently

\[
C_{end\leftarrow rot}
\]

obeys the corresponding Real matrix relation. The \(O(\sqrt b)\) decay is the same in both dagger-related entries.

Thus asymptotic decoupling respects completed symmetry.

## Infinite rotor packets

For an infinite symmetry-completed packet, the total rotor--endpoint Hilbert--Schmidt coupling is controlled by sums of the form

\[
\sum_j
\frac{
b_j
}
{
\gamma_j^2+(b_j\pm1/2)^2
}.
\]

Under a uniform Blaschke bound and exclusion of endpoint collisions, these sums are finite after the same observer localization used for the infinite rotor projection.

If all active widths tend to zero with a summable majorant, dominated convergence gives vanishing total rotor--endpoint coupling.

Without such a uniform majorant, factorwise decoupling does not justify interchange with the infinite sum.

## Tetrahedral consequence

At the crossing stratum, the terminal object decomposes to leading order as

\[
C_{13,7}^{cross}
=
C_{13,7}^{reg}
\oplus
\mathcal R_\gamma
\oplus
\mathscr H_{end},
\]

with zero rotor--endpoint cross block.

This direct sum is valid at the limiting crossing fiber. It must not be imposed at finite \(b\), where the Green cross block is small but nonzero.

The affine clutching acts on \(\mathcal R_\gamma\), while the fixed endpoint swap form remains unchanged.

## Consequence for negative index

The moving hostile crossing changes the interior negative index by two. The fixed endpoint odd line retains its independent index-one role.

Because their cross block vanishes at the crossing limit, the two indices do not cancel automatically. Any cancellation must come from a separate physical bulk coupling, not from identifying the moving rotor with the fixed endpoint channel.

## Disposition

The moving rotor and fixed completed endpoint graph are analytically distinct and asymptotically decoupled:

\[
\boxed{
\|C_{end\leftarrow rot}(b,\gamma)
\|
=
O(
\sqrt b
),
\qquad
b\downarrow0.
}
\]

The only direct collision occurs at the separate exceptional locus \((\gamma,b)=(0,1/2)\).
