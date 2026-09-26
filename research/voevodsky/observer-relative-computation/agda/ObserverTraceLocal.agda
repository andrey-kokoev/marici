{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverTraceLocal where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Sigma.Base using (fst)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import Cubical.Data.Fin.Arithmetic using (_+ₘ_; +ₘ-rUnit)
open import Cubical.Data.Empty.Base using (⊥)
import ObserverInternalComparison as C
import ObserverComparisonCompression as P
import ObserverJointRefinement as J
import ObserverFiniteCyclicBoundary as B
import ObserverSignedCyclicCover as S
import ObserverSignedNormalization as N
import ObserverFiniteAdaptive as T
module F = T.F

visited : T.Protocol → N.Loop → List ℕ
visited (T.done label) p = []
visited (T.query sensor test yes no) p = F.period-code sensor ∷
  T.choose (T.sameNat (fst (F.read sensor p)) test) (visited yes p) (visited no p)

extract : List T.Event → List ℕ
extract [] = []
extract (T.finished label ∷ rest) = extract rest
extract (T.answer sensor value ∷ rest) = F.period-code sensor ∷ extract rest

visited-is-transcript : (t : T.Protocol) (p : N.Loop) → visited t p ≡ extract (T.run t p)
visited-is-transcript (T.done label) p = refl
visited-is-transcript (T.query sensor test yes no) p with T.sameNat (fst (F.read sensor p)) test
... | true = cong (F.period-code sensor ∷_) (visited-is-transcript yes p)
... | false = cong (F.period-code sensor ∷_) (visited-is-transcript no p)

Agreement : List ℕ → N.Loop → N.Loop → Type
Agreement ns p q = (n : ℕ) → B.Member n ns → (x : S.State n)
  → subst (S.Fibre n) p x ≡ subst (S.Fibre n) q x

mutual
  replay : (t : T.Protocol) (p q : N.Loop) → Agreement (visited t q) p q → T.run t p ≡ T.run t q
  replay (T.done label) p q agree = refl
  replay (T.query sensor test yes no) p q agree =
    cong (λ value → T.answer sensor value ∷
      T.choose (T.sameNat (fst value) test) (T.run yes p) (T.run no p))
      (agree (F.period-code sensor) B.here (F.phase sensor))
    ∙ cong (T.answer sensor (F.read sensor q) ∷_)
      (branch (T.sameNat (fst (F.read sensor q)) test) yes no p q
        (λ n member → agree n (B.there member)))

  branch : (b : Bool) (yes no : T.Protocol) (p q : N.Loop)
    → Agreement (T.choose b (visited yes q) (visited no q)) p q
    → T.choose b (T.run yes p) (T.run no p) ≡ T.choose b (T.run yes q) (T.run no q)
  branch true yes no p q agree = replay yes p q agree
  branch false yes no p q agree = replay no p q agree

alternative : T.Protocol → N.Loop
alternative t = P.path (J.power (B.common (visited t refl)))

same-transcript : (t : T.Protocol) → T.run t (alternative t) ≡ T.run t refl
same-transcript t = replay t (alternative t) refl (λ n member x →
  F.power-action n (B.common (visited t refl)) x
    ∙ cong (x +ₘ_) (F.residue-zero (visited t refl) n member)
    ∙ +ₘ-rUnit x ∙ sym (substRefl {B = S.Fibre n} {x = C.base} x))

alternative-nontrivial : (t : T.Protocol) → alternative t ≡ refl → ⊥
alternative-nontrivial t = B.nontrivial (visited t refl)

-- A transcript predicate is a logical specification, not an extra
-- observation primitive. No finite zero transcript certifies uniqueness
-- over ALL loops without an additional domain hypothesis.
no-zero-certificate : (t : T.Protocol) (Certificate : List T.Event → Type)
  → Certificate (T.run t refl)
  → ((p : N.Loop) → Certificate (T.run t p) → p ≡ refl) → ⊥
no-zero-certificate t Certificate accepted sound = alternative-nontrivial t
  (sound (alternative t) (subst Certificate (sym (same-transcript t)) accepted))

no-trace-decoder : (t : T.Protocol) (recover : List T.Event → N.Loop)
  → ((p : N.Loop) → recover (T.run t p) ≡ p) → ⊥
no-trace-decoder t recover exact = alternative-nontrivial t
  (sym (exact (alternative t)) ∙ cong recover (same-transcript t) ∙ exact refl)
