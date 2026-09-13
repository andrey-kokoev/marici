# Green Gram determinant lines have local transition factors

## Ordered determinant formula

Let

\[
x_1<\cdots<x_n,
\qquad
\rho_i=e^{-(x_{i+1}-x_i)}.
\]

For the Green Gram matrix

\[
K_{ij}=e^{-|x_i-x_j|},
\]

successive Markov/Cholesky elimination gives

\[
\det K_n=
\prod_{i=1}^{n-1}(1-\rho_i^2).
\]

Every factor is positive for distinct points, recovering strict positive definiteness in ordered coordinates.

The formula supplies a canonical positive generator for each finite determinant line once the context order is fixed.

## Interior refinement

Insert \(x\) between adjacent old points \(a<b\), and set

\[
\alpha=e^{-(x-a)},
\qquad
\beta=e^{-(b-x)}.
\]

The old gap factor is

\[
1-\alpha^2\beta^2.
\]

After refinement it is replaced by

\[
(1-\alpha^2)(1-\beta^2).
\]

Therefore the determinant transition is

\[
\frac{\det K_{S\cup\{x\}}}{\det K_S}
=
\frac{(1-\alpha^2)(1-\beta^2)}
     {1-\alpha^2\beta^2}.
\]

This is exactly the squared norm of the Green-orthogonal innovation \(r_{x\mid S}\).

## Coherence

For a chain of refinements, determinant ratios multiply telescopically:

\[
\frac{\det K_U}{\det K_S}
=
\frac{\det K_U}{\det K_T}
\frac{\det K_T}{\det K_S}.
\]

Hence the determinant-line transitions form a strict multiplicative cocycle over the finite-context poset. Refinement order cannot create a scalar anomaly.

## Collision boundary

As the inserted point approaches either neighbor, \(\alpha\to1\) or \(\beta\to1\), and the transition factor tends to zero. Thus determinant-line transport is continuous on the configuration space of distinct ordered points but becomes noninvertible on collision strata.

The correct completion is consequently stratified:

```text
distinct-point stratum: positive invertible determinant transition
collision stratum:      innovation line collapses and rank drops
```

A determinant line can extend continuously across collision only as a possibly vanishing section, not as a nowhere-zero trivialization.

## Relation to the pro realization

The finite Green system now carries compatible data

```text
state inclusion
orthogonal projection
innovation line
positive determinant transition
```

at every refinement. This closes the scalar determinant-line part of the graded/pro construction. Pfaffian square roots require additional skew data and are not implied by this positive determinant formula.

## Verification

```text
python research/coherence/check_green_gram_determinant_transitions.py
```

The checker verifies the determinant product through nine points and 50 exact interior insertion identities.

Artifacts:

- `check_green_gram_determinant_transitions.py`
- `green-gram-determinant-transitions.v1.json`
