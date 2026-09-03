# Diagonal truncation data favor an inverse-degree correction

## Question

What correction to a leading \(n^{-3}\) diagonal relative perturbation is compatible with the degree-twelve grid?

Fit

\[
n^3\left(\frac{b_n^{(X)}}{b_n}-1\right)
=C+d n^{-\delta}.
\]

Across windows \(4\!:\!12\) through \(8\!:\!12\), fitted \(\delta\) increases monotonically from \(0.73\) to \(0.82\), fitted \(C\) remains positive near \(0.09\), and \(d<0\). Relative fit errors fall below \(2.5\times10^{-4}\).

## Disposition

The data favor a leading \(n^{-3}\) perturbation approached from below, with a correction compatible with \(n^{-1}\). The drift does not select \(\delta=1\); it excludes treating the short-window value as settled.

The next leaf is `inverse-degree-correction-test`: compare the fixed model \(C+d/n\) against free-exponent and two-correction alternatives on a longer grid.

## Claim boundary

This is finite regression, not a recurrence asymptotic. Fit quality does not supply a uniform remainder bound or establish cocycle summability.
