{-# OPTIONS --safe --cubical --guardedness #-}
module NativeQueryWordRealization where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.List.Base using (List; []; _∷_; _++_)
import NativeQueryControlledRecorder as R
import NativeSeedTransitionProbe as Q
import SeedAttachedObserver as Seed
import BoundaryGeneratedQuestions as B
import NativeTableRegression as Native
open Seed using (Vertex; A; B; C; D)

-- Exactly the eight generators of the frozen one-object word language.
data Op : Type where
  LABC LADB QAB QBC QCA QAD QDB QBA : Op

post : (Vertex ≃ Vertex) → R.Carrier → R.Carrier
post h (e , b) = compEquiv e h , b

post-equivalence : (h : Vertex ≃ Vertex) → R.Carrier ≃ R.Carrier
post-equivalence h = isoToEquiv (iso (post h) (post (invEquiv h)) right left)
  where
  right : (c : R.Carrier) → post h (post (invEquiv h) c) ≡ c
  right (e , b) = cong (λ f → f , b)
    (sym (compEquiv-assoc e (invEquiv h) h)
      ∙ cong (compEquiv e) (invEquiv-is-linv h) ∙ compEquivEquivId e)
  left : (c : R.Carrier) → post (invEquiv h) (post h c) ≡ c
  left (e , b) = cong (λ f → f , b)
    (sym (compEquiv-assoc e h (invEquiv h))
      ∙ cong (compEquiv e) (invEquiv-is-rinv h) ∙ compEquivEquivId e)

operation : Op → R.Carrier ≃ R.Carrier
operation LABC = post-equivalence Q.ABC
operation LADB = post-equivalence Q.ADB
operation QAB = R.record-equivalence A B
operation QBC = R.record-equivalence B C
operation QCA = R.record-equivalence C A
operation QAD = R.record-equivalence A D
operation QDB = R.record-equivalence D B
operation QBA = R.record-equivalence B A

step : Op → R.Carrier → R.Carrier
step o = equivFun (operation o)

filler : (o : Op) (c : R.Carrier)
  → B.Filler (R.prepared c) (R.prepared (step o c))
filler o c = operation o , refl

native-step : Op → R.Carrier → R.Carrier
native-step o c = equivFun
  (fst (equivFun (Native.actual-filler-equivalence
    (R.prepared c) (R.prepared (step o c))) (filler o c))) c

native-step-agrees : (o : Op) (c : R.Carrier) → native-step o c ≡ step o c
native-step-agrees o c = refl

run : List Op → R.Carrier → R.Carrier
run [] c = c
run (o ∷ os) c = run os (step o c)

native-run : List Op → R.Carrier → R.Carrier
native-run [] c = c
native-run (o ∷ os) c = native-run os (native-step o c)

native-run-agrees : (os : List Op) (c : R.Carrier) → native-run os c ≡ run os c
native-run-agrees [] c = refl
native-run-agrees (o ∷ os) c = native-run-agrees os (step o c)

chronological-composition : (u v : List Op) (c : R.Carrier)
  → run (u ++ v) c ≡ run v (run u c)
chronological-composition [] v c = refl
chronological-composition (o ∷ os) v c = chronological-composition os v (step o c)

word-equivalence : List Op → R.Carrier ≃ R.Carrier
word-equivalence [] = idEquiv R.Carrier
word-equivalence (o ∷ os) = compEquiv (operation o) (word-equivalence os)

word-equivalence-agrees : (os : List Op) (c : R.Carrier)
  → equivFun (word-equivalence os) c ≡ run os c
word-equivalence-agrees [] c = refl
word-equivalence-agrees (o ∷ os) c = word-equivalence-agrees os (step o c)

word-filler : (os : List Op) (c : R.Carrier)
  → B.Filler (R.prepared c) (R.prepared (run os c))
word-filler os c = word-equivalence os , word-equivalence-agrees os c

-- The selected-value witness need not be judgmentally refl for a variable word.
native-whole-run : List Op → R.Carrier → R.Carrier
native-whole-run os c = equivFun
  (fst (equivFun (Native.actual-filler-equivalence
    (R.prepared c) (R.prepared (run os c))) (word-filler os c))) c

native-whole-run-agrees : (os : List Op) (c : R.Carrier)
  → native-whole-run os c ≡ run os c
native-whole-run-agrees = word-equivalence-agrees

retained-word-filler : (os : List Op) (c : R.Carrier)
  → R.W.value (B.retain-filler (R.prepared c)
      (R.prepared (run os c)) (word-filler os c)) ≡ word-filler os c
retained-word-filler os c = refl
