# The integrality defect is a positive self-dual Haar deficit

## Fixed sign of the discrepancy

Define

\[
\Omega(t)=\frac1{2\sqrt t}-\Psi(t),
\qquad
\Psi(t)=\sum_{n\geq1}e^{-\pi n^2t}.
\]

For fixed (t>0), the function

\[
x\longmapsto e^{-\pi x^2t}
\]

is strictly decreasing on the positive half-line. Therefore

\[
e^{-\pi n^2t}
<\int_{n-1}^{n}e^{-\pi x^2t}\,dx
\]

for every (n\geq1). Summing gives

\[
\Psi(t)<\int_0^\infty e^{-\pi x^2t}\,dx
=\frac1{2\sqrt t}.
\]

Hence

\[
\Omega(t)>0
\]

for every (t>0). The integrality defect found in the preceding packet is
the negative of a canonical positive density: the Haar mass missing from
integer sampling.

## Exact Poisson sewing

Jacobi inversion gives

\[
\Psi(t)
=\frac{t^{-1/2}-1}{2}+t^{-1/2}\Psi(1/t).
\]

Subtracting from the Haar term yields

\[
\Omega(t)=t^{-1/2}\Omega(1/t).
\]

Thus the Haar deficit is closed under reciprocal sewing. The continuum mode
does not reappear as an extra boundary term: its contribution has already
been paired exactly with the completion carrier.

The completed Mellin function is consequently

\[
\Lambda(s)
=-\int_1^\infty
\Omega(t)\left(t^{s/2}+t^{(1-s)/2}\right)\frac{dt}{t}.
\]

This representation explains the sign of \(\Lambda(s)\) on the real critical
strip directly.

## The even logarithmic kernel

Put

\[
t=e^{2u},
\qquad
k(u)=4e^{u/2}\Omega(e^{2u}),
\qquad u\geq0.
\]

Then (k(u)>0), and with (z=s-1/2),

\[
\Lambda\left(\frac12+z\right)
=-\int_0^\infty k(u)\cosh(zu)\,du.
\]

The reciprocal law for \(\Omega\) says precisely that the extension

\[
k(-u)=k(u)
\]

is even. Therefore the completed source is a positive even Haar-deficit
kernel on logarithmic scale.

On the critical seam (z=i\tau),

\[
\xi\left(\frac12+i\tau\right)
=\frac{\tau^2+1/4}{2}
\int_0^\infty k(u)\cos(\tau u)\,du.
\]

The Riemann zeros are exactly the zeros of the cosine transform of this
positive self-dual deficit kernel.

## Conceptual correction

The previous statement that the completed source is a signed discrepancy was
correct in the orientation \(\Psi-\Psi_{\mathrm H}\), but it obscured a
stronger fact. With the source-natural orientation Haar minus lattice, the
physical kernel is strictly positive.

Completion therefore performs three operations:

1. compare discrete integer sampling with additive Haar sampling;
2. cancel the Haar continuum against the pole carrier;
3. retain the positive missing-mass density with reciprocal sewing.

The resulting positivity is relational. It belongs neither to the lattice
alone nor to the continuum alone, but to their ordered comparison.

## Remaining obstruction

Positive even kernels can have cosine transforms with complicated zero sets,
including off-axis zeros after analytic continuation. Positivity and Poisson
self-duality still do not prove RH; earlier hostile carriers already warn
against that inference.

The source-specific question has nevertheless narrowed again. The missing law
must distinguish this particular Haar-deficit kernel from arbitrary positive
even kernels. Candidate properties should now be tested directly on (k):

- strict total positivity of a translate or Hankel kernel;
- variation diminution under logarithmic translation;
- a source-derived canonical-system Hamiltonian;
- a discrete-convexity law inherited from the integer staircase;
- a conservation law comparing the deficit with its endpoint current.

The sharp falsifier is a positive self-dual Haar-deficit analogue with the
same monotone-sampling proof and an off-seam zero. Such a witness would show
that the missing force lies deeper than positivity, reciprocity, and the
discrete-versus-continuum comparison.

## Operator stimulus

The operator's loss-of-integrality proposal led to the continuum replacement.
The exact carrier cancellation exposed the discrepancy; asking what kind of
object that discrepancy is revealed the positive, self-dual missing-mass
kernel. The surprise therefore generated a second reinterpretation rather
than merely a new formula.
