import Mathlib

/-!
Finite gauge covariance for a one-dimensional transition and its distinguished
covector.  Normalizing a transition is not enough: the covector must transform
contragrediently if the endpoint pairing is to remain compatible.
-/

namespace MariciFormal

section Field

variable {K : Type*} [Field K]

/-- A covector at the target chart agrees with the source covector across `U`. -/
def PairingCompatible (U lambdaX lambdaY : K) : Prop :=
  lambdaY * U = lambdaX

/-- Transition law under coordinate changes `v'_X = rX v_X`, `v'_Y = rY v_Y`. -/
def gaugeTransition (rX rY U : K) : K :=
  rY * U / rX

/-- Contragredient law for a distinguished covector. -/
def gaugeCovector (r lambda : K) : K :=
  lambda / r

theorem pairingCompatible_gauge_transport
    {U lambdaX lambdaY rX rY : K}
    (compatible : PairingCompatible U lambdaX lambdaY)
    (hrX : rX ≠ 0) (hrY : rY ≠ 0) :
    PairingCompatible (gaugeTransition rX rY U)
      (gaugeCovector rX lambdaX) (gaugeCovector rY lambdaY) := by
  unfold PairingCompatible gaugeTransition gaugeCovector at *
  calc
    lambdaY / rY * (rY * U / rX) = (lambdaY * U) / rX := by
      field_simp
    _ = lambdaX / rX := by rw [compatible]

/-- The scalar ratio induced by a covector and a nonzero metric coefficient. -/
def pairingMetricRatio (lambda h : K) : K :=
  lambda ^ 2 / h

/-- Simultaneous contragredient covector and metric transport preserves the ratio. -/
theorem pairingMetricRatio_gauge_invariant
    {lambda h r : K} (hh : h ≠ 0) (hr : r ≠ 0) :
    pairingMetricRatio (lambda / r) (h / r ^ 2) =
      pairingMetricRatio lambda h := by
  unfold pairingMetricRatio
  field_simp

end Field

section ExactHostileFixture

/-- Strominger's two-chart transition is compatible before gauge normalization. -/
example : PairingCompatible (2 : Rat) 1 (1 / 2) := by
  norm_num [PairingCompatible]

/-- The coordinate change `(rX,rY)=(1,1/2)` normalizes `U=2` to one. -/
example : gaugeTransition (1 : Rat) (1 / 2) 2 = 1 := by
  norm_num [gaugeTransition]

/-- Retaining the old covectors after normalizing the transition breaks pairing compatibility. -/
theorem normalized_transition_with_stale_covector_is_incompatible :
    ¬ PairingCompatible (1 : Rat) 1 (1 / 2) := by
  norm_num [PairingCompatible]

/-- Contragredient transport repairs the pairing in the normalized chart. -/
theorem normalized_transition_with_transported_covector_is_compatible :
    PairingCompatible (gaugeTransition (1 : Rat) (1 / 2) 2)
      (gaugeCovector 1 1) (gaugeCovector (1 / 2) (1 / 2)) := by
  norm_num [PairingCompatible, gaugeTransition, gaugeCovector]

/-- The packet's exact metric/covector coefficients have equal invariant ratio. -/
example : pairingMetricRatio (1 : Rat) 1 = pairingMetricRatio (1 / 2) (1 / 4) := by
  norm_num [pairingMetricRatio]

end ExactHostileFixture

end MariciFormal
