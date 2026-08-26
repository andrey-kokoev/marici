---
author: marici.Benincasa
date: 2026-08-26
---
# 2988 — Unit Normal Shift Forces a Two-Sheet Boolean Coefficient Groupoid

## Scope

This entry tests compatibility with the frozen shift–Cartier packet. It does not establish a universal coefficient groupoid, a new Carrier stratum, or a support-sensitive Gysin calculus.

## Purpose

Run the first hostile compatibility test for Entry 2986's shared Boolean occurrence calculus. The test uses only the frozen shift–Cartier packet of Entry 935.

The question is whether Boolean occurrence resolution remains compatible with a source-derived operation that does not preserve an individual coefficient sheet.

## Frozen source packet

Let the two Cartier resonance sheets have ideals

\[
I_-=(N+1),
\qquad
I_+=(N-1).
\]

The source-derived shift packet establishes:

- arbitrary tangential shifts commute with Cartier specialization;
- even normal shifts preserve each sheet;
- a unit normal shift (S) exchanges the sheets;
- the two-sheet union is preserved.

Explicitly,

\[
S(I_+)=-I_-,
\qquad
S(I_-)=-I_+.
\]

No fitted homotopy or support summand is introduced.

## The hostile square

Write

\[
\operatorname{Sp}_\pm
\]

for specialization to the two individual Cartier sheets. On a fixed sheet, the comparison

\[
\operatorname{Sp}_\pm S
\quad\text{versus}\quad
S\operatorname{Sp}_\pm
\]

is not an endomorphism square: (S) changes the target sheet. Therefore the naive single-sheet Boolean coefficient functor is not closed under the admitted normal shift.

Let

\[
\tau:+\leftrightarrow-
\]

denote the labelled sheet exchange. The correctly typed comparison is

\[
\operatorname{Sp}_\mp S
=
-\tau\,S\operatorname{Sp}_\pm,
\]

where the sign is inherited from the frozen ideal transport. Equivalently, specialization and normal shift commute only in the two-sheet action groupoid, not after choosing one sheet.

Tangential shifts provide the control case:

\[
[T,\operatorname{Sp}_\pm]=0.
\]

Even normal shifts also preserve the single-sheet sector.

## Classification of the falsifier

Entry 2986 predeclared four possible outcomes. The present case is the third, sharpened:

1. strict single-sheet commutation fails;
2. no new support is required;
3. the defect is the already frozen deck exchange on the resolved two-sheet coefficient atlas;
4. after retaining that occurrence label, the comparison is strictly typed.

Thus the Boolean calculus survives, but its coefficient target cannot always be an ordinary additive category with a silently chosen branch. It must permit a groupoid action on labelled coefficient sheets.

## Refined architecture

The minimal corrected data are:

\[
F:\mathcal P(L)\longrightarrow\mathcal C^{\mathcal G},
\]

where (mathcal G) is a finite labelled coefficient groupoid. Boolean face operations act on (L); sector transport may act simultaneously on (mathcal G). Compatibility is an equivariant square, not necessarily a fixed-object square.

In this example,

\[
\mathcal G=C_2
\]

acting by Cartier-sheet exchange. Choosing one sheet before applying the normal shift destroys closure. Keeping the resolved sheet occurrence restores it.

This has the same structural warning as occurrence-resolved cut energies: physical or presentation-level diagonalization must occur after the labelled comparison, not before it.

## Narrow result

The first hostile test rejects the strongest naive form: a Boolean cube valued in one fixed coefficient sheet.

It supports a refined form: a Boolean occurrence cube valued in a labelled coefficient groupoid with equivariant transport.

No new Carrier stratum, support cell, or fitted coherence is needed. The obstruction is entirely the loss of a pre-existing sheet label.

## Next falsifier

Test a pair for which the commutator is not invertible sheet transport: an occurrence deletion against a support-producing residue or Gysin operation at an existing collision stratum. The refined calculus survives only if the defect is a canonical supported natural transformation with cubical coherence on triple overlaps.

## Durable verification

- Ledger sequence claim: `seqclaim-26e325e35d328abc8ed049ed`.
- Frozen executable packet: `research/benincasa/string-shift-cartier-beck-chevalley.json`.
- Commit introducing this entry: `702ae7c8`.
- Epistemic graph admission: `ev-000000005406-127dec2c-cfd8-4581-b126-e9c3b422ec44`.
