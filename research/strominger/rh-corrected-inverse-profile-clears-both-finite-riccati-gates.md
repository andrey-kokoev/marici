# A corrected inverse profile clears both finite Riccati gates

## Question

Can one profile simultaneously lie below the observed polynomial ratio and have positive defect slack?

For

\[
v_n^{(\kappa,c)}
=\frac1{n+\kappa}
\left(1+\frac{c}{n^2}
ight),
\]

a grid over \(0.31\le\kappa\le0.71\) and \(-5\le c\le5\) finds 71 profiles satisfying both finite gates. The maximin admitted profile is

\[
\kappa=0.31,
\qquad c=-1.
\]

At the initialization index \(n=9\), the actual Riccati ratio exceeds the profile ratio by \(1.66\times10^{-4}\). Its induced critical defect exceeds the Weibull defect through degree sixteen; the minimum slack is \(2.83\times10^{-5}\), and

\[
n^4(\varepsilon_n^{*,v}-\varepsilon_n)
=1.847,\ldots,1.851
\]

on degrees nine through sixteen.

## Disposition

Complete the finite corrected-barrier construction. The next leaf is `weibull-corrected-barrier-asymptotic`: derive \(\kappa\) and \(c\) from the Jacobi coefficient expansion and prove eventual positive slack with a signed remainder, rather than retaining fitted decimal parameters.

## Claim boundary

Finite barrier propagation does not prove an eventual inequality. The parameters are fitted diagnostics and currently have no source-derived exact values.
