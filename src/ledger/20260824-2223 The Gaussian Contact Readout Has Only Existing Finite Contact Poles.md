---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2223 — The Gaussian Contact Readout Has Only Existing Finite Contact Poles

## Meromorphic readout

For the channel complementary to a vertex, the contact coefficient is a
product

\[
C_jC_k=\frac1{\ell_j\ell_k}.
\]

Entry 2219's extracted Gaussian response is therefore

\[
R_{jk}=-\frac8{\ell_j\ell_k}.
\]

Its residues are

\[
\operatorname{Res}_{\ell_j=0}R_{jk}
=-\frac8{\ell_k},
\qquad
\operatorname{Res}_{\ell_k=0}
\operatorname{Res}_{\ell_j=0}R_{jk}=-8.
\]

Thus

\[
\boxed{
\operatorname{Pole}(R_{jk})=V(\ell_j\ell_k),
}
\]

with logarithmic order one on each component.

## Classification

These are precisely the source's existing shifted contact-energy divisors.
The mixed readout introduces no new finite support, branch character, or
Carrier incidence generator. It supplies a normalized residue on support
that was already present.

## Evidence

- Entries 2135–2136, 2177, and 2219
- `research/benincasa/checkers/contact_pole_score_residue.rs`
