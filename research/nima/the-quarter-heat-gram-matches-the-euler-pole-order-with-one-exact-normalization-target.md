# The quarter-heat Gram matches the Euler pole order with one exact normalization target

Apply the forced quarter-density smoothing to the counting-metric heat
amplitude:

\[
g_t
=
A^{1/4}e^{-\pi tA/2}\mathbf 1,
\qquad
Ae_n=n^2e_n.
\]

Its polarized Gram is

\[
\langle g_r,g_t\rangle
=
\sum_{n\ge1}
n\,e^{-\pi(r+t)n^2/2}.
\]

Let \(u=(r+t)/2\). Euler--Maclaurin or direct integral comparison gives

\[
\sum_{n\ge1}n e^{-\pi u n^2}
\sim
\int_0^\infty x e^{-\pi u x^2}\,dx
=
\frac{1}{2\pi u}.
\]

Therefore

\[
\langle g_r,g_t\rangle
\sim
\frac{1}{\pi(r+t)}.
\]

This closes the exponent audit. The quarter-heat carrier and the Euler Cauchy
carrier have the same Hankel order.

Their frozen normalizations still differ. The Euler singular kernel near
\(\sigma=\tau=1/2\) is

\[
\frac{4}{\zeta(3/2)^2}\frac1{a+b}.
\]

Under direct identification \(a=r,\ b=t\), an isometric leading-order
comparison requires the amplitude factor

\[
c_{\mathrm{ET}}
=
\frac{2\sqrt{\pi}}{\zeta(3/2)},
\]

because

\[
c_{\mathrm{ET}}^2
\frac1{\pi(r+t)}
=
\frac{4}{\zeta(3/2)^2}\frac1{r+t}.
\]

This number is now a sharp source-normalization target, not a free fitting
parameter. It combines:

- the Gaussian heat normalization \(\pi\);
- the Euler-state normalization \(\zeta(3/2)\);
- and the factor two from the two order sectors \(n\ge m\) and \(m\ge n\).

The quarter-density naturality cell must derive \(c_{\mathrm{ET}}\) from the
Tate/Mellin comparison. Matching only the exponent leaves a scalar gauge that
changes the Schur loading and every later coercivity margin.

The comparison must also identify parameters. Heat time and Mellin
displacement are different source coordinates. A source map may give

\[
r=\lambda a,\qquad t=\lambda b.
\]

Then the required amplitude changes by \(\sqrt{\lambda}\). Hence the frozen
scale conversion and amplitude normalization must be proved together.

The first finite audit packet is now only two-dimensional in parameter space:

1. construct \(g_t\) from the quarter-density heat lift;
2. derive the Tate map between \(t\) and \(a\);
3. compute the induced leading Gram coefficient;
4. compare it with \(4/\zeta(3/2)^2\);
5. verify that the regular remainder is bounded as \(a,b\downarrow0\).

The sharp hostile has the correct \((a+b)^{-1}\) pole but coefficient
\(c\ne4/\zeta(3/2)^2\). It passes topology and rank tests while failing the
source normalization required for a completion-stable Schur interface.
