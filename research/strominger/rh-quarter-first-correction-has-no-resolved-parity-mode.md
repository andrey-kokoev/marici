# Quarter first correction has no resolved parity mode

## Question

Does the parity freedom left by the exact two-step Y-system explain failure of the absolute affine intercept on shifts zero through twelve?

## Claim boundary

For each nested window, define the fitted intercept coordinate

\[
c_a=u_a+\frac{19a}{24}.
\]

The preregistered finite no-parity gate requires the difference between even- and odd-shift means to be below \(0.005\) on the latest window and to improve from the early window. This does not prove equality of asymptotic parity sectors.

## Disposition

All six gates pass. The even-minus-odd mean difference decreases from \(0.005519\) to \(-0.000827\), while the latest within-parity spreads remain \(0.02413\) and \(0.02110\). Thus no parity mode is resolved at the declared scale. The failed absolute intercept is instead associated with common cutoff drift and within-parity nonuniformity. The next executable test is `quarter-common-intercept-cutoff-drift`, which must test convergence toward \(29/24\) without changing the parity gate.
