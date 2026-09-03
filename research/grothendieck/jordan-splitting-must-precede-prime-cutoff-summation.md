# Jordan splitting must precede prime-cutoff summation

## Defect in the first finite-cutoff proposal

For the prime adjacency sum

\[
T_N=\sum_{n\le N}q_nJ_n,
\]

taking the canonical operator parts `T_N^+` and `T_N^-` does not produce feature spaces nested under `N -> N+1`. Even for commuting self-adjoint multipliers, adding one summand moves the sign-change locus of the total multiplier. A vector can belong to the positive spectral subspace at cutoff `N` and the negative subspace at cutoff `N+1`.

The scalar fixture already shows the issue: the positive part of `1` is `1`, while after adding `-2` the positive part of the sum is zero and the negative part is `1`. Canonical Jordan decomposition is not additive or covariant under source refinement.

## Provenance-preserving repair

Each labelled paired translation adjacency

\[
J_n=\frac{U_{\log n}+U_{-\log n}}2
\]

has source-fixed positive and negative functional-calculus parts

\[
J_n=J_n^+-J_n^-.
\]

Define prime feature rows by labelled direct sums:

\[
A_{\mathbb P,N}
=
\bigoplus_{n\le N}
\sqrt{q_n}(J_n^+)^{1/2},
\]

\[
B_{\mathbb P,N}
=
\bigoplus_{n\le N}
\sqrt{q_n}(J_n^-)^{1/2}.
\]

Cutoff extension now appends coordinates. The embeddings are isometric and compose exactly. The difference of squared norms still equals the finite prime quadratic form.

At fixed Gaussian width, the labelled log-Gaussian weights make the source sums convergent. The infinite row operators can therefore be defined by completion of the nested labelled direct sums, subject to the declared norm domain.

## Cost of the repair

The termwise split is larger than the minimal Jordan decomposition of the total prime operator. That redundancy is necessary for provenance: it remembers which prime identity generated each positive and negative feature. The meta-observers can now compare features across cutoffs without sign subspaces mutating underneath them.

The repair does not construct the contraction from the total negative row to the total positive row. It only makes the contraction question functorial.

## Disposition

Withdraw cutoff compatibility for positive and negative parts of the summed prime operator. Use labelled termwise Jordan channels before summation. The next contraction must act on these nested provenance-preserving rows and may use cross-label and cross-sector identities; a diagonal contraction prime by prime is neither expected nor sufficient.
