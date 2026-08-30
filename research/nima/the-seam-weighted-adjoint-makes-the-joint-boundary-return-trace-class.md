# The seam-weighted adjoint makes the joint boundary return trace class

## Adjoint is fixed by the coefficient topology

Let the prime coefficient inner product be

\[
\langle x,y\rangle_{\rm seam}
=
\sum_p(\log p)\overline{x_p}y_p.
\]

If the joint incidence is

\[
Bx=\sum_p b_px_p,
\]

then its adjoint is not the raw coordinate transpose. It is

\[
(B^\dagger f)_p
=
\frac{\langle b_p,f\rangle}{\log p}.
\]

The factor \(1/\log p\) is forced by the defining adjoint identity. Omitting
it changes the coefficient topology and generally makes the return
discontinuous.

## Hilbert–Schmidt incidence

After identifying the weighted coefficient space with ordinary \(\ell^2\),
the incidence columns are

\[
\frac{b_p}{\sqrt{\log p}}.
\]

Therefore

\[
\lVert B\rVert_2^2
=
\sum_p\frac{\lVert b_p\rVert^2}{\log p}.
\]

For the primitive common mode \(b_p\sim p^{-1/2}\phi\), this contains

\[
\lVert\phi\rVert^2
\sum_p\frac1{p\log p},
\]

which converges. Under the previously stated residual-tail condition, the full
incidence is Hilbert–Schmidt.

## Trace-class Schur return

Let \(G=(I-A)^{-1}\) be the bounded boundary propagator. The joint return is

\[
R=B^\dagger G B.
\]

The ideal product rule gives

\[
R\in\mathcal S_1,
\qquad
\lVert R\rVert_1
\leq
\lVert G\rVert\lVert B\rVert_2^2.
\]

On the centered seam, the Euler loop satisfies

\[
\lVert L\rVert\leq2^{-1/2}<1.
\]

Hence \((I-L)^{-1}\) is bounded and

\[
K=(I-L)^{-1}R
\]

is trace class. The boundary-mediated comparison therefore has an ordinary
Fredholm determinant

\[
\det(I-K).
\]

## Separation from the bare Euler determinant

This does not eliminate the third-regularization theorem. The bare Euler loop
\(L\) still has primitive, square, and trace-class-tail grades in its original
cyclic presentation.

The topology separates two objects:

- \(L\): the Euler loop, requiring paired low-grade data and \(\det_3\);
- \(K\): the boundary-mediated relative return, trace class after
  seam-weighted incidence.

Conflating them would double-count the primitive current. The global
comparison is a bare Euler determinant chart together with an ordinary
relative Fredholm determinant and its coherence cells.

## DPC verdict

Resolved under the explicit residual-tail hypothesis:

- the unique weighted adjoint return map;
- Hilbert–Schmidt joint incidence;
- trace-class boundary-mediated Schur return;
- ordinary Fredholm determinant for the relative comparison on the seam.

Withheld:

- verification of the residual-tail hypothesis for the exact theta source;
- off-seam boundedness;
- reciprocal projective-infinity and archimedean ports;
- the zero-state-to-phase-current bridge.

The smallest falsifier is a proposed raw transpose return. At finite cutoff it
fails the weighted adjoint identity unless all seam lengths are equal.

## Verification

The checker `check_seam_weighted_adjoint_return.py` verifies the weighted
adjoint identity, failure of the raw transpose, and the exact trace budget of
the positive finite Schur return.
