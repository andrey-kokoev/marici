import Mathlib

/-!
Typed Rosenbrock transmission-zero compiler and Sontag's exact passive
selected-port hostile.  This is a finite control gate, not a theta realization
or an RH theorem.
-/

namespace MariciFormal.RosenbrockTransmissionZero

variable (F State Input Output : Type*)
  [Field F]
  [AddCommGroup State] [Module F State]
  [AddCommGroup Input] [Module F Input]
  [AddCommGroup Output] [Module F Output]

/-- Linear discrete-time realization `x⁺=Ax+Bu`, `y=Cx+Du`. -/
structure LinearControlSystem where
  A : State →ₗ[F] State
  B : Input →ₗ[F] State
  C : State →ₗ[F] Output
  D : Input →ₗ[F] Output

namespace LinearControlSystem

variable {F State Input Output : Type*}
  [Field F]
  [AddCommGroup State] [Module F State]
  [AddCommGroup Input] [Module F Input]
  [AddCommGroup Output] [Module F Output]

/-- Rosenbrock operator at spectral parameter `parameter`. -/
def rosenbrock
    (system : LinearControlSystem F State Input Output) (parameter : F) :
    (State × Input) →ₗ[F] (State × Output) where
  toFun stateInput :=
    (parameter • stateInput.1 - system.A stateInput.1 - system.B stateInput.2,
      system.C stateInput.1 + system.D stateInput.2)
  map_add' := by
    intro first second
    ext <;> simp [sub_eq_add_neg, add_assoc, add_comm, add_left_comm]
  map_smul' := by
    intro scalar stateInput
    apply Prod.ext
    · change parameter • (scalar • stateInput.1) -
          system.A (scalar • stateInput.1) -
          system.B (scalar • stateInput.2) =
        scalar • (parameter • stateInput.1 -
          system.A stateInput.1 - system.B stateInput.2)
      simp only [map_smul]
      module
    · change system.C (scalar • stateInput.1) +
          system.D (scalar • stateInput.2) =
        scalar • (system.C stateInput.1 + system.D stateInput.2)
      simp only [map_smul]
      module

/-- An invariant transmission zero is a nonzero state-input pair in the
Rosenbrock kernel. -/
def HasTransmissionZero
    (system : LinearControlSystem F State Input Output) (parameter : F) : Prop :=
  ∃ stateInput : State × Input,
    stateInput ≠ 0 ∧ system.rosenbrock parameter stateInput = 0

/-- Expanded compiler: the kernel condition is exactly the state equation and
dark-output equation. -/
theorem hasTransmissionZero_iff
    (system : LinearControlSystem F State Input Output) (parameter : F) :
    system.HasTransmissionZero parameter ↔
      ∃ state : State, ∃ input : Input,
        (state, input) ≠ 0 ∧
        parameter • state - system.A state - system.B input = 0 ∧
        system.C state + system.D input = 0 := by
  unfold HasTransmissionZero
  constructor
  · rintro ⟨⟨state, input⟩, nonzero, equations⟩
    have stateEquation := congrArg Prod.fst equations
    have outputEquation := congrArg Prod.snd equations
    simp only [rosenbrock] at stateEquation outputEquation
    exact ⟨state, input, nonzero, stateEquation, outputEquation⟩
  · rintro ⟨state, input, nonzero, stateEquation, outputEquation⟩
    refine ⟨(state, input), nonzero, ?_⟩
    apply Prod.ext
    · simpa [rosenbrock] using stateEquation
    · simpa [rosenbrock] using outputEquation

/-- A selected output is a typed postcomposition, not an identification with
the full output family. -/
def selectOutput {Selected : Type*}
    [AddCommGroup Selected] [Module F Selected]
    (system : LinearControlSystem F State Input Output)
    (select : Output →ₗ[F] Selected) :
    LinearControlSystem F State Input Selected where
  A := system.A
  B := system.B
  C := select.comp system.C
  D := select.comp system.D

end LinearControlSystem

def scalarMap (coefficient : ℚ) : ℚ →ₗ[ℚ] ℚ where
  toFun value := coefficient * value
  map_add' := by intros; simp [mul_add]
  map_smul' := by intros; simp [mul_left_comm]

