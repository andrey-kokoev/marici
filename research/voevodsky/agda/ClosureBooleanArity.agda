{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureBooleanArity where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (Bool; false; true)

-- "For every input index, a function" is used throughout. This is NOT a
-- function consuming a product of all inputs jointly.
module Arity (A B I J : Type) (Ai : I → Type) (Bj : J → Type) where
  K L : Bool → Type
  K false = Unit
  K true = I
  L false = Unit
  L true = J

  X : (s : Bool) → K s → Type
  X false _ = A
  X true i = Ai i

  Y : (t : Bool) → L t → Type
  Y false _ = B
  Y true j = Bj j

  -- The single equation for all four cases.
  F : Bool → Bool → Type
  F s t = (i : K s) (j : L t) → X s i → Y t j

  Input : Bool → Type
  Input s = Σ (K s) (X s)

  Output : Bool → Type
  Output t = (j : L t) → Y t j

  -- Independent input indices assemble as a SUM; output indices as a PRODUCT.
  assemble : (s t : Bool) → F s t → Input s → Output t
  assemble s t f z j = f (fst z) j (snd z)

  disassemble : (s t : Bool) → (Input s → Output t) → F s t
  disassemble s t f i j x = f (i , x) j

  sumProductIso : (s t : Bool) → Iso (F s t) (Input s → Output t)
  Iso.fun (sumProductIso s t) = assemble s t
  Iso.inv (sumProductIso s t) = disassemble s t
  Iso.rightInv (sumProductIso s t) f = refl
  Iso.leftInv (sumProductIso s t) f = refl

  sumProductEquiv : (s t : Bool) → F s t ≃ (Input s → Output t)
  sumProductEquiv s t = isoToEquiv (sumProductIso s t)

  -- Remove the unindexed singleton coordinates in the three small corners.
  corner11Iso : Iso (F false false) (A → B)
  Iso.fun corner11Iso f x = f tt tt x
  Iso.inv corner11Iso f _ _ x = f x
  Iso.rightInv corner11Iso f = refl
  Iso.leftInv corner11Iso f = refl

  corner1ManyIso : Iso (F false true) ((j : J) → A → Bj j)
  Iso.fun corner1ManyIso f j x = f tt j x
  Iso.inv corner1ManyIso f _ j x = f j x
  Iso.rightInv corner1ManyIso f = refl
  Iso.leftInv corner1ManyIso f = refl

  cornerMany1Iso : Iso (F true false) ((i : I) → Ai i → B)
  Iso.fun cornerMany1Iso f i x = f i tt x
  Iso.inv cornerMany1Iso f i _ x = f i x
  Iso.rightInv cornerMany1Iso f = refl
  Iso.leftInv cornerMany1Iso f = refl

  -- The fourth corner already has exactly the requested signature.
  cornerManyMany : F true true ≃ ((i : I) (j : J) → Ai i → Bj j)
  cornerManyMany = idEquiv _

  -- Flags alone supply no arrows between corners. These are the two actual
  -- maps needed: assembly of a selected input and observation of all outputs.
  module Indexing (assembleInput : Input true → A) (observeOutput : B → Output true) where
    inputIndex : (t : Bool) → F false t → F true t
    inputIndex t f i j x = f tt j (assembleInput (i , x))

    outputIndex : (s : Bool) → F s false → F s true
    outputIndex s f i j x = observeOutput (f i tt x) j

    square : (f : F false false) →
      outputIndex true (inputIndex false f) ≡ inputIndex true (outputIndex false f)
    square f = refl

  -- Equivalences, rather than arbitrary assembly/observation maps, make
  -- both directions reversible and give a genuine round-trip cycle law.
  module Reversible (inputEquiv : Input true ≃ A) (outputEquiv : B ≃ Output true) where
    open Indexing (equivFun inputEquiv) (equivFun outputEquiv) public

    inputIso : (t : Bool) → Iso (F false t) (F true t)
    Iso.fun (inputIso t) = inputIndex t
    Iso.inv (inputIso t) f _ j a =
      f (fst (invEq inputEquiv a)) j (snd (invEq inputEquiv a))
    Iso.rightInv (inputIso t) f = funExt λ i → funExt λ j → funExt λ x →
      cong (λ z → f (fst z) j (snd z)) (retEq inputEquiv (i , x))
    Iso.leftInv (inputIso t) f = funExt λ { tt → funExt λ j → funExt λ a →
      cong (f tt j) (secEq inputEquiv a) }

    outputIso : (s : Bool) → Iso (F s false) (F s true)
    Iso.fun (outputIso s) = outputIndex s
    Iso.inv (outputIso s) f i _ x = invEq outputEquiv (λ j → f i j x)
    Iso.rightInv (outputIso s) f = funExt λ i → funExt λ j → funExt λ x →
      cong (λ p → p j) (secEq outputEquiv (λ j → f i j x))
    Iso.leftInv (outputIso s) f = funExt λ i → funExt λ { tt → funExt λ x →
      retEq outputEquiv (f i tt x) }

    cycle : F false false → F false false
    cycle f = Iso.inv (inputIso false)
      (Iso.inv (outputIso true) (inputIndex true (outputIndex false f)))

    cycleLaw : (f : F false false) → cycle f ≡ f
    cycleLaw f =
      cong (λ z → Iso.inv (inputIso false) (Iso.inv (outputIso true) z))
        (sym (square f))
      ∙ cong (Iso.inv (inputIso false))
          (Iso.leftInv (outputIso true) (inputIndex false f))
      ∙ Iso.leftInv (inputIso false) f

-- No path between false and true, no product-of-inputs identification, and
-- no equivalence between arbitrary corners is assumed by this selector.
