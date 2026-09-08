---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2205 — Deletion Parity Is Not a Keldysh Branch Observable

## Primary-source distinction

In Benincasa–Dian, arXiv:2401.05207, the probability-distribution derivation
first gives the erased-wavefunction-graph expansion

\[
\mathcal C_{\mathcal G}=\sum_{S\subseteq E}\psi_{\mathcal G\setminus S},
\]

with unit coefficient for every erased graph; see equations (2.13)–(2.14)
and the source discussion immediately surrounding them.

The coefficients

\[
(-2)^{|S|}
\]

appear in a different construction: equations (4.66)–(4.71) express the
weighted canonical form through overlapping polytopes associated with the
edge subsets. The signs encode the weights and relative orientations of that
subdivision.

Therefore

\[
\boxed{
\text{deletion parity is a weighted-geometry orientation character,
not a declared Keldysh outcome.}
}
\]

## Correction to the dilation lane

Entries 2202–2204 remain exact statements about the finite signed
subdivision measure. Their proposed Bernoulli/parity realization is not
source provenance for an in-in ancilla. The primary source supplies no
deletion-bit sampler or parity measurement, and the physical erased-graph
formula itself has no alternating deletion coefficients.

Thus the direct coherent-ancilla activation route is closed under this
source. Any such realization would be an enlargement rather than an
unpacking of the published Keldysh–Schwinger construction.

## Evidence

- Benincasa–Dian, arXiv:2401.05207, equations (2.13)–(2.14), (4.66)–(4.71)
- `research/benincasa/checkers/deletion_parity_provenance.rs`
