import Mathlib.Data.Bool.Basic
import Mathlib.Tactic

/-!
Finite hostile from Grothendieck's split-quotient transfer audit: a split
quotient need not have a section invariant under its base-preserving
symmetries.
-/

namespace MariciFormal

abbrev C2 := Bool

def splitQuotient : C2 × C2 → C2 := Prod.fst

/-- The nontrivial automorphism over the first coordinate. -/
def basePreservingShear (x : C2 × C2) : C2 × C2 :=
  (x.1, x.1.xor x.2)

def sectionZero : C2 → C2 × C2 := fun a => (a, false)

def sectionDiagonal : C2 → C2 × C2 := fun a => (a, a)

def IsSection (section : C2 → C2 × C2) : Prop :=
  splitQuotient ∘ section = id

def PreservesXor (section : C2 → C2 × C2) : Prop :=
  ∀ x y,
    section (x.xor y) =
      (section x).1.xor (section y).1, (section x).2.xor (section y).2

def ShearInvariant (section : C2 → C2 × C2) : Prop :=
  basePreservingShear ∘ section = section

theorem splitQuotient_has_two_xorSections :
    IsSection sectionZero ∧ PreservesXor sectionZero ∧
      IsSection sectionDiagonal ∧ PreservesXor sectionDiagonal := by
  constructor
  · funext a
    rfl
  constructor
  · intro x y
    rfl
  constructor
  · funext a
    rfl
  · intro x y
    rfl

theorem shear_preserves_splitQuotient :
    splitQuotient ∘ basePreservingShear = splitQuotient := by
  funext x
  rfl

theorem shear_exchanges_sections :
    basePreservingShear ∘ sectionZero = sectionDiagonal ∧
      basePreservingShear ∘ sectionDiagonal = sectionZero := by
  constructor <;> funext a <;> cases a <;> rfl

/-- Strong form: not even a set-theoretic right inverse is fixed by the
base-preserving shear, hence no homomorphic section can be natural under it. -/
theorem no_shearInvariant_section :
    ¬ ∃ section : C2 → C2 × C2, IsSection section ∧ ShearInvariant section := by
  rintro ⟨section, hsection, hinvariant⟩
  have hfirst : (section true).1 = true := by
    have := congrFun hsection true
    simpa [IsSection, splitQuotient] using this
  have hfixed : basePreservingShear (section true) = section true := by
    have := congrFun hinvariant true
    simpa [ShearInvariant] using this
  obtain ⟨a, b⟩ := section true
  change a = true at hfirst
  subst a
  cases b <;> simp [basePreservingShear] at hfixed

section WeightedTransferControl

def pullback (f : C2 → ℚ) : C2 × C2 → ℚ :=
  fun x => f x.1

def uniformTransfer (f : C2 × C2 → ℚ) : C2 → ℚ :=
  fun a => (f (a, false) + f (a, true)) / 2

def chosenLiftTransfer (f : C2 × C2 → ℚ) : C2 → ℚ :=
  fun a => f (a, false)

def kernelTranslate (f : C2 × C2 → ℚ) : C2 × C2 → ℚ :=
  fun x => f (x.1, !x.2)

def sourceIdentitySelector : C2 × C2 → ℚ :=
  fun x => if x = (false, false) then 1 else 0

def targetIdentitySelector : C2 → ℚ :=
  fun x => if x = false then 1 else 0

theorem uniformTransfer_leftInverse (f : C2 → ℚ) :
    uniformTransfer (pullback f) = f := by
  funext a
  simp [uniformTransfer, pullback]

theorem uniformTransfer_kernelInvariant (f : C2 × C2 → ℚ) :
    uniformTransfer (kernelTranslate f) = uniformTransfer f := by
  funext a
  cases a <;> simp [uniformTransfer, kernelTranslate, add_comm]

theorem uniformTransfer_dilutes_identitySelector :
    uniformTransfer sourceIdentitySelector false = (1 / 2 : ℚ) ∧
      uniformTransfer sourceIdentitySelector ≠ targetIdentitySelector := by
  constructor
  · norm_num [uniformTransfer, sourceIdentitySelector]
  · intro h
    have := congrFun h false
    norm_num [uniformTransfer, sourceIdentitySelector, targetIdentitySelector] at this

theorem chosenLiftTransfer_leftInverse (f : C2 → ℚ) :
    chosenLiftTransfer (pullback f) = f := by
  rfl

theorem chosenLiftTransfer_preserves_identitySelector :
    chosenLiftTransfer sourceIdentitySelector = targetIdentitySelector := by
  funext a
  cases a <;> rfl

theorem chosenLiftTransfer_breaks_kernelSymmetry :
    chosenLiftTransfer (kernelTranslate sourceIdentitySelector) ≠
      chosenLiftTransfer sourceIdentitySelector := by
  intro h
  have := congrFun h false
  norm_num [chosenLiftTransfer, kernelTranslate, sourceIdentitySelector] at this

end WeightedTransferControl

end MariciFormal
