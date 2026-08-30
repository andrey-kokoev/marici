---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2201 — The Generic Contact Kernel Is Pure Destructive Interference

## Mechanism sequence

Factor the contact observation as

\[
\mathcal S_{\rm ct}
\xrightarrow{T}
\mathcal P_2^{\oplus3}
\xrightarrow{\sigma}
\mathcal R_{\rm ct},
\]

where \(T\) sends the three source labels to the nonzero route pairs

\[
(8C_e,-8C_e)
\]

and \(\sigma\) sums each pair. The exact mechanism sequence is

\[
0\to\ker T\to\ker(\sigma T)
\to\operatorname{im}T\cap\ker\sigma\to0.
\]

At generic finite contact kinematics every \(C_e\neq0\). Hence

\[
\ker T=0,
\qquad
\dim(\operatorname{im}T\cap\ker\sigma)=3.
\]

Therefore

\[
\boxed{
\text{route-loss rank}=0,
\qquad
\text{interference rank}=3.
}
\]

The scalar correlator is blind because two nonzero routes cancel, not because
either route is absent. This is the exact three-channel cosmological analogue
of Strominger's magnetic route-packet witness.

## Boundary qualification

This theorem is generic and finite. Earlier infinity audits show that
ordinary restriction can turn the packet into route loss while the first
Cartier grade retains interference. That filtered boundary behavior does not
alter the generic classification.

## Evidence

- Entries 2174, 2178, and 2196–2200
- `research/benincasa/checkers/contact_route_mechanism_sequence.rs`

