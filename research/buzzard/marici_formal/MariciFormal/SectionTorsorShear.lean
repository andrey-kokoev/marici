import Mathlib.Algebra.Group.Hom.End

/-!
Finite additive form of Grothendieck's split-section torsor theorem. Sections
of `K × H -> H` are parametrized by `Hom(H,K)`, and base-preserving shears
act freely and transitively on those parameters.
-/

namespace MariciFormal

section SplitSectionTorsor

variable {K H : Type*} [AddCommGroup K] [AddCommGroup H]

def splitSection (u : H →+ K) : H →+ K × H where
  toFun h := (u h, h)
  map_zero' := by simp
  map_add' left right := by simp

def sectionFirstCoordinate (section : H →+ K × H) : H →+ K where
  toFun h := (section h).1
  map_zero' := by simp
  map_add' left right := by simp

theorem splitSection_second_coordinate (u : H →+ K) (h : H) :
    (splitSection u h).2 = h := rfl

/-- Every additive section of the second projection is uniquely the graph of
its first-coordinate homomorphism. -/
theorem section_eq_splitSection
    (section : H →+ K × H) (hsection : ∀ h, (section h).2 = h) :
    section = splitSection (sectionFirstCoordinate section) := by
  ext h <;> simp [splitSection, sectionFirstCoordinate, hsection]

def basePreservingShear (v : H →+ K) : K × H →+ K × H where
  toFun point := (point.1 + v point.2, point.2)
  map_zero' := by simp
  map_add' left right := by simp

theorem basePreservingShear_second_coordinate
    (v : H →+ K) (point : K × H) :
    (basePreservingShear v point).2 = point.2 := rfl

/-- Shearing a graph section adds the shear parameter. -/
theorem shear_acts_by_translation (u v : H →+ K) :
    (basePreservingShear v).comp (splitSection u) =
      splitSection (u + v) := by
  ext h <;> simp [basePreservingShear, splitSection]

/-- The shear action is transitive on the section parameters. -/
theorem shear_action_transitive (u target : H →+ K) :
    ∃ v : H →+ K,
      (basePreservingShear v).comp (splitSection u) =
        splitSection target := by
  refine ⟨target - u, ?_⟩
  rw [shear_acts_by_translation]
  ext h
  simp [splitSection]

/-- The shear action is free: a shear fixing one graph section is zero. -/
theorem shear_action_free (u v : H →+ K)
    (hfixed : (basePreservingShear v).comp (splitSection u) =
      splitSection u) :
    v = 0 := by
  ext h
  have hpoint := DFunLike.congr_fun hfixed h
  have hfirst := congrArg Prod.fst hpoint
  have : u h + v h = u h + 0 := by
    simpa [basePreservingShear, splitSection] using hfirst
  exact add_left_cancel this

/-- A nontrivial derivation excludes a section invariant under every shear. -/
theorem no_section_fixed_by_all_shears
    (hnontrivial : ∃ v : H →+ K, v ≠ 0) :
    ¬ ∃ u : H →+ K,
      ∀ v : H →+ K,
        (basePreservingShear v).comp (splitSection u) = splitSection u := by
  rintro ⟨u, hinvariant⟩
  obtain ⟨v, hv⟩ := hnontrivial
  exact hv (shear_action_free u v (hinvariant v))

end SplitSectionTorsor

end MariciFormal
