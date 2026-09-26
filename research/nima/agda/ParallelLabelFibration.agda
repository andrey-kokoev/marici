{-# OPTIONS --safe --cubical --guardedness #-}
module ParallelLabelFibration where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
import TableFibrationCycle as F

-- Group by an endpoint, then by the original row label within each fiber.
module Nested {ℓ : Level} {R B L : Type ℓ} (endpoint : R → B) (label : R → L) where
  GroupedRows : Type ℓ
  GroupedRows = Σ B (λ b → Σ L (λ l →
    Σ (F.fibrate endpoint b) (λ u → label (fst u) ≡ l)))
  recover : GroupedRows → R
  recover (b , l , (r , p) , q) = r
  regroup : R → GroupedRows
  regroup r = endpoint r , label r , (r , refl) , refl
  recovery : Iso GroupedRows R
  Iso.fun recovery = recover
  Iso.inv recovery = regroup
  Iso.rightInv recovery r = refl
  Iso.leftInv recovery (b , l , (r , p) , q) i =
    p i , q i , (r , (λ j → p (i ∧ j))) , (λ j → q (i ∧ j))

  -- An involution requires declaring what the operation does on BOTH sorts.
  -- This extension is not grouping applied twice: it groups, then ungroups.
  Presentation : Type ℓ
  Presentation = R ⊎ GroupedRows
  C : Presentation → Presentation
  C (inl r) = inr (regroup r)
  C (inr g) = inl (recover g)
  C-involutive : (x : Presentation) → C (C x) ≡ x
  C-involutive (inl r) = refl
  C-involutive (inr g) = cong inr (Iso.leftInv recovery g)
  observe : {A : Type ℓ} → (R → A) → Presentation → A
  observe w (inl r) = w r
  observe w (inr g) = w (recover g)
  observe-C : {A : Type ℓ} (w : R → A) (x : Presentation)
    → observe w (C x) ≡ observe w x
  observe-C w (inl r) = refl
  observe-C w (inr g) = refl

module Parallel {ℓ : Level} {L S T : Type ℓ} (table : F.Table L S T) where
  open F.Table table
  module Input = Nested from label
  module Output = Nested to label
  -- The parallel branches share the original row, not merely its label.
  input-output-recovery : (r : Rows)
    → Input.recover (Input.regroup r) ≡ Output.recover (Output.regroup r)
  input-output-recovery r = refl
  input-readout : {A : Type ℓ} (w : Rows → A) (r : Rows)
    → w (Input.recover (Input.regroup r)) ≡ w r
  input-readout w r = refl
  output-readout : {A : Type ℓ} (w : Rows → A) (r : Rows)
    → w (Output.recover (Output.regroup r)) ≡ w r
  output-readout w r = refl

-- No additive residual is defined on these types. Subtraction needs a further
-- common additive representation; its equations are separate obligations.
