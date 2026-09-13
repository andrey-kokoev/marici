# Constructive labelled-flux moment quotient

## Module

`agda/BoundaryPfaffianFluxMomentQuotient.agda` formalizes the finite labelled-flux to endpoint-double map over an arbitrary commutative ring.

A seam entry retains:

```text
reciprocal position weight
direct position weight
flux coefficient
```

No order, positivity, division, or analytic exponential is assumed.

## Endpoint observation

For a finite flux family, the module constructs the two unnormalized moments

\[
q_- = \sum_i J_i y_i^{-1},
\qquad
q_+ = \sum_i J_i y_i.
\]

The analytic factor \(-1/2\) is intentionally omitted, so the construction remains valid without assuming that two is invertible.

## Symmetry

Reflection swaps direct and reciprocal position weights while preserving flux. Agda proves:

- reflection of flux families is involutive;
- the endpoint observation transforms by swapping \(q_-\) and \(q_+\).

Rescaling position weights by \((z^{-1},z)\) gives

\[
(q_-,q_+)\mapsto(z^{-1}q_-,zq_+),
\]

proved recursively for arbitrary finite families.

## Kernel stability

`MomentKernel` stores the two equations

\[
q_-=0,
\qquad q_+=0.
\]

The module constructs proofs that this kernel is preserved by both reflection and rescaling. Hence the exact information discarded by endpoint observation is a symmetry-stable typed relation.

This formally realizes the algebraic part of the finite sequence

```text
labelled flux family -> endpoint double
```

but does not yet prove finite-dimensional surjectivity or kernel rank, which require hypotheses on distinct/invertible position weights.

## Verification

```text
agda --transliterate \
  -i research/voevodsky/agda \
  -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 \
  research/voevodsky/agda/BoundaryPfaffianFluxMomentQuotient.agda
```
