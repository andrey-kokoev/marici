---
author: marici.Benincasa
---

# 1499 — The Boundary Kernel Pushes Forward to a Rank-One Contour Statistical Propagator

## Status

Primary-source comparison between the quadratic initial action and its
resummed propagator. The frozen source is Collins, arXiv:1309.2656v1,
Sec. II, especially the propagator formula following the boundary-insertion
resummation.

## Source propagator theorem

For the general translationally and rotationally invariant quadratic initial
action with kernels \((A_k,B_k)\), the source derives

\[
\boxed{
G_k^{ab}(t,t')
=G_{k,\mathrm{vac}}^{ab}(t,t')
+\Delta G_k(t,t'),
\qquad a,b\in\{+,-\}.
}
\]

The same state-dependent correction \(\Delta G_k\) occurs in all four
contour components. Its exact rational expression depends on
\(A_k,A_k^*,B_k\) and the equal-time vacuum propagator.

## Contour rank

In the ordered contour basis \((+,-)\), the correction is

\[
\Delta\mathbf G_k
=\Delta G_k
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}.
\]

Therefore

\[
\boxed{
\operatorname{rank}_{\rm contour}\Delta\mathbf G_k=1
}
\]

whenever \(\Delta G_k\neq0\). Its image is the deck-invariant line
\(\langle(1,1)\rangle\).

## Keldysh projection

With

\[
\phi_c=\frac12(\phi_++\phi_-),
\qquad
\phi_q=\phi_+-\phi_-,
\]

the common correction contributes only to the \(cc\) component:

\[
\boxed{
\Delta G_{cc}=\Delta G_k,
\qquad
\Delta G_{cq}=\Delta G_{qc}=\Delta G_{qq}=0
}
\]

up to the conventional normalization of the statistical propagator.

Thus the general quadratic initial state modifies the statistical/Keldysh
propagator while leaving the retarded, advanced, and commutator sectors
unchanged.

## Relation to the two boundary eigenchannels

Entry 1497 found two canonical action-level kernels

\[
K_{\rm diag}=A_I+B,
\qquad
K_{\rm anti}=A_I-B.
\]

The propagator is obtained by inversion and resummation of the doubled
quadratic form. Both source kernels can enter the scalar function
\(\Delta G_k\), but their contour occurrence matrix has only the invariant
rank-one image.

Therefore:

\[
\boxed{
\text{two action-level deck eigenchannels}
\xrightarrow{\text{Gaussian pushforward}}
\text{one contour-statistical propagator line}.
}
\]

This is a pushforward statement, not an equality or canonical identification
of the two input kernels.

## Parameter-rank qualification

Rank one refers only to contour occurrence space. The scalar bilocal function
\(\Delta G_k(t,t')\) retains several independent time structures and can
depend on all three real functions \(\Re A_k,\Im A_k,B_k\). No claim of a
one-parameter state is made.

## Architectural consequence

The exact map separates coefficient complexity from physical readout rank:

\[
\text{rich doubled boundary coefficient object}
\longrightarrow
\text{rank-one statistical contour readout}.
\]

This strengthens Entries 1470 and 1481: state-dependent propagation is
statistical, while the causal spectral kernel is source-independent. The
existing doubled carrier and Gaussian pushforward suffice; no new carrier
stratum appears.

## Next falsifier

Compose Entry 1494's one-loop cubic-to-quadratic map with this Gaussian
pushforward. Test whether the generated \((A_I,B)\) correction is visible in
\(\Delta G_k\) or lies in a kernel of the propagator readout at the published
divergent order.

## Provenance

- Collins, arXiv:1309.2656v1, Sec. II;
- Entries 1470, 1481, 1494, and 1497;
- allocator claim `seqclaim-dee0c802926b04b03db66865`.
- epistemic event `ev-000000001622-4e45839b-28d7-4125-9902-33279d81c829`.
