# The seam-oriented coth current is a Tate ratio comparator, not an Euler factor

## Correction

Set \(z=s-1/2\). The two local Tate weights are

\[
w_+(z)=p^{-1/2}p^{-z},
\qquad
w_-(z)=p^{-1/2}p^z.
\]

Their ratio is

\[
\frac{w_+(z)}{w_-(z)}=p^{-2z}.
\]

Hence \(r=p^{-z}\) is the square-root ratio coordinate of the two sectoral
weights. It is not either occupation weight itself.

The current

\[
C_p(z)=\frac12\frac{1+p^{-z}}{1-p^{-z}}
\]

therefore measures the reciprocal comparison frame. It does not equal the
logarithmic derivative of \((1-p^{-s})^{-1}\), and its zeros are not zeros of
a local zeta factor.

## What survives

Three exact conclusions remain:

- ratio reciprocity sends \(z\mapsto-z\) and \(r\mapsto r^{-1}\);
- \(C_p(-z)=-C_p(z)\);
- the comparison current's zeros and poles lie on \(\Re z=0\).

The accumulated half-charge also remains:

\[
\frac12\sum_{p\le X}\log p.
\]

It is the divergent normalization of the global comparison frame, not a
term of the ordinary Euler logarithmic derivative.

## Correct next object

At finite cutoff, the comparison determinant is

\[
S_X(z)
=
\prod_{p\le X}
2\sinh\!\left(\frac{z\log p}{2}\right).
\]

Its logarithmic derivative is the sum of the weighted comparison currents.
The determinant is reciprocal up to the parity of the number of primes. Its
global failure is a normalization-line problem.

The genuine zeta Euler factors must enter as separate occupation objects
with the common coefficient \(p^{-1/2}\). The next categorical square must
compare:

- the Tate ratio determinant \(S_X\);
- the two occupation determinants built from \(1-p^{-1/2}p^{\mp z}\);
- their transition units;
- the archimedean completion.

## Result

The coth current is a faithful reciprocal comparator between the two Tate
sectors, not a local Euler factor. Its seam orientation describes the
comparison frame, while its divergent half-charge obstructs globalizing that
frame. Zero confinement still requires coupling this comparator to the
actual occupation determinants.
