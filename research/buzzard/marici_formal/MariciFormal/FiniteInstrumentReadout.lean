import MariciFormal.FiniteObservation

/-!
Finite, calibration-aware readout facts shared by Aspect's optics packets,
Strominger's port families, and Flavor's calibrated detector maps.

This file deliberately does not define a quantum `Instrument`: the current
cross-sector inputs specify outcome readouts but not a common post-measurement
state-update law.  Linear amplitude/state readouts and nonlinear statistical
coarsenings are therefore kept in separate sections.
-/

namespace MariciFormal.FiniteInstrumentReadout

open scoped BigOperators

section DeterministicReadout

variable {S R P : Type*}

/-- Two sources are observationally equivalent for a declared readout. -/
def Indistinguishable (readout : S → R) (first second : S) : Prop :=
  readout first = readout second

/-- Deterministic processing preserves every pre-existing observational
identification. -/
theorem indistinguishable_under_postprocess
    (readout : S → R) (process : R → P) {first second : S}
    (h : Indistinguishable readout first second) :
    Indistinguishable (process ∘ readout) first second := by
  exact congrArg process h

/-- If a processed record is faithful, the record before processing was
already faithful.  Processing cannot manufacture distinguishability. -/
theorem injective_of_postprocess_injective
    (readout : S → R) (process : R → P)
    (h : Function.Injective (process ∘ readout)) :
    Function.Injective readout := by
  intro first second hequal
  apply h
  exact congrArg process hequal

/-- Injective processing preserves observational equivalence exactly. -/
theorem indistinguishable_postprocess_iff_of_injective
    (readout : S → R) (process : R → P)
    (hprocess : Function.Injective process) (first second : S) :
    Indistinguishable (process ∘ readout) first second ↔
      Indistinguishable readout first second := by
  constructor
  · intro h
    exact hprocess h
  · intro h
    exact congrArg process h

end DeterministicReadout

section LinearReadout

variable {F V W O P : Type*} [Field F]
  [AddCommGroup V] [Module F V]
  [AddCommGroup W] [Module F W]
  [AddCommGroup O] [Module F O]
  [AddCommGroup P] [Module F P]

/-- Faithfulness of a finite linear readout is ordinary injectivity. -/
def Faithful (readout : V →ₗ[F] O) : Prop := Function.Injective readout

/-- Recalibrating source coordinates by a linear equivalence preserves
faithfulness. -/
theorem faithful_comp_sourceCalibration_iff
    (readout : V →ₗ[F] O) (calibration : W ≃ₗ[F] V) :
    Faithful (readout.comp calibration.toLinearMap) ↔ Faithful readout := by
  constructor
  · intro h x y hxy
    have hpre : calibration.symm x = calibration.symm y := by
      apply h
      simpa using hxy
    exact calibration.symm.injective hpre
  · intro h x y hxy
    apply calibration.injective
    exact h hxy

/-- Recalibrating outcome coordinates by a linear equivalence preserves
faithfulness. -/
theorem faithful_outcomeCalibration_comp_iff
    (readout : V →ₗ[F] O) (calibration : O ≃ₗ[F] P) :
    Faithful (calibration.toLinearMap.comp readout) ↔ Faithful readout := by
  constructor
  · intro h x y hxy
    apply h
    exact congrArg calibration hxy
  · intro h x y hxy
    apply h
    exact calibration.injective hxy

/-- Deterministic linear post-processing cannot shrink the observational
kernel. -/
theorem kernel_le_kernel_postprocess
    (readout : V →ₗ[F] O) (process : O →ₗ[F] P) :
    LinearMap.ker readout ≤ LinearMap.ker (process.comp readout) := by
  intro x hx
  change process (readout x) = 0
  rw [LinearMap.mem_ker] at hx
  rw [hx, map_zero]

/-- An injective post-processing map preserves the readout kernel exactly. -/
theorem kernel_postprocess_eq_of_injective
    (readout : V →ₗ[F] O) (process : O →ₗ[F] P)
    (hprocess : Function.Injective process) :
    LinearMap.ker (process.comp readout) = LinearMap.ker readout := by
  apply le_antisymm
  · intro x hx
    rw [LinearMap.mem_ker] at hx ⊢
    apply hprocess
    simpa using hx
  · exact kernel_le_kernel_postprocess readout process

end LinearReadout

section LinearHostile

abbrev RationalPair := Fin 2 → ℚ

/-- Keep only the first detector coordinate. -/
def firstCoordinate : RationalPair →ₗ[ℚ] ℚ := LinearMap.proj 0

/-- The identity readout is faithful before the non-injective coordinate
projection. -/
theorem firstCoordinate_postprocessing_loses_faithfulness :
    Faithful (LinearMap.id : RationalPair →ₗ[ℚ] RationalPair) ∧
      ¬ Faithful firstCoordinate := by
  constructor
  · exact fun _ _ h ↦ h
  · intro h
    change Function.Injective firstCoordinate at h
    have hequal : (![0, 1] : RationalPair) = ![0, 0] :=
      h (by simp [firstCoordinate])
    have h1 := congrFun hequal 1
    norm_num at h1

end LinearHostile

section CalibratedQuadratureFixture

variable {F : Type*} [Field F]

/-- Two predeclared quadrature rows, scaled by the common nonzero local
oscillator calibration.  The coordinates represent the phase rows at zero
and one quarter-turn; no trigonometric or continuum-mode claim is made. -/
def scaledQuadraturePorts (localOscillator : F) :
    Fin 2 → (Fin 2 → F) →ₗ[F] F :=
  fun i ↦ localOscillator • LinearMap.proj i

/-- The calibrated two-row mean readout is jointly faithful exactly when the
local-oscillator amplitude is nonzero. -/
theorem scaledQuadraturePorts_jointlyFaithful_iff
    (localOscillator : F) :
    MariciFormal.JointlyFaithful (scaledQuadraturePorts localOscillator) ↔
      localOscillator ≠ 0 := by
  rw [MariciFormal.jointlyFaithful_iff_point_separating]
  constructor
  · intro h hzero
    subst localOscillator
    let witness : Fin 2 → F := Pi.single 0 1
    have hwitness := h witness (by
      intro i
      simp [scaledQuadraturePorts])
    have hzeroCoordinate := congrFun hwitness 0
    simp [witness] at hzeroCoordinate
  · intro hnonzero vector hvanishes
    funext i
    have hi : localOscillator * vector i = 0 := by
      simpa [scaledQuadraturePorts] using hvanishes i
    exact (mul_eq_zero.mp hi).resolve_left hnonzero

/-- With no phase reference, every quadrature row is the zero map. -/
theorem zeroLocalOscillator_collapses_all_rows (i : Fin 2) :
    scaledQuadraturePorts (F := F) 0 i = 0 := by
  simp [scaledQuadraturePorts]

/-- The same two coordinate rows, with unit calibration, recover the declared
two-real-parameter displacement class. -/
theorem unitLocalOscillator_jointlyFaithful :
    MariciFormal.JointlyFaithful (scaledQuadraturePorts (F := F) 1) := by
  rw [scaledQuadraturePorts_jointlyFaithful_iff]
  exact one_ne_zero

/-- Temporal/spatial mode overlap scales the same finite quadrature rows. -/
def modeMatchedQuadraturePorts (localOscillator overlap : F) :
    Fin 2 → (Fin 2 → F) →ₗ[F] F :=
  scaledQuadraturePorts (localOscillator * overlap)

theorem modeMatchedQuadraturePorts_jointlyFaithful_iff
    (localOscillator overlap : F) :
    MariciFormal.JointlyFaithful
        (modeMatchedQuadraturePorts localOscillator overlap) ↔
      localOscillator ≠ 0 ∧ overlap ≠ 0 := by
  rw [modeMatchedQuadraturePorts, scaledQuadraturePorts_jointlyFaithful_iff]
  exact mul_ne_zero_iff

/-- A nonzero local oscillator does not rescue an orthogonal signal mode. -/
theorem zeroModeOverlap_collapses_liveLocalOscillator
    (localOscillator : F) (i : Fin 2) :
    modeMatchedQuadraturePorts localOscillator 0 i = 0 := by
  simp [modeMatchedQuadraturePorts, scaledQuadraturePorts]

end CalibratedQuadratureFixture

section BalancedDetectionCalibration

/-- Gain-weighted balanced intensity difference in the convention where each
beam-splitter output intensity carries the common factor one half. -/
def balancedDetectorDifference
    (gainPlus gainMinus signal localOscillator : ℚ) : ℚ :=
  (gainPlus * (signal + localOscillator) ^ 2 -
    gainMinus * (signal - localOscillator) ^ 2) / 2

/-- Matched calibrated gains remove both common square terms and retain the
signal/local-oscillator cross term. -/
theorem matchedGain_balancedDifference
    (signal localOscillator : ℚ) :
    balancedDetectorDifference 1 1 signal localOscillator =
      2 * signal * localOscillator := by
  unfold balancedDetectorDifference
  ring

/-- With zero signal, gain mismatch leaves a residual proportional to the
large local-oscillator background. -/
theorem gainMismatch_zeroSignal_residual
    (gainPlus gainMinus localOscillator : ℚ) :
    balancedDetectorDifference gainPlus gainMinus 0 localOscillator =
      (gainPlus - gainMinus) * localOscillator ^ 2 / 2 := by
  unfold balancedDetectorDifference
  ring

theorem gainMismatch_strongReference_hostile :
    balancedDetectorDifference 1 (9 / 10) 0 10 = 5 ∧
      balancedDetectorDifference 1 1 0 10 = 0 := by
  norm_num [balancedDetectorDifference]

end BalancedDetectionCalibration

section HeterodyneMeanAndNoise

/-- After declared gain rescaling, the finite heterodyne mean map is the two
coordinate family. -/
abbrev heterodyneMeanPorts :
    Fin 2 → (Fin 2 → ℚ) →ₗ[ℚ] ℚ :=
  MariciFormal.FiniteObservation.coordinateProbes 2

theorem heterodyneMeanPorts_jointlyFaithful :
    MariciFormal.JointlyFaithful heterodyneMeanPorts :=
  MariciFormal.FiniteObservation.coordinateProbes_jointlyFaithful 2

def homodyneQuadratureVariance (intrinsicVariance : ℚ) : ℚ :=
  intrinsicVariance

/-- The unused splitter port contributes a separately declared variance. -/
def heterodyneQuadratureVariance
    (intrinsicVariance unusedPortVariance : ℚ) : ℚ :=
  intrinsicVariance + unusedPortVariance

