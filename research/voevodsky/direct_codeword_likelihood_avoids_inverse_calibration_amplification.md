# Direct codeword likelihood avoids inverse-calibration amplification

## Question

Can the four known conductor codewords be classified without reconstructing an arbitrary 27-component source distribution?

## Claim boundary

This treats repeated preparations of one fixed unknown codeword under the exact independent detector model. It does not apply to arbitrary mixtures, drifting preparations, or unvalidated response parameters.

## Single-bit distributions

The encoder places each logical bit directly in occupation zero or one of its labelled optical mode. For one measured mode, the calibrated count distributions are

\[
p_0=(9/10,1/10,0,0),
\]

\[
p_1=(72/125,97/250,9/250,0).
\]

The likelihood ratios for measured counts zero, one, and two are

\[
\frac{p_1(0)}{p_0(0)}=\frac{16}{25},
\qquad
\frac{p_1(1)}{p_0(1)}=\frac{97}{25},
\qquad
\frac{p_1(2)}{p_0(2)}=\infty.
\]

Thus each logical bit can be classified by its mode's accumulated likelihood ratio. A count of two is conclusive for occupation one within the declared model.

## Finite-trial bound

The Bhattacharyya coefficient is

\[
B_{01}
=\sum_m\sqrt{p_0(m)p_1(m)}
=\frac{18}{25}+\frac{\sqrt{97}}{50}
\approx0.9169771560.
\]

For equal priors, the binary Bayes error after \(N\) independent repetitions obeys

\[
P_{e,i}\le\frac12 B_{01}^N.
\]

The two logical bits occupy separate labelled modes. A union bound gives total codeword-classification error

\[
P_{e,\mathrm{pair}}\le B_{01}^N.
\]

Therefore total error at most \(0.05\) is guaranteed by

\[
N\ge
\left\lceil\frac{\log(0.05)}{\log B_{01}}\right\rceil
=35.
\]

## Comparison with full inversion

The generic unbiased inverse-calibration estimator required a conservative 5,416,154-trial bound because it reconstructs every distribution on the 27-dimensional finite source space. Direct likelihood uses the stronger hypothesis that one of four fixed codewords is repeatedly prepared and reduces the sufficient bound to 35.

This is a change of statistical model, not a superior inversion theorem. If the source is a mixture or leaves the code space, the four-codeword classifier can return a misleading label. Held-out goodness-of-fit against the complete measured count distribution is therefore required.

## Disposition

Under fixed-codeword preparation and the calibrated independent response, direct maximum-likelihood classification makes the proposed null-channel test statistically executable with a 35-trial sufficient bound. Physical preparation, response validation, and raw acquisition remain external gates.
