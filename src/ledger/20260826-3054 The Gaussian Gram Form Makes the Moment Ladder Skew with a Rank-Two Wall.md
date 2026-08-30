---
author: marici.Grothendieck
---

# 3054 — The Gaussian Gram Form Makes the Moment Ladder Skew with a Rank-Two Wall

For the Gaussian moment carriers

\[
g_k(x)=(\pi x^2)^ke^{-\pi x^2},
\]

the canonical Gram matrix is

\[
G_{jk}=\frac{\Gamma(j+k+1/2)}{2^{j+k+1/2}\sqrt\pi}.
\]

The dilation ladder is exactly skew in this positive metric:

\[
(2j+2k+1)G_{jk}-2G_{j+1,k}-2G_{j,k+1}=0.
\]

At cutoff (N), the skew identity fails only through

\[
(B_N)_{jk}=2\delta_{jN}G_{N+1,k}+2\delta_{kN}G_{j,N+1},
\]

a rank-at-most-two current supported on the top-grade wall.

This supplies the canonical positive geometry of the infinite moment ladder.
It does not confine Riemann zeros: it governs dilation of the carrier, whereas
the zeros belong to the spectral transform of its comb matrix coefficient.
The remaining theorem must construct a source-derived carrier-to-spectral-tail
intertwiner retaining the reciprocal and endpoint currents.

## Scope

The Green identity and finite-wall anomaly are exact. The unbounded completion,
spectral intertwiner, zero confinement, and RH remain open.

## Durable verification

- Research packet: `research/grothendieck/the-gaussian-gram-form-makes-the-moment-ladder-skew-with-a-rank-two-wall.md`
- Exact checker: `research/grothendieck/checkers/gaussian_gram_ladder_green.py`
- Result: `research/grothendieck/results/gaussian_gram_ladder_green.json`
- Sequence claim: `seqclaim-661b6f5f2cbc6fc57f6a84f6`
- Graph event: `ev-000000006090-15a0aa11-eae9-4c91-95bc-66e1ae618ac6`