theorem heterodyneVariance_penalty
    (intrinsicVariance unusedPortVariance : ℚ) :
    heterodyneQuadratureVariance intrinsicVariance unusedPortVariance -
        homodyneQuadratureVariance intrinsicVariance =
      unusedPortVariance := by
  unfold heterodyneQuadratureVariance homodyneQuadratureVariance
  ring

theorem heterodyneVariance_strictlyGreater
    (intrinsicVariance unusedPortVariance : ℚ)
    (hunused : 0 < unusedPortVariance) :
    homodyneQuadratureVariance intrinsicVariance <
      heterodyneQuadratureVariance intrinsicVariance unusedPortVariance := by
  unfold heterodyneQuadratureVariance homodyneQuadratureVariance
  linarith

theorem vacuumHeterodyne_fixture :
    homodyneQuadratureVariance (1 / 2) = 1 / 2 ∧
      heterodyneQuadratureVariance (1 / 2) (1 / 2) = 1 ∧
      heterodyneQuadratureVariance (1 / 2) (1 / 2) ≠
        homodyneQuadratureVariance (1 / 2) := by
  norm_num [homodyneQuadratureVariance, heterodyneQuadratureVariance]

end HeterodyneMeanAndNoise

section CalibratedReciprocityFixture

abbrev RationalTwoPortMatrix := Matrix (Fin 2) (Fin 2) ℚ

/-- Symmetric orthogonal mirror in common energy-normalized port coordinates. -/
def energyNormalizedMirror : RationalTwoPortMatrix :=
  !![3 / 5, 4 / 5; 4 / 5, -3 / 5]

/-- The same map displayed after unequal input/output coordinate scaling. -/
def unequallyScaledMirror : RationalTwoPortMatrix :=
  !![3 / 5, 8 / 5; 2 / 5, -3 / 5]

/-- Transported energy metric for the scaling `diag(2,1)`. -/
def scaledPortMetric : RationalTwoPortMatrix :=
  !![1 / 4, 0; 0, 1]

theorem energyNormalizedMirror_symmetric :
    energyNormalizedMirror.transpose = energyNormalizedMirror := by
  ext i j
  fin_cases i <;> fin_cases j <;> norm_num [energyNormalizedMirror]

theorem energyNormalizedMirror_orthogonal :
    energyNormalizedMirror.transpose * energyNormalizedMirror = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [energyNormalizedMirror, Matrix.mul_apply, Fin.sum_univ_succ]

/-- Unequal coordinate scaling makes the displayed matrix nonsymmetric. -/
theorem unequallyScaledMirror_not_symmetric :
    unequallyScaledMirror.transpose ≠ unequallyScaledMirror := by
  intro h
  have h01 := congrArg (fun matrix : RationalTwoPortMatrix ↦ matrix 0 1) h
  norm_num [unequallyScaledMirror] at h01

/-- Reciprocity survives in the transported energy metric. -/
theorem unequallyScaledMirror_metric_reciprocal :
    scaledPortMetric * unequallyScaledMirror =
      unequallyScaledMirror.transpose * scaledPortMetric := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [scaledPortMetric, unequallyScaledMirror,
      Matrix.mul_apply, Fin.sum_univ_succ]

/-- Euclidean symmetry and metric reciprocity are distinct calibration
statements for the same physical two-port map. -/
theorem reciprocity_requires_common_metric_hostile :
    unequallyScaledMirror.transpose ≠ unequallyScaledMirror ∧
      scaledPortMetric * unequallyScaledMirror =
        unequallyScaledMirror.transpose * scaledPortMetric :=
  ⟨unequallyScaledMirror_not_symmetric,
    unequallyScaledMirror_metric_reciprocal⟩

end CalibratedReciprocityFixture

section TwoPathInterferometerFixture

/-- Aspect's balanced recombiner uses the already shared Hadamard port family.
Coordinate zero is the bright output and coordinate one the dark output. -/
abbrev balancedRecombinerPorts :
    Fin 2 → (Fin 2 → ℚ) →ₗ[ℚ] ℚ :=
  MariciFormal.FiniteObservation.magneticHadamardPorts

/-- The equal two-route amplitude before recombination.  Normalization by a
common nonzero scalar is irrelevant to the kernel distinction. -/
def symmetricRouteState : Fin 2 → ℚ := ![1, 1]

theorem symmetricRouteState_ne_zero : symmetricRouteState ≠ 0 := by
  intro h
  have h0 := congrFun h 0
  norm_num [symmetricRouteState] at h0

theorem balancedRecombiner_jointlyFaithful :
    MariciFormal.JointlyFaithful balancedRecombinerPorts :=
  MariciFormal.FiniteObservation.magneticHadamardPorts_faithful

theorem symmetricRoute_bright_value :
    balancedRecombinerPorts 0 symmetricRouteState = 2 := by
  norm_num [balancedRecombinerPorts,
    MariciFormal.FiniteObservation.magneticHadamardPorts,
    symmetricRouteState]

theorem symmetricRoute_dark_value :
    balancedRecombinerPorts 1 symmetricRouteState = 0 := by
  norm_num [balancedRecombinerPorts,
    MariciFormal.FiniteObservation.magneticHadamardPorts,
    symmetricRouteState]

/-- A selected dark detector amplitude does not annihilate either the route
state or the full detector record. -/
theorem selectedDarkPort_zero_not_route_annihilation :
    symmetricRouteState ≠ 0 ∧
      balancedRecombinerPorts 1 symmetricRouteState = 0 ∧
      balancedRecombinerPorts 0 symmetricRouteState ≠ 0 := by
  exact ⟨symmetricRouteState_ne_zero, symmetricRoute_dark_value,
    by norm_num [symmetricRoute_bright_value]⟩

/-- Availability is typed separately from the detector value.  This port is
present and executable even though it is dark on `symmetricRouteState`. -/
def availableDarkPort :
    MariciFormal.FiniteObservation.AuthorizedPort (Fin 2 → ℚ) ℚ :=
  ⟨some (balancedRecombinerPorts 1)⟩

theorem availableDarkPort_ne_unavailable :
    availableDarkPort ≠
      (MariciFormal.FiniteObservation.unavailablePort :
        MariciFormal.FiniteObservation.AuthorizedPort (Fin 2 → ℚ) ℚ) := by
  intro h
  have hexecute := congrArg
    MariciFormal.FiniteObservation.AuthorizedPort.execute h
  simp [availableDarkPort,
    MariciFormal.FiniteObservation.unavailablePort] at hexecute

theorem availableDarkPort_executes_and_returns_zero :
    availableDarkPort.execute = some (balancedRecombinerPorts 1) ∧
      balancedRecombinerPorts 1 symmetricRouteState = 0 := by
  exact ⟨rfl, symmetricRoute_dark_value⟩

end TwoPathInterferometerFixture

section LossEnvironmentDilation

/-- Squared amplitude for the finite rational loss fixture. -/
def scalarIntensity (amplitude : ℚ) : ℚ := amplitude ^ 2

/-- Retained and environmental amplitudes of a two-port loss dilation. -/
def lossDilation (retained environment amplitude : ℚ) : Fin 2 → ℚ :=
  ![retained * amplitude, environment * amplitude]

def dilationIntensity (output : Fin 2 → ℚ) : ℚ :=
  scalarIntensity (output 0) + scalarIntensity (output 1)

/-- The enlarged retained-plus-environment record preserves intensity under
the declared isometry equation. -/
theorem lossDilation_preserves_intensity
    (retained environment amplitude : ℚ)
    (hisometry : retained ^ 2 + environment ^ 2 = 1) :
    dilationIntensity (lossDilation retained environment amplitude) =
      scalarIntensity amplitude := by
  unfold dilationIntensity lossDilation scalarIntensity
  change
    (retained * amplitude) ^ 2 + (environment * amplitude) ^ 2 =
      amplitude ^ 2
  calc
    (retained * amplitude) ^ 2 + (environment * amplitude) ^ 2 =
        (retained ^ 2 + environment ^ 2) * amplitude ^ 2 := by ring
    _ = amplitude ^ 2 := by rw [hisometry]; ring

/-- Omitting the environment loses exactly its output intensity. -/
theorem omittedEnvironment_intensity_defect
    (retained environment amplitude : ℚ)
    (hisometry : retained ^ 2 + environment ^ 2 = 1) :
    scalarIntensity amplitude - scalarIntensity (retained * amplitude) =
      scalarIntensity (environment * amplitude) := by
  have hcomplement : 1 - retained ^ 2 = environment ^ 2 := by
    linarith
  unfold scalarIntensity
  calc
    amplitude ^ 2 - (retained * amplitude) ^ 2 =
        (1 - retained ^ 2) * amplitude ^ 2 := by ring
    _ = environment ^ 2 * amplitude ^ 2 := by rw [hcomplement]
    _ = (environment * amplitude) ^ 2 := by ring

/-- Exact finite efficiency witness used across Aspect's calibrated detector
packets. -/
theorem threeFourFive_loss_fixture :
    scalarIntensity ((3 / 5 : ℚ) * 1) = 9 / 25 ∧
      scalarIntensity ((4 / 5 : ℚ) * 1) = 16 / 25 ∧
      dilationIntensity (lossDilation (3 / 5) (4 / 5) 1) = 1 ∧
      scalarIntensity ((3 / 5 : ℚ) * 1) ≠ scalarIntensity 1 := by
  norm_num [scalarIntensity, dilationIntensity, lossDilation]

end LossEnvironmentDilation

section JointRecordMarginals

abbrev JointBinaryRecord := Fin 2 → Fin 2 → ℚ

def IsJointProbability (record : JointBinaryRecord) : Prop :=
  (∀ route marker, 0 ≤ record route marker) ∧
    ∑ route, ∑ marker, record route marker = 1

def correlatedJointRecord : JointBinaryRecord :=
  !![1 / 2, 0; 0, 1 / 2]

def anticorrelatedJointRecord : JointBinaryRecord :=
  !![0, 1 / 2; 1 / 2, 0]

def routeMarginal (record : JointBinaryRecord) : Fin 2 → ℚ :=
  fun route ↦ record route 0 + record route 1

def markerMarginal (record : JointBinaryRecord) : Fin 2 → ℚ :=
  fun marker ↦ record 0 marker + record 1 marker

/-- An unnormalized marker-selected route slice. Selection acts on an
already supplied joint record. -/
def markerSelectedSlice
    (record : JointBinaryRecord) (marker : Fin 2) : Fin 2 → ℚ :=
  fun route ↦ record route marker

/-- The unconditional route marginal is exactly the sum of the two selected
slices. -/
theorem routeMarginal_eq_sum_selectedSlices
    (record : JointBinaryRecord) (route : Fin 2) :
    routeMarginal record route =
      markerSelectedSlice record 0 route +
        markerSelectedSlice record 1 route := by
  rfl

