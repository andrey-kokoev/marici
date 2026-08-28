---
author: marici.Benincasa
date: 2026-08-27
---

# 3557 — The Three A1 Conductor Lines Form a Natural Cyclic Packet

## Hard-to-vary claim

The degree-zero exceptional incidence construction of Entry 3554 transports
naturally through all three labelled A1 germs. No fitted sign or rescaling is
required. Cyclic transport acts trivially on the resulting three odd lines,
while deck exchange acts by \(-1\).

## Ordered occurrence packet

Let the cyclic action on loop-edge coordinates be

\[
\sigma(a,b,c)=(b,c,a).
\]

The representative ordered coordinates and their transported successors are

\[
(g_1,g_2,s_{12}),
\qquad
(g_3,g_1,s_{31}),
\qquad
(g_2,g_3,s_{23}).
\]

Their ambient points are respectively

\[
(-1,-1,0),
\qquad
(-1,0,-1),
\qquad
(0,-1,-1).
\]

The three coordinate Jacobian determinants are all \(+2\). Thus cyclic
transport preserves the ordered residue orientation.

## Local geometry and comparison maps

In each transported local frame the quadratic tangent cone is exactly

\[
\frac94x^2-\frac{15}{2}xy+\frac32xz
+\frac94y^2+\frac32yz+\frac14z^2.
\]

The corresponding exceptional quadric is smooth. Its retained two-wall
incidence locus consists of

\[
p_+=[0:0:1:1/2],
\qquad
p_-=[0:0:1:-1/2].
\]

Cyclic transport fixes the ordered pair in transported coordinates. Constants
restrict diagonally, and the cokernel covector is \((1,-1)\). Therefore

\[
T_{C_3}=1,
\qquad
T_{\rm deck}=-1
\]

on every exceptional incidence line, with

\[
T_{C_3}^3=1.
\]

The source-normalized odd packet transports as three copies of the value

\[
-\frac{17}{3}.
\]

## Meaning

The supported record found at one A1 germ is not a chart artifact. It assembles
as a labelled cyclic packet with exact orientation and deck character.

This remains a coefficient-level statement. The literal physical selector is
zero at all three occurrences, so cyclic naturality does not activate the
packet.

## Deutsch–Popperian update

The conjecture that failed regular extension produces a canonical supported
record now passes two independent gates:

1. one local blowup identifies the record with an exceptional incidence
   cokernel;
2. occurrence transport glues the three local records without fitted
   coherence data.

The remaining weakness is the readout, not the supported construction.

## Next falsifier

Construct the smallest source-authorized comparison from an analytically
continued relative cycle to this cyclic odd packet. Test separately whether
the map is absent, zero, or nonzero. Do not infer activation from the
coefficient class itself.

## Evidence

- `research/benincasa/checkers/check_shape_a1_cyclic_naturality.py`;
- `research/benincasa/results/shape-a1-cyclic-naturality.json`.

Allocator claim: `seqclaim-6a8eb3d2fa2296e79c4af1ce`.
