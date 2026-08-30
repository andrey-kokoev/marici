# A Positive Cross Minor Is a Spin-Two Frame Coordinate

Restrict the abstract readout mismatch to a real symmetric positive-definite
matrix

\[
M=\begin{pmatrix}a&b\\b&d\end{pmatrix}.
\]

Define the trace, determinant, and labelled anisotropy coordinates

\[
t=a+d,
\qquad
\Delta=ad-b^2,
\qquad
q=a-d,
\qquad
r=2b.
\]

They satisfy

\[
q^2+r^2=t^2-4\Delta.
\]

The unordered spectrum fixes \(t\), \(\Delta\), and therefore the radius
\(\sqrt{q^2+r^2}\). It does not fix the labelled direction \((q,r)\). Under a
rotation of the eigenframe through angle \(\theta\),

\[
q=(\lambda_1-\lambda_2)\cos2\theta,
\qquad
r=(\lambda_1-\lambda_2)\sin2\theta.
\]

This is a spin-two frame coordinate.

The positive symmetric cross minor is

\[
X=b^2=\frac{r^2}{4}
=
\frac{t^2-4\Delta-q^2}{4}.
\]

Hence trace and determinant plus one labelled quadrature magnitude \(q^2\)
recover \(X\). Equivalently, the diagonal product is

\[
ad=\Delta+X.
\]

This supplies the geometric meaning of the one scalar reference identified in
the determinant-kernel theorem.

## Magnitude versus orientation

The cross minor \(b^2\) is blind to the sign of \(b\). Reflection of the
labelled frame sends

\[
r\longmapsto-r
\]

while preserving \(q\), spectrum, determinant, and \(X\). Therefore:

- recovering the cross-minor magnitude needs one quadrature-magnitude port;
- recovering the signed off-diagonal coordinate needs an additional \(C_2\)
  orientation bit whenever \(b\ne0\);
- at \(b=0\), the sign frame is singular and no orientation bit is operative.

This is the same hierarchy as the earlier torsor correction: a bit selects an
orientation sheet but does not reconstruct the continuous eigenframe angle.

## Exact rational frame

Rotate \(\operatorname{diag}(2,1)\) using the rational orthogonal frame with
\(\cos\theta=3/5\), \(\sin\theta=4/5\). Then

\[
q=-7/25,
\qquad
r=24/25,
\qquad
X=144/625.
\]

The reflected frame has \(r=-24/25\) and the same cross minor. Both retain
trace three, determinant two, and eigenvalues \(2,1\).

## Authority boundary

This theorem applies only if Grothendieck's Weyl/theta packet is source-typed
as a symmetric positive \(2\times2\) form in a declared labelled basis. If the
actual lower minor is nonsymmetric \(bc\), complex, or belongs to a different
block, the spin-two formula changes. The current theta application therefore
remains frozen.

The abstract result says what a suitable source row would measure: a labelled
anisotropy quadrature, not another eigenvalue or positivity certificate.

## Falsifiers

- Unordered eigenvalues are used to choose a labelled eigenframe angle.
- The even cross minor \(b^2\) is treated as a signed off-diagonal entry.
- An orientation bit is used to reconstruct the continuous angle.
- The symmetric formula is applied to a nonsymmetric or complex lower minor.
- Theta instantiation resumes before the labelled basis and block are derived.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to identify the geometric content of the one missing
determinant-kernel reference.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The port is a spin-two quadrature magnitude, its residual sign is a
separate \(C_2\) frame, and the exact scope of the symmetric-positive model is
frozen.
