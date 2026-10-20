{-# OPTIONS --safe --cubical --guardedness #-}
module SourceChainOverlap where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (cong-∙)
open import NativeExtensionFamilyAudit using (Vertex; A; B; C; D; AB; BC; CA; BA; AD; DB; sigma; sigma²; Seeds; pointQ)
import WholePackageResolution as Resolution
open Resolution.Generators ℓ-zero
open import RetainedPackageFeedback using (Chain; initial; extend; Total)
import RetainedFeedbackCovariance as R
import ForwardSourceLiftComposition as F
import SourceInitialOverlap as I

-- Normalize ONLY the presentation of the existing square, with a comparison
-- back to that exact witness below. No new cancellation choice is installed.
squareChain : (v : Vertex) (c : Chain v)
  → PathP (λ i → Chain (sigma² v i)) (R.moveChain (R.moveChain c)) c
squareChain v (initial .v d) i = initial (sigma² v i) (F.forward-square-initial v d i)
squareChain _ (extend c (_ , AB)) i = extend (squareChain A c i) (B , AB)
squareChain _ (extend c (_ , BC)) i = extend (squareChain B c i) (C , BC)
squareChain _ (extend c (_ , CA)) i = extend (squareChain C c i) (A , CA)
squareChain _ (extend c (_ , BA)) i = extend (squareChain B c i) (A , BA)
squareChain _ (extend c (_ , AD)) i = extend (squareChain A c i) (D , AD)
squareChain _ (extend c (_ , DB)) i = extend (squareChain D c i) (B , DB)
square : (c : Total) → R.move (R.move c) ≡ c
square (v , c) i = sigma² v i , squareChain v c i

ChainOverlap : (v : Vertex) → Chain v → Type₁
ChainOverlap A c = squareChain B (R.moveChain c) ≡ cong R.moveChain (squareChain A c)
ChainOverlap B c = squareChain A (R.moveChain c) ≡ cong R.moveChain (squareChain B c)
ChainOverlap C c = squareChain D (R.moveChain c) ≡ cong R.moveChain (squareChain C c)
ChainOverlap D c = squareChain C (R.moveChain c) ≡ cong R.moveChain (squareChain D c)
initialOverlap : (v : Vertex) (d : Resolve Seeds (pointQ v)) → ChainOverlap v (initial v d)
initialOverlap A d = cong (cong (initial B)) (I.initial-A d)
initialOverlap B d = cong (cong (initial A)) (I.initial-B d)
initialOverlap C d = cong (cong (initial D)) (I.initial-C d)
initialOverlap D d = cong (cong (initial C)) (I.initial-D d)
chainOverlap : (v : Vertex) (c : Chain v) → ChainOverlap v c
chainOverlap v (initial .v d) = initialOverlap v d
chainOverlap _ (extend c (_ , AB)) = cong (cong (λ q → extend q (A , BA))) (chainOverlap A c)
chainOverlap _ (extend c (_ , BC)) = cong (cong (λ q → extend q (D , AD))) (chainOverlap B c)
chainOverlap _ (extend c (_ , CA)) = cong (cong (λ q → extend q (B , DB))) (chainOverlap C c)
chainOverlap _ (extend c (_ , BA)) = cong (cong (λ q → extend q (B , AB))) (chainOverlap B c)
chainOverlap _ (extend c (_ , AD)) = cong (cong (λ q → extend q (C , BC))) (chainOverlap A c)
chainOverlap _ (extend c (_ , DB)) = cong (cong (λ q → extend q (A , CA))) (chainOverlap D c)
normalized-overlap : (c : Total) → square (R.move c) ≡ cong R.move (square c)
normalized-overlap (A , c) = cong (cong (λ q → B , q)) (chainOverlap A c)
normalized-overlap (B , c) = cong (cong (λ q → A , q)) (chainOverlap B c)
normalized-overlap (C , c) = cong (cong (λ q → D , q)) (chainOverlap C c)
normalized-overlap (D , c) = cong (cong (λ q → C , q)) (chainOverlap D c)

lift-composite : ∀ {ℓ ℓ'} {X : Type ℓ} {Y : Type ℓ'} (f : X → Y)
  {a b c : X} (p : a ≡ b) (q : b ≡ c) (r : a ≡ c)
  → p ∙ q ≡ r → cong f p ∙ cong f q ≡ cong f r
lift-composite f p q r h = sym (cong-∙ f p q) ∙ cong (cong f) h

ChainAgreement : (v : Vertex) → Chain v → Type₁
ChainAgreement A c = F.forward-back-chain (R.moveChain c) ∙ R.back-moveChain A c ≡ squareChain A c
ChainAgreement B c = F.forward-back-chain (R.moveChain c) ∙ R.back-moveChain B c ≡ squareChain B c
ChainAgreement C c = F.forward-back-chain (R.moveChain c) ∙ R.back-moveChain C c ≡ squareChain C c
ChainAgreement D c = F.forward-back-chain (R.moveChain c) ∙ R.back-moveChain D c ≡ squareChain D c
initialAgreement : (v : Vertex) (d : Resolve Seeds (pointQ v)) → ChainAgreement v (initial v d)
initialAgreement A d = sym (cong-∙ (initial A) _ _)
initialAgreement B d = sym (cong-∙ (initial B) _ _)
initialAgreement C d = sym (cong-∙ (initial C) _ _)
initialAgreement D d = sym (cong-∙ (initial D) _ _)
chainAgreement : (v : Vertex) (c : Chain v) → ChainAgreement v c
chainAgreement v (initial .v d) = initialAgreement v d
chainAgreement _ (extend c (_ , AB)) = lift-composite (λ q → extend q (B , AB))
  _ _ _ (chainAgreement A c)
chainAgreement _ (extend c (_ , BC)) = lift-composite (λ q → extend q (C , BC))
  _ _ _ (chainAgreement B c)
chainAgreement _ (extend c (_ , CA)) = lift-composite (λ q → extend q (A , CA))
  _ _ _ (chainAgreement C c)
chainAgreement _ (extend c (_ , BA)) = lift-composite (λ q → extend q (A , BA))
  _ _ _ (chainAgreement B c)
chainAgreement _ (extend c (_ , AD)) = lift-composite (λ q → extend q (D , AD))
  _ _ _ (chainAgreement A c)
chainAgreement _ (extend c (_ , DB)) = lift-composite (λ q → extend q (B , DB))
  _ _ _ (chainAgreement D c)
chosen-square-agrees : (c : Total) → F.forward-square c ≡ square c
chosen-square-agrees (A , c) = lift-composite (λ q → A , q) _ _ _ (chainAgreement A c)
chosen-square-agrees (B , c) = lift-composite (λ q → B , q) _ _ _ (chainAgreement B c)
chosen-square-agrees (C , c) = lift-composite (λ q → C , q) _ _ _ (chainAgreement C c)
chosen-square-agrees (D , c) = lift-composite (λ q → D , q) _ _ _ (chainAgreement D c)

abstract
  triple-exchange-overlap : F.TripleExchangeOverlap
  triple-exchange-overlap c = chosen-square-agrees (R.move c)
    ∙ normalized-overlap c ∙ sym (cong (cong R.move) (chosen-square-agrees c))
