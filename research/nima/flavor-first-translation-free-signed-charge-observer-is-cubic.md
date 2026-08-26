# Flavor First Translation-Free Signed Charge Observer Is Cubic

## Result

On the affine family of three Flavor charges, the first centered polynomial
observer that is both translation-invariant and reflection-odd occurs at cubic
degree.

This explains why cubic structure repeatedly appears in the orientation
problem. Linear centered data vanish. Quadratic centered data measure spread
but cannot distinguish the two orientations of the charge line. Cubic centered
data supply the first signed shape coordinate.

## Centered moments

For a charge triple \(q\), let

\[
\bar q=\frac{q_1+q_2+q_3}{3}
\]

and define

\[
m_k(q)=\sum_{i=1}^3(q_i-\bar q)^k.
\]

Every \(m_k\) is invariant under common translation because centering removes
the charge origin.

Under reflection

\[
q\longmapsto -q+c(1,1,1),
\]

the centered deviations change sign. Therefore even moments are
reflection-even and odd moments are reflection-odd.

## Why degree three is first

The centered linear moment is identically zero:

\[
m_1(q)=0.
\]

The quadratic moment

\[
m_2(q)
\]

is positive spread and is unchanged by reflection. It belongs to the unsigned
hierarchy observer.

The cubic moment

\[
m_3(q)
\]

is translation-invariant and changes sign under reflection. It is the first
nontrivial centered signed scalar.

For \(q=(3,2,0)\), the exact values are

\[
m_2(q)=\frac{14}{3},
\qquad
m_3(q)=-\frac{20}{9}.
\]

The reflected charge line has the same \(m_2\) and opposite \(m_3\).

## Joint reconstruction

Once the hierarchy distance matrix has fixed the affine family, the mean
constrains the origin and the signed cubic constrains orientation.

The checker sets the target mean and cubic moment to those of \((3,2,0)\). Of
the two reflected affine sheets, exactly one satisfies both. This reconstruction
works over rational charges and does not rely on integer filtering.

## Relation to anomaly constraints

This theorem does not assert that the physical anomaly equation is \(m_3=0\)
or that it takes the target value above. It supplies a classification tool.

For every candidate anomaly or representation system, restrict its equations
to

\[
q(s,c)=s(3,2,0)+c(1,1,1)
\]

and inspect:

- dependence on \(c\), which measures origin sensitivity;
- parity under \(s\), which measures orientation sensitivity;
- dependence on charge-lattice assumptions;
- coupling to charges from other representations.

A purely even centered equation cannot select the reflected sheet. A signed
cubic contribution can, provided its coefficient and target are independently
derived.

## Two staged observers

The minimal affine reconstruction now has a natural division:

1. an origin observer, represented by the mean or another translation-sensitive
   source relation;
2. an orientation observer, represented by a translation-free odd cubic
   relation.

They reconcile over the same charge and messenger lineage. Neither is a second
copy of the hierarchy measurement.

## Connection to the earlier cubic carrier

There are now two distinct cubic objects:

- the alternating determinant of three typed vector ports;
- the centered cubic moment of one three-charge configuration.

Both are reflection-odd, but they live on different carriers and have different
gauge behavior. The Krylov determinant failed to descend without a phase
reference. The centered charge cubic already descends through common
translation, but still requires its physical source equation to be derived.

They must not be identified merely because both are cubic.

## Finite falsifier

Any proposed translation-free signed charge observer of degree at most two is
falsified immediately:

- degree one vanishes after centering;
- degree two is reflection-even.

The exact checker verifies the cubic sign flip and the unique reconstruction
from mean plus signed cubic.

## Status

The next Flavor audit should substitute the WP614 affine family into actual
candidate anomaly polynomials. The decisive question is whether their odd
centered component is nonzero and source-fixed. If all surviving equations are
reflection-even, they cannot select charge orientation.
