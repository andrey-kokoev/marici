{-# OPTIONS --safe --cubical --guardedness #-}
module SingleSourceRouteCompiler where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
import WholePackageSigmaPi as Whole
import DependentNormalizationCoherence as Coherence
import NativeNormalizationRouteCompiler as Native
import RetainedTransportResolution as Transport

module Compiler (ℓ : Level) (Q : Whole.Universe.Code ℓ) where
  open Whole.Universe ℓ
  module H = Coherence.Coherence ℓ Q
  module N = Native.Compiler ℓ Q
  module T = Transport.Extension ℓ
  open H.Presentation

  -- A view exposes a value type without dropping the complete packet.
  record Viewed (P : H.Presentation) : Type (ℓ-suc ℓ) where
    constructor viewed
    field
      packet : Complete
      view : El (expression packet) ≃ El (expression P)
  open Viewed public

  viewed-value : {P : H.Presentation} → Viewed P → El (expression P)
  viewed-value v = equivFun (view v) (value (packet v))

  start : (P : H.Presentation) → El (expression P) → Viewed P
  start P x = viewed (pack (expression P) x) (idEquiv _)

  step-equiv : {P R : H.Presentation} (f : H.CoherentMap P R) (v : Viewed P)
    → El (expression (packet v)) ≃ El (expression R)
  step-equiv {P} {R} f v = compEquiv (view v) (N.map-equiv {P} {R} f)

  advance : {P R : H.Presentation} → H.CoherentMap P R → Viewed P → Viewed R
  advance {P} {R} f v = viewed
    (T.transported (packet v) (expression R) (step-equiv {P} {R} f v)) (idEquiv _)

  run : {P R : H.Presentation} → H.Route P R → Viewed P → Viewed R
  run H.stop v = v
  run (H.next {P} {R} f tail) v = run tail (advance {P} {R} f v)

  run-agrees : {P R : H.Presentation} (route : H.Route P R) (v : Viewed P)
    → viewed-value (run route v) ≡ N.execute route (viewed-value v)
  run-agrees H.stop v = refl
  run-agrees (H.next {P} {R} f tail) v = run-agrees tail (advance {P} {R} f v)

  module WithSeeds (S : Complete → Type (ℓ-suc ℓ)) where
    compile : {P R : H.Presentation} (route : H.Route P R) (v : Viewed P)
      → T.ResolveT S (packet v) → T.ResolveT S (packet (run route v))
    compile H.stop v d = d
    compile (H.next {P} {R} f tail) v d = compile tail (advance {P} {R} f v)
      (T.transportT (packet v) (expression R) (step-equiv {P} {R} f v) d)

    compile-one-seed : {P R : H.Presentation} (route : H.Route P R) (v : Viewed P)
      (d : T.ResolveT S (packet v)) → T.TransportOnly d → T.TransportOnly (compile route v d)
    compile-one-seed H.stop v d proof = proof
    compile-one-seed (H.next {P} {R} f tail) v d proof =
      compile-one-seed tail (advance {P} {R} f v)
        (T.transportT (packet v) (expression R) (step-equiv {P} {R} f v) d)
        (T.one-step (packet v) (expression R) (step-equiv {P} {R} f v) d proof)

  OnlySource : Complete → Complete → Type (ℓ-suc ℓ)
  OnlySource source q = q ≡ source

  source-compile : {P R : H.Presentation} (route : H.Route P R) (x : El (expression P))
    → T.ResolveT (OnlySource (packet (start P x))) (packet (run route (start P x)))
  source-compile {P} route x = WithSeeds.compile (OnlySource (packet (start P x)))
    route (start P x) (T.seedT refl)

  source-one-seed : {P R : H.Presentation} (route : H.Route P R) (x : El (expression P))
    → T.TransportOnly (source-compile route x)
  source-one-seed {P} route x = WithSeeds.compile-one-seed (OnlySource (packet (start P x)))
    route (start P x) (T.seedT refl) (T.one-seed refl)

  source-effect : {P R : H.Presentation} (route : H.Route P R) (x : El (expression P))
    → viewed-value (run route (start P x)) ≡ fst (H.evaluate route x)
  source-effect {P} route x = run-agrees route (start P x) ∙ N.execution-agrees route x

  record Retained : Type (ℓ-suc ℓ) where
    constructor compiled-source
    field
      source target : H.Presentation
      route : H.Route source target
      input-value : El (expression source)
      history : T.ResolveT (OnlySource (packet (start source input-value)))
        (packet (run route (start source input-value)))
      single-seed : T.TransportOnly history
      effect : viewed-value (run route (start source input-value)) ≡ fst (H.evaluate route input-value)

  retain-compilation : {P R : H.Presentation} → H.Route P R → El (expression P) → Retained
  retain-compilation {P} {R} route x = compiled-source P R route x
    (source-compile route x) (source-one-seed route x) (source-effect route x)

  next-Q : Retained → Whole.Universe.Complete (ℓ-suc ℓ)
  next-Q r = Whole.Universe.pack (Whole.Universe.atom Retained) r
