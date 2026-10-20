{-# OPTIONS --safe --cubical --guardedness #-}
module MixedSourceAdmissionClosure where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Relation.Nullary.Base using (¬_)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open import NativeExtensionFamilyAudit using
  (Vertex; A; B; C; D; AB; BC; CA; BA; AD; DB; pointQ; Seeds; root; sigma; sigma²)
open import SourceIndexedExtensionFamilies using (Out; moveOut)
open import RetainedFeedbackCovariance using
  (moveInitial; backInitial; back-moveInitial; move-backInitial)
import ExactSourceAdmission

open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- The two-schema fragment is DECLARED. Attachment is exact source incidence;
-- identity comparison is admitted by the actual native identity rule.
data Assembly : Vertex → Type₁ where
  initial : (v : Vertex) → Resolve Seeds (pointQ v) → Assembly v
  attach : {v : Vertex} (previous : Assembly v) (edge : Out v) → Assembly (fst edge)
  certify : {v : Vertex} → Assembly v → Assembly v

package : {v : Vertex} → Assembly v → Complete
package (initial v d) = pointQ v
package (attach {v} a e) = E-package (Out v)
  (λ _ → path-package (expression (package a)) (value (package a)) (value (package a)) refl) e
package (certify a) = identity-comparison (package a)

derivation : {v : Vertex} (a : Assembly v) → Resolve Seeds (package a)
derivation (initial v d) = d
derivation (attach {v} a e) = apply
  (E-rule (Out v)
    (λ _ → path-package (expression (package a)) (value (package a)) (value (package a)) refl) e)
  (λ _ → apply (reflexivity-rule (expression (package a)) (value (package a)))
    (λ _ → derivation a))
derivation (certify a) = apply (identity-rule (package a)) (λ _ → derivation a)

Total : Type₁
Total = Σ Vertex Assembly
Task : Total → Type
Task (v , a) = Out v ⊎ Unit
run : (a : Total) → Task a → Total
run (v , a) (inl e) = fst e , attach a e
run (v , a) (inr _) = v , certify a
closure : Total → Closure Seeds
closure (v , a) = package a , derivation a

peel : Closure Seeds → Closure Seeds
peel (_ , apply (E-rule I F i) ds) = F i , ds (lift i)
peel (_ , apply (reflexivity-rule Q x) ds) = pack Q x , ds (lift tt)
peel (_ , apply (identity-rule q) ds) = q , ds (lift tt)
peel c = c
attachment-retains : (v : Vertex) (a : Assembly v) (e : Out v)
  → peel (peel (closure (fst e , attach a e))) ≡ closure (v , a)
attachment-retains v a e = refl
comparison-retains : (v : Vertex) (a : Assembly v)
  → peel (closure (v , certify a)) ≡ closure (v , a)
comparison-retains v a = refl

-- No policy between constructors is required: the output remains an Assembly,
-- and every native premise below is the actual previous derivation.
run-twice : (a : Total) (t : Task a) → Task (run a t) → Total
run-twice a t u = run (run a t) u
reified : Total → Whole.Universe.Complete (ℓ-suc ℓ-zero)
reified a = Whole.Universe.pack
  (Whole.Universe.atom (Σ Total (λ _ → Closure Seeds))) (a , closure a)
recovery : (a : Total) → Whole.Universe.value (reified a) ≡ (a , closure a)
recovery a = refl

moveAssembly : {v : Vertex} → Assembly v → Assembly (sigma v)
moveAssembly (initial v d) = initial (sigma v) (moveInitial v d)
moveAssembly (attach a e) = attach (moveAssembly a) (moveOut e)
moveAssembly (certify a) = certify (moveAssembly a)
backAssembly : {v : Vertex} → Assembly v → Assembly (sigma v)
backAssembly (initial v d) = initial (sigma v) (backInitial v d)
backAssembly (attach a e) = attach (backAssembly a) (moveOut e)
backAssembly (certify a) = certify (backAssembly a)

back-move : (v : Vertex) (a : Assembly v)
  → PathP (λ i → Assembly (sigma² v i)) (backAssembly (moveAssembly a)) a
back-move v (initial .v d) i = initial (sigma² v i) (back-moveInitial v d i)
back-move _ (attach a (_ , AB)) i = attach (back-move A a i) (B , AB)
back-move _ (attach a (_ , BC)) i = attach (back-move B a i) (C , BC)
back-move _ (attach a (_ , CA)) i = attach (back-move C a i) (A , CA)
back-move _ (attach a (_ , BA)) i = attach (back-move B a i) (A , BA)
back-move _ (attach a (_ , AD)) i = attach (back-move A a i) (D , AD)
back-move _ (attach a (_ , DB)) i = attach (back-move D a i) (B , DB)
back-move v (certify a) i = certify (back-move v a i)
move-back : (v : Vertex) (a : Assembly v)
  → PathP (λ i → Assembly (sigma² v i)) (moveAssembly (backAssembly a)) a
move-back v (initial .v d) i = initial (sigma² v i) (move-backInitial v d i)
move-back _ (attach a (_ , AB)) i = attach (move-back A a i) (B , AB)
move-back _ (attach a (_ , BC)) i = attach (move-back B a i) (C , BC)
move-back _ (attach a (_ , CA)) i = attach (move-back C a i) (A , CA)
move-back _ (attach a (_ , BA)) i = attach (move-back B a i) (A , BA)
move-back _ (attach a (_ , AD)) i = attach (move-back A a i) (D , AD)
move-back _ (attach a (_ , DB)) i = attach (move-back D a i) (B , DB)
move-back v (certify a) i = certify (move-back v a i)

move back : Total → Total
move (v , a) = sigma v , moveAssembly a
back (v , a) = sigma v , backAssembly a
wholeEquiv : Total ≃ Total
wholeEquiv = isoToEquiv (iso move back
  (λ { (v , a) i → sigma² v i , move-back v a i })
  (λ { (v , a) i → sigma² v i , back-move v a i }))
moveTask : (a : Total) → Task a → Task (move a)
moveTask a (inl e) = inl (moveOut e)
moveTask a (inr t) = inr t
mixed-square : (a : Total) (t : Task a) → move (run a t) ≡ run (move a) (moveTask a t)
mixed-square a (inl e) = refl
mixed-square a (inr t) = refl
native-mixed-square : (a : Total) (t : Task a)
  → closure (move (run a t)) ≡ closure (run (move a) (moveTask a t))
native-mixed-square a t = cong closure (mixed-square a t)

-- Mixed closure does NOT make distinct construction orders equal.
base : Assembly A
base = initial A (root A)
attachmentThenComparison comparisonThenAttachment : Complete
attachmentThenComparison = package (certify (attach base (B , AB)))
comparisonThenAttachment = package (attach (certify base) (B , AB))
isE : Code → Bool
isE (E _ _) = true
isE _ = false
orders-distinct : ¬ (attachmentThenComparison ≡ comparisonThenAttachment)
orders-distinct p = false≢true (cong (λ q → isE (expression q)) p)
