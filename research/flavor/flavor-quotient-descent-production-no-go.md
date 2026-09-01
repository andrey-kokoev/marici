# Quotient descent is not the production kernel: WP1115

## Question

Can physical16 quotient descent supply the six-row production kernel directly?

## Exact gate

An invertible descent on the six soft branches is a permutation. It preserves
the weight multiset

\[
\frac1{23}(6,8,1,4,2,2),
\]

so it cannot produce \((1/4)^6\). A non-invertible descent is a projection of
rank at most \(5\), so it cannot be the required \(6\times6\) kernel. In
either case the gain is not \(3/2\): a permutation has gain \(1\).

## Classification

Negative gate. Physical16 descent maps labels and states; it is not a source
interaction kernel, event reweighting law, or gain law.

Checker: `research/flavor/checkers/wp1115_quotient_descent_production_no_go.py`

Result: `results/wp1115_quotient_descent_production_no_go.json`
