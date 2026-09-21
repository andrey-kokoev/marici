{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureIntermediateCutComparison where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (rUnit)
open import Cubical.Data.Unit
open import Cubical.HITs.Pushout.Base
open import Cubical.HITs.Pushout.Properties using (pushoutEquiv)
open import ClosureCanonicalRejoin using (module Rejoin; module Naturality)

module CutComparison {A B C D : Type}
  (f : A → B) (g : B → C) (h : C → D) where
  module N = Naturality f g h
  module AfterA = Rejoin g h
  module AfterMiddle = Rejoin (λ a → g (f a)) h

  -- ((D/A)/(B/A)) / ((C/A)/(B/A)), with the actual induced map.
  TripleQuotient : Type
  TripleQuotient = cofib N.upper

  -- Collapse A in both numerator and denominator. Naturality of rejoin
  -- supplies the commuting square; here its constructor equations expose a
  -- direct, attachment-sensitive map on the resulting cofiber.
  collapseA : TripleQuotient → AfterA.Quotient
  collapseA (inl tt) = inl tt
  collapseA (inr x) = inr (N.After.rejoin x)
  collapseA (push (inl tt) w) = push (inl tt) w
  collapseA (push (inr (inl tt)) w) = push (inl tt) w
  collapseA (push (inr (inr c)) w) = push (inr c) w
  collapseA (push (inr (push a u)) w) = push (push (f a) u) w
  collapseA (push (push (inl tt) v) w) = push (inl tt) w
  collapseA (push (push (inr b) v) w) = push (push b v) w
  collapseA (push (push (push a u) v) w) = push (push (f a) (u ∧ v)) w

  -- Alternatively remove the common middle quotient B/A first.
  -- The result is (D/A)/(C/A). Split the A-attachments explicitly so that
  -- composition of the normalized transports has its required boundaries.
  collapseMiddle : TripleQuotient → AfterMiddle.Quotient
  collapseMiddle (inl tt) = inl tt
  collapseMiddle (inr (inl tt)) = inl tt
  collapseMiddle (inr (inr y)) = inr y
  collapseMiddle (inr (push (inl tt) v)) = push (inl tt) v
  collapseMiddle (inr (push (inr b) v)) = push (inr (g b)) v
  collapseMiddle (inr (push (push a u) v)) = push (push a u) v
  collapseMiddle (push (inl tt) w) = inl tt
  collapseMiddle (push (inr y) w) = push y w
  collapseMiddle (push (push (inl tt) v) w) = push (inl tt) (v ∧ w)
  collapseMiddle (push (push (inr b) v) w) = push (inr (g b)) (v ∧ w)
  collapseMiddle (push (push (push a u) v) w) = push (push a u) (v ∧ w)

  -- These composites are independently defined via different intermediate
  -- quotient types. Both land in D/C = cofib h.
  removeAFirst : TripleQuotient → cofib h
  removeAFirst x = AfterA.rejoin (collapseA x)

  removeMiddleFirst : TripleQuotient → cofib h
  removeMiddleFirst x = AfterMiddle.rejoin (collapseMiddle x)

  -- On the deepest cell the formulas are push(g(f a)) ((u ∧ v) ∧ w)
  -- and push(g(f a)) (u ∧ (v ∧ w)). Interval meet is associative.
  cutComparison : (x : TripleQuotient) → removeAFirst x ≡ removeMiddleFirst x
  cutComparison (inl tt) = refl
  cutComparison (inr (inl tt)) = refl
  cutComparison (inr (inr (inl tt))) = refl
  cutComparison (inr (inr (inr d))) = refl
  cutComparison (inr (inr (push a u))) = refl
  cutComparison (inr (push (inl tt) v)) = refl
  cutComparison (inr (push (inr b) v)) = refl
  cutComparison (inr (push (push a u) v)) = refl
  cutComparison (push (inl tt) w) = refl
  cutComparison (push (inr (inl tt)) w) = refl
  cutComparison (push (inr (inr c)) w) = refl
  cutComparison (push (inr (push a u)) w) = refl
  cutComparison (push (push (inl tt) v) w) = refl
  cutComparison (push (push (inr b) v) w) = refl
  cutComparison (push (push (push a u) v) w) = refl

  -- Certify collapseA as an equivalence, not merely as a commuting function.
  -- Both vertical maps of this pushout span are the proved rejoin equivalences.
  spanEquivalence : TripleQuotient ≃ AfterA.Quotient
  spanEquivalence = pushoutEquiv
    (λ _ → tt) N.upper (λ _ → tt) N.Lower.direct
    N.Before.rejoinEquiv (idEquiv Unit) N.After.rejoinEquiv
    refl N.rejoinFunctionSquare

  spanMapComparison : (x : TripleQuotient) → equivFun spanEquivalence x ≡ collapseA x
  spanMapComparison (inl tt) = refl
  spanMapComparison (inr x) = refl
  spanMapComparison (push (inl tt) w) j = sym (rUnit (push (inl tt))) j w
  spanMapComparison (push (inr (inl tt)) w) j = sym (rUnit (push (inl tt))) j w
  spanMapComparison (push (inr (inr c)) w) j = sym (rUnit (push (inr c))) j w
  spanMapComparison (push (inr (push a u)) w) j = sym (rUnit (push (push (f a) u))) j w
  spanMapComparison (push (push (inl tt) v) w) j = sym (rUnit (push (inl tt))) j w
  spanMapComparison (push (push (inr b) v) w) j = sym (rUnit (push (push b v))) j w
  spanMapComparison (push (push (push a u) v) w) j = sym (rUnit (push (push (f a) (u ∧ v)))) j w

  -- Keep certified isEquiv witnesses opaque to avoid expanding the library's
  -- large pushout inverse proofs when specializing examples. The forward
  -- maps and all attachment computations remain transparent.
  abstract
    collapseAIsEquiv : isEquiv collapseA
    collapseAIsEquiv =
      subst isEquiv (funExt spanMapComparison) (snd spanEquivalence)

  collapseAEquiv : TripleQuotient ≃ AfterA.Quotient
  collapseAEquiv = collapseA , collapseAIsEquiv

  abstract
    removeAFirstIsEquiv : isEquiv removeAFirst
    removeAFirstIsEquiv = snd (compEquiv collapseAEquiv AfterA.rejoinEquiv)

  removeAFirstEquiv : TripleQuotient ≃ cofib h
  removeAFirstEquiv = removeAFirst , removeAFirstIsEquiv

  abstract
    removeMiddleFirstIsEquiv : isEquiv removeMiddleFirst
    removeMiddleFirstIsEquiv =
      subst isEquiv (funExt cutComparison) (snd removeAFirstEquiv)

  removeMiddleFirstEquiv : TripleQuotient ≃ cofib h
  removeMiddleFirstEquiv = removeMiddleFirst , removeMiddleFirstIsEquiv

  -- Upgrade the constructed homotopy to equality of equivalences. Only the
  -- proof that a map is an equivalence is propositional; no quotient paths
  -- or attachment data are truncated.
  equivalenceComparison : removeAFirstEquiv ≡ removeMiddleFirstEquiv
  equivalenceComparison = equivEq (funExt cutComparison)

  inverseComparison : (y : cofib h) →
    invEq removeAFirstEquiv y ≡ invEq removeMiddleFirstEquiv y
  inverseComparison y = cong (λ e → invEq e y) equivalenceComparison

  -- Two-out-of-three, with the actual map retained as the forward function.
  abstract
    collapseMiddleIsEquiv : isEquiv collapseMiddle
    collapseMiddleIsEquiv = subst isEquiv
      (funExt (λ x → retEq AfterMiddle.rejoinEquiv (collapseMiddle x)))
      (snd (compEquiv removeMiddleFirstEquiv (invEquiv AfterMiddle.rejoinEquiv)))

  collapseMiddleEquiv : TripleQuotient ≃ AfterMiddle.Quotient
  collapseMiddleEquiv = collapseMiddle , collapseMiddleIsEquiv

-- This is an intermediate-cut comparison for a triple quotient. It is not
-- yet the pentagon comparing five rebracketings of a four-stage quotient.
