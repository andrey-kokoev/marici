import MariciFormal.FactorizationDescent
import MariciFormal.ProbeContinuityGap

/-!
The single-port hostile for constructor-stable endpoint completion.
-/

namespace MariciFormal

abbrev EndpointPacket := Nat →₀ Rat

/-- Sum every coefficient of a finite packet. -/
noncomputable def packetSum : EndpointPacket →ₗ[Rat] Rat :=
  Finsupp.lsum Rat fun _ => LinearMap.id

/-- The retained scalar endpoint is coordinate zero. -/
def baseEndpoint : EndpointPacket →ₗ[Rat] Rat :=
  Finsupp.lapply 0

/-- Authorized constructor `A(x) = (sum_j x_j) e₀`. -/
noncomputable def sumToEndpointConstructor : EndpointPacket →ₗ[Rat] EndpointPacket :=
  (Finsupp.lsingle 0).comp packetSum

/-- The first constructor-orbit endpoint `L ∘ A`. -/
noncomputable def constructorOrbitEndpoint : EndpointPacket →ₗ[Rat] Rat :=
  baseEndpoint.comp sumToEndpointConstructor

noncomputable def endpointInvisiblePacket : EndpointPacket :=
  Finsupp.single 1 1

theorem endpointInvisiblePacket_base_zero :
    baseEndpoint endpointInvisiblePacket = 0 := by
  simp [baseEndpoint, endpointInvisiblePacket]

theorem endpointInvisiblePacket_orbit_one :
    constructorOrbitEndpoint endpointInvisiblePacket = 1 := by
  simp [constructorOrbitEndpoint, sumToEndpointConstructor, baseEndpoint,
    packetSum, endpointInvisiblePacket]

/-- The constructor-generated endpoint does not vanish on the kernel of `L`. -/
theorem baseEndpoint_kernel_not_preserved_by_constructor :
    ¬ LinearMap.ker baseEndpoint ≤ LinearMap.ker constructorOrbitEndpoint := by
  intro kernelPreserved
  have hmemBase : endpointInvisiblePacket ∈ LinearMap.ker baseEndpoint := by
    exact endpointInvisiblePacket_base_zero
  have hmemOrbit := kernelPreserved hmemBase
  change constructorOrbitEndpoint endpointInvisiblePacket = 0 at hmemOrbit
  rw [endpointInvisiblePacket_orbit_one] at hmemOrbit
  norm_num at hmemOrbit

/-- `L ∘ A` cannot descend through the single endpoint presentation `L`. -/
theorem constructorOrbitEndpoint_does_not_factor_through_baseEndpoint :
    ¬ FactorsThrough baseEndpoint constructorOrbitEndpoint := by
  intro factorization
  exact baseEndpoint_kernel_not_preserved_by_constructor
    (factorsThrough_implies_ker_le factorization)

/-- Adding the orbit endpoint separates the hostile packet missed by `L`. -/
theorem orbitEndpoint_repairs_hostile_packet :
    baseEndpoint endpointInvisiblePacket = 0 ∧
      constructorOrbitEndpoint endpointInvisiblePacket ≠ 0 := by
  constructor
  · exact endpointInvisiblePacket_base_zero
  · rw [endpointInvisiblePacket_orbit_one]
    norm_num

end MariciFormal
