# The primitive-square-incidence packet is faithful for one split but not for multiple factors

## Two positive factor packets

Consider

\[
P_X(u)=\prod_{x\in X}(1+xu)
\]

for the positive rational multisets

\[
X=\{1,2,3\},
\qquad
Y=\{17/7,6/7,19/7\}.
\]

They have the same first two power sums:

\[
\sum_{x\in X}x=sum_{y\in Y}y=6,
\]

\[
\sum_{x\in X}x^2=sum_{y\in Y}y^2=14.
\]

Hence their connected logarithms agree through the square grade:

\[
[u]\log P_X=[u]\log P_Y=6,
\]

\[
[u^2]\log P_X=[u^2]\log P_Y=-7.
\]

Both packets also have the same numerator incidence and positive factor
orientation.

## The third grade separates them

Their third power sums differ:

\[
\sum_{x\in X}x^3=36,
\qquad
\sum_{y\in Y}y^3=\frac{11988}{343}.
\]

Therefore

\[
[u^3]\log P_X=12,
\qquad
[u^3]\log P_Y=\frac{3996}{343}.
\]

The polynomials have different roots because their positive factor multisets
are different. Applying reciprocal reflection to both produces two-chart
packets with identical reflected primitive and square data but still distinct
reciprocal divisors.

## Consequence for the boundary filtration

The coupled primitive-square-incidence packet is faithful for one reciprocal
quadratic because two power sums determine two roots. It is not faithful once
three or more factors are admitted. The connected `k>=3` tail is therefore the
next coherence rung that distinguishes global factorizations sharing the same
low boundary currents.

This gives the three-level filtration a precise division of labor:

```text
k=1      phase and primitive supply
k=2      radial split discriminant for one reciprocal pair
k>=3     coherence among several simultaneously present factors
```

The tail may be divisor-neutral when represented by a determinant unit, but
its connection is still necessary to identify which low-current packet is
being glued. Removing it turns distinct divisor-bearing source packets into
the same boundary presentation.

## Scope

This is a finite algebraic faithfulness obstruction, not an RH theorem. It
shows that the proposed global comparison cannot terminate at the first two
connected grades. A successful bridge must be natural across the full
connected pro-tower or prove an independent source law reducing the admissible
factorization rank.

## Durable verification

- Checker: `checkers/check_primitive_square_multifactor_collision.py`
- The checker verifies the exact first-two-grade collision, third-grade
  separation, and distinct factor multisets.
