# The global prime action is a product system, not an endpoint intertwiner

## Finite correspondences exist exactly

At prime cutoff \(X\), let \(m_X\) be the finite Haar product measure and let

\[
d\mu_X=L_X\,dm_X
\]

be the arithmetic Poisson product measure. The half-density map

\[
J_X:L^2(\mu_X)\longrightarrow L^2(m_X),
\qquad
J_Xf=L_X^{1/2}f
\]

is unitary because

\[
\|J_Xf\|_{L^2(m_X)}^2
=\int |f|^2L_X\,dm_X
=\|f\|_{L^2(\mu_X)}^2.
\]

For nested cutoffs \(X\subset Y\), the likelihood factors over the new prime coordinates. The corresponding half-density maps compose by tensor product. All finite action cells therefore exist and are source-normalized.

## Why the endpoint arrow disappears

The image of the arithmetic vacuum has Haar overlap

\[
\langle 1,L_X^{1/2}\rangle_{m_X}
=\int L_X^{1/2}\,dm_X.
\]

This is the finite Hellinger affinity. The local logarithmic deficits add, and their leading term is proportional to \(1/p\). Hence the global affinity tends to zero. The finite vacuum images do not converge to a nonzero vector in the Haar vacuum sector.

Kakutani disjointness is therefore not a failure of finite composition. It is failure of the terminal endpoint arrow in the chosen vacuum representation.

## Correct global action object

The surviving object is the directed family

\[
\{J_{X,Y}:X\subset Y\}
\]

with its exact tensor-composition cells. This is a product system or pro-correspondence of finite representation changes. It joins the sectors pathwise without identifying their disjoint endpoints by one bounded intertwiner.

The infinite action cell should therefore be typed as a diagram-level constructor:

- objects are finite cutoff GNS sectors;
- arrows are half-density correspondences for added prime packets;
- composition is tensoring independent increments;
- the primitive centered log-likelihood is the fluctuating additive coordinate;
- the square current is its deterministic normalization or quadratic-variation coordinate;
- the terminal arithmetic and Haar representations are distinct boundary objects of the diagram.

## Martingale coordinates

For one prime Poisson density \(P_{r_p}\), write

\[
\ell_p=\log P_{r_p}-\mathbb E_m\log P_{r_p}.
\]

Then

\[
\log L_X
=\sum_{p\le X}\ell_p
+\sum_{p\le X}\mathbb E_m\log P_{r_p}.
\]

The centered primitive coordinate has divergent quadratic variation of order \(\sum_p1/p\). The square coordinate supplies the deterministic compensator at the same order. Exponentiating after erasing either coordinate destroys the finite normalized correspondence.

This explains why the two grades must remain coupled before completion.

## Move to the observation cell

Once action is represented by the product system, the next lattice cell is not a single trace on one Hilbert space. A compatible scalar state on cylinder observables already exists, but it erases the accumulated logarithmic current. The required wave observer is an affine family \(O_X\) with typed increments satisfying

\[
O_Y=O_X+\Delta O_{X,Y},
\qquad
\Delta O_{X,Z}=\Delta O_{X,Y}+\Delta O_{Y,Z}.
\]

The equalities hold on the declared cylinder domain after the correspondence transports are inserted. Primitive fluctuation and square compensator are separate coordinates of \(\Delta O\). Strict invariance is the correct law only for a stable scalar cylinder expectation, not for the additive wave current.

Only such a natural observer can descend to a distributional adelic functional. A scalar limit formed after exponentiating \(L_X\) is already too late because \(L_X\to0\) almost surely and is not uniformly integrable.

## Finite falsifiers

Reject a proposed action if:

1. a finite half-density map fails the isometry identity;
2. two packet additions fail tensor composition;
3. the square compensator is deleted before exponentiation;
4. a terminal bounded intertwiner is asserted despite disjoint GNS representations;
5. the proposed observer is not natural across finite correspondence arrows;
6. the construction depends only on the scalar likelihood limit.

## Decisive outcome

The infinite carrier and action cells can coexist without a common endpoint representation:

- carrier splitting is Kakutani disjointness;
- action is the finite-correspondence product system;
- the missing next cell is a natural distributional observer on that system.

This advances the lattice rather than repairing the impossible tensor-product endpoint.
