# The Pick gate is one denominator-free quadratic theta inequality

Put `z=sqrt(t)=a+ib` on the principal branch of the upper `t` half-plane, so
`a>0` and `b>0`. Write the centered completed source as

\[
 B(z)=\int_0^\infty \Phi(u)\cosh(zu)\,du,
 \qquad
 F(t)=\left(2z-\frac1{2z}\right)\frac{B'(z)}{B(z)}.    \tag{1}
\]

Define four real source transforms

\[
\begin{aligned}
 P&=\int\Phi(u)\cosh(au)\cos(bu)\,du,\\
 Q&=\int\Phi(u)\sinh(au)\sin(bu)\,du,\\
 R&=\int\Phi(u)u\sinh(au)\cos(bu)\,du,\\
 T&=\int\Phi(u)u\cosh(au)\sin(bu)\,du.
\end{aligned}                                           \tag{2}
\]

Then `B=P+iQ` and `B'=R+iT`. If

\[
 \alpha=2a-\frac{a}{2(a^2+b^2)},\qquad
 \beta =2b+\frac{b}{2(a^2+b^2)},                         \tag{3}
\]

direct multiplication gives

\[
 \boxed{|B(z)|^2\operatorname{Im}F(t)
 =\beta(RP+TQ)+\alpha(TP-RQ).}                           \tag{4}
\]

Therefore, away from a zero of `B`, the RH-equivalent Pick target is the
single denominator-free source inequality

\[
 \boxed{\beta(RP+TQ)+\alpha(TP-RQ)\ge0}                  \tag{5}
\]

for every `a,b>0` corresponding to the principal square root.

## Why this is a better attack surface

Equation (5) uses only the positive Riemann theta density and elementary real
oscillatory transforms. It does not mention zeros, meromorphic pole locations,
or a retrospectively constructed operator. Endpoint, gamma, and prime data
have already been coupled inside the completed theta source before the sign is
taken.

It also displays the difficulty honestly. The sine factors make `Q` and `T`
oscillatory, while `alpha` changes sign inside the quarter-circle
`a^2+b^2=1/4`. No termwise positivity proof can work globally. The four-atom
falsifier in `positive-even-measure-loewner-curvature-falsifier.md` further
shows that positivity and evenness of `Phi` alone cannot imply (5).

The next analytic attack is to use the special modular structure and explicit
differential estimates of the Riemann theta density to control the two coupled
combinations `RP+TQ` and `TP-RQ`, rather than bounding the four transforms
separately. No closed local differential equation strong enough to imply that
control has yet been established.

Equation (4) is exact. Inequality (5) for the actual Riemann source remains
open and is equivalent to the global Pick gate; RH is not proved.

## Durable verification

- Checker: `checkers/theta_four_transform_pick_reduction.py`
- Result: `results/theta-four-transform-pick-reduction.json`
