import Mathlib.Data.Matrix.Notation
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Directional finite core of Grothendieck's direct and dual theta tail systems.
The reciprocal sewing map is intentionally not inferred from the two arrows.
-/

namespace MariciFormal

open Matrix

section TriangularGenerators

variable {R : Type*} [CommRing R]

def directTailGenerator (p : R) : Matrix (Fin 2) (Fin 2) R :=
  !![0, p;
     0, 0]

def dualTailGenerator (p : R) : Matrix (Fin 2) (Fin 2) R :=
  (directTailGenerator p)ᵀ

theorem directTailGenerator_forward (p : R) :
    directTailGenerator p 0 1 = p := by
  simp [directTailGenerator]

theorem directTailGenerator_reverse_absent (p : R) :
    directTailGenerator p 1 0 = 0 := by
  simp [directTailGenerator]

theorem dualTailGenerator_forward_absent (p : R) :
    dualTailGenerator p 0 1 = 0 := by
  simp [dualTailGenerator, directTailGenerator]

theorem dualTailGenerator_reverse (p : R) :
    dualTailGenerator p 1 0 = p := by
  simp [dualTailGenerator, directTailGenerator]

theorem directTailGenerator_sq_zero (p : R) :
    directTailGenerator p * directTailGenerator p = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [directTailGenerator, Matrix.mul_apply]

theorem dualTailGenerator_sq_zero (p : R) :
    dualTailGenerator p * dualTailGenerator p = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [dualTailGenerator, directTailGenerator, Matrix.mul_apply]

/-- On a carrier identified by hand, adding the two sectors creates both
blocks. The typing section below records why this sum is not source-authorized
without sewing. -/
theorem manually_identified_sum_is_bidirectional (p : R) :
    (directTailGenerator p + dualTailGenerator p) 0 1 = p ∧
      (directTailGenerator p + dualTailGenerator p) 1 0 = p := by
  simp [directTailGenerator, dualTailGenerator]

end TriangularGenerators

section DirectionalTyping

inductive TailLocus
  | directForcing
  | directEndpoint
  | dualEndpoint
  | dualForcing
  deriving DecidableEq

structure TypedTailArrow where
  source : TailLocus
  target : TailLocus
  deriving DecidableEq

def directIncidenceArrow : TypedTailArrow :=
  ⟨TailLocus.directForcing, TailLocus.directEndpoint⟩

def dualIncidenceArrow : TypedTailArrow :=
  ⟨TailLocus.dualEndpoint, TailLocus.dualForcing⟩

def TailComposable (first second : TypedTailArrow) : Prop :=
  first.target = second.source

/-- Opposite incidence directions live in different reciprocal loci and do
not compose before a sewing arrow identifies the relevant carriers. -/
theorem direct_dual_not_composable :
    ¬ TailComposable directIncidenceArrow dualIncidenceArrow := by
  decide

def reciprocalEndpointSewing : TypedTailArrow :=
  ⟨TailLocus.directEndpoint, TailLocus.dualEndpoint⟩

theorem direct_composes_with_explicit_sewing :
    TailComposable directIncidenceArrow reciprocalEndpointSewing := by
  rfl

theorem sewing_composes_with_dual :
    TailComposable reciprocalEndpointSewing dualIncidenceArrow := by
  rfl

end DirectionalTyping

section ObservationDoesNotActuate

variable {R : Type*} [CommRing R]

def endpointObservationRow (response : R) : Fin 2 → R
  | 0 => 1
  | 1 => response

/-- Changing an output row cannot fill the absent reverse generator block. -/
theorem observation_does_not_manufacture_reverse_block
    (p response : R) :
    endpointObservationRow response 0 = 1 ∧
      directTailGenerator p 1 0 = 0 := by
  simp [endpointObservationRow, directTailGenerator]

end ObservationDoesNotActuate

end MariciFormal
