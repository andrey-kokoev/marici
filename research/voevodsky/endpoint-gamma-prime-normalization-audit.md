# Endpoint--gamma--prime normalization audit

## Question

Do the completed Xi logarithmic derivative, its three inverse-Laplace pieces, and the paired-zero resolvent use one consistent sign and multiplicity convention?

## Claim boundary

Yes algebraically. Every coefficient and Gaussian scale agrees. Independent confirmation by the source owner and inspection of authoritative Hadamard theorem text remain pending.

## Completed logarithmic derivative

Use

\[
\xi(s)
=
\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Then

\[
\frac{\xi'(s)}{\xi(s)}
=
\frac1s+rac1{s-1}
+
\frac{\psi(s/2)-\log\pi}{2}
+
\frac{\zeta'(s)}{\zeta(s)}.
\]

Set

\[
s=\frac12+y,
\qquad
x=y^2,
\qquad
B'(x)=\frac{\xi'(s)/\xi(s)}{2y}.
\]

## Endpoint

Direct simplification gives

\[
\frac1{2y}
\left(
\frac1s+rac1{s-1}
\right)
=
\frac1{x-1/4}.
\]

Therefore

\[
K_{\mathrm{endpoint}}(t)=e^{t/4}.
\]

There is no extra factor of two.

## Gamma term

The gamma contribution is

\[
G(x)
=
\frac{\psi(y/2+1/4)-\log\pi}{4y}.
\]

Using

\[
\psi(z)
=
-\gamma_E
+
\int_0^\infty
\frac{e^{-r}-e^{-zr}}{1-e^{-r}}\,dr
\]

and the square-root Laplace identity with \(a=r/2\) gives

\[
K_\Gamma(t)
=
\frac1{4\sqrt{\pi t}}
\left[
-\gamma_E-\log\pi
+
\int_0^\infty
\frac{e^{-r}-e^{-r/4-r^2/(16t)}}{1-e^{-r}}\,dr
\right].
\]

Thus the required constants are:

- outer coefficient \(1/4\);
- Gaussian denominator \(16t\);
- removable integrand limit \(-3/4\) at \(r=0\).

## Prime term

For \(\operatorname{Re}s>1\),

\[
\frac{\zeta'(s)}{\zeta(s)}
=
-
\sum_{n\geq2}
\Lambda(n)n^{-s}.
\]

After division by \(2y\), the inverse kernel is

\[
K_{\mathrm{prime}}(t)
=
-
\frac1{2\sqrt{\pi t}}
\sum_{n\geq2}
\Lambda(n)n^{-1/2}
\exp\left(-\frac{(\log n)^2}{4t}\right).
\]

Thus the sign is negative, the outer coefficient is \(1/2\), and the Gaussian denominator is \(4t\).

## Zero orbits

For one functional-equation orbit \([a]=\{a,-a\}\),

\[
\frac1{2y}
\left(
\frac1{y-a}+rac1{y+a}
\right)
=
\frac1{x-a^2}.
\]

An orbit of holomorphic multiplicity \(m_a\) contributes

\[
\frac{m_a}{x-a^2}
=
\frac{m_a}{x+\lambda_a}.
\]

The multiplicity is not doubled.

## Cross-audit result

The four presentations agree exactly:

\[
K_{\mathrm{completed}}
=
K_{\mathrm{endpoint}}
+
K_\Gamma
+
K_{\mathrm{prime}},
\]

and its Laplace transform equals the one-pole-per-functional-orbit resolvent. No normalization residual remains in this audit.

## Disposition

The factors of two, signs, Gaussian scales, and orbit multiplicities are fixed. Promotion to source-complete status still requires source-owner confirmation and authoritative Hadamard theorem text.

## Verification

- `research/voevodsky/endpoint-gamma-prime-normalization-audit-v1.json`
- `research/voevodsky/checkers/check_endpoint_gamma_prime_normalization.py`
- `research/voevodsky/results/endpoint_gamma_prime_normalization.json`
