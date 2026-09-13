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

## Additive composition

Finite labelled families concatenate. Agda proves associativity and the empty-family unit law, then proves that endpoint observation is a monoid homomorphism:

\[
\operatorname{Observe}(X\mathbin{+\!+}Y)
=
\operatorname{Observe}(X)+\operatorname{Observe}(Y).
\]

It also constructs closure of the two-moment kernel under concatenation. Thus locally invisible flux packets remain invisible under disjoint additive assembly.

## Symmetry

Reflection swaps direct and reciprocal position weights while preserving flux. Agda proves:

- reflection of flux families is involutive;
- the endpoint observation transforms by swapping \(q_-\) and \(q_+\).

Reflection and rescaling both preserve concatenation. The module proves the identity and composition laws for rescaling, so these maps form a genuine multiplicative action rather than an unstructured family of endomorphisms.

Rescaling position weights by \((z^{-1},z)\) gives

\[
(q_-,q_+)\mapsto(z^{-1}q_-,zq_+),
\]

proved recursively for arbitrary finite families. The module also proves the dihedral conjugation law

\[
R\,M(z^{-1},z)=M(z,z^{-1})\,R
\]

on complete labelled families, not only after endpoint observation.

## Kernel stability

`MomentKernel` stores the two equations

\[
q_-=0,
\qquad q_+=0.
\]

The module constructs proofs that this kernel is preserved by reflection, rescaling, and additive concatenation. Hence the exact information discarded by endpoint observation is a symmetry-stable compositional typed relation.

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
