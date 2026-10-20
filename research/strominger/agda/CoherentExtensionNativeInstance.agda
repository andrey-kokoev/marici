{-# OPTIONS --safe --cubical --guardedness #-}
module CoherentExtensionNativeInstance where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Base using (_×_)
import CoherentDependentExtensions as General
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import RetainedPackageFeedback as Feedback
import RetainedFeedbackCovariance as Covariance
open import NativeExtensionFamilyAudit using (A; B; C; D)
open import SourceIndexedExtensionFamilies using (outEquiv)

-- The native signature determines the possible Rule shapes, but the source
-- policy deciding which shapes/parameters are admissible remains explicit.
module NativeAdmission (ℓ : Level)
  (S : Whole.Universe.Complete ℓ → Type (ℓ-suc ℓ))
  (X : Type (ℓ-suc ℓ)) (Tasks : X → Type (ℓ-suc ℓ))
  (Admit : (x : X) → Tasks x → Resolution.Generators.Rule ℓ → Type (ℓ-suc ℓ)) where
  open Resolution.Generators ℓ
  Premises : Rule → Type (ℓ-suc ℓ)
  Premises r = (i : Arity r) → Resolve S (input r i)
  Witness : (x : X) → Tasks x → Type (ℓ-suc ℓ)
  Witness x task = Σ Rule (λ r → Admit x task r × Premises r)
  Application : Type (ℓ-suc ℓ)
  Application = Σ X (λ x → Σ (Tasks x) (Witness x))
  compile : Application → Closure S
  compile (x , task , r , admission , premises) = output r , apply r premises
  -- Reify the WHOLE application, including policy evidence and the selected
  -- task, not only its native output. This does not discover that evidence.
  module Next = Whole.Universe (ℓ-suc ℓ)
  retain : Application → Next.Complete
  retain a = Next.pack (Next.atom (Application × Closure S)) (a , compile a)
  recover-application : (a : Application) → fst (Next.value (retain a)) ≡ a
  recover-application a = refl
  recover-native-history : (a : Application) → snd (Next.value (retain a)) ≡ compile a
  recover-native-history a = refl

-- Instantiate the general dependent-extension theorem with the actual
-- retained feedback payload and its source-admitted outgoing-edge questions.
FeedbackFamily : General.Family (ℓ-suc ℓ-zero)
General.Base FeedbackFamily = Feedback.Total
General.Witness FeedbackFamily c = Lift {j = ℓ-suc ℓ-zero} (Feedback.Questions c)

feedbackComparison : General.Comparison FeedbackFamily FeedbackFamily
General.baseEquiv feedbackComparison = Covariance.wholeEquiv
General.witnessEquiv feedbackComparison c = Lift≃Lift (outEquiv (fst c))

applicationEquiv : General.Total FeedbackFamily ≃ General.Total FeedbackFamily
applicationEquiv = General.liftComparison feedbackComparison
realize : General.Total FeedbackFamily → Feedback.Total
realize (c , lift e) = Feedback.step c e

-- The concrete feedback interpreter realizes the abstract transport square.
-- Four endpoint cases expose the already checked outEquiv computation rule;
-- the retained chain/history argument remains arbitrary in each case.
realization-square : (a : General.Total FeedbackFamily)
  → Covariance.move (realize a) ≡ realize (equivFun applicationEquiv a)
realization-square ((A , c) , lift e) = refl
realization-square ((B , c) , lift e) = refl
realization-square ((C , c) , lift e) = refl
realization-square ((D , c) , lift e) = refl

native-realization-square : (a : General.Total FeedbackFamily)
  → Feedback.closure (Covariance.move (realize a))
    ≡ Feedback.closure (realize (equivFun applicationEquiv a))
native-realization-square a = cong Feedback.closure (realization-square a)
