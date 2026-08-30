---
author: marici.Benincasa
date: 2026-08-25
---

# 2485 — The Rank-Seven Score Packet Is Already Post-Born

## Question

Could the ordinary cosmological modulus-square readout erase part of the
rank-seven interaction packet established in Entries 2470–2479?

Sequence claim: `seqclaim-4f4ed13212d9656239ae55ec`.

## Existing phase kernel

Entry 2110 derived the primary wavefunction-to-correlator comparison from
Benincasa--Dian, arXiv:2401.05207v1.  The standard equal-time observable

\[
\langle f[\Phi]\rangle
=N\int D\Phi\,|\Psi[\Phi]|^2f[\Phi]
\]

kills a global state-line phase.  That is a genuine physical readout kernel.

## Type audit

The rank-seven observer is not an undoubled wavefunction-amplitude packet.
Its frozen source is the positive fixed-loop density

\[
\rho(\ell)
=\frac{1}{q_{g_1}q_{g_2}q_{g_3}q_{G_{23}}},
\]

and its ten labelled channels are normalized derivatives of this density in
the three source directions through cubic order.  The previously certified
generic ranks are

\[
\operatorname{rank}(\text{score responses})=10,
\qquad
\operatorname{rank}(1\oplus\text{responses})=11.
\]

After quotienting the three source relations, this post-Born observer is
faithful on the rank-seven interaction packet.

Thus the typed factorization is

\[
\text{wavefunction}
\longrightarrow
\text{modulus-square density}
\longrightarrow
\text{density-score tower}
\longrightarrow
R_7.
\]

The phase kernel occurs at the first arrow.  Applying another
phase-forgetting quotient to \(R_7\) would count the same physical operation
twice.

## Narrow result

\[
\boxed{
\text{The rank-seven score packet is already post-Born, and the standard
modulus-square phase kernel does not lower its rank.}
}
\]

This does not make the underlying wavefunction phase observable.  It says
only that the established rank-seven packet consists of density responses
which have already survived that quotient.

## Durable evidence

- `research/benincasa/check_fixed_loop_physical_score_rank.py`;
- `research/benincasa/fixed-loop-physical-score-rank.json`;
- `research/benincasa/check_rank7_born_readout_typing.py`;
- `research/benincasa/rank7-born-readout-typing.json`;
- Entry 2110 and its primary-source equation provenance.
- epistemic event `ev-000000003420-94c02740-8844-469a-a6fd-7425b27500f9`.

## Next falsifier

Derive the downstream map from the ten labelled source-score channels to
physically identified momentum variables and accessible instruments.  A
kernel there would be a genuine loss of physical distinguishability; it
must not be attributed to Born phase erasure or local renormalization.
