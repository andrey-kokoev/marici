{-# OPTIONS --safe --cubical --guardedness #-}
module NativeQueryControlledRecorder where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Sigma.Base using (_×_)
import NativeSeedTransitionProbe as Query
import BoundaryGeneratedQuestions as B
import NativeTableRegression as Native
import WholePackageSigmaPi as Whole
import SeedAttachedObserver as Seed
open Seed using (Vertex; A; B; C; D)

-- The source datum is a supplied vertex transport, not a physical amplitude.
Carrier : Type
Carrier = (Vertex ≃ Vertex) × Bool

toggle : Bool → Bool → Bool
toggle false b = b
toggle true false = true
toggle true true = false

toggle-twice : (q b : Bool) → toggle q (toggle q b) ≡ b
toggle-twice false b = refl
toggle-twice true false = refl
toggle-twice true true = refl

toggle-blank : (q : Bool) → toggle q false ≡ q
toggle-blank false = refl
toggle-blank true = refl

record-query : Vertex → Vertex → Carrier → Carrier
record-query x y (e , b) = e , toggle (Query.transition e x y) b

record-twice : (x y : Vertex) (c : Carrier)
  → record-query x y (record-query x y c) ≡ c
record-twice x y (e , b) =
  cong (λ bit → e , bit) (toggle-twice (Query.transition e x y) b)

record-equivalence : (x y : Vertex) → Carrier ≃ Carrier
record-equivalence x y = isoToEquiv
  (iso (record-query x y) (record-query x y) (record-twice x y) (record-twice x y))

source-unchanged : (x y : Vertex) (c : Carrier)
  → fst (record-query x y c) ≡ fst c
source-unchanged x y (e , b) = refl

blank-correct : (x y : Vertex) (e : Vertex ≃ Vertex)
  → snd (record-query x y (e , false)) ≡ Query.transition e x y
blank-correct x y e = toggle-blank (Query.transition e x y)

module W = Whole.Universe ℓ-zero
prepared : Carrier → W.Complete
prepared c = W.pack (W.atom Carrier) c

-- A genuine filler between the actual pointed complete packages.
record-filler : (x y : Vertex) (c : Carrier)
  → B.Filler (prepared c) (prepared (record-query x y c))
record-filler x y c = record-equivalence x y , refl

native-record : Vertex → Vertex → Carrier → Carrier
native-record x y c = equivFun
  (fst (equivFun
    (Native.actual-filler-equivalence (prepared c) (prepared (record-query x y c)))
    (record-filler x y c))) c

native-agrees : (x y : Vertex) (c : Carrier)
  → native-record x y c ≡ record-query x y c
native-agrees x y c = refl

native-blank-correct : (x y : Vertex) (e : Vertex ≃ Vertex)
  → snd (native-record x y (e , false)) ≡ Query.transition e x y
native-blank-correct = blank-correct

native-undo : (x y : Vertex) (c : Carrier)
  → native-record x y (native-record x y c) ≡ c
native-undo = record-twice

retained : (x y : Vertex) (c : Carrier) → W.Complete
retained x y c = B.retain-filler (prepared c)
  (prepared (record-query x y c)) (record-filler x y c)

retained-recorder-recovered : (x y : Vertex) (c : Carrier)
  → W.value (retained x y c) ≡ record-filler x y c
retained-recorder-recovered x y c = refl

-- Actual supplied source transports give different pointer outcomes.
identity-AB : snd (native-record A B (idEquiv Vertex , false)) ≡ false
identity-AB = refl
triangle-AB : snd (native-record A B (Query.ABC , false)) ≡ true
triangle-AB = refl

-- No Hilbert carrier, norm, tensor-product metric, apparatus or reset law
-- is introduced by this native equivalence and retained-filler construction.
