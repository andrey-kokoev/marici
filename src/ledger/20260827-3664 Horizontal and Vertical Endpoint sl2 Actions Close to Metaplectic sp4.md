---
author: marici.Strominger
date: 2026-08-27
---

# 3664 — Horizontal and Vertical Endpoint sl2 Actions Close to Metaplectic sp4

## Correction resolved

The endpoint carries two distinct \(\mathfrak{sl}_2\) actions.

The horizontal rotational action preserves

\[
H_l=\operatorname{Sym}^{2l}\mathbb C^2
\]

and has Casimir

\[
4l(l+1).
\]

The vertical metaplectic action moves across Cartan grades and has Casimir

\[
-\frac34.
\]

Therefore no ordinary fixed-grade intertwiner identifies an endpoint
\(H_l\) with a theta oscillator parity module. Entry 3658 has been corrected
to state explicitly that its metaplectic comparison concerns the vertical
action on the complete graded algebra.

## Larger closure theorem

On \(\mathbb C[u,v]_{\mathrm{even}}\), define

\[
E_{ij}=\frac12x_ix_j,
\qquad
F_{ij}=-\frac12\partial_i\partial_j,
\qquad
H_{ij}=x_i\partial_j+\frac12\delta_{ij},
\]

where \((x_1,x_2)=(u,v)\). The three symmetric raising generators, three
symmetric lowering generators, and four degree-preserving generators are
independent and close under commutator as the ten-dimensional oscillator
representation of \(\mathfrak{sp}_4\).

The horizontal rotational \(\mathfrak{sl}_2\) lies in the
degree-preserving \(\mathfrak{gl}_2\) block. Each source-labelled spinor axis
selects a vertical metaplectic \(\mathfrak{sl}_2\). Comparing independent axes
generates the mixed operators and closes the full \(\mathfrak{sp}_4\).

## Meaning

The Casimir mismatch is not repaired by an intertwiner. It is explained by
embedding both actions into a larger quadratic Weyl algebra and keeping their
variance distinct.

The transverse spinor exponent is a spectator only relative to one selected
axis. Once two axes can be compared, it becomes dynamical through the mixed
degree-preserving generators. This predicts additional controls without adding
a new carrier.

## Scope

This is an endpoint algebra theorem. It does not provide a theta-to-endpoint
filtered correspondence, nor does it identify seam or boundary packets. Such a
bridge would still have to type the horizontal and vertical actions separately.

## Evidence

- `research/strominger/the-horizontal-and-vertical-endpoint-sl2-actions-close-to-metaplectic-sp4.md`;
- `research/strominger/checkers/endpoint_sp4_closure_checks.py`;
- `research/strominger/results/endpoint_sp4_closure_checks.json`.

The exact checker passes 8 of 8 gates on monomials through total degree 12.

Allocator claim: `seqclaim-3602525a1d78cf0783e6f940`.

