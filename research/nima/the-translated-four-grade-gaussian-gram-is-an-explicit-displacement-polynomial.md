# The translated four-grade Gaussian Gram is an explicit displacement polynomial

Let \(U_af(x)=f(x+a)\) and \(f_j(x)=x^je^{-\pi x^2}\). For \(d=a-b\), completing the square gives

\[
\langle U_af_i,U_bf_j\rangle
=
\frac{e^{-\pi d^2/2}}{\sqrt2}\,P_{ij}(d,\pi^{-1}),
\]

where \(P_{ij}\) is a finite exact rational polynomial. Expanding

\[
(x+a)^i(x+b)^j
=
\left(y+\frac d2\right)^i
\left(y-\frac d2\right)^j,
\qquad
y=x+\frac{a+b}{2},
\]

and integrating even powers of \(y\) determines every entry for \(0\le i,j\le3\).

The exact checker records all sixteen polynomials and verifies

\[
P_{ij}(d)=P_{ji}(-d).
\]

At \(d=0\), the ordinary parity-blocked Gram is recovered. At nonzero displacement, naive parity cancellation fails. For example,

\[
\langle U_af_3,U_bf_0\rangle
=
\frac{e^{-\pi d^2/2}}{\sqrt2}
\left(
\frac{d^3}{8}+rac{3d}{8\pi}
\right),
\]

which is nonzero for real \(d\ne0\). Likewise the differently translated \(f_3\)-\(f_2\) pairing is generally nonzero.

Thus all ordinary Hilbert pairings needed by the translated four-grade packet are now explicit. The remaining G1.1 data are genuinely relative: Wronskian boundary terms, causal-history graph contributions, saturated-topology transport, and radical descent. None can be inferred from unshifted parity.

Evidence: `research/nima/results/rh-translated-four-grade-gaussian-gram.json`.
