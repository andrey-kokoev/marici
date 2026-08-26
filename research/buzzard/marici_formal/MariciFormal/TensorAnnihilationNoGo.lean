import Mathlib.Algebra.Ring.Defs

/-!
Information-theoretic core of Grothendieck's Gaussian-annihilation no-go.
The analytic Mellin commutator is a source interface; this file proves what
follows once its archimedean factor is zero.
-/

namespace MariciFormal

section SeparableReadout

variable {R : Type*} [CommRing R]

def tensorSeparatedReadout (archimedean finite : R) : R :=
  archimedean * finite

/-- A locally annihilated archimedean factor makes every tensor-separable
global readout zero, independently of the finite factor. -/
theorem local_annihilation_kills_separated_readout (finite : R) :
    tensorSeparatedReadout 0 finite = 0 := by
  simp [tensorSeparatedReadout]

theorem annihilated_readouts_agree (finite₁ finite₂ : R) :
    tensorSeparatedReadout 0 finite₁ =
      tensorSeparatedReadout 0 finite₂ := by
  simp [tensorSeparatedReadout]

end SeparableReadout

section FaithfulnessHostile

variable {R : Type*} [CommRing R] [Nontrivial R]

/-- The annihilated tensor channel is not faithful on finite source data. -/
theorem annihilated_tensor_readout_not_injective :
    ¬ Function.Injective (tensorSeparatedReadout (R := R) 0) := by
  intro hinjective
  have hzeroOne : (0 : R) = 1 :=
    hinjective (by simp [tensorSeparatedReadout])
  exact zero_ne_one hzeroOne

/-- No post-processing of the cached zero can reconstruct every live finite
factor. -/
theorem no_decoder_recovers_finite_factor (decode : R → R) :
    ¬ ∀ finite, decode (tensorSeparatedReadout 0 finite) = finite := by
  intro hdecode
  have hzero := hdecode 0
  have hone := hdecode 1
  simp [tensorSeparatedReadout] at hzero hone
  exact zero_ne_one (hzero.symm.trans hone)

/-- A nonseparable mixed channel can remain faithful when the local factor is
zero; this is an additional coupling, not a consequence of annihilation. -/
def mixedSourceReadout (archimedean finite : R) : R :=
  archimedean + finite

theorem mixedSourceReadout_zero_injective :
    Function.Injective (mixedSourceReadout (R := R) 0) := by
  intro x y h
  simpa [mixedSourceReadout] using h

end FaithfulnessHostile

end MariciFormal
