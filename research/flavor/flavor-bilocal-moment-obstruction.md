# Bilocal neutral-B moment obstruction

## Question

WP520 supplies the exact source form factor \(F(q^2)\). A neutral-\(B\)
prediction requires a hadronic linear functional. After factoring the contact
matrix element, write its schematic action as

\[
\mathcal B[\mu]=\int F(q^2)\,d\mu(q^2).
\]

WP511 supplies only the local contact normalization, corresponding to
\(\int d\mu=1\). WP521 asks whether adding finitely many ordinary
\(q^2\)-moments could determine the exact convolution.

## Hostile positive subclass

The checker restricts to positive normalized measures supported on
\(0\le q^2\le1\ {\rm GeV}^2\). This positivity assumption is used only to make
the counterexample stronger; it is not asserted as the complete physical
neutral-\(B\) bilocal domain.

For each \(N\), choose \(N+2\) equally spaced rational nodes. The alternating
binomial vector

\[
w_j=(-1)^j {N+1\choose j}
\]

annihilates every polynomial of degree at most \(N\). Small symmetric
perturbations of the uniform measure by this vector therefore produce two
strictly positive normalized measures with identical moments through \(N\).

The checker constructs exact hostile pairs for \(N=0,\ldots,6\). Every pair
has a different WP520 convolution. The response differences begin with:

| Highest matched moment | Response difference |
|---:|---:|
| 0 | 0.3575679481 |
| 1 | 0.0449121186 |
| 2 | 0.0062581750 |
| 6 | \(5.23430\mathbin{\cdot}10^{-7}\) |

Thus contact normalization is nonfaithful, and adding a first momentum moment
does not repair it.

## General theorem

After exact cancellation, the WP520 form factor is rational with denominator
degree six. If integration against \(F\) were determined by moments
\(0,\ldots,N\) for every positive measure on an interval, then \(F\) would
belong to the polynomial span of those moment functions. A reduced rational
function with nonconstant denominator belongs to no finite polynomial span.

Consequently no finite ordinary-moment tower determines the exact bilocal
response on the declared measure class.

## Typing and gate

- Source domain: the exact WP520 finite-propagator kernel.
- Hostile hadronic domain: positive normalized measures on the declared
  diagnostic interval.
- Classification: exact nonfaithfulness theorem for local and finite-moment
  summaries; neither selector nor physical instrument.
- Smallest falsifier: two positive normalized measures with the same contact
  normalization give unequal responses. The next pair also shares the first
  \(q^2\) moment.

Faithfulness requires either the calibrated bilocal matrix-element functional
itself or an independently justified complete representation with a controlled
truncation error. A finite fitted moment list without that error contract has
no identification authority.
