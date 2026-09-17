# Full `esd_7(Delta^3)` graded Tate-torus realization

Using the generated source manifest, the Tate-torus construction extends from the rank-four skeleton to every nondegenerate cell of the seventh edgewise subdivision under the maximal all-cells designation profile.

## Assignment

For each labelled simplex `sigma`, assign

\[
\mathfrak R(\sigma)=N_*\mathbb C[\sigma]\widehat\otimes V,
\]

where `V` is the channel-lattice distribution complex in even charts and its Pontryagin-dual trigonometric complex in odd charts.

Face maps are signed normalized-chain inclusions tensored with the identity. For the source-recorded Freudenthal monotone flag of each triangle, use its canonical mapping-cone triangle. For the source-recorded three-stage increment flag of each tetrahedron, use the canonical octahedron of composable inclusions.

The chart successor combines:

1. the manifest permutation `rho` on simplex and channel labels;
2. Pontryagin Fourier transform on `V`;
3. a homological shift at the phase-four wrap.

Therefore

\[
\widetilde{\mathcal F}^{\,4}=\Sigma.
\]

Reciprocity combines the manifest reversal `omega`, lattice reflection, and derived duality.

## Mechanical verification

`check_full_esd7_tate_torus_functor.py` checks all

\[
120+560+784+343=1807
\]

nondegenerate cells. It finds:

- zero failures of signed `rho` chain naturality;
- zero failures of signed `omega` chain naturality;
- all 784 designated triangles admit the flag-cone model;
- all 343 designated tetrahedra have the required four oriented triangular faces.

The cone and octahedron identities then hold formally in the derived target.

## Claim boundary

This is a nonzero exact realization for the explicit maximal profile in `esd7-source-manifest.json`. If the intended universal category later declares only a proper subset of quotient cells, this realization restricts to it automatically. If it declares additional zero vertices or different orientation signs, those declarations must be compared separately.

The statement that each of four charts has weight `1/4` refers to the finite source/chart multiplicity

\[
\frac{1807}{4\cdot1807}=\frac14
\]

(or to the Catalan-basis enlargement degreewise). It is not a normalized operator trace on the infinite-dimensional distribution target unless a separate trace-class regularization is chosen.
