# Commutator-gradient selector audit (WP260)

## Candidate geometry

Promote the down-sector Gram matrix to a candidate dynamical flavon variable
and consider the full weak-basis-invariant commutator energy

\[
V(H_u,H_d)=\frac12\lVert[H_u,H_d]\rVert_{\mathrm{HS}}^2.
\]

With \(H_u\) held fixed, its negative gradient flow is

\[
\frac{dH_d}{dt}=-[H_u,[H_u,H_d]].
\]

In the spectral frame of \(H_u\), each matrix element evolves as

\[
(H_d)_{ij}(t)=e^{-(\lambda_i-\lambda_j)^2t}(H_d)_{ij}(0).
\]

The construction is equivariant under simultaneous weak-basis conjugation and
therefore descends to `physical16`. Its Schur kernel is positive, so it gives a
positive dephasing semigroup on the Gram matrix.

## Finite-time obstruction

Every coefficient is strictly positive at finite time. Consequently the
linear map on the ambient Hermitian space has nonzero determinant and is
invertible. The exact checker uses
eigenvalues \((0,1,2)\) at \(t=\log 2\), verifies positivity through all
principal minors, and proves exact semigroup composition. The commutator
energy decreases strictly, but the contextual partition is unchanged. This
does not claim that the inverse preserves the positive cone globally; it proves
the narrower selector gate relevant here: no finite-time dimension reduction,
proper subspace, or distinguished point is produced.

Thus finite dissipative-looking evolution is still transport, not selection.
The proper image appears only as \(t\) tends to infinity, where the channel
becomes spectral pinching and selects

\[
[H_u,H_d]=0.
\]

That limit is not a finite executable operation. It also predicts trivial CKM
mixing and vanishing CP violation, contrary to the admitted flavor record.

## Classification

The flow is a weak-basis-descending positive finite-time transport, neither a
selector nor a rigidifier. Its infinite-time limit is a mathematical selector
with two independent failures: no source-derived finite stopping and
stabilization instrument, and an empirically false fixed locus.

The first nonfaithful arrow is the passage from finite executable evolution to
the infinite-time pinching limit. A progressive successor must derive a
dynamical flavon substrate and a finite stabilization law with a nontrivial
mixing fixed locus before inspecting flavor data.

Run `uv run --with sympy python
research/flavor/checkers/wp260_commutator_gradient_selector.py` for exact
descent, positivity, semigroup, determinant, energy, and hostile-limit checks.
