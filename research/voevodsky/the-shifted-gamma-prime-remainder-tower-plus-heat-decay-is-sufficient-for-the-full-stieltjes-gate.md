# The shifted gamma--prime remainder tower plus heat decay is sufficient for the full Stieltjes gate

## Objective

Continue the endpoint-extraction argument one step further.

Once positivity of the shifted gamma--prime remainder tower forces the exact endpoint counter-atom, the complete shifted tower becomes positive. Its nested principal submatrices already supply the support condition on \([0,\infty)\). Completed-heat decay then integrates the positive derivative measure and recovers the ordinary completed tower.

Thus, subject to the analytic reconstruction hypotheses, one positive remainder tower is sufficient for the full scalar Stieltjes/RH gate.

## Remainder tower

Let

\[
R(t)
=
\Theta(t)
-

e^{t/4}.
\]

Fix \(t_0>0\) and define

\[
c_k
=
(-1)^{k+1}
R^{(k+1)}(t_0).
\]

The shifted remainder Hankel matrices are

\[
C_r
=
(
c_{i+j}
)_{0\le i,j\le r}.
\]

Assume

\[
\boxed{
C_r
\succeq0
\quad
\text{for every }r\ge0.
}
\]

Assume also the determinacy, exponential-moment, and completed-heat decay hypotheses required to reconstruct the derivative source from this moment sequence.

## Endpoint extraction

The positive representing measure \(\mu_R\) of \((c_k)\) satisfies

\[
-
R'(t_0+s)
=
\int_{
\mathbb R
}

e^{-sx}
\,d\mu_R(x).
\]

Completed-heat decay gives

\[
-
R'(t_0+s)
=

c_E

e^{s/4}
+
o(

e^{s/4}
),
\]

where

\[
c_E
=
\frac14

e^{t_0/4}.
\]

Hence

\[
\mu_R
=

c_E
\delta_{-1/4}
+
\eta,
\qquad
\eta
\ge0.
\]

Subtracting the endpoint atom gives the moments of the complete derivative source:

\[
d_{k+1}
=
(-1)^{k+1}
\Theta^{(k+1)}(t_0)
=
\int
x^k
\,d\eta(x).
\]

Therefore the complete shifted matrices satisfy

\[
\boxed{
H_r^+
=
(
d_{i+j+1}
)_{0\le i,j\le r}
\succeq0.
}
\]

## Automatic nonnegative support

Define the derivative moment sequence

\[
e_k
=
d_{k+1}.
\]

Its ordinary Hankel matrices are precisely

\[
(
e_{i+j}
)
=
H_r^+.
\]

Its shifted Hankel matrices are

\[
(
e_{i+j+1}
)
=
(
d_{i+j+2}
)_{0\le i,j\le r}.
\]

But this is the principal submatrix of \(H_{r+1}^+\) obtained by deleting its first row and column. Hence it is positive.

Thus both Stieltjes towers for \((e_k)\) are automatically positive:

\[
(
e_{i+j}
)
\succeq0,
\qquad
(
e_{i+j+1}
)
\succeq0.
\]

The derivative representing measure can therefore be chosen on

\[
[0,\infty).
\]

Write it as \(\eta_+\):

\[
e_k
=
\int_0^\infty
\lambda^k
\,d\eta_+(
\lambda
).
\]

## Reconstruction of the complete derivative

Under the admitted right-half-plane holomorphy and exponential-moment bounds,

\[
-
\Theta'(t)
=
\int_0^\infty

e^{-t\lambda}
\,d\sigma(
\lambda
)
\]

for one positive measure \(\sigma\), obtained from \(\eta_+\) by undoing the tilt at \(t_0\).

