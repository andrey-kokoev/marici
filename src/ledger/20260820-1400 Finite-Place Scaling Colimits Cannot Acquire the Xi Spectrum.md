---
author: marici.Grothendieck
---

# 1400 — Finite-Place Scaling Colimits Cannot Acquire the Xi Spectrum

Sequence claim: `seqclaim-bc180db10f45c7a986404e99`.

Epistemic-graph event: 1446.

For every finite set (S) of places, the CCM Hardy--Titchmarsh transform puts
the scaling generator in the form

\[
M_s\quad\text{on}\quad
L^2\!\left(\mathbb R,
c_S\left|\prod_{v\in S}L_v(1/2-is)\right|^2ds\right).
\]

The density is finite and strictly positive on the real line.  Multiplication
by its square-root is therefore a unitary to Lebesgue (L^2(\mathbb R)) and
commutes with (M_s).  Every finite-(S) scaling operator is consequently the
same purely absolutely-continuous multiplication operator up to unitary
equivalence: it has spectrum (\mathbb R), no eigenvalues, and noncompact
resolvent.  Adding finite places changes the cyclic weight, not the spectral
type.

The raw all-places multiplier also fails at the central point:

\[
\log\prod_{p\le P}(1-p^{-1/2})^{-1}
\geq \sum_{p\le P}p^{-1/2}
\geq \sum_{p\le P}p^{-1}\longrightarrow\infty,
\]

while completed Xi is finite there.  Hence the unrenormalized critical-line
Euler multipliers have no pointwise, much less locally uniform, Xi limit.

Thus the naive semilocal Hilbert colimit cannot be the desired discrete Xi
operator.  A nonunitary step—Weil radical quotient, compression, or boundary
condition—is mathematically necessary.  Any renormalized all-places proposal
must additionally prove canonical normalization and convergence of domains,
resolvents, and determinants.

Scope: no-go theorem for the ambient scaling colimit and unrenormalized Euler
product.  It does not exclude a source-derived conditioned or radical quotient.

Durable verification:

- Research packet:
  `research/grothendieck/finite-place-scaling-colimit-no-go.md`.
- CCM canonical spectral form and elementary equivalence-of-measures proof.
- Euler divergence at the central critical-line point.
- Sequence claim: `seqclaim-bc180db10f45c7a986404e99`.
- Epistemic-graph event: 1446.
