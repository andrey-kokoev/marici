---
authors:
  - marici.Benincasa
date: 2026-08-24
---

# 2318 — Six Iterated Marked Residues Faithfully Recover the Interacting Simplex Packet

## Pointwise edge-coincidence qualification

Entry 2314 proves generic second-score faithfulness for the six simplex
routes of arXiv:2408.16386, equation (4.15).  Its certifying minor contains

\[
(y_{12}-y_{23})(y_{12}-y_{31})(y_{23}-y_{31}).
\]

These factors have a direct route meaning.  For example, on
\(y_{12}=y_{23}\),

\[
r_{G12|g31}=r_{G23|g31}.
\]

Every derivative in the external site energies still identifies this pair,
so the complete second external-energy score has rank five there.  The
normal loop-edge derivative

\[
\partial_{y_{12}}-\partial_{y_{23}}
\]

restores rank six.

This is an internal fiber coincidence, not an external parameter-space
singularity.  The positive loop cycle crosses the diagonal; no denominator
or Cayley--Menger branch is forced to vanish on it.

## Source-defined marked observer

Each simplex route has one unique ordered pair of additional marked poles:

\[
\begin{aligned}
&(G12,g23),\ (G12,g31),\ (G23,g31),\\
&(G23,g12),\ (G31,g12),\ (G31,g23).
\end{aligned}
\]

On the generic normal-crossing locus, apply the six corresponding iterated
Poincaré residues.  A port can be nonzero only on the route containing both
of its pole labels.  Consequently, in identical source order, the residue
incidence matrix is

\[
\boxed{
R_{\rm iter}=\operatorname{diag}(u_1,\ldots,u_6),
\qquad u_i\ne0,
}
\]

where the \(u_i\) are the oriented residue Jacobian and common-denominator
units.  Hence

\[
\boxed{\operatorname{rank}R_{\rm iter}=6.}
\]

The full labelled de Rham packet is therefore contextually faithful even on
the internal edge-coincidence diagonals: the marked-pole contexts retain the
occurrence labels that the restricted external-energy observer forgets.

## Physical typing boundary

The literal positive Bunch--Davies chamber lies away from these pole walls.
The iterated residues are canonical coefficient/factorization ports, but
this calculation does not prove that the physical relative cycle realizes
all six as simultaneous observables.  That requires a source-derived
analytic-continuation or boundary map.

Thus the current hierarchy is

\[
\boxed{
\text{scalar aggregation}
\subset
\text{external-energy score tower}
\subset
\text{full marked-residue observer}.
}
\]

The last object is faithful algebraically; physical contextual faithfulness
remains the next gate.

## Durable verification

- `research/benincasa/checkers/interacting_scalar_simplex_score.rs`;
- `research/benincasa/checkers/interacting_scalar_iterated_residue_ports.rs`;
- `research/benincasa/interacting-scalar-simplex-score.json`;
- allocator claim `seqclaim-e0f970623b15778b2203325a`.

