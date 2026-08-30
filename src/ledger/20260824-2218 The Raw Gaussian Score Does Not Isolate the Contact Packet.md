---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2218 — The Raw Gaussian Score Does Not Isolate the Contact Packet

## Contamination audit

For any labelled edge \(e\), the score derivative acts on every erased subset
containing that edge. In the three-edge Boolean family there are four such
subsets.

The hidden contact channel contains only the two routes isolated in Entry
2174. Therefore the unprojected mixed correlator generally contains other
connected and partially deleted contributions:

\[
\boxed{
\langle O S_{K_e}\rangle_c
\neq
\text{contact packet alone}.
}

Entry 2216 correctly computes the contact packet's contribution to the score
response, but it must not be read as saying that one raw higher correlator
contains no background.

## Required operation

A physical extraction needs the independently frozen contact-normal channel
of Entries 2158–2159 and 2174, or an equivalent source-derived residue. No
projector may be fitted from the desired value \(-8C_e\).

## Evidence

- Entries 2174 and 2211–2217
- `research/benincasa/checkers/score_total_response_contamination.rs`

