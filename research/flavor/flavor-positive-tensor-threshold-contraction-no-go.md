# Positive Tensor Restriction Cannot Supply the Required Threshold Screening

## Question

Can one source-derived positive scalar/Yukawa tensor realize WP842's full
screening (Y_{\rm full}=70) and its active-threshold screening
(Y_{\rm act}=84) by ordinary decoupling restriction?

## Positive tensor grammar

Let (T) be a real finite interaction tensor represented as a matrix after
grouping its source and target indices. Type its screening contribution by the
positive Frobenius pairing

\[
Y(T)=\lVert T\rVert_F^2=\operatorname{Tr}(T^TT).
\]

Deleting a heavy flavor sector acts by an orthogonal projection (P). The
ordinary active tensor is either (PT), (TP), or (PTP). Every such map is
contractive in Frobenius norm. In particular,

\[
\lVert PTP\rVert_F^2\leq\lVert T\rVert_F^2.
\]

For deletion of the first state, the difference is exactly the sum of squares
of every entry removed by the compression and is therefore nonnegative.

## Exact conflict with WP842

WP842 requires

\[
Y_{\rm full}=70,
\qquad
Y_{\rm act}=84.
\]

Since (84>70), no tensor in the positive restriction grammar can satisfy
both conditions. This is independent of tensor dimension, rank, mixing
orientation, or the detailed distribution of its entries.

The explicit full tensor

\[
T_0=
\begin{pmatrix}
1&2&0\\
0&4&7\\
0&0&0
\end{pmatrix}
\]

has norm squared 70. No orthogonal compression can have norm squared above
70, so 84 is unreachable even though the full target itself is realizable.

## Smallest repairs and their authority

Two algebraic repairs exist:

1. a noncontractive matched rescaling (T_{\rm act}=zPTP), requiring at
   least (z^2=84/70=6/5) when the compression loses no norm;
2. a new threshold-induced positive contribution
   (Y_{\rm new}=84-70=14).

Neither repair follows from decoupling. The factor (6/5) must be derived
from finite wavefunction, mixing, and matching calculations. The increment
14 equals the primitive Ward index, which is suggestive, but numerical
equality is not source authority. A source action must generate the new term
and its sign through a named threshold operation.

## Consequence for the candidate principle

The WP841 diameter flow cannot survive an extremal threshold through a fixed
positive tensor plus ordinary restriction. The source constructor must be
dynamical across the threshold: it must regenerate or amplify the interaction
contraction while preserving the portal's oriented labelled channel.

This refines the missing arrow to

\[
(T_Y,\text{heavy sector})
\longrightarrow
\mathcal M_{\rm finite}
\longrightarrow
T_{Y,\rm act},
\]

where (mathcal M_{\rm finite}) is not an orthogonal projection and must be
computed in one common source normalization.

## Disposition

Exact negative theorem for positive conditional-expectation or orthogonal-
restriction matching. The smallest falsifier is the required increase
(70\to84). A noncontractive finite matching factor or a generated positive
increment is necessary; physical derivation and instrument realization remain
open.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp843_positive_tensor_threshold_contraction_no_go.py
```
