# Adjacent swaps give the proper Catalan extremizer candidate

Let

\[
\alpha=(\ldots,x,a,b,y,\ldots),\qquad
\beta=(\ldots,x,b,a,y,\ldots)
\]

be cyclic orders differing by one adjacent transposition, with at least two other labels.

## Proposition

A cubic tree is planar in both orders if and only if it contains the channel separating the pair `{a,b}` from the remaining labels. Consequently

\[
|K(\alpha,\beta)|=C_{n-3}.
\]

## Proof

The four labels `x,a,b,y` occur in opposite local orders. Any planar binary refinement that does not first combine `a` and `b` separates one of them from the other by a channel whose two sides interleave in one of the two cyclic orders. Such a channel cannot be planar in both. Therefore a common tree must contain the split

\[
\{a,b\}\mid [n]\setminus\{a,b\}.
\]

Conversely, after cutting along this split, the two-point side has a unique cubic completion. Contract it to one effective label. The induced cyclic orders on the remaining `(n-1)` labels agree. Every triangulation of that polygon therefore glues to a common tree, and cut/glue is inverse to contraction.

The number of triangulations of an `(n-1)`-gon is

\[
C_{(n-1)-2}=C_{n-3}.
\]

## Extremal conjecture

The exhaustive census through `n=9` and structured dynamic-programming tests through `n=33` support

\[
\alpha\not\sim_{D_n}\beta
\quad\Longrightarrow\quad
|K(\alpha,\beta)|\le C_{n-3}.
\]

Equality is attained by an adjacent transposition and its dihedral relabellings. The asymptotic proper/full density ratio is

\[
\frac{C_{n-3}}{C_{n-2}}\longrightarrow\frac14.
\]

The proposition proves attainability, not the universal upper bound. A proof of the bound likely requires a compression/injection sending common triangulations for an arbitrary non-dihedral permutation into triangulations containing one fixed short channel, with equality forcing the adjacent-swap pattern.
