# Multi-domain majority amplification (WP283)

## Formal probability amplifier

Take independent CP domains with favored-branch probability \(p=3/4\). For an
odd number \(N\), a formal majority aggregator has wrong-sign probability

\[
P_{\mathrm{err}}(N)
=\sum_{k=0}^{(N-1)/2}
\binom Nk p^k(1-p)^{N-k}.
\]

The exact errors decrease across the tested odd counts. Seventeen domains give

\[
\frac{106384445}{8589934592}>\frac1{100},
\]

while nineteen are the first to pass, with error

\[
\frac{611828695}{68719476736}<\frac1{100}.
\]

Thus independent repetition can amplify WP282's probabilistic readout.

## Majority is not coarsening

A physical flavor vacuum is spatial, not a list sent to an external voter. On
a five-site ring, the configurations `+++--` and `+-+-+` have the same three-to-
two majority and the same mean orientation \(1/5\). They have respectively two
and four domain walls. Their energies and subsequent evolution therefore need
not agree.

The majority statistic forgets source geometry at the arrow from local branch
ensemble to globally homogenized vacuum. It cannot substitute for domain-wall
dynamics.

## Classification

Independent-domain majority is a formal probabilistic amplifier, not yet a
physical global flavor selector. A source-derived coarsening operation must
supply spatial coupling, wall tension and mobility, expansion and quench
history, boundary conditions, homogenization time, and stabilization.

Run `uv run --with sympy python
research/flavor/checkers/wp283_multidomain_majority_amplification.py` for the
exact binomial threshold and hostile equal-majority spatial pair.
