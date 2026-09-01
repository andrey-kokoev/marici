# Bifundamental-pairing production-kernel no-go: WP1102

## Question

Can the nondegenerate \((3,3)\) \(A\)-\(B\) pairing serve as the missing
production/decay kernel?

## Alignment gate

In WP1080's aligned frame the coefficient matrix is \(I_3\), with rank \(3\)
and trace \(3\). It pairs the internal \(A\) and \(B\) three-state factors.

It supplies zero rows from the six localized soft branches and zero rows to
physical16:

\[
\operatorname{rows}(I_3\to{\rm soft})=0,
\qquad
\operatorname{rows}(I_3\to{\rm physical16})=0.
\]

## Gain gate

The trace is \(3\), not the required gain \(3/2\). Dividing by two would be an
additional un sourced normalization. The soft distribution remains

\[
q=\frac1{23}(6,8,1,4,2,2),
\]

not \((1/4)^6\).

## Classification

Negative gate. Rank, trace, or \(A\)-\(B\) alignment cannot be promoted to six
event weights, production couplings, channel selection, or gain.

Checker: `research/flavor/checkers/wp1102_bifundamental_pairing_production_kernel_no_go.py`

Result: `results/wp1102_bifundamental_pairing_production_kernel_no_go.json`
