# The theta-weighted shift has an exact passive Green balance

## State space and generator

Take

\[
\mathcal H_\Phi
=
L^2(\mathbb R_+,\Phi(u)\,du)
\]

and define

\[
Af=-f'.
\]

Use the natural weighted Sobolev domain on which the endpoint trace \(f(0)\) exists and the boundary term at infinity vanishes.

## Green identity

Integration by parts gives

\[
\langle Af,g\rangle_\Phi
+
\langle f,Ag\rangle_\Phi
=
\Phi(0)f(0)\overline{g(0)}
+
\int_0^\infty
f(u)\overline{g(u)}
\Phi'(u)\,du.
\]

The formal weighted adjoint is

\[
A^*g
=
g'
+
\frac{\Phi'}{\Phi}g.
\]

For the completed theta kernel, \(\Phi'(u)<0\) for positive \(u\). Define the endpoint input and distributed output

\[
Bf=
\sqrt{\Phi(0)}f(0),
\]

\[
Cf(u)=
\sqrt{-\Phi'(u)}f(u).
\]

Then the Green balance is

\[
2\operatorname{Re}
\langle Af,f\rangle_\Phi
=
|Bf|^2-
\|Cf\|_2^2.
\]

Equivalently, in quadratic-form notation,

\[
A^*+A
=
B^*B-C^*C.
\]

This is a continuous-time KYP equality with storage operator

\[
P=I_{\mathcal H_\Phi}.
\]

## Functional meaning

The theta-tail shift is passive:

- energy enters through the modular-seam endpoint \(u=0\);
- energy is dissipated through the positive density \(-\Phi'(u)\);
- the stored energy is the theta-weighted \(L^2\) norm.

The endpoint and bulk dissipation are derived from the same source weight. No fitted Green metric is used.

## Spectral sections

For

\[
e_z(u)=e^{-zu},
\]

we have

\[
Ae_z=ze_z.
\]

Thus the bilateral and half-line theta transforms arise as observation pairings of eigen-sections of this passive transport generator. This provides the requested control-system carrier before any Xi zero is named.

## Numerical consistency check

Checker:

`research/voevodsky/checkers/scout_theta_weighted_shift_green_identity.py`

Result:

`research/voevodsky/results/theta-weighted-shift-green-identity-scout.json`

Three independent exponential test pairs satisfy the Green identity to approximately \(10^{-51}\). A grid on \(0<u\le4\) finds \(\Phi'(u)<0\) throughout.

The integration-by-parts identity is exact. The monotonicity scan is not interval certified.

## What this constructs

We now have an explicit common storage element:

\[
P=I.
\]

We also have source-defined input and output operators \(B,C\) satisfying an exact lossless-dissipative balance.

This is stronger than a coordinate tetrahedron: it is an actual passive realization of the theta-tail transport.

## What remains

The current output \(C\) records distributed dissipation. It has not yet been shown that the associated transfer function is

\[
\Theta(z)
=
\frac{X(z)-iX'(z)}{X(z)+iX'(z)}.
\]

That identification requires attaching the two terminal observations generating \(X\) and \(X'\), then proving that their boundary scattering matrix is the Clark ratio above.

Passivity of the shift alone does not imply this determinant identity. The next calculation is therefore finite and explicit:

1. evaluate the boundary transfer matrix on \(e_z\);
2. add the observations corresponding to \(1\) and \(u\);
3. compare its Cayley transfer with \((X-iX')/(X+iX')\);
4. identify the residual boundary term, if any.

## Scope

This constructs a passive theta-tail system, not a proof of the global Pick property. The unresolved issue is whether the physical Xi boundary quotient is the transfer function of this passive realization.