theorem correlatedJointRecord_isProbability :
    IsJointProbability correlatedJointRecord := by
  constructor
  · intro route marker
    fin_cases route <;> fin_cases marker <;>
      norm_num [correlatedJointRecord]
  · norm_num [correlatedJointRecord, Fin.sum_univ_succ]

theorem anticorrelatedJointRecord_isProbability :
    IsJointProbability anticorrelatedJointRecord := by
  constructor
  · intro route marker
    fin_cases route <;> fin_cases marker <;>
      norm_num [anticorrelatedJointRecord]
  · norm_num [anticorrelatedJointRecord, Fin.sum_univ_succ]

/-- Equal flat marginals do not identify the joint route/marker correlation
pattern. -/
theorem equalMarginals_differentJointRecord_hostile :
    IsJointProbability correlatedJointRecord ∧
      IsJointProbability anticorrelatedJointRecord ∧
      correlatedJointRecord ≠ anticorrelatedJointRecord ∧
      routeMarginal correlatedJointRecord =
        routeMarginal anticorrelatedJointRecord ∧
      markerMarginal correlatedJointRecord =
        markerMarginal anticorrelatedJointRecord := by
  refine ⟨correlatedJointRecord_isProbability,
    anticorrelatedJointRecord_isProbability, ?_, ?_, ?_⟩
  · intro h
    have h00 := congrArg (fun record : JointBinaryRecord ↦ record 0 0) h
    norm_num [correlatedJointRecord, anticorrelatedJointRecord] at h00
  · funext route
    fin_cases route <;>
      norm_num [routeMarginal, correlatedJointRecord,
        anticorrelatedJointRecord]
  · funext marker
    fin_cases marker <;>
      norm_num [markerMarginal, correlatedJointRecord,
        anticorrelatedJointRecord]

/-- Equal unconditional route records can support different pre-existing
marker-selected slices.  Selection reveals the joint correlation; it does not
rewrite the marginal from which the slices were summed. -/
theorem postselection_partitions_not_produces_hostile :
    routeMarginal correlatedJointRecord =
        routeMarginal anticorrelatedJointRecord ∧
      markerSelectedSlice correlatedJointRecord 0 ≠
        markerSelectedSlice anticorrelatedJointRecord 0 := by
  constructor
  · funext route
    fin_cases route <;>
      norm_num [routeMarginal, correlatedJointRecord,
        anticorrelatedJointRecord]
  · intro h
    have h0 := congrArg (fun slice : Fin 2 → ℚ ↦ slice 0) h
    norm_num [markerSelectedSlice, correlatedJointRecord,
      anticorrelatedJointRecord] at h0

end JointRecordMarginals

section NonlinearAndStatisticalHostiles

/-- Real-coordinate intensity of one complex amplitude.  It is intentionally
not presented as a linear map. -/
def intensity (amplitude : Fin 2 → ℚ) : ℚ :=
  amplitude 0 ^ 2 + amplitude 1 ^ 2

/-- Rational real-coordinate action of a declared phase rotation. -/
def phaseRotate (cosine sine : ℚ) (amplitude : Fin 2 → ℚ) : Fin 2 → ℚ :=
  ![cosine * amplitude 0 - sine * amplitude 1,
    sine * amplitude 0 + cosine * amplitude 1]

/-- Intensity is invariant under every admitted rational orthogonal phase
rotation. -/
theorem intensity_phaseRotate_invariant
    (cosine sine : ℚ) (amplitude : Fin 2 → ℚ)
    (hunit : cosine ^ 2 + sine ^ 2 = 1) :
    intensity (phaseRotate cosine sine amplitude) = intensity amplitude := by
  unfold intensity phaseRotate
  change
    (cosine * amplitude 0 - sine * amplitude 1) ^ 2 +
        (sine * amplitude 0 + cosine * amplitude 1) ^ 2 =
      amplitude 0 ^ 2 + amplitude 1 ^ 2
  calc
    (cosine * amplitude 0 - sine * amplitude 1) ^ 2 +
          (sine * amplitude 0 + cosine * amplitude 1) ^ 2 =
        (cosine ^ 2 + sine ^ 2) *
          (amplitude 0 ^ 2 + amplitude 1 ^ 2) := by ring
    _ = amplitude 0 ^ 2 + amplitude 1 ^ 2 := by rw [hunit]; ring

def quarterTurn (amplitude : Fin 2 → ℚ) : Fin 2 → ℚ :=
  phaseRotate 0 1 amplitude

theorem quarterTurn_is_phaseRotate (amplitude : Fin 2 → ℚ) :
    quarterTurn amplitude = phaseRotate 0 1 amplitude := rfl

theorem intensity_quarterTurn_invariant (amplitude : Fin 2 → ℚ) :
    intensity (quarterTurn amplitude) = intensity amplitude := by
  exact intensity_phaseRotate_invariant 0 1 amplitude (by norm_num)

/-- Intensity cannot distinguish a field amplitude from its quarter-turn
phase rotation. -/
theorem intensity_phase_blind_hostile :
    let amplitude : Fin 2 → ℚ := ![3 / 5, 4 / 5]
    amplitude ≠ quarterTurn amplitude ∧
      intensity amplitude = intensity (quarterTurn amplitude) := by
  dsimp [quarterTurn, phaseRotate, intensity]
  constructor
  · intro h
    have h0 := congrFun h 0
    norm_num at h0
  · norm_num

def integratedCount (record : Fin 2 → Nat) : Nat := record 0 + record 1

def swapArrivalBins (record : Fin 2 → Nat) : Fin 2 → Nat :=
  ![record 1, record 0]

/-- Total counting is invariant under exchanging the two arrival bins. -/
theorem integratedCount_swap_invariant (record : Fin 2 → Nat) :
    integratedCount (swapArrivalBins record) = integratedCount record := by
  simp [integratedCount, swapArrivalBins, Nat.add_comm]

theorem swappedArrivalBins_indistinguishable (record : Fin 2 → Nat) :
    Indistinguishable integratedCount record (swapArrivalBins record) := by
  exact (integratedCount_swap_invariant record).symm

/-- Retaining the complete two-bin record is faithful before integration. -/
theorem timeResolvedRecord_faithful :
    Function.Injective (id : (Fin 2 → Nat) → (Fin 2 → Nat)) :=
  fun _ _ h ↦ h

/-- Integrated counts erase arrival-bin order. -/
theorem integrated_count_order_blind_hostile :
    let early : Fin 2 → Nat := ![1, 0]
    let late : Fin 2 → Nat := ![0, 1]
    early ≠ late ∧ integratedCount early = integratedCount late := by
  dsimp [integratedCount]
  constructor
  · intro h
    have h0 := congrFun h 0
    norm_num at h0
  · norm_num

def thresholdClick (count : Fin 3) : Bool := count != 0

/-- A threshold detector identifies one photon with two photons. -/
theorem threshold_not_numberResolving_hostile :
    (1 : Fin 3) ≠ 2 ∧ thresholdClick 1 = thresholdClick 2 := by
  decide

/-- The full finite number record itself remains faithful. -/
theorem numberRecord_faithful : Function.Injective (id : Fin 3 → Fin 3) :=
  fun _ _ h ↦ h

/-- A finite diagonal photon-number distribution.  Normalization and
nonnegativity are kept as explicit predicates instead of hidden structure. -/
abbrev PhotonDistribution₃ := Fin 3 → ℚ

def IsProbability (distribution : PhotonDistribution₃) : Prop :=
  (∀ n, 0 ≤ distribution n) ∧ ∑ n, distribution n = 1

def onePhoton : PhotonDistribution₃ :=
  fun n ↦ match n.val with
    | 1 => 1
    | _ => 0

def twoPhotons : PhotonDistribution₃ :=
  fun n ↦ match n.val with
    | 2 => 1
    | _ => 0

def zeroTwoMixture : PhotonDistribution₃ :=
  fun n ↦ match n.val with
    | 0 => 1 / 2
    | 2 => 1 / 2
    | _ => 0

/-- First and second moments on distributions supported on photon numbers
zero, one, and two. -/
def photonMean (distribution : PhotonDistribution₃) : ℚ :=
  distribution 1 + 2 * distribution 2

def photonSecondMoment (distribution : PhotonDistribution₃) : ℚ :=
  distribution 1 + 4 * distribution 2

def photonVariance (distribution : PhotonDistribution₃) : ℚ :=
  photonSecondMoment distribution - photonMean distribution ^ 2

def photonFactorialMoment₂ (distribution : PhotonDistribution₃) : ℚ :=
  2 * distribution 2

def photonG₂ (distribution : PhotonDistribution₃) : ℚ :=
  photonFactorialMoment₂ distribution / photonMean distribution ^ 2

def thresholdDistributionReadout
    (distribution : PhotonDistribution₃) : Fin 2 → ℚ :=
  ![distribution 0, distribution 1 + distribution 2]

/-- Detected-count distribution for a two-photon input under independently
calibrated intensity efficiency `efficiency`. -/
def twoPhotonLossDistribution (efficiency : ℚ) : PhotonDistribution₃ :=
  ![(1 - efficiency) ^ 2,
    2 * efficiency * (1 - efficiency),
    efficiency ^ 2]

theorem twoPhotonLossDistribution_normalized (efficiency : ℚ) :
    ∑ count, twoPhotonLossDistribution efficiency count = 1 := by
  simp [twoPhotonLossDistribution, Fin.sum_univ_succ]
  ring

theorem twoPhotonLossDistribution_nonnegative
    (efficiency : ℚ) (hzero : 0 ≤ efficiency) (hone : efficiency ≤ 1) :
    ∀ count, 0 ≤ twoPhotonLossDistribution efficiency count := by
  intro count
  fin_cases count
  · simpa [twoPhotonLossDistribution] using sq_nonneg (1 - efficiency)
  · simpa [twoPhotonLossDistribution] using
      mul_nonneg (mul_nonneg (by norm_num : (0 : ℚ) ≤ 2) hzero)
        (sub_nonneg.mpr hone)
  · simpa [twoPhotonLossDistribution] using sq_nonneg efficiency

theorem twoPhotonLossDistribution_isProbability
    (efficiency : ℚ) (hzero : 0 ≤ efficiency) (hone : efficiency ≤ 1) :
    IsProbability (twoPhotonLossDistribution efficiency) := by
  exact ⟨twoPhotonLossDistribution_nonnegative efficiency hzero hone,
    twoPhotonLossDistribution_normalized efficiency⟩

