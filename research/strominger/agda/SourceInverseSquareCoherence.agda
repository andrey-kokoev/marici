{-# OPTIONS --safe --cubical --guardedness #-}
module SourceInverseSquareCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence using (ua; ua-gluePath)
open import Cubical.Foundations.Transport using (transport⁻Transport)
open import Cubical.Foundations.HLevels using
  (isOfHLevel≡; isOfHLevelPathP'; isOfHLevelRespectEquiv; isSetΣ)
open import Cubical.Data.Sigma.Properties using (ΣPath≃PathΣ)
open import NativeExtensionFamilyAudit using
  (Vertex; A; B; C; D; Seeds; graphQ; pointQ; sigma; sigmaEquiv)
open import SourceIndexedExtensionFamilies using (vertex-is-set)
import ForwardSourceLiftComposition as F
import RetainedFeedbackCovariance as R
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- A local h-level result about pointed VERTEX carriers, not Code, Complete,
-- Chain or Resolve. Only this path space is proved to be a set.
PointedType : Type₁
PointedType = Σ[ X ∈ Type ] X
at : Vertex → PointedType
at v = Vertex , v
pointed-path-is-set : (x y : Vertex) → isSet (at x ≡ at y)
pointed-path-is-set x y = isOfHLevelRespectEquiv 2 ΣPath≃PathΣ
  (isSetΣ (isOfHLevel≡ 2 vertex-is-set vertex-is-set)
    (λ p → isProp→isSet (isOfHLevelPathP' 1 vertex-is-set x y)))

encode : PointedType → Complete
encode (X , x) = remember graphQ (pack (atom X) x)
pointed : (x y : Vertex) → sigma x ≡ y → at x ≡ at y
pointed x y p i = ua sigmaEquiv i , ua-gluePath sigmaEquiv p i
pointed-binding : (x y : Vertex) (p : sigma x ≡ y)
  → cong encode (pointed x y p) ≡ F.pointedPath x y p
pointed-binding x y p = refl

-- Reconstruct precisely the selected dependent square, not a replacement
-- chosen for convenience. Its projection to Complete is definitionally old.
inverseSquare : (x y : Vertex) (p : sigma x ≡ y) (q : sigma y ≡ x)
  → pointed x y p ≡ sym (pointed y x q)
inverseSquare x y p q j i = F.ua-inverse j i , valueSquare j i
  where
  valueSquare : PathP (λ j → PathP (λ i → F.ua-inverse j i) x y)
    (ua-gluePath sigmaEquiv p) (λ i → ua-gluePath sigmaEquiv q (~ i))
  valueSquare = isProp→PathP
    (λ j → isOfHLevelPathP' {A = λ i → F.ua-inverse j i} 1 vertex-is-set x y)
    (ua-gluePath sigmaEquiv p) (λ i → ua-gluePath sigmaEquiv q (~ i))
inverse-binding : (x y : Vertex) (p : sigma x ≡ y) (q : sigma y ≡ x)
  → cong (cong encode) (inverseSquare x y p q) ≡ F.pointed-inverse x y p q
inverse-binding x y p q = refl

-- The two actual chosen inversion squares are compatible under reversal.
-- This is a cube in the pointed-carrier presentation, projected back through
-- the exact retained graph/atom encoding. No native proof is truncated.
pointed-inverse-coherent : (x y : Vertex) (p : sigma x ≡ y) (q : sigma y ≡ x)
  → F.pointed-inverse y x q p ≡ cong sym (sym (F.pointed-inverse x y p q))
pointed-inverse-coherent x y p q = cong (cong (cong encode))
  (pointed-path-is-set y x (pointed y x q) (sym (pointed x y p))
    (inverseSquare y x q p) (cong sym (sym (inverseSquare x y p q))))

AB-square = pointed-inverse-coherent A B refl refl
BA-square = pointed-inverse-coherent B A refl refl
CD-square = pointed-inverse-coherent C D refl refl
DC-square = pointed-inverse-coherent D C refl refl

-- A candidate foundational transport bridge, stated for unrestricted fibers.
-- This signature is NOT a proof or a claim of impossibility.
TransportCancellationTriangle : (ℓ : Level) → Type (ℓ-suc ℓ)
TransportCancellationTriangle ℓ = {X Y : Type ℓ} (p : X ≡ Y) (x : X)
  → transport⁻Transport (sym p) (transport p x)
    ≡ cong (transport p) (transport⁻Transport p x)

-- Exact next boundaries on arbitrary native initial proofs. These are TYPES,
-- not inhabited claims: the transport/cancellation coherence is still needed.
InitialOverlapA InitialOverlapB InitialOverlapC InitialOverlapD : Type₁
InitialOverlapA = (d : Resolve Seeds (pointQ A))
  → F.forward-square-initial B (R.moveInitial A d)
    ≡ cong (R.moveInitial A) (F.forward-square-initial A d)
InitialOverlapB = (d : Resolve Seeds (pointQ B))
  → F.forward-square-initial A (R.moveInitial B d)
    ≡ cong (R.moveInitial B) (F.forward-square-initial B d)
InitialOverlapC = (d : Resolve Seeds (pointQ C))
  → F.forward-square-initial D (R.moveInitial C d)
    ≡ cong (R.moveInitial C) (F.forward-square-initial C d)
InitialOverlapD = (d : Resolve Seeds (pointQ D))
  → F.forward-square-initial C (R.moveInitial D d)
    ≡ cong (R.moveInitial D) (F.forward-square-initial D d)
