# Independent two-demand cells are not universally five-vertex paths

## Question

Do all independent fixed-eight two-demand Hasse cells have the extremal five-vertex path topology and endpoint-deficit regime?

## Claim boundary

No. Among 500,634 negative pairs, 3,763 have collective slack strictly below both singleton slacks. Only 218 have the three-supply/four-edge five-vertex path topology, and those 218 are in the endpoint-deficit regime.

The first counterexample occurs for empty base and \((i,j)=(0,2)\). Demands \(\{0\},\{2\}\) have positive neighbors \(\{1\},\{3\}\) and three edges, giving a four-vertex alternating path rather than the five-vertex cell. The census contains twenty distinct degree-sequence topologies, with up to eight positive neighbors.

## Disposition

Literal path-cell universality is rejected. A stronger aggregation theorem survives: for any two demands, partition positive neighbors into left-private, shared, and right-private classes and sum each class. This quotient has exactly the \(P-D-P-D-P\) capacity model, allowing zero endpoint aggregates. Prove and test that every two-demand Hall problem factors through this three-supply quotient; topology then changes multiplicities but not cut algebra.
