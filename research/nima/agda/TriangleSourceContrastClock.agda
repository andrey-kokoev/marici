{-# OPTIONS --safe --cubical --guardedness #-}
module TriangleSourceContrastClock where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.List.Base using (List; []; _∷_; _++_)
open import Cubical.Data.Nat.Base using (ℕ; suc)
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false; false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Algebra.CommRing.Base
open import Cubical.Algebra.CommRing.Instances.Int using (ℤCommRing)
open import Cubical.Tactics.CommRingSolver
import NativeTriangleCompositionSuccessor as Source
open Source using (Edge; end; Joined)
open import SeedAttachedObserver using (Vertex; A; B; C; D)
open CommRingStr (snd ℤCommRing)

same : Vertex → Vertex → ℤ
same A A = pos 1
same B B = pos 1
same C C = pos 1
same D D = pos 1
same _ _ = pos 0

Counts : Type
Counts = Vertex → ℤ
incoming : List Edge → Counts → Counts
incoming [] c v = pos 0
incoming (e ∷ es) c v = same (end e) v · c (fst e) + incoming es c v
step : Counts → Counts
step = incoming (Source.left ++ Source.right)

count : List Joined → Counts
count [] v = pos 0
count (w ∷ ws) v = same (end (Joined.second w)) v + count ws v
actual : Counts
actual v = count (Source.Next.words Source.LR) v - count (Source.Next.words Source.RL) v

Pair : Type
Pair = ℤ × ℤ
encode : Pair → Counts
encode (a , b) A = a
encode (a , b) B = - a
encode (a , b) C = b
encode (a , b) D = - b
advance : Pair → Pair
advance (a , b) = b - a , - a
initial : Pair
initial = pos 1 , negsuc 0
actual-is-encoded : actual ≡ encode initial
actual-is-encoded = funExt λ { A → refl ; B → refl ; C → refl ; D → refl }

-- The count transition is computed from the actual six typed source edges,
-- not postulated as a three-state cycle.
intertwines : (p : Pair) → step (encode p) ≡ encode (advance p)
intertwines (a , b) = funExt λ
  { A → solve! ℤCommRing
  ; B → solve! ℤCommRing
  ; C → solve! ℤCommRing
  ; D → solve! ℤCommRing }

third-return : (p : Pair) → advance (advance (advance p)) ≡ p
third-return (a , b) = λ i → first i , second i
  where
  first : fst (advance (advance (advance (a , b)))) ≡ a
  first = solve! ℤCommRing
  second : snd (advance (advance (advance (a , b)))) ≡ b
  second = solve! ℤCommRing

run : ℕ → Counts → Counts
run 0 c = c
run (suc n) c = step (run n c)
phase : ℕ → Pair → Pair
phase 0 p = p
phase (suc n) p = advance (phase n p)
run-intertwines : (n : ℕ) (p : Pair) → run n (encode p) ≡ encode (phase n p)
run-intertwines 0 p = refl
run-intertwines (suc n) p = cong step (run-intertwines n p) ∙ intertwines (phase n p)
phase-period : (n : ℕ) (p : Pair) → phase (suc (suc (suc n))) p ≡ phase n p
phase-period 0 p = third-return p
phase-period (suc n) p = cong advance (phase-period n p)
sector-period : (n : ℕ) (p : Pair) → run (suc (suc (suc n))) (encode p) ≡ run n (encode p)
sector-period n p = run-intertwines (suc (suc (suc n))) p
  ∙ cong encode (phase-period n p) ∙ sym (run-intertwines n p)
actual-period : (n : ℕ) → run (suc (suc (suc n))) actual ≡ run n actual
actual-period n = cong (run (suc (suc (suc n)))) actual-is-encoded
  ∙ sector-period n initial ∙ sym (cong (run n) actual-is-encoded)

negative : ℤ → Bool
negative (pos n) = false
negative (negsuc n) = true
not-first-return : run 1 actual ≡ actual → ⊥
not-first-return p = true≢false (cong (λ c → negative (c A)) p)
not-second-return : run 2 actual ≡ actual → ⊥
not-second-return p = false≢true (cong (λ c → negative (c C)) p)

-- No real-valued duration, physical event emitter, or rate occurs in the
-- theorem's premises or conclusion. This is a source count-phase recurrence.
