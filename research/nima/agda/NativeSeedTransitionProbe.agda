{-# OPTIONS --safe --cubical --guardedness #-}
module NativeSeedTransitionProbe where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; true; false; _and_)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
import SeedAttachedObserver as Seed
import BoundaryGeneratedQuestions as B
import NativeTableRegression as Native
import WholePackageSigmaPi as Whole
open Seed using (Vertex; A; B; C; D)

-- The concrete task is to observe the result of an actual vertex transport.
-- It is not a physical detector or a rule selecting carrier amplitudes.
equal : Vertex → Vertex → Bool
equal A A = true
equal B B = true
equal C C = true
equal D D = true
equal _ _ = false

module W = Whole.Universe ℓ-zero
prepared : Vertex → W.Complete
prepared x = W.pack (W.atom Vertex) x

attached : (e : Vertex ≃ Vertex) (x : Vertex)
  → B.Filler (prepared x) (prepared (equivFun e x))
attached e x = e , refl

transition : (Vertex ≃ Vertex) → Vertex → Vertex → Bool
transition e x y = equal (equivFun e x) y

-- Evaluate the SAME filler through the existing native table equivalence.
native-transition : (e : Vertex ≃ Vertex) → Vertex → Vertex → Bool
native-transition e x y = equal
  (equivFun (fst (equivFun
    (Native.actual-filler-equivalence (prepared x) (prepared (equivFun e x)))
    (attached e x))) x) y

native-agrees : (e : Vertex ≃ Vertex) (x y : Vertex)
  → native-transition e x y ≡ transition e x y
native-agrees e x y = refl

retained-transition : (e : Vertex ≃ Vertex) → Vertex → Vertex → Bool
retained-transition e x y = equal
  (equivFun (fst (W.value (B.retain-filler (prepared x)
    (prepared (equivFun e x)) (attached e x)))) x) y

retention-preserves-query : (e : Vertex ≃ Vertex) (x y : Vertex)
  → retained-transition e x y ≡ transition e x y
retention-preserves-query e x y = refl

composition : (e f : Vertex ≃ Vertex) (x y : Vertex)
  → transition (compEquiv e f) x y ≡ transition f (equivFun e x) y
composition e f x y = refl

-- Actual triangle cycles, completed by fixing the unused vertex. This
-- construction is explicit; it does not promote each noninvertible seed
-- arrow to an equivalence on all vertices.
abc abc-inverse adb adb-inverse : Vertex → Vertex
abc A = B
abc B = C
abc C = A
abc D = D
abc-inverse A = C
abc-inverse B = A
abc-inverse C = B
abc-inverse D = D
adb A = D
adb B = A
adb C = C
adb D = B
adb-inverse A = B
adb-inverse B = D
adb-inverse C = C
adb-inverse D = A

abc-right : (x : Vertex) → abc (abc-inverse x) ≡ x
abc-right A = refl
abc-right B = refl
abc-right C = refl
abc-right D = refl
abc-left : (x : Vertex) → abc-inverse (abc x) ≡ x
abc-left A = refl
abc-left B = refl
abc-left C = refl
abc-left D = refl
adb-right : (x : Vertex) → adb (adb-inverse x) ≡ x
adb-right A = refl
adb-right B = refl
adb-right C = refl
adb-right D = refl
adb-left : (x : Vertex) → adb-inverse (adb x) ≡ x
adb-left A = refl
adb-left B = refl
adb-left C = refl
adb-left D = refl

ABC ADB : Vertex ≃ Vertex
ABC = isoToEquiv (iso abc abc-inverse abc-right abc-left)
ADB = isoToEquiv (iso adb adb-inverse adb-right adb-left)

abc-AB : abc A ≡ Seed.target Seed.AB
abc-AB = refl
abc-BC : abc B ≡ Seed.target Seed.BC
abc-BC = refl
abc-CA : abc C ≡ Seed.target Seed.CA
abc-CA = refl
adb-AD : adb A ≡ Seed.target Seed.AD
adb-AD = refl
adb-DB : adb D ≡ Seed.target Seed.DB
adb-DB = refl
adb-BA : adb B ≡ Seed.target Seed.BA
adb-BA = refl

-- The two old probe queries answer different questions on the SAME native
-- admitted transport; no scalar normalization can make them that same task.
fixes-endpoints : (Vertex ≃ Vertex) → Vertex → Vertex → Bool
fixes-endpoints e x y = equal (equivFun e x) x and equal (equivFun e y) y

identity-distinguishes-queries : transition (idEquiv Vertex) A B
  ≡ fixes-endpoints (idEquiv Vertex) A B → ⊥
identity-distinguishes-queries = false≢true

actual-cycle-transfers : native-transition ABC A B ≡ true
actual-cycle-transfers = refl
actual-cycle-not-endpoint-fixing : fixes-endpoints ABC A B ≡ false
actual-cycle-not-endpoint-fixing = refl
