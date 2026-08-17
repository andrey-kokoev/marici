---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# Residue Packets Do Not Determine the Bivariate Marked Connection

## Question

Entries 300, 371, and 372 determine the generic total-energy nilpotent, the
\(e_6\) bridge, and the radial behavior of the absolute nine-master module.
Before fitting the three marked rows, test the hard-to-vary claim

\[
\boxed{\text{the existing residue and Rees packets uniquely determine the
bivariate rank-twelve connection.}}
\]

## Frozen rank data

For the one-wall class, the degree-five exact system has 188 unknown
coefficient jets and rank 93. Its affine nullity is therefore 95. More
importantly, the audited residue projection has variation rank five: only
the quotient coefficient and the \(e_4,e_7,e_8,e_9\) coordinates are fixed,
while \(e_1,e_2,e_3,e_5,e_6\) vary with the exact lift.

For the two-wall top class, the degree-five three-order system has

\[
540-194=346
\]

free certificate parameters. The six-order degree-five calculation used in
Entry 299 has

\[
1080-416=664
\]

free parameters.

These are not missing carrier cells. They are the expected freedom in
choosing exact relative primitives and representatives. The source lifts fix
the classes, but the surviving scalar residue coordinates do not encode the
full bivariate reduction.

## Solver shape forced by the source geometry

The four frozen denominator strata are

\[
l_1l_2\sqrt K,\qquad l_1\sqrt K,\qquad
l_2\sqrt K,\qquad \sqrt K.
\]

At polynomial degree four there are 15 monomials in \((a,b)\). Each stratum
has two primitive one-form components, so one reduction layer has

\[
12+4\cdot2\cdot15=132
\]

unknowns: twelve master coefficients and 120 exact-field coefficients. This
reproduces the reported 264 unknowns for two Laurent layers and 396 for three.
Thus the missing computation is mechanically specified; it is not permission
to choose a splitting.

## Verdict

The tested claim is falsified:

\[
\boxed{\text{the existing packets constrain but do not uniquely reconstruct
the bivariate marked connection.}}
\]

A connection assembled by selecting convenient free parameters and imposing
flatness afterward would be a prohibited post hoc splitting. The admissible
next step is to reconstruct the source-normalized four-stratum relative de
Rham quotient and carry its exact-lift gauge explicitly.

## Classification

| Datum | Classification |
|---|---|
| fixed residue coordinates | intrinsic marked extension data |
| varying residue coordinates | exact-lift gauge |
| large affine nullities | primitive-certificate freedom |
| four denominator strata | frozen relative coefficient geometry |
| missing object | reduction engine, not carrier stratum |
| new carrier datum | none |

## Next falsifier

Implement the four-stratum reduction over a large finite field in the frozen
basis

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_1,\ldots,e_9).
\]

First require it to reproduce the reported equation/unknown/rank data and all
fixed one-/two-wall coordinates. Then compute generic \(u\)- and \(v\)-jets,
transport the quotient modulo exact-lift gauge, and test the radial Rees
lattice. Failure of the frozen exact calculus to reproduce those source
certificates is the first implementation falsifier; only after it passes may
the full rank-twelve exceptional support be classified.

## Evidence

- `research/benincasa/one-wall-total-energy-extension.json`;
- `research/benincasa/two-wall-second-rees-extension.json`;
- `research/benincasa/marked-top-column-e1-q-falsifier.json`;
- `research/benincasa/marici-gm/src/bin/marked_connection_reconstruction_gate.rs`;
- `research/benincasa/marked-connection-reconstruction-gate-certificate.json`.
