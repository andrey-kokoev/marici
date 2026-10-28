{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyNativePNOverlapSpan where
open import Cubical.Foundations.Prelude
open import Agda.Builtin.String using (String)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution
module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero

module Spans (Chart Face : Type) (Permit : Chart → Face → Type)
  (packet : (c : Chart) (f : Face) → Permit c f → String) where
  InputIndex : Type
  InputIndex = Σ Chart (λ c → Σ Face (Permit c))
  port-package : (c : Chart) (f : Face) → Permit c f → G.Package
  port-package c f p = N.pack (G.atom-node String) (packet c f p)
  Admit : G.Package → Type (ℓ-suc ℓ-zero)
  Admit q = Σ InputIndex (λ { (c , (f , p)) → q ≡ port-package c f p })
  module R = Resolution.Full ℓ-zero Admit
  port-proof : (c : Chart) (f : Face) (p : Permit c f) → R.Resolve (port-package c f p)
  port-proof c f p = R.seed ((c , (f , p)) , refl)
  Common : Chart → Chart → Type
  Common a b = Σ Face (λ f → Σ (Permit a f) (λ _ → Permit b f))
  data Side : Type where
    source-leg target-leg : Side
  leg : (a b : Chart) → Common a b → Side → G.Package
  leg a b (f , (p , q)) source-leg = port-package a f p
  leg a b (f , (p , q)) target-leg = port-package b f q
  leg-proof : (a b : Chart) (x : Common a b) (s : Side) → R.Resolve (leg a b x s)
  leg-proof a b (f , (p , q)) source-leg = port-proof a f p
  leg-proof a b (f , (p , q)) target-leg = port-proof b f q
  pair-package : (a b : Chart) → Common a b → G.Package
  pair-package a b x = N.Pi-package Side (leg a b x)
  pair-proof : (a b : Chart) (x : Common a b) → R.Resolve (pair-package a b x)
  pair-proof a b x = R.apply (N.P-kind , Side , leg a b x) (λ { (lift s) → leg-proof a b x s })
  span-package : Chart → Chart → G.Package
  span-package a b = N.Pi-package (Common a b) (pair-package a b)
  span-proof : (a b : Chart) → R.Resolve (span-package a b)
  span-proof a b = R.apply (N.P-kind , Common a b , pair-package a b) (λ { (lift x) → pair-proof a b x })
  selected-package : (a b : Chart) → Common a b → G.Package
  selected-package a b x = N.E-package (Common a b) (pair-package a b) x
  selected-proof : (a b : Chart) (x : Common a b) → R.Resolve (selected-package a b x)
  selected-proof a b x = R.apply (N.E-kind , Common a b , pair-package a b , x) (λ { (lift y) → pair-proof a b y })
  retained-index : (a b : Chart) (x : Common a b) → fst (N.value (selected-package a b x)) ≡ x
  retained-index a b x = refl
  retained-source : (a b : Chart) (x : Common a b)
    → R.premise (R.premise (selected-package a b x , selected-proof a b x) (lift x)) (lift source-leg)
      ≡ (leg a b x source-leg , leg-proof a b x source-leg)
  retained-source a b x = refl
  retained-target : (a b : Chart) (x : Common a b)
    → R.premise (R.premise (selected-package a b x , selected-proof a b x) (lift x)) (lift target-leg)
      ≡ (leg a b x target-leg , leg-proof a b x target-leg)
  retained-target a b x = refl

  Triple : Chart → Chart → Chart → Type
  Triple a b c = Σ Face (λ f → Σ (Permit a f) (λ _ → Σ (Permit b f) (λ _ → Permit c f)))
  ab-index : {a b c : Chart} → Triple a b c → Common a b
  ab-index (f , (p , (q , s))) = f , (p , q)
  bc-index : {a b c : Chart} → Triple a b c → Common b c
  bc-index (f , (p , (q , s))) = f , (q , s)
  ac-index : {a b c : Chart} → Triple a b c → Common a c
  ac-index (f , (p , (q , s))) = f , (p , s)
  -- The middle full packet AND its input certificate coincide, not just a color.
  middle-seam : (a b c : Chart) (t : Triple a b c)
    → R.premise (R.premise (selected-package a b (ab-index t) , selected-proof a b (ab-index t)) (lift (ab-index t))) (lift target-leg)
      ≡ R.premise (R.premise (selected-package b c (bc-index t) , selected-proof b c (bc-index t)) (lift (bc-index t))) (lift source-leg)
  middle-seam a b c (f , (p , (q , s))) = refl
  source-face-cell : (a b c : Chart) (t : Triple a b c)
    → fst (fst (N.value (selected-package a b (ab-index t)))) ≡ fst (fst (N.value (selected-package a c (ac-index t))))
  source-face-cell a b c t = refl
  target-face-cell : (a b c : Chart) (t : Triple a b c)
    → fst (fst (N.value (selected-package b c (bc-index t)))) ≡ fst (fst (N.value (selected-package a c (ac-index t))))
  target-face-cell a b c t = refl
  data Three : Type where
    first-port middle-port final-port : Three
  whole-port : (a b c : Chart) → Triple a b c → Three → G.Package
  whole-port a b c (f , (p , (q , s))) first-port = port-package a f p
  whole-port a b c (f , (p , (q , s))) middle-port = port-package b f q
  whole-port a b c (f , (p , (q , s))) final-port = port-package c f s
  whole-proof : (a b c : Chart) (t : Triple a b c) (i : Three) → R.Resolve (whole-port a b c t i)
  whole-proof a b c (f , (p , (q , s))) first-port = port-proof a f p
  whole-proof a b c (f , (p , (q , s))) middle-port = port-proof b f q
  whole-proof a b c (f , (p , (q , s))) final-port = port-proof c f s
  three-proof : (a b c : Chart) (t : Triple a b c) → R.Resolve (N.Pi-package Three (whole-port a b c t))
  three-proof a b c t = R.apply (N.P-kind , Three , whole-port a b c t) (λ { (lift i) → whole-proof a b c t i })
  data Piece : Type where
    AB BC AC full-source : Piece
  composition-part : (a b c : Chart) → Triple a b c → Piece → G.Package
  composition-part a b c t AB = selected-package a b (ab-index t)
  composition-part a b c t BC = selected-package b c (bc-index t)
  composition-part a b c t AC = selected-package a c (ac-index t)
  composition-part a b c t full-source = N.Pi-package Three (whole-port a b c t)
  composition-part-proof : (a b c : Chart) (t : Triple a b c) (p : Piece) → R.Resolve (composition-part a b c t p)
  composition-part-proof a b c t AB = selected-proof a b (ab-index t)
  composition-part-proof a b c t BC = selected-proof b c (bc-index t)
  composition-part-proof a b c t AC = selected-proof a c (ac-index t)
  composition-part-proof a b c t full-source = three-proof a b c t
  composition-package : (a b c : Chart) → Triple a b c → G.Package
  composition-package a b c t = N.Pi-package Piece (composition-part a b c t)
  composition-proof : (a b c : Chart) (t : Triple a b c) → R.Resolve (composition-package a b c t)
  composition-proof a b c t = R.apply (N.P-kind , Piece , composition-part a b c t)
    (λ { (lift p) → composition-part-proof a b c t p })
  retains-route : (a b c : Chart) (t : Triple a b c) (p : Piece)
    → R.premise (composition-package a b c t , composition-proof a b c t) (lift p)
      ≡ (composition-part a b c t p , composition-part-proof a b c t p)
  retains-route a b c t p = refl
