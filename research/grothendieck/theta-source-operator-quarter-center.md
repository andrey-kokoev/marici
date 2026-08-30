# The theta source operator generates the quarter center

## Exact source factorization

Let

\[
\Theta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x}
\]

and define the modular profile

\[
A(u)=\frac12e^{u/2}\Theta(e^{2u}).
\]

The theta transformation gives

\[
A(-u)=A(u).
\]

For a positive label, put \(x=\pi n^2e^{2u}\). Direct differentiation gives

\[
\left(\partial_u^2-\frac14\right)
\left(e^{u/2}e^{-x}\right)
=left(4x^2-6x\right)e^{u/2}e^{-x}.
\]

Therefore the completed Mellin amplitude used throughout the theta program is
exactly

\[
\boxed{
\Phi(u)=\left(\partial_u^2-\frac14\right)A(u).
}
\]

The zero label is annihilated by the same operator. Thus using the full theta
series introduces no extra source term and makes modular evenness manifest.

## Why the characteristic center is \(1/4\)

Formally, bilateral Laplace transformation sends

\[
\partial_u^2-\frac14
\quad\longmapsto\quad
z^2-\frac14.
\]

With \(w=z^2\), this multiplier is

\[
\boxed{w-\frac14.}
\]

This is precisely the factor in the normalized angular current

\[
H(w)=\left(w-\frac14\right)\frac{C'(w)}{C(w)},
\]

and precisely the center of the characteristic circles

\[
\left|w-\frac14\right|=R.
\]

Hence the quarter center is not an externally chosen Pick normalization. It
is already the spectral shift of the second-order source operator that turns
the modular theta profile into the completed Xi kernel.

## The boundary-term obstruction

The formal transform cannot be justified by simply discarding endpoint
terms. The modular profile has the asymptotic growth

\[
A(u)\sim\frac12e^{|u|/2}
\qquad(|u|\to\infty).
\]

Its bilateral transform is therefore meromorphic rather than an ordinary
convergent integral across the target strip. The endpoint contribution is the
source of the completed-zeta poles that are cancelled by
\(z^2-1/4\).

In standard completed notation, with \(s=1/2+z\),

\[
z^2-\frac14=s(s-1),
\]

and

\[
\xi(s)=\frac12s(s-1)\Lambda(s).
\]

Thus the entire function \(C(w)\) is a polynomially completed meromorphic
theta transform. Any positive-resolvent argument must retain this pole
cancellation. Removing it by an unjustified integration by parts would erase
the very endpoint data that select the Herglotz sign.

## Operator interpretation

The natural source operator is

\[
L=\partial_u^2-\frac14.
\]

The angular-current multiplier is its transform-side symbol. This suggests a
more concrete operator route than attempting to manufacture an operator whose
spectrum is declared to be the Riemann zeros:

1. treat \(A\) as the modular Green precursor and \(\Phi=LA\) as its localized
   source;
2. formulate the pole-subtracted transform of \(A\) as a resolvent-like
   object in \(w\);
3. derive the imaginary sign of
   \((w-1/4)C'/C\) from a positive boundary or Green identity; and
4. keep the endpoint pole contribution explicit throughout.

The identity supplies the missing reason that the same factor appears in the
source differential operator, the completed zeta normalization, the Pick
vector field, and the characteristic-circle center.

## Immediate square-identity gate

A canonical simultaneous subtraction is available. Define

\[
K(u)=\cosh(u/2)-A(u).
\]

Both terms are even, and \(\cosh(u/2)\) supplies exactly the two asymptotic
null modes of \(\partial_u^2-1/4\). Hence \(K\) decays like
\(e^{-|u|/2}\), up to the superexponential theta correction, and

\[
\boxed{
\Phi(u)=\left(\frac14-\partial_u^2\right)K(u).
}
\]

For \(|\Re z|<1/2\), put

\[
F(z)=\int_{\mathbb R}e^{zu}K(u)\,du.
\]

The endpoint terms now vanish honestly, giving

\[
\boxed{
Z(z)=\left(\frac14-z^2\right)F(z),
}
\]

where \(Z(z)=\int e^{zu}\Phi(u)\,du\). Under the half-line convention used
for the angular current, \(B=Z/2\); this fixed factor has no effect on a
logarithmic derivative or its sign.

Since \(K\) is even, \(F(z)=\mathcal F(w)\) with \(w=z^2\), and therefore

\[
\boxed{
C(w)=\frac12\left(\frac14-w\right)\mathcal F(w).
}
\]

The normalized current reduces to

\[
\boxed{
H(w)=1+\left(w-\frac14\right)
\frac{\mathcal F'(w)}{\mathcal F(w)}.
}
\]

The real constant contributes no imaginary part. Thus the Herglotz problem is
relocated exactly to the logarithmic derivative of the decaying,
pole-subtracted precursor transform.

The precursor can be split once more into its exact decaying null mode and a
positive superexponential theta remainder. Completion sends the null-mode
pole to the constant \(1/4\), giving the globally entire representation
\(C(w)=1/4+(w-1/4)T(w)\). See
`theta-null-mode-critical-renormalization.md`.

This is progress in explanation, not yet in sign: positivity and decay of a
real-space kernel do not generically force its bilateral transform to have
the required Herglotz logarithmic derivative. The next source-specific gate
is whether \(K\) has a stronger total-positivity, Green-kernel, or
variation-diminishing property.

Low-order translation minors pass a first hostile scan through order four,
but PF\(_\infty\) is analytically impossible: \(F\) vanishes at established
critical-line Xi zeros, whereas a PF\(_\infty\) bilateral transform has the
reciprocal Laguerre--Pólya form and cannot have those Fourier-axis zeros. The
surviving target is therefore a centered resolvent/Loewner kernel that permits
real \(w\)-axis zero atoms. See
`theta-renormalized-precursor-finite-tp-latency.md`.

The endpoint subtraction passes exactly in the open critical strip. The next
sharp falsifier is therefore a failure of every admissible stronger kernel
property for \(K\), or a point where
\(\Im((w-1/4)\mathcal F'/\mathcal F)\le0\). Such a failure would show that the
source-operator factorization explains the geometry without itself supplying
the positive resolvent.
