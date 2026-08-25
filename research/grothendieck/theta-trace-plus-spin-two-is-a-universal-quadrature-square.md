# Theta trace plus spin two is a universal quadrature square

**Strictness correction:** at coefficient `lambda=+1` or `-1`, the coupled
form is nonnegative but rank one, not positive definite. Packet 148 isolates
the required complementary-sheet or boundary-transversality closure.

## Bounded algebraic question

Packet 146 identifies the completed Green bulk as a bare norm plus a
reflection-coboundary correction. Earlier work identifies these representation
types respectively as the invariant trace and spin-two curvature of one
two-copy source amplitude. Does their coupled sign still require a new
inequality?

## Universal coupled positivity theorem

Let

\[
 \psi=A+iB
\]

be any complex amplitude. Its invariant quadratic trace and oriented spin-two
component are

\[
 T=|\psi|^2=A^2+B^2,
 \qquad
 S=\Re(\psi^2)=A^2-B^2.
\]

Therefore

\[
 \boxed{
 T+S=2A^2\ge0,
 \qquad
 T-S=2B^2\ge0.}
\]

After integration against any positive measure,

\[
 \boxed{
 \int T\pm\int S\ge0.}
\]

Equivalently,

\[
 \left|\Re\int\psi^2\right|
 \le\int|\psi|^2.
\]

This is the first universal coupled positivity statement needed here. It does
not orient the spin-two component separately; it proves that the invariant
trace dominates it with exact sharp constant one.

## Theta specialization

For the two-copy source amplitude

\[
 \psi_z(u,v)
 =(u-v)\sqrt{f(u)f(v)}e^{iz(u+v)/2},
\]

earlier work gives

\[
 -\mathscr C_F(z)=\frac12\iint\psi_z(u,v)^2\,du\,dv
\]

and the invariant Gram trace

\[
 \mathcal T(z)=\frac12\iint|\psi_z(u,v)|^2\,du\,dv.
\]

On a real spectral slice where the real/imaginary quadratures are defined,

\[
 \boxed{
 \mathcal T(z)\pm\Re[-\mathscr C_F(z)]\ge0.}
\]

Thus if the completed Green correction `M` is exactly the appropriately
oriented curvature component with coefficient `+1` or `-1`, then

\[
 \mathcal N_{\rm comp}=\mathcal N+\mathcal M
\]

is a nonnegative quadrature square. A nondegeneracy theorem is still needed
unless the reciprocal sheet supplies the complementary quadrature.

## Sharpness and the normalization gate

For a general coefficient `lambda`,

\[
 T+\lambda S
 =(1+\lambda)A^2+(1-\lambda)B^2.
\]

This is nonnegative for every amplitude exactly when

\[
 \boxed{|\lambda|\le1.}
\]

Therefore the remaining source question is a normalization question:

\[
 \boxed{
 \text{What coefficient does exact Fourier--Tate sewing place in front of
 the reflection spin-two correction?}}
\]

The coefficient cannot be rescaled after the fact. It is fixed by the doubled
tail operator, endpoint orientation, Clark shear, and Mellin normalization.

## Relation to the earlier geometric ratio

The earlier de Branges quotient displays a factor `x/y` multiplying the
transverse jet. That coefficient is not bounded by one throughout its domain.
Hence positivity of that quotient does **not** follow from this universal
theorem. The new doubled boundary system must be audited to determine whether
its completed energy uses the unit trace--spin coupling or reproduces the
unbounded geometric factor.

This distinction prevents importing the desired normalization from a
different kernel coordinate.

## Falsifier

Expand the finite labelled doubled Green identity in the two-copy quadrature
basis. If its bulk has coefficients

\[
 \alpha_XA^2+\beta_XB^2,
\]

then positivity is source-certified only when `alpha_X,beta_X>=0` with the
correct cutoff-compatible limit. A negative coefficient at any labelled
cutoff falsifies universal coupled positivity for that construction.

Equivalently, if the normalized spin-two coefficient satisfies

\[
 |\lambda_X|>1,
\]

the smallest source packet supported entirely in the amplified quadrature is
the hostile witness.

## Present boundary

The quadrature-square theorem is exact and universal. Its identification with
the bulk `N+M` of packet 146 is not proved. The immediate calculation is to
track the coefficient of the reflection quotient through the exact doubled
tail normalization, without using a zero or desired sign.
