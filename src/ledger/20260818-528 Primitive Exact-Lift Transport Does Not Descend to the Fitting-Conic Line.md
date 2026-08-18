---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# Primitive Transport Does Not Canonically Descend to the Fitting-Conic Line

## Question

For the canonical special-fiber line

\[
\mathcal L_{\rm fit}=G_{C_{\rm fit}}/G_{\rm lim},
\]

test whether the complete primitive equation

\[
A(u)r'(u)=-A'(u)r(u)
\]

canonically induces line transport. Two choices must be removed independently:

1. the primitive exact lift of a fixed twelve-master representative;
2. the affine solver section for \(r'\).

## Frozen computation

Along \(C_{\rm fit}\), the entries of \(A(u)\) have degree at most \(30\):
\(K\) has degree at most \(12\), and the largest common-denominator column
has degree at most \(30\). Compute \(A'\) by exact interpolation and require
agreement between derivative stencils of orders \(32\) and \(40\).

Use the normalized \(e_6\)-pivot representative of Entry 525, solve all
primitive exact coordinates, and retain the complete relation. Test exact-form
degrees \(8,10\) at \(u=3,5,7\) and at both nonsoft roots of

\[
8u^2-29u+8.
\]

At every point the derivative stencils agree and the primitive transport
equation is solvable.

## Invariance audit

For four independent exact-only null vectors, vary the primitive lift while
holding all twelve master coordinates fixed. The difference between the two
transport solutions satisfies

\[
\operatorname{rank}\langle G_{\rm lim},\Delta r'_{\rm master}\rangle=2.
\]

Thus primitive-lift ambiguity dies in the persistent plane.

For eight homogeneous null vectors with nonzero master projection, vary the
affine solver section. Uniformly,

\[
\operatorname{rank}\langle G_{\rm lim},\Delta r'_{\rm master}\rangle=3,
\]

while

\[
\operatorname{rank}\langle G_{C_{\rm fit}},\Delta r'_{\rm master}\rangle=3.
\]

Hence solver ambiguity vanishes modulo the full special gauge plane, but not
modulo the persistent two-plane.

The raw transported master vector itself is transverse to the full gauge
plane:

\[
operatorname{rank}\langle G_{C_{\rm fit}},r'_{\rm master}\rangle=4.
\]

## Verdict

\[
\boxed{
A r'=-A'r
\text{ defines ambient Grassmannian transport, but does not by itself
define a canonical connection on }\mathcal L_{\rm fit}.
}
\]

A choice of solver section changes the would-be line component. Selecting a
splitting after seeing this defect would be post hoc and is prohibited.

Therefore no diagonal pole divisor—and in particular no
\(8u^2-29u+8\) factor—may yet be assigned to \(\mathcal L_{\rm fit}\).

## Classification

| Datum | Classification |
|---|---|
| degree-certified \(A'\) | primitive coefficient geometry |
| primitive-lift ambiguity | killed by persistent gauge |
| solver-section ambiguity | killed only by full special gauge |
| ambient rank-four tangent direction | extension/Grassmannian transport datum |
| diagonal line connection | not canonically defined by this equation |
| new carrier datum | none |

## Epistemic boundary

This calculation rejects only the claim that differentiating the homogeneous
primitive relation canonically supplies a line connection. Independently,
Entry 527 uses ambient connection regularity to exclude
\(\mathcal L_{\rm fit}\) as the intrinsic \(\mathcal Q\)-sector of the
generic nine-master module. The remaining admissible possibility is
source-derived physical relative-chain data not present in that absolute
module.

## Next falsifier

Construct the source-defined inhomogeneous Gauss--Manin target along
\(C_{\rm fit}\), including the elliptic quotient, and test whether its
block decomposition canonically fixes the solver section. Then distinguish:

- a diagonal \(8u^2-29u+8\) pole;
- only an off-diagonal algebraic--elliptic factor;
- no quartic support.

No fitted splitting or carrier modification is admissible.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_tangency_support.rs`;
- `research/benincasa/gauge-fitting-conic-primitive-transport.json`;
- Entries 525--526.
