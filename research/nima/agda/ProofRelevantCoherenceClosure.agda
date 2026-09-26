{-# OPTIONS --safe --cubical --guardedness #-}
module ProofRelevantCoherenceClosure where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Equiv.HalfAdjoint using (congIso)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv-snd)

private
  variable
    ℓ ℓ' ℓQ ℓT : Level
    A : Type ℓ
    B : Type ℓ'

-- The actual forward function is path application, with an inverse and
-- both inverse homotopies supplied by the checked library construction.
pathLift : (e : A ≃ B) {x y : A}
         → (x ≡ y) ≃ (equivFun e x ≡ equivFun e y)
pathLift e = isoToEquiv (congIso (equivToIso e))

pathLift-computes : (e : A ≃ B) {x y : A} (p : x ≡ y)
                 → equivFun (pathLift e) p ≡ cong (equivFun e) p
pathLift-computes e p = refl

higherLift : (e : A ≃ B) {x y : A} (p q : x ≡ y)
           → (p ≡ q) ≃ (cong (equivFun e) p ≡ cong (equivFun e) q)
higherLift e p q = pathLift (pathLift e)

-- Full trace data are arbitrary and proof-relevant. No truncation or
-- inhabitedness test is applied to either traces or comparison witnesses.
module Records {Q : Type ℓQ} {Y : Type ℓ} {Z : Type ℓ'}
               (Trace : Q → Type ℓT)
               (left right : (q : Q) → Trace q → Y)
               (e : Y ≃ Z) where

  SourceRecord : Type (ℓ-max ℓQ (ℓ-max ℓT ℓ))
  SourceRecord = Σ[ q ∈ Q ] Σ[ t ∈ Trace q ] (left q t ≡ right q t)

  TargetRecord : Type (ℓ-max ℓQ (ℓ-max ℓT ℓ'))
  TargetRecord = Σ[ q ∈ Q ] Σ[ t ∈ Trace q ]
                  (equivFun e (left q t) ≡ equivFun e (right q t))

  recordLift : SourceRecord ≃ TargetRecord
  recordLift = Σ-cong-equiv-snd (λ q → Σ-cong-equiv-snd (λ t → pathLift e))

  source-retained : (r : SourceRecord) → fst (equivFun recordLift r) ≡ fst r
  source-retained r = refl

  trace-retained : (r : SourceRecord)
                 → fst (snd (equivFun recordLift r)) ≡ fst (snd r)
  trace-retained r = refl

  witness-transported : (r : SourceRecord)
                     → snd (snd (equivFun recordLift r))
                       ≡ cong (equivFun e) (snd (snd r))
  witness-transported r = refl

  record-roundtrip : (r : SourceRecord)
                   → invEq recordLift (equivFun recordLift r) ≡ r
  record-roundtrip = retEq recordLift

  target-roundtrip : (r : TargetRecord)
                   → equivFun recordLift (invEq recordLift r) ≡ r
  target-roundtrip = secEq recordLift

  -- The complete record equivalence is itself eligible for path lifting.
  recordPathLift : (r s : SourceRecord)
                 → (r ≡ s) ≃ (equivFun recordLift r ≡ equivFun recordLift s)
  recordPathLift r s = pathLift recordLift

  recordHigherLift : {r s : SourceRecord} (p q : r ≡ s)
                  → (p ≡ q) ≃
                    (cong (equivFun recordLift) p ≡ cong (equivFun recordLift) q)
  recordHigherLift p q = higherLift recordLift p q
