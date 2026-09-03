# Operator-valued contiguous Beck–Chevalley

## Question

Do contiguous restriction and noncommutative Markov amalgamation satisfy an invertible Beck–Chevalley law?

## Claim boundary

The result concerns fixed finite fiber dimension, ordered contiguous vertex intervals, and path-product kernels. It does not cover arbitrary subsets, general pullbacks, quotient probes, or varying fibers.

## Square

Let a chain have transfers \((A_0,\ldots,A_{n-1})\), and let \([p,q]\) be a contiguous vertex interval. There are two routes:

1. construct the full block Green kernel and compress to blocks indexed by \([p,q]\);
2. restrict the transfer list to \((A_p,\ldots,A_{q-1})\) and construct its block Green kernel.

For local indices \(i<j\), both routes yield the same ordered product

\[
A_{p+i}A_{p+i+1}\cdots A_{p+j-1}.
\]

Hence the Beck–Chevalley comparison is identity and therefore invertible.

## Pasting

For nested intervals \([r,s]\subseteq[p,q]\), principal block compression composes strictly. The direct comparison and the pasted pair of comparisons are the same identity cell.

## Gauge compatibility

A compatible orthogonal vertex gauge restricts blockwise to every interval. Since block compression commutes with the block-diagonal gauge, the Beck–Chevalley identity cell is natural with respect to the gauge companions and conjoints.

## Hostile boundary

A noncontiguous subset can have the same number of retained vertices as a contiguous interval but omits intermediate path transfers. Its compressed cross block is a multi-edge product, whereas constructing a chain from only adjacent retained labels requires an independently supplied effective transfer. Equal dimension does not identify these constructions.

## Disposition

Invertible contiguous Beck–Chevalley and strict nested pasting extend to fixed-fiber noncommutative Markov kernels and are compatible with orthogonal gauge correspondences. General pullback/amalgamation Beck–Chevalley remains open.

## Verification

- `research/voevodsky/checkers/check_operator_valued_contiguous_beck_chevalley.py`
- `research/voevodsky/results/operator_valued_contiguous_beck_chevalley.json`
