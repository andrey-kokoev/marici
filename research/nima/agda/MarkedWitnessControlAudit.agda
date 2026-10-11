{-# OPTIONS --safe --cubical --guardedness #-}
module MarkedWitnessControlAudit where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import RetainedTetrahedralPackage as Retained
import TetrahedralEdgeReadout as Read
open import TetrahedralWitnessControl using (disagrees)

-- An edge between typed inhabited vertices already contains compatibility
-- of the transported source inhabitant with its target inhabitant.
marked-path-respects-value : {ℓ : Level}
  (a b : Retained.TypedValue ℓ) (p : a ≡ b)
  → transport (λ i → fst (p i)) (snd a) ≡ snd b
marked-path-respects-value a b p = fromPathP (λ i → snd (p i))

module C = Retained.Cells (Retained.TypedValue ℓ-zero)
first-edge : (p : C.Full) → C.vertex p C.zero ≡ C.vertex p C.one
first-edge p = C.T.Edges.e01 (C.Over.Surface.edges (fst (snd p)))

own-endpoints-agree : (p : C.Full)
  → transport (λ i → fst (first-edge p i)) (snd (C.vertex p C.zero))
    ≡ snd (C.vertex p C.one)
own-endpoints-agree p = marked-path-respects-value
  (C.vertex p C.zero) (C.vertex p C.one) (first-edge p)

fixture = Retained.TypedFixture.result
fixture-source : snd (C.vertex fixture C.zero) ≡ false
fixture-source = refl
fixture-target : snd (C.vertex fixture C.one) ≡ true
fixture-target = refl
fixture-transport : transport (λ i → fst (first-edge fixture i)) false ≡ true
fixture-transport = own-endpoints-agree fixture
fixture-control-zero : disagrees (transport (λ i → fst (first-edge fixture i)) false) true ≡ false
fixture-control-zero = cong (λ b → disagrees b true) fixture-transport

-- The earlier false/false question is a different, independently prepared
-- reference. It cannot be claimed to be the pointed target of this flip.
false-is-not-flip-target : transport (Read.L.first-edge Read.L.twisted) false ≡ false → ⊥
false-is-not-flip-target h = true≢false (sym (Read.twisted01 false) ∙ h)
