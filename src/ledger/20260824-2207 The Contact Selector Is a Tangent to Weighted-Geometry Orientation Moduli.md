---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2207 — The Contact Selector Is a Tangent to Weighted-Geometry Orientation Moduli

## Retyping the normal direction

Entry 2206 identifies the source of the subdivision coefficients: they are
the unique Boolean pullback of cell-orientation parity. The formal edge
weights used in Entries 2197 and 2204 therefore deform the relative weights
of an overlapping weighted-positive-geometry presentation.

For each labelled edge \(e\), varying its singleton/final-edge weight changes
exactly the four resolved cells containing \(e\). These three tangent vectors
are independent and cyclically permuted. They define a rank-three tangent
space in the moduli of weighted orientations.

The contact conormal response is consequently typed as

\[
\boxed{
K_{\rm ct}
\longrightarrow
T^*_{w_{\rm phys}}\mathcal W_{\rm orient},
}

where \(\mathcal W_{\rm orient}\) denotes the local space of relative weight
assignments on the frozen subdivision.

## What has improved

The target is no longer an invented deletion-fugacity space or hypothetical
ancilla score space. It is a genuine geometric deformation space discussed
by the source when varying relative weights of weighted polytopes.

The source still singles out the physical weight by the orientation-changing
construction and does not interpret nearby weights as physical cosmologies.
Thus the selector is a geometric susceptibility, not yet a physical response.

The next test is comparison invariance: transport this tangent/conormal class
through a second source-derived subdivision of the same weighted geometry.
If it agrees, it belongs to the weighted geometry; if not, it remains tied to
the Boolean cover.

## Evidence

- Entries 2197 and 2205–2206
- Benincasa–Dian discussion of variable relative weights following the
  weighted-triangle adjoint conditions
- `research/benincasa/checkers/orientation_moduli_conormal.rs`

