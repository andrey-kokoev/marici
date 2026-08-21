# One bivariate source function contains every linear RH inequality

Let `m_k=4^(-k)A_k` and `M(z)=sum m_k z^k`. The Taylor definition gives

\[
 \boxed{M(z)=S\!\left(\frac{1-z}{4}\right)}.
\]

For `C_(k,j)=sum_r(-1)^r binom(j,r)m_(k+r)`, define
`G(z,w)=sum C_(k,j)z^kw^j`. Partial fractions give

\[
 \boxed{G(z,w)=
 \frac{zM(z)+\frac{w}{1-w}M(-\frac{w}{1-w})}
 {z(1-w)+w}.}
\]

Thus complete monotonicity asks for coefficientwise positivity of one
two-variable function built from two completed-source resolvent evaluations.

Conditionally in squared-zero coordinate `lambda`, with
`u=4/(1+4lambda)`,

\[
 C_{k,j}=4^{j+1}\sum_\lambda
 \frac{m_\lambda\lambda^j}{(1+4\lambda)^{k+j+1}}.
\]

Nonnegative `lambda` makes every coefficient manifestly positive. The source
attack is to decompose `G` into a positive kernel or Gram object before using
zeros, preserving pole cancellation and gamma--prime coupling across both
fractional branches.

## Scope

The identity is algebraic. Infinite coefficient positivity and RH are not
proved.

## Durable verification

- Checker: `checkers/hausdorff_bivariate_source_generator.py`
- Result: `results/hausdorff-bivariate-source-generator.json`

After a fractional coordinate change, this generator is `y` times the Loewner
kernel of `F(t)=(4t-1)S(t)`. See
`loewner-kernel-universal-coupled-positivity-theorem.md`.
