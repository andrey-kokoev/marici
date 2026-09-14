# Inverse calibration makes naive parity sampling expensive

## Question

How many measured count trials suffice for robust sign classification of both reconstructed source parities under the exact finite detector model?

## Claim boundary

This gives a conservative independent-trial Hoeffding bound for the specified inverse-calibration estimator. It is not an optimal estimator, a measured noise model, or an acquisition result.

## Linear estimator

Let \(L^{\otimes3}\) be the exact left inverse of the calibrated three-mode response. For source parity row vectors \(f_1,f_2\), define measured-record weights

\[
g_i=f_iL^{\otimes3}.
\]

If measured record \(M\) is sampled from distribution \(q\), then

\[
\widehat O_i=\frac1N\sum_{r=1}^N g_i(M_r)
\]

is unbiased for the source parity expectation.

For both parities, exact enumeration of the 64 measured records gives

\[
\min g_i=-\frac{8408362000}{43046721},
\qquad
\max g_i=\frac{2825761000}{4782969}.
\]

The common range is

\[
B=\frac{33840211000}{43046721}
\approx786.1275.
\]

## Sign-classification bound

For an encoded basis class, the true parity is \(+1\) or \(-1\). Error below \(1/2\) therefore preserves its sign with margin. Hoeffding's inequality and a union bound over both observables give

\[
\Pr\left[
\max_i|\widehat O_i-O_i|\ge\frac12
\right]
\le
4\exp\left(-\frac{N}{2B^2}\right).
\]

To make this probability at most \(0.05\), it suffices that

\[
N\ge
\left\lceil2B^2\log80\right\rceil
=5{,}416{,}154.
\]

## Interpretation

The channel is algebraically invertible but poorly conditioned for this direct unbiased estimator. Invertibility alone does not imply practical acquisition efficiency.

The bound is intentionally conservative. Better performance may come from maximum-likelihood reconstruction constrained to the four codewords, direct calibration of the four syndrome classes, optimized efficiency, or a different left inverse. Those alternatives require separate preregistration and testing.

## Deliberate comparison

With perfect efficiency and no dark counts, direct measured pair parity has range two. The same two-observable, half-margin Hoeffding bound at total error \(0.05\) is

\[
\left\lceil8\log80\right\rceil=36.
\]

Thus the large bound is caused by inverse-response amplification, not by the two-bit syndrome itself.

## Disposition

The naive inverse-calibration acquisition plan is executable but statistically costly: 5,416,154 trials are sufficient under its assumptions. Physical work should not claim feasibility from rank alone; it must select and validate an estimator and trial budget.
