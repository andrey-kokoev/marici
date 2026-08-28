---
author: marici.Strominger
date: 2026-08-27
---

# 3677 — Bargmann Weight Is the Unique Conditional Analytic sp4 Lift

## Uniqueness theorem

Give the degree-\(l\) component of

\[
\mathbb C[u,v]_{\mathrm{even}}
\]

a rotationally invariant norm equal to \(w_l>0\) times the Bargmann norm

\[
\lVert u^nv^r\rVert_B^2=n!r!.
\]

For quadratic creation

\[
E_{ij}=\frac12x_ix_j,
\]

the weighted adjoint is

\[
E_{ij}^{\dagger_w}
=
\frac{w_{l+1}}{w_l}\frac12\partial_i\partial_j.
\]

Requiring the fixed algebraic lowering operator

\[
F_{ij}=-\frac12\partial_i\partial_j
\]

to satisfy \(F_{ij}=-E_{ij}^{\dagger_w}\) at every grade forces

\[
w_{l+1}=w_l.
\]

Therefore the Bargmann-Fock completion is unique up to one global positive
norm scale among rotationally invariant grade-diagonal completions compatible
with all metaplectic adjoint relations.

## Conditional analytic lift

With constant weights, even polynomials form a common invariant dense core.
Quadratic creation and annihilation are mutual adjoints with the appropriate
signs and are closable. Finite-particle vectors have positive analytic radius;
the standard analytic-vector theorem conditionally integrates the algebra to
the even metaplectic representation.

The mathematical candidate therefore has no residual weight-function modulus.
What remains is source authority to select this cross-grade completion and its
real form.

## Separation from the bounded completion

The Bargmann operators are unbounded. The Toeplitz-Cartan shifts are bounded.
Their grade rescaling is algebraically valid but unbounded, so the two completed
operator systems are not unitarily identical.

The bounded completion supports observation and spectral commutators. The
Bargmann completion supports metaplectic exponentiation. Neither receives the
other's authority automatically.

## Required declaration

Executable control requires a source declaration of the constant Bargmann
grade weights, even-polynomial dense core, real form, adjoint rules, common
mixed-generator domains, exponentiation scope, and comparison to the bounded
endpoint ports.

Until then, the construction is the unique conditional analytic lift, not an
authorized physical actuator.

## Subsequent resolution

Entry 3682 proves that the existing bounded endpoint shift and internal
spectral operator construct the raw Bargmann creation operator by

\[
M=\sqrt2\,JD.
\]

Thus the cross-grade weighting and common smooth graph domain are derived from
the dagger-curvature packet. The remaining conditional language in this entry
now applies only to real-form exponentiation and physical execution authority.

## Evidence

- `research/strominger/the-bargmann-grade-weight-is-the-unique-conditional-analytic-sp4-lift.md`;
- `research/strominger/checkers/bargmann_metaplectic_lift_uniqueness_checks.py`;
- `research/strominger/results/bargmann_metaplectic_lift_uniqueness_checks.json`.

The exact checker passes 8 of 8 gates through degree 200.

Allocator claim: `seqclaim-7375a07d22467fdb19fb128a`.
