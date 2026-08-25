import Mathlib

/-!
Finite, source-frozen facts about the `D(S₃)` label census.

This module does not construct a fusion category.  In particular, it supplies no
associator, `F`-matrix, `R`-matrix, pentagon, or hexagon witness.
-/

namespace MariciFormal.DS3

/-- The three conjugacy classes of `S₃`, named by cycle type. -/
inductive ConjugacyClass
  | identity
  | transposition
  | threeCycle
  deriving DecidableEq, Repr

open ConjugacyClass

/-- Frozen class cardinalities `1, 3, 2`. -/
def classSize : ConjugacyClass → ℕ
  | identity => 1
  | transposition => 3
  | threeCycle => 2

/-- Frozen centralizer orders `6, 2, 3`. -/
def centralizerOrder : ConjugacyClass → ℕ
  | identity => 6
  | transposition => 2
  | threeCycle => 3

/-- Irreducible representation labels for the identity centralizer `S₃`. -/
inductive IdentityIrrep | trivial | sign | standard
  deriving DecidableEq, Repr

/-- Irreducible representation labels for a transposition centralizer `C₂`. -/
inductive TranspositionIrrep | trivial | sign
  deriving DecidableEq, Repr

/-- Irreducible representation labels for a three-cycle centralizer `C₃`. -/
inductive ThreeCycleIrrep | chi0 | chi1 | chi2
  deriving DecidableEq, Repr

/-- The coefficient label over a flux class is an irrep of its centralizer. -/
def CentralizerIrrep : ConjugacyClass → Type
  | identity => IdentityIrrep
  | transposition => TranspositionIrrep
  | threeCycle => ThreeCycleIrrep

def irrepDimension : (c : ConjugacyClass) → CentralizerIrrep c → ℕ
  | identity, IdentityIrrep.trivial => 1
  | identity, IdentityIrrep.sign => 1
  | identity, IdentityIrrep.standard => 2
  | transposition, TranspositionIrrep.trivial => 1
  | transposition, TranspositionIrrep.sign => 1
  | threeCycle, ThreeCycleIrrep.chi0 => 1
  | threeCycle, ThreeCycleIrrep.chi1 => 1
  | threeCycle, ThreeCycleIrrep.chi2 => 1

/-- The centralizer irrep dimension-square census, checked class by class. -/
theorem centralizer_irrep_square_census :
    (1 ^ 2 + 1 ^ 2 + 2 ^ 2 : ℕ) = centralizerOrder identity ∧
    (1 ^ 2 + 1 ^ 2 : ℕ) = centralizerOrder transposition ∧
    (1 ^ 2 + 1 ^ 2 + 1 ^ 2 : ℕ) = centralizerOrder threeCycle := by
  decide

/-- The eight simple `D(S₃)` labels in the source packet's fixed order. -/
inductive AnyonLabel | A | B | C | D | E | F | G | H
  deriving DecidableEq, Repr

open AnyonLabel

def labelClass : AnyonLabel → ConjugacyClass
  | A | B | C => identity
  | D | E => transposition
  | F | G | H => threeCycle

/-- Quantum dimension `|C| dim(ρ)` for the frozen eight-label census. -/
def quantumDimension : AnyonLabel → ℕ
  | A | B => 1
  | C => 2
  | D | E => 3
  | F | G | H => 2

def allLabels : List AnyonLabel := [A, B, C, D, E, F, G, H]

theorem allLabels_exhaustive : allLabels.Nodup ∧ ∀ a, a ∈ allLabels := by
  constructor
  · decide
  · intro a
    cases a <;> decide

theorem quantum_dimension_list :
    allLabels.map quantumDimension = [1, 1, 2, 3, 3, 2, 2, 2] := by
  decide

/-- `Σₐ dₐ² = 36 = |S₃|²`. -/
theorem quantum_dimension_square_sum :
    (allLabels.map fun a => quantumDimension a ^ 2).sum = 6 ^ 2 := by
  decide

theorem eight_anyon_labels : allLabels.length = 8 := by
  decide

/-- The transposition-flux basis used by the frozen conjugation calculation. -/
inductive TranspositionFlux | t01 | t12 | t02
  deriving DecidableEq, Repr

open TranspositionFlux

/-- Conjugation by `(01)` fixes `(01)` and exchanges `(12)` with `(02)`. -/
def conjugationBraid : TranspositionFlux → TranspositionFlux
  | t01 => t01
  | t12 => t02
  | t02 => t12

theorem conjugation_braid_permutation :
    [t01, t12, t02].map conjugationBraid = [t01, t02, t12] := by
  decide

theorem conjugation_braid_involutive : Function.Involutive conjugationBraid := by
  intro x
  cases x <;> rfl

/-- A scalar action cannot change a basis label.  This braid does. -/
def ActsAsScalarOnFluxLabels (f : TranspositionFlux → TranspositionFlux) : Prop :=
  ∀ x, f x = x

theorem conjugation_braid_not_scalar :
    ¬ ActsAsScalarOnFluxLabels conjugationBraid := by
  intro h
  have := h t12
  contradiction

/- The explicit permutation calculation behind the flux-basis table. -/

def t01Perm : Fin 3 → Fin 3 := ![1, 0, 2]
def t12Perm : Fin 3 → Fin 3 := ![0, 2, 1]
def t02Perm : Fin 3 → Fin 3 := ![2, 1, 0]

/-- Since `(01)` is self-inverse, conjugation is `g ∘ h ∘ g`. -/
def conjugateByT01 (h : Fin 3 → Fin 3) : Fin 3 → Fin 3 :=
  fun i => t01Perm (h (t01Perm i))

theorem conjugate_t12_by_t01 : conjugateByT01 t12Perm = t02Perm := by
  funext i
  fin_cases i <;> rfl

theorem concrete_conjugation_changes_flux :
    conjugateByT01 t12Perm ≠ t12Perm := by
  rw [conjugate_t12_by_t01]
  intro h
  have hi := congrFun h 0
  contradiction

/-- The exact finite layer certified here; categorical coherence is absent. -/
structure FrozenFiniteLayer where
  classSizes : List ℕ
  centralizerOrders : List ℕ
  dimensions : List ℕ
  dimensionSquareSum : ℕ
  braidOnTranspositions : List TranspositionFlux

def frozenFiniteLayer : FrozenFiniteLayer where
  classSizes := [1, 3, 2]
  centralizerOrders := [6, 2, 3]
  dimensions := allLabels.map quantumDimension
  dimensionSquareSum := (allLabels.map fun a => quantumDimension a ^ 2).sum
  braidOnTranspositions := [t01, t12, t02].map conjugationBraid

theorem frozenFiniteLayer_values :
    frozenFiniteLayer.classSizes = [1, 3, 2] ∧
    frozenFiniteLayer.centralizerOrders = [6, 2, 3] ∧
    frozenFiniteLayer.dimensions = [1, 1, 2, 3, 3, 2, 2, 2] ∧
    frozenFiniteLayer.dimensionSquareSum = 36 ∧
    frozenFiniteLayer.braidOnTranspositions = [t01, t02, t12] := by
  decide

end MariciFormal.DS3
