{-# OPTIONS --safe --cubical --guardedness #-}
module GuardedTransportComparisonBasis where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels using (isContr→isContrPath)
import WholePackageSigmaPi as Whole
import SingleSourceRouteCompiler as Compiler

module Basis (ℓ : Level) (Q : Whole.Universe.Code ℓ) where
  open Whole.Universe ℓ
  module C = Compiler.Compiler ℓ Q
  module H = C.H
  open H.Presentation

  -- Observe the ACTUAL source-only compiled packet for every source value.
  -- The second component supplies the shared-coordinate guard.
  observe : {P R : H.Presentation} → H.Route P R → H.CoherentMap P R
  observe {P} {R} route x =
    C.viewed-value (C.run route (C.start P x)) ,
    cong (equivFun (coordinates R)) (C.source-effect route x) ∙ snd (H.evaluate route x)

  Semantic : {P R : H.Presentation} → H.Route P R → H.Route P R → Type ℓ
  Semantic a b = observe a ≡ observe b

  semantic-contractible : {P R : H.Presentation} (a b : H.Route P R) → isContr (Semantic a b)
  semantic-contractible {P} {R} a b =
    isContr→isContrPath (H.map-contractible P R) (observe a) (observe b)

  canonical : (P R : H.Presentation) → H.Route P R
  canonical P R = H.next {R = R} (H.map-center P R) H.stop

  prefix-compatible : {P R T : H.Presentation} (f : H.CoherentMap P R) (tail : H.Route R T)
    → observe (H.next {P} {R} {T} f tail) ≡ H.compose {P} {R} {T} f (observe tail)
  prefix-compatible {P} {R} {T} f tail = H.compare-maps {P} {T}
    (observe (H.next {P} {R} {T} f tail)) (H.compose {P} {R} {T} f (observe tail))

  -- A new typed calculus for differently retained compiled endpoints.
  -- Only stop normalization and one-step normalization are primitive laws.
  -- No constructor accepts an arbitrary Semantic witness.
  data Generated : {P R : H.Presentation} → H.Route P R → H.Route P R → Type (ℓ-suc ℓ) where
    identity : {P R : H.Presentation} (a : H.Route P R) → Generated a a
    reverse : {P R : H.Presentation} {a b : H.Route P R} → Generated a b → Generated b a
    concatenate : {P R : H.Presentation} {a b c : H.Route P R}
      → Generated a b → Generated b c → Generated a c
    stop-normalization : (P : H.Presentation) → Generated (H.stop {P}) (canonical P P)
    step-normalization : {P R T : H.Presentation} (f : H.CoherentMap P R)
      → Generated (H.next {P} {R} {T} f (canonical R T)) (canonical P T)
    prefix : {P R T : H.Presentation} (f : H.CoherentMap P R) (a b : H.Route R T)
      → Generated a b → Generated (H.next {P} {R} {T} f a) (H.next {P} {R} {T} f b)

  sound : {P R : H.Presentation} {a b : H.Route P R} → Generated a b → Semantic a b
  sound (identity _) = refl
  sound (reverse c) = sym (sound c)
  sound (concatenate c c') = sound c ∙ sound c'
  sound (stop-normalization P) = fst (semantic-contractible (H.stop {P}) (canonical P P))
  sound (step-normalization {P} {R} {T} f) = fst
    (semantic-contractible (H.next {P} {R} {T} f (canonical R T)) (canonical P T))
  sound (prefix {P} {R} {T} f a b c) = prefix-compatible {P} {R} {T} f a
    ∙ cong (H.compose {P} {R} {T} f) (sound c) ∙ sym (prefix-compatible {P} {R} {T} f b)

  reduce : {P R : H.Presentation} (a : H.Route P R) → Generated a (canonical P R)
  reduce (H.stop {P}) = stop-normalization P
  reduce (H.next {P} {R} {T} f tail) = concatenate
    (prefix {P} {R} {T} f tail (canonical R T) (reduce tail))
    (step-normalization {P} {R} {T} f)

  compare : {P R : H.Presentation} (a b : H.Route P R) → Generated a b
  compare a b = concatenate (reduce a) (reverse (reduce b))

  completeness : {P R : H.Presentation} (a b : H.Route P R) (p : Semantic a b)
    → Σ[ c ∈ Generated a b ] (sound c ≡ p)
  completeness a b p = compare a b , isContr→isProp (semantic-contractible a b) _ p

  higher-contractible : {P R : H.Presentation} (a b : H.Route P R)
    (p q : Semantic a b) → isContr (p ≡ q)
  higher-contractible a b = isContr→isContrPath (semantic-contractible a b)

  record Requested : Type (ℓ-suc ℓ) where
    constructor requested
    field
      source target : H.Presentation
      first second : H.Route source target
      input-value : El (expression source)
      witness : Semantic first second
      derivation : Generated first second
      reconstructs : sound derivation ≡ witness
      first-native : C.T.ResolveT (C.OnlySource (C.packet (C.start source input-value)))
        (C.packet (C.run first (C.start source input-value)))
      second-native : C.T.ResolveT (C.OnlySource (C.packet (C.start source input-value)))
        (C.packet (C.run second (C.start source input-value)))
      first-single-seed : C.T.TransportOnly first-native
      second-single-seed : C.T.TransportOnly second-native
      viewed-effect : C.viewed-value (C.run first (C.start source input-value))
        ≡ C.viewed-value (C.run second (C.start source input-value))

  realize : {P R : H.Presentation} (a b : H.Route P R) (x : El (expression P))
    → Semantic a b → Requested
  realize {P} {R} a b x p = requested P R a b x p
    (fst result) (snd result) (C.source-compile a x) (C.source-compile b x)
    (C.source-one-seed a x) (C.source-one-seed b x)
    (cong (λ f → C.N.underlying {P} {R} f x) p)
    where
    result = completeness a b p

  next-Q : Requested → Whole.Universe.Complete (ℓ-suc ℓ)
  next-Q r = Whole.Universe.pack (Whole.Universe.atom Requested) r
