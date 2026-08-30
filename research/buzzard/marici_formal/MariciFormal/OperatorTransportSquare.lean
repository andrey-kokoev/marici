import Mathlib

/-!
Kernel transport requires a commuting operator square and relative injectivity
of codomain transport on the realized operator image.
-/

namespace MariciFormal

def InKernel {V W : Type} [Zero W] (map : V → W) (x : V) : Prop := map x = 0

theorem commutingSquare_transports_kernel
    {V V' W W' : Type} [Zero W] [Zero W']
    (sourceMap : V → W) (targetMap : V' → W')
    (domainTransport : V → V') (domainInverse : V' → V)
    (codomainTransport : W → W')
    (_hLeftInverse : ∀ x, domainInverse (domainTransport x) = x)
    (hRightInverse : ∀ y, domainTransport (domainInverse y) = y)
    (hSquare : ∀ x, targetMap (domainTransport x) =
      codomainTransport (sourceMap x))
    (hCodomainZero : codomainTransport 0 = 0)
    (hRelativeInjective : ∀ x, codomainTransport (sourceMap x) = 0 →
      sourceMap x = 0) :
    ∀ y, InKernel targetMap y ↔
      ∃ x, InKernel sourceMap x ∧ domainTransport x = y := by
  intro y
  constructor
  · intro hy
    refine ⟨domainInverse y, ?_, hRightInverse y⟩
    apply hRelativeInjective
    rw [← hSquare, hRightInverse]
    exact hy
  · rintro ⟨x, hx, rfl⟩
    unfold InKernel at hx ⊢
    rw [hSquare, hx, hCodomainZero]

abbrev TransportPlane := Fin 2 → Rat

def sourceInclusion (x : Rat) : TransportPlane := ![x, 0]

/-- Noninjective globally, but injective on the first-coordinate source image. -/
def safeCodomainTransport (x : TransportPlane) : Rat := x 0

def safeTargetMap (x : Rat) : Rat := x

theorem safeNoninjectiveTransport_square :
    (∀ x, safeTargetMap x = safeCodomainTransport (sourceInclusion x)) ∧
      (∃ x y, x ≠ y ∧ safeCodomainTransport x = safeCodomainTransport y) ∧
      (∀ x, safeTargetMap x = 0 ↔ sourceInclusion x = 0) := by
  constructor
  · intro x
    rfl
  · constructor
    · refine ⟨![0, 0], ![0, 1], ?_, rfl⟩
      intro h
      have h1 := congrFun h 1
      norm_num at h1
    · intro x
      constructor
      · intro h
        funext i
        fin_cases i
        · simpa [safeTargetMap, sourceInclusion] using h
        · rfl
      · intro h
        have h0 := congrFun h 0
        simpa [safeTargetMap, sourceInclusion] using h0

/-- This noninjective transport kills the complete realized source image. -/
def badCodomainTransport (x : TransportPlane) : Rat := x 1

def badTargetMap (_ : Rat) : Rat := 0

theorem badNoninjectiveTransport_commutes_but_growsKernel :
    (∀ x, badTargetMap x = badCodomainTransport (sourceInclusion x)) ∧
      InKernel sourceInclusion 0 ∧
      ¬ InKernel sourceInclusion 1 ∧
      InKernel badTargetMap 0 ∧
      InKernel badTargetMap 1 := by
  constructor
  · intro x
    rfl
  · constructor
    · funext i
      fin_cases i <;> rfl
    · constructor
      · intro h
        have h0 := congrFun h 0
        norm_num [InKernel, sourceInclusion] at h0
      · exact ⟨rfl, rfl⟩

theorem relativeInjectivity_is_independent_of_commutativity :
    (∀ x, badTargetMap x = badCodomainTransport (sourceInclusion x)) ∧
      ¬ (∀ x, badCodomainTransport (sourceInclusion x) = 0 →
        sourceInclusion x = 0) := by
  constructor
  · intro x
    rfl
  · intro h
    have hOne := h 1 rfl
    have h0 := congrFun hOne 0
    norm_num [sourceInclusion] at h0

end MariciFormal
