---
author: marici.Benincasa
date: 2026-08-27
---

# 3398 — Instrument Evaluation Is a Mate Pairing, Not an Inverse Transport

## Correction

Entry 3394 writes the instrument transformation as (d\mapsto dP^{-1}) for
invertible cyclic transport (P). That formula is correct for comparing two
charts along an automorphism, but it is not the primitive definition of
contravariance.

For an arbitrary Carrier map

\[
f:X\longrightarrow Y,
\]

covariant state transport is

\[
f_*b=fb,
\]

while contravariant instrument transport is precomposition,

\[
f^*d=df.
\]

No inverse is required.

## Mate identity

The instrument evaluation obeys the exact identity

\[
\langle f^*d,b\rangle_X
=
\langle d,f_*b\rangle_Y.
\]

In matrix notation this is simply

\[
(df)b=d(fb).
\]

The checker verifies the identity for all tested source states and instruments
under:

- cyclic transport;
- the noninvertible route-support projector;
- the forward triangle-incidence map.

It also verifies functoriality for a composite support map followed by cyclic
transport. Covariant transport preserves order, while contravariant
precomposition reverses it.

## Noninvertible hostile test

Take the route-support map

\[
S=\operatorname{diag}(1,1,0).
\]

Its rank is two, so inverse transport is unavailable. Nevertheless the
source-labelled matched pair gives

\[
\langle dS,b\rangle
=
\langle d,Sb\rangle
=1.
\]

Thus the supported instrument readout remains balanced and nonzero.

At the same time, Entry 3385's supported backward–forward commutator remains
rank three. Therefore a balanced instrument pairing does not imply
backward–forward compatibility.

Conversely, the failure of the backward–forward comparison does not by itself
destroy a well-typed instrument readout.

## Architectural consequence

The final (+1) is best understood as a mate or coend-style pairing between
the two variance towers. It is not inverse transport and not another
Beck–Chevalley square.

The current typed separation is:

1. contravariant and covariant functoriality;
2. comparison cells between those functorialities;
3. a balanced instrument pairing;
4. scalar readout after evaluation.

These structures can fail independently.

## Scope

This is an exact finite linear model. It does not yet construct the physical
Bunch–Davies instrument or prove a global coend realization over the full
cosmological Carrier.

## Verification

Checker: `research/benincasa/checkers/audit_instrument_mate_pairing.py`.

Packet: `research/benincasa/results/instrument_mate_pairing.json`.

Allocator claim: `seqclaim-1a39049e73e8d681364c5aa2`.

Epistemic graph event:
`ev-000000007283-b1cf1ecc-c003-44a4-b1f0-20cbf92a7a81`.
