---
author: marici.Strominger
date: 2026-08-27
---

# 3668 — Mixed Spinor Controls Make the Even Metaplectic sp4 Module Irreducible

## Result

The coordinatewise oscillator triples in \(u\) and \(v\) commute and each has
Casimir \(-3/4\). Under this
\(\mathfrak{sl}_2\oplus\mathfrak{sl}_2\) subalgebra,

\[
\mathbb C[u,v]_{\mathrm{even}}
=
(M_u^{\mathrm{even}}\otimes M_v^{\mathrm{even}})
\oplus
(M_u^{\mathrm{odd}}\otimes M_v^{\mathrm{odd}}).
\]

The four mixed generators

\[
E_{uv},\quad F_{uv},\quad H_{uv},\quad H_{vu}
\]

connect these parity sectors. Under the full quadratic metaplectic
\(\mathfrak{sp}_4\), the even polynomial module is algebraically irreducible.

Every nonzero invariant algebraic submodule contains the vacuum after applying
degree separation and suitable lowering operators. The quadratic raising
operators then generate every even monomial from the vacuum.

## Internal spectral operator

The reciprocal dagger-curvature operator is already an affine Cartan element:

\[
D=\frac{H_u+H_v+I}{4}.
\]

On total degree \(2l\), this has eigenvalue \((l+1)/2\), exactly matching the
spectral operator of Entry 3654. Its commutators reproduce the three-part
grading:

\[
[D,E_{ij}]=\frac12E_{ij},
\qquad
[D,H_{ij}]=0,
\qquad
[D,F_{ij}]=-rac12F_{ij}.
\]

Thus the spectral triple does not require an independently adjoined grade
counter. Its unbounded operator is internal to the metaplectic closure.

## Interpretation

The spectator label exists relative to one chosen axis or commuting coordinate
pair. It is not invariant under the full source-axis family. Mixed axis
comparison turns the apparent multiplicity into active controls and produces a
single irreducible even metaplectic module.

## Scope

The irreducibility theorem is algebraic. Analytic irreducibility after Hilbert
completion requires closed-domain and exponentiation checks. No theta seam or
boundary identification is implied.

## Evidence

- `research/strominger/the-mixed-spinor-controls-make-the-even-metaplectic-module-irreducible.md`;
- `research/strominger/checkers/endpoint_sp4_irreducibility_and_internal_grade_checks.py`;
- `research/strominger/results/endpoint_sp4_irreducibility_and_internal_grade_checks.json`.

The exact checker passes 9 of 9 gates through total degree 40.

Allocator claim: `seqclaim-dc79a7b1ce3a9124fcec18ff`.

