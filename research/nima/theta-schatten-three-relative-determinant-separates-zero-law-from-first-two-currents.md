# Schatten-three relative determinant separates zero law from first two currents

## Exact regularization

Let (K) belong to the Schatten class (mathcal S_3). The third regularized
Fredholm determinant is

\[
\det_3(I+K)
=
\det\left((I+K)e^{-K+K^2/2}\right).
\]

The operator inside the ordinary Fredholm determinant differs from the
identity by a trace-class operator.

At finite cutoff,

\[
\det(I+K)
=
\det_3(I+K)
\exp\left(
\operatorname{Tr}K
-\frac12\operatorname{Tr}K^2
\right).
\]

Thus third-order regularization removes exactly the linear and quadratic trace
currents.

## Zero law

The exponential regularization factor never vanishes. Therefore

\[
\det_3(I+K)=0
\]

if and only if

\[
I+K
\]

is not invertible.

The first two trace currents affect the determinant frame and exact finite
normalization. They do not create, remove, or move determinant zeros.

If the sector operator is accretive, then (I+K) is invertible in the open
sector. Hence the regularized determinant is zero-free there independently of
the divergent behavior of the first two currents.

## Connection formula

For an analytic family (K(z)), the regularized logarithmic derivative is

\[
\frac{d}{dz}\log\det_3(I+K)
=
\operatorname{Tr}
\left(
(I+K)^{-1}K'
-K'
+\frac12(KK'+K'K)
\right),
\]

whenever the displayed combination is trace class.

Using cyclicity on the trace-class combination gives

\[
\frac{d}{dz}\log\det_3(I+K)
=
\operatorname{Tr}
\left(
\big((I+K)^{-1}-I+K\big)K'
\right).
\]

The subtracted first and second currents must be restored separately if the
goal is exact finite Euler reconstruction rather than only the zero divisor.

## Arithmetic interpretation

The existing prime filtration has the same formal shape:

- the primitive current is not Hilbert-controlled;
- the square current is Hilbert but not trace class;
- the connected tail beginning at the third level is trace class.

This makes a third regularized determinant the first source-compatible scalar
determinant candidate. The correspondence is still conditional: one must
derive an actual Schatten-three sector operator whose finite-cutoff trace
counterterms equal the typed primitive and square currents.

The relative completed determinant would have the form

\[
D_{\mathrm{rel}}(z)
=
e^{J_1(z)+J_2(z)+J_{\partial}(z)}
\det_3(I+K(z)),
\]

where (J_1), (J_2), and (J_{\partial}) retain the primitive, square, and
other boundary-frame currents.

The exponential factor is zero-free. All zero confinement comes from
invertibility of (I+K) and stability of that invertibility under completion.

## Multiplicative anomaly boundary

Regularized determinants need not be naively multiplicative. A factorization
can acquire an explicit exponential anomaly built from finite trace
polynomials. Such an anomaly may be essential for exact sewing, but it remains
nonvanishing and therefore cannot supply zero exclusion by itself.

Any claimed sewing-dependent scalar anomaly must be typed as one of:

- a regularized multiplicative frame factor;
- a kernel or cokernel index;
- a domain or endpoint contribution;
- a genuine failure of invertibility.

Only the last two categories can change the zero divisor, and an exponential
frame factor never can.

## Finite reconstruction gate

For every cutoff (N), compute

\[
\mathcal E_N
=
\log\det(I+K_N)
-
\log\det_3(I+K_N)
-
\operatorname{Tr}K_N
+
\frac12\operatorname{Tr}K_N^2.
\]

Exact finite-dimensional algebra requires

\[
\mathcal E_N=0
\]

up to the declared logarithm branch. A nonzero residual disproves the proposed
countercurrent typing.

The next gates are:

1. derive (K_N) from labelled theta/Tate incidence;
2. prove the sector accretivity of (K_N);
3. identify its linear trace with the primitive current;
4. identify its quadratic trace with the square current;
5. retain seam, endpoint, and continuation factors;
6. prove local uniform convergence of the relative determinant on compact
   subsets of each open sector;
7. freeze a nonzero source basepoint.

## Decisive conclusion

The Schatten-three filtration does not itself orient the completed kernel. It
does something more precise: it separates the zero-bearing invertibility law
from the first two divergent frame currents.

This is the correct determinant architecture if, and only if, the source
constructs the required accretive (mathcal S_3) operator and the finite Euler
countercurrent identities exactly.
