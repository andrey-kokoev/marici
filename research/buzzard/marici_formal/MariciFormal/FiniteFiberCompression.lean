import MariciFormal.FiniteInstrumentReadout

/-!
Finite two-point model of source-fiber information lost under scalar
compression.  This instantiates Grothendieck's Mellin radial obstruction and
the same post-readout blindness seen in Aspect's marginalization fixtures.

The file does not construct an idele-class Hilbert space, Mellin transform,
Poisson operator, or completed Green form.
-/

namespace MariciFormal.FiniteFiberCompression

open MariciFormal.FiniteInstrumentReadout

/-- Two-point fiber state over exact rational coefficients. -/
abbrev TwoPointFiber := Fin 2 → ℚ

/-- Scalar radial compression forgets the distribution within the fiber. -/
def radialCompression : TwoPointFiber →ₗ[ℚ] ℚ where
  toFun state := state 0 + state 1
  map_add' := by intros; simp; ring
  map_smul' := by intros; simp; ring

/-- The nonzero angular mode on the two-point fiber. -/
def angularMode : TwoPointFiber
  | 0 => 1
  | 1 => -1

theorem angularMode_ne_zero : angularMode ≠ 0 := by
  intro equality
  have := congrFun equality 0
  norm_num [angularMode] at this

theorem angularMode_mem_radialKernel :
    angularMode ∈ LinearMap.ker radialCompression := by
  simp [LinearMap.mem_ker, radialCompression, angularMode]

/-- A scalar post-compression Gram readout. -/
def radialGramReadout : ℚ →ₗ[ℚ] ℚ := LinearMap.id

/-- The general post-processing kernel law certifies that every radially
invisible mode stays invisible after the scalar Gram readout. -/
theorem radialKernel_le_gramKernel :
    LinearMap.ker radialCompression ≤
      LinearMap.ker (radialGramReadout.comp radialCompression) :=
  kernel_le_kernel_postprocess radialCompression radialGramReadout

theorem angularMode_mem_gramKernel :
    angularMode ∈
      LinearMap.ker (radialGramReadout.comp radialCompression) :=
  radialKernel_le_gramKernel angularMode_mem_radialKernel

/-- Finite-cutoff theorem: scalar compression and every displayed
post-compression readout are unfaithful on the undecomposed two-point source.
-/
theorem scalar_postcompression_not_faithful :
    ¬ Function.Injective radialCompression ∧
      ¬ Function.Injective (radialGramReadout.comp radialCompression) := by
  constructor <;> intro injective
  · exact angularMode_ne_zero
      (injective (by simpa [LinearMap.mem_ker] using
        angularMode_mem_radialKernel))
  · exact angularMode_ne_zero
      (injective (by simpa [LinearMap.mem_ker] using
        angularMode_mem_gramKernel))

/-- The radial mode survives, distinguishing information loss from the zero
map. -/
def radialMode : TwoPointFiber
  | 0 => 1
  | 1 => 1

theorem radialMode_survives : radialCompression radialMode = 2 := by
  norm_num [radialCompression, radialMode]

/-- The nontrivial two-point fiber action exchanges its two sites. -/
def fiberSwap (state : TwoPointFiber) : TwoPointFiber
  | 0 => state 1
  | 1 => state 0

def radialCoefficient (state : TwoPointFiber) : ℚ :=
  (state 0 + state 1) / 2

def angularCoefficient (state : TwoPointFiber) : ℚ :=
  (state 0 - state 1) / 2

/-- Exact two-mode reconstruction over `ℚ`. -/
theorem radial_angular_reconstruction (state : TwoPointFiber) :
    state = radialCoefficient state • radialMode +
      angularCoefficient state • angularMode := by
  funext site
  fin_cases site <;>
    simp [radialCoefficient, angularCoefficient, radialMode, angularMode] <;>
    ring

/-- In the finite fiber model, invariance under the nontrivial fiber action is
equivalent to vanishing of the angular coefficient. -/
theorem fiberSwap_invariant_iff_angularCoefficient_zero
    (state : TwoPointFiber) :
    fiberSwap state = state ↔ angularCoefficient state = 0 := by
  constructor
  · intro invariant
    have atZero := congrFun invariant 0
    simp [fiberSwap, angularCoefficient] at atZero ⊢
    linarith
  · intro angularZero
    funext site
    fin_cases site <;>
      simp [fiberSwap, angularCoefficient] at angularZero ⊢ <;>
      linarith

/-- Finite standard-vacuum fixture: the constant radial state is invariant and
has no angular component. -/
theorem standardVacuum_only_trivialFiberMode :
    fiberSwap radialMode = radialMode ∧
      angularCoefficient radialMode = 0 := by
  constructor
  · funext site
    fin_cases site <;> rfl
  · norm_num [angularCoefficient, radialMode]

/-- Hostile perturbation: the ambient source admits a nontrivial angular
component even though the standard radial vacuum does not activate it. -/
def oneSitePerturbation : TwoPointFiber
  | 0 => 1
  | 1 => 0

theorem ambientFiberCapacity_not_standardVacuumActivation :
    angularCoefficient oneSitePerturbation = 1 / 2 ∧
      fiberSwap oneSitePerturbation ≠ oneSitePerturbation := by
  constructor
  · norm_num [angularCoefficient, oneSitePerturbation]
  · intro equality
    have atZero := congrFun equality 0
    norm_num [fiberSwap, oneSitePerturbation] at atZero

end MariciFormal.FiniteFiberCompression
