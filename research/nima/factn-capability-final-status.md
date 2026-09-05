# Polygon-factorization capability: final status

## Constructed

1. A generic finite-poset simplicial nerve whose degree-`k` simplices are weak
   chains, with faces, degeneracies, exhaustive simplicial-identity checks,
   Segal bijections, and Rezk completeness for antisymmetric orders.
2. Generic convex-`n`-gon diagonals, crossing, noncrossing dissections, region
   splitting, regional restriction, and union.
3. An unbounded mathematical proof that restriction and union give the
   refinement-order isomorphism
   \[
   \operatorname{Face}(D)\simeq
   \prod_{R\in\operatorname{Regions}(D)}\operatorname{Fact}(R),
   \]
   including nested-cut naturality.
4. Generic formal planar amplitudes as sums of inverse-propagator monomials and
   coefficient residues satisfying
   \[
   \operatorname{Res}_D(m_n)=
   \prod_{R\in\operatorname{Regions}(D)}m_R.
   \]
5. Five-point Rzk syntax and carrier-parametric evaluation for all channel
   residue values.

## Final verification

Fresh executions passed:

- `check_finite_poset_nerve.py`: 7,096 simplicial identities and 328 Segal
  simplex instances across the walking arrow and `Fact_5`; invertible arrows
  are exactly identity arrows.
- `check_generic_polygon_face_product.py`: all 257 dissections for `3 <= n <=
  7`, comprising 1,849 face elements and factor tuples.
- `check_generic_biadjoint_residue_factorization.py`: all 257 residues and 809
  residual monomials for `3 <= n <= 7`.
- the Rzk suite previously passed against pinned source digest
  `b396523107ce51d24fb8e248c6f8409f2e1efd402854843791356d29a07566a8`.

## Remaining foundation boundary

The nerve is a genuine external simplicial set, not an internal Rzk type.
Pinned Rzk/sHoTT has no constructor interpreting an external simplicial set or
strict finite category as a type, and no located poset nerve or Rezk completion.
Adding `#assume` declarations would expose an interface but would not create the
requested realization. Therefore no honest internalization step remains
executable in the current foundation.

Reopening requires a new Rzk primitive/library implementing strict-category
nerves or an authorized change to a proof assistant with simplicial-object
internalization. This is a typed foundation dependency, not a remaining
polygon or amplitude calculation.
