{-# OPTIONS --safe --cubical --guardedness #-}
module NativeExtensionFamilyAudit where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import Cubical.Data.Maybe.Base using (just)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Relation.Nullary.Base using (¬_)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import BoundaryGeneratedQuestions as Boundary

-- The actual twelve-schema signature supplies this rule-relative family.
-- A formed Rule already contains its parameters and evidence; these are not
-- discovered by forming this dependent sum.
module AllApplications (ℓ : Level)
  (S : Whole.Universe.Complete ℓ → Type (ℓ-suc ℓ)) where
  open Resolution.Generators ℓ
  Extensions : Type (ℓ-suc ℓ)
  Extensions = Σ Rule (λ r → (i : Arity r) → Resolve S (input r i))
  perform : Extensions → Closure S
  perform (r , premises) = output r , apply r premises
  nextQ : Extensions → Whole.Universe.Complete (ℓ-suc ℓ)
  nextQ (r , premises) = reify-history (apply r premises)
  recover-application : (x : Extensions)
    → Whole.Universe.value (nextQ x) ≡ perform x
  recover-application _ = refl

open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

data Vertex : Type where
  A B C D : Vertex

data Edge : Vertex → Vertex → Type where
  AB : Edge A B
  BC : Edge B C
  CA : Edge C A
  BA : Edge B A
  AD : Edge A D
  DB : Edge D B

-- The complete source graph is retained, rather than erased from the code.
graphQ : Complete
graphQ = pack (atom (List (Vertex × Vertex)))
  ((A , B) ∷ (B , C) ∷ (C , A) ∷ (B , A) ∷ (A , D) ∷ (D , B) ∷ [])
pointQ : Vertex → Complete
pointQ v = remember graphQ (pack (atom Vertex) v)
graph-retained : (v : Vertex) → recover (expression (pointQ v)) ≡ just graphQ
graph-retained v = refl

-- This source policy explicitly supplies every vertex-pointed package.
-- It does not derive this policy from an unpointed graph or from an empty seed.
data Seeds : Complete → Type₁ where
  source : (v : Vertex) → Seeds (pointQ v)
root : (v : Vertex) → Resolve Seeds (pointQ v)
root v = seed (source v)
module App = Boundary.Application Seeds

sigma : Vertex → Vertex
sigma A = B
sigma B = A
sigma C = D
sigma D = C
sigma² : (v : Vertex) → sigma (sigma v) ≡ v
sigma² A = refl
sigma² B = refl
sigma² C = refl
sigma² D = refl
sigmaEquiv : Vertex ≃ Vertex
sigmaEquiv = isoToEquiv (iso sigma sigma sigma² sigma²)

sigmaEdge : {s t : Vertex} → Edge s t → Edge (sigma s) (sigma t)
sigmaEdge AB = BA
sigmaEdge BC = AD
sigmaEdge CA = DB
sigmaEdge BA = AB
sigmaEdge AD = BC
sigmaEdge DB = CA

-- A different equivalence carries A to B but breaks the retained incidence.
tau : Vertex → Vertex
tau A = B
tau B = A
tau C = C
tau D = D
tau² : (v : Vertex) → tau (tau v) ≡ v
tau² A = refl
tau² B = refl
tau² C = refl
tau² D = refl
tauEquiv : Vertex ≃ Vertex
tauEquiv = isoToEquiv (iso tau tau tau² tau²)

sigmaFiller tauFiller : Boundary.Filler (pointQ A) (pointQ B)
sigmaFiller = sigmaEquiv , refl
tauFiller = tauEquiv , refl

-- Both are ACTUAL applications of the existing unrestricted comparison rule.
sigma-derived : Resolve Seeds
  (comparison-package (pointQ A) (pointQ B) sigmaEquiv refl)
sigma-derived = App.perform sigmaFiller (root A) (root B)
tau-derived : Resolve Seeds
  (comparison-package (pointQ A) (pointQ B) tauEquiv refl)
tau-derived = App.perform tauFiller (root A) (root B)

sigma-nextQ : Whole.Universe.Complete (ℓ-suc ℓ-zero)
sigma-nextQ = reify-history sigma-derived
sigma-history-recovered : snd (Whole.Universe.value sigma-nextQ) ≡ sigma-derived
sigma-history-recovered = refl

PreservesEdges : (Vertex ≃ Vertex) → Type
PreservesEdges e = (s t : Vertex) → Edge s t → Edge (equivFun e s) (equivFun e t)
SeedFiller : (a b : Vertex) → Type
SeedFiller a b = Σ (Boundary.Filler (pointQ a) (pointQ b))
  (λ f → PreservesEdges (fst f) × PreservesEdges (invEquiv (fst f)))

sigma-structured : SeedFiller A B
sigma-structured = sigmaFiller , (λ _ _ e → sigmaEdge e) , (λ _ _ e → sigmaEdge e)

-- A source-specific checked adapter can consume the stronger fiber without
-- changing the generic rule. Its complete record retains the extra witnesses,
-- not just the resulting native comparison derivation.
SourceApplication : Type₁
SourceApplication = Σ Vertex (λ a → Σ Vertex (λ b → Σ (SeedFiller a b)
  (λ f → Resolve Seeds (output (App.rule {a = pointQ a} {b = pointQ b} (fst f))))))
compile-structured : (a b : Vertex) → SeedFiller a b
  → Resolve Seeds (pointQ a) → Resolve Seeds (pointQ b) → SourceApplication
compile-structured a b f da db = a , b , f , App.perform (fst f) da db
retain-structured : SourceApplication → Whole.Universe.Complete (ℓ-suc ℓ-zero)
retain-structured x = Whole.Universe.pack (Whole.Universe.atom SourceApplication) x
structured-record-recovered : (x : SourceApplication)
  → Whole.Universe.value (retain-structured x) ≡ x
structured-record-recovered x = refl
structured-sigma-record : SourceApplication
structured-sigma-record = compile-structured A B sigma-structured (root A) (root B)

no-AC : ¬ (Edge A C)
no-AC ()
tau-breaks-incidence : ¬ (PreservesEdges tauEquiv)
tau-breaks-incidence preserves = no-AC (preserves B C BC)

-- Endpoint indexing is essential: sigma is not a self-filler at marked A.
isB : Vertex → Bool
isB A = false
isB B = true
isB C = false
isB D = false
sigma-not-pointed-self : ¬ (equivFun sigmaEquiv (value (pointQ A)) ≡ value (pointQ A))
sigma-not-pointed-self p = false≢true (sym (cong isB p))

isD : Vertex → Bool
isD D = true
isD _ = false
native-fillers-distinct : ¬ (sigmaFiller ≡ tauFiller)
native-fillers-distinct p = false≢true
  (sym (cong (λ f → isD (equivFun (fst f) C)) p))
