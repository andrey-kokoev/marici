import Mathlib.Tactic

/-!
Full-line and compressed finite core of Grothendieck's
translation/reflection mixed square.
-/

namespace MariciFormal

section FullLine

variable {A R : Type*} [AddCommGroup A]

def translate (a : A) (f : A → R) : A → R :=
  fun q => f (q + a)

def reflect (f : A → R) : A → R :=
  fun q => f (-q)

/-- Reflection conjugates translation by `a` to translation by `-a`. -/
theorem reflect_translate_reflect
    (a : A) (f : A → R) :
    reflect (translate a (reflect f)) = translate (-a) f := by
  funext q
  simp only [reflect, translate]
  congr 1
  abel

/-- Equivalent flat mixed-square form of the dihedral relation. -/
theorem reflect_translate
    (a : A) (f : A → R) :
    reflect (translate a f) = translate (-a) (reflect f) := by
  funext q
  simp only [reflect, translate]
  congr 1
  abel

end FullLine

section HalfLineCompression

variable {R : Type*} [AddCommGroup R]

def nonnegativeProjection (f : ℤ → R) : ℤ → R :=
  fun q => if 0 ≤ q then f q else 0

def compressedTranslationResidual (a : ℤ) (f : ℤ → R) : ℤ → R :=
  fun q => nonnegativeProjection (translate a f) q -
    translate a (nonnegativeProjection f) q

/-- For nonnegative displacement, half-line compression leaves exactly the
interval crossed by the moving seam. -/
theorem compressedTranslationResidual_eq
    (a : ℤ) (ha : 0 ≤ a) (f : ℤ → R) (q : ℤ) :
    compressedTranslationResidual a f q =
      if -a ≤ q ∧ q < 0 then -f (q + a) else 0 := by
  by_cases hq : 0 ≤ q
  · have hqa : 0 ≤ q + a := by omega
    simp [compressedTranslationResidual, nonnegativeProjection, translate,
      hq, hqa, show ¬ (-a ≤ q ∧ q < 0) by omega]
  · have hqneg : q < 0 := by omega
    by_cases hqa : 0 ≤ q + a
    · have hleft : -a ≤ q := by omega
      simp [compressedTranslationResidual, nonnegativeProjection, translate,
        hq, hqa, hleft, hqneg]
    · have hleft : ¬ -a ≤ q := by omega
      simp [compressedTranslationResidual, nonnegativeProjection, translate,
        hq, hqa, hleft]

/-- The crossed-interval residual is already nonzero for a constant hostile
source, so its existence is not theta-specific. -/
theorem universal_crossedInterval_hostile :
    compressedTranslationResidual (R := ℤ) 1 (fun _ => 1) (-1) = -1 := by
  norm_num [compressedTranslationResidual, nonnegativeProjection, translate]

end HalfLineCompression

end MariciFormal
