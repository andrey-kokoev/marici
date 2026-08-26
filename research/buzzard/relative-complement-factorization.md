# Relative complement factorization packet

## Grothendieck source

This formalizes the finite theorem and hostile model in
`research/grothendieck/relative-complement-incidence-factorization.md`.

## Formal objects

- `admittedRestriction p U` is the coordinate incidence `P_in U`.
- `complementRestriction p U` is the independently defined omitted
  incidence `P_out U`.
- `transposeGram U = U^T U` uses the source packet's real coefficient model.
- `admitted_add_complement_gram` proves the orthogonal coordinate split.
- `relative_complement_factors_defect` derives
  `1 - C^T C = Q^T Q` when the full incidence is normalized.
- `normalizedGramScalar_complement` and the `C2` examples formalize the
  regular finite-fiber checker.
- `fixed_split_is_height_constant` records the hostile absence of analytic
  height dependence.

## Assumptions and coefficient types

The matrix theorem uses finite index types and an arbitrary commutative ring.
Transpose, rather than conjugate transpose, is intentional: this is the real
coefficient incidence theorem. The regular-fiber scalar examples use
rational coefficients.

## Missing interfaces and gates

The theorem does not say that the rectangular complement has a determinant.
A signed Xi candidate still requires a square rank-preserving oriented
complex or determinant-line torsion. Analytic height-dependent weights,
cutoff compatibility, and a physical relative-chain pushforward are absent.
The factorization therefore supplies neither an analytic Xi model nor RH.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
