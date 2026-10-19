{-# OPTIONS --safe --cubical --guardedness #-}
module NativeRelationAttachmentAction where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc; _+_; _·_)
open import RelationPacketEncoding
import ActualRelationPacketCase as C
import WholePackageSigmaPi as W

Vec : Type
Vec = Σ[ x ∈ ℤ ] Σ[ y ∈ ℤ ] ℤ
Pair : Type
Pair = Σ[ x ∈ ℤ ] ℤ
zeroV : Vec
zeroV = pos 0 , pos 0 , pos 0
zeroQ : Pair
zeroQ = pos 0 , pos 0
unitA : Vec
unitA = pos 1 , pos 0 , pos 0
unitV : Vec
unitV = pos 0 , pos 0 , pos 1
unitQ : Pair
unitQ = pos 1 , pos 0

-- Read the source-computed matrix FROM the actual retained attachment.
-- Its domain uses nonnegative matrix entries; coordinates are signed integers.
item : ℕ → List Datum → Datum
item zero (x ∷ xs) = x
item (suc n) (x ∷ xs) = item n xs
item _ [] = nat 0
entry : ℕ → Datum → Datum
entry n (tuple xs) = item n xs
entry _ _ = nat 0
coefficient : Datum → ℤ
coefficient (nat n) = pos n
coefficient (neg zero) = pos 0
coefficient (neg (suc n)) = negsuc n
coefficient _ = pos 0

row-action : Datum → Vec → ℤ
row-action row (x , y , z) =
  (coefficient (entry 0 row) · x + coefficient (entry 1 row) · y)
    + coefficient (entry 2 row) · z
matrix-action : Datum → Vec → Vec
matrix-action matrix v = row-action (entry 0 matrix) v ,
  row-action (entry 1 matrix) v , row-action (entry 2 matrix) v

right : Case → Vec → Vec
right c = matrix-action (entry 3 (Case.attachment c))
disconnected : Case → Vec → Vec
disconnected c = matrix-action (entry 4 (Case.attachment c))

-- These reductions bind the evaluator to the exported actual source action.
right-formula : (v : Vec) → right C.actual v ≡ (pos 0 , pos 0 , fst v)
right-formula (x , y , z) = refl
disconnected-formula : (v : Vec) → disconnected C.actual v ≡ zeroV
disconnected-formula (x , y , z) = refl
right-a : right C.actual unitA ≡ unitV
right-a = refl
right-square-zero : (v : Vec) → right C.actual (right C.actual v) ≡ zeroV
right-square-zero (x , y , z) = refl

-- A native result retains the original certified answer AND before/after data.
record Applied (c : Case) (v : Vec) : Type where
  constructor applied
  field
    packet : Answer c
    packet-correct : packet ≡ solve c
    before after : Vec
    before-correct : before ≡ v
    after-correct : after ≡ right c v

execute : (c : Case) (v : Vec) → Applied c v
execute c v = applied (solve c) refl v (right c v) refl refl
complete-action : (c : Case) (v : Vec) → W.Universe.Complete ℓ-zero
complete-action c v = W.Universe.pack (W.Universe.atom (Applied c v)) (execute c v)

retained-case : (c : Case) (v : Vec)
  → Answer.retained (Applied.packet (W.Universe.value (complete-action c v))) ≡ c
retained-case c v = refl
retained-input : (c : Case) (v : Vec)
  → Applied.before (W.Universe.value (complete-action c v)) ≡ v
retained-input c v = refl
retained-action : (c : Case) (v : Vec)
  → right (Answer.retained (Applied.packet (W.Universe.value (complete-action c v)))) v
      ≡ right c v
retained-action c v = refl

-- The quotient forgets the product coordinate. Its induced right-b action is0.
quotient : Vec → Pair
quotient (x , y , z) = x , y
third : Vec → ℤ
third v = snd (snd v)
quotient-kills-action : (v : Vec) → quotient (right C.actual v) ≡ zeroQ
quotient-kills-action (x , y , z) = refl

is-zero : ℤ → Bool
is-zero (pos zero) = true
is-zero _ = false
one-not-zero : pos 1 ≡ pos 0 → ⊥
one-not-zero p = false≢true (cong is-zero p)

-- Even without assuming additivity, no zero-preserving section can intertwine
-- these actions. For linear/module sections zero preservation is necessary.
no-action-section : (section : Pair → Vec)
  → ((q : Pair) → quotient (section q) ≡ q)
  → section zeroQ ≡ zeroV
  → ((q : Pair) → right C.actual (section q) ≡ section zeroQ)
  → ⊥
no-action-section section recover zero-law commute = one-not-zero
  (sym (cong fst (recover unitQ))
   ∙ sym (cong third (right-formula (section unitQ)))
   ∙ cong third (commute unitQ)
   ∙ cong third zero-law)

no-disconnected-substitute : right C.actual unitA ≡ disconnected C.actual unitA → ⊥
no-disconnected-substitute p = one-not-zero (cong third p)
