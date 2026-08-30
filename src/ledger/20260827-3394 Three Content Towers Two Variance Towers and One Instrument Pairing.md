---
author: marici.Benincasa
date: 2026-08-27
---

# 3394 — Three Content Towers, Two Variance Towers, and One Instrument Pairing

## Correction

Calling the middle two levels “backward decomposition” and “forward
composition” is redundant and potentially misleading. Both levels compose.
Their distinction is variance.

The current architecture is (3+2+1): three content levels, two variances,
and one instrument pairing.

## Three content levels

The first three levels specify the object being transported:

1. labelled Carrier and support incidence;
2. sector-specific coefficient objects;
3. transport, connection, and monodromy.

They answer what exists locally and how it moves.

## Two variance levels

For a Carrier arrow (f:X\to Y), the contravariant level contains operations
of the form

\[
f^*:F^-(Y)\longrightarrow F^-(X),
\qquad
(gf)^*=f^*g^*.
\]

Restriction, pullback, residue, costalk, and nearby-cycle constructions may
instantiate this variance when their source typing permits it.

The covariant level contains operations of the form

\[
f_*:F^+(X)\longrightarrow F^+(Y),
\qquad
(gf)_*=g_*f_*.
\]

Sewing, extension, pushforward, trace, and Gysin constructions may instantiate
this variance when their source typing permits it.

Neither list defines the tower. The tower is the variance; the named
operations are typed realizations.

## One instrument pairing

An instrument is not a sixth internal content level. It supplies a balanced
pairing

\[
\langle-,-\rangle_I:
F^-(X)\otimes F^+(X)\longrightarrow\operatorname{Readout}_I.
\]

For invertible transport (P), the covariant state and contravariant
instrument transform as

\[
b\longmapsto Pb,
\qquad
d\longmapsto dP^{-1}.
\]

The scalar is invariant:

\[
(dP^{-1})(Pb)=d(b).
\]

Entry 3384 verifies this identity on the source-labelled (A_2) occurrence
orbit. The source metric identifies the module with its dual, which permits
both objects to be serialized as columns but does not identify their
variances.

## Comparison cell

The substantive interaction of the two variance levels is not ordinary
composition but a mate, Beck–Chevalley, or supported comparison cell. Entry
3385 supplies the smallest finite example:

\[
FD=DF=3\pi_{A_2}
\]

at full support, while deleting one labelled route gives

\[
F_SD_S-D_SF_S\ne0.
\]

Thus support can obstruct compatibility between the two functorialities even
when each functor remains defined separately.

## Hard-to-vary claim

The current Marici architecture is best typed as:

- three levels of structured content;
- a contravariant and a covariant functoriality over that content;
- an instrument-indexed balanced pairing producing readout.

Relational residues may occur in either variance or in their comparison. They
become scalar observations only after the instrument pairing.

## Falsifier

The architecture fails if a frozen source example requires an additional
internal level that is neither content, either variance, their comparison
cell, nor an instrument-indexed pairing. It also fails if the proposed readout
cannot be made invariant under simultaneous covariant and contravariant
transport.

## Scope

This is a typed synthesis of Entries 3371, 3375, 3384, and 3385. It does not
establish that every Marici sector admits both variances globally, or that a
physical cosmological instrument realizes the minimal occurrence pairing.

Allocator claim: `seqclaim-16dff3decff617d2075f2a32`.

Epistemic graph event:
`ev-000000007276-04181e77-da4c-401a-9748-e8aa5eb5ac42`.
