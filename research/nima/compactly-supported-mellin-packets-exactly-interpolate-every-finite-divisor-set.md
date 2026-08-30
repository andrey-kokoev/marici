# Compactly supported Mellin packets exactly interpolate every finite divisor set

Event 10289 used an entire Gaussian interpolant but left source authority
open. Finite interpolation can be done directly inside the standard
compactly supported smooth Mellin class.

Work in logarithmic coordinate \(x=\log u\). Choose

\[
h\in C_c^\infty(\mathbb R)
\]

with bilateral Laplace transform

\[
H(s)=\int_{\mathbb R}h(x)e^{sx}\,dx.
\]

For a real translation \(x_j\), define

\[
h_j(x)=h(x-x_j).
\]

Then

\[
\widehat h_j(s)=e^{s x_j}H(s).
\]

Let

\[
Z=\{z_1,\ldots,z_N\}
\]

be any finite set of distinct divisor evaluation points. Choose \(h\) so that

\[
H(z_k)\ne0
\qquad(1\le k\le N).
\]

This is possible because nonvanishing at finitely many points is an open
generic condition on the bump.

Now choose real translations \(x_1,\ldots,x_N\) such that the exponential
evaluation matrix

\[
V_{kj}=e^{z_kx_j}
\]

is invertible. Such choices exist because the functions
\(x\mapsto e^{z_kx}\) are linearly independent for distinct \(z_k\); their
evaluation determinant is not identically zero.

For arbitrary target values \(c_1,\ldots,c_N\), solve

\[
\sum_{j=1}^N a_j e^{z_kx_j}H(z_k)=c_k.
\]

Then

\[
f=\sum_{j=1}^N a_jh_j
\]

lies in \(C_c^\infty(\mathbb R)\) and satisfies

\[
\widehat f(z_k)=c_k
\qquad(1\le k\le N).
\]

Thus the compactly supported smooth Mellin test class separates every finite
divisor packet exactly.

## Weil hostile

Taking

\[
c(\rho)=1,
\qquad
c(\rho^\vee)=-1,
\qquad
c(z)=0
\]

at all other points of a finite packet produces the exact negative swap mode
without leaving the standard explicit-formula test class.

Therefore finite source authority is closed. No arbitrary entire Gaussian or
postulated evaluation vector is needed.

## What remains at completion

The coefficients \(a_j\), translation range, support diameter, and
\(C_c^\infty\) seminorms may grow rapidly with \(N\), point height, or
separation. The condition number is governed by

\[
\left\|
\left[
H(z_k)e^{z_kx_j}
\right]^{-1}
\right\|.
\]

Hence the unresolved theorem is quantitative, not algebraic:

- obtain bounds for finite packets adapted to height cutoffs;
- control leakage from zeros outside the packet;
- pass the negative value through the explicit-formula completion.

For the logical Weil criterion, one may not need a uniform bound over all
packets: given one hypothetical off-seam pair, a sequence of expanding
finite interpolants with controlled tail error can suffice. The required
estimate is therefore

\[
\text{tail contribution}
<
\text{fixed local negative mass},
\]

not necessarily uniform interpolation over the entire divisor.

This reduces the terminal test-space frontier to a concrete
interpolation-versus-tail inequality inside a fully authorized Mellin class.
