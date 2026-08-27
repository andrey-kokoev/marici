# RH Schatten-three filtration selects a regularized determinant

## Result

Grothendieck's three-level prime-current filtration selects an order-three regularized determinant rather than an ordinary Fredholm determinant.

For one relative eigenvalue (lambda), the order-three factor is

\[
(1+\lambda)\exp\left(-\lambda+\frac{\lambda^2}{2}\right).
\]

Its logarithm is

\[
\log(1+\lambda)-\lambda+\frac{\lambda^2}{2}
=
\frac{\lambda^3}{3}-\frac{\lambda^4}{4}+\cdots.
\]

The linear and quadratic cumulants are removed exactly. This matches the source filtration:

- primitive current: order one;
- prime-square current: order two;
- connected tail: order three and higher.

The first two currents are not discarded. They must remain as typed boundary data supplying the two counterterms removed from the bulk determinant.

## Correct completed object

The candidate comparison is therefore not just (det(I+K)). Its architecture is

\[
u_X
=
u_X^{(1)}u_X^{(2)}\det_3(I+K_X),
\]

where (K_X) is a Schatten-three relative operator and the first two factors are independently derived primitive and square boundary currents, coupled to seam and archimedean completion.

This is a source-typing statement, not yet a construction. It forbids absorbing the first two currents into an arbitrary scalar renormalization.

## Completion gates

The ordinary Fredholm compiler has an order-three analogue:

1. uniform Schatten-three mass on compact spectral sets;
2. uniform inverse control of (I+K_X);
3. local Schatten-three convergence;
4. independently derived and invertible first- and second-order boundary factors;
5. exact agreement with every finite Euler cutoff.

Both earlier hostile mechanisms survive.

A single eigenvalue may approach (-1) while the Schatten-three norm stays bounded. Conversely, repeating the safe eigenvalue (-1/2) makes the regularized factor

\[
\frac12\exp\left(\frac58\right)<1
\]

per mode, so unbounded Schatten-three mass collapses the product despite a uniform inverse gap.

## Categorical interpretation

The completion target is a determinant line with a two-step anomaly trivialization. The primitive and square currents form the boundary data required to lift a Schatten-three operator family into that line. Forgetting either current changes the comparison functor, even if the connected tail converges.

This gives a concrete meaning to the earlier claim that the (k=1) and (k=2) currents are boundary partners preventing escape at infinity: they are exactly the low-order cumulants absent from the regularized bulk determinant.

## Decisive next calculation

Construct the finite relative operator for one labelled prime addition and compare:

1. its full finite determinant;
2. its order-three regularized determinant;
3. the explicit primitive and square source currents;
4. the seam and archimedean boundary normalization.

The product of items 2 through 4 must reproduce item 1 before any infinite limit. A residual at one prime falsifies the proposed typing. Exact finite agreement would justify testing Schatten-three convergence and inverse control globally.
