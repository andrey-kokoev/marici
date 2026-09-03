# Singular-evaluation closability obstruction

## Question

What can prevent the coupled gamma-remainder-plus-prime form from closing on the leading archimedean GNS space?

## Claim boundary

An uncompensated point evaluation at a point carrying no reference mass is nonclosable. An explicit polynomial sequence demonstrates the defect. This does not establish that the regularized prime form contains such an evaluation; its distributional order remains to be classified.

## Closability criterion

Let \(q\) be a nonnegative quadratic form on a dense polynomial core in a Hilbert space. Closability requires:

if

\[
p_n\to0
\]

in the reference norm and

\[
q(p_n-p_m)\to0,
\]

then

\[
q(p_n)\to0.
\]

## Endpoint evaluation fixture

Take the reference space

\[
L^2([0,1],dy)
\]

and the point-evaluation form

\[
q_1(p)=|p(1)|^2.
\]

Set

\[
p_n(y)=y^n.
\]

Then

\[
\lVert p_n\rVert_{L^2}^2
=
\int_0^1y^{2n}\,dy
=
\frac1{2n+1}
\longrightarrow0.
\]

But

\[
q_1(p_n)=1
\]

for every \(n\), while

\[
q_1(p_n-p_m)=0
\]

for every \(n,m\). Therefore \(q_1\) is not closable.

This is stronger than unboundedness: no closed extension agrees with the evaluation form on the polynomial core.

## Outside-support evaluation

For \(z_E<0\) or \(|z_E|>1\), polynomial sequences can be chosen whose reference norm vanishes while evaluation remains fixed or grows. In the endpoint case

\[
z_E=1-e^{h/4}<0.
\]

When \(|z_E|>1\), monomials already produce exponential evaluation growth. When \(|z_E|\leq1\) but \(z_E\) lies outside reference support, polynomial approximation supplies analogous separating sequences.

Thus endpoint subtraction is required not only to restore Hausdorff support but also to avoid a singular nonclosable evaluation in the reference GNS topology.

## Measure-order criterion

If the coupled perturbation is an order-zero signed measure \(\nu\), a multiplication-form realization in \(L^2(\mu_0)\) requires

\[
\nu\ll\mu_0.
\]

Writing

\[
d\nu=w\,d\mu_0,
\]

the lower form bound is exactly

\[
w\geq-1
\]

almost everywhere. No upper bound on \(w\) is necessary.

If \(\nu\) has a singular component, the multiplication-form realization fails unless that component is separately represented by a closable form on a stronger domain.

## Prime-sector gate

The source-regularized prime functional must therefore be classified before applying a density argument:

1. If it is an order-zero measure in the Bernstein coordinate, prove absolute continuity with respect to \(\mu_0\) and bound its density below.
2. If it is a higher-order distribution or nonlocal translation form, construct its domain and prove closability directly.
3. If an uncompensated singular evaluation remains, the leading-measure GNS strategy fails in that topology.

The gamma remainder must remain coupled to the prime functional because cancellation may lower the distributional order. Classifying the prime sector separately and then assuming recombination is invalid.

## Disposition

Closability is a substantive source gate, not a formal consequence of compatible finite matrices. The explicit sequence \(p_n(y)=y^n\) is the hostile test for any proposed atomic or point-evaluation component. The next task is to determine the distributional order and singular support of the coupled source functional in the Bernstein coordinate.

## Verification

- `research/voevodsky/checkers/check_singular_evaluation_closability_obstruction.py`
- `research/voevodsky/results/singular_evaluation_closability_obstruction.json`
