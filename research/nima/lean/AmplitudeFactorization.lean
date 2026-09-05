import Mathlib.Algebra.BigOperators.Ring.Finset

namespace Marici.Amplitude

set_option checkBinderAnnotations false
set_option linter.style.haveILetI false

open scoped BigOperators

universe u v w

/-- A finite sum of weights is the abstract algebraic amplitude. -/
def amplitude {R : Type u} [AddCommMonoid R] {T : Type v} [Fintype T]
    (weight : T → R) : R := ∑ t, weight t

/-- Reindexing terms along an equivalence does not change an amplitude. -/
theorem amplitude_equiv {R : Type u} [AddCommMonoid R]
    {T : Type v} {U : Type w} [Fintype T] [Fintype U]
    (e : T ≃ U) (weight : T → R) :
    amplitude weight = amplitude (weight ∘ e.symm) := by
  unfold amplitude
  exact Fintype.sum_equiv e weight (weight ∘ e.symm) (fun x => by simp)

/-- Generic residue factorization once the face-product equivalence identifies
global compatible completions with tuples of regional completions and the
weight of a completion is the product of its regional weights. -/
theorem amplitude_factorization {R : Type u} [CommSemiring R]
    {ι : Type v} [Fintype ι] {T : Type w} [Fintype T]
    (U : ι → Type w) (finiteU : ∀ i, Fintype (U i))
    (terms : T ≃ ((i : ι) → U i))
    (weight : T → R) (regionalWeight : (i : ι) → U i → R)
    (weight_product : ∀ t, weight t = ∏ i, regionalWeight i (terms t i)) :
    amplitude weight = ∏ i, @amplitude R _ (U i) (finiteU i) (regionalWeight i) := by
  classical
  letI (i : ι) : Fintype (U i) := finiteU i
  calc
    amplitude weight = ∑ t, ∏ i, regionalWeight i (terms t i) := by
      apply Finset.sum_congr rfl
      intro t _
      exact weight_product t
    _ = ∑ a : ((i : ι) → U i), ∏ i, regionalWeight i (a i) := by
      exact Fintype.sum_equiv terms
        (fun t => ∏ i, regionalWeight i (terms t i))
        (fun a => ∏ i, regionalWeight i (a i)) (fun _ => rfl)
    _ = ∏ i, ∑ u : U i, regionalWeight i u := by
      exact (Fintype.prod_sum regionalWeight).symm
    _ = ∏ i, amplitude (regionalWeight i) := rfl

end Marici.Amplitude
