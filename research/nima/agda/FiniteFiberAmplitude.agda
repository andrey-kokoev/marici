{-# OPTIONS --safe --cubical --guardedness #-}
module FiniteFiberAmplitude where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.List.Base using (List; []; _∷_; map)
import TableFibrationCycle as Kernel

-- The coefficient operations and local weights are supplied inputs. Nothing
-- here derives a field theory, a measure, or a propagator from unweighted rows.
module Weighted {ℓ : Level} (W : Type ℓ) (zero : W) (add : W → W → W) where
  select : Bool → W → W
  select false w = zero
  select true w = w
  fold : {R : Type ℓ} → (R → W) → List R → W
  fold f [] = zero
  fold f (r ∷ rs) = add (f r) (fold f rs)
  amplitude : {L B P : Type ℓ} (table : Kernel.Table L B P)
    → List (Kernel.Table.Rows table) → (B → Bool) → (L → W) → W
  amplitude table enumeration boundary weight = fold
    (λ r → select (boundary (Kernel.Table.from table r)) (weight (Kernel.Table.label table r))) enumeration
  fold-map : {R S : Type ℓ} (f : R → W) (g : S → W) (encode : R → S)
    → ((r : R) → f r ≡ g (encode r))
    → (rs : List R) → fold f rs ≡ fold g (map encode rs)
  fold-map f g encode compatible [] = refl
  fold-map f g encode compatible (r ∷ rs) =
    cong₂ add (compatible r) (fold-map f g encode compatible rs)

  -- Enumerations retain multiplicity. For a fiber bijection the caller must
  -- also establish that these are complete, duplicate-free enumerations.
  fiber-readout-commutes : {R S : Type ℓ}
    (encode : R → S) (old-mark : R → Bool) (native-mark : S → Bool)
    (old-weight : R → W) (native-weight : S → W)
    → ((r : R) → old-mark r ≡ native-mark (encode r))
    → ((r : R) → old-weight r ≡ native-weight (encode r))
    → (rs : List R)
    → fold (λ r → select (old-mark r) (old-weight r)) rs
      ≡ fold (λ s → select (native-mark s) (native-weight s)) (map encode rs)
  fiber-readout-commutes encode old-mark native-mark old-weight native-weight marks weights =
    fold-map _ _ encode (λ r → cong₂ select (marks r) (weights r))
