# The Naive Bulk–Polar Hermitian Pairing Is Not Source-Universal

## Question

Entry 3245 identifies the polar-odd port

\[
R_3(s)=c\frac{2s-1}{s(s-1)}.
\]

Can the missing fourth-tower attachment simply be the Hermitian pairing of
this port with the bulk-odd port

\[
R_2(s)=A_f(s)-A_f(1-s)?
\]

The natural candidate, up to orientation, is

\[
Q_f(s)=-\operatorname{Re}\bigl(R_2(s)\overline{R_3(s)}\bigr).
\]

## Exact hostile fiber

Write \(z=s-\tfrac12\). A positive source atom at scale \(u=1\) contributes

\[
R_2(z)=2w\sinh z,
\qquad
R_3(z)=\frac{2cz}{z^2-\tfrac14},
\]

with \(w,c>0\). Take

\[
z=x+\frac{3\pi i}{2},
\qquad 0<x<\frac12.
\]

Then \(\sinh z=-i\cosh x\), while

\[
\operatorname{Im}\frac{z}{z^2-\tfrac14}
=
-\frac{y(x^2+y^2+\tfrac14)}{|z^2-\tfrac14|^2}<0,
\qquad y=\frac{3\pi}{2}.
\]

Therefore \(Q_f(s)<0\). The opposite global orientation fails near the real
axis. Smooth positive sources approximating the atom preserve the strict
hostile sign; a small positive tail fixing \(c=f(0)>0\) does not remove it.

## Consequence

The fourth-tower Green attachment cannot be the unweighted Hermitian dot
product of the bulk-odd and polar-odd ports. Reciprocal parity gives the right
types but does not orient their comparison.

The next admissible target must retain the operator that transports bulk odd
data into the polar boundary frame. The missing cell is not merely an
evaluation pairing. It is a source-derived mate or Green morphism

\[
R_2\longrightarrow R_3^\vee
\]

whose kernel contains the scale variable and modular boundary incidence. The
hostile atom is the smallest falsifier for any construction forgetting that
transport.

## Status

This closes the naive scalar Hermitian attachment. It does not falsify a
theta-specific Green attachment.

