{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedSquareConeClock where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.List.Base using (List; []; _∷_; map; _++_; length)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc; _+_)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false; notEquiv)
open import Cubical.Data.Empty.Base using (⊥)
import RetainedSquareReversal as Square
import ThreeWitnessRetainedCone as RetainedCone

-- This consumes the ACTUAL existing square/return constructor, not a count
-- of abstract tetrahedral edges. One selected completed square return is a
-- tick record; no physical duration or autonomous production law is assumed.
module Bridge {ℓ : Level} (O R : Type ℓ) (e : O ≃ R) where
  module Return = Square.Construction O R e
  module G = Return.G
  Source = O × O

  module AtSource (s : Source) where
    record Tick : Type ℓ where
      constructor tick
      field
        returned : Return.RetainedReturn
        attachment : G.RealizedSquare.source (Return.RetainedReturn.original returned) ≡ s
    open Tick

    fresh : Tick
    fresh = tick (Return.make-return s) (Return.recover-source s)

    RouteWitness : Type ℓ
    RouteWitness = Σ[ route ∈ G.Schedule ] Σ[ value ∈ R × R ] (value ≡ G.run route s)
    ReturnSection : Type ℓ
    ReturnSection = (i j : I) → Return.backward-cell i j

    first : Tick → RouteWitness
    first t = G.ComparedRoutes.first comparison , G.RealizedSquare.target original ,
      (G.RealizedSquare.target-law original ∙ cong (G.run (G.ComparedRoutes.first comparison)) (attachment t))
      where
      original = Return.RetainedReturn.original (returned t)
      comparison = G.RealizedSquare.comparison original

    second : Tick → RouteWitness
    second t = G.ComparedRoutes.second comparison , G.RealizedSquare.target original ,
      (G.RealizedSquare.target-law original
       ∙ cong (λ f → f (G.RealizedSquare.source original)) (G.ComparedRoutes.witness comparison)
       ∙ cong (G.run (G.ComparedRoutes.second comparison)) (attachment t))
      where
      original = Return.RetainedReturn.original (returned t)
      comparison = G.RealizedSquare.comparison original

    third : Tick → ReturnSection
    third t = Return.RetainedReturn.return-section (returned t)

    module Cone = RetainedCone.Cone Tick RouteWitness RouteWitness ReturnSection first second third
    module Cell = Cone.Cell

    -- The apex type certificate permits a decoder from a standalone typed
    -- tetrahedral package, rather than reading back the original argument.
    record ConeRecord : Type (ℓ-suc ℓ) where
      constructor cone-record
      field
        diagram : Cell.Full
        apex-type : fst (Cell.vertex diagram Cell.zero) ≡ Tick
    open ConeRecord

    encode : Tick → ConeRecord
    encode t = cone-record (Cone.At.tetrahedron t) refl
    decode : ConeRecord → Tick
    decode c = transport (apex-type c) (snd (Cell.vertex (diagram c) Cell.zero))
    decode-encode : (t : Tick) → decode (encode t) ≡ t
    decode-encode t = transportRefl t

    encode-injective : (t u : Tick) → encode t ≡ encode u → t ≡ u
    encode-injective t u path = sym (decode-encode t) ∙ cong decode path ∙ decode-encode u

    -- Whole-record recovery includes both original schedule tags, the route
    -- comparison, the return section, endpoint laws AND the source attachment.
    return-recovered : (t : Tick) → returned (decode (encode t)) ≡ returned t
    return-recovered t = cong returned (decode-encode t)
    first-route-recovered : (t : Tick) → fst (first (decode (encode t))) ≡ fst (first t)
    first-route-recovered t = cong (λ u → fst (first u)) (decode-encode t)
    second-route-recovered : (t : Tick) → fst (second (decode (encode t))) ≡ fst (second t)
    second-route-recovered t = cong (λ u → fst (second u)) (decode-encode t)

    swapped : Tick
    swapped = tick
      (Return.retained-return
        (G.realized s (G.compared G.rightFirst G.leftFirst (sym G.route-homotopy))
          (G.run G.rightFirst s) refl)
        (Return.backward-section s) refl refl) refl
    schedule-records-distinct : fresh ≡ swapped → ⊥
    schedule-records-distinct path = G.routes-distinct (cong (λ t → fst (first t)) path)
    same-count-distinct-records : length (fresh ∷ []) ≡ length (swapped ∷ [])
    same-count-distinct-records = refl

    History = List Tick
    ConeHistory = List ConeRecord
    encode-history : History → ConeHistory
    encode-history = map encode
    decode-history : ConeHistory → History
    decode-history = map decode
    history-recovered : (h : History) → decode-history (encode-history h) ≡ h
    history-recovered [] = refl
    history-recovered (t ∷ h) = cong₂ _∷_ (decode-encode t) (history-recovered h)

    encode-composes : (h k : History)
      → encode-history (h ++ k) ≡ encode-history h ++ encode-history k
    encode-composes [] k = refl
    encode-composes (t ∷ h) k = cong (encode t ∷_) (encode-composes h k)
    count-adds : (h k : History) → length (h ++ k) ≡ length h + length k
    count-adds [] k = refl
    count-adds (t ∷ h) k = cong suc (count-adds h k)
    count-preserved : (h : History) → length (encode-history h) ≡ length h
    count-preserved [] = refl
    count-preserved (t ∷ h) = cong suc (count-preserved h)

    terminal : History → Source
    terminal [] = s
    terminal (t ∷ h) = third t i1 i1
    terminal-correct : (h : History) → terminal h ≡ s
    terminal-correct [] = refl
    terminal-correct (t ∷ h) = Return.RetainedReturn.end-law (returned t) ∙ attachment t

    is-zero : ℕ → Bool
    is-zero zero = true
    is-zero (suc n) = false
    no-endpoint-clock : (read : Source → ℕ)
      → ((h : History) → read (terminal h) ≡ length h) → ⊥
    no-endpoint-clock read law = true≢false (cong is-zero
      (sym (law []) ∙ cong read (sym (terminal-correct (fresh ∷ []))) ∙ law (fresh ∷ [])))

-- Existing nontrivial Bool equivalence supplies an inhabited concrete test.
module Example = Bridge Bool Bool notEquiv
module ExampleAt = Example.AtSource (false , true)
one : ExampleAt.History
one = ExampleAt.fresh ∷ []
two : ExampleAt.History
two = one ++ one
one-cone-count : length (ExampleAt.encode-history one) ≡ 1
one-cone-count = refl
two-cone-count : length (ExampleAt.encode-history two) ≡ 2
two-cone-count = refl
