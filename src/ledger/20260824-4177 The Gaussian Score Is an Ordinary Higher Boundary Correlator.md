---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 4177 — The Gaussian Score Is an Ordinary Higher Boundary Correlator

## Operational form

For momentum mode \(q\), the normalized score is

\[
S_K(q)=a(q)\Phi(q)\Phi(-q)-\frac12.
\]

Inside a connected pairing with \(O\), the constant term drops out:

\[
\boxed{
\langle O S_K(q)\rangle_c
=a(q)\langle O\Phi(q)\Phi(-q)\rangle_c.
}
\]

Thus the mixed port of Entry 2216 is an ordinary connected boundary
correlator with two additional opposite-momentum legs, followed by the
source-fixed factor \(a(q)=\operatorname{Re}\psi_2(q)\).

No hypothetical ancilla, branch detector, or nearby-state preparation is
required. The readout belongs to the existing algebra of late-time boundary
correlators.

## Qualification

This establishes operational typing, not experimental ease. Extracting the
specific contact contribution from the full higher correlator still requires
a canonical kinematic/support projector.

## Evidence

- Entries 2214–2216
- `research/benincasa/checkers/score_higher_correlator.rs`