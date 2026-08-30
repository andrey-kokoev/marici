# Correction: the Euler quadratic pole is a continuum Hankel channel, not a rank-one wall

The diagonal residue computed at the Euler boundary does not determine the
rank of the singular sector. The two-parameter asymptotic does.

Write

\[
\sigma=\frac12+a,
\qquad
\tau=\frac12+b,
\qquad
a,b>0.
\]

The singular part of the normalized Cauchy Gram is

\[
G_{\mathrm{sing}}(a,b)
\sim
\frac{4}{\zeta(3/2)^2}\frac1{a+b}.
\]

The kernel

\[
\frac1{a+b}
=
\int_0^\infty e^{-au}e^{-bu}\,du
\]

is positive, but it has infinite rank as \(a,b\) vary. Its minimal
Kolmogorov carrier is the continuum Laplace channel

\[
a\longmapsto \left(u\mapsto e^{-au}\right)
\in L^2(\mathbb R_+,du).
\]

Therefore the simple pole seen on the diagonal is not a one-dimensional
coefficient-wall residue. A single constant or delta coordinate cannot absorb
the full two-parameter singular Gram.

This corrects the previous matching prescription. The finite external
five-cell may carry endpoint incidence and finite-rank residues, but the
Euler quadratic wall requires an infinite-dimensional continuum channel. The
natural source candidate is the theta heat/tail sector, whose scale variable
already has Laplace geometry.

A valid completion interface must produce an isometric or uniformly
bi-bounded comparison between the Euler singular features

\[
e^{-au}
\]

and a source-derived theta heat family. Only after this continuum channel is
matched may a finite wall coordinate account for any remaining endpoint
residue.

The exact next diagram is

\[
\begin{array}{ccc}
\text{Euler max-kernel singular sector}
&\longrightarrow&
L^2(\mathbb R_+,du)
\\
\downarrow && \downarrow
\\
\text{theta heat history}
&\longrightarrow&
\text{completed relative Green carrier}.
\end{array}
\]

The upper arrow is fixed by the Laplace factorization of \(1/(a+b)\); the
lower comparison must be source-derived from Poisson/Tate sewing.

Three gates are now separate:

1. continuum Hankel-channel identification;
2. finite external-wall incidence;
3. regular relative Green continuation.

The sharp hostile subtracts only the diagonal scalar pole

\[
\frac{4}{\zeta(3/2)^2}\frac1{2a}
\]

from each norm. Diagonal norms become finite, but off-diagonal singularities
\(1/(a+b)\) remain and the polarized form does not descend. Another hostile
uses one fitted rank-one vector, which cannot reproduce three or more distinct
Laplace features.

Thus the Euler boundary has supplied a concrete infinite-dimensional
interface target: theta completion must replace a Cauchy Hankel/Laplace
channel, not merely renormalize one wall coefficient.
