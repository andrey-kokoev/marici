# Weighted completion gate for crystal seam support

Date: 2026-09-08

## Question

Which existing Marici estimate is strong enough to remove the generic cutoff leakage before applying seam localization?

## Conditional bridge

The weighted completion theorem in `reciprocal-orbit-weighted-completion.md` supplies the required estimate on a fixed reciprocal orbit.  If every matrix coefficient of the generic comparison leakage has a tail presentation

\[
L_N(z)=\sum_{r\notin F_N}c_rH(r)^{-z}
\]

with

\[
\sum_r |c_r|H(r)^\epsilon<\infty
\]

and the orbit `K_w={sw:s∈[-1,1]}` satisfies `|Re(w)|<epsilon`, then

\[
\sup_{z\in K_w}\|L_N(z)\|
\leq
\sum_{r\notin F_N}\|c_r\|H(r)^\epsilon
\longrightarrow0.
\]

This is operator-norm tail control on the fixed finite packet, not merely strong convergence of projections.  It therefore removes the generic leakage in the completed evaluation graph.

Let `C_N` be the comparison cone and separate it as

\[
C_N\simeq G_N\oplus B_N,
\]

where `G_N` is the generic approximation tail and `B_N` is the independently typed seam/polar residual.  Under the weighted estimate, `G_N→0` in the completed graph norm.  If `B_N` converges and its restriction to `X\setminus Z` is zero, the completed cone is supported on `Z` and becomes eligible for crystal Kashiwara localization.

## Quantifier boundary

The estimate is only for each fixed reciprocal orbit strictly inside a supplied decay strip.  It does not provide one cutoff valid uniformly over all orbits, all spectral widths, or a moving family of diagnostic projections.  The order is

\[
\forall K_w\Subset\{|\operatorname{Re}z|<\epsilon\}\;
\forall\delta>0\;
\exists N(K_w,\delta)
\]

such that the generic tail is below `delta`.  No interchange with a supremum over `w` is authorized.

## First missing source theorem

For the RH packet one must prove that the actual plus/minus comparison leakage admits the displayed coefficient expansion with a common positive `epsilon`. Gaussian theta decay plausibly controls the archimedean Poisson channel. The raw primitive Euler channel with weight `p^{-1/2}` is not absolutely summable, but the already derived mixed primitive--square Adams block has weight

\[
w_p(\sigma)=\frac12p^{-3/2-\sigma}
\]

and polylogarithmic packet growth, hence is absolutely Green-summable uniformly through the seam. Analytic continuation alone would not supply this estimate; the mixed source weight does.

Consequently the completion route splits:

1. **Archimedean channel:** use the direct Gaussian weighted-tail bound.
2. **Renormalized mixed Euler channel:** use the uniform majorant `p^{-3/2}(1+(log p)^2)` after proving that this packet is the source-authorized Adams edge.
3. **Raw primitive self-channel:** keep it out of the absolutely summable block or supply a separate relative renormalization.
4. **Boundary channel:** retain endpoint/polar terms outside the vanishing generic-tail object.

## Falsifier

The existing weighted-completion deliberate failure takes coefficients `c_n=n^-4`, source exponent `2`, and orbit width `3`.  The evaluated tail is harmonic and every dyadic block is at least `1/2`.  Thus failure of the strict strip inequality produces a nonvanishing generic residual and blocks seam localization.

## Disposition

A valid conditional arrow now exists:

\[
\text{weighted source decay}
\Longrightarrow
\text{generic leakage vanishes in graph completion}
\Longrightarrow
\text{support test reduces to the retained boundary residual}.
\]

The analytic premise is available for the renormalized mixed Euler packet, but its source typing as the authorized Adams comparison edge remains unproved. The DAG/crystal proposal is therefore deferred at that typing and support gate rather than at Euler summability itself.

## Verification

- `research/voevodsky/reciprocal-orbit-weighted-completion.md`
- `research/voevodsky/checkers/check_reciprocal_orbit_weighted_completion.py`
- `research/voevodsky/results/reciprocal_orbit_weighted_completion.json`
- `research/nima/fixed-diagnostic-leakage-converges-without-uniform-strictification.md`
- `research/nima/checkers/check_fixed_vs_uniform_leakage.py`
- `research/nima/euler-half-density-weights-make-the-renormalized-prime-assembly-absolutely-green-summable.md`
