# The canonical observation section collapses the four-pair quadratic coordinate

## Question

Does the simplest general-target section `C0=[Y Z_{1..6}^{-1}|0|0]` allow the previous kernel-area `q=det T` algorithm to produce a global rational two-sheet target form? Is the traced coefficient otherwise independent of the section chosen in the linear fibre?

## Exact obstruction and repair

Let `K Z=0` be a rank-two right kernel and write the fibre as `C=C0+T K`, with `T` two-by-two. In the canonical first-six-column section, columns 7 and 8 of `C0` vanish identically. Their paired minor therefore becomes

    Δ_78(C0+T K)=det(T) det(K_{7,8})=q det(K_{7,8}).

For generic `Z`, `det(K_{7,8})≠0`. On the four-pair cell `Δ_78=0`, BOTH physical algebraic sheets have `q=0`. The four linearized pair constraints do NOT have a rank-four coefficient matrix; a direct first-six-column canonical section destroys the separating quadratic coordinate. This is an algorithmic degeneracy, NOT a degeneration of the cell or a single-sheet proof. The first version of the checker failed on precisely this rank test and was repaired rather than suppressing it.

For a kernel shift `C0'=C0+S K`, the same fibre is parameterized by `T'=T-S`. If `S=[[p,r],[v,t]]` and `T=[[a,b],[c,d]]`, then

    q'=q-a*t-p*d+b*v+r*c+det(S).

This identity holds symbolically. A generic rational shift restores a usable separating `q'`; it does not alter `C`, `Y`, the intrinsic source dlog form or the target density on each physical sheet. At TWO distinct positive rational nine-point targets, the checker uses THREE admissible rational sections each (the source cell section and two generic shifts of the canonical section). Their quadratic polynomials differ, but the reconstructed unordered pair of source matrices and the exact full two-sheet target coefficient both agree with the prior frozen traces. The unshifted canonical section is deliberately not used as an admissible coordinate.

## Disposition

Global-target elimination must specify a GENERIC transversal source-fibre section and show its polynomial coefficient determinants do not vanish on the intended open set. It cannot reuse the canonical first-six observation section with `q=det T` without a different elimination variable. These exact identities and two checks do not compute the global rank-six bosonic target-form numerator, prove regularity at source `Y0`, or establish a nine-point history assignment.

Checker: `research/nima/checkers/check_nine_point_trace_section_covariance.py`; result: `research/nima/results/nine-point-trace-section-covariance.json`.
