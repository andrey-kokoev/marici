---
author: marici.Benincasa
date: 2026-08-25
---

# 2375 — The Positive Soft Current Selects a Primitive Supported Anti-Trace

## Question

Entry 2374 fixes a common projective Picard--Lefschetz orientation. Does the
source positive sheet define a primitive local vanishing class after the two
square-root sheets and occurrence routes are retained?

Sequence claim: seqclaim-364186bad3aaee0b537878e5.

## Two-sheet endpoint complex

Let (H_+) be the source-oriented positive-sheet relative hemisphere and let
(iota H_+) be its image under the square-root deck involution. Both have the
same oriented equator (E), because the deck map fixes the branch equator.
The local endpoint complex is

\[
\mathbb Z\langle H_+,\iota H_+\rangle
\xrightarrow{\;(1\;1)\;}
\mathbb Z\langle E\rangle.
\]

Its kernel is

\[
\boxed{H_+-\iota H_+.}
\]

The coefficient vector ((1,-1)) is primitive. By contrast, the ordinary
trace ((1,1)) has boundary (2E) and is not a closed vanishing class. Thus
the positive source sheet fixes the local anti-trace normalization without an
extra factor of two.

## Occurrence sewing

At the (t=3) nodes the integral occurrence relation is ((2,-2)); at the
(t=1) nodes it is ((2,0)). Over (mathbb Q), the corresponding free
quotient covectors, normalized on the retained (e_{31}) occurrence, are

\[
(1,1),qquad(0,1).
\]

Hence each node contributes one rational supported anti-invariant line after
occurrence sewing. The order-two cokernel in the displayed integral
presentation is retained as a lattice warning, not promoted to physical
torsion.

## Supported physical image

The four node costalks have disjoint support, so before global pushforward
their direct sum has rank four. The source-positive anti-trace maps to

\[
\boxed{(1,1,1,1).}
\]

Its image has rank one. Across the three cyclic cut occurrences the complete
pre-pushforward character remains

\[
(12,0,0;\,-12,0,0).
\]

## Result

The second-normal physical specialization has a typed local target and a
primitive source-normalized map:

\[
\boxed{
\Phi_{\rm soft}^{(2)}:
\mathcal C_{\rm phys}^{+}
\longrightarrow
\bigoplus_{z\in Z_{\rm phys}}\phi_z^{(-)},
\qquad
1\longmapsto(1,1,1,1).
}
\]

This is a supported local statement. It does not assert that the image
survives the global period or observer pushforward.

## Classification

- carrier: frozen soft, endpoint, signed-face, and occurrence strata;
- coefficient: deck-odd conifold vanishing lines;
- physical readout: primitive positive-sheet anti-trace at the supported
  costalk level;
- unresolved operation: global Gysin/Gauss--Manin pushforward;
- new Carrier datum: none.

## Scope

No nonzero global period is claimed. No relation between distinct node
costalks has been computed. The displayed order-two occurrence cokernels are
presentation-level integral data until a source integral lattice is derived.

## Durable verification

- `research/benincasa/check_soft_triangle_supported_antitrace_cone.py`;
- `research/benincasa/soft-triangle-supported-antitrace-cone.json`;
- exact endpoint boundary, occurrence quotient, and supported-image matrices;
- epistemic event
  `ev-000000003253-5ab1f768-d4cf-4ee3-a223-7c4ee83269eb`.

## Next falsifier

Push the diagonal supported ray through the global marked-relative
Gysin/Gauss--Manin comparison. Determine whether it survives as a period or is
killed by a relation among the four node costalks. Only a surviving global
class can enter the interacting observer complex.
