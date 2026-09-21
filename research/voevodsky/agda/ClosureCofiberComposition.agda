{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureCofiberComposition where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence
open import Cubical.Foundations.GroupoidLaws using (rUnit)
open import Cubical.Data.Unit
open import Cubical.HITs.Pushout.Base
open import Cubical.HITs.Pushout.Properties

-- Homotopy pushouts, NOT hom-set quotients. All attachment paths are retained.
-- This is the space-valued cofiber-composition theorem. No positivity or
-- analytical realization is assumed. The desired equivalence is an output.

-- Contract an identity-leg pushout to its other (terminal) leg.
module Collapse (T : Type) where
  P : Type
  P = Pushout (idfun T) (λ _ → tt)

  center : P
  center = inr tt

  contraction : (x : P) → center ≡ x
  contraction (inl t) = sym (push t)
  contraction (inr tt) = refl
  contraction (push t i) j = push t (i ∨ ~ j)

  collapseIso : Iso P Unit
  Iso.fun collapseIso _ = tt
  Iso.inv collapseIso _ = center
  Iso.rightInv collapseIso _ = refl
  Iso.leftInv collapseIso = contraction

  collapseEquiv : P ≃ Unit
  collapseEquiv = isoToEquiv collapseIso

module Composition (A B C : Type) (f : A → B) (g : B → C) where
  -- The source square commutes definitionally: (g f) = g composed with f.
  -- Rows:  Unit <- A -> C
  --        Unit <- A -> B
  --        Unit <- Unit -> Unit
  -- Vertical maps from the middle row are identities/g upwards and the
  -- terminal maps downwards. The four square witnesses are all explicit.
  diagram : 3x3-span
  3x3-span.A00 diagram = Unit
  3x3-span.A02 diagram = A
  3x3-span.A04 diagram = C
  3x3-span.A20 diagram = Unit
  3x3-span.A22 diagram = A
  3x3-span.A24 diagram = B
  3x3-span.A40 diagram = Unit
  3x3-span.A42 diagram = Unit
  3x3-span.A44 diagram = Unit
  3x3-span.f01 diagram _ = tt
  3x3-span.f03 diagram a = g (f a)
  3x3-span.f21 diagram _ = tt
  3x3-span.f23 diagram = f
  3x3-span.f41 diagram = idfun Unit
  3x3-span.f43 diagram = idfun Unit
  3x3-span.f10 diagram = idfun Unit
  3x3-span.f12 diagram = idfun A
  3x3-span.f14 diagram = g
  3x3-span.f30 diagram = idfun Unit
  3x3-span.f32 diagram _ = tt
  3x3-span.f34 diagram _ = tt
  3x3-span.H11 diagram _ = refl
  3x3-span.H13 diagram _ = refl
  3x3-span.H31 diagram _ = refl
  3x3-span.H33 diagram _ = refl

  open 3x3-span diagram

  B/A : Type
  B/A = cofib f

  C/A : Type
  C/A = cofib (λ a → g (f a))

  C/B : Type
  C/B = cofib g

  -- This induced map includes its action on the A-attachment paths, supplied
  -- by the explicit commuting square above, not only its values on B.
  induced : B/A → C/A
  induced = f1□

  induced-on-B : (b : B) → induced (inr b) ≡ inr (g b)
  induced-on-B b = refl

  induced-on-base : induced (inl tt) ≡ inl tt
  induced-on-base = refl

  induced-on-attachment : (a : A) → cong induced (push a) ≡ push a
  induced-on-attachment a = sym (rUnit (push a))

  iteratedQuotient : Type
  iteratedQuotient = cofib induced

  -- First total: push out each column, then across. Two identity-leg columns
  -- contract, leaving C/B. The compatibility on their attachment is retained.
  columnSpanEquiv : 3-span-equiv
    (3span f□1 f□3)
    (3span (idfun Unit) (λ _ → inr {f = g} {g = λ _ → tt} tt))
  3-span-equiv.e0 columnSpanEquiv = Collapse.collapseEquiv Unit
  3-span-equiv.e2 columnSpanEquiv = Collapse.collapseEquiv A
  3-span-equiv.e4 columnSpanEquiv = idEquiv A□4
  3-span-equiv.H1 columnSpanEquiv _ = refl
  3-span-equiv.H3 columnSpanEquiv x =
    cong f□3 (Collapse.contraction A x)

  columnsReduced : A□○ ≃ C/B
  columnsReduced = compEquiv
    (pathToEquiv (spanEquivToPushoutPath columnSpanEquiv))
    (compEquiv
      (invEquiv (pushoutIdfunEquiv' (λ (_ : Unit) → inr {f = g} {g = λ _ → tt} tt)))
      (symPushout g (λ _ → tt)))

  -- Second total: push out each row, then down. Its source and middle rows
  -- are C/A and B/A. The terminal row contracts to the cone point.
  rowSpanEquiv : 3-span-equiv
    (3span f1□ f3□)
    (3span induced (λ _ → tt))
  3-span-equiv.e0 rowSpanEquiv = idEquiv C/A
  3-span-equiv.e2 rowSpanEquiv = idEquiv B/A
  3-span-equiv.e4 rowSpanEquiv = Collapse.collapseEquiv Unit
  3-span-equiv.H1 rowSpanEquiv _ = refl
  3-span-equiv.H3 rowSpanEquiv _ = refl

  rowsReduced : A○□ ≃ iteratedQuotient
  rowsReduced = compEquiv
    (pathToEquiv (spanEquivToPushoutPath rowSpanEquiv))
    (symPushout induced (λ _ → tt))

  -- Cut-change: row decomposition -> column decomposition -> C/B.
  cofiberComposition : iteratedQuotient ≃ C/B
  cofiberComposition = compEquiv (invEquiv rowsReduced)
    (compEquiv (invEquiv (isoToEquiv 3x3-Iso)) columnsReduced)

  rejoin : iteratedQuotient → C/B
  rejoin = equivFun cofiberComposition

  cut : C/B → iteratedQuotient
  cut = invEq cofiberComposition

  rejoin-cut : (x : C/B) → rejoin (cut x) ≡ x
  rejoin-cut = secEq cofiberComposition

  cut-rejoin : (x : iteratedQuotient) → cut (rejoin x) ≡ x
  cut-rejoin = retEq cofiberComposition

  -- Univalence also gives the type-level comparison, without truncating paths.
  quotientIdentification : iteratedQuotient ≡ C/B
  quotientIdentification = ua cofiberComposition
