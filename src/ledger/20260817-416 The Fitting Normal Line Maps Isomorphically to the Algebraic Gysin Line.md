---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# The Fitting Normal Line Maps Isomorphically to the Algebraic Gysin Line

## Record

Status: gauge-invariant finite-field line-map census on both components of
\(D=E^4-X_1^2X_2^2\). This continues Entries 390, 400, 410, and 415.

## Hard-to-vary claim

The projective vector agreement of Entry 410 and the simple Fitting
multiplicity of Entry 390 might fail to define the same local line map. The
test must combine them at each fiber without using the noncanonical RREF
scalar \(\lambda_\pm\).

## Frozen construction

At a generic neighbor of each divisor point, freeze a maximal-rank square
minor of the exact-lift presentation. On specializing to \(D_\pm\), compute:

1. its right kernel line;
2. its left cokernel line;
3. their pairing with the transverse first derivative of the frozen minor;
4. the projective \((e_7,e_8,e_9)\) tail of the additional \(e_6\)-pivot
   relation.

The first three data define the first Fitting normal map. The fourth is
compared with the source vector \(v_{\rm alg}\). No scalar normalization of
the special-fiber line is retained.

## Result

At exact-form degree 8, for every \(u=3,\ldots,60\) on both
\[
D_-=E^2-X_1X_2=0,qquad D_+=E^2+X_1X_2=0,
\]
all 116 tested fibers satisfy simultaneously:

- the special kernel projects projectively to \(v_{\rm alg}\);
- the kernel--cokernel transverse pairing is nonzero;
- the specialized maximal minor has rank defect exactly one.

Hence
\[
\boxed{
N^{\rm Fit}_{D_\pm}
\longrightarrow
\langle e_6,v_{\rm alg}\rangle/\langle e_6\rangle
\text{ is nonzero, hence an isomorphism of tested one-dimensional fibers.}
}
\]

This is the gauge-invariant comparison requested by Entry 415.

## Interpretation

The exact-lift rank defect is not merely supported on the same divisor as the
algebraic quotient. Its first normal class lands in the same source-defined
rank-one Gysin quotient. The scalar complexity seen in Entry 415 is therefore
a choice-of-generator artifact.

The supported architecture is now
\[
\text{unchanged carrier}
+
\text{relative coefficient presentation}
+
\text{algebraic Gysin quotient controlling its simple Fitting normal line}.
\]

No new cosmological primitive is indicated. The result supplies no support
for \(\mathcal Q\).

## Epistemic boundary

A nonzero map of tested fibers is not a global scheme-theoretic line-bundle
isomorphism. The calculation uses one large finite field and degree 8, though
the component, vector, and normal tests were separately stable at degree 10.
It excludes the intersection locus \(D_+\cap D_-\), where total-energy and
soft support meet.

## Classification

- carrier: unchanged energy/Cut carrier;
- coefficient support: \(D=0\);
- normal line: first Fitting normal of the exact-lift presentation;
- target line: algebraic Gysin quotient represented by \(v_{\rm alg}\);
- generic tested map: isomorphism;
- new carrier datum: none.

## Next falsifier

Approach
\[
D_+\cap D_- = \{E=0,\ X_1X_2=0\}.
\]
Saturate by the known soft factors and compute whether the normal-line map
extends through the total-energy/soft intersection or acquires a supported
kernel or cokernel. Any defect must be classified as existing soft support,
nearby-cycle data, or genuinely new coefficient support before carrier
language is considered.

## Evidence

- `research/benincasa/exact-lift-algebraic-normal-line-map.json`
- `research/benincasa/marici-gm/src/bin/marked_tangency_support.rs`
