# Raw Metaplectic Creation Is the First-Order Lift of the Bounded Endpoint Shift

## Two normalizations of the same Cartan map

Let

\[
C_l:H_1\otimes H_l\longrightarrow H_{l+1}
\]

be the normalized Cartan coisometry. Let \(M_l\) be raw multiplication of
binary forms in Bargmann normalization. On output degree \(2l+2\), summing the
three normalized quadratic input channels gives

\[
M_lM_l^\dagger
=
(2l+1)(l+1)I_{H_{l+1}}.
\]

Therefore

\[
M_l=\sqrt{(2l+1)(l+1)}\,C_l.
\]

The bounded spin-weighted endpoint shift is

\[
J_l=c_lC_l,
\qquad
c_l^2=\frac{2(2l+1)}{l+1}.
\]

Taking the ratio gives

\[
M_l
=
\frac{l+1}{\sqrt2}J_l.
\]

## First-order factorization

The internal spectral operator satisfies

\[
D|_{H_l}=\frac{l+1}{2}I.
\]

Hence, on the finite-grade core,

\[
M=\sqrt2\,JD,
\qquad
M^\dagger=\sqrt2\,DJ^\dagger.
\]

Raw unbounded creation is exactly the first-order lift of the bounded endpoint
shift by the internally reconstructed grade operator. It is not an unrelated
completion chosen after the fact.

## Source-derived common domain

Let

\[
\mathscr H_D^\infty
=
\bigcap_{k\geq0}\operatorname{Dom}(D^k).
\]

Because \(J\) raises grade by one,

\[
DJ=J\left(D+\frac12\right).
\]

Similarly,

\[
DJ^\dagger=J^\dagger\left(D-\frac12\right)
\]

on positive grades. Therefore \(J\) and \(J^\dagger\) preserve the smooth
domain, and so do \(JD\) and \(DJ^\dagger\). The spectral graph norms of \(D\)
provide a source-derived common Fréchet domain for the ten first-order lifted
quadratic generators.

The finite-grade vectors are contained in this domain and remain analytic for
the linearly growing creation coefficients.

## Resolution of the completion question

The Bargmann weighting remains the unique grade-diagonal weighting compatible
with exact metaplectic adjoints. The new factorization shows that the existing
dagger-curvature packet selects that weighting constructively once the unitary
spinor/Cartan identification is retained.

Thus the domain and graph-norm portions of the previously missing
`BargmannMetaplecticLift` are not independent source choices. They descend from
\((J,J^\dagger,D)\).

## Remaining authority boundary

The factorization supplies closed-operator candidates and a common smooth
domain. It does not by itself authorize physical exponentiation. The remaining
declarations are:

- the real form to exponentiate;
- essential self-adjointness or skew-adjointness of the selected real
  combinations;
- the allowed one-parameter groups;
- their physical or observational interpretation;
- compatibility with any boundary or support restriction.

The algebraic and analytic-domain bridge is now derived. Executable control is
still a separate authority gate.

## Relation to finite local normal forms

This construction concerns the complete endpoint grade tower and its
first-order graph domain. It does not imply that a finite-dimensional local
\(\mathfrak{sp}_4\) jet controls an infinite-dimensional RH seam field. The
global no-finite-jet obstruction remains untouched.

## Evidence replay

The checker verifies the raw multiplication coisometry factor, the exact ratio
to the bounded endpoint shift, the first-order factorization, smooth-domain
invariance, linear graph growth, and analytic-vector ratios through grade two
hundred.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/endpoint_first_order_metaplectic_lift_checks.py
```

Machine-readable results are written to
`research/strominger/results/endpoint_first_order_metaplectic_lift_checks.json`.

