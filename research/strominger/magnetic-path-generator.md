# Magnetic path weights are Euler-transport characters

Let

\[
C_{g,a}(x)=\sum_{j=0}^g
\binom gj(-1)^{g-j}a^{\overline{g-j}}(4-a)^{\overline j}x^j.
\]

The complete magnetic path column is the coefficient vector of

\[
\boxed{
B_{g,a,m}(x)=
\left[x(1+x)\frac{d}{dx}+m+(m-g)x\right]C_{g,a}(x).
}
\]

Indeed, the coefficient of `x^j` is

\[
(m+j)c_j+(m+j-1-g)c_{j-1},
\]

including both endpoint conventions.  This identifies the apparently ad hoc
integer matrix entries as weights of the Euler operator `x d/dx`, the two
boundary multiplications, and the grade correction `-gx`.

The source polynomial is a terminating Gauss polynomial:

\[
C_{g,a}(x)=(-1)^g a^{\overline g}
{}_2F_1(-g,4-a;1-a-g;-x).
\]

Its adjacent coefficients obey the first-order contiguous law

\[
(j+1)(a+g-j-1)c_{j+1}
+(g-j)(4-a+j)c_j=0.
\]

Thus the path matrix is not a generic band matrix.  It is a coefficient atlas
for one contiguous hypergeometric family followed by one first-order transport
operator.  This is the source-level reason its large determinants repeatedly
collapse to rising-factorial characters.

In particular, the endpoint weights are immediately

\[
[x^0]B=m(-1)^g a^{\overline g},
\qquad
[x^{g+1}]B=m(4-a)^{\overline g}.
\]

The remaining unbounded determinant proof should therefore be sought as a
contiguous-relation elimination identity under `a -> a+2`.  The finite memory
is the bandwidth of that contiguous transport, while the scalar determinant
character is its exterior character.

The checker verifies the differential identity on 5,586 exact columns, the
hypergeometric presentation on 15 formal-parameter polynomials, 9,300 contiguous
coefficient identities, and 14,250 endpoint pairs.
