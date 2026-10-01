{-# OPTIONS --safe --cubical --guardedness #-}
module PathLedgerInterpretations where

open import Cubical.Foundations.Prelude
import RetainedComparisonSeries as R

-- Checked readout lemmas, NOT an interpretation of the Python path ledger.
-- In particular no identification of compose_payloads with pointwise product
-- is assumed. Split/reassemble, stage maps, and their bridge remain open.
module PathOps where
  filler-pull-is-native : {A : Type} (f : R.Filler) (v : R.Point → A)
    → R.native-pull f v ≡ R.pull f v
  filler-pull-is-native = R.native-pull-agrees

  -- The operation must be supplied. No multiplication exists on arbitrary A,
  -- and no bilinearity follows without an additive structure and its laws.
  pointwise : {A D E : Type} → (A → D → E)
    → (R.Point → A) → (R.Point → D) → R.Point → E
  pointwise op u v x = op (u x) (v x)

  pull-pointwise : {A D E : Type} (op : A → D → E)
    (f : R.Filler) (u : R.Point → A) (v : R.Point → D)
    → R.pull f (pointwise op u v)
      ≡ pointwise op (R.pull f u) (R.pull f v)
  pull-pointwise = R.pull-pointwise
