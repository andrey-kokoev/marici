# Discrete SSR-infinity does not orient cosine-transform zeros

## Outcome

The integral-square completed-circle kernel is strictly sign regular of all
orders. This gives a genuine variation-diminishing map from signed mode
coefficients to functions of scale. It does not imply that a positive mode
sum has a cosine transform with only real zeros.

The missing implication is false even for the canonical Laplace kernel.

## Finite separation witness

Consider

\[
K(u,\lambda)=e^{-u\lambda},
\qquad u,\lambda>0.
\]

For ordered \(\lambda_1<\cdots<\lambda_n\), the Wronskian of the functions
\(e^{-\lambda_j u}\) is

\[
e^{-u\sum_j\lambda_j}
\det[(-\lambda_j)^{k-1}]_{k,j=1}^n,
\]

so \(K\) is strictly reverse-sign-regular of every order.

Take two positive mode weights:

\[
\phi(u)=e^{-u}+e^{-2u}.
\]

Its cosine transform, initially for real \(z\), is

\[
\begin{aligned}
F(z)
&=\int_0^\infty\phi(u)\cos(zu)\,du\\
&=\frac1{1+z^2}+\frac2{4+z^2}\\
&=\frac{3(z^2+2)}{(1+z^2)(4+z^2)}.
\end{aligned}
\]

Therefore

\[
F(\pm i\sqrt2)=0.
\]

The spectral kernel is SSR-infinity, the weights are positive, and the
cosine transform nevertheless has nonreal zeros. This is a finite logical
falsifier for the proposed bridge.

## What the arithmetic theorem does prove

For every finitely supported real coefficient sequence \(c_m\), the
integral-square spectral transform

\[
g(t)=\sum_m c_m b(t,m^2)
\]

cannot have more sign changes in \(t\) than the ordered sequence \(c_m\),
with the usual strict qualifications. This is the correct
variation-diminishing content of the all-order minor theorem.

For the completed theta density all coefficients are positive. The theorem
then recovers positivity and rigidity of the mode mixture, but zero sign
changes in \(\Phi\) say nothing by themselves about complex zeros after the
oscillatory cosine transform.

## Why translation PF-infinity is not the repair

One might try to strengthen spectral sign regularity to total positivity of
the translation kernel

\[
\Phi(r-s).
\]

The existing Schoenberg audit already rules this out for the completed theta
density. If \(\Phi\) were a Pólya-frequency function of infinite order, its
bilateral Laplace transform would have reciprocal Laguerre-Pólya form and
would be zero-free on its entire continuation. Here that continuation is the
completed Xi transform up to convention, and unconditionally known
critical-line zeros contradict zero-freeness.

Thus translation PF-infinity is too strong and is not an RH-compatible
bridge. The new spectral SSR-infinity theorem and the old translation
PF-infinity no-go concern different kernels and are perfectly consistent.

## Typed diagram

\[
\begin{array}{ccc}
\{c_m\}
&\xrightarrow{\ b(t,m^2)\ }&
g(t)\\
&&\downarrow\ t=e^{2u},\ \text{sum}\\
&&\Phi(u)\\
&&\downarrow\ \text{cosine transform}\\
&&\Xi(z).
\end{array}
\]

SSR-infinity controls only the first arrow. Neither the nonlinear chart,
positive infinite summation, nor the cosine transform is automatically a
sign-regular constructor of the required type.

## Consequence for the RH lane

The durable gain remains substantial:

\[
\text{adelic integrality}
\Longrightarrow
\text{all-order spectral variation diminution}.
\]

But the direct route

\[
\text{spectral SSR}_{\infty}
\Longrightarrow
\text{real zeros of the cosine transform}
\]

is closed.

Any further RH-bearing step must add a different source-derived interaction
law coupling the scale variable to the oscillatory transform. Candidate
laws must be tested directly on the denominator-free Loewner/de Branges
kernel or another RH-relevant two-parameter object; they cannot be inferred
from coefficient-to-scale variation diminution alone.

## Finite falsifier

For any proposed theorem claiming that positive mixtures of an
SSR-infinity spectral kernel have real-zero cosine transforms, the pair

\[
K(u,\lambda)=e^{-u\lambda},
\qquad
c_1=c_2=1,\quad\lambda_1=1,\lambda_2=2
\]

is the smallest counterexample.

