{-# OPTIONS --safe --cubical --guardedness #-}
module NativeTransitionInstrument where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sigma.Base using (_×_)
import NativeSeedTransitionProbe as Q
import SeedAttachedObserver as Seed
import BoundaryGeneratedQuestions as Boundary
import WholePackageSigmaPi as Whole
open Seed using (Vertex; A; B; C; D)

-- The extra Boolean memory and reversible XOR policy are explicit inputs
-- to this instrument construction, not a claim that observation forces it.
flip : Bool → Bool
flip false = true
flip true = false
flip-square : (b : Bool) → flip (flip b) ≡ b
flip-square false = refl
flip-square true = refl
write : Bool → Bool → Bool
write false b = b
write true b = flip b
write-square : (a b : Bool) → write a (write a b) ≡ b
write-square false b = refl
write-square true b = flip-square b
write-blank : (a : Bool) → write a false ≡ a
write-blank false = refl
write-blank true = refl

State : Type
State = Vertex × Bool
module W = Whole.Universe ℓ-zero
prepared : State → W.Complete
prepared x = W.pack (W.atom State) x

module Instrument (e : Vertex ≃ Vertex) (target : Vertex) where
  answer : Vertex → Bool
  answer x = Q.transition e x target

  record-only : State → State
  record-only (x , b) = x , write (answer x) b

  involutive : (s : State) → record-only (record-only s) ≡ s
  involutive (x , b) = cong (λ r → x , r) (write-square (answer x) b)

  equivalence : State ≃ State
  equivalence = isoToEquiv (iso record-only record-only involutive involutive)

  admitted : (s : State) → Boundary.Filler (prepared s) (prepared (record-only s))
  admitted s = equivalence , refl

  reads-query : (x : Vertex) → snd (record-only (x , false)) ≡ answer x
  reads-query x = write-blank (answer x)

  source-unchanged : (s : State) → fst (record-only s) ≡ fst s
  source-unchanged (x , b) = refl

module Test = Instrument Q.ABC B

-- Another actual vertex equivalence preserves this yes/no query. It rotates
-- the three states with answer false; no response value or scale is fitted.
h h-inverse : Vertex → Vertex
h A = A
h B = C
h C = D
h D = B
h-inverse A = A
h-inverse B = D
h-inverse C = B
h-inverse D = C
h-right : (x : Vertex) → h (h-inverse x) ≡ x
h-right A = refl
h-right B = refl
h-right C = refl
h-right D = refl
h-left : (x : Vertex) → h-inverse (h x) ≡ x
h-left A = refl
h-left B = refl
h-left C = refl
h-left D = refl
same-answer : (x : Vertex) → Test.answer (h x) ≡ Test.answer x
same-answer A = refl
same-answer B = refl
same-answer C = refl
same-answer D = refl

-- The rival is already a composition of the two source-derived cycles.
h-source : (x : Vertex) → h x ≡ Q.adb (Q.abc x)
h-source A = refl
h-source B = refl
h-source C = refl
h-source D = refl

frame-lift : State → State
frame-lift (x , b) = h x , b
unlift : State → State
unlift (x , b) = h-inverse x , b
lift-right : (s : State) → frame-lift (unlift s) ≡ s
lift-right (x , b) = cong (λ y → y , b) (h-right x)
lift-left : (s : State) → unlift (frame-lift s) ≡ s
lift-left (x , b) = cong (λ y → y , b) (h-left x)
lift-equiv : State ≃ State
lift-equiv = isoToEquiv (iso frame-lift unlift lift-right lift-left)

rival-equiv : State ≃ State
rival-equiv = compEquiv Test.equivalence lift-equiv
rival : State → State
rival = equivFun rival-equiv
rival-admitted : (s : State) → Boundary.Filler (prepared s) (prepared (rival s))
rival-admitted s = rival-equiv , refl

same-memory : (s : State) → snd (rival s) ≡ snd (Test.record-only s)
same-memory (x , b) = refl
rival-reads-query : (x : Vertex) → snd (rival (x , false)) ≡ Test.answer x
rival-reads-query = Test.reads-query
rival-preserves-query : (s : State) → Test.answer (fst (rival s)) ≡ Test.answer (fst s)
rival-preserves-query (x , b) = same-answer x

-- The rival acts within an answer fiber, yet changes a retained source
-- observable. Equal answers and reversible native admissibility do not
-- select one state-update law.
is-B : Vertex → Bool
is-B B = true
is-B _ = false
updates-distinct : Test.record-only (B , false) ≡ rival (B , false) → ⊥
updates-distinct p = false≢true (sym (cong (λ s → is-B (fst s)) p))
