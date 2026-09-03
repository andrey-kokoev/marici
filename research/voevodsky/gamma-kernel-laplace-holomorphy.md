# Gamma-kernel Laplace holomorphy

## Question

Does the explicit gamma heat kernel have an absolutely convergent Laplace transform for complex \(x\) throughout the common initial domain?

## Claim boundary

Yes. The explicit kernel is locally integrable at zero and of polynomial order at infinity. Its Laplace transform is holomorphic for \(\operatorname{Re}x>0\), so it imposes no restriction beyond the endpoint boundary \(\operatorname{Re}x>1/4\). Identification with the digamma expression still inherits the source identity proved in the gamma packet.

## Kernel

Write

\[
K_\Gamma(t)
=
\frac{-\gamma_E-\log\pi+J(t)}{4\sqrt{\pi t}},
\]

where

\[
J(t)
=
\int_0^\infty
\frac{e^{-r}-e^{-r/4-r^2/(16t)}}{1-e^{-r}}\,dr.
\]

The apparent singularity at \(r=0\) is removable because both exponentials equal one there.

## Small \(t\)

For \(0<t\leq1\), split the \(r\)-integral into

\[
(0,t),
\qquad
(t,1),
\qquad
(1,\infty).
\]

On \((0,t)\), the mean-value estimate for the numerator and

\[
1-e^{-r}\asymp r
\]

give an integrated \(O(1)\) bound.

On \((t,1)\), division by \(1-e^{-r}\asymp r\) gives

\[
O\left(\int_t^1\frac{dr}{r}\right)
=
O(|\log t|).
\]

On \((1,\infty)\), the denominator is bounded away from zero and the exponential tails are integrable. Therefore

\[
J(t)=O(1+|\log t|)
\]

and

\[
K_\Gamma(t)
=
O\left(t^{-1/2}(1+|\log t|)\right).
\]

This is integrable at zero because

\[
\int_0^1t^{-1/2}\,dt=2
\]

and

\[
\int_0^1t^{-1/2}(-\log t)\,dt=4.
\]

## Large \(t\)

For \(t\geq1\), the removable quotient is uniformly bounded on \((0,1)\). On \((1,\infty)\), both numerator exponentials are bounded by constant multiples of \(e^{-r/4}\). Hence

\[
J(t)=O(1)
\]

and

\[
K_\Gamma(t)=O(t^{-1/2}).
\]

## Complex Laplace domain

For every compact subset of

\[
\operatorname{Re}x>0,
\]

the small- and large-\(t\) bounds provide an integrable majorant for

\[
e^{-xt}K_\Gamma(t).
\]

Thus

\[
\int_0^\infty e^{-xt}K_\Gamma(t)\,dt
\]

converges absolutely and locally uniformly and is holomorphic for \(\operatorname{Re}x>0\).

In particular it is holomorphic throughout the completed common domain

\[
\operatorname{Re}x>\frac14.
\]

## Disposition

The gamma kernel does not narrow the common transform half-plane. The remaining gamma obligation is source-level identification of this transform with the stated digamma expression and joint verification of constants; convergence for complex \(x\) is resolved.

## Verification

- `research/voevodsky/gamma-kernel-laplace-holomorphy-v1.json`
- `research/voevodsky/checkers/check_gamma_kernel_laplace_holomorphy.py`
- `research/voevodsky/results/gamma_kernel_laplace_holomorphy.json`
