{-# OPTIONS --safe --cubical --guardedness #-}
module FibrationRouteInterchange where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
import TableFibrationCycle as F

-- Actual input/output fibers, not a replacement grouping implementation.
module Routes {ℓ : Level} {L S T : Type ℓ} (table : F.Table L S T) where
  open F.Table table
  InputThenOutput : S → T → Type ℓ
  InputThenOutput s t = Σ (F.fibrate from s) (λ u → to (fst u) ≡ t)
  OutputThenInput : S → T → Type ℓ
  OutputThenInput s t = Σ (F.fibrate to t) (λ u → from (fst u) ≡ s)
  interchange : (s : S) (t : T) → Iso (InputThenOutput s t) (OutputThenInput s t)
  Iso.fun (interchange s t) ((r , p) , q) = (r , q) , p
  Iso.inv (interchange s t) ((r , q) , p) = (r , p) , q
  Iso.rightInv (interchange s t) _ = refl
  Iso.leftInv (interchange s t) _ = refl
  read-input-output : {A : Type ℓ} → (Rows → A) → {s : S} {t : T} → InputThenOutput s t → A
  read-input-output w ((r , p) , q) = w r
  read-output-input : {A : Type ℓ} → (Rows → A) → {s : S} {t : T} → OutputThenInput s t → A
  read-output-input w ((r , q) , p) = w r
  readout-commutes : {A : Type ℓ} (w : Rows → A) (s : S) (t : T) (u : InputThenOutput s t)
    → read-input-output w u ≡ read-output-input w (Iso.fun (interchange s t) u)
  readout-commutes w s t ((r , p) , q) = refl

-- This does not identify retained operation histories, arbitrary path-sensitive
-- observers, or extra connection/phase data not present in the table readout.
