# An elementary farther anchor certifies the complex Pick disk of radius seven

At `t=25`, the squared central coordinate is `s=11/2`. The completed source
formula and elementary inequalities give

\[
 \pi^{-11/4}<\frac1{20},\qquad
 \Gamma(11/4)<\frac{63}{32},\qquad
 \zeta(11/2)<\frac{21}{20}.
\]

For the gamma bound, use log-convexity to obtain
`Gamma(3/4)<=pi^(1/4)<3/2`, followed by
`Gamma(11/4)=(7/4)(3/4)Gamma(3/4)`. For zeta, separate the first term and use
the decreasing-function integral bound. Therefore

\[
 \Xi(11/2)<\frac{99}{8}\frac1{20}\frac{63}{32}\frac{21}{20},
 \qquad C(25)=\frac{\Xi(11/2)}{\Xi(1/2)}<3.             \tag{1}
\]

Positive coefficients now bound the degree-seven tails of `C`, `C'`, and
`C''` by the anchor `3/25^7`. Combining those tails with the directed first
six coefficients and preserving the logarithmic denominator proves

\[
 \boxed{\operatorname{Re}F'(t)>0.017
 \qquad(|t|\le7).}                                    \tag{2}
\]

The earlier `C(9)<1.726299<2` theorem independently guarantees that the
source has no zero throughout `|t|<=9`. Vertical integration of (2) therefore
gives

\[
 \boxed{|t|\le7,\quad\operatorname{Im}t>0
 \Longrightarrow\operatorname{Im}F(t)>0.}              \tag{3}
\]

No zero locations are used. This is bounded Pick positivity, not RH.

## Durable verification

- Checker: `checkers/central_complex_pick_radius_seven_certificate.py`
- Result: `results/central-complex-pick-radius-seven-certificate.json`
