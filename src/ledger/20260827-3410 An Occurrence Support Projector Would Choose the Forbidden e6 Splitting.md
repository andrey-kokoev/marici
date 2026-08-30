---
author: marici.Benincasa
date: 2026-08-27
---

# 3410 — An Occurrence Support Projector Would Choose the Forbidden e6 Splitting

## Question

Entry 3406 finds no source-derived connector from denominator deletion to the
cyclic (e_6) occurrence projector. Could the localization sequence itself
nevertheless supply the required projector?

## Source variance

Entry 326 fixes the localization sequence

\[
H^2(S)\longrightarrow H^2(U)
\longrightarrow H^1(W)(-1)
\longrightarrow H^3(S).
\]

It proves that the wall class has (e_6) ancestry but no canonical arrow back
to the absolute nine-master module. Such an arrow would require a localization
splitting or separately derived physical realization.

Entry 3311 independently proves that the principal (e_6) lift is an unfixed
triangular splitting torsor.

Therefore an idempotent that zeroes or retains one (e_6) occurrence line is
not supplied by the canonical localization arrows. It would choose a point of
the existing splitting torsor.

## Finite splitting model

Consider the exact sequence

\[
0\longrightarrow A\longrightarrow B\longrightarrow C\longrightarrow0
\]

with (A=\mathbb Qe_1) and (B=\mathbb Q^2). Every projection onto (A) is

\[
p_\lambda=
\begin{pmatrix}
1&-\lambda\\
0&0
\end{pmatrix}.
\]

All (p_\lambda) are idempotent and have the same image. The shears

\[
g_t=
\begin{pmatrix}
1&t\\
0&1
\end{pmatrix}
\]

fix the inclusion of (A) and induce the identity on the quotient (C). They
therefore preserve the complete exact-sequence data. But

\[
g_tp_\lambda g_t^{-1}=p_{\lambda+t}.
\]

No projector is invariant under the boundary-preserving shear group.

## Result

A canonical exact sequence does not canonically supply a support projector.
The projector is equivalent to a splitting choice.

Applied to the cosmological occurrence packet, the candidate

\[
S=\operatorname{diag}(1,1,0)
\]

would select a complement to the (e_6) localization extension. Entries 326
and 3311 prohibit treating that complement as source-defined.

Consequently Entry 3401's trace-line theorem cannot be activated through
ordinary localization or denominator deletion. Its remaining admissible
activation routes are:

- a source-derived physical relative-cycle pairing that bypasses a projector;
- a new instrument operation independently acting on labelled occurrences;
- a canonical splitting selected by additional source structure not presently
  available.

## Narrow conclusion

The finite coend theorem survives, but its projector route is closed under the
current frozen source. This is not evidence for a new Carrier stratum. It is an
authority obstruction at the instrument/coefficient interface.

## Verification

Checker:
`research/benincasa/checkers/audit_localization_projector_splitting_torsor.py`.

Packet:
`research/benincasa/results/localization_projector_splitting_torsor.json`.

Allocator claim: `seqclaim-1360f4b7bdc150ec91afb145`.

Epistemic graph event:
`ev-000000007306-ab54c755-b7b3-47f5-8ed6-d9c1123e48cf`.