theorem twoPhotonLossDistribution_nineTwentyFifths :
    twoPhotonLossDistribution (9 / 25) =
      ![(256 / 625 : ℚ), 288 / 625, 81 / 625] := by
  funext count
  fin_cases count <;> norm_num [twoPhotonLossDistribution]

/-- First two moments of the detected optical count for a two-photon input. -/
def twoPhotonDetectedMean (efficiency : ℚ) : ℚ := 2 * efficiency

def twoPhotonDetectedVariance (efficiency : ℚ) : ℚ :=
  2 * efficiency * (1 - efficiency)

/-- Independent Bernoulli dark counts add their mean and variance to the
optical count moments.  Independence is an explicit premise of this formula,
not a conclusion inferred from the observed record. -/
def observedMeanWithDarkCount (efficiency darkProbability : ℚ) : ℚ :=
  twoPhotonDetectedMean efficiency + darkProbability

def observedVarianceWithDarkCount (efficiency darkProbability : ℚ) : ℚ :=
  twoPhotonDetectedVariance efficiency +
    darkProbability * (1 - darkProbability)

theorem subtractingDarkMean_recovers_opticalMean
    (efficiency darkProbability : ℚ) :
    observedMeanWithDarkCount efficiency darkProbability - darkProbability =
      twoPhotonDetectedMean efficiency := by
  unfold observedMeanWithDarkCount
  ring

/-- Subtracting the calibrated mean dark rate does not remove its variance. -/
theorem darkVariance_remains_after_mean_subtraction
    (efficiency darkProbability : ℚ) :
    observedVarianceWithDarkCount efficiency darkProbability -
        twoPhotonDetectedVariance efficiency =
      darkProbability * (1 - darkProbability) := by
  unfold observedVarianceWithDarkCount
  ring

theorem calibratedDarkCount_moment_fixture :
    observedMeanWithDarkCount (9 / 25) (1 / 10) = 41 / 50 ∧
      observedVarianceWithDarkCount (9 / 25) (1 / 10) = 1377 / 2500 ∧
      observedVarianceWithDarkCount (9 / 25) (1 / 10) ≠
        twoPhotonDetectedVariance (9 / 25) := by
  norm_num [observedMeanWithDarkCount, observedVarianceWithDarkCount,
    twoPhotonDetectedMean, twoPhotonDetectedVariance]

theorem onePhoton_isProbability : IsProbability onePhoton := by
  constructor
  · intro n
    fin_cases n <;> norm_num [onePhoton]
  · norm_num [onePhoton, Fin.sum_univ_succ]

theorem twoPhotons_isProbability : IsProbability twoPhotons := by
  constructor
  · intro n
    fin_cases n <;> norm_num [twoPhotons]
  · norm_num [twoPhotons, Fin.sum_univ_succ]

theorem zeroTwoMixture_isProbability : IsProbability zeroTwoMixture := by
  constructor
  · intro n
    fin_cases n <;> norm_num [zeroTwoMixture]
  · norm_num [zeroTwoMixture, Fin.sum_univ_succ]

/-- Equal mean intensity does not determine photon-number variance or the
second normalized factorial correlation. -/
theorem equalMean_differentPhotonStatistics_hostile :
    IsProbability onePhoton ∧ IsProbability zeroTwoMixture ∧
      photonMean onePhoton = 1 ∧ photonMean zeroTwoMixture = 1 ∧
      photonVariance onePhoton = 0 ∧ photonVariance zeroTwoMixture = 1 ∧
      photonG₂ onePhoton = 0 ∧ photonG₂ zeroTwoMixture = 1 := by
  refine ⟨onePhoton_isProbability, zeroTwoMixture_isProbability, ?_⟩
  norm_num [photonMean, photonVariance, photonSecondMoment,
    photonG₂, photonFactorialMoment₂, onePhoton, zeroTwoMixture]

/-- Even on normalized nonnegative distributions, threshold coarse-graining
identifies the certain one-photon and certain two-photon sources. -/
theorem threshold_distribution_not_faithful_on_probabilities :
    IsProbability onePhoton ∧ IsProbability twoPhotons ∧
      onePhoton ≠ twoPhotons ∧
      Indistinguishable thresholdDistributionReadout onePhoton twoPhotons := by
  refine ⟨onePhoton_isProbability, twoPhotons_isProbability, ?_, ?_⟩
  · intro h
    have h1 := congrFun h 1
    norm_num [onePhoton, twoPhotons] at h1
  · funext i
    fin_cases i <;>
      norm_num [Indistinguishable, thresholdDistributionReadout,
        onePhoton, twoPhotons]

/-- Four source bins, with the final bin representing counts beyond a
three-outcome truncated counter. -/
abbrev PhotonDistribution₄ := Fin 4 → ℚ

def IsProbability₄ (distribution : PhotonDistribution₄) : Prop :=
  (∀ n, 0 ≤ distribution n) ∧ ∑ n, distribution n = 1

def overflowOnlyDistribution : PhotonDistribution₄ :=
  fun n ↦ match n.val with
    | 3 => 1
    | _ => 0

/-- Incorrect truncation: the overflow coordinate is silently discarded. -/
def dropOverflowReadout (distribution : PhotonDistribution₄) : Fin 3 → ℚ :=
  ![distribution 0, distribution 1, distribution 2]

/-- Correct finite record: retain the declared overflow outcome. -/
def retainOverflowReadout (distribution : PhotonDistribution₄) : Fin 4 → ℚ :=
  distribution

theorem overflowOnlyDistribution_isProbability :
    IsProbability₄ overflowOnlyDistribution := by
  constructor
  · intro n
    fin_cases n <;> norm_num [overflowOnlyDistribution]
  · norm_num [overflowOnlyDistribution, Fin.sum_univ_succ]

theorem retainOverflowReadout_faithful :
    Function.Injective retainOverflowReadout :=
  fun _ _ h ↦ h

/-- Dropping overflow maps a valid nonzero source distribution to a zero,
unnormalized record. -/
theorem droppingOverflow_destroys_faithfulness_and_normalization :
    IsProbability₄ overflowOnlyDistribution ∧
      overflowOnlyDistribution ≠ 0 ∧
      dropOverflowReadout overflowOnlyDistribution = 0 ∧
      (∑ count, dropOverflowReadout overflowOnlyDistribution count) = 0 := by
  refine ⟨overflowOnlyDistribution_isProbability, ?_, ?_, ?_⟩
  · intro h
    have h3 := congrFun h 3
    norm_num [overflowOnlyDistribution] at h3
  · funext count
    fin_cases count <;>
      norm_num [dropOverflowReadout, overflowOnlyDistribution]
  · norm_num [dropOverflowReadout, overflowOnlyDistribution,
      Fin.sum_univ_succ]

end NonlinearAndStatisticalHostiles

section FiniteSamplingAliasing

/-- A finite sampler with `sampleCount` samples records an integer frequency
only through its residue class.  This is a finite quotient, not a continuum
frequency space or a sampling-reconstruction theorem. -/
def sampledFrequencyClass (sampleCount : ℕ) (frequency : ℤ) : ZMod sampleCount :=
  frequency

/-- Shifting an integer frequency by one sample rate does not change its
finite sampled-frequency class. -/
theorem sampledFrequencyClass_add_sampleRate
    (sampleCount : ℕ) (frequency : ℤ) :
    sampledFrequencyClass sampleCount (frequency + sampleCount) =
      sampledFrequencyClass sampleCount frequency := by
  simp [sampledFrequencyClass]

/-- Concrete four-sample alias from Aspect's finite-bandwidth packet: the
frequency indices `1` and `5` are distinct before sampling and identical
after sampling. -/
theorem fourSample_frequency_alias_hostile :
    (1 : ℤ) ≠ 5 ∧ sampledFrequencyClass 4 1 = sampledFrequencyClass 4 5 := by
  constructor
  · norm_num
  · decide

/-- Hence the four-sample frequency quotient is not faithful on unrestricted
integer frequencies.  A bandlimit or anti-alias premise is additional data. -/
theorem fourSample_frequency_readout_not_faithful :
    ¬ Function.Injective (sampledFrequencyClass 4) := by
  intro faithful
  have := faithful fourSample_frequency_alias_hostile.2
  exact fourSample_frequency_alias_hostile.1 this

end FiniteSamplingAliasing

section FiniteBandwidthProjection

/-- Three declared spectral bins before detector bandwidth restriction. -/
abbrev ThreeBinSpectrum := Fin 3 → ℚ

/-- A detector retaining only bins zero and one.  Bin two remains part of the
source type and lies outside the detector bandwidth. -/
def retainFirstTwoBins (spectrum : ThreeBinSpectrum) : Fin 2 → ℚ :=
  ![spectrum 0, spectrum 1]

def outOfBandUnitSpectrum : ThreeBinSpectrum := ![0, 0, 1]

/-- An out-of-band source is nonzero even though its retained record is zero. -/
theorem outOfBandUnitSpectrum_in_detectorKernel :
    outOfBandUnitSpectrum ≠ 0 ∧
      retainFirstTwoBins outOfBandUnitSpectrum = 0 := by
  constructor
  · intro h
    have h2 := congrFun h 2
    change (1 : ℚ) = 0 at h2
    norm_num at h2
  · funext bin
    fin_cases bin <;> norm_num [retainFirstTwoBins, outOfBandUnitSpectrum]

/-- Aspect's sign-flipped third-bin fixture: finite bandwidth identifies two
distinct unrestricted spectra. -/
theorem finiteBandwidth_signFlip_hostile :
    let first : ThreeBinSpectrum := ![1, 2, 3]
    let second : ThreeBinSpectrum := ![1, 2, -3]
    first ≠ second ∧ retainFirstTwoBins first = retainFirstTwoBins second := by
  dsimp
  constructor
  · intro h
    have h2 := congrFun h 2
    change (3 : ℚ) = -3 at h2
    norm_num at h2
  · rfl

