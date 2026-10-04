{-# OPTIONS --safe --cubical --guardedness #-}
module TypedGeneratorCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_; isEquiv; equivFun; invEq; secEq; retEq; isPropIsEquiv)
open import Cubical.Foundations.Equiv.Properties using (isEquivCong)
open import Cubical.Foundations.HLevels using (isContr→isContrPath)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Unit.Base using (tt)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Empty.Base using (⊥)
open import TypedGeneratorLayers using (Layer1)
open import TypedGeneratorPresentation using (Reduction; Layer4; Stack4)
import TypedGeneratorPresentation as P
import GradedBoundaryCoherence as G

-- Reuse the existing globular tower. Here Cell means its boundary-indexed
-- filler type (Tower.Fill), NOT its total boundary-and-filler package.
Boundary : {ℓ : Level} → ℕ → Type ℓ → Type ℓ
Boundary n X = G.Tower.Boundary X n

Cell : {ℓ : Level} (n : ℕ) (X : Type ℓ) → Boundary n X → Type ℓ
Cell n X = G.Tower.Fill X n

-- Induced maps are the actual iterated action of f on paths.
mutual
  boundaryMap : {ℓA ℓB : Level} {A : Type ℓA} {B : Type ℓB}
    (n : ℕ) → (A → B) → Boundary n A → Boundary n B
  boundaryMap zero f β = lift tt
  boundaryMap (suc n) f (β , x , y) =
    boundaryMap n f β , cellMap n f β x , cellMap n f β y

  cellMap : {ℓA ℓB : Level} {A : Type ℓA} {B : Type ℓB}
    (n : ℕ) (f : A → B) (β : Boundary n A)
    → Cell n A β → Cell n B (boundaryMap n f β)
  cellMap zero f β x = f x
  cellMap (suc n) f (β , x , y) p = cong (cellMap n f β) p

-- Uniform preservation: induction on arbitrary n, not bounded enumeration.
map-is-equivalence : {ℓA ℓB : Level} {A : Type ℓA} {B : Type ℓB}
  (n : ℕ) (e : A ≃ B) (β : Boundary n A)
  → isEquiv (cellMap n (equivFun e) β)
map-is-equivalence zero e β = snd e
map-is-equivalence (suc n) e (β , x , y) =
  isEquivCong {x = x} {y = y}
    (cellMap n (equivFun e) β , map-is-equivalence n e β)

-- Uniform relative coherence: each next type is a path type in a
-- contractible preceding type. No set-truncation assumption is introduced.
cell-contractible : {ℓ : Level} {X : Type ℓ} (n : ℕ)
  → isContr X → (β : Boundary n X) → isContr (Cell n X β)
cell-contractible zero c β = c
cell-contractible (suc n) c (β , x , y) =
  isContr→isContrPath (cell-contractible n c β) x y

record AllDimensions {ℓA ℓB ℓF : Level} {A : Type ℓA} {B : Type ℓB}
  (q : Reduction {ℓF = ℓF} A B) : Type (ℓ-max ℓA ℓB) where
  module R = Reduction q
  field
    preservation : (n : ℕ) (β : Boundary n A)
      → isEquiv (cellMap n R.compact β)
    relative-coherence : (b : B) (n : ℕ) (β : Boundary n (R.Recovery b))
      → isContr (Cell n (R.Recovery b) β)

  equivalence : (n : ℕ) (β : Boundary n A)
    → Cell n A β ≃ Cell n B (boundaryMap n R.compact β)
  equivalence n β = cellMap n R.compact β , preservation n β

  recover-cell : (n : ℕ) (β : Boundary n A)
    → Cell n B (boundaryMap n R.compact β) → Cell n A β
  recover-cell n β = invEq (equivalence n β)

  source-cell-recovered : (n : ℕ) (β : Boundary n A) (x : Cell n A β)
    → recover-cell n β (cellMap n R.compact β x) ≡ x
  source-cell-recovered n β = retEq (equivalence n β)

  target-cell-recovered : (n : ℕ) (β : Boundary n A)
    (y : Cell n B (boundaryMap n R.compact β))
    → cellMap n R.compact β (recover-cell n β y) ≡ y
  target-cell-recovered n β = secEq (equivalence n β)

