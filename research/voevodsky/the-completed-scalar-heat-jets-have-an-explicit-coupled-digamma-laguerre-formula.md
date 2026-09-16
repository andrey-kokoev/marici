# The completed scalar heat jets have an explicit coupled digamma--Laguerre formula

## Objective

Write the complete-monotonicity target explicitly, with endpoint, gamma, and prime contributions differentiated in one common normalization.

This closes the formula-construction step. It does not prove the resulting inequalities.

## Scalar completed heat source

At zero shift, the explicit Gaussian Weil source is

\[
\Theta(t)
=
E(t)
+
G(t)
+
P(t),
\qquad
t>0,
\]

with

\[
E(t)
=

e^{t/4},
\]

\[
G(t)
=
-
\frac{
\log\pi
}
{
4\sqrt{
\pi t
}
}
+
\frac1{4\pi}
\int_{\mathbb R}

e^{-tu^2}
\operatorname{Re}
\psi
\left(
\frac14+
\frac{iu}{2}
\right)
\,du,
\]

and

\[
P(t)
=
-
\frac1{2\sqrt{
\pi t
}}
\sum_{n\ge2}
\frac{
\Lambda(n)
}
{
\sqrt n
}
\exp
\left(
-
\frac{
(
\log n
)^2
}
{
4t
}
\right).
\]

All three terms must be retained before testing signs.

## Completed heat jets

Define

\[
D_k(t)
=
(-1)^k
\frac{d^k}{dt^k}
\Theta(t),
\qquad
k\in\mathbb N_0.
\]

Complete monotonicity is exactly

\[
D_k(t)
\ge
0
\]

for every \(k\ge0\) and \(t>0\).

## Endpoint jet

Direct differentiation gives

\[
\boxed{
D_k^E(t)
=
(-1)^k
4^{-k}

e^{t/4}.
}
\]

The endpoint contribution alternates in sign and is not separately completely monotone.

## Gamma jet

Let

\[
\left(
\frac12
\right)_k
=
\frac{
\Gamma(k+1/2)
}
{
\Gamma(1/2)
}
\]

be the rising Pochhammer symbol. Then

\[
(-1)^k
\frac{d^k}{dt^k}
t^{-1/2}
=
\left(
\frac12
\right)_k

t^{-k-1/2}.
\]

Differentiating the Gaussian under the integral gives

\[
(-1)^k
\partial_t^k

e^{-tu^2}
=
u^{2k}

e^{-tu^2}.
\]

Therefore

\[
\boxed{
\begin{aligned}
D_k^G(t)
={}&
-
\frac{
\log\pi
}
{
4\sqrt\pi
}
\left(
\frac12
\right)_k

t^{-k-1/2}\\
&+
\frac1{4\pi}
\int_{\mathbb R}

u^{2k}

e^{-tu^2}
\operatorname{Re}
\psi
\left(
\frac14+
\frac{iu}{2}
\right)
\,du.
\end{aligned}
}
\]

For every fixed \(t>0\) and \(k\), the integral is absolutely convergent because the digamma factor has logarithmic growth while the Gaussian moment decays rapidly.

## Prime jet

For

\[
a_n
=
\log n,
\qquad

y_n
=
\frac{
a_n^2
}
{
4t
},
\]

set

\[
g_{a_n}(t)
=
t^{-1/2}

e^{-y_n}.
\]

The exact Laguerre identity is

\[
(-1)^k
\partial_t^k
g_{a_n}(t)
=

t^{-k-1/2}

e^{-y_n}

k!
L_k^{-1/2}(y_n).
\]

Hence

\[
\boxed{
D_k^P(t)
=
-
\frac{
k!
}
{
2\sqrt\pi

t^{k+1/2}
}
\sum_{n\ge2}
\frac{
\Lambda(n)
}
{
\sqrt n
}

e^{-y_n}
L_k^{-1/2}(y_n).
}
\]

The sum converges absolutely for every fixed \(t>0\) and finite \(k\).

## Full coupled formula

