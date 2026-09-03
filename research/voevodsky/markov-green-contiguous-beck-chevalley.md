# Contiguous Beck–Chevalley cells for scalar Markov Green chains

## Question

Does the scalar Markov Green fragment admit an analytic Beck–Chevalley cell relating path-product completion and restriction to contiguous subchains?

## Claim boundary

This packet treats order-preserving contiguous interval inclusions in a scalar Markov chain. It does not prove Beck–Chevalley for arbitrary pullbacks, noncontiguous probes, gauge quotients, or operator-valued kernels.

## Reindexing constructor

Let \(G(a_1,\ldots,a_n)\) be the path-product Gram certificate. For a contiguous vertex interval \([p,q]\), restriction takes the principal submatrix on vertices \(p,\ldots,q\). Entrywise,

\[
G_{ij}=
\prod_{k=i}^{j-1}a_k,
\qquad p\le i<j\le q,
\]

so the restricted matrix is exactly

\[
G(a_{p+1},\ldots,a_q)
\]

after reindexing the vertices from zero. Thus completion commutes strictly with contiguous restriction.

## Beck–Chevalley square

Suppose two certified segments meet at one normalized vertex and concatenate to a longer chain. Let a target contiguous interval cross the seam. There are two routes:

1. concatenate the full segments, complete by path products, then restrict;
2. restrict each segment to the portions meeting the target interval, concatenate those portions at the same seam, then complete.

Both routes retain the same ordered edge sublist. Their full Gram matrices, determinant witnesses, and interface labels agree. The Beck–Chevalley cell is the identity isometry and is invertible.

## Pasting

Nested contiguous restrictions correspond to nested edge slices. Slicing first to \([p,q]\) and then to \([r,s]\subseteq[p,q]\) equals direct slicing to \([r,s]\). Hence pasted Beck–Chevalley identity cells agree strictly.

## Hostile test

A route that changes the seam label or uses a noncontiguous vertex selection does not satisfy this constructor's admission predicate. Equality of resulting dimensions is insufficient; no Beck–Chevalley cell is emitted.

## Disposition

The scalar Markov Green fragment now instantiates invertible Beck–Chevalley cells and their strict pasting law for contiguous restrictions. General pullback/amalgamation Beck–Chevalley remains open.

## Verification

- `research/voevodsky/checkers/check_markov_green_contiguous_beck_chevalley.py`
- `research/voevodsky/results/markov_green_contiguous_beck_chevalley.json`