certify-reduction : {ℓA ℓB ℓF : Level} {A : Type ℓA} {B : Type ℓB}
  (q : Reduction {ℓF = ℓF} A B) → AllDimensions q
certify-reduction q = record
  { preservation = λ n β → map-is-equivalence n (Reduction.equivalence q) β
  ; relative-coherence = λ b n β → cell-contractible n (Reduction.recovery-certificate q b) β
  }

-- For a FIXED reduction, the theorem's complete certificate itself has no
-- independent proof choice. This does not identify different reductions.
certificate-unique : {ℓA ℓB ℓF : Level} {A : Type ℓA} {B : Type ℓB}
  (q : Reduction {ℓF = ℓF} A B) → isProp (AllDimensions q)
certificate-unique q a b i = record
  { preservation = λ n β → isPropIsEquiv (cellMap n (Reduction.compact q) β)
      (AllDimensions.preservation a n β) (AllDimensions.preservation b n β) i
  ; relative-coherence = λ v n β → isPropIsContr
      (AllDimensions.relative-coherence a v n β) (AllDimensions.relative-coherence b v n β) i
  }

certificate-contractible : {ℓA ℓB ℓF : Level} {A : Type ℓA} {B : Type ℓB}
  (q : Reduction {ℓF = ℓF} A B) → isContr (AllDimensions q)
certificate-contractible q = certify-reduction q , certificate-unique q (certify-reduction q)

-- Quantification over the actual Layers 1--4 stack and all typed endpoints.
Coherent4 : {ℓ ℓP ℓB ℓF : Level} (stack : Stack4 ℓ ℓP ℓB ℓF)
  → Type (ℓ-max ℓ (ℓ-max ℓP ℓB))
Coherent4 stack = (s t : Layer1.State (fst stack)) →
  AllDimensions (Layer4.reduction (snd (snd (snd stack))) s t)

certify : {ℓ ℓP ℓB ℓF : Level} (stack : Stack4 ℓ ℓP ℓB ℓF) → Coherent4 stack
certify stack s t = certify-reduction (Layer4.reduction (snd (snd (snd stack))) s t)

module Controls where
  module C = P.Controls

  -- Concrete application to the earlier two-stage reduction.
  two-stage : AllDimensions C.combined
  two-stage = certify-reduction C.combined

  canonical-stack : Coherent4 (P.extend4 C.Policy.layer4)
  canonical-stack = certify (P.extend4 C.Policy.layer4)

  separated : Boundary 1 C.Run
  separated = lift tt , C.idle , C.twice

  no-global-execution-filler : Cell 1 C.Run separated → ⊥
  no-global-execution-filler = C.runs-distinct

  -- A many-to-one score cannot support even the claimed dimension-one
  -- preservation: the shared score path would recover a forbidden history path.
  no-score-preservation : ((n : ℕ) (β : Boundary n C.Run)
    → isEquiv (cellMap n C.score β)) → ⊥
  no-score-preservation preserve = no-global-execution-filler
    (invEq (cellMap 1 C.score separated , preserve 1 separated) C.same-score)

  incompatible : Boundary 1 Bool
  incompatible = lift tt , false , true

  -- Existing higher distinctions survive as well: identity and Boolean flip
  -- are distinct paths between the same two universe terms.
  higher-separated : Boundary 2 (Type ℓ-zero)
  higher-separated = G.marked-type-boundary , G.plain-filler , G.twisted-filler

  no-global-higher-filler : Cell 2 (Type ℓ-zero) higher-separated → ⊥
  no-global-higher-filler = G.marked-fillers-distinct
