import Mathlib

/-!
Reciprocity-even formal germs have no odd jets, while six independent even
jets can faithfully encode a six-dimensional observation target.
-/

namespace MariciFormal

abbrev FormalJet := Nat → Rat

/-- Reciprocity acts on the normalized jet of order `n` by `(-1)^n`. -/
def reflectJet (jet : FormalJet) : FormalJet :=
  fun n => (-1 : Rat) ^ n * jet n

def ReciprocityEven (jet : FormalJet) : Prop := reflectJet jet = jet

theorem reciprocityEven_oddJet_zero
    (jet : FormalJet) (hEven : ReciprocityEven jet) (k : Nat) :
    jet (2 * k + 1) = 0 := by
  have h := congrFun hEven (2 * k + 1)
  simp [reflectJet, pow_add, pow_mul] at h
  linarith

abbrev PairingParameter := Fin 6 → Rat

/-- The model feature germ has coordinate `i` concentrated in even order `2i`. -/
def modelFeatureGerm (coordinate : Fin 6) : FormalJet :=
  fun order => if order = 2 * coordinate.val then 1 else 0

def normalizedEvenJetObservation
    (feature : Fin 6 → FormalJet) (order coordinate : Fin 6) : Rat :=
  feature coordinate (2 * order.val)

theorem modelFeatureGerm_even
    (coordinate : Fin 6) : ReciprocityEven (modelFeatureGerm coordinate) := by
  funext order
  unfold reflectJet modelFeatureGerm
  split_ifs with h
  · subst order
    simp [pow_mul]
  · simp

theorem model_evenJetMatrix_identity (order coordinate : Fin 6) :
    normalizedEvenJetObservation modelFeatureGerm order coordinate =
      if order = coordinate then 1 else 0 := by
  by_cases h : order = coordinate
  · subst coordinate
    simp [normalizedEvenJetObservation, modelFeatureGerm]
  · have hValue : 2 * order.val ≠ 2 * coordinate.val := by
      intro hEqual
      apply h
      apply Fin.ext
      omega
    simp [normalizedEvenJetObservation, modelFeatureGerm, h, hValue]

def observeThroughEvenJets (parameters : PairingParameter) : PairingParameter :=
  fun order => ∑ coordinate, normalizedEvenJetObservation modelFeatureGerm
    order coordinate * parameters coordinate

theorem observeThroughEvenJets_eq (parameters : PairingParameter) :
    observeThroughEvenJets parameters = parameters := by
  funext order
  simp [observeThroughEvenJets, model_evenJetMatrix_identity]

theorem sixEvenJets_are_faithful : Function.Injective observeThroughEvenJets := by
  intro p q h
  simpa [observeThroughEvenJets_eq] using h

/-- Degree-eight truncation retains only the first five even jet coordinates. -/
def degreeEightObservation (parameters : PairingParameter) : Fin 5 → Rat :=
  fun i => parameters i.castSucc

def invisibleTenthOrderParameter : PairingParameter :=
  fun i => if i = 5 then 1 else 0

theorem degreeEightObservation_not_faithful :
    invisibleTenthOrderParameter ≠ 0 ∧
      degreeEightObservation invisibleTenthOrderParameter =
        degreeEightObservation 0 := by
  constructor
  · intro h
    have h5 := congrFun h 5
    norm_num [invisibleTenthOrderParameter] at h5
  · funext i
    have hi : i.castSucc ≠ (5 : Fin 6) := by
      intro h
      have hValue := congrArg Fin.val h
      simp at hValue
      omega
    simp [degreeEightObservation, invisibleTenthOrderParameter, hi]

end MariciFormal
