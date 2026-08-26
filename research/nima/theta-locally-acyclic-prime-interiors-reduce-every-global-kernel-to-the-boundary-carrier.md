# Locally acyclic prime interiors reduce every global kernel to the boundary carrier

## Finite assembled system

Let \(X\) be a finite set of prime-valuation chains. For each \(p\in X\),
let \(D_p(s)\) be its source-derived interior block. Across the open critical
strip, the reciprocal prime-chain calculation gives

\[
D_p(s)^{-1}
\]

for every local block.

Let \(\mathcal E\) be the common boundary carrier. It must retain the endpoint,
gamma, primitive, square, and seam types required by the source construction.
Write the assembled operator as

\[
\mathcal D_X(s)
=
\begin{pmatrix}
D_X(s)&C_X(s)\\
R_X(s)&A_X(s)
\end{pmatrix},
\]

where

\[
D_X=\bigoplus_{p\in X}D_p.
\]

The maps \(C_X\) and \(R_X\) are the incidence maps between the boundary
carrier and the labelled prime interiors. The block \(A_X\) contains only
independently declared boundary dynamics.

## Exact boundary reduction

Since \(D_X\) is invertible, eliminate all prime interiors. The effective
boundary operator is

\[
M_X(s)
=
A_X(s)-R_X(s)D_X(s)^{-1}C_X(s).
\]

The block determinant identity gives

\[
\det\mathcal D_X(s)
=
\det D_X(s)\det M_X(s).
\]

For the unbordered nilpotent prime shifts,

\[
\det D_X(s)=1.
\]

Therefore

\[
\det\mathcal D_X(s)=\det M_X(s).
\]

Every finite assembled zero is already a zero of the boundary Schur
complement.

## Kernel localization

If

\[
\mathcal D_X
\begin{pmatrix}
x\\y
\end{pmatrix}
=0,
\]

then the interior equation forces

\[
x=-D_X^{-1}C_Xy.
\]

The remaining equation is

\[
M_Xy=0.
\]

Thus projection onto the boundary carrier gives an isomorphism

\[
\ker\mathcal D_X
\cong
\ker M_X.
\]

There is no independent prime-interior zero state in the critical strip.
Every global kernel is a boundary state whose prime components are uniquely
reconstructed by the local Green operators.

This is the exact operator form of the earlier statement that a zero is
global destructive interference rather than a local arithmetic puncture.

## Boundary dimension matters

If the boundary carrier has dimension one, \(M_X\) is a scalar. The entire
operator construction then compresses back to a scalar nonvanishing problem.
It improves provenance but supplies no new orientation unless the source also
forces a sign, half-plane, monotonicity, or index law for \(M_X\).

If the boundary carrier has dimension \(r>1\), a scalar zero is a failure of
invertibility of an \(r\)-dimensional boundary interaction. The extra
coordinates matter only if their typing and incidence are source-derived.
Adding fitted coordinates merely hides the scalar section in a larger
matrix.

The smallest credible completed carrier is therefore not selected by a
desired matrix size. It is selected by the independent endpoint, gamma,
primitive, square, seam, and archimedean ports that survive source
elimination.

## Cumulant interpretation

The bordered prime-chain determinant forces

\[
-\log(1-p^{-s})
=
p^{-s}
+\frac12p^{-2s}
+\sum_{k\ge3}\frac{p^{-ks}}{k}.
\]

These are the primitive, square, and order-three tail cumulants of the same
source block. They are not optional scalar counterterms.

After summing over primes:

- the primitive cumulant requires boundary continuation;
- the square cumulant reaches its threshold at the critical seam;
- the order-three tail is normally convergent near the seam.

Consequently the first two cumulants must enter \(A_X\), \(C_X\), or \(R_X\)
as typed reconstructive boundary data. Removing them from the state system
while retaining only their scalar subtraction destroys the source-local
elimination square.

## Completion gate

At finite \(X\), kernel localization is exact. Passing to all primes requires
more than pointwise convergence of \(\det M_X\). One must prove:

1. the local inverses remain compatible with packet inclusions;
2. the incidence maps converge in their declared graph topology;
3. \(M_X\) converges locally uniformly or in a stronger operator topology;
4. no boundary state escapes through unbounded reconstructed interior norm;
5. the limiting kernel correspondence remains exact.

Failure of the fifth condition is precisely completion-created cohomology.

## Finite falsifier

For any proposed common-boundary model, compute

\[
F_X(s)
=
\det\mathcal D_X(s)
-
\det D_X(s)\det M_X(s).
\]

A nonzero \(F_X\) is an algebraic implementation failure. More importantly,
type each entry of \(A_X,C_X,R_X\). If an entry depends on the completed scalar
section, a zero location, or a fitted determinant coefficient, the model is a
backward scalar lift.

Finally compute the boundary null vector \(y\) and reconstruct

\[
x=-D_X^{-1}C_Xy.
\]

If a claimed global kernel has \(y=0\), it contradicts local acyclicity. If
\(y\ne0\), the exact support of \(y\) identifies the boundary port carrying
the unresolved mechanism.

## Disposition

The arithmetic interior is now structurally understood:

- labelled prime chains generate the Euler factors;
- their determinant cumulants generate the three Tate currents;
- reciprocal local interiors are acyclic throughout the critical strip;
- every finite global kernel is carried by the common boundary Schur
  complement.

The RH problem has therefore moved into one sharply typed object: the
completed boundary interaction \(M(s)\) and the stability of its kernel
correspondence under infinite restricted-product completion.
