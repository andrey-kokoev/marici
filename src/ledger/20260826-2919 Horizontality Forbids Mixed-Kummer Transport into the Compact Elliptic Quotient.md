# 2919 — Horizontality Forbids Mixed-Kummer Transport into the Compact Elliptic Quotient

## Relative coefficient type

At the bridge face, order the coefficient basis as

\[
(1,F_L,F_R,F_LF_R,\omega_0,\omega_2).
\]

The forget-the-marks morphism is

\[
R_{\rm forget}
=
\begin{pmatrix}
0&0&0&0&1&0\\
0&0&0&0&0&1
\end{pmatrix}.
\]

Its kernel contains the complete pointed Kummer tensor object, including the
mixed line \(F_LF_R\).

## Horizontal block constraint

If the source relative Gauss–Manin system extends over the normal directions,
the forgetful map must satisfy

\[
R_{\rm forget}A_{\rm total}
=
A_{\rm ell}R_{\rm forget}.
\]

Writing the total connection in kernel-plus-quotient order, this identity
forces

\[
A_{\rm total}
=
\begin{pmatrix}
A_{\rm K}&B_{\rm ell\to K}\\
0&A_{\rm ell}
\end{pmatrix}.
\]

The block from the marked kernel into compact elliptic cohomology must vanish.
An extension in the opposite direction may remain.

## Consequence for the mixed class

Because

\[
R_{\rm forget}(F_LF_R)=0,
\]

horizontality gives

\[
R_{\rm forget}\nabla(F_LF_R)=0.
\]

Thus the mixed Kummer line cannot acquire an elliptic quotient component in
any correctly typed horizontal lift.

## Status

This is a conditional no-mixing theorem.  Its algebra is exact, but its premise
must still be constructed for the double-triangle source: the complete
moving-fiber relative coefficient system and the horizontal forget-marks map.

Therefore the remaining alternatives are narrower:

- the mixed line persists inside the marked kernel;
- it becomes torsion inside that kernel;
- the required relative Gauss–Manin extension fails to exist.

Direct mixing into compact elliptic cohomology is not an admissible fourth
outcome.

## Next finite construction

Derive the marked denominator sections of the double-triangle moving-fiber
family from the twenty-one-variable contour and construct its relative de Rham
complex.  The first acceptance gate is a horizontal forget-marks morphism
specializing to the matrix above.

## Durable artifacts

- `research/benincasa/check_mixed_kummer_horizontal_kernel.py`
- `research/benincasa/mixed-kummer-horizontal-kernel.json`
