# The mixed bulk--endpoint coupling is a Clifford bicomplex, not a direct intertwiner

## Objective

Retype the remaining coupling between the completed endpoint bundle and the
gamma--prime/Sonin Green form.

## Direct intertwining is impossible

The tempting equation

\[
(\partial_x^2-\tfrac14)T_S
=T_S(-i\partial_t+V_{loc,S})
\]

cannot hold for a nonzero Fourier-multiplier comparison. After Fourier
transform, its left side is multiplication by \(-(t^2+1/4)\), while its right
side contains a first derivative of every test vector. Equality forces the
multiplier to vanish. A boundedly invertible intertwiner is also excluded by
the incompatible essential spectra.

Therefore the open mixed Green coupling must not be formulated as an
identification of the endpoint Laplacian with the Euler connection.

## Correct canonical pair

On the common spectral carrier define

\[
X=M_t,
\qquad
D_S=-i\partial_t+V_{loc,S}(t).
\]

Then

\[
\mathcal F(\partial_x^2-\tfrac14)\mathcal F^{-1}
=-(X^2+\tfrac14)
\]

and

\[
[D_S,X]=-iI.
\]

Thus endpoints and the gamma--prime current are transverse canonical
directions. Their exact coupling datum is the Heisenberg commutator, not a
chain-map equality.

## Four-component realization

Let \(\gamma_1,\ldots,\gamma_4\) be Hermitian Clifford generators and write
\(A_S'=V_{loc,S}\). Define

\[
\mathbb D_S
=
\gamma_1(-i\partial_t)
+
\gamma_2A_S
+
\gamma_3X
+
\frac12\gamma_4.
\]

Its square is

\[
\boxed{
\mathbb D_S^2
=D^2+A_S^2+X^2+\frac14
+
\Gamma_{12}V_{loc,S}
+
\Gamma_{13},}
\]

where

\[
\Gamma_{12}=-i\gamma_1\gamma_2,
\qquad
\Gamma_{13}=-i\gamma_1\gamma_3.
\]

Clifford-channel extraction gives

\[
\frac14\operatorname{tr}_{Cl}
(\Gamma_{12}\mathbb D_S^2)=V_{loc,S},
\]

\[
\frac14\operatorname{tr}_{Cl}
(\Gamma_{13}\mathbb D_S^2)=I.
\]

Hence the local Weil current and endpoint Heisenberg orientation already occupy
orthogonal matrix channels of one source-typed operator. The scalar bulk
contains \(X^2+1/4\), exactly the endpoint mass polynomial.

## Relation to the completed endpoint bundle

The endpoint pair is the generalized null fiber of

\[
X^2+\frac14
\]

at \(t=\pm i/2\), equivalently the harmonic cokernel of
\(\partial_x^2-1/4\). Its actual evaluation is a residue/boundary operation,
not the local matrix coefficient \(I\) extracted from the Clifford square.

The reflected logarithmic differential

\[
\Omega_S(z)dz
=
\left[
\frac1{2i}\partial_z\log\frac{M_S(z)}{M_S^\#(z)}
+
\varepsilon_{end}\frac{2z}{z^2+1/4}
\right]dz
\]

already combines the two channels at the signed contour level: its real
boundary is the gamma--prime current and its residues are the endpoint swap
form. This is the correct signed mixed Green object.

## What is closed

- endpoint and local current live on one canonical \((X,D_S)\) carrier;
- their cross relation \([D_S,X]=-iI\) is exact;
- the four-component Clifford square separates both channels exactly;
- the reflected contour differential combines current and endpoint residues;
- prime succession changes only the logarithmic-current channel and is flat;
- endpoint residue transport remains the exact metric natural bundle already
  constructed.

## Remaining analytic realization

The Clifford heat coefficient does not automatically equal analytic evaluation
at \(\pm i/2\). The remaining coupling theorem must therefore be formulated as
a boundary-triple or relative-resolvent identity:

1. close \(\mathbb D_S\) on a domain compatible with the Sonin absolute graph
   form and the second-order endpoint trace domain;
2. construct the boundary trace \(\Gamma\) for that closure;
3. prove that the boundary/Weyl function has jump and residues equal to
   \(\Omega_S\);
4. identify its endpoint residue matrix with the transported swap metric;
5. prove compatibility under prime and cutoff successors.

A scalar Herglotz factorization is impossible because the endpoint swap form
has one negative parity direction. Any positive realization must be matrix
Nevanlinna/Krein valued.

## Status change

“Completed endpoints constructed, mixed bulk Green coupling open” is now more
precise:

\[
\boxed{
\text{signed algebraic and contour coupling: constructed;
boundary-resolvent realization: open}.}
\]

The failed direct-intertwiner route is closed and should not be retried. The
next nonredundant object is the boundary triple/Weyl function of the
four-component Clifford operator.

## Repository dependencies

- `no-nonzero-local-intertwiner-can-identify-the-euler-phase-connection-with-the-endpoint-shifted-laplacian.md`
- `the-four-component-clifford-bicomplex-separates-the-local-weil-current-from-the-oscillator-index-but-does-not-yet-produce-endpoint-evaluation.md`
- `a-single-reflected-logarithmic-contour-differential-unifies-the-local-weil-current-and-endpoint-residues.md`
- `globally-completed-endpoint-channels-form-a-source-reached-metric-natural-bundle.md`
- `the-sonin-green-form-is-closed-in-the-absolute-connection-graph-norm.md`
