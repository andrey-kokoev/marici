{-# OPTIONS --safe --cubical --guardedness #-}
module WitnessedHistories where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (Iso; iso)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Unit.Base using (Unit*; tt*; Unit)
import MetaWitnessGenerator as Meta
import NestedWitnessSpecialization as Nested
import FourDomainPentagon as Four
import WitnessSelectionGenerator as Selection
import ReSpecializeWitnessSelection as First
import TripleWitnessSpecialization as Triple

-- No truncation: each edge keeps its endpoint, full witness, and suffix.
History : {ℓ : Level} (S : Type ℓ) → (S → S → Type ℓ) → ℕ → S → Type ℓ
History S R zero x = Unit*
History S R (suc n) x = Σ[ y ∈ S ] Σ[ w ∈ R x y ] History S R n y

run : {ℓ : Level} {S : Type ℓ} {R : S → S → Type ℓ}
  → ((x : S) → Σ[ y ∈ S ] R x y) → (n : ℕ) (x : S) → History S R n x
run g zero x = tt*
run g (suc n) x = fst (g x) , snd (g x) , run g n (fst (g x))

module Specialization {ℓ : Level} (S : Type ℓ) (R : S → S → Type ℓ)
  (first : Meta.Specialize.Compatible S R) where
  module N = Nested.Nested S R first
  module Second (d : N.M2.Domain)
    (a : (v : N.C1.State) → fst (N.C1.generator v) ≡ N.M2.Domain.compute d v)
    (c : (v : N.C1.State) → N.M2.Domain.Allowed d v
      → N.M2.Domain.Allowed d (fst (N.C1.generator v))) where
    module T = N.Followup d a c
    H = History T.C2.State T.C2.Relation
    F = History T.Flat T.FlatRelation

    flatten-history : (n : ℕ) (x : T.C2.State) → H n x → F n (T.flatten x)
    flatten-history zero x h = tt*
    flatten-history (suc n) x (y , w , h) = T.flatten y , w , flatten-history n y h
    unflatten-history : (n : ℕ) (x : T.Flat) → F n x → H n (T.unflatten x)
    unflatten-history zero x h = tt*
    unflatten-history (suc n) x (y , w , h) = T.unflatten y , w , unflatten-history n y h

    flatten-unflatten : (n : ℕ) (x : T.Flat) (h : F n x)
      → flatten-history n (T.unflatten x) (unflatten-history n x h) ≡ h
    flatten-unflatten zero x h = refl
    flatten-unflatten (suc n) x (y , w , h) =
      cong (λ tail → y , w , tail) (flatten-unflatten n y h)
    unflatten-flatten : (n : ℕ) (x : T.C2.State) (h : H n x)
      → unflatten-history n (T.flatten x) (flatten-history n x h) ≡ h
    unflatten-flatten zero x h = refl
    unflatten-flatten (suc n) x (y , w , h) =
      cong (λ tail → y , w , tail) (unflatten-flatten n y h)
    history-iso : (n : ℕ) (x : T.C2.State) → Iso (H n x) (F n (T.flatten x))
    history-iso n x = iso (flatten-history n x) (unflatten-history n (T.flatten x))
      (flatten-unflatten n (T.flatten x)) (unflatten-flatten n x)

    -- Compare actual iteration of the independently defined direct generator.
    run-commutes : (n : ℕ) (x : T.C2.State)
      → flatten-history n x (run T.C2.generator n x)
        ≡ run T.direct-generator n (T.flatten x)
    run-commutes zero x = refl
    run-commutes (suc n) ((s , p) , q) =
      cong (λ tail → T.flatten (fst (T.C2.generator ((s , p) , q))) ,
        snd (T.C2.generator ((s , p) , q)) , tail)
        (run-commutes n (fst (T.C2.generator ((s , p) , q))))

module HistoryPentagon {ℓ : Level} (A : Type ℓ) (B : A → Type ℓ)
  (C : (ab : Σ A B) → Type ℓ) (D : (abc : Σ (Σ A B) C) → Type ℓ) where
  module P = Four.Pentagon A B C D
  module Witnessed (R : P.P0 → P.P0 → Type ℓ)
    (g : (x : P.P0) → Σ[ y ∈ P.P0 ] R x y) where
    H0 = History P.P0 R
    H1 = History P.P1 (λ x y → R (P.decode1 x) (P.decode1 y))
    H2 = History P.P2 (λ x y → R (P.decode2 x) (P.decode2 y))
    H3 = History P.P3 (λ x y → R (P.decode3 x) (P.decode3 y))
    H4 = History P.P4 (λ x y → R (P.decode4 x) (P.decode4 y))

    h01 : (n : ℕ) (x : P.P0) → H0 n x → H1 n (Iso.fun P.e01 x)
    h01 zero x h = tt*
    h01 (suc n) x (y , w , h) = Iso.fun P.e01 y , w , h01 n y h
    h12 : (n : ℕ) (x : P.P1) → H1 n x → H2 n (Iso.fun P.e12 x)
    h12 zero x h = tt*
    h12 (suc n) x (y , w , h) = Iso.fun P.e12 y , w , h12 n y h
    h23 : (n : ℕ) (x : P.P2) → H2 n x → H3 n (Iso.fun P.e23 x)
    h23 zero x h = tt*
    h23 (suc n) x (y , w , h) = Iso.fun P.e23 y , w , h23 n y h
    h04 : (n : ℕ) (x : P.P0) → H0 n x → H4 n (Iso.fun P.e04 x)
    h04 zero x h = tt*
    h04 (suc n) x (y , w , h) = Iso.fun P.e04 y , w , h04 n y h
    h43 : (n : ℕ) (x : P.P4) → H4 n x → H3 n (Iso.fun P.e43 x)
    h43 zero x h = tt*
    h43 (suc n) x (y , w , h) = Iso.fun P.e43 y , w , h43 n y h

    long short : (n : ℕ) (x : P.P0) → H0 n x
      → H3 n (Iso.fun P.e43 (Iso.fun P.e04 x))
    long n x h = h23 n _ (h12 n _ (h01 n x h))
    short n x h = h43 n _ (h04 n x h)
    history-pentagon : (n : ℕ) (x : P.P0) (h : H0 n x) → long n x h ≡ short n x h
    history-pentagon zero x h = refl
    history-pentagon (suc n) x (y , w , h) =
      cong (λ tail → Iso.fun P.e43 (Iso.fun P.e04 y) , w , tail)
        (history-pentagon n y h)
    generated-history-pentagon : (n : ℕ) (x : P.P0)
      → long n x (run g n x) ≡ short n x (run g n x)
    generated-history-pentagon n x = history-pentagon n x (run g n x)

module SelectionFixture where
  module N = Nested.Example
  module H = Specialization.Second Selection.State Selection.SelectionWitness
    First.selection-pair N.second-domain (λ v → refl) (λ v p → p)
  all-lengths : (n : ℕ)
    → H.flatten-history n N.request (run H.T.C2.generator n N.request)
      ≡ run H.T.direct-generator n (H.T.flatten N.request)
  all-lengths n = H.run-commutes n N.request

  module D1 = Four.Domains Selection.State Selection.SelectionWitness First.selection-pair
  module D2 = D1.Second N.second-domain (λ v → refl) (λ v p → p)
  module D3 = D2.Third Triple.SelectionExample.third-domain (λ v → refl) (λ v p → p)
  fourth-domain : D3.M4.Domain
  fourth-domain = record
    { compute = λ v → fst (D3.C3.generator v)
    ; Allowed = λ _ → Lift {j = ℓ-suc ℓ-zero} Unit
    ; LawInput = Lift {j = ℓ-suc ℓ-zero} Unit
    ; request = λ _ → Triple.SelectionExample.example
    ; expected = λ _ → fst (D3.C3.generator Triple.SelectionExample.example)
    ; law = λ _ → refl }
  module D4 = D3.Fourth fourth-domain (λ v → refl) (λ v p → p)
  module P = HistoryPentagon D1.C1.State (D1.M2.Domain.Allowed N.second-domain)
    (D2.M3.Domain.Allowed Triple.SelectionExample.third-domain)
    (D3.M4.Domain.Allowed fourth-domain)
  module W = P.Witnessed D4.C4.Relation D4.C4.generator
  four-domain-history-pentagon : (n : ℕ) (x : D4.C4.State)
    → W.long n x (run D4.C4.generator n x) ≡ W.short n x (run D4.C4.generator n x)
  four-domain-history-pentagon = W.generated-history-pentagon
