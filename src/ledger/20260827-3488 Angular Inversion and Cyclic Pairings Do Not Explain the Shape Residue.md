---
author: marici.Benincasa
date: 2026-08-27
status: numerical falsification of three proposed positivity mechanisms
---

# 3488 — Angular, Inversion, and Cyclic Pairings Do Not Explain the Shape Residue

## Question

Can the positive quadratic relative-period pilot be reduced to a simple
source-derived positivity theorem before undertaking exact relative IBP?

## Angular averaging

Let \(A(r)\) be the spherical average of the analytic second-shape jet at
fixed loop radius. A 321-point logarithmic radial scan with 200,000 angular
points per radius finds a negative band

\[
0.71\lesssim r\lesssim1.19,
\]

with minimum approximately \(-0.00419\) at \(r=1\). Thus angular averaging
does not make the insertion positive.

## Radial inversion

The measure-compatible inversion pair is

\[
P(r)=r^2A(r)+r^{-4}A(1/r),
\qquad 0<r\le1.
\]

It remains negative near \(r=1\), with observed minimum approximately
\(-0.00831\). Radial inversion therefore does not pair the negative band with
a sufficient positive partner.

## Cyclic loop routings

Average the analytic jet over the three cyclic momentum routings before
integration. At eight million points the fraction with positive local jet
rises from about \(76.5\%\) to \(85.0\%\), but the signed integrals become

\[
I''_+\approx0.2568,
\qquad
I''_-\approx-0.2564.
\]

The small positive total remains a cancellation residue. Cyclic occurrence
completion does not convert it into pointwise positivity.

## Result

Three natural explanatory mechanisms are falsified:

1. positivity after angular completion;
2. positivity after radial inversion pairing;
3. positivity after cyclic routing completion.

The surviving response depends on the complete signed relative pairing. This
is compatible with Aspect's marked-germ calculus but is not explained by a
simple local mate.

## Next attack

Construct the analytic second-shape insertion in the retained marked-wall
relative complex and reduce it by exact relative IBP. The target is its scalar
coefficient on the physical relative class, not an absolute elliptic
projection. Numerical positivity should no longer guide basis selection.

## Evidence

`research/benincasa/marici-gm/src/bin/physical_relative_shape_jet_qmc.rs`.

Allocator claim: `seqclaim-8941b7408c7c027e98eed2a5`.

