# The primitive Mertens current is invisible to ordinary Dixmier trace

## Primitive observed carrier

After finite Cauchy observation, the primitive diagonal is

\[
D e_p=p^{-1}e_p.
\]

Ordering primes as \(p_1<p_2<\cdots\), its singular values are

\[
\mu_n(D)=p_n^{-1}.
\]

Mertens' theorem gives

\[
\sum_{n\leq N}\mu_n(D)
=\sum_{p\leq p_N}\frac1p
=\log\log p_N+B_1+o(1).
\]

Using \(p_N\sim N\log N\), this grows like \(\log\log N\).

## Ordinary weak trace sees zero

The standard weak trace ideal \(\mathcal L^{1,\infty}\) uses the scale
\(\log(1+N)\). Here

\[
\frac1{\log(1+N)}
\sum_{n\leq N}\mu_n(D)
\longrightarrow0.
\]

Therefore \(D\) belongs to \(\mathcal L^{1,\infty}\), but every ordinary
Dixmier trace obtained from that normalized partial-sum sequence vanishes on
\(D\).

This is not the Mertens current. The primitive divergence survives on the
finer scale \(\log\log p_N\), and its finite part is the Meissel--Mertens
constant \(B_1\).

## Required source trace

The appropriate primitive functional is not a standard logarithmic singular
trace. It is a prime-labelled finite-part operation of the form

\[
\operatorname{FP}_{\mathrm{prime}}(D)
=\lim_{N\to\infty}
\left(
\sum_{n\leq N}\mu_n(D)-\log\log p_N
\right).
\]

This formula states the scalar target only. To become a lawful operation on the
filtered boundary carrier it still needs:

- a declared domain containing the primitive observed density;
- compatibility with prime-cutoff refinement;
- covariance under the admitted labelled source maps;
- coupling to endpoint and gamma normalization;
- continuity relative to the boundary-corona topology;
- a relative version on mixed prime words and Green kernels.

Arbitrary unitary or basis transport cannot be assumed to preserve the
prime-labelled subtraction. The labels and cutoff authority are part of the
functional's type.

## Consequence

Standard noncommutative integration does not supply the missing orientation
for free. An ordinary Dixmier trace reports zero on the primitive carrier even
though the Mertens finite part is nontrivial. Replacing the source-labelled
finite part by that zero would erase the primitive current before the
completion comparison.

The state-valued comparison must therefore use a finer Marcinkiewicz-type
prime scale, or an equivalent labelled relative-trace construction, rather
than only the usual Schatten and weak-trace ideals.

## Finite audit

For the first 100, 1000, 5000, and 10000 primes, the normalized sums

\[
\frac{\sum_{n\leq N}1/p_n}{\log(N+1)}
\]

decrease from approximately \(0.456\) to \(0.294\), while normalization by
\(\log\log p_N\) remains near one. The finite calculation is not an asymptotic
proof; it is a hostile check that distinguishes the two scales.

## Verdict

The primitive Mertens current lives below the resolution of ordinary Dixmier
trace. Its completion law must retain the prime-labelled double-logarithmic
finite part. The next gate is to construct this functional on the full
filtered boundary carrier and test its relative Green-boundary correction.

