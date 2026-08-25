# The completed circle kernel is strictly sign-regular of order two

## Bounded question

Does the positive completed operator family of packet 107 carry a coherent
variation-diminishing orientation across scale and winding energy?

## Scalar spectral kernel

For continuous spectral parameter `x>=1` and completed scale `t>=1`, define

\[
 b(t,x)
 =\pi x\,t^{5/4}(2\pi tx-3)e^{-\pi tx}.
\]

The winding eigenvalues of `B_t` are `b(t,n^2)`.  Positivity follows from
`2 pi t x-3>0` on the stated domain.

## Exact monotone-likelihood-ratio calculation

For `y>x>=1`, differentiate the logarithmic ratio:

\[
 \frac{\partial}{\partial t}
 \log\frac{b(t,y)}{b(t,x)}
 =
 \frac{2\pi y}{2\pi ty-3}
 -\frac{2\pi x}{2\pi tx-3}
 -\pi(y-x).
\]

At fixed `t`, the function

\[
 g_t(x)=\frac{2\pi x}{2\pi tx-3}
\]

satisfies

\[
 g_t'(x)=\frac{-6\pi}{(2\pi tx-3)^2}<0.
\]

Therefore both terms in

\[
 g_t(y)-g_t(x)-\pi(y-x)
\]

are strictly negative, and

\[
 \boxed{
 \frac{\partial}{\partial t}
 \log\frac{b(t,y)}{b(t,x)}<0.}
\]

This is a global reverse monotone-likelihood-ratio law.

## Oriented minors

For `1<=t_1<t_2` and `1<=x_1<x_2`, the ratio law is equivalent to

\[
 \boxed{
 \det
 \begin{pmatrix}
 b(t_1,x_1)&b(t_1,x_2)\\
 b(t_2,x_1)&b(t_2,x_2)
 \end{pmatrix}<0.}
\]

Reversing the winding-energy order makes every supported order-two minor
positive.  The completed kernel is therefore strictly sign-regular of order
two, with one coherent orientation over the entire outer chart.  No bandwise
sign choices or fitted gauge are required.

Restricting `x` to the integral spectrum `n^2` preserves the theorem.  Thus
every pair of winding modes crosses in relative weight at most once as scale
increases; higher-energy modes decay monotonically faster in the normalized
comparison.

## Why the completion polynomial matters

The factor `2 pi t x-3` could have introduced an interior fold.  The integral
gap and `t>=1` keep its zero at

\[
 tx=\frac3{2\pi}<1
\]

outside the physical chart.  Moreover, its logarithmic derivative reinforces
rather than opposes the exponential ordering.  Completion therefore preserves
the heat kernel's coherent orientation on precisely the source-authorized
domain.

## Explanatory gain

Packets 101--107 explained which modes exist, why the circle appears, and why
the completed kernel is positive.  This packet adds a dynamical statement:

\[
 \boxed{
 \text{integral spectral gap}
 +\text{completion differential}
 +\text{heat flow}
 \Longrightarrow
 \text{one coherent order-two orientation}.}
\]

This is the first exact variation-diminishing law obtained from the completed
circle operator rather than conjectured from the final scalar transform.

## RH boundary and next falsifier

Order-two sign regularity does not imply total positivity of every order and
does not imply that the cosine transform has only real zeros.  The next gate
is the order-three minor.  Because the kernel is an exponential multiplied by
an affine polynomial in `tx`, its third-order determinant is the smallest
place where the completion factor can create a new circuit not detected by
monotone likelihood ratios.

The sharp falsifier is one ordered triple `t_1<t_2<t_3`, `x_1<x_2<x_3` for
which the canonically oriented third-order determinant changes sign.  The
preferred attack is symbolic factorization or a Chebyshev-system proof, not a
finite numerical census.
