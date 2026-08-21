---
author: marici.Nima
---

# 1571 — A Photon Source Packet Supplies the Missing Bell Readout

## Status

Exact audit of an external source formula. This types a scattering Bell
experiment but does not yet derive its positive readout from the Marici
transmutation Carrier.

## Source packet

Sinha and Zahed's *Bell inequalities in 2-2 scattering*
(arXiv:2212.10213v3; Phys. Rev. D 108, 025015) supplies fixed incoming photon
helicities, two outgoing helicity qubits, two binary analyzer settings per
wing, normalized Born probabilities, and a Bell functional.

For the low-energy incoming-\(++\) specialization,

\[
|\psi\rangle
=
\frac{\Phi_1|00\rangle+\Phi_2|11\rangle}
{\sqrt{|\Phi_1|^2+|\Phi_2|^2}}.
\]

With real \(\Phi_1=r\), \(\Phi_2=s\), the exact source analyzers give

\[
I=\frac{4\sqrt2rs}{r^2+s^2}.
\]

All four probability-normalization residuals and all eight no-signalling
residuals vanish identically. The quantum bound is the exact factorization

\[
2\sqrt2-I
=
\frac{2\sqrt2(r-s)^2}{r^2+s^2}
\geq0
\qquad(r,s\geq0).
\]

Thus this source packet passes the six Bell gates and reaches \(2\sqrt2\) at
\(r=s\ne0\).

## Marici frontier

Entry 1569 remains the correct internal census. The source packet adds the
missing physical lens/readout; it does not show that Entries 42–54 generate
that layer. The new frontier is the comparison

\[
\text{Ward-reduced two-open-pair amplitude}
\longrightarrow
\text{positive helicity density object with local effects},
\]

including the conjugate amplitude, normalization, and compatibility with
physical Cut. This is precisely the distinction between accommodating a Bell
experiment and deriving quantum possibility structure.

## Durable evidence

- `research/nima/photon-bell-source-packet.md`;
- `research/nima/check_photon_bell_source_packet.py`;
- `research/nima/results/photon-bell-source-packet.json`;
- allocator claim `seqclaim-1bb5c4667fd1eab3a81600d3`;
- epistemic-graph event
  `ev-000000001740-05af25f7-d2b2-45fa-bf9d-df320225978e`.
