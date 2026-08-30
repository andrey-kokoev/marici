---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2156 — The Correlator Deletion Object Is an Augmented Star, Not a Coefficient Cube

## Source-derived object

For the three labelled edges, let (S\subseteq\{12,23,31\}) index the eight
edge-erased graph sectors. The source gives one port per sector,

\[
T_S:\mathcal M_S\longrightarrow\mathcal R,
\]

and the weighted augmentation

\[
\boxed{
\epsilon
=
\sum_S(-2)^{|S|}T_S:
\bigoplus_S\mathcal M_S\longrightarrow\mathcal R.
}
\]

Here (mathcal R) is the common correlator readout. The deletion-grade
multiplicities and total weights are

\[
(1,3,3,1),
\qquad
(1,-6,12,-8).
\]

## Typing consequence

The Boolean lattice remains the labelled indexing carrier for the eight
summands. It does not carry a source-defined coefficient differential.
Accordingly, the actual diagram is an augmented star with one common sink,
not a cube-shaped chain complex.

This simultaneously retains the two valid observations:

1. port compositions commute whenever they are compared in the common
   readout;
2. no inter-grade map (mathcal M_S\to\mathcal M_{S\cup\{e\}}) has been
   constructed.

## Derived frontier

The first canonical place where cross-sector coherence could live is

\[
\operatorname{Fib}(\epsilon)
\quad\text{or equivalently the shifted cofiber of }epsilon.
\]

This is a proposal for a calculation, not an assertion that the fiber is
nonzero or that it carries a physical class. Any such class must be derived
from the eight coefficient systems and the frozen weighted augmentation.

## Architectural update

This gives a sharper form of H2 in the correlator lane:

\[
\boxed{
\text{shared Boolean occurrence carrier}
+
\text{sector-specific coefficient modules}
+
\text{one source-weighted readout augmentation}.
}
\]

The correction removes the need for invented cube arrows without discarding
the source’s genuine deletion combinatorics.

## Evidence

- `research/benincasa/correlator-augmented-star-architecture.md`
- `research/benincasa/checkers/three_site_weighted_correlator_adapter.py`
- `research/benincasa/checkers/results/three-site-weighted-correlator-adapter.json`
- allocator claim `seqclaim-ec9edbfb3c68223b65d2c406`
