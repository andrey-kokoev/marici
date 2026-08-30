---
authors:
  - marici.Benincasa
date: 2026-08-28
---
# 3877 — The Source Conductor Port Requires the Labelled Root Cover

## Hostile sheet test

For the (G_{12}:g_1) conductor, write

\[
R_1=-xa^2+C_1,
\qquad
r^2=\frac{C_1}{x}.
\]

Entry 3862 used the physical positive-root coefficient

\[
c_+=\left.-\frac{F_1}{\partial_aR_1}\right|_{a=r}.
\]

The other sheet carries

\[
c_-=\left.-\frac{F_1}{\partial_aR_1}\right|_{a=-r}.
\]

Under the deck action (r\mapsto-r), the two coefficients exchange. Define

\[
c_{\rm ev}=\frac{c_++c_-}{2},
\qquad
c_{\rm odd}=\frac{c_+-c_-}{2}.
\]

Exact reduction proves

\[
c_{\rm ev}(-r)=c_{\rm ev}(r),
\qquad
c_{\rm odd}(-r)=-c_{\rm odd}(r).
\]

Both components are generically nonzero and are nonzero at the asymmetric
sample ((x,y,z)=(2,3,4)). Hence

\[
c_+=c_{\rm ev}+c_{\rm odd}
\]

is not a base-descended scalar section.

## Consequence

The deck-even aggregate descends to the kinematic base, but it discards the
nonzero anti-invariant component of the source-selected positive sheet. The
correct specialization target is therefore the labelled rank-two projector
packet on the root cover, or equivalently its even and odd local systems.

This falsifies the simpler gate in which the jet-residue constructor of Entry
3875 maps directly to one scalar costalk over the base. The constructor must
be applied separately at (r) and (-r), with deck transport retained before
any physical-sheet selection or aggregation.

The cover branches on (C_1=0). This calculation classifies that locus only
as projector/coefficient branching. It does not promote it to a Carrier
divisor or physical singularity.

## Next falsifier

Construct the two sheet-resolved jet covectors on the physical rank-26 basis
and test the connection identity on the joint parameter-root cover. Then test
whether the source integration chain canonically selects one sheet on its
entire admitted domain. Aggregate descent alone is insufficient.

## Verification

- checker: `research/benincasa/checkers/check_rank26_conductor_root_cover_deck_splitting.py`;
- packet: `research/benincasa/results/rank26-conductor-root-cover-deck-splitting.json`;
- allocator claim: `seqclaim-5e7089f2e12f59945a038ddc`.
