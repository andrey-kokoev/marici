# Full Determinant Needs One Kernel Reference to Recover the Cross Minor

For a labelled \(2\times2\) coefficient matrix

\[
M=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]

define the diagonal product and cross minor

\[
P=ad,
\qquad
X=bc.
\]

The full determinant readout is

\[
\Delta=P-X.
\]

As a linear map on the invariant packet \((P,X)\), it has kernel

\[
\ker\Delta=\operatorname{span}\{(1,1)\}.
\]

Therefore \(X\) does not descend through \(\Delta\): simultaneous shifts

\[
(P,X)\longmapsto(P+t,X+t)
\]

preserve the full determinant while changing the cross minor.

## Minimal reference theorem

Let an additional scalar reference be

\[
R=\alpha P+\beta X.
\]

Then the joint readout \((\Delta,R)\) is faithful on the labelled invariant
packet exactly when

\[
\alpha+\beta\ne0.
\]

This is precisely the kernel-reference theorem: \(R\) must be nonzero on
\((1,1)\). One scalar port is both necessary and sufficient.

The simplest candidate is the diagonal product \(P\), for which

\[
X=P-\Delta.
\]

The sum \(P+X\) is another valid reference, giving

\[
X=\frac{(P+X)-\Delta}{2}.
\]

Algebra identifies the class of sufficient ports; it does not authorize any
particular one in the theta/Tate source.

## Positivity and spectrum do not supply the reference

Consider the positive-definite matrices

\[
M_0=\begin{pmatrix}2&0\\0&1\end{pmatrix},
\qquad
M_1=\begin{pmatrix}3/2&1/2\\1/2&3/2\end{pmatrix}.
\]

Both have trace three, determinant two, and eigenvalues \(2,1\). Yet

\[
X(M_0)=0,
\qquad
X(M_1)=1/4.
\]

Thus positivity, full rank, determinant, trace, and complete unordered
spectrum still do not determine the labelled cross minor. The missing datum is
the eigenframe relative to the source-labelled diagonal/cross decomposition.

## Strength of the obstruction

This theorem grants the readout the exact determinant value. A statement that
knows only full Weyl rank, determinant sign, or Cayley positivity is weaker,
so the non-descent obstruction applies a fortiori.

If the source supplies labelled diagonal entries \(a,d\), their product is the
needed reference. If it supplies trace and diagonal imbalance, then

\[
P=\frac{(a+d)^2-(a-d)^2}{4}
\]

recovers the same port. Without such a source-derived labelled reference, the
theta cross minor remains outside the full-determinant quotient.

## Authority boundary

No theta-specific identification is asserted. The actual Weyl determinant,
theta cross minor, and their labelled matrix entries must be supplied by
Grothendieck. Only after that typing may this compiler decide whether an
existing source row is nonzero on the determinant kernel. Seam and resistance
optimization remain frozen until this gate passes.

## Falsifiers

- Full positivity or rank is used to reconstruct a labelled cross minor.
- Trace plus determinant is treated as an eigenframe measurement.
- The diagonal product is imported because it solves the algebra rather than
  derived from the source.
- Unordered spectral data are confused with labelled matrix entries.
- Seam optimization resumes before the determinant-to-cross-minor port is
  source-authorized.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to classify the lower-minor readout mismatch without
projecting any abstract seam theorem into theta.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The determinant kernel is one-dimensional, one nonconstant reference
port is minimally sufficient, and positive isospectral hostiles prove that
the missing datum is a labelled eigenframe coordinate.
