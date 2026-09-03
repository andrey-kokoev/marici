# Minus alpha squared is the centered image of a hard-edge log free energy

## Question

Which relative determinant term produces the observed \(-\alpha^2/n^2\) recurrence remainder?

The centered determinant identity sends

\[
\log D_n^{(\alpha)}-\log D_n^{(0)}
\longmapsto
\log\frac{(a_n^{(\alpha)})^2}{(a_n^{(0)})^2}.
\]

Since

\[
\Delta^2\log n=-\frac1{n^2}+O(n^{-4}),
\]

the finite diagnostic is exactly consistent with the relative free-energy target

\[
\log\frac{D_n^{(\alpha)}}{D_n^{(0)}}
=rac{\alpha}{\beta}n\log n
+c_\alpha n
+\alpha^2\log n
+C_\alpha
+E_n^{(\alpha)},
\]

provided

\[
\Delta^2 E_n^{(\alpha)}=o(n^{-2}).
\]

Centered differencing then gives

\[
\log\frac{(a_n^{(\alpha)})^2}{(a_n^{(0)})^2}
=rac{\alpha}{\beta n}
-rac{\alpha^2}{n^2}
+o(n^{-2}),
\]

up to the \(O(n^{-3})\) correction in \(\Delta^2(n\log n)\).

## Disposition

Resolve the coefficient reduction: \(-\alpha^2\) is the centered image of a \(+\alpha^2\log n\) hard-edge term in relative Hankel free energy.

The next leaf is `hard-edge-log-free-energy`: prove the \(+\alpha^2\log n\) coefficient and centered remainder for the quarter-Weibull moment ensemble.

## Claim boundary

This identifies the necessary free-energy term; it does not derive that term. Calling it a hard-edge self-energy is only an interpretation until a determinant asymptotic supplies the coefficient and remainder.
