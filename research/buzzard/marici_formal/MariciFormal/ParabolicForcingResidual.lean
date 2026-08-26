import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum

/-!
Finite adjoint-line core of Grothendieck's theta tail forcing residual.
No differential equation or theta source is manufactured here.
-/

namespace MariciFormal

section TailSystem

variable {K : Type*} [CommRing K]

abbrev TailCovector (K : Type*) := Fin 2 → K

/-- Right action of the row covector on the triangular tail generator
`[[-z,-forcing],[0,0]]`. -/
def tailAdjointAction (spectral forcing : K)
    (covector : TailCovector K) : TailCovector K :=
  ![-covector 0 * spectral, -covector 0 * forcing]

def endpointTailCovector : TailCovector K := ![1, 0]
def constantTailCovector : TailCovector K := ![0, 1]

def SpansInvariantAdjointLine
    (action : TailCovector K → TailCovector K)
    (covector : TailCovector K) : Prop :=
  ∃ rate : K, action covector = fun i => rate * covector i

/-- The endpoint readout is an invariant adjoint line precisely when the
source forcing residual vanishes. -/
theorem endpointTailCovector_invariant_iff_forcing_zero
    (spectral forcing : K) :
    SpansInvariantAdjointLine (tailAdjointAction spectral forcing)
      endpointTailCovector ↔ forcing = 0 := by
  constructor
  · rintro ⟨rate, h⟩
    have h1 := congrFun h 1
    simpa [tailAdjointAction, endpointTailCovector] using h1
  · intro hforcing
    refine ⟨-spectral, ?_⟩
    funext i
    fin_cases i <;> simp [tailAdjointAction, endpointTailCovector, hforcing]

/-- The constant coordinate is always invariant, independently of forcing,
but it is not the endpoint scalar. -/
theorem constantTailCovector_always_invariant
    (spectral forcing : K) :
    SpansInvariantAdjointLine (tailAdjointAction spectral forcing)
      constantTailCovector := by
  refine ⟨0, ?_⟩
  funext i
  fin_cases i <;> simp [tailAdjointAction, constantTailCovector]

end TailSystem

section Hostile

theorem nonzero_forcing_breaks_endpoint_but_not_constant :
    (¬ SpansInvariantAdjointLine
      (tailAdjointAction (K := ℚ) 2 1) endpointTailCovector) ∧
      SpansInvariantAdjointLine
        (tailAdjointAction (K := ℚ) 2 1) constantTailCovector := by
  constructor
  · rw [endpointTailCovector_invariant_iff_forcing_zero]
    norm_num
  · exact constantTailCovector_always_invariant 2 1

end Hostile

end MariciFormal
