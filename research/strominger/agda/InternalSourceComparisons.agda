{-# OPTIONS --safe --cubical --guardedness #-}
module InternalSourceComparisons where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Transport using (substEquiv)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv)
open import Cubical.Data.Unit.Base using (tt)
open import Cubical.Data.Bool.Base using (true; false)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open import NativeExtensionFamilyAudit using
  (Vertex; Edge; A; B; C; D; pointQ; Seeds; root; sigma; sigmaEquiv; sigmaEdge)
open import SourceIndexedExtensionFamilies using (Out; moveOut; outEquiv)
open import ProofRelevantCoherenceClosure using (pathLift)

open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

data Mode : Type where
  stay exchange : Mode
act : Mode → Vertex → Vertex
act stay v = v
act exchange v = sigma v
edgeAction : (m : Mode) {s t : Vertex} → Edge s t → Edge (act m s) (act m t)
edgeAction stay e = e
edgeAction exchange e = sigmaEdge e
edgeMap : (m : Mode) {v : Vertex} → Out v → Out (act m v)
edgeMap m (w , e) = act m w , edgeAction m e
edgeEquiv : (m : Mode) (v : Vertex) → Out v ≃ Out (act m v)
edgeEquiv stay v = idEquiv _
edgeEquiv exchange v = outEquiv v
edge-computes : (m : Mode) (v : Vertex) (e : Out v)
  → equivFun (edgeEquiv m v) e ≡ edgeMap m e
edge-computes stay v e = refl
edge-computes exchange A e = refl
edge-computes exchange B e = refl
edge-computes exchange C e = refl
edge-computes exchange D e = refl
edge-target : (m : Mode) (v : Vertex) (e : Out v)
  → act m (fst e) ≡ fst (equivFun (edgeEquiv m v) e)
edge-target stay v e = refl
edge-target exchange A e = refl
edge-target exchange B e = refl
edge-target exchange C e = refl
edge-target exchange D e = refl

-- The chosen continuation port of comparison is its TARGET side. This is an
-- explicit interface convention, not an inference from existence of an equiv.
-- Every old reader, operand, native derivation and compatibility witness stays
-- in this inductive-recursive retained package.
mutual
  data Body : Vertex → Type₁ where
    prepared : (v : Vertex) (q : Complete) → Resolve Seeds q
      → (read : El (expression q) → Vertex) → read (value q) ≡ v → Body v
    attach : {v : Vertex} → Body v → (e : Out v) → Body (fst e)
    compare : (m : Mode) {v : Vertex} (a : Body v) (b : Body (act m v))
      (e : El (expression (package a)) ≃ El (expression (package b)))
      → equivFun e (value (package a)) ≡ value (package b)
      → ((x : El (expression (package a))) → act m (reader a x) ≡ reader b (equivFun e x))
      → Body (act m v)

  package : {v : Vertex} → Body v → Complete
  package (prepared v q d read p) = q
  package (attach {v} a e) = E-package (Out v)
    (λ _ → path-package (expression (package a)) (value (package a)) (value (package a)) refl) e
  package (compare m a b e p h) = comparison-package (package a) (package b) e p

  reader : {v : Vertex} (a : Body v) → El (expression (package a)) → Vertex
  reader (prepared v q d read p) = read
  reader (attach a e) (edge , loop) = fst edge
  reader (compare m a b e p h) (x , y , witness) = reader b y

aligned : {v : Vertex} (a : Body v) → reader a (value (package a)) ≡ v
aligned (prepared v q d read p) = p
aligned (attach a e) = refl
aligned (compare m a b e p h) = aligned b

derivation : {v : Vertex} (a : Body v) → Resolve Seeds (package a)
derivation (prepared v q d read p) = d
derivation (attach {v} a e) = apply
  (E-rule (Out v)
    (λ _ → path-package (expression (package a)) (value (package a)) (value (package a)) refl) e)
  (λ _ → apply (reflexivity-rule (expression (package a)) (value (package a))) (λ _ → derivation a))
derivation (compare m a b e p h) = apply (compare-rule (package a) (package b) e p)
  (λ { (lift true) → derivation a ; (lift false) → derivation b })

seedBody : (v : Vertex) → Body v
seedBody v = prepared v (pointQ v) (root v) (λ x → x) refl
nonidentity : (v : Vertex) → Body (sigma v)
nonidentity v = compare exchange (seedBody v) (seedBody (sigma v)) sigmaEquiv refl (λ x → refl)

-- Source compatibility holds at every value of the comparison carrier, not
-- only its selected value. Both sides remain readable.
comparison-reading : (m : Mode) {v : Vertex} (a : Body v) (b : Body (act m v))
  (e : El (expression (package a)) ≃ El (expression (package b)))
  (p : equivFun e (value (package a)) ≡ value (package b))
  (h : (x : El (expression (package a))) → act m (reader a x) ≡ reader b (equivFun e x))
  (z : El (expression (package (compare m a b e p h))))
  → act m (reader a (fst z)) ≡ reader (compare m a b e p h) z
comparison-reading m a b e p h (x , y , w) = h x ∙ cong (reader b) w

-- Pointed equivalences induce equivalences of actual loop witnesses.
loopTransport-refl : {X : Type} {x y : X} (p : x ≡ y)
  → subst (λ z → z ≡ z) p refl ≡ refl
loopTransport-refl {X} {x} = J
  (λ y p → subst (λ z → z ≡ z) p refl ≡ refl)
  (substRefl {B = λ z → z ≡ z} {x = x} refl)
loopEquiv : {X Y : Type} (e : X ≃ Y) {x : X} {y : Y}
  → equivFun e x ≡ y → (x ≡ x) ≃ (y ≡ y)
loopEquiv e p = compEquiv (pathLift e) (substEquiv (λ z → z ≡ z) p)
loop-refl : {X Y : Type} (e : X ≃ Y) {x : X} {y : Y}
  (p : equivFun e x ≡ y) → equivFun (loopEquiv e p) refl ≡ refl
loop-refl e p = loopTransport-refl p
