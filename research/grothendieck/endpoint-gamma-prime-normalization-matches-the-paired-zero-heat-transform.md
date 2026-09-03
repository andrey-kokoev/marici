# Endpoint–gamma–prime normalization matches the paired-zero heat transform

## Question

Do the endpoint, gamma, and prime kernels have the exact constants and common complex domain needed to equal the paired-zero transform without a factor-of-two or branch ambiguity?

## Claim boundary

Yes. The comparison is an identity of holomorphic functions on `Re x>1/4`, followed by uniqueness of their continuous inverse-Laplace kernels. This closes normalization and analytic interchange. It does not prove positivity of the resulting arithmetic kernel.

## Completed source identity

Use exactly

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad s=\frac12+y,
\qquad x=y^2.
\]

Then

\[
\frac1{2y}\frac{\xi'(s)}{\xi(s)}
=E(x)+G(x)+P(x),
\]

where

\[
E(x)=\frac1{2y}\left(\frac1s+\frac1{s-1}\right)
=\frac1{x-1/4},
\]

\[
G(x)=\frac{\psi(s/2)-\log\pi}{4y}
=\frac{\psi(1/4+y/2)-\log\pi}{4y},
\]

and, initially for `Re s>1`,

\[
P(x)=-\frac1{2y}\sum_{n\ge2}\Lambda(n)n^{-1/2-y}.
\]

Every coefficient follows directly from logarithmically differentiating the declared normalization of `xi`: the gamma derivative contributes `1/2`, division by `2y` contributes another `1/2`, and the Euler product has its standard minus sign.

## Common complex domain

Choose the principal square root. If `Re x>1/4`, then

\[
\operatorname{Re}\sqrt{x}
=\sqrt{\frac{|x|+\operatorname{Re}x}{2}}
\ge \sqrt{\operatorname{Re}x}>rac12.
\]

Hence `Re s>1`, so the von Mangoldt series converges absolutely. This half-plane is also exactly where the endpoint transform of `e^{t/4}` converges.

For `sigma=Re x>1/4`, absolute prime-kernel interchange follows from

\[
\int_0^\infty e^{-\sigma t}
\frac{e^{-(\log n)^2/(4t)}}{\sqrt{\pi t}}\,dt
=\frac{n^{-\sqrt\sigma}}{\sqrt\sigma}.
\]

Thus the absolute majorant is

\[
\frac1{2\sqrt\sigma}
\sum_{n\ge2}\Lambda(n)n^{-1/2-\sqrt\sigma},
\]

which converges because `1/2+sqrt(sigma)>1`. The gamma kernel is locally integrable at zero and of polynomial order at infinity by `research/voevodsky/gamma-kernel-laplace-holomorphy.md`, so its transform is absolutely convergent and holomorphic already on `Re x>0`.

## Exact inverse kernels

The three transforms are

\[
K_E(t)=e^{t/4},
\]

\[
K_P(t)=-\frac1{2\sqrt{\pi t}}
\sum_{n\ge2}\Lambda(n)n^{-1/2}
\exp\!\left(-\frac{(\log n)^2}{4t}\right),
\]

and

\[
K_\Gamma(t)=
\frac1{4\sqrt{\pi t}}
\left[-\gamma_E-\log\pi+
\int_0^\infty
\frac{e^{-r}-e^{-r/4-r^2/(16t)}}{1-e^{-r}}\,dr
\right].
\]

The gamma formula follows from

\[
\psi(z)=-\gamma_E+
\int_0^\infty\frac{e^{-r}-e^{-zr}}{1-e^{-r}}\,dr
\]

with `z=1/4+y/2`, and from the inverse transform of `e^{-a sqrt(x)}/sqrt(x)`. The exponent is `r^2/(16t)` because `a=r/2`.

## Comparison with the paired zeros

The paired-Hadamard theorem gives, with one representative per `a~-a` orbit and original multiplicity,

\[
\frac1{2y}\frac{\Xi'(y)}{\Xi(y)}
=\sum_{[a]}\frac{m_a}{x+\lambda_a}
=\int_0^\infty e^{-xt}H(t)\,dt,
\]

where

\[
H(t)=\sum_{[a]}m_a e^{-\lambda_a t}.
\]

Since `Xi(y)=xi(1/2+y)`, the completed source identity and the paired-zero identity have the same left side. Therefore, on the connected domain `Re x>1/4`,

\[
\int_0^\infty e^{-xt}H(t)\,dt
=
\int_0^\infty e^{-xt}
\bigl(K_E(t)+K_\Gamma(t)+K_P(t)\bigr)\,dt.
\]

Widder–Lerch uniqueness gives equality almost everywhere; normal convergence of `H`, continuity of the explicit kernels, and local uniform convergence of the prime series upgrade this to every `t>0`:

\[
H(t)=K_E(t)+K_\Gamma(t)+K_P(t).
\]

The orbit convention produces no factor two: on RH, the functional-equation orbit pairs ordinates `gamma` and `-gamma`, so one positive ordinate contributes one heat atom with its original multiplicity.

## Disposition

The source-normalized paired-Hadamard/Laplace bridge is complete. The remaining RH-strength statement is the independent implication that the explicit endpoint–gamma–prime kernel has the required all-rank Hankel positivity. Neither transform equality nor pointwise kernel positivity proves that cone condition.