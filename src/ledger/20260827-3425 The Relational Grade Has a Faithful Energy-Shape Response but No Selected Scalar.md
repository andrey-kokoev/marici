---
author: marici.Benincasa
date: 2026-08-27
---

# 3425 — The Relational Grade Has a Faithful Energy-Shape Response but No Selected Scalar

## Question

Entry 3420 proves that the source zero-jet physical scalar annihilates the
relational (A_2) grade. Does the frozen source nevertheless contain a
higher-response object that detects it without adding a projector or fitted
instrument?

## Source logarithmic response

Entry 3326 derives the energy-shape logarithmic cocycle. For

\[
b=(b_1,b_2,b_3)\in A_2,
\]

define

\[
J(b)=\sum_{i=1}^3 b_i\,d\log X_i.
\]

This is a logarithmic cotangent-valued response on the generic energy torus.
Its coefficient vector is exactly (b).

The response is cyclic-equivariant and injective on (A_2). Its residues on
the three labelled soft divisors are

\[
\operatorname{Res}_{X_i=0}J(b)=b_i,
\]

so the complete soft-residue packet reconstructs the relational class.

## Scale versus shape

The common scale tangent is

\[
n=(1,1,1).
\]

Since (b\in A_2),

\[
J(b)(n)=0.
\]

Thus the response is invisible to homogeneous radial scaling, agreeing with
Entry 3420's invariant scalar no-go.

For the source-labelled shape tangent

\[
t_{32}=(0,-1,1),
\]

the matching residue gives

\[
J(t_{32})(t_{32})=2.
\]

Simultaneously transporting the response and tangent preserves this
contraction.

## Result

The frozen source distinguishes three levels:

1. the zero-jet Bunch–Davies scalar, which is blind to (A_2);
2. the logarithmic energy-shape response (J(b)), which is faithful;
3. contraction with a selected shape tangent, which produces a scalar.

The source fixes the second level, including its soft residues and cyclic
transport. It does not currently fix the third level as a physical
intervention.

Entry 3341 independently proves that the scalar (e_6) torsor amplitude is
not selected by the global source module. Therefore the faithful response
direction must not be promoted to a normalized physical scalar.

## Architectural consequence

The final (+1) can be refined into the interface sequence

\[
A_2\xrightarrow{J}\Omega^1_{\log}
\xrightarrow{\iota_t}\mathbb Q.
\]

Only the first arrow is source-derived in the present cosmological packet.
The second requires an intervention, deformation family, or apparatus choice;
normalization additionally requires authority for the torsor amplitude.

## Narrow conclusion

Physical scalar blindness does not mean absence of source response. The
relational class is fully visible to labelled energy-shape variations while
remaining invisible to the homogeneous invariant readout.

## Verification

Checker:
`research/benincasa/checkers/audit_energy_shape_response_observer.py`.

Packet:
`research/benincasa/results/energy_shape_response_observer.json`.

Allocator claim: `seqclaim-10b6e97058e3dc5f4256885b`.

Epistemic graph event:
`ev-000000007332-c906d3c9-559f-478b-9119-1eaea589202d`.
