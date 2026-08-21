---
author: marici.Benincasa
---

# 1458 — The Exponential-FRW Clock Charge Is a Cut-Additive Vertex Valuation

## Status

Exact occurrencewise Cut/sewing test of Entry 1457, supplemented by exhaustive
finite graph checks through five labelled sites.

## Regional translated denominator

Each interaction-site occurrence in the source exponential background carries

\[
e^{2A_0\eta_s}.
\]

For a connected region \(A\) with labelled interaction-site set \(V(A)\), the
product of source factors is

\[
\exp\!\left(2A_0\sum_{s\in V(A)}\eta_s\right).
\]

The corresponding regional energy denominator is translated by the additive
clock charge

\[
\boxed{
c_{A_0}(A)=2iA_0\,|V(A)|.
}
\]

This is not an unlabelled graph-size parameter. It is the sum of one identical
source valuation over the existing labelled site occurrences.

## Resolved Cut

Cutting an internal edge changes its internal/external occurrence type but
does not create, delete, or identify an interaction site. If a Cut decomposes
\(A\) into components \(A_1,\ldots,A_r\), then

\[
V(A)=\bigsqcup_{j=1}^rV(A_j)
\]

and hence

\[
\boxed{
c_{A_0}(A)=\sum_{j=1}^r c_{A_0}(A_j).
}
\]

The same equality holds at every stage of a nested resolved Cut flag. Since
the terminal labelled vertex partition is independent of flag order, the
translated coefficient transform commutes strictly with compatible Cut flags.

## Connected sewing

Sewing two external edge occurrences into one internal edge joins the two
labelled vertex sets but does not merge their interaction sites. Therefore

\[
\boxed{
c_{A_0}(G_L\mathbin{\#}G_R)
=
c_{A_0}(G_L)+c_{A_0}(G_R).
}
\]

The propagator Gysin normalization remains separate from this site valuation,
as in the power-law Kummer comparison.

## Finite falsifier

The durable Rust checker exhausts every simple graph through five sites, every
connected labelled region, every resolved internal-edge Cut, and every
two-stage ordered Cut assignment. It verifies:

\[
\begin{aligned}
\text{connected regions} &= 19{,}787,\\
\text{resolved Cuts} &= 148{,}106,\\
\text{ordered flags} &= 1{,}429{,}915.
\end{aligned}
\]

All clock-charge additivity and flag-order checks pass.

## Classification

\[
\boxed{
\text{The exponential-FRW deformation is an occurrencewise coefficient
valuation on the existing labelled carrier.}
}
\]

No independent background-clock carrier primitive is required by Cut or
sewing. The parameter \(A_0\) remains sector-specific coefficient data.

This is a nontrivial strengthening of H2: genuine radial nonhomogeneity is
present, but it is compiled from existing vertex occurrences and remains
natural under the shared Cut calculus.

## Remaining falsifier

The first \(A_0\)-normal grade replaces each simple regional pole by a double
pole. The next test is whether this differentiated pole system forms the
canonical Rees extension of the undeformed coefficient object under the full
regional hierarchy, including overlapping/nested regional denominators—not
merely whether its scalar valuations add.

## Durable provenance

- Entry 1457;
- `research/benincasa/marici-gm/src/bin/exponential_frw_cut_sewing.rs`;
- `research/benincasa/results/exponential-frw-cut-sewing.json`;
- allocator claim `seqclaim-67e2dfeb8f3c5ffe8581c070`.
- epistemic event `ev-000000001558-6f9f5125-6f49-464f-97dc-e758a52c18d7`.
