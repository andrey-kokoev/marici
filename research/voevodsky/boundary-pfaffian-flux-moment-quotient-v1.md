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

## Constructive two-seam section

For two seam frames \((a^{-1},a)\) and \((b^{-1},b)\), define the moment determinant

\[
d=a^{-1}b-b^{-1}a.
\]

`TwoSeamFrame` requires explicit data \(d^{-1}\) and a proof \(d^{-1}d=1\). Under exactly this unit hypothesis, the module constructs flux coefficients for every endpoint pair and proves

\[
\operatorname{Observe}(\operatorname{Section}(q_-,q_+))
=(q_-,q_+).
\]

Thus the endpoint observation is constructively split-surjective whenever two labelled positions have invertible moment determinant. No field axiom or hidden division operation is used.

The module also defines additive negation of flux families. For any two admissible frames \(F,G\), it constructs the difference between their sections and proves

\[
\operatorname{Section}_F(q)-\operatorname{Section}_G(q)
\in\ker\operatorname{Observe}.
\]

Hence frame-dependent lifts represent the same endpoint class, with their exact discrepancy retained in the two-moment kernel.

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

The module proves split surjectivity under the explicit invertible two-seam determinant hypothesis. It does not yet compute the kernel rank for arbitrary finite families, which would require a developed finite free-module rank library.

## Verification

```text
agda --transliterate \
  -i research/voevodsky/agda \
  -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 \
  research/voevodsky/agda/BoundaryPfaffianFluxMomentQuotient.agda
```
