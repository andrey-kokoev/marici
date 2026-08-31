# Tail splitting preserves the atomic Gram form

## Question

May the quadrature comparison begin at a later label without discarding the original atomic carrier?

## Exact split

For an integer \(q\geq3\), write

\[
Q_{\rm at}(p)
=
Q_{<q}(p)+Q_{\geq q}(p),
\]

where

\[
Q_{<q}(p)=
\sum_{3\leq n<q}
\frac{|p(\log n)|^2}{n e^{2a(\log n)^\beta}}
\]

and

\[
Q_{\geq q}(p)=
\sum_{n\geq q}
\frac{|p(\log n)|^2}{n e^{2a(\log n)^\beta}}.
\]

Each finite-prefix summand is a positive rank-one evaluation form. Hence

\[
Q_{<q}(p)\geq0
\]

and every lower bound for \(Q_{\geq q}\) is also a lower bound for the full atomic form:

\[
Q_{\rm at}(p)
\geq Q_{\geq q}(p).
\]

No label is removed from the carrier; the prefix is retained as additional positive mass.

## Shifted quadrature comparison

Let

\[
Q_{{\rm cont},q}(p)
=
\int_{\log q}^{\infty}|p(x)|^2e^{-2ax^\beta}dx.
\]

Repeating the positive error-form construction at \(x_q=\log q\) gives a value component bounded by

\[
R_{{\rm val},q}(p)
\leq
\frac{2+2a\beta}{q}Q_{{\rm cont},q}(p).
\]

For \(a=1\), \(\beta=1/4\), the analytic constants are

\[
q=3:\frac56,
\qquad
q=4:\frac58,
\qquad
q=6:\frac5{12},
\qquad
q=12:\frac5{24}.
\]

The corresponding remaining budgets are \(1/6,3/8,7/12,19/24\).

## Compatibility boundary

The continuous comparator changes with \(q\). Endpoint and derivative constants must be recomputed against \(Q_{{\rm cont},q}\); the label-three Christoffel values cannot be reused. A tail lower bound also does not by itself compare anchored correction norms for different \(q\), because omitting positive prefix atoms weakens the lower Gram form.

## Disposition

Tail movement is Loewner-safe: finite omitted labels remain positive and need not be discarded from the physical carrier. It creates a larger analytic coercivity budget for the tail comparison. Whether that budget dominates the shifted endpoint and derivative forms is the next test.
