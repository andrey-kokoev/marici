import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum

/-!
Finite route/covector core of Grothendieck's canonical half-line antipode.
The analytic half-line integral and its source-selected frame are not inferred.
-/

namespace MariciFormal

section RoutePairing

variable {K : Type*} [Field K]

abbrev TwoRouteState (K : Type*) := Fin 2 → K
abbrev TwoRouteCovector (K : Type*) := Fin 2 → K

def routePairing (covector : TwoRouteCovector K) (state : TwoRouteState K) : K :=
  covector 0 * state 0 + covector 1 * state 1

def equalRouteCovector : TwoRouteCovector K := ![1, 1]

def routeRescale (scale : Fin 2 → K) (state : TwoRouteState K) : TwoRouteState K :=
  fun i => scale i * state i

def covectorRescale (scale : Fin 2 → K) (covector : TwoRouteCovector K) :
    TwoRouteCovector K :=
  fun i => covector i / scale i

/-- A diagonal route-basis change preserves incidence only when the covector
is transported contragrediently. -/
theorem routePairing_contragredient_invariant
    (scale : Fin 2 → K) (covector : TwoRouteCovector K)
    (state : TwoRouteState K) (hscale : ∀ i, scale i ≠ 0) :
    routePairing (covectorRescale scale covector) (routeRescale scale state) =
      routePairing covector state := by
  simp [routePairing, covectorRescale, routeRescale, hscale]

/-- In the source-selected equal-covector chart, zero incidence is equivalent
to the route ratio being the antipode, provided the denominator route is
nonzero. -/
theorem equalRoute_zero_iff_antipode
    (state : TwoRouteState K) (hminus : state 1 ≠ 0) :
    routePairing equalRouteCovector state = 0 ↔ state 0 / state 1 = -1 := by
  simp only [routePairing, equalRouteCovector, Matrix.cons_val_zero,
    Matrix.cons_val_one, one_mul]
  constructor
  · intro h
    apply (div_eq_iff hminus).2
    linear_combination h
  · intro h
    have := (div_eq_iff hminus).1 h
    linear_combination this

end RoutePairing

section Hostile

inductive SpectralLocus
  | seam
  | offSeam
  deriving DecidableEq

structure LocatedRoutePoint where
  locus : SpectralLocus
  route : TwoRouteState ℚ

def offSeamAntipodalPoint : LocatedRoutePoint :=
  ⟨SpectralLocus.offSeam, ![1, -1]⟩

/-- The equal-covector antipode condition alone contains no field connecting
it to the spectral seam. -/
theorem antipodal_incidence_can_be_offSeam :
    offSeamAntipodalPoint.locus = SpectralLocus.offSeam ∧
      routePairing equalRouteCovector offSeamAntipodalPoint.route = 0 ∧
      offSeamAntipodalPoint.route 0 / offSeamAntipodalPoint.route 1 = -1 := by
  norm_num [offSeamAntipodalPoint, routePairing, equalRouteCovector]

end Hostile

end MariciFormal
