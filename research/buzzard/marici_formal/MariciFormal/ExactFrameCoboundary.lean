import Mathlib

/-!
Group-level endpoint-frame coboundary shared by Grothendieck's reciprocal
prime frames and cross-sector transport/descent comparisons.
-/

namespace MariciFormal.ExactFrameCoboundary

variable {Label G : Type*} [Group G]

/-- Comparison generated solely by one frame at each endpoint. -/
def endpointTransition (frame : Label → G) (source target : Label) : G :=
  (frame source)⁻¹ * frame target

theorem endpointTransition_self
    (frame : Label → G) (label : Label) :
    endpointTransition frame label label = 1 := by
  simp [endpointTransition]

/-- Exact cocycle law for endpoint-generated comparisons. -/
theorem endpointTransition_comp
    (frame : Label → G) (first second third : Label) :
    endpointTransition frame first second *
        endpointTransition frame second third =
      endpointTransition frame first third := by
  simp [endpointTransition, mul_assoc]

/-- Every endpoint-generated triangle has trivial holonomy. -/
theorem endpointTransition_triangle
    (frame : Label → G) (first second third : Label) :
    endpointTransition frame first second *
        endpointTransition frame second third *
        endpointTransition frame third first = 1 := by
  rw [endpointTransition_comp]
  simp [endpointTransition]

/-- A local operator obtained by conjugating one universal operator returns to
that operator in its source-native frame. -/
def framedOperator (frame : Label → G) (universal : G) (label : Label) : G :=
  frame label * universal * (frame label)⁻¹

theorem normalize_framedOperator
    (frame : Label → G) (universal : G) (label : Label) :
    (frame label)⁻¹ * framedOperator frame universal label * frame label =
      universal := by
  simp [framedOperator, mul_assoc]

/-- Hostile triangle: three individually valid group elements with nontrivial
product cannot all arise from one-label endpoint frames. -/
theorem nontrivial_triangle_not_endpoint_coboundary :
    ¬ ∃ frame : Fin 3 → ℚˣ,
      endpointTransition frame 0 1 = (-1 : ℚˣ) ∧
      endpointTransition frame 1 2 = 1 ∧
      endpointTransition frame 2 0 = 1 := by
  rintro ⟨frame, firstEdge, secondEdge, thirdEdge⟩
  have flat := endpointTransition_triangle frame 0 1 2
  rw [firstEdge, secondEdge, thirdEdge] at flat
  norm_num at flat

end MariciFormal.ExactFrameCoboundary
