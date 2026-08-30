# Cross-degree symmetry obstruction (WP263)

## Question

Can an ordinary linear source symmetry supply the relative coefficient needed
by WP262's minimal interior-mixing selector?

In the underlying Gram fields, the commutator norm invariant \(I_4\) is
homogeneous of field degree four. Its square \(I_4^2\) is homogeneous of degree
eight. The candidate action has the schematic form

\[
V=-a I_4+b I_4^2.
\]

## Degree theorem

An invertible linear transformation of the underlying fields preserves total
polynomial degree. It therefore acts separately on the degree-four and
degree-eight operator spaces. It may forbid operators or relate multiple
operators within one degree, but it cannot exchange \(I_4\) with \(I_4^2\) or
fix their relative coefficient.

The smallest exact witness is uniform field scaling. For arbitrary nonzero
scale \(s\),

\[
I_4\mapsto s^4 I_4,
\qquad
I_4^2\mapsto s^8 I_4^2.
\]

No nonzero constant linear identification is compatible with both weights.
The checker verifies the same obstruction for a generic two-variable linear
substitution by exact polynomial degree support and coefficient comparison.

## Consequence

Weak-basis symmetry alone cannot close WP262's coefficient-authority gate. A
dimensionful spurion or normalization scale, nonlinear symmetry, radiative
matching relation, or other microscopic constructor must explicitly join the
two degree sectors. Introducing such an object is legitimate, but it is new
source structure whose value and instrument must be typed independently of
the desired mixing angle.

This theorem does not exclude nonlinear or duality transformations,
supersymmetric relations with additional multiplets, or microscopic matching.
It shows why an ordinary linear flavor symmetry is insufficient.

Run `uv run --with sympy python
research/flavor/checkers/wp263_cross_degree_symmetry_obstruction.py` for the
exact degree, scaling-weight, coefficient, and hostile-exchange checks.
