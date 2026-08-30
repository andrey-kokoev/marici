---
author: marici.Benincasa
date: 2026-08-27
---

# 3636 — The Physical Relative Cycle Activates Endpoint Torsion but Mod Two Forgets Its Deck Selection

## Corrected status

Entry 3637 proves that the boundary divisor \(\tau\) is principal. The
chain-level identity \(\partial\Gamma_-=\tau\) and the mod-two alias below
remain correct, but they do not activate a nonzero Jacobian torsion class.
The proposed Weil-pairing frontier is withdrawn.

## Physical boundary

Entry 3618 constructs the source sign-weighted relative cycle

\[
\Gamma_-=\gamma_+-\gamma_-.
\]

Its boundary is

\[
\partial\Gamma_-
=q_{S\infty}-q_{S0}
=(p_\infty^+-p_0^+)-(p_\infty^--p_0^-)
=\tau.
\]

Thus the endpoint two-torsion of Entry 3627 is not detached from the physical
relative-chain packet. It is exactly the boundary of the source-selected odd
completion.

## Characteristic-two alias

The ordinary trace completion has boundary

\[
q_T=(p_\infty^++p_\infty^-)-(p_0^++p_0^-).
\]

In the ordered basis

\[
(p_\infty^+,p_0^+,p_\infty^-,p_0^-),
\]

the two integral boundaries are

\[
q_T=(1,-1,1,-1),
\qquad
\tau=(1,-1,-1,1).
\]

They are distinct over \(\mathbb Z\): \(q_T\) is deck-even and \(\tau\) is
deck-odd. After reduction modulo two, however,

\[
q_T\equiv\tau\equiv(1,1,1,1).
\]

Therefore the mod-two boundary map forgets the source distinction between
ordinary and sign-weighted completion.

## Result

Physical activation is established at integral chain level:

\[
\partial\Gamma_-=\tau.
\]

But reduction to the torsion boundary alone is not a faithful physical
readout. It identifies the deck-even and deck-odd completions. The missing
datum is not incidence; it is an integral or polarized functional retaining
the lift that selected \(\Gamma_-\).

The next admissible test is to derive an integral linking pairing or a
principal-polarization Weil pairing from the source packet. No dual torsion
class may be chosen merely to make the pairing nonzero.

## Evidence

- `research/benincasa/checkers/check_endpoint_torsion_physical_boundary.py`;
- `research/benincasa/results/endpoint-torsion-physical-boundary.json`.

The exact checker passes seven of seven gates.

Epistemic graph event:
`ev-000000007809-853ffe9e-af12-45da-bb2f-6e69cedeb1cc`.

Allocator claim: `seqclaim-a46d1c0afc1b448e21c14a74`.
