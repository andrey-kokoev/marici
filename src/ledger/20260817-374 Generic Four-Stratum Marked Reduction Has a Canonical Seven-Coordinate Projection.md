---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# Generic Four-Stratum Marked Reduction Has a Canonical Seven-Coordinate Projection

## Question

Entry 373 showed that residue packets cannot be fitted into a canonical
rank-twelve connection. The next hard-to-vary claim is

\[
\boxed{\text{the frozen four-stratum relative de Rham calculus fails to
reduce the generic derivatives of the twelve source masters.}}
\]

## Frozen engine

Use

\[
u=E_T,\qquad v=\ell_3,
\]

\[
l_1=b+1-u,
\qquad
l_2=a+\frac{v-u}{2}-1,
\]

and the source basis

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_1,\ldots,e_9).
\]

All forms are cleared to the common denominator

\[
l_1^2l_2^2K^{5/2}.
\]

Exact one-forms are admitted only on the four frozen strata

\[
l_1l_2K^{3/2},\qquad l_1K^{3/2},\qquad
l_2K^{3/2},\qquad K^{3/2}.
\]

The degree-eight primitive bound is the common-denominator encoding of both
the simple- and double-branch-pole reductions: multiplication by the quartic
\(K\) embeds the corresponding \(K^{-1/2}\) primitives without adding a
stratum.

## Exact finite-field result

Over

\[
\mathbf F_{2305843009213693951},
\]

the engine reduces all twelve masters in both \(u\)- and \(v\)-directions at
three generic fibers. Each polynomial identity has 132 monomial equations
and 372 unknowns. The coefficient rank is 117 in every tested reduction, and
every reconstructed cleared identity vanishes exactly.

The invariant-coordinate mask is constant across all 72 reductions:

\[
\boxed{
(\Omega_{111},\Omega_{101},\Omega_{110},e_6,e_7,e_8,e_9).
}
\]

The coordinates \(e_1,\ldots,e_5\) vary with the exact primitive. Thus the
engine produces a canonical seven-coordinate projection, not a preferred
twelve-coordinate splitting.

For derivatives of the absolute masters, all three marked quotient
coordinates vanish. Hence the exact sequence remains block triangular:

\[
\nabla\langle e_1,\ldots,e_9\rangle
\subseteq
\langle e_1,\ldots,e_9\rangle.
\]

## Verdict

The tested claim is falsified:

\[
\boxed{\text{the frozen four-stratum calculus reduces every tested generic
derivative exactly.}}
\]

No new denominator stratum or carrier cell is required. At the same time,
the calculation confirms Entry 373's warning: five displayed absolute
coordinates are representative-dependent, so a full raw matrix is not the
canonical output.

## Classification

| Datum | Classification |
|---|---|
| four denominator strata | frozen relative coefficient geometry |
| quotient coordinates | intrinsic marked quotient connection |
| \(e_6,e_7,e_8,e_9\) projection | invariant algebraic extension data |
| \(e_1,\ldots,e_5\) coordinates | exact-lift gauge |
| degree-eight primitive bound | common-denominator implementation choice |
| new carrier datum | none |

## Epistemic scope and next falsifier

This is a generic finite-field de Rham certificate. It does not yet reproduce
the Laurent systems at \(u=0\), prove a rational reconstruction over
\(\mathbf Q(u,v)\), or test the physical relative chain.

The next finite test is wall replication. Expand the same polynomial system
at \(u=0\), require the canonical seven-coordinate projection to reproduce
the fixed one-wall and two-wall coefficients, then pull that projection to
the radial charts. A failure of those fixed coordinates would falsify the
engine before any carrier conclusion is drawn.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_relative_reduction_engine.rs`;
- `research/benincasa/marked-relative-reduction-engine-certificate.json`;
- `research/benincasa/one-wall-total-energy-extension.json`;
- `research/benincasa/two-wall-second-rees-extension.json`;
- Entry 373.
