---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2172 — The Correlator Star Separates Route Loss from Destructive Interference

## Packet factorization

Entry 2156's weighted augmentation must be factored through the labelled
route-packet object

\[
\mathcal S=\bigoplus_S\mathcal M_S
\xrightarrow{\widetilde T}
\mathcal P=\bigoplus_S\mathcal R_S
\xrightarrow{\sigma}
\mathcal R,
\]

where

\[
(\widetilde Tm)_S=(-2)^{|S|}T_Sm_S,
\qquad
\sigma((r_S)_S)=\sum_Sr_S.
\]

Thus Entry 2156's augmentation is

\[
\epsilon=\sigma\widetilde T.
\]

Because the eight copies \(\mathcal R_S\) retain their occurrence labels,
there is a canonical exact mechanism sequence

\[
\boxed{
0\longrightarrow\ker\widetilde T
\longrightarrow\ker\epsilon
\longrightarrow
\operatorname{im}\widetilde T\cap\ker\sigma
\longrightarrow0.
}
\]

The final arrow sends a source class to its nonaggregated route packet.

## Two mechanisms

This separates two physically different reasons for a null readout:

1. **route loss**:
   \[
   \widetilde Tm=0;
   \]
2. **destructive interference**:
   \[
   \widetilde Tm\ne0,
   \qquad
   \sigma\widetilde Tm=0.
   \]

The distinction disappears if the eight outputs are summed too early.

## Consequence for the component-soft packet

Entries 2160–2166 constructed a supported Tor packet from simultaneous
vanishing of local component and soft routes. That is evidence for the
route-loss side of the sequence. It is not evidence that the cosmological
correlator already contains a nonzero destructive-interference packet.

Conversely, the moving pointwise kernel of Entries 2158–2159 was calculated
after aggregation. Its mechanism cannot be classified until the eight
weighted route values are retained before applying \(\sigma\).

The next finite test is therefore fixed:

\[
\boxed{
\text{evaluate the eight source-defined }(-2)^{|S|}T_S
\text{ on one common physical input before summation.}
}
\]

A nonzero packet in \(\ker\sigma\) would be the cosmological analogue of
Strominger's magnetic destructive-interference witness. Componentwise zero
would instead confirm pure route loss.

## Scope

The exact sequence is formal once Entry 2156's source-defined star is
retained. It does not assert that either kernel contains a physical class,
and it does not identify the sector-specific domains \(\mathcal M_S\).
Those require the actual deletion-sector integrands and a common physical
relative chain.

## Evidence

- Entries 2156–2160
- `research/benincasa/checkers/three_site_weighted_correlator_adapter.py`
- `research/benincasa/checkers/correlator_route_packet_exact_sequence.rs`
- allocator claim `seqclaim-0cedfe0e5b21cb49eb67badb`
