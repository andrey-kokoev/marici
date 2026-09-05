import Mathlib.AlgebraicTopology.SimplicialSet.StrictSegal
import Mathlib.CategoryTheory.Category.Preorder

/-!
# Finite-poset nerves

A polygon-refinement order is modeled as a category, and its ordinary nerve is
an actual simplicial set. Faces and degeneracies are supplied by the
simplicial-set functor; strict Segal follows from the nerve theorem in Mathlib.
-/

open CategoryTheory
open CategoryTheory.SimplicialObject

namespace Marici

universe u

/-- The genuine simplicial-set nerve of any partial order. Finiteness is not
required by the construction. -/
def posetNerve (P : Type u) [PartialOrder P] : SSet.{u} :=
  CategoryTheory.nerve P

/-- Every poset nerve is strict Segal: a simplex is uniquely determined by its
composable spine. -/
instance posetNerveIsStrictSegal (P : Type u) [PartialOrder P] :
    SSet.IsStrictSegal (posetNerve P) :=
  CategoryTheory.Nerve.isStrictSegal P

/-- Antisymmetry is the completeness statement for a poset nerve: the only
invertible refinement arrows are those between equal objects. -/
theorem poset_iso_nonempty_iff_eq {P : Type u} [PartialOrder P] (x y : P) :
    Nonempty (x ≅ y) ↔ x = y := by
  constructor
  · rintro ⟨i⟩
    exact le_antisymm i.hom.le i.inv.le
  · rintro rfl
    exact ⟨Iso.refl x⟩

/-- Application-specific name for the nerve of a polygon-dissection refinement
order. Any concrete dissection type only has to provide `PartialOrder`. -/
abbrev dissectionNerve (Dissection : Type u) [PartialOrder Dissection] : SSet.{u} :=
  posetNerve Dissection

example (P : Type u) [PartialOrder P] :
    SSet.IsStrictSegal (dissectionNerve P) := inferInstance

end Marici
