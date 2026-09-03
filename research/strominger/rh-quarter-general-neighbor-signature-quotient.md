# Exact neighbor-signature quotient for arbitrary demand count

## Question

What source-independent aggregation remains after three-class and interval compressions fail?

## Claim boundary

For any finite capacitated bipartite supply-demand network, aggregate supply vertices having the same nonempty demand-neighbor subset. This preserves every Hall cut because each original supply contributes to a cut exactly when its signature intersects that cut. It preserves max-flow feasibility by the max-flow/min-cut theorem. A quotient flow lifts by distributing each signature-class outgoing vector among original class members subject to their capacities; this is a finite transportation allocation with total requested flow no larger than total class capacity.

Exact testing covers 28,224 three-demand two-supply weighted networks and 5,000 seeded networks with up to seven supplies. Flow lifting passes 5,000 capacity vectors. A deliberate failure merges distinct signatures and changes feasibility, showing that arbitrary further aggregation is unsound.

## Disposition

The exact class bound is \(2^m-1\) for \(m\) demands. This theorem removes graph size from the quotient but does not provide polynomial all-order Hall control. Hasse incidence alone supplied no smaller quotient in the tested three-demand cells. The next bounded test asks whether the seven-class bound is attained by one independent fixed-eight cell; failure would leave a source-specific reduction open, while attainment would make the generic bound locally sharp.
