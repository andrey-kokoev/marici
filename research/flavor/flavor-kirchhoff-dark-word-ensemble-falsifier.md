# Kirchhoff Dark-Word Ensemble Falsifier

## Question

Does WP861's proper rank-three `physical16` family reproduce the measured mass
hierarchies anywhere inside the complete stored viability envelope?

## Exact single-sector shape law

Up to an arbitrary overall sector scale, the WP861 matrix is

\[
Y=aI+F_-,
\qquad
F_-=
\begin{pmatrix}
0&-i&0\\
0&0&-i\\
0&0&0
\end{pmatrix}.
\]

Let (t=|a|^2\geq0), and let 
(\lambda_1,\lambda_2,\lambda_3) be the squared singular values before the
irrelevant common scale. Their elementary symmetric polynomials are

\[
e_1=3t+2,
\qquad
e_2=3t^2+2t+1,
\qquad
e_3=t^3.
\]

Consequently the scale-free mass-shape invariant is

\[
R_2(t)=\frac{e_2}{e_1^2}
=\frac{3t^2+2t+1}{(3t+2)^2}.
\]

Its derivative is

\[
R_2'(t)=\frac{2(3t-1)}{(3t+2)^3},
\]

so the exact global bound is

\[
R_2\geq R_2(1/3)=\frac29.
\]

This bound is independent of (a), its phase, and the overall sector scale.

## Measured and complete-ensemble hostile

Using the frozen WP7 central Yukawas gives

\[
R_{2,u}=1.3553\times10^{-5},
\qquad
R_{2,d}=3.5307\times10^{-4}.
\]

Both are far below (2/9).

The result is stronger than a central-value mismatch. Every stored viable fit
has total 
(\chi^2\leq20.28), so each individual Yukawa residual is bounded by
(\sqrt{20.28}\) standard deviations. Maximizing the two smaller masses and
the numerator while minimizing the largest-mass contribution to the
denominator gives the conservative envelope bounds

\[
R_{2,u}<1.76\times10^{-5},
\qquad
R_{2,d}<4.61\times10^{-4}.
\]

These remain separated from (2/9) by more than three orders of magnitude.
Hence none of the complete 1,210 stored viable sheets can lie in the WP861
family.

## Disposition

WP861 is a mathematically proper, CP-violating `physical16` image, but its
numerical prediction fails the complete fitted ensemble. The complete-grammar
interpretation therefore closes negative. The additive interpretation remains
surjective and is not a selector.

This falsifier does not invalidate WP859's boundary selector. It rejects the
minimal interface that maps its single dark word identically into each entire
Yukawa sector. A successor needs additional source-derived flavor words or a
different physical operator while retaining the fixed portal coefficients.
Adding arbitrary word coefficients would restore fitting capacity and forfeit
selection authority.

## Smallest exact falsifier

One sector suffices: every WP861 mass triple obeys (R_2\ge2/9), while the
entire viable up-sector envelope obeys (R_{2,u}<1.76\times10^{-5}).

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp862_kirchhoff_dark_word_ensemble_falsifier.py
```
