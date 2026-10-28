{-# OPTIONS --safe --cubical --guardedness #-}
module DependentFourReturn where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (hcomp-unique)

-- No isSet, proof irrelevance, chosen successor law or periodicity axiom.
module General {ℓ : Level} {S : Type ℓ} (G : S → S) where
  F : S → S
  F a = G (G (G (G a)))

  Per4 : Type ℓ
  Per4 = Σ S (λ a → F a ≡ a)

  shift : Per4 → Per4
  shift (a , p) = G a , cong G p

  -- This square retains the dependent witness while moving its base along p.
  -- Its four sides are F(p), p, F(p), p, with the required orientations.
  return-square : (a : S) (p : F a ≡ a)
    → PathP (λ i → F (p i) ≡ p i) (cong F p) p
  return-square a p i j =
    hcomp (λ k → λ { (i = i0) → F (p j)
                    ; (i = i1) → p (j ∧ k)
                    ; (j = i0) → F (p i)
                    ; (j = i1) → p (i ∧ k) })
          (F (p (i ∨ j)))

  shift-four : (x : Per4) → shift (shift (shift (shift x))) ≡ x
  shift-four (a , p) i = p i , return-square a p i

  -- A map preserves this composition up to a path relative to its tube.
  -- The relative boundary, not just an unbased equality, is needed below.
  map-hcomp : (f : S → S) {φ : I}
    (u : I → Partial φ S) (u0 : S [ φ ↦ u i0 ])
    → (f (hcomp u (outS u0)) ≡
       hcomp (λ k o → f (u k o)) (f (outS u0)))
       [ φ ↦ (λ { (φ = i1) → refl }) ]
  map-hcomp f u u0 = inS (sym (outS
    (hcomp-unique (λ k o → f (u k o)) (inS (f (outS u0)))
      (λ k → inS (f (hfill u u0 k))))))

  -- First higher equivariance square for the ACTUAL return homotopy above.
  -- This does not assert all higher laws of a coherent C4 action.
  shift-four-equivariant : (x : Per4)
    → cong shift (shift-four x) ≡ shift-four (shift x)
  shift-four-equivariant (a , p) k i =
    G (p i) , λ j → outS (map-hcomp G
      (λ l → λ { (i = i0) → F (p j)
                 ; (i = i1) → p (j ∧ l)
                 ; (j = i0) → F (p i)
                 ; (j = i1) → p (i ∧ l) })
      (inS (F (p (i ∨ j))))) k

-- Separate source binding: actual free directed occurrences are NOT paths
-- in the identity type. Selecting this successor is additional input.
import ActualSeedEndpointTable as Seed
import SeedSeamPathComparisonBoundary as Free
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)

module SelectedSeed where
  open Seed using (Vertex; A; B; C; D; Occurrence; AD; DB; BC; CA)

  next : Vertex → Vertex
  next A = D
  next D = B
  next B = C
  next C = A

  selected : Vertex → Occurrence
  selected A = AD
  selected D = DB
  selected B = BC
  selected C = CA

  source-correct : (v : Vertex) → Seed.source (selected v) ≡ v
  source-correct A = refl
  source-correct D = refl
  source-correct B = refl
  source-correct C = refl

  target-correct : (v : Vertex) → Seed.target (selected v) ≡ next v
  target-correct A = refl
  target-correct D = refl
  target-correct B = refl
  target-correct C = refl

  open General next

  next-four : (v : Vertex) → F v ≡ v
  next-four A = refl
  next-four D = refl
  next-four B = refl
  next-four C = refl

  orbit : Per4
  orbit = A , next-four A

  dependent-return : shift (shift (shift (shift orbit))) ≡ orbit
  dependent-return = shift-four orbit

  history : Free.Path A A
  history = Free.step AD (Free.step DB (Free.step BC (Free.step CA Free.stop)))

  history-length : Free.length history ≡ 4
  history-length = refl

  is-empty : ℕ → Bool
  is-empty zero = true
  is-empty (suc n) = false

  history-not-erased : history ≡ Free.stop → ⊥
  history-not-erased p = true≢false (sym (cong (λ h → is-empty (Free.length h)) p))

  -- The terminal vertex comparison and the actual word remain separate fields.
  RetainedReturn : Type
  RetainedReturn = Σ Vertex (λ t → Σ (Free.Path A t) (λ h → t ≡ A))

  witnessed-return : RetainedReturn
  witnessed-return = A , history , refl

  retained-length : Free.length (witnessed-return .snd .fst) ≡ 4
  retained-length = refl