def twoOutputMap (first second : ℚ) : ℚ →ₗ[ℚ] (Fin 2 → ℚ) where
  toFun value := fun port => if port = 0 then first * value else second * value
  map_add' := by
    intro left right
    funext port
    fin_cases port <;> simp <;> ring
  map_smul' := by
    intro scalar value
    funext port
    fin_cases port <;> simp <;> ring

def selectFirstOutput : (Fin 2 → ℚ) →ₗ[ℚ] ℚ where
  toFun output := output 0
  map_add' := by intros; simp
  map_smul' := by intros; simp

/-- Sontag's exact one-state, one-input, two-output lossless hostile. -/
def passiveTwoPortSystem :
    LinearControlSystem ℚ ℚ ℚ (Fin 2 → ℚ) where
  A := scalarMap (3 / 5)
  B := scalarMap (-12 / 25)
  C := twoOutputMap (4 / 5) 0
  D := twoOutputMap (9 / 25) (4 / 5)

def passiveSelectedFirstSystem : LinearControlSystem ℚ ℚ ℚ ℚ :=
  passiveTwoPortSystem.selectOutput selectFirstOutput

theorem passiveTwoPort_storage_identity (state input : ℚ) :
    let next := passiveTwoPortSystem.A state + passiveTwoPortSystem.B input
    let output := passiveTwoPortSystem.C state + passiveTwoPortSystem.D input
    next ^ 2 + output 0 ^ 2 + output 1 ^ 2 = state ^ 2 + input ^ 2 := by
  dsimp [passiveTwoPortSystem, scalarMap, twoOutputMap]
  ring

theorem passiveTwoPort_controllable_observable_witnesses :
    passiveTwoPortSystem.B 1 ≠ 0 ∧ passiveTwoPortSystem.C 1 ≠ 0 := by
  constructor
  · norm_num [passiveTwoPortSystem, scalarMap]
  · intro equality
    have atFirst := congrFun equality 0
    norm_num [passiveTwoPortSystem, twoOutputMap] at atFirst

/-- The selected first port has the exact off-disk transmission-zero witness
`parameter=5/3`, `state=-9/20`, `input=1`. -/
theorem selectedFirst_has_offDisk_transmissionZero :
    passiveSelectedFirstSystem.HasTransmissionZero (5 / 3) := by
  rw [LinearControlSystem.hasTransmissionZero_iff]
  refine ⟨-9 / 20, 1, ?_, ?_, ?_⟩
  · norm_num
  · norm_num [passiveSelectedFirstSystem, passiveTwoPortSystem,
      LinearControlSystem.selectOutput, scalarMap]
  · norm_num [passiveSelectedFirstSystem, passiveTwoPortSystem,
      LinearControlSystem.selectOutput, scalarMap, twoOutputMap,
      selectFirstOutput]

/-- At the selected-port zero, the complementary full-output port remains
bright. -/
theorem complementary_port_bright_at_selected_zero :
    (passiveTwoPortSystem.C (-9 / 20) + passiveTwoPortSystem.D 1) 0 = 0 ∧
      (passiveTwoPortSystem.C (-9 / 20) + passiveTwoPortSystem.D 1) 1 = 4 / 5 := by
  norm_num [passiveTwoPortSystem, twoOutputMap]

/-- Exact hostile conclusion: losslessness plus elementary reachability and
full-output visibility do not exclude a selected-port transmission zero. -/
theorem passive_fullOutput_properties_do_not_imply_selected_zeroFree :
    (∀ state input : ℚ,
      let next := passiveTwoPortSystem.A state + passiveTwoPortSystem.B input
      let output := passiveTwoPortSystem.C state + passiveTwoPortSystem.D input
      next ^ 2 + output 0 ^ 2 + output 1 ^ 2 = state ^ 2 + input ^ 2) ∧
      passiveTwoPortSystem.B 1 ≠ 0 ∧
      passiveTwoPortSystem.C 1 ≠ 0 ∧
      passiveSelectedFirstSystem.HasTransmissionZero (5 / 3) := by
  exact ⟨passiveTwoPort_storage_identity,
    passiveTwoPort_controllable_observable_witnesses.1,
    passiveTwoPort_controllable_observable_witnesses.2,
    selectedFirst_has_offDisk_transmissionZero⟩

end MariciFormal.RosenbrockTransmissionZero
