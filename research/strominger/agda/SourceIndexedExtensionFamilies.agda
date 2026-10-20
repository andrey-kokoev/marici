{-# OPTIONS --safe --cubical --guardedness #-}
module SourceIndexedExtensionFamilies where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels using (isSetRetract; isSet×)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true; isSetBool)
open import Cubical.Relation.Nullary.Base using (¬_)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open import NativeExtensionFamilyAudit using
  (Vertex; A; B; C; D; Edge; AB; BC; CA; BA; AD; DB;
   sigma; sigma²; sigmaEquiv; sigmaEdge; pointQ; Seeds; root; isB)

-- This family is extracted from the supplied directed incidence relation.
Out : Vertex → Type
Out v = Σ Vertex (Edge v)
moveOut : {v : Vertex} → Out v → Out (sigma v)
moveOut (w , e) = sigma w , sigmaEdge e
out-return : (v : Vertex) (o : Out v)
  → PathP (λ i → Out (sigma² v i)) (moveOut (moveOut o)) o
out-return _ (_ , AB) = refl
out-return _ (_ , AD) = refl
out-return _ (_ , BC) = refl
out-return _ (_ , BA) = refl
out-return _ (_ , CA) = refl
out-return _ (_ , DB) = refl
outIso : (v : Vertex) → Iso (Out v) (Out (sigma v))
outIso A = iso moveOut moveOut (out-return B) (out-return A)
outIso B = iso moveOut moveOut (out-return A) (out-return B)
outIso C = iso moveOut moveOut (out-return D) (out-return C)
outIso D = iso moveOut moveOut (out-return C) (out-return D)
outEquiv : (v : Vertex) → Out v ≃ Out (sigma v)
outEquiv v = isoToEquiv (outIso v)

-- Universal dependent-pair description: to map into an extension is exactly
-- to give an old record and an admissible outgoing witness for that record.
-- The endpoint-attachment operation is a DECLARED task, not a physical law.
module Extension {ℓ : Level} (X : Type ℓ) (endpoint : X → Vertex) where
  Next : Type ℓ
  Next = Σ X (λ x → Out (endpoint x))
  projection : Next → X
  projection = fst
  universal : {k : Level} (T : Type k)
    → Iso (T → Next) (Σ (T → X) (λ f → (t : T) → Out (endpoint (f t))))
  Iso.fun (universal T) f = (λ t → fst (f t)) , (λ t → snd (f t))
  Iso.inv (universal T) (f , witnesses) t = f t , witnesses t
  Iso.rightInv (universal T) _ = refl
  Iso.leftInv (universal T) _ = refl

-- Depth is structural. Every existing arrow and incidence witness is retained.
PathsFrom : ℕ → Vertex → Type
PathsFrom zero v = Unit
PathsFrom (suc n) v = Σ (Out v) (λ o → PathsFrom n (fst o))
Paths : ℕ → Type
Paths n = Σ Vertex (PathsFrom n)
endFrom : (n : ℕ) (v : Vertex) → PathsFrom n v → Vertex
endFrom zero v _ = v
endFrom (suc n) v (o , tail) = endFrom n (fst o) tail
endpoint : (n : ℕ) → Paths n → Vertex
endpoint n (v , p) = endFrom n v p

-- Actual all-finite-depth transport of the entire incidence-typed index,
-- not merely a permutation of observed endpoints.
pathEquivFrom : (n : ℕ) (v : Vertex) → PathsFrom n v ≃ PathsFrom n (sigma v)
pathEquivFrom zero v = idEquiv Unit
pathEquivFrom (suc n) A = Σ-cong-equiv (outEquiv A) (λ o → pathEquivFrom n (fst o))
pathEquivFrom (suc n) B = Σ-cong-equiv (outEquiv B) (λ o → pathEquivFrom n (fst o))
pathEquivFrom (suc n) C = Σ-cong-equiv (outEquiv C) (λ o → pathEquivFrom n (fst o))
pathEquivFrom (suc n) D = Σ-cong-equiv (outEquiv D) (λ o → pathEquivFrom n (fst o))
pathEquiv : (n : ℕ) → Paths n ≃ Paths n
pathEquiv n = Σ-cong-equiv sigmaEquiv (pathEquivFrom n)
end-natural : (n : ℕ) (v : Vertex) (p : PathsFrom n v)
  → endFrom n (sigma v) (equivFun (pathEquivFrom n v) p) ≡ sigma (endFrom n v p)
