---
author: marici.Strominger
date: 2026-08-27
---

# 3658 — The Even-Veronese Endpoint Carries the Metaplectic sl2 with Spectator Multiplicity

## Result

Under the spinor presentation

\[
\mathcal C
\cong
\mathbb C[u,v]_{\mathrm{even}},
\]

choose one spinor coordinate \(u\) and define

\[
E=\frac{u^2}{2},
\qquad
F=-\frac{\partial_u^2}{2},
\qquad
H=u\partial_u+\frac12.
\]

These operators preserve the even-Veronese algebra and shift Cartan grade by
zero or one as appropriate. They obey

\[
[H,E]=2E,
\qquad
[H,F]=-2F,
\qquad
[E,F]=H.
\]

Their fixed Casimir is

\[
H^2+2H+4FE=-\frac34I.
\]

Thus the Strominger endpoint realizes the same metaplectic
\(\mathfrak{sl}_2\) algebra and the same quantum Casimir as Grothendieck's theta
control system. The agreement is at operator level, not merely at the level of
the classical Veronese relation.

## Typed difference

The exponent of \(v\) is preserved. Consequently the Cartan endpoint is a
direct sum of metaplectic parity sectors carrying spectator multiplicity. It
is not a literal identification with one theta oscillator module.

The invariant conic also does not select a preferred spinor coordinate.
Choosing \(u\) requires a source-labelled axis; other choices are conjugate by
spinor symmetry.

Raw polynomial multiplication and the normalized endpoint shift differ by
nonzero grade scalars. Entry 3639 proves that those scalars are algebraically
gauge on the forward chain. The dagger normalization remains a separate norm
comparison and is not silently identified with the Bargmann convention.

## Horizontal-versus-vertical correction

The metaplectic algebra above acts vertically across Cartan grades. It must not
be confused with the rotational \(\mathfrak{sl}_2\) acting horizontally inside
a fixed irreducible space

\[
H_l=\operatorname{Sym}^{2l}\mathbb C^2.
\]

The horizontal Casimir is \(4l(l+1)\), while the vertical metaplectic Casimir
is \(-3/4\). Therefore there is no ordinary fixed-grade intertwiner from
\(H_l\) to a theta oscillator parity module. The comparison in this entry is
between theta's oscillator action and the vertical action on the complete
graded endpoint algebra, not between theta and one fixed endpoint grade.

## Consequence

The classical relation and quantum correction now line up across the two
systems:

- the quadratic symbols lie on the even-Veronese conic;
- quantization replaces its zero relation by the central value \(-3/4\);
- source differences survive as multiplicity, axis selection, and boundary
  data.

## Scope

This is an exact representation-theoretic comparison. It does not identify
theta seam currents, completion data, or physical carriers with celestial
endpoint data.

## Evidence

- `research/strominger/the-even-veronese-endpoint-carries-the-metaplectic-sl2-with-spectator-multiplicity.md`;
- `research/strominger/checkers/endpoint_metaplectic_sl2_checks.py`;
- `research/strominger/results/endpoint_metaplectic_sl2_checks.json`.

The exact checker passes 8 of 8 gates through total degree 80.

Allocator claim: `seqclaim-d9c65f05f603205ece4348fd`.
