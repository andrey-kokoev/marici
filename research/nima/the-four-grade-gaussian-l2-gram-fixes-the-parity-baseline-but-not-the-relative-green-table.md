# The four-grade Gaussian L2 Gram fixes the parity baseline but not the relative Green table

## Exact baseline

Let

\[
f_j(x)=x^je^{-\pi x^2},
\qquad j=0,1,2,3.
\]

In the ordinary real \(L^2(\mathbb R)\) pairing,

\[
\langle f_i,f_j\rangle
=
\int_{\mathbb R}x^{i+j}e^{-2\pi x^2}\,dx.
\]

Odd total degree vanishes. For \(i+j=2k\),

\[
\langle f_i,f_j\rangle
=
\frac{(2k-1)!!}{2^{2k}\sqrt2\,\pi^k}.
\]

Thus the exact Gram table is

\[
\frac1{\sqrt2}
\begin{pmatrix}
1&0&\frac1{4\pi}&0\\
0&\frac1{4\pi}&0&\frac3{16\pi^2}\\
\frac1{4\pi}&0&\frac3{16\pi^2}&0\\
0&\frac3{16\pi^2}&0&\frac{15}{64\pi^3}
\end{pmatrix}.
\]

The fourth grade therefore has a positive diagonal energy and a nonzero coupling to \(f_1\):

\[
\langle f_3,f_3\rangle
=\frac{15}{64\sqrt2\pi^3},
\qquad
\langle f_3,f_1\rangle
=\frac3{16\sqrt2\pi^2}.
\]

Any three-grade truncation loses both entries.

## Scope

This table is a source-canonical Hilbert baseline. It is preserved by a common translation applied to both arguments, but it does not determine pairings between differently translated rays. More importantly, it is not automatically the complete relative theta-history Green form.

The completed target may contain:

- Wronskian boundary contributions;
- causal-history graph energy;
- saturated wall/tail sectors;
- radical reduction;
- different translations on the two arguments.

Those terms can alter the quadratic table while preserving the ordinary Gaussian parity pattern only if the full Green form has the corresponding reflection symmetry.

## Use as a hostile

A proposed target table must explain any departure from this baseline. In particular it may not:

1. set the \(f_1\)-\(f_3\) entry to zero solely because \(f_3\) is called a fourth grade;
2. omit the positive \(f_3\) diagonal;
3. use unshifted parity to kill a pairing between differently translated packets;
4. identify ordinary \(L^2\) energy with relative Green energy without a representation theorem.

## Verdict

The fourth-grade ordinary Gram data are now exact. The translated relative Green row and column remain open, so G1.1 is not closed.

Evidence: `research/nima/results/rh-four-grade-gaussian-gram.json`.