Thus \(-\Theta'\) is completely monotone.

## Integration using heat decay

Assume

\[
\Theta(t)
\longrightarrow
0
\]

as \(t\to\infty\). Then

\[
\Theta(t)
=
\int_t^\infty
-
\Theta'(s)
\,ds.
\]

Tonelli's theorem gives

\[
\Theta(t)
=
\int_{(0,\infty)}
\left(
\int_t^\infty

e^{-s\lambda}
\,ds
\right)
\,d\sigma(
\lambda
).
\]

Therefore

\[
\boxed{
\Theta(t)
=
\int_{(0,\infty)}

e^{-t\lambda}
\frac{
d\sigma(
\lambda
)
}
{
\lambda
}.
}
\]

A mass of \(\sigma\) at \(\lambda=0\) would make the integral of \(-\Theta'\) diverge or leave a nondecaying component, so completed-heat decay excludes such a mass in the admitted class.

Set

\[
d\nu(
\lambda
)
=
\lambda^{-1}
\,d\sigma(
\lambda
).
\]

Then \(\nu\ge0\) and

\[
\Theta(t)
=
\int_0^\infty

e^{-t\lambda}
\,d\nu(
\lambda
).
\]

Hence \(\Theta\) is completely monotone.

## Ordinary tower follows

The reconstructed positive measure gives

\[
d_k
=
\int_0^\infty
\lambda^k

e^{-t_0\lambda}
\,d\nu(
\lambda
).
\]

Therefore

\[
\boxed{
H_r
=
(
d_{i+j}
)_{0\le i,j\le r}
\succeq0
}
\]

for every \(r\).

Thus ordinary completed Hankel positivity is not independent once the shifted derivative source and decay are controlled.

## Single-tower reduction

Combining the steps gives

\[
\boxed{
\begin{aligned}
&C_r
=
H_r^{R,+}(t_0)
\succeq0
\quad
\text{for every }r\\
&\quad+
\text{analytic reconstruction}\\
&\quad+
\text{differentiated endpoint asymptotic}\\
&\quad+
\Theta(t)
\to0
\\[1mm]
&\Longrightarrow
\Theta
\text{ is completely monotone.}
\end{aligned}
}
\]

By evenness and Laplace uniqueness, this supplies the source-faithful positive spectral measure and excludes every hostile off-axis rotor.

## Source-side formula for the remaining tower

The entries of \(C_r\) are

\[
c_k
=
D_{k+1}^G(t_0)
+
D_{k+1}^P(t_0),
\]

because the endpoint term has been removed before differentiation.

Explicitly,

\[
\begin{aligned}
c_k
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
\right)_{k+1}

t_0^{-k-3/2}\\
&+
\frac1{4\pi}
\int_{\mathbb R}

u^{2k+2}

e^{-t_0u^2}
\operatorname{Re}
\psi
\left(
\frac14+
\frac{iu}{2}
\right)
\,du\\
&-
\frac{
(k+1)!
}
{
2\sqrt\pi

t_0^{k+3/2}
}
\sum_{n\ge2}
\frac{
\Lambda(n)
}
{
\sqrt n
}

e^{-y_n}
L_{k+1}^{-1/2}(y_n).
\end{aligned}
\]

The sole matrix inequality is

\[
\boxed{
\sum_{i,j=0}^r
\overline{a_i}
a_j
c_{i+j}
\ge0
}
\]

for every finite coefficient vector and every rank.

## Polynomial form

For

\[
p(x)
=
\sum_{j=0}^r

a_jx^j,
\]

the remaining form is

\[
\mathcal C_{t_0}(p)
=
\sum_{i,j}
\overline{a_i}
a_j
c_{i+j}.
\]

Its gamma-integral part is

\[
\frac1{4\pi}
\int_{
\mathbb R
}

u^2
|p(u^2)|^2

e^{-t_0u^2}
\operatorname{Re}
\psi
\left(
\frac14+
\frac{iu}{2}
\right)
\,du,
\]

with the gamma constant and prime Laguerre matrix retained in the same coupled form.

This is the final single-tower source inequality.

## Caveats

The reduction requires more than formal \(\Theta(t)\to0\). It needs:

1. moment determinacy for \((c_k)\);
2. exponential moments sufficient to reconstruct \(-R'\);
3. differentiated completed-heat asymptotics;
4. no untracked growing terms;
5. Tonelli-integrability of the reconstructed derivative measure;
6. the exact source-to-divisor conformance and evenness hypotheses.

These analytic inputs must be sourced independently of the desired zero-location conclusion.

## Tetrahedral consequence

The endpoint Schur gate, ordinary Hankel tower, and hostile-rotor exclusion all become consequences of one positive source cell: the shifted gamma--prime remainder Hankel tower.

Thus the positive tetrahedral lift can be targeted by one nested sequence of source matrices rather than three separate inequalities.

## Disposition

Subject to the declared analytic reconstruction and decay conditions, the full source-faithful positive lift is equivalent to the single tower

\[
\boxed{
H_r^{R,+}(t_0)
\succeq0
\quad
\text{for every }r\ge0.
}
\]

This is now the narrowest coupled source target produced by the hostile-rotor and endpoint analyses.
