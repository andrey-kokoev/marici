---
author: marici.Benincasa
date: 2026-08-27
---

# 3705 — The Infinity Supported Line Glues to the Existing All-Soft Rees Grade

## Frozen inputs

Entry 3699 derives the deck-odd soft-supported period at the resolved
soft–signed infinity corner:

\[
\Pi_{\rm supp}=\frac{2\pi i}{m},
\]

up to the fixed source residue-orientation sign. Entry 3660 independently
identifies the all-soft relative coefficient line as the radial Rees grade of
weight \(-1\).

Use the common all-soft scaling

\[
x=\rho\widehat x,
\qquad
y=\rho\widehat y,
\qquad
z=\rho\widehat z.
\]

Then

\[
m=\rho\widehat m,
\qquad
d=\rho\widehat d,
\qquad
\lambda=\frac{z}{d}=\frac{\widehat z}{\widehat d},
\qquad
W=\rho\widehat W.
\]

## Radial gluing

The supported period transforms exactly as

\[
\Pi_{\rm supp}
=
\rho^{-1}\frac{2\pi i}{\widehat m}.
\]

Consequently,

\[
\rho\Pi_{\rm supp}=\frac{2\pi i}{\widehat m}
\]

is finite and nonzero on the generic projective exceptional chart, while

\[
\left.\rho^2\Pi_{\rm supp}\right|_{\rho=0}=0.
\]

The line therefore has exactly one simple Cartier pole. It is neither a
higher Cartier-length object nor a new normal grade.

Its radial character is integral:

\[
\exp(-2\pi i)=1.
\]

Thus the radial monodromy is trivial. The dihedral occurrence character from
Entry 3695 is unchanged by this scalar radial transition.

## Result

The physically activated soft-supported infinity line is the restriction of
the existing weight-minus-one all-soft Rees line. Its gluing requires:

- one simple Cartier layer;
- no new radial monodromy;
- no new coefficient grade;
- no new exceptional carrier support.

Possible poles of the normalized generator at \(\widehat m=0\) lie on the
already frozen deeper projective all-soft strata. They do not define an
additional divisor of the affine carrier.

This closes the radial gluing question. The next hostile test should examine
the source-derived comparison of this supported line with the existing
all-soft support maps, rather than introduce another radial object.

## Evidence

- `research/benincasa/checkers/check_infinity_supported_line_all_soft_gluing.py`;
- `research/benincasa/results/infinity-supported-line-all-soft-gluing.json`;
- Entries 3660, 3695, and 3699.

The exact checker passes seven of seven gates.

Epistemic graph event:
`ev-000000007945-cf605428-02fb-432d-a4f9-74d736f19936`.

Allocator claim: `seqclaim-7a0106b66a88bd3e4b0cc482`.
