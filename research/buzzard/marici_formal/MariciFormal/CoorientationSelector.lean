import MariciFormal.LagrangianDomainSelection

/-!
An orbit-separating boundary selector is a coorientation choice. Reversing it
swaps the selected domain, and its zero wall removes unique selection without
changing the bulk operator.
-/

namespace MariciFormal

inductive BoundaryDomainChoice
  | injectiveDomain
  | kernelDomain
  deriving DecidableEq, Repr

def selectorScore (coorientation : Rat) : BoundaryDomainChoice → Rat
  | .injectiveDomain => -coorientation
  | .kernelDomain => coorientation

def swapBoundaryChoice : BoundaryDomainChoice → BoundaryDomainChoice
  | .injectiveDomain => .kernelDomain
  | .kernelDomain => .injectiveDomain

theorem selectorScore_antiInvariant
    (coorientation : Rat) (choice : BoundaryDomainChoice) :
    selectorScore coorientation (swapBoundaryChoice choice) =
      -selectorScore coorientation choice := by
  cases choice <;> simp [selectorScore, swapBoundaryChoice]

theorem positiveCoorientation_selectsInjectiveDomain
    {coorientation : Rat} (hPositive : 0 < coorientation) :
    selectorScore coorientation .injectiveDomain <
      selectorScore coorientation .kernelDomain := by
  simp [selectorScore]
  linarith

theorem negativeCoorientation_selectsKernelDomain
    {coorientation : Rat} (hNegative : coorientation < 0) :
    selectorScore coorientation .kernelDomain <
      selectorScore coorientation .injectiveDomain := by
  simp [selectorScore]
  linarith

theorem zeroCoorientation_selectsNeitherUniquely :
    selectorScore 0 .injectiveDomain = selectorScore 0 .kernelDomain := by
  norm_num [selectorScore]

def selectedBoundaryDomain (parameter : Rat) : Option BoundaryDomainChoice :=
  if 0 < parameter then some .injectiveDomain
  else if parameter < 0 then some .kernelDomain
  else none

def restrictedKernelDimension : BoundaryDomainChoice → Nat
  | .injectiveDomain => 0
  | .kernelDomain => 1

def selectedKernelDimension (parameter : Rat) : Option Nat :=
  restrictedKernelDimension <$> selectedBoundaryDomain parameter

/-- The selector wall changes the restricted kernel without changing `M`. -/
theorem selectorWall_kernelBirthFixture :
    selectedBoundaryDomain 1 = some .injectiveDomain ∧
      selectedKernelDimension 1 = some 0 ∧
      selectedBoundaryDomain 0 = none ∧
      selectedKernelDimension 0 = none ∧
      selectedBoundaryDomain (-1) = some .kernelDomain ∧
      selectedKernelDimension (-1) = some 1 := by
  native_decide

theorem coorientationReversal_swapsSelection
    {parameter : Rat} (hNonzero : parameter ≠ 0) :
    selectedBoundaryDomain (-parameter) =
      Option.map swapBoundaryChoice (selectedBoundaryDomain parameter) := by
  unfold selectedBoundaryDomain
  by_cases hPositive : 0 < parameter
  · have hNegative : -parameter < 0 := by linarith
    have hNotNegative : ¬ parameter < 0 := by linarith
    simp [hPositive, hNegative, hNotNegative, swapBoundaryChoice]
  · have hNegative : parameter < 0 := lt_of_le_of_ne (le_of_not_gt hPositive) hNonzero
    have hPositiveNeg : 0 < -parameter := by linarith
    simp [hPositive, hNegative, hPositiveNeg, swapBoundaryChoice]

/-- A synthetic asymmetric score separates the orbit but carries new data. -/
def syntheticBoundaryEnergy : BoundaryDomainChoice → Rat
  | .injectiveDomain => 1
  | .kernelDomain => 2

theorem syntheticBoundaryEnergy_orbitSeparating :
    syntheticBoundaryEnergy .injectiveDomain <
      syntheticBoundaryEnergy .kernelDomain ∧
      syntheticBoundaryEnergy (swapBoundaryChoice .injectiveDomain) ≠
        syntheticBoundaryEnergy .injectiveDomain := by
  norm_num [syntheticBoundaryEnergy, swapBoundaryChoice]

end MariciFormal
