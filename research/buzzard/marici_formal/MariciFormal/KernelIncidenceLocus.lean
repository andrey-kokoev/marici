import MariciFormal.LagrangianDomainSelection

/-!
Restricted kernel birth is an incidence property of the pair consisting of a
boundary domain and the bulk kernel. It is invariant under simultaneous
injective transport, not one-sided transport.
-/

namespace MariciFormal

def MapKernel {V W : Type} [Zero W] (map : V → W) : Set V :=
  {x | map x = 0}

def RestrictedKernel {V W : Type} [Zero W]
    (map : V → W) (domain : Set V) : Set V :=
  {x | x ∈ domain ∧ map x = 0}

theorem restrictedKernel_eq_incidence {V W : Type} [Zero W]
    (map : V → W) (domain : Set V) :
    RestrictedKernel map domain = domain ∩ MapKernel map := by
  rfl

def GeneratedLine (generator : VarianceChannel) : Set VarianceChannel :=
  {x | ∃ t : Rat, x = scaleChannel t generator}

def HasNontrivialIncidence (left right : Set VarianceChannel) : Prop :=
  ∃ x, x ≠ 0 ∧ x ∈ left ∧ x ∈ right

theorem firstDomain_has_trivial_bulkKernelIncidence :
    ¬ HasNontrivialIncidence (GeneratedLine firstCoordinateDomain)
      (MapKernel observationMap) := by
  rintro ⟨x, hx, ⟨t, rfl⟩, hKernel⟩
  have ht := observationMap_injective_on_firstCoordinateDomain t hKernel
  subst t
  apply hx
  funext i
  simp [scaleChannel]

theorem kernelDomain_has_nontrivial_bulkKernelIncidence :
    HasNontrivialIncidence (GeneratedLine kernelBoundaryDomain)
      (MapKernel observationMap) := by
  refine ⟨kernelBoundaryDomain, ?_, ⟨1, ?_⟩, ?_⟩
  · exact boundaryDomainFixtures_lagrangian.2.2.1
  · funext i
    simp [scaleChannel]
  · funext i
    fin_cases i <;>
      norm_num [MapKernel, observationMap, kernelBoundaryDomain,
        ordinaryKernelWitness]

theorem simultaneousInjectiveTransport_preservesIntersection
    {V U : Type} (transport : V → U) (hInjective : Function.Injective transport)
    (left right : Set V) :
    transport '' (left ∩ right) = transport '' left ∩ transport '' right := by
  ext y
  constructor
  · rintro ⟨x, ⟨hxLeft, hxRight⟩, rfl⟩
    exact ⟨⟨x, hxLeft, rfl⟩, ⟨x, hxRight, rfl⟩⟩
  · rintro ⟨⟨xLeft, hxLeft, hLeft⟩, ⟨xRight, hxRight, hRight⟩⟩
    have hSame : xLeft = xRight := hInjective (hLeft.trans hRight.symm)
    subst xRight
    exact ⟨xLeft, ⟨hxLeft, hxRight⟩, hLeft⟩

theorem boundaryExchange_injective : Function.Injective boundaryExchange := by
  intro x y h
  funext i
  fin_cases i
  · exact congrFun h 1
  · exact congrFun h 0

theorem simultaneousExchange_preserves_coordinateIncidence :
    boundaryExchange ''
        (GeneratedLine firstCoordinateDomain ∩ GeneratedLine firstCoordinateDomain) =
      boundaryExchange '' GeneratedLine firstCoordinateDomain ∩
        boundaryExchange '' GeneratedLine firstCoordinateDomain :=
  simultaneousInjectiveTransport_preservesIntersection boundaryExchange
    boundaryExchange_injective _ _

/-- Moving only the domain while freezing the reference kernel changes the pair. -/
theorem oneSidedTransport_can_destroyIncidence :
    HasNontrivialIncidence (GeneratedLine firstCoordinateDomain)
        (GeneratedLine firstCoordinateDomain) ∧
      ¬ HasNontrivialIncidence (GeneratedLine secondCoordinateDomain)
        (GeneratedLine firstCoordinateDomain) := by
  constructor
  · refine ⟨firstCoordinateDomain, ?_, ⟨1, ?_⟩, ⟨1, ?_⟩⟩
    · exact boundaryDomainFixtures_lagrangian.1.1
    · funext i
      simp [scaleChannel]
    · funext i
      simp [scaleChannel]
  · rintro ⟨x, hx, ⟨s, hs⟩, ⟨t, ht⟩⟩
    have h0 := congrArg (fun v : VarianceChannel => v 0) (hs.symm.trans ht)
    have h1 := congrArg (fun v : VarianceChannel => v 1) (hs.symm.trans ht)
    norm_num [scaleChannel, firstCoordinateDomain, secondCoordinateDomain] at h0 h1
    subst s
    subst t
    apply hx
    rw [ht]
    funext i
    simp [scaleChannel]

end MariciFormal
