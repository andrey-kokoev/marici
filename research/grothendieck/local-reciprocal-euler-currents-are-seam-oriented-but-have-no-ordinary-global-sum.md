# Local reciprocal Euler currents are seam-oriented but have no ordinary global sum

## Typing correction

The coordinate \(r=p^{-z}\) below is the square-root ratio between the two
centered Tate weights, not the occupation variable of the zeta Euler factor:

\[
p^{-s}=p^{-1/2}p^{-z},
\qquad
p^{s-1}=p^{-1/2}p^z.
\]

Accordingly, \(C_p\) is a reciprocal comparison-frame current. Its local
zeros are not local zeta zeros, and its right-chart series is not the
ordinary zeta Euler current. The seam orientation and divergent half-charge
claims remain valid for the comparison frame.

## Spectral specialization

Use the centered spectral coordinate

\[
z=s-\frac12
\]

and specialize the reciprocal scale coordinate at a prime by

\[
r=p^{-z}.
\]

Then \(z\mapsto-z\) sends \(r\mapsto r^{-1}\), exactly matching reciprocal
scale reflection.

The centered comparison current becomes

\[
C_p(z)
=
\frac12\frac{1+p^{-z}}{1-p^{-z}}
=
\frac12\coth\!\left(\frac{z\log p}{2}\right).
\]

It satisfies

\[
C_p(-z)=-C_p(z).
\]

## Local seam orientation

The zeros of \(C_p\) occur at

\[
z=\frac{(2k+1)\pi i}{\log p},
\qquad k\in\mathbb Z,
\]

and its poles occur at

\[
z=\frac{2k\pi i}{\log p}.
\]

Every comparison-frame event lies on \(\Re z=0\). Thus the reciprocal
current is a local model of seam orientation derived without using
Riemann-zero data.

This local fact does not imply that a sum of such currents has only seam
zeros. Sums of nonvanishing off-seam terms can cancel.

## Global assembly obstruction

In the right Euler chart \(\Re z>0\),

\[
C_p(z)
=
\frac12+sum_{k\geq1}p^{-kz}.
\]

After applying the spectral scale derivative, the local contribution is

\[
(\log p)C_p(z)
=
\frac{\log p}{2}
+
(\log p)\sum_{k\geq1}p^{-kz}.
\]

The second term is the geometric expansion of the comparison ratio, not the
ordinary zeta prime-power current. The first term is the reciprocal
half-density charge. Summed over primes, it diverges:

\[
\frac12\sum_p\log p=+\infty.
\]

Therefore the manifestly reciprocal-centered local currents do not possess
an ordinary global sum.

## Why subtraction is not a solution

Subtracting \((\log p)/2\) prime by prime produces the decaying right-chart
comparison series. But that subtraction chooses one sector and destroys the
manifest odd law \(C_p(-z)=-C_p(z)\). The removed terms must remain as typed
relative boundary data.

The global object must therefore be a relative current consisting of:

- the decaying sectoral comparison tail;
- the divergent primitive half-charge;
- the reciprocal comparison between the two;
- the archimedean completion channel;
- the seam phase.

## Finite-cutoff determinant

For a finite prime set, the current is the logarithmic derivative of

\[
\prod_{p\leq X}
2\sinh\!\left(\frac{z\log p}{2}\right).
\]

This product is source-derived and reciprocal up to its parity. Its failure
to converge as \(X\to\infty\) is precisely the accumulated half-charge, not
a defect of any individual prime factor.

## Scope

Local seam confinement is exact but is not RH evidence by itself. The global
relative regularization and its coupling to the theta archimedean channel
remain unproved. A regularization chosen after seeing the desired divisor
would be circular.

## Result

Each prime supplies a reciprocal-centered comparison current whose zeros and
poles lie on the critical axis. The local half-density charges accumulate to
a divergent global comparison current, so ordinary summation cannot preserve
both sectoral decay and reciprocal symmetry. The next theorem must build the
global comparison frame as a source-derived relative object.
