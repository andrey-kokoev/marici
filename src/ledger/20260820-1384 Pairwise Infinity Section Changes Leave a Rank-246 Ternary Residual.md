# 1384 — Pairwise Infinity Section Changes Leave a Rank-246 Ternary Residual

## Status

Replicated one-characteristic modular result at \((p,z)=(1019,7)\) and \((1019,13)\). Characteristic-zero certification remains open.

## Correctly typed direction spaces

Let

\[
K=\ker A
\]

be the homogeneous direction space of the cubic affine primitive system. At both maximal-rank fibers,

\[
\dim K=769.
\]

For the representative occurrence triple \((1,2,3)\), define

\[
T_{ij}
=
K\cap\ker B_{ij},
\]

where \(B_{ij}\) imposes the boundary-zero conditions on occurrence orbits \(i\) and \(j\).

The three dimensions are

\[
\dim T_{12}=152,
\qquad
\dim T_{13}=152,
\qquad
\dim T_{23}=219.
\]

These agree with the pairwise trivialization dimensions from Entry 1364.

## Sum of pairwise section changes

Exact finite-field nullspace bases were constructed from one common labelled matrix and concatenated.

At both tested maximal-rank fibers,

\[
\operatorname{rank}
\left(
T_{12}+T_{13}+T_{23}
\right)
=
523.
\]

But

\[
152+152+219=523.
\]

Therefore

\[
\boxed{
T_{12}\oplus T_{13}\oplus T_{23}
\hookrightarrow K
}
\]

is a direct sum at the tested fibers.

The residual quotient has dimension

\[
\boxed{
\dim
\frac{K}{T_{12}+T_{13}+T_{23}}
=
769-523
=
246.
}
\]

## Interpretation

The pairwise section-change directions do not overlap and do not exhaust the affine kernel.

Thus the ternary incompatibility found in Entry 1379 survives after all independently available pairwise gauge changes are retained.

The replicated modular architecture is

\[
\boxed{
0
\longrightarrow
T_{12}\oplus T_{13}\oplus T_{23}
\longrightarrow
K
\longrightarrow
R_{123}^{(246)}
\longrightarrow
0.
}
\]

## Prohibited inference

The number \(246\) is not yet:

- a physical state count;
- a period rank;
- a characteristic-zero Čech cohomology dimension;
- evidence for a new carrier cell.

It is the dimension of a modular linear quotient in the frozen cubic ansatz.

The inhomogeneous triple class must still be shown to have a nonzero image in the appropriate comparison cone built from these spaces.

## Next finite falsifier

Construct the induced boundary map on

\[
R_{123}
=
K/(T_{12}\oplus T_{13}\oplus T_{23})
\]

and test whether the inhomogeneous triple datum defines a nonzero cokernel class there.

Then repeat over a second characteristic or reconstruct the relevant minors in characteristic zero.

If the inhomogeneous class dies after the full comparison differential is included, the rank-246 quotient is only unused gauge geometry, not the ternary obstruction object.

## Artifacts

- `research/benincasa/results/five-site-asymmetric-pair-torsor-residual.json`
- `research/benincasa/results/five-site-asymmetric-kummer-resolved-ibp-pilot.json`
- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_kummer_resolved_ibp_pilot.rs`

Allocator claim: `seqclaim-5bd5c59b19ffebfe46b91705`.
