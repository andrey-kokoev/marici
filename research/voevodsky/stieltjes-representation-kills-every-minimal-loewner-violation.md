# A Stieltjes representation kills every minimal Loewner violation

On a zero-free positive interval let

\[
R(x)=\frac{P(x)}{I(x)},\qquad
q(x,y)=\frac{R(y)-R(x)}{x-y}.
\]

The exact sufficient source theorem is the existence of `beta>=0` and a
positive measure `mu`, independent of `x`, such that

\[
\boxed{
R(x)=\alpha-\beta x+
\int_{[0,\infty)}\frac{d\mu(t)}{x+t}.}
\]

Indeed,

\[
\boxed{
q(x,y)=\beta+
\int_{[0,\infty)}
\frac{d\mu(t)}{(x+t)(y+t)}.}
\]

Hence with

\[
r_x=\sqrt\beta\oplus\left(t\mapsto\frac1{x+t}\right)
\in\mathbb R\oplus L^2(\mu),
\]

one has `q(x,y)=<r_x,r_y>`. Every finite Loewner matrix is therefore positive
semidefinite. In particular, for every positive old packet `A` and new column
`b`, automatically

\[
b\in\operatorname{ran}A,
\qquad
q(x,x)-b^TA^\dagger b\ge0.
\]

Thus both minimal-witness failure modes are impossible at once. No
stationarity, rank bound, or compactification argument is needed.

## Derivative consequences and their limitation

The representation implies

\[
(-1)^m R^{(m)}(x)
=\mathbf 1_{m=1}\beta+
 m!\int\frac{d\mu(t)}{(x+t)^{m+1}}
\quad(m\ge1),
\]

with the evident sign correction: `R'<=0`, `R''>=0`, and alternating higher
derivatives. More precisely, `-R'` is an order-two Stieltjes transform,

\[
-R'(x)=\beta+
\int\frac{d\mu(t)}{(x+t)^2}.
\]

Alternating scalar derivatives alone are not enough: complete monotonicity
only gives a Laplace representation and does not force the resolvent Gram
kernel above. What is required is the stronger common positive measure in the
order-two Stieltjes representation.

## Denominator-free theta target

Since `R=P/I`, the derivative density is

\[
-R'(x)=\frac{P(x)I'(x)-P'(x)I(x)}{I(x)^2}.
\]

Therefore the remaining source statement can be posed without selecting
zeros:

\[
\boxed{
P I'-P'I
=I^2\left(\beta+
\int_{[0,\infty)}\frac{d\mu(t)}{(x+t)^2}\right).}
\]

Here `I` and `P` are the paired transforms of `K` and `Phi`. A construction of
`mu` directly from the modular theta labels would finish the all-rank
positivity argument. Recovering `mu` from the poles or zeros of `R` would not
be a source construction and gives no contradiction proof.

Prior work sharply restricts what such a construction can be. The free
ancestor `L_0=1/4-partial_u^2`, with any ordinary `L^2` cyclic vector, has an
absolutely continuous spectral measure, whereas meromorphic continuation of
the required response forces a discrete Stieltjes measure. The canonical
one-density confining choice

\[
A_\Phi=\frac14+Q_\Phi^*Q_\Phi,
\qquad Q_\Phi=\partial_u-\frac12(\log\Phi)',
\]

also has the wrong spectral locations. Consequently neither choosing a better
vector for the free carrier nor using only the scalar density `Phi` can
construct `mu`. The remaining operator candidate must retain the labelled
modular sewing, likely through a matrix-valued canonical or Jacobi system.

## Concrete next falsifier

An order-two Stieltjes function must satisfy all Stieltjes moment Hankel
conditions after expansion at any positive base point. Failure of one finite
Hankel minor for the jets of `-R'` disproves this proposed representation even
if ordinary Loewner positivity survives. Passing finitely many such minors is
only evidence; proving the common measure requires the complete hierarchy or
a direct theta pushforward construction.
