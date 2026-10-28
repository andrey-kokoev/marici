{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedDomainRepresentation where

open import Cubical.Foundations.Prelude
import ThreeWitnessRetainedCone as Existing

-- Supplied domain and supplied focus maps. No source-admission theorem is assumed
-- to follow from encoding these data.
module Representation {ℓ : Level} (P A B C : Type ℓ)
  (first : P → A) (second : P → B) (third : P → C) where
  module Cone = Existing.Cone P A B C first second third
  module Cell = Cone.Cell

  record TriangleRecord : Type (ℓ-suc ℓ) where
    constructor triangle-record
    field
      diagram : Cell.FacePackage
      first-type : fst (Cell.FacePackage.a diagram) ≡ Cone.V1.View
  open TriangleRecord

  encode : P → TriangleRecord
  encode p = triangle-record (Cone.At.O.f123 p (Cone.At.surface p)) refl

  decode : TriangleRecord → P
  decode q = Cone.V1.recover
    (transport (first-type q) (snd (Cell.FacePackage.a (diagram q))))

  decode-encode : (p : P) → decode (encode p) ≡ p
  decode-encode p = cong Cone.V1.recover (transportRefl (Cone.V1.decorate p))

  encoded-equality-reflects : (p q : P) → encode p ≡ encode q → p ≡ q
  encoded-equality-reflects p q e =
    sym (decode-encode p) ∙ cong decode e ∙ decode-encode q

  observe : {κ : Level} {O : Type κ} → (P → O) → TriangleRecord → O
  observe r q = r (decode q)

  observation-preserved : {κ : Level} {O : Type κ}
    (r : P → O) (p : P) → observe r (encode p) ≡ r p
  observation-preserved r p = cong r (decode-encode p)

  execute : (P → P) → TriangleRecord → TriangleRecord
  execute f q = encode (f (decode q))

  execute-on-encoded : (f : P → P) (p : P)
    → execute f (encode p) ≡ encode (f p)
  execute-on-encoded f p = cong (λ x → encode (f x)) (decode-encode p)

  execute-composes : (f g : P → P) (q : TriangleRecord)
    → execute g (execute f q) ≡ execute (λ p → g (f p)) q
  execute-composes f g q =
    cong (λ x → encode (g x)) (decode-encode (f (decode q)))

  -- Unit law on encoded records, not arbitrary tetrahedral/triangle packages.
  execute-unit-on-encoded : (p : P)
    → execute (λ x → x) (encode p) ≡ encode p
  execute-unit-on-encoded p = cong encode (decode-encode p)

-- Recovery is the only hypothesis used to transport observations through an
-- already established tower stage. No arbitrary-generation claim is hidden here.
module TowerBinding {ℓ κ : Level} (D : Type ℓ) (P : Type κ)
  (promote : D → P) (recover : P → D)
  (recovery : (d : D) → recover (promote d) ≡ d) where
  readout-preserved : {ν : Level} {O : Type ν} (read : D → O) (d : D)
    → read (recover (promote d)) ≡ read d
  readout-preserved read d = cong read (recovery d)
