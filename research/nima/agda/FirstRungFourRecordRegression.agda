{-# OPTIONS --safe --cubical --guardedness #-}
module FirstRungFourRecordRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Sigma.Base using (_×_)
import TableFibrationCycle as F

next-column : F.Column → F.Column
next-column F.label-column = F.from-column
next-column F.from-column = F.to-column
next-column F.to-column = F.label-column

module Descent {ℓ : Level} {L S T : Type ℓ} where
  step : F.Column → F.Table L S T → F.Table L S T
  step k q = F.restore-table {L = L} {S = S} {T = T} k (F.fibrate-table q k)

  descend : ℕ → F.Column → F.Table L S T → F.Table L S T
  descend zero k q = q
  descend (suc n) k q = descend n (next-column k) (step k q)

  retained : (n : ℕ) (k : F.Column) (q : F.Table L S T)
    → F.TableIso (descend n k q) q
  retained zero k q = F.identity-iso q
  retained (suc n) k q = F.compose (retained n (next-column k) (step k q))
    (F.restore-correct q k)

  floor : F.Table L S T → F.Table L S T
  floor q = descend 8 F.label-column q
  floor-iso : (q : F.Table L S T) → F.TableIso (floor q) q
  floor-iso q = retained 8 F.label-column q
  run : (q : F.Table L S T) → F.Table.Rows q → F.Table.Rows (floor q)
  run q = Iso.inv (F.TableIso.rows (floor-iso q))
  recover : (q : F.Table L S T) → F.Table.Rows (floor q) → F.Table.Rows q
  recover q = Iso.fun (F.TableIso.rows (floor-iso q))
  roundtrip : (q : F.Table L S T) (x : F.Table.Rows q) → recover q (run q x) ≡ x
  roundtrip q = Iso.rightInv (F.TableIso.rows (floor-iso q))
  no-extra-floor-values : (q : F.Table L S T) (r : F.Table.Rows (floor q))
    → run q (recover q r) ≡ r
  no-extra-floor-values q = Iso.leftInv (F.TableIso.rows (floor-iso q))

single : F.Table Unit Unit Unit
single = F.table Unit (λ _ → tt) (λ _ → tt) (λ _ → tt)
module One = Descent {L = Unit} {S = Unit} {T = Unit}
single-floor = One.run single tt

X : Type
X = Bool × Bool
four : F.Table X Bool Bool
four = F.table X (λ x → x) fst snd
module Four = Descent {L = X} {S = Bool} {T = Bool}

floor00 = Four.run four (false , false)
floor01 = Four.run four (false , true)
floor10 = Four.run four (true , false)
floor11 = Four.run four (true , true)

label-preserved : (x : X) → F.Table.label (Four.floor four) (Four.run four x) ≡ x
label-preserved x = sym (F.TableIso.preserves-label (Four.floor-iso four) (Four.run four x))
  ∙ Four.roundtrip four x
from-preserved : (x : X) → F.Table.from (Four.floor four) (Four.run four x) ≡ fst x
from-preserved x = sym (F.TableIso.preserves-from (Four.floor-iso four) (Four.run four x))
  ∙ cong fst (Four.roundtrip four x)
to-preserved : (x : X) → F.Table.to (Four.floor four) (Four.run four x) ≡ snd x
to-preserved x = sym (F.TableIso.preserves-to (Four.floor-iso four) (Four.run four x))
  ∙ cong snd (Four.roundtrip four x)

-- The outer key after the eighth selector is the from-coordinate.
outer-from-key : (x : X) → fst (Four.run four x) ≡ fst x
outer-from-key x = refl
