# Full labelled Poisson sewing rigidly selects the unweighted integer comb

## Question

After the integer heat-support gap rejects finite-germ hostiles, can a weighted
square-spectrum source remain admissible under the complete labelled
Fourier–Poisson correspondence?

## Source cone

Let

\[
\mu_w=\sum_{n\in\mathbb Z}w_n\delta_n
\]

be an order-zero tempered measure with polynomially bounded coefficients.
Positivity may be imposed by $w_n\geq0$, but the rigidity argument does not
need it. Evenness is $w_{-n}=w_n$.

The complete labelled sewing law is the distributional identity

\[
\mathcal F\mu_w=c\mu_w
\]

for a fixed nonzero scalar $c$, with one Fourier convention used throughout.
At first sight this appears stronger than the scalar Gaussian trace. For an
even tempered source, however, the complete continuous scale family recovers
the distributional identity, as shown below.

## Rigidity theorem

Because $\mu_w$ is supported on the integers, its Fourier transform is
one-periodic:

\[
\tau_1\mathcal F\mu_w=\mathcal F\mu_w.
\]

If $\mathcal F\mu_w=c\mu_w$, then

\[
\tau_1\mu_w=\mu_w.
\]

Translation by one sends the coefficient at $n$ to the coefficient at
$n+1$. Equality of the atomic measures therefore gives

\[
w_{n+1}=w_n
\]

for every integer $n$. Hence $w_n=w$ is constant and

\[
\mu_w=w\sum_{n\in\mathbb Z}\delta_n.
\]

With the self-dual normalization, the standard Dirac comb is Fourier-fixed, so
a nonzero solution has $c=1$. Source normalization fixes the remaining
overall scalar.

Thus no nonconstant weighted square-spectrum hostile survives full labelled
Poisson sewing in the order-zero comb category.

## Why this is not RH

The theorem selects the arithmetic source before scalar compression. It does
not orient the Mellin transform of the completed heat readout. The ordinary
integer comb is exactly the source whose completed transform carries the
unresolved zeros.

The gain is nevertheless decisive: weight deformation is not the next honest
hostile class. Any surviving hostile must alter a later constructor while
preserving this unique source.

## The all-scale scalar trace is faithful on the even sector

Assume the modular identity holds for every $t>0$:

\[
\Theta_w(t)=t^{-1/2}\Theta_w(1/t),
\]

Set $\eta=\mu_w-\mathcal F\mu_w$. Fourier covariance of the Gaussian shows
that modularity is exactly

\[
\langle\eta,e^{-\pi t x^2}\rangle=0
\]

for every $t>0$. Since $\eta$ is even, push it forward by $r=x^2$. The
displayed family is the Laplace transform of the resulting distribution on
$[0,\infty)$. Injectivity of the Laplace transform for distributions
supported on a half-line makes that pushforward zero.

Every even Schwartz test function has the form $\varphi(x^2)$ for a smooth
rapidly decaying half-line function $\varphi$, so the pushforward is faithful
on even distributions. Consequently $\eta=0$.

Therefore evenness, temperedness, and the exact scalar modular law at every
positive scale already imply full distributional Fourier sewing. The weaker
observer is a finite scale sample or finite jet, not the complete continuous
scalar scale family. There is no weighted hostile inside the declared class.

## Updated DPC

Full labelled Poisson sewing uniquely selects the integer comb, while RH
requires a further source-derived law ensuring that subsequent completion and
Mellin compression cannot create an off-seam scalar codiagonal zero.

The immediate attack has moved from coefficient classification to the
functoriality of the completion/readout map.
