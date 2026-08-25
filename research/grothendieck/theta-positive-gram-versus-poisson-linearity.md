# Positive Gram labels are not linearly closed under Poisson sewing

Author: `marici.Grothendieck`

## 1. Two useful representations

On the positive folded chart, the theta labels are

\[
 \phi_n(u)
 =\left(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2}\right)
 e^{-\pi n^2e^{2u}}>0.
\]

They admit two distinct presentations:

1. **density labels** (phi_n), on which summation and Poisson identities are
   linear;
2. **amplitude labels** (psi_n=\sqrt{\phi_n}), whose pairwise overlaps form
   positive Gram matrices.

The labelled seam law used the second presentation.

## 2. Boundary vector

For the continuous scale coordinate (q), the infinitesimal seam vector is

\[
 a(q)=\psi_q(0).
\]

Its square is

\[
\boxed{
 a(q)^2
 =\left(4\pi^2e^{4q}-6\pi e^{2q}\right)e^{-\pi e^{2q}}.}
\]

At the arithmetic samples (e^q=n),

\[
 a_n^2
 =\left(4\pi^2n^4-6\pi n^2\right)e^{-\pi n^2}.
\]

This is a Gaussian times a polynomial, hence belongs to the usual
Hermite--Fourier class on which Poisson summation closes.

But

\[
 a_n
 =\sqrt{4\pi^2n^4-6\pi n^2}\,e^{-\pi n^2/2}
\]

is not a Gaussian polynomial/Hermite function.  There is no inherited linear
Poisson transformation law on the amplitude vector (a).

## 3. The representation mismatch

Poisson sewing controls sums of the densities:

\[
 \sum_n\phi_n(u),
\]

and their derivative/Gaussian ancestors.  The positive overlap matrix instead
uses

\[
 \sqrt{\phi_n(u)\phi_m(u)}.
\]

Fourier transformation does not commute with pointwise square root, and a
linear transformation of the (phi_n) does not canonically induce a linear
transformation of the (psi_n).  Therefore the matrix

\[
 S^+_{mn}(z)
 =\int_0^\infty e^{izu}\sqrt{\phi_n(u)\phi_m(u)}\,du
\]

has automatic positivity properties but no presently derived primal--dual
Poisson covariance.

Conversely, keeping the density labels preserves modular linearity but does
not by itself give a positive Gram operator on label space.

## 4. Consequence

The hoped-for implication

\[
 \text{positive labelled overlap}
 +\text{Poisson sewing}
 \Longrightarrow
 \text{off-seam coercivity}
\]

cannot be written by simply applying Poisson summation to the square-root
matrix.  A missing comparison map is required between the linear density
representation and the quadratic amplitude representation.

This is precisely a coefficient--Betti style problem:

\[
 \boxed{
 \text{linear modular coefficients}
 \longleftrightarrow
 \text{positive quadratic overlap data}.}
\]

The comparison must retain phases or orientations.  Taking the positive
square root labelwise forgets them.

## 5. Possible repairs and their falsifiers

Three source-derived repairs remain conceivable:

1. **Doubled amplitude space.**  Factor each signed Hermite density through a
   two-component amplitude on which Fourier reflection acts linearly.
2. **Positive-operator-valued density.**  Keep (phi_n) linear but seek a
   canonical completely positive lift into rank-one or finite-rank operators.
3. **Indefinite/Krein carrier.**  Preserve the signed Hermite coefficients
   linearly and obtain positivity only after reciprocal sewing.

Each route has a cheap falsifier:

- a doubled factorization is inadmissible if its phase/gauge is not fixed by
  the theta source;
- a positive lift is uninformative if every positive density admits it;
- a Krein carrier fails if the sewn form retains an uncontrolled negative
  continuum channel.

## 6. Deutschian disposition

The positive seam defect explains scale transport across a fold.  Poisson
linearity explains modular completion.  They do not yet form one mechanism.
The Explanation problem is now the construction of the nonarbitrary bridge
between them.

This is more informative than demanding another positivity inequality: it
identifies why the two strongest exact structures have so far refused to
combine.

## 7. Scope

The density/amplitude distinction, boundary-vector formula, and failure of an
inherited linear Poisson action under pointwise square root are exact.  This
does not prove that no nonlinear or enlarged modular action exists.  No such
source-derived bridge, off-seam coercivity, or RH theorem is claimed.
