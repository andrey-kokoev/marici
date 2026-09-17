# Four chart projections are not four fixed forced-channel sectors

A direct Cech model using four pairwise-compatible fixed ear channels can be counted exactly. Each single ear sector has `C_(n-3)` facets. Intersections of `k` selected compatible ear sectors contract `k` ears and have `C_(n-2-k)` facets. Hence

\[
\left|\bigcup_{i=1}^4E_i\right|
=4C_{n-3}-6C_{n-4}+4C_{n-5}-C_{n-6}.
\]

After normalization by `C_(n-2)`, this tends to

\[
1-\binom42\frac1{4^2}+\binom43\frac1{4^3}-\frac1{4^4}
=1-\left(\frac34\right)^4
=\frac{175}{256}.
\]

Thus the uncovered fraction tends to `81/256`, not zero. At `n=33`, four such charts cover about `0.70349`; at `n=100`, about `0.69000`.

Therefore the four realization charts cannot be diagonal projections onto four fixed ear/adjacent-swap submodules. The chart operation must rotate the full presentation, and its sector projections must generally be non-diagonal in the triangulation basis.

The correct candidate is the order-four representation itself. If an operator `q` acts on the realized Catalan module with `q^4=1` (or suspension after stable regrading), its character projectors are

\[
P_j=\frac14\sum_{k=0}^3 i^{-jk}q^k.
\]

Their normalized traces tend to `1/4` whenever the normalized traces of `q`, `q^2`, and `q^3` tend to zero. This gives an analytic criterion for the quarter-limit that does not identify chart sectors with fixed channels.

The next test is therefore to construct the finite-degree chart operator and measure its three nontrivial normalized character traces, rather than combining four ear projections.
