{-# OPTIONS --safe --cubical --guardedness #-}
module DependentArbitraryIndexRoutes where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
import WholePackageSigmaPi as Whole
import DependentPackageNormalization as Normal
import DependentNormalizationCoherence as Coherence
import DependentSigmaPiCoherence as Chains

module Routes {ℓ : Level}
  (I : Type ℓ) (J : I → Type ℓ)
  (K : (i : I) → J i → Type ℓ)
  (L : (i : I) (j : J i) → K i j → Type ℓ)
  (B : (i : I) (j : J i) (k : K i j) → L i j k → Type ℓ) where
  open Whole.Universe ℓ
  module C = Chains.Construction I J K L B
  module N = Normal.Normalization ℓ

  Q : Code
  Q = Pi I (λ i → E (J i) (λ j → Pi (K i j)
        (λ k → E (L i j k) (λ l → atom (B i j k l)))))

  module H = Coherence.Coherence ℓ Q

  chart : {T : Type ℓ} → Iso C.X T → H.Presentation
  chart {T} e = H.presentation (atom T)
    (compEquiv (isoToEquiv (invIso e)) (N.normalize-equiv Q))

  A1 A2 B1 B2 B3 terminal : H.Presentation
  A1 = chart C.edgeA1
  A2 = chart (compIso C.edgeA1 C.edgeA2)
  B1 = chart C.edgeB1
  B2 = chart (compIso C.edgeB1 C.edgeB2)
  B3 = chart (compIso (compIso C.edgeB1 C.edgeB2) C.edgeB3)
  terminal = chart C.routeA

  a1 : H.CoherentMap H.original A1
  a1 x = Iso.fun C.edgeA1 x , refl
  a2 : H.CoherentMap A1 A2
  a2 x = Iso.fun C.edgeA2 x , refl
  a3 : H.CoherentMap A2 terminal
  a3 x = Iso.fun C.edgeA3 x , refl

  b1 : H.CoherentMap H.original B1
  b1 x = Iso.fun C.edgeB1 x , refl
  b2 : H.CoherentMap B1 B2
  b2 x = Iso.fun C.edgeB2 x , refl
  b3 : H.CoherentMap B2 B3
  b3 x = Iso.fun C.edgeB3 x , refl
  -- Agda checks the common chart here against route A's inverse.
  b4 : H.CoherentMap B3 terminal
  b4 x = Iso.fun C.edgeB4 x , refl

  outer-first inner-first : H.Route H.original terminal
  outer-first = H.next {R = A1} a1 (H.next {R = A2} a2 (H.next {R = terminal} a3 H.stop))
  inner-first = H.next {R = B1} b1 (H.next {R = B2} b2
    (H.next {R = B3} b3 (H.next {R = terminal} b4 H.stop)))

  complete-route-comparison : H.evaluate outer-first ≡ H.evaluate inner-first
  complete-route-comparison = H.route-comparison outer-first inner-first

  route-certificate : H.Certificate
  route-certificate = H.certify outer-first inner-first

  -- Full source values, seven intermediate values/links, the two raw route
  -- records, and their coordinate-preserving comparison survive together.
  Retained : Type (ℓ-suc ℓ)
  Retained = Σ[ x ∈ C.X ] Σ[ trace ∈ C.Trace x ] H.Certificate

  retain-complete : C.X → Retained
  retain-complete x = x , C.canonicalTrace x , route-certificate

  next-Q : C.X → Whole.Universe.Complete (ℓ-suc ℓ)
  next-Q x = Whole.Universe.pack (Whole.Universe.atom Retained) (retain-complete x)

  original-retained : (x : C.X) → fst (Whole.Universe.value (next-Q x)) ≡ x
  original-retained x = refl
