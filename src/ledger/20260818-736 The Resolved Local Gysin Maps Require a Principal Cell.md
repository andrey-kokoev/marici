---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 736 — The Resolved Local Gysin Maps Require a Principal Cell

## Frozen map problem

Entries 729–734 require exact local maps for the resolved coefficient Čech
complex.  At a simple crossing the exceptional residue is meromorphic at one
incident endpoint, so direct evaluation of its (L_1)-kernel is undefined.
The source-derived replacement is the double-residue indicial complex.

## Homogeneous resonance columns

For every simple and weighted incidence, let (K_i=\ker L_1(R_i)).  In the
common extension-coordinate order ((00,01,10,11)), the corner operator on
the homogeneous resonance directions is

\[
L_0(C)\big|_{K_i}=0.
\]

Thus all exported homogeneous maps vanish:

\[
\boxed{K_i\longrightarrow E_{ij}\text{ is zero at first corner grade}.}
\]

This is basis-independent.  It is not permission to delete the local
coefficient complexes.

## Principal-cell boundary

The nonzero corner residue lies entirely in the inhomogeneous extension block
(C_E).  Therefore the typed source is the augmented object

\[
\widetilde K_i=K_i\oplus\mathbbm1_{\rm principal},
\]

and the local map is

\[
(X,c)\longmapsto c\,C_E.
\]

In source order ((k_1,k_2,1)), every matrix has two zero columns and one
principal column.

Over (K_{12}=\mathbb Q(\sqrt{-3})), the (D_1) map is zero and the oriented
(D_2) principal column is

\[
\begin{pmatrix}
-3\\
\frac12+\frac16\sqrt{-3}\\
\frac32-\frac32\sqrt{-3}\\
-\frac12+\frac16\sqrt{-3}
\end{pmatrix}.
\]

Over (K_{13}=\mathbb Q(\sqrt5)), the (D_1) map is zero and the oriented
(D_3) principal column is

\[
\begin{pmatrix}
-2+\sqrt5\\
\frac32+\frac7{10}\sqrt5\\
-\frac{11}2+\frac52\sqrt5\\
\frac12+\frac3{10}\sqrt5
\end{pmatrix}.
\]

The conjugate geometric points are obtained by the stated Galois involutions;
no independent bases are chosen there.

## Weighted rational edge

The full nonresonant (E_{23}) is retained.  Before trace, both oriented
endpoint maps have principal column

\[
\begin{pmatrix}0&-\frac14&0&\frac34\end{pmatrix}^{T}.
\]

The transformed lattice is (mu_2)-even.  The unnormalized finite trace
therefore gives

\[
\boxed{
\begin{pmatrix}0&-\frac12&0&\frac32\end{pmatrix}^{T}.
}
\]

No resonant (e_{23}) generator is introduced.

## Typing consequence for Entry 734

The (V_i) in the coefficient differential cannot be replaced by their
two-dimensional homogeneous resonance spaces.  The local comparison is a
map of labelled augmented complexes, and the principal cell carries all
first-corner incidence information.

This entry stops before assembling or interpreting the global cokernel.

## Evidence

- exact modular corner derivation:
  `research/benincasa/gysin_ordinary_crossing_blowup.py` and
  `research/benincasa/gysin_weighted_crossing_blowup.py`;
- exact quadratic/rational lifts:
  `research/benincasa/lift_gysin_corner_maps.py` and
  `research/benincasa/lift_gysin_weighted_maps.py`;
- machine-readable packet:
  `research/benincasa/marici-gm/gysin-resolved-local-maps.packet`;
- Rust certificate:
  `research/benincasa/marici-gm/src/bin/gysin_resolved_local_maps_certificate.rs`;
- the Rust certificate uses Symbolica 2.2 with its pure-Rust `no_gmp`
  backend to verify the exact identities and involutions;
- allocator claim `seqclaim-97d78d511178c63fd80d4026`.
- epistemic event
  `ev-000000000352-4ab101fb-264b-4ba4-8c1b-71f5e5185b2a`.

## Next falsifier

Replace Entry 734's vector-space placeholders by the augmented local
complexes and verify that the principal-cell maps commute with both Galois
involutions, the two chart transitions, and independent basis changes.  Only
then form the four character blocks.
