# Theta positivity certifies the complex Pick disk of radius three

The normalized theta series extends the complex Pick theorem to

\[
 \boxed{|t|\le3,\quad\operatorname{Im}t>0
 \Longrightarrow \operatorname{Im}F(t)>0.}             \tag{1}
\]

The proof uses no zero locations.

Let `C(t)=Y(t)/Y(0)`. Its coefficients are positive, the first six are
directed, and the source bound gives `C(9)<1.726299`. For `r<=9`, positivity
therefore controls every omitted coefficient through

\[
 \sum_{n\ge7}n^{\underline j}c_nr^{n-j}
 \le 7^{\underline j}C(9)\frac{r^{7-j}}{9^7},
 \qquad j=0,1,2.                                      \tag{2}
\]

At `r=3`, combining (2) with the first six coefficients gives a strict lower
bound for `|C|`. Applying the denominator-aware identities

\[
 p=C'/C,\qquad q=C''/C-p^2,qquad F'=4p+(4t-1)q
\]

then proves, with directed rounding,

\[
 \operatorname{Re}F'(t)>0.014\qquad(|t|\le3).          \tag{3}
\]

Vertical integration from the real axis gives (1) with the same margin per
unit imaginary height.

The same coefficient positivity proves `|C(t)|>=2-C(9)>0.2737` throughout
`|t|<=9`. Thus analyticity is protected well beyond the radius-three Pick
disk. The present perturbation inequality remains positive until approximately
radius `3.09895`; radius three is retained as a clean directed theorem.

This is still bounded source positivity, not global Pick positivity or RH.

## Durable verification

- Checker: `checkers/central_complex_pick_radius_three_certificate.py`
- Result: `results/central-complex-pick-radius-three-certificate.json`
