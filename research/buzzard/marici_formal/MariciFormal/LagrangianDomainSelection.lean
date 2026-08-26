import MariciFormal.KernelCokernelVariance

/-!
The Green form determines admissible Lagrangian boundary domains but does not
select one; different choices can change the restricted kernel.
-/

namespace MariciFormal

def symplecticBoundaryForm (x y : VarianceChannel) : Rat :=
  x 0 * y 1 - x 1 * y 0

/-- In a two-dimensional symplectic space, a nonzero isotropic generator
determines a Lagrangian line. -/
def IsLagrangianGenerator (v : VarianceChannel) : Prop :=
  v ≠ 0 ∧ symplecticBoundaryForm v v = 0

def scaleChannel (t : Rat) (v : VarianceChannel) : VarianceChannel :=
  fun i => t * v i

def firstCoordinateDomain : VarianceChannel := ![1, 0]

def secondCoordinateDomain : VarianceChannel := ![0, 1]

def kernelBoundaryDomain : VarianceChannel := ordinaryKernelWitness

theorem boundaryDomainFixtures_lagrangian :
    IsLagrangianGenerator firstCoordinateDomain ∧
      IsLagrangianGenerator secondCoordinateDomain ∧
      IsLagrangianGenerator kernelBoundaryDomain := by
  constructor
  · constructor
    · intro h
      have h0 := congrFun h 0
      norm_num [firstCoordinateDomain] at h0
    · norm_num [symplecticBoundaryForm, firstCoordinateDomain]
  · constructor
    · constructor
      · intro h
        have h1 := congrFun h 1
        norm_num [secondCoordinateDomain] at h1
      · norm_num [symplecticBoundaryForm, secondCoordinateDomain]
    · constructor
      · intro h
        have h0 := congrFun h 0
        norm_num [kernelBoundaryDomain, ordinaryKernelWitness] at h0
      · norm_num [symplecticBoundaryForm, kernelBoundaryDomain,
          ordinaryKernelWitness]

def InjectiveOnGeneratedLine
    (map : VarianceChannel → VarianceChannel) (v : VarianceChannel) : Prop :=
  ∀ t : Rat, map (scaleChannel t v) = 0 → t = 0

theorem observationMap_injective_on_firstCoordinateDomain :
    InjectiveOnGeneratedLine observationMap firstCoordinateDomain := by
  intro t h
  have h0 := congrFun h 0
  simpa [observationMap, scaleChannel, firstCoordinateDomain] using h0

theorem observationMap_not_injective_on_kernelBoundaryDomain :
    ¬ InjectiveOnGeneratedLine observationMap kernelBoundaryDomain := by
  intro h
  have hOne := h 1
  have hZero : observationMap (scaleChannel 1 kernelBoundaryDomain) = 0 := by
    native_decide
  exact one_ne_zero (hOne hZero)

/-- Two Lagrangian choices for one fixed map yield different restricted kernels. -/
theorem boundaryChoice_is_part_of_kernelData :
    IsLagrangianGenerator firstCoordinateDomain ∧
      IsLagrangianGenerator kernelBoundaryDomain ∧
      InjectiveOnGeneratedLine observationMap firstCoordinateDomain ∧
      ¬ InjectiveOnGeneratedLine observationMap kernelBoundaryDomain := by
  exact ⟨boundaryDomainFixtures_lagrangian.1,
    boundaryDomainFixtures_lagrangian.2.2,
    observationMap_injective_on_firstCoordinateDomain,
    observationMap_not_injective_on_kernelBoundaryDomain⟩

def boundaryReflection (x : VarianceChannel) : VarianceChannel := ![x 0, -x 1]

def boundaryExchange (x : VarianceChannel) : VarianceChannel := ![x 1, x 0]

def positiveBoundaryEnergy (x : VarianceChannel) : Rat := x 0 ^ 2 + x 1 ^ 2

def ReflectionInvariantLine (v : VarianceChannel) : Prop :=
  ∃ c : Rat, boundaryReflection v = scaleChannel c v

theorem boundaryReflection_antisymplectic (x y : VarianceChannel) :
    symplecticBoundaryForm (boundaryReflection x) (boundaryReflection y) =
      -symplecticBoundaryForm x y := by
  simp [symplecticBoundaryForm, boundaryReflection]
  ring

theorem boundaryExchange_preservesEnergy (x : VarianceChannel) :
    positiveBoundaryEnergy (boundaryExchange x) = positiveBoundaryEnergy x := by
  simp [positiveBoundaryEnergy, boundaryExchange]
  ring

theorem boundaryExchange_antisymplectic (x y : VarianceChannel) :
    symplecticBoundaryForm (boundaryExchange x) (boundaryExchange y) =
      -symplecticBoundaryForm x y := by
  simp [symplecticBoundaryForm, boundaryExchange]

theorem coordinateDomains_one_geometryOrbit :
    firstCoordinateDomain ≠ secondCoordinateDomain ∧
      ReflectionInvariantLine firstCoordinateDomain ∧
      ReflectionInvariantLine secondCoordinateDomain ∧
      positiveBoundaryEnergy firstCoordinateDomain = 1 ∧
      positiveBoundaryEnergy secondCoordinateDomain = 1 ∧
      boundaryExchange firstCoordinateDomain = secondCoordinateDomain := by
  refine ⟨by native_decide, ?_, ?_, by native_decide, by native_decide,
    by native_decide⟩
  · exact ⟨1, by native_decide⟩
  · exact ⟨-1, by native_decide⟩

/-- Any exchange-invariant scalar score is unable to distinguish the orbit. -/
theorem invariantScore_cannot_select_coordinateDomain
    (score : VarianceChannel → Rat)
    (hInvariant : ∀ v, score (boundaryExchange v) = score v) :
    score firstCoordinateDomain = score secondCoordinateDomain := by
  rw [← coordinateDomains_one_geometryOrbit.2.2.2.2.2]
  exact (hInvariant firstCoordinateDomain).symm

end MariciFormal
