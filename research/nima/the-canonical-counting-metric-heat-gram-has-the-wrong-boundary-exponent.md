# The canonical counting-metric heat Gram has the wrong boundary exponent

There is one immediate positive metric available before the full Green theorem:
the integer-label counting metric.

Let

\[
A e_n=n^2e_n
\]

on \(\ell^2(\mathbb N)\), and for heat time \(t>0\) define

\[
h_t
=
A^{1/2}e^{-\pi tA/2}\mathbf 1,
\]

where the formal vacuum \(\mathbf 1=(1,1,\ldots)\) becomes an admitted vector
after positive heat displacement. Then

\[
\|h_t\|^2
=
\sum_{n\ge1}n^2e^{-\pi t n^2}
=
H_1(t),
\]

and the polarized Gram is

\[
\langle h_r,h_t\rangle
=
\sum_{n\ge1}n^2
e^{-\pi(r+t)n^2/2}
=
H_1\!\left(\frac{r+t}{2}\right).
\]

This construction is canonical relative to the counting metric and heat
generator. It therefore supplies a legitimate first candidate for the
primitive heat Green form.

Its boundary order, however, does not match the Euler Hankel channel under
direct parameter identification. The standard small-time asymptotic is

\[
H_1(t)
\sim
\int_0^\infty x^2e^{-\pi t x^2}\,dx
=
\frac{1}{4\pi}t^{-3/2}.
\]

Hence

\[
\langle h_r,h_t\rangle
\sim
\frac{\sqrt2}{2\pi}(r+t)^{-3/2}.
\]

The Euler singular kernel is instead

\[
\frac{4}{\zeta(3/2)^2}(a+b)^{-1}.
\]

Thus the raw heat-energy orbit has spectral weight of order \(u^{1/2}du\),
whereas the Euler Cauchy wall requires flat weight \(du\).

This is a useful falsifier, not yet a contradiction between the two source
charts. The heat times \(r,t\) and Mellin displacements \(a,b\) are not
automatically the same parameter. A Mellin transform, fractional integration,
or relative Green resolvent may change the exponent. But a direct
identification

\[
a=t,\qquad b=r
\]

is excluded.

The exponent gap is exactly one half. Formally, applying \(A^{-1/4}\) to the
heat amplitude replaces the coefficient \(n\) by \(n^{1/2}\); its continuum
Gram has order

\[
(r+t)^{-1}.
\]

Therefore the minimal analytic bridge is a quarter-power smoothing of the
heat amplitude, equivalently a half-order change in its energy density.

That bridge is admissible only if the complete theta Green/Stokes source
derives the fractional power. It cannot be inserted because it matches the
desired pole.

The next exact source question is:

> Does the Mellin/Tate boundary map act on the primitive heat amplitude by the
> source-derived quarter-power \(A^{-1/4}\), or by an equivalent fractional
> integral, before comparison with the Euler Cauchy carrier?

If yes, the boundary exponent matches and only normalization remains. If no,
the primitive \(H_1\) counting-metric Gram cannot supply the Euler wall.

The sharp hostile chooses \(A^{-1/4}\) retrospectively from exponent matching
without deriving it from Mellin half-density typing.
