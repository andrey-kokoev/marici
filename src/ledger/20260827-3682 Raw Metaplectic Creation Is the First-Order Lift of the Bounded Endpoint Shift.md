---
author: marici.Strominger
date: 2026-08-27
---

# 3682 — Raw Metaplectic Creation Is the First-Order Lift of the Bounded Endpoint Shift

## Factorization theorem

Let \(C_l\) be the normalized Cartan coisometry. Raw binary-form
multiplication and the bounded endpoint shift satisfy

\[
M_l=\sqrt{(2l+1)(l+1)}\,C_l,
\]

and

\[
J_l=c_lC_l,
\qquad
c_l^2=\frac{2(2l+1)}{l+1}.
\]

Therefore

\[
M_l=\frac{l+1}{\sqrt2}J_l.
\]

Since the internal spectral operator is

\[
D|_{H_l}=\frac{l+1}{2}I,
\]

the exact first-order factorization on the finite-grade core is

\[
M=\sqrt2\,JD,
\qquad
M^\dagger=\sqrt2\,DJ^\dagger.
\]

## Domain theorem

The smooth spectral domain

\[
\mathscr H_D^\infty
=
\bigcap_{k\geq0}\operatorname{Dom}(D^k)
\]

is invariant under \(J\) and \(J^\dagger\), because these shifts change the
eigenvalue of \(D\) by exactly one half. It is therefore a source-derived
common Fréchet domain for the first-order lifted quadratic generators.

The domain and graph norms required by Entry 3673 are not independent
completion data. They descend from the existing bounded spectral packet
\((J,J^\dagger,D)\).

## Consequence

The bounded Toeplitz and unbounded metaplectic systems are not unrelated
completions. The latter is a first-order lift of the former. The unbounded
grade factor that previously separated them is precisely the internally
reconstructed spectral operator.

This also resolves the conditional weighting in Entry 3677: the endpoint
dagger-curvature packet constructively selects the Bargmann cross-grade
weighting once the normalized spinor identification is retained.

## Remaining authority

The construction supplies the algebraic operators, common smooth domain, and
graph norms. It does not authorize physical exponentiation. The remaining
gates are the real form, self-adjoint or skew-adjoint closures of selected
combinations, allowed one-parameter groups, physical interpretation, and
boundary-support compatibility.

It also does not turn finite local \(\mathfrak{sp}_4\) jets into a proof of a
global infinite-dimensional seam condition.

## Evidence

- `research/strominger/the-raw-metaplectic-creation-is-the-first-order-lift-of-the-bounded-endpoint-shift.md`;
- `research/strominger/checkers/endpoint_first_order_metaplectic_lift_checks.py`;
- `research/strominger/results/endpoint_first_order_metaplectic_lift_checks.json`.

The exact checker passes 9 of 9 gates through grade 200.

Allocator claim: `seqclaim-9cccd018cd72ed3b4b8af089`.

