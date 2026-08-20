---
title: "The First-Rees Physical Pairing Is Cyclically Invariant"
date: 2026-08-20
entry: 1135
status: established-supported-cyclic
sector: cosmology
---

# 1135 — The First-Rees Physical Pairing Is Cyclically Invariant

Sequence claim: `seqclaim-f217dee18ff4bbbc66431a99`.

## Typed transport

The transported object is Entry 1134's supported pairing, not the retracted
target-to-target arrow of Entry 1128.

For the cyclic residue-chart change of Entry 764, the \(e_6\) covector has
physical-energy homogeneity \(-2\). The dual physical relative boundary has
homogeneity \(+2\). Hence on every chart edge

\[
z^{-2}z^{2}=1.
\]

Entry 366 independently fixes every cyclic Leray orientation, Jacobian, and
multiplicity to \(+1\). The threefold chart transport is the identity.

Therefore the source-normalized pairing is

\[
\boxed{
\left(\frac14,\frac14,\frac14\right)
}
\]

on the three site-soft occurrences. Equivalently, it is the invariant
functional

\[
\frac14(1,1,1):\mathbb Q[C_3]\longrightarrow\mathbb Q.
\]

## Consequence

The physical first-Rees \(e_6\) class descends through cyclic occurrence
transport with no sign, scale, sheet, or overlap obstruction. This is a
genuine cyclic statement because both coefficient and relative-chain
variances are retained and their homogeneities cancel.

The result remains rational. It does not choose a saturated integral target
lattice or reinterpret the value \(1/4\) as an index.

## Classification and next falsifier

This is sector-specific coefficient/relative-period data assembled by the
existing occurrence and Gysin calculus. No new carrier datum appears.

The next finite test is reflection: the transposition exchanging the two
node sheets reverses both the anti-invariant coefficient covector and the
physical difference boundary. Their pairing is predicted to remain \(+1/4\).
Failure would obstruct extension from \(C_3\) to the full dihedral occurrence
group.

Evidence:

- `research/benincasa/checkers/rank12_e6_supported_pairing_cyclic.py`;
- `research/benincasa/results/rank12-e6-supported-pairing-cyclic.json`;
- Entries 366, 764, and 1131--1134.
