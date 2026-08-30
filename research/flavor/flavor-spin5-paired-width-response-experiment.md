# Spin(5) paired-width response experiment (WP900)

## Question

What finite, distribution-free experiment can replace WP898's Gaussian
assumption and directly test whether the tau response is stable over WP897's
mixing-width interval?

## Frozen experiment

At each of the two preregistered pole masses, generate and reconstruct two
independent CP-even source cells through the identical WP895 detector chain:

- a zero-width/narrow-width reference cell;
- the maximal admitted width cell \(q_i=1\), with
  \(\Gamma_i=\Gamma_i^{\rm SM}\).

Use forced tau decays for response statistics, but normalize physical yields
separately through WP897. Freeze random seeds, event budgets, WP251 selection,
WP253's six bins, source-card hashes, and nuisance variations before opening
the histograms. Stop each cell only after a preregistered number of selected
events, recording generated and rejected counts as part of the efficiency
instrument.

## Distribution-free certificate

For a \(k\)-bin multinomial distribution and \(n\) selected events, the
Bretagnolle--Huber--Carol bound implies

\[
\Pr\!\left[d_{\rm TV}(\widehat p,p)>r(n,\alpha)\right]
\leq 2^k e^{-2nr^2}.
\]

Allocating failure probability \(\alpha\) jointly across all four width cells
at both poles gives

\[
r(n,\alpha)=
\sqrt{\frac{\log(2^{k+2}/\alpha)}{2n}}.
\]

Hence, with observed empirical drift \(\widehat d_i\), the source-width drift
is certified by

\[
d_{{\rm TV},i}
\leq
\widehat d_i+r(n_{i,0},\alpha)+r(n_{i,1},\alpha).
\]

Admission at tolerance \(\varepsilon\) requires the right-hand side not to
exceed \(\varepsilon\) at both poles. This includes arbitrary non-Gaussian
tails because it acts directly on the frozen six-bin probabilities.

For \(k=6\), \(\alpha=0.05\), equal cell sizes, and the diagnostic choice
\(\varepsilon=0.01\), even \(\widehat d_i=0\) requires

\[
n\geq
\left\lceil
\frac{2\log(2^8/0.05)}{0.01^2}
\right\rceil
=170819
\]

selected events per width cell. This is four cells total. The number is a
design diagnostic, not a claim that such samples currently exist.

## Falsifiers and boundary

The smallest direct falsifier is one pole for which the upper confidence bound
exceeds the frozen tolerance. A zero selected cell, source-card mismatch,
post-unblinding bin change, or nuisance completion that violates the bound also
fails the experiment.

WP900 closes the statistical grammar for the width-response test. It does not
execute CMS simulation, choose \(q_u,q_v\), establish finite collision-data
power, or select a flavor point.

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp900_spin5_paired_width_response_experiment.py
~~~
