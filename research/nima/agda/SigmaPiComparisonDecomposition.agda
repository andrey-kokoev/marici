{-# OPTIONS --safe --cubical --guardedness #-}
-- Checked using the installed agda-cubical.ps1 launcher.
-- See sigma-pi-comparison-decomposition.md for scope and verification.
module SigmaPiComparisonDecomposition where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Path using (PathP≃Path)
open import Cubical.Foundations.HLevels using (isEquiv-Σ≡Prop)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv-snd; ΣPath≃PathΣ; Σ≡Prop)
import WholePackageSigmaPi as Whole
import ProofRelevantCoherenceClosure as LiftPaths

module Decomposition (ℓ : Level) where
  open Whole.Universe ℓ

  pointwise : {I : Type ℓ} {F : I → Type ℓ} (f g : (i : I) → F i)
    → ((i : I) → f i ≡ g i) ≃ (f ≡ g)
  pointwise f g = isoToEquiv (iso funExt (λ p i j → p j i) (λ _ → refl) (λ _ → refl))

  equivalence-paths : (Q R : Code) (e f : El Q ≃ El R)
    → (equivFun e ≡ equivFun f) ≃ (e ≡ f)
  equivalence-paths Q R e f =
    Σ≡Prop isPropIsEquiv , isEquiv-Σ≡Prop isPropIsEquiv

  -- The graph projection has contractible fibres. Its inverse laws retain
  -- and reconstruct the original target and boundary witness, up to path.
  comparison-projection : (Q R : Code) (e : El Q ≃ El R)
    → El (comparison Q R e) ≃ El Q
  comparison-projection Q R e = isoToEquiv
    (iso fst (λ x → x , equivFun e x , refl) (λ _ → refl)
      (λ { (x , y , p) t → x , p t , (λ u → p (t ∧ u)) }))

  -- A finite collection of schemas, recursively applied at arbitrary code
  -- depth. Atomic/index identities remain explicitly required data.
  mutual
    Evidence : (Q : Code) → El Q → El Q → Type ℓ
    Evidence (atom A) x y = x ≡ y
    Evidence (E I F) x y = Σ[ p ∈ (fst x ≡ fst y) ]
      Evidence (F (fst y)) (transport (λ j → El (F (p j))) (snd x)) (snd y)
    Evidence (Pi I F) x y = (i : I) → Evidence (F i) (x i) (y i)
    Evidence (retain Q q R) x y = Evidence R x y
    Evidence (maps Q R) x y = (i : El Q) → Evidence R (x i) (y i)
    Evidence (paths Q a b) p q =
      invEq (decode-equiv Q a b) p ≡ invEq (decode-equiv Q a b) q
    Evidence (equivalences Q R) e f =
      (a : El Q) → Evidence R (equivFun e a) (equivFun f a)
    Evidence (comparison Q R e) x y = Evidence Q (fst x) (fst y)

    decode-equiv : (Q : Code) (x y : El Q) → Evidence Q x y ≃ (x ≡ y)
    decode-equiv (atom A) x y = idEquiv _
    decode-equiv (E I F) x y = compEquiv
      (Σ-cong-equiv-snd (λ p → compEquiv
        (decode-equiv (F (fst y))
          (transport (λ j → El (F (p j))) (snd x)) (snd y))
        (invEquiv (PathP≃Path (λ j → El (F (p j))) (snd x) (snd y)))))
      ΣPath≃PathΣ
    decode-equiv (Pi I F) x y = compEquiv
      (equivΠCod (λ i → decode-equiv (F i) (x i) (y i))) (pointwise x y)
    decode-equiv (retain Q q R) x y = decode-equiv R x y
    decode-equiv (maps Q R) x y = compEquiv
      (equivΠCod (λ i → decode-equiv R (x i) (y i))) (pointwise x y)
    decode-equiv (paths Q a b) p q =
      invEquiv (LiftPaths.pathLift (invEquiv (decode-equiv Q a b)))
    decode-equiv (equivalences Q R) e f = compEquiv
      (equivΠCod (λ a → decode-equiv R (equivFun e a) (equivFun f a)))
      (compEquiv (pointwise (equivFun e) (equivFun f)) (equivalence-paths Q R e f))
    decode-equiv (comparison Q R e) x y = compEquiv
      (decode-equiv Q (fst x) (fst y))
      (invEquiv (LiftPaths.pathLift (comparison-projection Q R e)))

  encode : (Q : Code) {x y : El Q} → x ≡ y → Evidence Q x y
  encode Q = invEq (decode-equiv Q _ _)

  decode : (Q : Code) {x y : El Q} → Evidence Q x y → x ≡ y
  decode Q = equivFun (decode-equiv Q _ _)

  witness-completeness : (Q : Code) {x y : El Q} (p : x ≡ y)
    → decode Q (encode Q p) ≡ p
  witness-completeness Q = secEq (decode-equiv Q _ _)

  evidence-recovery : (Q : Code) {x y : El Q} (c : Evidence Q x y)
    → encode Q (decode Q c) ≡ c
  evidence-recovery Q = retEq (decode-equiv Q _ _)

  -- Comparisons BETWEEN generated comparison witnesses are preserved too.
  higher-completeness : (Q : Code) {x y : El Q} (c d : Evidence Q x y)
    → (c ≡ d) ≃ (decode Q c ≡ decode Q d)
  higher-completeness Q c d = LiftPaths.pathLift (decode-equiv Q _ _)

  record Certificate : Type (ℓ-suc ℓ) where
    constructor certificate
    field
      source : Code
      left right : El source
      original-witness : left ≡ right
      decomposed : Evidence source left right
      recovery : decode source decomposed ≡ original-witness

  certify : (Q : Code) {x y : El Q} (p : x ≡ y) → Certificate
  certify Q {x} {y} p = certificate Q x y p (encode Q p) (witness-completeness Q p)

  reify-certificate : Certificate → Whole.Universe.Complete (ℓ-suc ℓ)
  reify-certificate c = Whole.Universe.pack (Whole.Universe.atom Certificate) c