end-natural zero v p = refl
end-natural (suc n) A (o , tail) = end-natural n (fst o) tail
end-natural (suc n) B (o , tail) = end-natural n (fst o) tail
end-natural (suc n) C (o , tail) = end-natural n (fst o) tail
end-natural (suc n) D (o , tail) = end-natural n (fst o) tail

open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- Branch inputs are actual native reflexivity derivations of the retained
-- endpoint packages. No new arbitrary atomic seed is inserted for an edge.
branch : (n : ℕ) → Paths n → Complete
branch n p = path-package (expression (pointQ (endpoint n p)))
  (endpoint n p) (endpoint n p) refl
branch-derived : (n : ℕ) (p : Paths n) → Resolve Seeds (branch n p)
branch-derived n p = apply
  (reflexivity-rule (expression (pointQ (endpoint n p))) (endpoint n p))
  (λ _ → root (endpoint n p))

selected : (n : ℕ) → Paths n → Complete
selected n p = E-package (Paths n) (branch n) p
selected-derived : (n : ℕ) (p : Paths n) → Resolve Seeds (selected n p)
selected-derived n p = apply (E-rule (Paths n) (branch n) p)
  (λ { (lift q) → branch-derived n q })

-- The full family requires no selected path. Its entire indexed input family
-- survives in Code; its interpreted value is a family of reflexive witnesses.
all-family : ℕ → Complete
all-family n = Pi-package (Paths n) (branch n)
all-family-derived : (n : ℕ) → Resolve Seeds (all-family n)
all-family-derived n = apply (Pi-rule (Paths n) (branch n))
  (λ { (lift p) → branch-derived n p })

nextQ : ℕ → Whole.Universe.Complete (ℓ-suc ℓ-zero)
nextQ n = reify-history (all-family-derived n)
nextQ-recovers : (n : ℕ)
  → snd (Whole.Universe.value (nextQ n)) ≡ all-family-derived n
nextQ-recovers n = refl

-- Nontrivial interpreted configurations already occur at structural depth 1.
-- This is not just a larger provenance code around the same interpreted value.
branchCode : ℕ → Code
branchCode n = E (Paths n) (λ p → retained (branch n p))
-- No extra multiplicity is hidden in the endpoint reflexivity witnesses.
encode : Vertex → Bool × Bool
encode A = false , false
encode B = true , false
encode C = false , true
encode D = true , true
decode : Bool × Bool → Vertex
decode (false , false) = A
decode (true , false) = B
decode (false , true) = C
decode (true , true) = D
decode-encode : (v : Vertex) → decode (encode v) ≡ v
decode-encode A = refl
decode-encode B = refl
decode-encode C = refl
decode-encode D = refl
vertex-is-set : isSet Vertex
vertex-is-set = isSetRetract encode decode decode-encode (isSet× isSetBool isSetBool)
branchIso : (n : ℕ) → Iso (El (branchCode n)) (Paths n)
Iso.fun (branchIso n) = fst
Iso.inv (branchIso n) p = p , refl
Iso.rightInv (branchIso n) p = refl
Iso.leftInv (branchIso n) (p , q) i = p , vertex-is-set (endpoint n p) (endpoint n p) refl q i
branchEquiv : (n : ℕ) → El (branchCode n) ≃ Paths n
branchEquiv n = isoToEquiv (branchIso n)
branchTransport : (n : ℕ) → El (branchCode n) ≃ El (branchCode n)
branchTransport n = compEquiv (branchEquiv n)
  (compEquiv (pathEquiv n) (invEquiv (branchEquiv n)))

-- The source-derived index comparison also supplies an actual native
-- comparison between selected full E packages, at every finite depth.
native-transport : (n : ℕ) (p : Paths n) → Resolve Seeds
  (comparison-package (selected n p) (selected n (equivFun (pathEquiv n) p))
    (branchTransport n) refl)
native-transport n p = apply
  (compare-rule (selected n p) (selected n (equivFun (pathEquiv n) p))
    (branchTransport n) refl)
  (λ { (lift true) → selected-derived n p
     ; (lift false) → selected-derived n (equivFun (pathEquiv n) p) })

leftPath rightPath : Paths (suc zero)
leftPath = A , (B , AB) , tt
rightPath = A , (D , AD) , tt
leftValue rightValue : El (branchCode (suc zero))
leftValue = leftPath , refl
rightValue = rightPath , refl
branch-values-distinct : ¬ (leftValue ≡ rightValue)
branch-values-distinct p = false≢true
  (sym (cong (λ x → isB (endpoint (suc zero) (fst x))) p))
branch-carrier-not-prop : ¬ (isProp (El (branchCode (suc zero))))
branch-carrier-not-prop prop = branch-values-distinct (prop leftValue rightValue)
