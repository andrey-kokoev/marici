# The central Euler current and its first jet form a uniformly faithful normalized valuation frame

## Result

The source-authorized zeroth reciprocal current is exactly the complementary valuation observer missing from the Euler first jet.

After dividing by the frozen local half-density scales, the zeroth current and first jet have no common spectral zero and form a uniformly positive frame over every prime.

Thus the full bilateral valuation Hilbert space has a source-native two-port arithmetic observer. No restriction to the vacuum line is needed locally.

## Two source ports

Let

\[
a=p^{-1/2},
\qquad
L=\log p,
\]

and let \(U\) be the bilateral shift.

The central reciprocal current is

\[
\mathcal J_p(0)
=
\sum_{k\ge1}
\frac{a^k}{k}
\left(
U^k-U^{-k}
\right).
\]

It is skew-adjoint. Define its self-adjoint oriented port

\[
Q_p=-i\mathcal J_p(0).
\]

The first central jet is

\[
D_p
=
\mathcal J_p'(0)
=
L\sum_{k\ge1}a^k
\left(
U^k+U^{-k}
\right).
\]

Both operators come from the same reciprocal Euler constructor. The first is seam-skew; the second is the normal derivative.

## Fourier symbols

On \(L^2(\mathbb T)\), the first-jet symbol is

\[
d_{a,L}(\theta)
=
2L\sum_{k\ge1}a^k\cos(k\theta)
=
2L
\frac{a\cos\theta-a^2}
{1-2a\cos\theta+a^2}.
\]

The self-adjoint zeroth-current symbol is

\[
q_a(\theta)
=
2\sum_{k\ge1}
\frac{a^k}{k}\sin(k\theta).
\]

Using the logarithmic sum,

\[
q_a(\theta)
=
2\operatorname{Arg}
\left(
1-ae^{-i\theta}
\right)
\]

with the continuous branch fixed by \(q_a(0)=0\). Equivalently,

\[
q_a(\theta)
=
2\arctan
\left(
\frac{a\sin\theta}
{1-a\cos\theta}
\right).
\]

The denominator is positive because \(0<a<1\).

## No common spectral zero

The first-jet symbol vanishes exactly when

\[
\cos\theta=a.
\]

At such a point,

\[
\sin\theta=\pm\sqrt{1-a^2},
\]

and

\[
q_a(\theta)
=
\pm2\arctan
\left(
\frac{a}{\sqrt{1-a^2}}
\right)
\ne0.
\]

Conversely, \(q_a(\theta)=0\) exactly when

\[
\sin\theta=0,
\]

so \(\theta=0\) or \(\pi\). At those points,

\[
d_{a,L}(0)
=
\frac{2La}{1-a}>0,
\]

\[
d_{a,L}(\pi)
=
-\frac{2La}{1+a}<0.
\]

Therefore

\[
|q_a(\theta)|^2+|d_{a,L}(\theta)|^2>0
\]

for every prime and every spectral point.

## Source normalization

The two ports have different physical scales:

- \(Q_p\) begins at size \(a\);
- \(D_p\) begins at size \(La\).

Normalize by those independently frozen Euler half-density factors:

\[
\widetilde q_a(\theta)
=
\frac{q_a(\theta)}{a},
\]

\[
\widetilde d_a(\theta)
=
\frac{d_{a,L}(\theta)}{La}
=
2\frac{\cos\theta-a}
{1-2a\cos\theta+a^2}.
\]

This is not fitted normalization. The factors \(a\) and \(La\) are the primitive Euler amplitude and its logarithmic position derivative.

As \(a\downarrow0\),

\[
\widetilde q_a(\theta)\longrightarrow2\sin\theta,
\]

\[
\widetilde d_a(\theta)\longrightarrow2\cos\theta
\]

uniformly in \(\theta\).

Thus both symbols extend continuously to \(a=0\).

## Uniform prime frame

All primes satisfy

\[
0<a\le2^{-1/2}.
\]

Consider the compact parameter set

\[
[0,2^{-1/2}]\times\mathbb T.
\]

The function

\[
F(a,\theta)
=
|\widetilde q_a(\theta)|^2
+
|\widetilde d_a(\theta)|^2
\]

is continuous there.

At \(a=0\),

\[
F(0,\theta)=4.
\]

For \(a>0\), the no-common-zero theorem gives

\[
F(a,\theta)>0.
\]

Compactness therefore yields

\[
\delta_{\mathrm{val}}^2
=
\min_{\substack{0\le a\le2^{-1/2}\\\theta\in\mathbb T}}
F(a,\theta)
>0.
\]

Hence, on every local bilateral valuation fiber,

\[
\|\widetilde Q_px\|^2
+
\|\widetilde D_px\|^2
\ge
\delta_{\mathrm{val}}^2\|x\|^2,
\]

uniformly over all primes.

The matching upper bound also follows from compactness.

## Global direct sum

On the block-diagonal prime direct sum, define

\[
\mathcal O_E
=
\begin{pmatrix}
\bigoplus_p\widetilde Q_p\\
\bigoplus_p\widetilde D_p
\end{pmatrix}.
\]

The uniform local frame gives

\[
\|\mathcal O_Ex\|
\ge
\delta_{\mathrm{val}}\|x\|
\]

on the Hilbert direct sum.

Thus the arithmetic odd plane has a genuine essential lower margin before theta sampling.

The compact theta/Wronskian route may now be attached as a third realization/calibration port without being asked to supply essential coercivity.

## Typing qualification

The theorem uses the full bilateral valuation fiber and its Fourier spectral representation. To enter the mixed Adams cell, one must still prove that:

- both \(Q_p\) and \(D_p\) preserve the admitted primitive/square boundary domains;
- reciprocal reflection acts with the declared characters;
- the normalization agrees with the source Euler half-density metric;
- cutoff direct sums are the authorized global assembly;
- the mixed incidence does not quotient out one of the two ports.

The spectral frame is exact once those domain identifications are admitted.

## Consequence

The arithmetic observability problem now has the desired separation:

\[
\text{uniform two-port valuation frame}
\longrightarrow
\text{compact theta realization}
\longrightarrow
\text{Wronskian/seam calibration}.
\]

The first arrow supplies essential coercivity. The latter arrows supply source realization and orientation comparison.

This avoids demanding a noncompact inverse from the theta source.

## Next gate

The remaining first-edge theorem is now a domain-intertwining statement:

> Prove that the primitive-to-square Adams boundary incidence carries both normalized valuation ports into the enlarged Green cell without radical leakage or mixed-output cancellation.

That theorem, rather than another scalar normalization, is the next bridge into the global five-margin system.