Combining the three channels gives

\[
\boxed{
\begin{aligned}
D_k(t)
={}&
(-1)^k
4^{-k}

e^{t/4}\\
&-
\frac{
\log\pi
}
{
4\sqrt\pi
}
\left(
\frac12
\right)_k

t^{-k-1/2}\\
&+
\frac1{4\pi}
\int_{\mathbb R}

u^{2k}

e^{-tu^2}
\operatorname{Re}
\psi
\left(
\frac14+
\frac{iu}{2}
\right)
\,du\\
&-
\frac{
k!
}
{
2\sqrt\pi

t^{k+1/2}
}
\sum_{n\ge2}
\frac{
\Lambda(n)
}
{
\sqrt n
}

e^{-y_n}
L_k^{-1/2}(y_n).
\end{aligned}
}
\]

This is the explicit source-side complete-monotonicity hierarchy.

## Justification of differentiation

Fix

\[
0<t_0\le t\le t_1<\infty.
\]

For \(t\in[t_0,t_1]\), each differentiated gamma integrand is bounded by

\[
C_{k,t_0}
(
1+|u|
)^{2k}

e^{-t_0u^2}
\log(2+|u|),
\]

which is integrable.

For the prime series, each derivative is a polynomial in \(y_n\) times

\[

t^{-k-1/2}

e^{-y_n}.
\]

On the same compact \(t\)-interval, Gaussian decay in \(\log n\) dominates the von Mangoldt and polynomial Laguerre factors. Thus termwise differentiation is justified locally uniformly.

Consequently every \(D_k\) is continuous on \((0,\infty)\).

## Sectorwise signs cannot work

The three displayed terms have no stable separate sign:

1. \(D_k^E\) alternates with \(k\);
2. the real digamma factor changes relative size across \(u\);
3. \(L_k^{-1/2}\) changes sign as a function of \(y\).

Therefore complete monotonicity can only arise from coupled endpoint--gamma--prime cancellation.

Any proof that takes absolute values before adding the channels destroys the target mechanism.

## Zero-side interpretation

Under the exact completed divisor expansion, critical-line zeros give

\[
\Theta(t)
=
\sum_{
\gamma>0
}
m_\gamma

e^{-t\gamma^2}
\]

in the declared positive-ordinate normalization. Then

\[
D_k(t)
=
\sum_{
\gamma>0
}
m_\gamma

\gamma^{2k}

e^{-t\gamma^2}
\ge
0.
\]

An off-axis quartet instead contributes complex or signed squared spectral parameters, and the resulting exponential sum cannot be completely monotone at every order.

The source-side formula above states the same gate without assuming zero locations.

## Relation to centered source squares

The scalar hierarchy constructs the common Bernstein measure if all inequalities hold. Its symmetric square-root lift then generates every heat--character Gram and every centered Gaussian-square observation.

Thus proving the displayed \(D_k(t)\ge0\) hierarchy supplies the source-faithful positive carrier required by the tetrahedral theorem.

## Practical falsifier

For fixed \((k,t)\), a rigorous interval computation can:

1. enclose the endpoint term exactly;
2. enclose the digamma moment integral;
3. truncate the Laguerre-weighted prime sum with a certified tail;
4. add all channels before testing the sign.

A strictly negative enclosure is a valid complete-monotonicity falsifier. Positive checks at finitely many \((k,t)\) are diagnostic only.

## Remaining analytic target

The formula reduces the constructive search to finding an all-order representation of the form

\[
D_k(t)
=
\int_0^\infty
\lambda^k

e^{-t\lambda}
\,d\nu(
\lambda
)
\]

with one source-derived positive measure \(\nu\) independent of \(k\) and \(t\).

Constructing such a measure is equivalent to the desired complete monotonicity and remains RH-strength.

## Disposition

The coupled endpoint--gamma--prime heat jets are now explicit in one formula. The remaining proof problem is no longer differentiation or normalization; it is the all-order sign of this exact digamma--Laguerre combination.