/-- The declared bandlimited source class.  Its witness is source-side data;
it cannot be inferred merely from a zero detector record. -/
def FirstTwoBinBandlimited :=
  { spectrum : ThreeBinSpectrum // spectrum 2 = 0 }

def retainFirstTwoBandlimited
    (spectrum : FirstTwoBinBandlimited) : Fin 2 → ℚ :=
  retainFirstTwoBins spectrum.1

/-- Bandwidth projection becomes faithful only on the explicitly restricted
bandlimited source type. -/
theorem retainFirstTwoBandlimited_faithful :
    Function.Injective retainFirstTwoBandlimited := by
  intro first second equalRecords
  apply Subtype.ext
  funext bin
  fin_cases bin
  · exact congrFun equalRecords 0
  · exact congrFun equalRecords 1
  · exact first.2.trans second.2.symm

end FiniteBandwidthProjection

section FiniteCausalResponse

/-- A discrete-time input indexed by signed time.  The sign convention is
declared: nonpositive indices are present or past at observation time zero. -/
abbrev DiscreteTimeInput := ℤ → ℚ

def SamePastAtZero (first second : DiscreteTimeInput) : Prop :=
  ∀ time, time ≤ 0 → first time = second time

/-- The causal three-tap response from Aspect's packet, with delays
`0`, `1`, and `2`. -/
def causalThreeTapAtZero (input : DiscreteTimeInput) : ℚ :=
  input 0 + (1 / 2) * input (-1) + (1 / 4) * input (-2)

theorem causalThreeTap_respects_samePast
    {first second : DiscreteTimeInput}
    (samePast : SamePastAtZero first second) :
    causalThreeTapAtZero first = causalThreeTapAtZero second := by
  simp only [causalThreeTapAtZero]
  rw [samePast 0 (by omega), samePast (-1) (by omega),
    samePast (-2) (by omega)]

/-- A row with a coefficient at delay `-1` reads the future sample at time
`1`; naming it a frequency response does not make it causal. -/
def advancedTapAtZero (input : DiscreteTimeInput) : ℚ := input 1

def zeroTimeInput : DiscreteTimeInput := fun _ ↦ 0

def unitFuturePulse : DiscreteTimeInput :=
  fun time ↦ if time = 1 then 1 else 0

theorem zeroAndFuturePulse_have_samePast :
    SamePastAtZero zeroTimeInput unitFuturePulse := by
  intro time htime
  have hne : time ≠ 1 := by omega
  simp [zeroTimeInput, unitFuturePulse, hne]

/-- Hostile causality fixture: identical local histories can have different
present outputs when an advanced coefficient is admitted. -/
theorem advancedTap_depends_on_future_hostile :
    SamePastAtZero zeroTimeInput unitFuturePulse ∧
      advancedTapAtZero zeroTimeInput = 0 ∧
      advancedTapAtZero unitFuturePulse = 1 := by
  exact ⟨zeroAndFuturePulse_have_samePast, by rfl, by
    simp [advancedTapAtZero, unitFuturePulse]⟩

end FiniteCausalResponse

section FiniteWindowTail

/-- Squared magnitude of the stable impulse response `h n = 2⁻ⁿ`. -/
noncomputable def geometricImpulseEnergy (n : ℕ) : ℝ := (1 / 4 : ℝ) ^ n

theorem geometricImpulseEnergy_total :
    ∑' n, geometricImpulseEnergy n = 4 / 3 := by
  rw [show (4 / 3 : ℝ) = (1 - (1 / 4 : ℝ))⁻¹ by norm_num]
  exact tsum_geometric_of_norm_lt_one (by norm_num)

theorem geometricImpulseEnergy_firstThree :
    ∑ n ∈ Finset.range 3, geometricImpulseEnergy n = 21 / 16 := by
  norm_num [geometricImpulseEnergy, Finset.sum_range_succ]

/-- The certified total energy exceeds the three-sample window by exactly
`1/48`; stability therefore does not turn an observed prefix into a complete
record. -/
theorem geometricImpulseEnergy_omittedTail :
    (∑' n, geometricImpulseEnergy n) -
        (∑ n ∈ Finset.range 3, geometricImpulseEnergy n) = 1 / 48 := by
  rw [geometricImpulseEnergy_total, geometricImpulseEnergy_firstThree]
  norm_num

theorem geometricImpulseEnergy_omittedTail_positive :
    0 < (∑' n, geometricImpulseEnergy n) -
        (∑ n ∈ Finset.range 3, geometricImpulseEnergy n) := by
  rw [geometricImpulseEnergy_omittedTail]
  norm_num

end FiniteWindowTail

section PointwiseInverseUniformGap

/-- A sampled positive singular value tending toward the unresolved boundary. -/
noncomputable def sampledSmallSingularValue (n : ℕ) : ℝ :=
  1 / (n + 1)

/-- The corresponding scalar inverse gain. -/
noncomputable def sampledInverseGain (n : ℕ) : ℝ := n + 1

/-- Every finite sample has an exact inverse. -/
theorem sampledSmallSingularValue_pointwise_inverse (n : ℕ) :
    sampledSmallSingularValue n * sampledInverseGain n = 1 := by
  unfold sampledSmallSingularValue sampledInverseGain
  have positive : (0 : ℝ) < n + 1 := by positivity
  field_simp

/-- Nevertheless the inverse gains have no cutoff-independent upper bound. -/
theorem sampledInverseGain_unbounded (bound : ℝ) :
    ∃ n : ℕ, bound < sampledInverseGain n := by
  obtain ⟨n, hn⟩ := exists_nat_gt bound
  refine ⟨n, hn.trans ?_⟩
  simp [sampledInverseGain]

/-- Pointwise invertibility therefore does not supply uniform inverse control. -/
theorem pointwiseInverse_does_not_imply_uniformBound :
    (∀ n, sampledSmallSingularValue n * sampledInverseGain n = 1) ∧
      ¬ ∃ bound : ℝ, ∀ n, sampledInverseGain n ≤ bound := by
  refine ⟨sampledSmallSingularValue_pointwise_inverse, ?_⟩
  rintro ⟨bound, bounded⟩
  obtain ⟨n, hn⟩ := sampledInverseGain_unbounded bound
  exact (not_lt_of_ge (bounded n)) hn

end PointwiseInverseUniformGap

section FinitePrefixAsymptoticGap

def SameFinitePrefix {Value : Type*}
    (cutoff : ℕ) (first second : ℕ → Value) : Prop :=
  ∀ n, n < cutoff → first n = second n

/-- A declared infinite-time readout descends through a finite prefix only if
prefix-identical streams always have the same readout. -/
def FinitePrefixDetermines {Value Result : Type*}
    (cutoff : ℕ) (readout : (ℕ → Value) → Result) : Prop :=
  ∀ first second, SameFinitePrefix cutoff first second →
    readout first = readout second

/-- Reusable obstruction: one prefix collision separated by the asymptotic
readout refutes descent through that finite observation window. -/
theorem finitePrefix_does_not_determine_of_separated_collision
    {Value Result : Type*} {cutoff : ℕ}
    {readout : (ℕ → Value) → Result}
    {first second : ℕ → Value}
    (samePrefix : SameFinitePrefix cutoff first second)
    (separated : readout first ≠ readout second) :
    ¬ FinitePrefixDetermines cutoff readout := by
  intro determines
  exact separated (determines first second samePrefix)

def zeroStream : ℕ → ℚ := fun _ ↦ 0

def delayedOneStream (cutoff : ℕ) : ℕ → ℚ :=
  fun n ↦ if n < cutoff then 0 else 1

theorem zeroAndDelayedOne_sameFinitePrefix (cutoff : ℕ) :
    SameFinitePrefix cutoff zeroStream (delayedOneStream cutoff) := by
  intro n hn
  simp [zeroStream, delayedOneStream, hn]

/-- The concrete streams from Aspect's packet.  Their Cesàro means require a
separately named mean functional and convergence theorem; this lemma records
exactly the finite-prefix evidence available before that analytic interface. -/
theorem finitePrefix_has_zero_then_one_hostile (cutoff : ℕ) :
    SameFinitePrefix cutoff zeroStream (delayedOneStream cutoff) ∧
      (∀ n, cutoff ≤ n → delayedOneStream cutoff n = 1) := by
  refine ⟨zeroAndDelayedOne_sameFinitePrefix cutoff, ?_⟩
  intro n hn
  simp [delayedOneStream, Nat.not_lt.mpr hn]

end FinitePrefixAsymptoticGap

section PositiveImpedanceDarkReflection

/-- Normalized driving-point impedance on positive real probes.  This is the
real-axis algebraic shadow of the half-plane packet, not an analytic
positive-real function class. -/
noncomputable def normalizedPositiveAxisImpedance
    (scale probe : ℝ) : ℝ := probe / scale

/-- Reflection readout after the unit-reference Cayley convention. -/
noncomputable def unitReferenceReflection
    (scale probe : ℝ) : ℝ :=
  let impedance := normalizedPositiveAxisImpedance scale probe
  (impedance - 1) / (impedance + 1)

theorem normalizedPositiveAxisImpedance_positive
    {scale probe : ℝ} (scalePositive : 0 < scale)
    (probePositive : 0 < probe) :
    0 < normalizedPositiveAxisImpedance scale probe := by
  exact div_pos probePositive scalePositive

theorem unitReferenceReflection_eq_ratio
    {scale probe : ℝ} (scaleNonzero : scale ≠ 0) :
    unitReferenceReflection scale probe =
      (probe - scale) / (probe + scale) := by
  unfold unitReferenceReflection normalizedPositiveAxisImpedance
  field_simp

/-- At the matched positive probe, impedance equals one and the selected
reflection row is dark. -/
theorem matchedPositiveImpedance_has_darkReflection
    {scale : ℝ} (scalePositive : 0 < scale) :
    normalizedPositiveAxisImpedance scale scale = 1 ∧
      unitReferenceReflection scale scale = 0 := by
  have scaleNonzero := ne_of_gt scalePositive
  constructor
  · simp [normalizedPositiveAxisImpedance, scaleNonzero]
  · rw [unitReferenceReflection_eq_ratio scaleNonzero]
    simp

/-- Positive impedance values do not imply a nonvanishing Cayley reflection
readout.  Port type and constructor order remain essential. -/
theorem positiveImpedance_does_not_force_nonzeroReflection :
    ∀ scale : ℝ, 0 < scale →
      (∀ probe : ℝ, 0 < probe →
        0 < normalizedPositiveAxisImpedance scale probe) ∧
      unitReferenceReflection scale scale = 0 := by
  intro scale scalePositive
  exact ⟨fun _ probePositive ↦
    normalizedPositiveAxisImpedance_positive scalePositive probePositive,
    (matchedPositiveImpedance_has_darkReflection scalePositive).2⟩

/-- Complex right-half-plane impedance with the positive real scale fixed
before probing. -/
noncomputable def complexNormalizedImpedance
    (scale : ℝ) (probe : ℂ) : ℂ :=
  (scale⁻¹ : ℂ) * probe

/-- The corresponding selected reflection coefficient in its reduced ratio
form.  Its codomain is a wave ratio, not the impedance codomain. -/
noncomputable def complexUnitReferenceReflection
    (scale : ℝ) (probe : ℂ) : ℂ :=
  (probe - scale) / (probe + scale)

theorem complexNormalizedImpedance_re
    (scale : ℝ) (probe : ℂ) :
    (complexNormalizedImpedance scale probe).re =
      scale⁻¹ * probe.re := by
  simp [complexNormalizedImpedance]

/-- Strict positivity of the impedance real part throughout the declared open
right half-plane. -/
theorem complexNormalizedImpedance_strictlyPositive
    {scale : ℝ} (scalePositive : 0 < scale)
    {probe : ℂ} (rightHalfPlane : 0 < probe.re) :
    0 < (complexNormalizedImpedance scale probe).re := by
  rw [complexNormalizedImpedance_re]
  exact mul_pos (inv_pos.mpr scalePositive) rightHalfPlane

/-- The positive real probe `scale` is the unique numerator zero of the
reduced reflection ratio. -/
theorem complexReflection_dark_at_matchedProbe
    (scale : ℝ) :
    complexUnitReferenceReflection scale scale = 0 := by
  simp [complexUnitReferenceReflection]

/-- At the opposite probe the reduced reflection denominator vanishes. -/
theorem complexReflection_denominator_zero_at_oppositeProbe
    (scale : ℝ) :
    ((-(scale : ℂ)) + scale) = 0 := by
  ring

/-- Full finite hostile: strict right-half-plane impedance positivity coexists
with a selected reflection zero inside that half-plane. -/
theorem strictPositiveComplexImpedance_with_offSeamDarkReflection
    {scale : ℝ} (scalePositive : 0 < scale) :
    (∀ probe : ℂ, 0 < probe.re →
      0 < (complexNormalizedImpedance scale probe).re) ∧
      (0 : ℝ) < (scale : ℂ).re ∧
      complexUnitReferenceReflection scale scale = 0 := by
  exact ⟨fun _ hright ↦
    complexNormalizedImpedance_strictlyPositive scalePositive hright,
    by simpa using scalePositive,
    complexReflection_dark_at_matchedProbe scale⟩

end PositiveImpedanceDarkReflection

section ScalarSchurFirstJet

/-- Value of a scalar Schur complement `e - c a⁻¹ b`. -/
def scalarSchurValue (a b c e : ℚ) : ℚ :=
  e - c * a⁻¹ * b

/-- First jet of the Schur complement when `b` and `c` are static while the
retained scalar block `a` and boundary scalar `e` vary. -/
def scalarSchurFirstJet
    (a aFirst b c eFirst : ℚ) : ℚ :=
  eFirst + c * a⁻¹ * aFirst * a⁻¹ * b

/-- Determinant and first jet of the scalar-block matrix
`[[a,b],[c,e]]`, with static off-diagonal couplings. -/
def scalarBlockDeterminant (a b c e : ℚ) : ℚ := a * e - b * c

def scalarBlockDeterminantFirstJet
    (a aFirst e eFirst : ℚ) : ℚ :=
  aFirst * e + a * eFirst

theorem scalarBlockDeterminant_eq_retained_mul_schur
    {a b c e : ℚ} (aNonzero : a ≠ 0) :
    scalarBlockDeterminant a b c e =
      a * scalarSchurValue a b c e := by
  unfold scalarBlockDeterminant scalarSchurValue
  field_simp

/-- Exact logarithmic first-jet bonding law for one scalar boundary mode. -/
theorem scalarSchur_logJet_increment
    {a aFirst b c e eFirst : ℚ}
    (aNonzero : a ≠ 0)
    (detNonzero : scalarBlockDeterminant a b c e ≠ 0) :
    scalarBlockDeterminantFirstJet a aFirst e eFirst /
          scalarBlockDeterminant a b c e - aFirst / a =
      scalarSchurFirstJet a aFirst b c eFirst /
        scalarSchurValue a b c e := by
  have determinantFactorization :=
    scalarBlockDeterminant_eq_retained_mul_schur
      (a := a) (b := b) (c := c) (e := e) aNonzero
  have schurAsQuotient :
      scalarSchurValue a b c e =
        scalarBlockDeterminant a b c e / a := by
    apply (eq_div_iff aNonzero).2
    rw [determinantFactorization]
    ring
  rw [schurAsQuotient]
  have determinantExpressionNonzero : a * e - b * c ≠ 0 := by
    simpa [scalarBlockDeterminant] using detNonzero
  unfold scalarBlockDeterminantFirstJet scalarBlockDeterminant
    scalarSchurFirstJet
  field_simp [aNonzero, determinantExpressionNonzero]
  field_simp [determinantExpressionNonzero]
  ring

/-- Hostile to the diagonal-only derivative: the boundary scalar has zero
first jet, but variation of the retained inverse block contributes `1/4`. -/
theorem dropping_mixedSchurJet_is_wrong_hostile :
    scalarSchurFirstJet 2 1 1 1 0 = 1 / 4 ∧
      scalarSchurFirstJet 2 1 1 1 0 ≠ 0 ∧
      (0 : ℚ) ≠ scalarSchurFirstJet 2 1 1 1 0 := by
  norm_num [scalarSchurFirstJet]

end ScalarSchurFirstJet

section DeterminantJetPathCoherence

/-- Value and first derivative of a determinant channel at one fixed
basepoint. -/
structure DeterminantFirstJet where
  value : ℚ
  first : ℚ
  deriving DecidableEq

def DeterminantFirstJet.logSlope (jet : DeterminantFirstJet) : ℚ :=
  jet.first / jet.value

/-- Local logarithmic increment between two retained-mode stages. -/
def determinantJetIncrement
    (source target : DeterminantFirstJet) : ℚ :=
  target.logSlope - source.logSlope

/-- First-jet increments telescope along every two-step mode-addition path. -/
theorem determinantJetIncrement_telescopes
    (base intermediate full : DeterminantFirstJet) :
    determinantJetIncrement base intermediate +
        determinantJetIncrement intermediate full =
      determinantJetIncrement base full := by
  unfold determinantJetIncrement
  ring

/-- Two constructor orders with the same base and full determinant jets have
the same total increment, regardless of their different intermediate block. -/
theorem determinantJet_two_orders_same_total
    (base firstIntermediate secondIntermediate full : DeterminantFirstJet) :
    determinantJetIncrement base firstIntermediate +
        determinantJetIncrement firstIntermediate full =
      determinantJetIncrement base secondIntermediate +
        determinantJetIncrement secondIntermediate full := by
  rw [determinantJetIncrement_telescopes,
    determinantJetIncrement_telescopes]

def sewingBaseJet : DeterminantFirstJet := ⟨1, 1⟩
def sewingFirstOrderIntermediate : DeterminantFirstJet := ⟨1, 2⟩
def sewingSecondOrderIntermediate : DeterminantFirstJet := ⟨1, 3⟩
def sewingFullJet : DeterminantFirstJet := ⟨1, 5⟩

/-- Concrete hostile: local increments remember constructor order, although
both ordered sums equal the endpoint increment. -/
theorem localSchurIncrements_orderDependent_but_totalCoherent :
    determinantJetIncrement sewingBaseJet sewingFirstOrderIntermediate = 1 ∧
      determinantJetIncrement sewingFirstOrderIntermediate sewingFullJet = 3 ∧
      determinantJetIncrement sewingBaseJet sewingSecondOrderIntermediate = 2 ∧
      determinantJetIncrement sewingSecondOrderIntermediate sewingFullJet = 2 ∧
      determinantJetIncrement sewingBaseJet sewingFirstOrderIntermediate ≠
        determinantJetIncrement sewingBaseJet sewingSecondOrderIntermediate ∧
      determinantJetIncrement sewingBaseJet sewingFirstOrderIntermediate +
          determinantJetIncrement sewingFirstOrderIntermediate sewingFullJet =
        determinantJetIncrement sewingBaseJet sewingSecondOrderIntermediate +
          determinantJetIncrement sewingSecondOrderIntermediate sewingFullJet := by
  norm_num [determinantJetIncrement, DeterminantFirstJet.logSlope,
    sewingBaseJet, sewingFirstOrderIntermediate,
    sewingSecondOrderIntermediate, sewingFullJet]

end DeterminantJetPathCoherence

section ReciprocalSectorJetSewing

/-- Reflection `z ↦ -z` preserves the determinant value at the basepoint and
reverses its first derivative. -/
def reflectDeterminantFirstJet
    (jet : DeterminantFirstJet) : DeterminantFirstJet :=
  ⟨jet.value, -jet.first⟩

/-- Product rule for determinant first jets. -/
def multiplyDeterminantFirstJets
    (left right : DeterminantFirstJet) : DeterminantFirstJet :=
  ⟨left.value * right.value,
    left.first * right.value + left.value * right.first⟩

/-- Finite reciprocal sector double `D₊(z)D₊(-z)` at first-jet level. -/
def sewReciprocalDeterminantJet
    (jet : DeterminantFirstJet) : DeterminantFirstJet :=
  multiplyDeterminantFirstJets jet (reflectDeterminantFirstJet jet)

theorem sewReciprocalDeterminantJet_value
    (jet : DeterminantFirstJet) :
    (sewReciprocalDeterminantJet jet).value = jet.value ^ 2 := by
  simp [sewReciprocalDeterminantJet, multiplyDeterminantFirstJets,
    reflectDeterminantFirstJet, pow_two]

/-- Reciprocal sewing cancels the odd first jet exactly. -/
theorem sewReciprocalDeterminantJet_first_zero
    (jet : DeterminantFirstJet) :
    (sewReciprocalDeterminantJet jet).first = 0 := by
  simp [sewReciprocalDeterminantJet, multiplyDeterminantFirstJets,
    reflectDeterminantFirstJet]
  ring

/-- Vanishing of the sewn odd jet does not imply that either unsown sector
has zero first derivative. -/
theorem sewnOddJet_zero_does_not_descend_to_sector_hostile :
    let direct : DeterminantFirstJet := ⟨2, 3⟩
    direct.first ≠ 0 ∧
      (reflectDeterminantFirstJet direct).first ≠ 0 ∧
      (sewReciprocalDeterminantJet direct).first = 0 := by
  norm_num [reflectDeterminantFirstJet, sewReciprocalDeterminantJet,
    multiplyDeterminantFirstJets]

end ReciprocalSectorJetSewing

section ThreeModeDeterminantChannels

/-- Denominator determinant in the eigenbasis with source eigenvalues
`1/2`, `1/4`, and `1/5`. -/
def threeModePositiveDenominator (probe : ℚ) : ℚ :=
  (probe + 3 / 2) * (probe + 5 / 4) * (probe + 6 / 5)

/-- Selected Cayley numerator determinant for the same three eigenmodes. -/
def threeModeCayleyNumerator (probe : ℚ) : ℚ :=
  (probe - 1 / 2) * (probe - 3 / 4) * (probe - 4 / 5)

/-- The denominator is strictly positive on every positive real probe. -/
theorem threeModePositiveDenominator_positive
    {probe : ℚ} (probePositive : 0 < probe) :
    0 < threeModePositiveDenominator probe := by
  unfold threeModePositiveDenominator
  positivity

/-- At the matched first eigenmode, the selected numerator is dark while the
driving-point denominator remains strictly positive. -/
theorem threeMode_darkNumerator_nonzeroDenominator_hostile :
    threeModeCayleyNumerator (1 / 2) = 0 ∧
      0 < threeModePositiveDenominator (1 / 2) ∧
      threeModePositiveDenominator (1 / 2) ≠ 0 := by
  norm_num [threeModeCayleyNumerator, threeModePositiveDenominator]

/-- Reciprocal sector product of the positive denominator channels. -/
def sewnThreeModeDenominator (probe : ℚ) : ℚ :=
  threeModePositiveDenominator probe *
    threeModePositiveDenominator (-probe)

/-- The finite sewn denominator is globally even as a rational polynomial. -/
theorem sewnThreeModeDenominator_even (probe : ℚ) :
    sewnThreeModeDenominator (-probe) = sewnThreeModeDenominator probe := by
  simp [sewnThreeModeDenominator, mul_comm]

end ThreeModeDeterminantChannels

section ZeroFreeCompletionHostile

/-- Constant determinant channel at finite stage `n`. -/
noncomputable def vanishingZeroFreeStage
    (n : ℕ) (_probe : ℚ) : ℝ :=
  (1 / 2 : ℝ) ^ n

/-- Its explicit uniform error against the zero limit function. -/
noncomputable def vanishingStageUniformError (n : ℕ) : ℝ :=
  (1 / 2 : ℝ) ^ n

theorem vanishingZeroFreeStage_nonzero
    (n : ℕ) (probe : ℚ) :
    vanishingZeroFreeStage n probe ≠ 0 := by
  exact pow_ne_zero _ (by norm_num)

theorem vanishingStageUniformError_tendsto_zero :
    Filter.Tendsto vanishingStageUniformError Filter.atTop (nhds 0) := by
  exact tendsto_pow_atTop_nhds_zero_of_lt_one (by norm_num) (by norm_num)

/-- The same geometric error bounds every probe, so convergence to zero is
uniform in the declared probe variable. -/
theorem vanishingZeroFreeStage_uniform_error
    (n : ℕ) (probe : ℚ) :
    |vanishingZeroFreeStage n probe - 0| ≤
      vanishingStageUniformError n := by
  simp [vanishingZeroFreeStage, vanishingStageUniformError, abs_of_nonneg]

/-- Even an explicit uniform limit of zero-free finite stages may be the zero
function.  A Hurwitz-style nonvanishing conclusion needs an additional
nonzero normalization or exclusion of the identically-zero limit. -/
theorem finiteZeroFreeStages_can_uniformlyCollapse_to_zero :
    (∀ n probe, vanishingZeroFreeStage n probe ≠ 0) ∧
      Filter.Tendsto vanishingStageUniformError Filter.atTop (nhds 0) ∧
      (∀ n probe,
        |vanishingZeroFreeStage n probe - 0| ≤
          vanishingStageUniformError n) ∧
      (∃ probe : ℚ, (0 : ℚ → ℝ) probe = 0) := by
  exact ⟨vanishingZeroFreeStage_nonzero,
    vanishingStageUniformError_tendsto_zero,
    vanishingZeroFreeStage_uniform_error,
    ⟨0, rfl⟩⟩

end ZeroFreeCompletionHostile

section NormalizedCompletionGate

/-- An approximation remains nonzero at a normalized basepoint whenever its
error is strictly smaller than the limiting magnitude there. -/
theorem nonzero_of_error_lt_limitMagnitude
    {stage limit error : ℝ}
    (errorBound : |stage - limit| ≤ error)
    (errorSmall : error < |limit|) :
    stage ≠ 0 := by
  intro stageZero
  subst stage
  have : |limit| ≤ error := by
    simpa [abs_neg] using errorBound
  exact (not_lt_of_ge this) errorSmall

/-- Source-normalized stages converging to the fixed basepoint value one. -/
noncomputable def normalizedNonzeroStage
    (n : ℕ) (_probe : ℚ) : ℝ :=
  1 + (1 / 2 : ℝ) ^ (n + 1)

noncomputable def normalizedStageUniformError (n : ℕ) : ℝ :=
  (1 / 2 : ℝ) ^ (n + 1)

theorem normalizedStage_error_exact
    (n : ℕ) (probe : ℚ) :
    |normalizedNonzeroStage n probe - 1| =
      normalizedStageUniformError n := by
  simp [normalizedNonzeroStage, normalizedStageUniformError, abs_of_nonneg]

theorem normalizedStage_error_lt_basepointMagnitude (n : ℕ) :
    normalizedStageUniformError n < |(1 : ℝ)| := by
  rw [normalizedStageUniformError, abs_of_nonneg (by norm_num : (0 : ℝ) ≤ 1)]
  exact pow_lt_one₀ (by norm_num : (0 : ℝ) ≤ 1 / 2)
    (by norm_num : (1 / 2 : ℝ) < 1) (Nat.succ_ne_zero n)

/-- The fixed nonzero normalization blocks the uniform-collapse hostile at
every finite stage. -/
theorem normalizedNonzeroStage_nonzero
    (n : ℕ) (probe : ℚ) :
    normalizedNonzeroStage n probe ≠ 0 := by
  apply nonzero_of_error_lt_limitMagnitude
    (error := normalizedStageUniformError n) (limit := 1)
  · exact (normalizedStage_error_exact n probe).le
  · exact normalizedStage_error_lt_basepointMagnitude n

theorem normalizedStageUniformError_tendsto_zero :
    Filter.Tendsto normalizedStageUniformError Filter.atTop (nhds 0) := by
  have scaled :=
    vanishingStageUniformError_tendsto_zero.const_mul (1 / 2 : ℝ)
  convert scaled using 1
  funext n
  simp only [normalizedStageUniformError, vanishingStageUniformError,
    pow_succ]
  ring
  norm_num

end NormalizedCompletionGate

section TypedLogarithmicDeterminantJets

/-- A logarithmic determinant jet is admitted only with an explicit nonzero
basepoint value. -/
def NonvanishingDeterminantFirstJet :=
  { jet : DeterminantFirstJet // jet.value ≠ 0 }

def NonvanishingDeterminantFirstJet.logSlope
    (jet : NonvanishingDeterminantFirstJet) : ℚ :=
  jet.1.first / jet.1.value

def reflectNonvanishingDeterminantJet
    (jet : NonvanishingDeterminantFirstJet) :
    NonvanishingDeterminantFirstJet :=
  ⟨reflectDeterminantFirstJet jet.1, by
    simpa [reflectDeterminantFirstJet] using jet.2⟩

def multiplyNonvanishingDeterminantJets
    (left right : NonvanishingDeterminantFirstJet) :
    NonvanishingDeterminantFirstJet :=
  ⟨multiplyDeterminantFirstJets left.1 right.1, by
    simp only [multiplyDeterminantFirstJets]
    exact mul_ne_zero left.2 right.2⟩

theorem reflectedTypedLogSlope_neg
    (jet : NonvanishingDeterminantFirstJet) :
    (reflectNonvanishingDeterminantJet jet).logSlope = -jet.logSlope := by
  simp [NonvanishingDeterminantFirstJet.logSlope,
    reflectNonvanishingDeterminantJet, reflectDeterminantFirstJet]
  ring

/-- The product rule becomes addition of logarithmic slopes once both
nonvanishing witnesses are present. -/
theorem multipliedTypedLogSlope_add
    (left right : NonvanishingDeterminantFirstJet) :
    (multiplyNonvanishingDeterminantJets left right).logSlope =
      left.logSlope + right.logSlope := by
  rcases left with ⟨⟨leftValue, leftFirst⟩, leftNonzero⟩
  rcases right with ⟨⟨rightValue, rightFirst⟩, rightNonzero⟩
  simp only [NonvanishingDeterminantFirstJet.logSlope,
    multiplyNonvanishingDeterminantJets,
    multiplyDeterminantFirstJets]
  field_simp [leftNonzero, rightNonzero]

def sewNonvanishingReciprocalJet
    (jet : NonvanishingDeterminantFirstJet) :
    NonvanishingDeterminantFirstJet :=
  multiplyNonvanishingDeterminantJets jet
    (reflectNonvanishingDeterminantJet jet)

theorem sewnTypedLogSlope_zero
    (jet : NonvanishingDeterminantFirstJet) :
    (sewNonvanishingReciprocalJet jet).logSlope = 0 := by
  rw [sewNonvanishingReciprocalJet, multipliedTypedLogSlope_add,
    reflectedTypedLogSlope_neg]
  ring

def zeroValuedRawDeterminantJet : DeterminantFirstJet := ⟨0, 1⟩

/-- Hostile to Lean's totalized division: the raw formula returns zero at a
zero denominator, but no typed logarithmic determinant jet can carry this
underlying record. -/
theorem totalizedDivision_does_not_authorize_logarithmicJet :
    zeroValuedRawDeterminantJet.logSlope = 0 ∧
      ¬ ∃ typed : NonvanishingDeterminantFirstJet,
        typed.1 = zeroValuedRawDeterminantJet := by
  constructor
  · norm_num [DeterminantFirstJet.logSlope, zeroValuedRawDeterminantJet]
  · rintro ⟨typed, typedValue⟩
    have := typed.2
    rw [typedValue] at this
    exact this rfl

end TypedLogarithmicDeterminantJets

section TypedDeterminantJetPaths

def typedDeterminantJetIncrement
    (source target : NonvanishingDeterminantFirstJet) : ℚ :=
  target.logSlope - source.logSlope

theorem typedDeterminantJetIncrement_telescopes
    (base intermediate full : NonvanishingDeterminantFirstJet) :
    typedDeterminantJetIncrement base intermediate +
        typedDeterminantJetIncrement intermediate full =
      typedDeterminantJetIncrement base full := by
  unfold typedDeterminantJetIncrement
  ring

theorem typedDeterminantJet_two_orders_same_total
    (base firstIntermediate secondIntermediate full :
      NonvanishingDeterminantFirstJet) :
    typedDeterminantJetIncrement base firstIntermediate +
        typedDeterminantJetIncrement firstIntermediate full =
      typedDeterminantJetIncrement base secondIntermediate +
        typedDeterminantJetIncrement secondIntermediate full := by
  rw [typedDeterminantJetIncrement_telescopes,
    typedDeterminantJetIncrement_telescopes]

def rawZeroIntermediateJet : DeterminantFirstJet := ⟨0, 7⟩

/-- Raw totalized slopes still telescope numerically through a zero-valued
intermediate, but that intermediate is not an admissible logarithmic stage. -/
theorem rawTelescoping_does_not_authorize_zeroIntermediate :
    determinantJetIncrement sewingBaseJet rawZeroIntermediateJet = -1 ∧
      determinantJetIncrement rawZeroIntermediateJet sewingFullJet = 5 ∧
      determinantJetIncrement sewingBaseJet rawZeroIntermediateJet +
          determinantJetIncrement rawZeroIntermediateJet sewingFullJet = 4 ∧
      ¬ ∃ typed : NonvanishingDeterminantFirstJet,
        typed.1 = rawZeroIntermediateJet := by
  constructor
  · norm_num [determinantJetIncrement, DeterminantFirstJet.logSlope,
      sewingBaseJet, rawZeroIntermediateJet]
  constructor
  · norm_num [determinantJetIncrement, DeterminantFirstJet.logSlope,
      sewingFullJet, rawZeroIntermediateJet]
  constructor
  · norm_num [determinantJetIncrement, DeterminantFirstJet.logSlope,
      sewingBaseJet, sewingFullJet, rawZeroIntermediateJet]
  · rintro ⟨typed, typedValue⟩
    have := typed.2
    rw [typedValue] at this
    exact this rfl

end TypedDeterminantJetPaths

section AspectThreeModeTypedPath

/-- Exact determinant value/derivative data derived from Aspect's source-fixed
three-mode rational matrix at `z=0`. -/
def aspectThreeModeBaseJet : NonvanishingDeterminantFirstJet :=
  ⟨⟨55463 / 42250, 1⟩, by norm_num⟩

def aspectThreeModeOrder12IntermediateJet :
    NonvanishingDeterminantFirstJet :=
  ⟨⟨12243 / 6760, 9151 / 3380⟩, by norm_num⟩

def aspectThreeModeOrder21IntermediateJet :
    NonvanishingDeterminantFirstJet :=
  ⟨⟨6891 / 4225, 107963 / 42250⟩, by norm_num⟩

def aspectThreeModeFullJet : NonvanishingDeterminantFirstJet :=
  ⟨⟨9 / 4, 207 / 40⟩, by norm_num⟩

theorem aspectThreeMode_order12_exactIncrements :
    typedDeterminantJetIncrement aspectThreeModeBaseJet
        aspectThreeModeOrder12IntermediateJet =
      497817076 / 679033509 ∧
    typedDeterminantJetIncrement aspectThreeModeOrder12IntermediateJet
        aspectThreeModeFullJet = 98569 / 122430 := by
  norm_num [typedDeterminantJetIncrement,
    NonvanishingDeterminantFirstJet.logSlope,
    aspectThreeModeBaseJet, aspectThreeModeOrder12IntermediateJet,
    aspectThreeModeFullJet]

theorem aspectThreeMode_order21_exactIncrements :
    typedDeterminantJetIncrement aspectThreeModeBaseJet
        aspectThreeModeOrder21IntermediateJet =
      3076504369 / 3821955330 ∧
    typedDeterminantJetIncrement aspectThreeModeOrder21IntermediateJet
        aspectThreeModeFullJet = 5053 / 6891 := by
  norm_num [typedDeterminantJetIncrement,
    NonvanishingDeterminantFirstJet.logSlope,
    aspectThreeModeBaseJet, aspectThreeModeOrder21IntermediateJet,
    aspectThreeModeFullJet]

/-- The source network's two actual constructor orders have different local
increments but the same full-minus-base logarithmic jet. -/
theorem aspectThreeMode_typedOrders_localDifference_globalCoherence :
    typedDeterminantJetIncrement aspectThreeModeBaseJet
        aspectThreeModeOrder12IntermediateJet ≠
      typedDeterminantJetIncrement aspectThreeModeBaseJet
        aspectThreeModeOrder21IntermediateJet ∧
    typedDeterminantJetIncrement aspectThreeModeBaseJet
          aspectThreeModeOrder12IntermediateJet +
        typedDeterminantJetIncrement aspectThreeModeOrder12IntermediateJet
          aspectThreeModeFullJet = 853149 / 554630 ∧
    typedDeterminantJetIncrement aspectThreeModeBaseJet
          aspectThreeModeOrder21IntermediateJet +
        typedDeterminantJetIncrement aspectThreeModeOrder21IntermediateJet
          aspectThreeModeFullJet = 853149 / 554630 := by
  norm_num [typedDeterminantJetIncrement,
    NonvanishingDeterminantFirstJet.logSlope,
    aspectThreeModeBaseJet, aspectThreeModeOrder12IntermediateJet,
    aspectThreeModeOrder21IntermediateJet, aspectThreeModeFullJet]

end AspectThreeModeTypedPath

section AspectThreeModeActualSchurJet

/-- Exact first retained scalar block and coupling from Aspect's calibrated
three-mode matrix. -/
def aspectFirstRetainedValue : ℚ := 55463 / 42250
def aspectFirstRetainedJet : ℚ := 1
def aspectFirstBoundaryCoupling : ℚ := 2967 / 21125
def aspectFirstBoundaryValue : ℚ := 117849 / 84500
def aspectFirstBoundaryJet : ℚ := 1

def aspectFirstMixedSchurJet : ℚ :=
  aspectFirstBoundaryCoupling * aspectFirstRetainedValue⁻¹ *
    aspectFirstRetainedJet * aspectFirstRetainedValue⁻¹ *
    aspectFirstBoundaryCoupling

theorem aspectFirstSchurValue_exact :
    scalarSchurValue aspectFirstRetainedValue
        aspectFirstBoundaryCoupling aspectFirstBoundaryCoupling
        aspectFirstBoundaryValue = 306075 / 221852 := by
  norm_num [scalarSchurValue, aspectFirstRetainedValue,
    aspectFirstBoundaryCoupling, aspectFirstBoundaryValue]

theorem aspectFirstMixedSchurJet_exact_nonzero :
    aspectFirstMixedSchurJet = 35212356 / 3076144369 ∧
      aspectFirstMixedSchurJet ≠ 0 := by
  norm_num [aspectFirstMixedSchurJet, aspectFirstBoundaryCoupling,
    aspectFirstRetainedValue, aspectFirstRetainedJet]

theorem aspectFirstSchurFirstJet_exact :
    scalarSchurFirstJet aspectFirstRetainedValue
        aspectFirstRetainedJet aspectFirstBoundaryCoupling
        aspectFirstBoundaryCoupling aspectFirstBoundaryJet =
      3111356725 / 3076144369 := by
  norm_num [scalarSchurFirstJet, aspectFirstRetainedValue,
    aspectFirstRetainedJet, aspectFirstBoundaryCoupling,
    aspectFirstBoundaryJet]

/-- The actual Schur logarithmic jet equals the first typed determinant-path
increment, while the diagonal-only value one does not. -/
theorem aspectFirstSchurJet_matches_typedIncrement_and_rejects_diagonalOnly :
    scalarSchurFirstJet aspectFirstRetainedValue
          aspectFirstRetainedJet aspectFirstBoundaryCoupling
          aspectFirstBoundaryCoupling aspectFirstBoundaryJet /
        scalarSchurValue aspectFirstRetainedValue
          aspectFirstBoundaryCoupling aspectFirstBoundaryCoupling
          aspectFirstBoundaryValue =
      typedDeterminantJetIncrement aspectThreeModeBaseJet
        aspectThreeModeOrder12IntermediateJet ∧
    aspectFirstBoundaryJet /
          scalarSchurValue aspectFirstRetainedValue
            aspectFirstBoundaryCoupling aspectFirstBoundaryCoupling
            aspectFirstBoundaryValue ≠
      typedDeterminantJetIncrement aspectThreeModeBaseJet
        aspectThreeModeOrder12IntermediateJet := by
  norm_num [scalarSchurFirstJet, scalarSchurValue,
    typedDeterminantJetIncrement,
    NonvanishingDeterminantFirstJet.logSlope,
    aspectFirstRetainedValue, aspectFirstRetainedJet,
    aspectFirstBoundaryCoupling, aspectFirstBoundaryValue,
    aspectFirstBoundaryJet, aspectThreeModeBaseJet,
    aspectThreeModeOrder12IntermediateJet]

end AspectThreeModeActualSchurJet

section FiniteTailSeamCutEnergy

/-- Squared energy of the first `length` samples of a rational source. -/
def finitePrefixEnergy (source : ℕ → ℚ) (length : ℕ) : ℚ :=
  ∑ k ∈ Finset.range length, source k ^ 2

def shiftedEnergySource (source : ℕ → ℚ) (offset : ℕ) : ℕ → ℚ :=
  fun k ↦ source (offset + k)

/-- Exact finite cut isometry: total interval energy is prefix energy plus the
energy of the translated tail interval. -/
theorem finitePrefixEnergy_add
    (source : ℕ → ℚ) (first second : ℕ) :
    finitePrefixEnergy source (first + second) =
      finitePrefixEnergy source first +
        finitePrefixEnergy (shiftedEnergySource source first) second := by
  simp only [finitePrefixEnergy, shiftedEnergySource, Finset.sum_range_add]

/-- Two staged cuts reconstruct the same three-piece energy decomposition as
one cut at the combined marked positions. -/
theorem finiteTailSeam_twoStage_energy
    (source : ℕ → ℚ) (first second third : ℕ) :
    finitePrefixEnergy source (first + second + third) =
      finitePrefixEnergy source first +
        finitePrefixEnergy (shiftedEnergySource source first) second +
        finitePrefixEnergy
          (shiftedEnergySource source (first + second)) third := by
  rw [finitePrefixEnergy_add source (first + second) third,
    finitePrefixEnergy_add source first second]

def seamOnlyUnitSource : ℕ → ℚ
  | 0 => 1
  | _ => 0

/-- Tail-only observation may vanish after a cut even though the retained seam
prefix carries nonzero energy. -/
theorem vanishingTail_does_not_erase_seamEnergy :
    finitePrefixEnergy seamOnlyUnitSource 1 = 1 ∧
      finitePrefixEnergy (shiftedEnergySource seamOnlyUnitSource 1) 2 = 0 ∧
      finitePrefixEnergy seamOnlyUnitSource 1 +
          finitePrefixEnergy
            (shiftedEnergySource seamOnlyUnitSource 1) 2 = 1 := by
  norm_num [finitePrefixEnergy, shiftedEnergySource, seamOnlyUnitSource,
    Finset.sum_range_succ]

end FiniteTailSeamCutEnergy

end MariciFormal.FiniteInstrumentReadout
