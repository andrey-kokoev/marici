# Global oriented relative realization of common-tree complexes

The local shedding block `T,T'` cancels its shared ridge after the unique incidence-sign correction. These local signs glue globally.

For each nonempty common-tree complex choose one facet sign and propagate signs across the connected dual flip graph by requiring opposite total incidence on every shared ridge. Consistency around every flip cycle is the orientability condition. The resulting top chain

\[
[K]_{rel}=\sum_T \epsilon_T[T]
\]

satisfies

\[
\partial[K]_{rel}=\sum_{R\text{ free}}\epsilon_R[R],
\]

because every internal ridge has two incident facets whose coefficients cancel.

Thus:

- in the full associahedral case there are no free ridges and `[K]rel` is an absolute fundamental cycle;
- in every proper case `[K]rel` is a relative fundamental chain whose boundary is supported exactly on free ridges.

`check_double_partial_nine_point_orientation_coherence.py` exhausts all 20,160 nine-point order orbits. Among the 4,279 nonempty complexes:

- all 4,279 admit a coherent global facet orientation;
- every internal ridge cancels;
- one closed complex yields an absolute cycle;
- 4,278 proper complexes yield relative chains with nonzero free-ridge boundary;
- no orientation holonomy occurs around any flip cycle.

This upgrades the local Hadamard correspondence to a global simplicial relation. Edges carry signed flip pairings, triangles enforce common-ridge cancellation, and cycle consistency of these triangular signs is the tetrahedral/octahedral coherence condition. A target realization functor only needs to preserve this boundary relation to send the global relative chain to the analytical difference row.
