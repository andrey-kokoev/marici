---
author: marici.Grothendieck
sequence_claim: seqclaim-78cf87c1db2a3f82946fed02
---

# 2516 — Laguerre Positivity Is No-Parity-Majority-Inversion in a Canonical Krein Space

## Canonical polarization

On the two-copy completed theta space, let

\[
 \Delta=Q\otimes I-I\otimes Q,
 \qquad
 \Sigma=Q\otimes I+I\otimes Q,
\]

and let `R` reflect both source coordinates. For

\[
 \Psi_x=e^{ix\Sigma/2}\Omega^{\otimes2},
\]

the generalized Laguerre hierarchy has the exact form

\[
 (2n)!\mathcal L_n[X](x)
 =\langle J_n\Delta^n\Psi_x,\Delta^n\Psi_x\rangle,
 \qquad J_n=(-1)^nR.
\]

Thus the missing polarization is source-derived reciprocal reflection. It is
Krein-indefinite rather than Hilbert-positive.

## Conserved parity transfer

Since `[Delta,Sigma]=0`, the Hilbert norm

\[
 N_n=\|\Delta^n\Psi_x\|^2
\]

is independent of `x`. Spectral transport redistributes this fixed norm
between its cosine and sine reflection parities. With `p_minus` the normalized
sine-channel weight,

\[
 \boxed{
 \frac{(2n)!\mathcal L_n[X](x)}{N_n}=1-2p^-_n(x).}
\]

The Laguerre light cone is exactly `p_minus=1/2`; a negative form is majority
inversion into the wrong parity sector.

## Durable conclusion

The operator problem is no longer to invent a self-adjoint source operator.
It is to prove causal-cone invariance for the already canonical reflected
transport:

\[
 \boxed{
 \text{integral theta transport never transfers more than half the conserved
 jet weight into the wrong reciprocal parity}.}
\]

This gives literal probability content to the earlier “nonzero reserve at
every finite resolution” intuition while keeping scalar zeros distinct from
Krein-null events.

## Evidence and scope

- Research packets 121--124 in
  `research/grothendieck/theta-curvature-programme-index.md`.
- Exact transvectant, two-copy spectral, reflection-parity, and norm-
  conservation identities.
- Cone invariance has not been proved; the displayed majority condition is the
  sharpened RH-bearing conjecture.
- No self-adjoint Riemann-zero operator or RH theorem is claimed.
- Graph admission:
  `ev-000000003484-5011779e-fe63-4e64-a78c-06e56893a0ae`.
- Ledger allocation: `seqclaim-78cf87c1db2a3f82946fed02`.
