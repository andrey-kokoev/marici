# Vanishing Exchange-Center Errors Can Still Accumulate into Unbounded Gain Drift

Exact agreement of all exchanging-loop centers gives a bounded twisted safety
frame. Finite approximants may only satisfy approximate agreement. The
completion criterion is not pointwise decay of the errors but control of their
partial sums.

Let the \(k\)-th consecutive pair of exchanging constructors be

\[
r_{2k-1}(x)=-x+\ell_{2k-1},
\]

\[
r_{2k}(x)=-x+\ell_{2k}.
\]

Their composite is the even translation

\[
r_{2k}r_{2k-1}(x)=x+\delta_k,
\qquad
\delta_k=\ell_{2k}-\ell_{2k-1}.
\]

After \(N\) pairs,

\[
x_N=x_0+\sum_{k=1}^N\delta_k.
\]

## Sharp completion conditions

The affine orbit is bounded if and only if

\[
\sup_N
\left|
\sum_{k=1}^N\delta_k
\right|<\infty.
\]

It converges to a limiting frame if and only if the series

\[
\sum_{k=1}^\infty\delta_k
\]

converges.

Absolute summability,

\[
\sum_{k=1}^\infty|\delta_k|<\infty,
\]

is a robust sufficient condition. It is stable under reordering and gives the
explicit modulus

\[
|x_N-x_0|
\le
\sum_{k=1}^N|\delta_k|.
\]

In multiplicative safety coordinates, a total error budget \(E\) gives

\[
e^{-E}M_0
\le M_N\le
e^E M_0.
\]

## Vanishing-error hostile family

Take

\[
\delta_k=\frac1k.
\]

Then \(\delta_k\to0\), so every successive exchange pair becomes more nearly
centered. Nevertheless,

\[
\sum_{k=1}^N\delta_k=H_N\sim\log N
\longrightarrow\infty.
\]

The gain frame drifts without bound. Pointwise improvement of every local
fixture does not imply completion stability.

## Conditional cancellation

For

\[
\delta_k=\frac{(-1)^{k+1}}{k},
\]

the partial sums converge to \(\log2\). This yields a bounded limiting frame,
but the convergence is conditional. If the source permits reordering the
constructors, the same unsigned errors can be rearranged to alter or destroy
the limit.

Therefore:

- bounded partial sums are the exact ordered-path criterion;
- convergence is the exact limiting-frame criterion;
- absolute summability is the natural order-robust compiler certificate.

## Uniform local bounds are insufficient

A bound

\[
|\delta_k|\le\varepsilon
\]

gives only

\[
|x_N-x_0|\le N\varepsilon.
\]

Even arbitrarily small fixed leakage accumulates linearly. A useful completion
bound must be summable, telescoping, or protected by a source cancellation
law.

## Source-authority boundary

The compiler does not determine the ordering of Fourier--Tate constructors or
their center errors. The source must specify whether the tail is ordered,
whether reorderings are equivalent, and whether cancellations are structural
or accidental.

## Falsifiers

- Center mismatches tending to zero but having unbounded partial sums.
- A fixed per-stage error bound reported as a completion bound.
- Conditional cancellation under a source that permits reordering.
- Cutoffwise centered frames with normalization drift growing like \(\log N\)
  or faster.
- Ignoring the distinction between a bounded orbit and a convergent frame.
- Claiming absolute summability without a source-derived estimate.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to replace exact center matching by the sharp approximate
completion theorem.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Bounded partial sums are necessary and sufficient; harmonic center
errors give the minimal vanishing-but-divergent hostile family.
