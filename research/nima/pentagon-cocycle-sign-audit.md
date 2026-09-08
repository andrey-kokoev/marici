# Pentagon increment and contraction audit

## Question

Does the oriented five-flip relation used in the local-factorization converse have exactly the simplex coboundary signs?

## Claim boundary

The checker handles six labelled pentagons on six ordered vertices and formal independent triangle weights over the integers. It does not verify source coefficients or context independence of arbitrary functions.

For a<b<c<d, define g_abcd as the increment replacing diagonal ac by bd. Triangle additivity gives

\[
g_{abcd}=h_{bcd}-h_{acd}+h_{abd}-h_{abc}= (\delta h)_{abcd}.
\]

For a<b<c<d<e the oriented pentagon cycle is, up to the choice of traversal direction,

\[
g_{bcde}-g_{acde}+g_{abde}-g_{abce}+g_{abcd}=0.
\]

Enumerating the five triangulations and their adjacency on each of six pentagons returns precisely this alternating vector, with overall sign -1 for the chosen traversal. Reversing a single increment leaves four formal triangle coefficients of magnitude two. This deliberately corrupted identity is nonzero over the integers, but cannot detect sign reversal in characteristic two.

For a closed g fix root 0. Define h_ijk=g_0ijk away from the root and h_0ij=0. The cocycle equation on (0,i,j,k,l) gives delta h=g; root-containing quadruples give the same identity directly. This is a division-free contraction. The checker verifies it on all fifteen quadruples using formal triangle cochains. The closed-cochain argument, rather than this exact-input test alone, proves it for arbitrary closed g.

## Disposition

The pentagon sign and contraction edges of the converse are verified. The remaining independent audit is context independence: facet separability must make flip increments insensitive to changes in surrounding triangulations. No source-embedding promotion follows.
