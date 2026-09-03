# Ordered-subset Markov Beck–Chevalley

## Question

Can noncontiguous restriction be made canonical by retaining the effective transition induced by every omitted interval?

## Claim boundary

This packet treats strictly increasing injections of finite ordered vertex sets into metric-transition Markov chains. It does not cover repeated vertices, unordered maps, branching diagrams, or arbitrary categorical pullbacks.

## Induced restriction

For retained vertices

\[
i_0<i_1<\cdots<i_m,
\]

retain metrics \(M_{i_r}\) and define the effective adjacent covariance

\[
C^{\mathrm{eff}}_r=K_{i_r,i_{r+1}}
=C_{i_r}M_{i_r+1}^{-1}\cdots M_{i_{r+1}-1}^{-1}C_{i_{r+1}-1}.
\]

This is typed from the later retained fiber to the earlier retained fiber. Reconstructing the metric-transition kernel from these effective covariances yields

\[
K^{\mathrm{eff}}_{rs}=K_{i_r,i_s}.
\]

Therefore induced restriction equals principal block compression for every ordered subset, not only contiguous intervals. The Beck–Chevalley comparison is identity and invertible.

## Pasting

If a second increasing injection selects a subset of the retained vertices, recomputing effective covariances gives the same long blocks as direct selection from the original chain. Ordered-subset restrictions therefore compose strictly, and their Beck–Chevalley identity cells paste strictly.

## Relation to the prior hostile fixture

The earlier noncontiguous rejection concerned deletion without supplying an effective transfer. Equal cardinality still does not authorize a probe. The present constructor adds the missing typed effective covariance derived from the source kernel; it does not reinterpret the naive retained-edge list.

## Hostile boundary

A vertex list with duplicates or reversed order is not a strictly increasing injection. Its apparent covariance matrix may exist as a raw compression, but it is not an admitted Markov restriction because no forward ordered interval defines each effective edge.

## Disposition

General contiguous Beck–Chevalley extends canonically to all strictly increasing ordered-subset injections. The remaining pullback gate concerns branching or non-monic diagrams, not noncontiguity itself.

## Verification

- `research/voevodsky/checkers/check_ordered_subset_markov_beck_chevalley.py`
- `research/voevodsky/results/ordered_subset_markov_beck_chevalley.json`
