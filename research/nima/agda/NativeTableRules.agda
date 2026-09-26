{-# OPTIONS --safe --cubical --guardedness #-}
module NativeTableRules where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv; Σ-cong-equiv-snd)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
import IndexedConstructorTables as Tables
import ProofRelevantCoherenceClosure as Witness
import WholePackageSigmaPi as Legacy
import WholePackageResolution as Resolution

module Native (ℓ : Level) where
  module G = Tables.Core ℓ
  Ty : G.Package → Type ℓ
  Ty a = G.Value (fst a)
  expression : (a : G.Package) → G.Node (Ty a)
  expression a = snd (fst a)
  value : (a : G.Package) → Ty a
  value = snd
  pack : {A : Type ℓ} → G.Node A → A → G.Package
  pack {A} g v = (A , g) , v
  retained : (a : G.Package) → G.Node (Ty a)
  retained a = G.retain-node (expression a) (value a) (expression a)
  E-package : (I : Type ℓ) → (I → G.Package) → I → G.Package
  E-package I F i = pack (G.E-node I (λ j → retained (F j))) (i , value (F i))
  Pi-package : (I : Type ℓ) → (I → G.Package) → G.Package
  Pi-package I F = pack (G.P-node I (λ i → retained (F i))) (λ i → value (F i))
  remember : G.Package → G.Package → G.Package
  remember a b = pack (G.retain-node (expression a) (value a) (expression b)) (value b)
  comparison-package : (a b : G.Package) (e : Ty a ≃ Ty b)
    → equivFun e (value a) ≡ value b → G.Package
  comparison-package a b e p = pack (G.comparison-node (retained a) (retained b) e) (value a , value b , p)
  path-package : (g : G.Graph) (x y : G.Value g) → x ≡ y → G.Package
  path-package (A , g) x y p = pack (G.paths-node g x y) p
  identity-comparison : G.Package → G.Package
  identity-comparison a = comparison-package a a (idEquiv _) refl
  inverse-comparison : (a b : G.Package) (e : Ty a ≃ Ty b)
    → equivFun e (value a) ≡ value b → G.Package
  inverse-comparison a b e p = remember (comparison-package a b e p)
    (comparison-package b a (invEquiv e) (sym (cong (invEq e) p) ∙ retEq e (value a)))
  compose-comparisons : (a b c : G.Package) (e : Ty a ≃ Ty b) (f : Ty b ≃ Ty c)
    → equivFun e (value a) ≡ value b → equivFun f (value b) ≡ value c → G.Package
  compose-comparisons a b c e f p q = remember (comparison-package a b e p)
    (remember (comparison-package b c f q)
      (comparison-package a c (compEquiv e f) (cong (equivFun f) p ∙ q)))
  higher-package : (g : G.Graph) (x y : G.Value g) (p q : x ≡ y) → p ≡ q → G.Package
  higher-package (A , g) x y p q alpha = pack (G.paths-node (G.paths-node g x y) p q) alpha
  lift-paths : (c d : G.Graph) (e : G.Value c ≃ G.Value d) (x y : G.Value c) → G.Package
  lift-paths (A , c) (B , d) e x y = pack
    (G.retain-node (G.equivalences-node c d) e
      (G.equivalences-node (G.paths-node c x y) (G.paths-node d (equivFun e x) (equivFun e y))))
    (Witness.pathLift e)
  module Congruence (I : Type ℓ) (F H : I → G.Package)
    (e : (i : I) → Ty (F i) ≃ Ty (H i))
    (p : (i : I) → equivFun (e i) (value (F i)) ≡ value (H i)) where
    all-comparisons : G.Package
    all-comparisons = Pi-package I (λ i → comparison-package (F i) (H i) (e i) (p i))
    E-comparison : I → G.Package
    E-comparison i = remember all-comparisons
      (comparison-package (E-package I F i) (E-package I H i) (Σ-cong-equiv-snd e) (λ j → i , p i j))
    Pi-comparison : G.Package
    Pi-comparison = remember all-comparisons
      (comparison-package (Pi-package I F) (Pi-package I H) (equivΠCod e) (funExt p))
  module Distribution (I : Type ℓ) (J : I → Type ℓ) (F : (i : I) → J i → G.Package) where
    left right : G.Graph
    left = G.P-table I (λ i → G.E-table (J i) (λ j → Ty (F i j) , retained (F i j)))
    right = G.E-table ((i : I) → J i) (λ f → G.P-table I (λ i → Ty (F i (f i)) , retained (F i (f i))))
    law : Iso (G.Value left) (G.Value right)
    Iso.fun law v = (λ i → fst (v i)) , (λ i → snd (v i))
    Iso.inv law (f , w) i = f i , w i
    Iso.rightInv law _ = refl
    Iso.leftInv law _ = refl
    generator : G.Value left → G.Package
    generator v = comparison-package (left , v) (right , Iso.fun law v) (isoToEquiv law) refl

  -- A declaration is a tag plus typed native parameters. The schemas below
  -- store no old Code, Complete, Rule or derivation.
  data Kind : Type where
    E-kind P-kind compare-kind identity-kind inverse-kind compose-kind : Kind
    higher-kind reflexivity-kind path-lift-kind distribution-kind : Kind
    E-congruence-kind P-congruence-kind : Kind
  Filler : G.Package → G.Package → Type ℓ
  Filler a b = Σ (Ty a ≃ Ty b) (λ e → equivFun e (value a) ≡ value b)
  compose-filler : {a b c : G.Package} → Filler a b → Filler b c → Filler a c
  compose-filler (e , p) (f , q) = compEquiv e f , cong (equivFun f) p ∙ q
  ComparisonParameters : Type (ℓ-suc ℓ)
  ComparisonParameters = Σ G.Package (λ a → Σ G.Package (λ b → Filler a b))
  CongruenceParameters : (I : Type ℓ) (F H : I → G.Package) → Type ℓ
  CongruenceParameters I F H = Σ ((i : I) → Ty (F i) ≃ Ty (H i))
    (λ e → (i : I) → equivFun (e i) (value (F i)) ≡ value (H i))
  Parameters : Kind → Type (ℓ-suc ℓ)
  Parameters E-kind = Σ (Type ℓ) (λ I → Σ (I → G.Package) (λ _ → I))
  Parameters P-kind = Σ (Type ℓ) (λ I → I → G.Package)
  Parameters compare-kind = ComparisonParameters
  Parameters identity-kind = G.Package
  Parameters inverse-kind = ComparisonParameters
  Parameters compose-kind = Σ G.Package (λ a → Σ G.Package (λ b → Σ G.Package (λ c →
    Σ (Ty a ≃ Ty b) (λ e → Σ (Ty b ≃ Ty c) (λ f →
      Σ (equivFun e (value a) ≡ value b) (λ _ → equivFun f (value b) ≡ value c))))))
  Parameters higher-kind = Σ G.Graph (λ c → Σ (G.Value c) (λ x → Σ (G.Value c) (λ y →
    Σ (x ≡ y) (λ p → Σ (x ≡ y) (λ q → p ≡ q)))))
  Parameters reflexivity-kind = G.Package
  Parameters path-lift-kind = Σ G.Graph (λ c → Σ G.Graph (λ d →
    Σ (G.Value c ≃ G.Value d) (λ _ → Σ (G.Value c) (λ _ → G.Value c))))
  Parameters distribution-kind = Σ (Type ℓ) (λ I → Σ (I → Type ℓ) (λ J →
    Σ ((i : I) → J i → G.Package) (λ F → G.Value (Distribution.left I J F))))
  Parameters E-congruence-kind = Σ (Type ℓ) (λ I → Σ (I → G.Package) (λ F → Σ (I → G.Package) (λ H →
    Σ (CongruenceParameters I F H) (λ _ → I))))
  Parameters P-congruence-kind = Σ (Type ℓ) (λ I → Σ (I → G.Package) (λ F → Σ (I → G.Package) (λ H →
    CongruenceParameters I F H)))
  Rule : Type (ℓ-suc ℓ)
  Rule = Σ Kind Parameters
  Arity : Rule → Type (ℓ-suc ℓ)
  Arity (E-kind , I , F , i) = Lift I
  Arity (P-kind , I , F) = Lift I
  Arity (compare-kind , _) = Lift {j = ℓ-suc ℓ} Bool
  Arity (identity-kind , _) = Lift {j = ℓ-suc ℓ} Unit
  Arity (inverse-kind , _) = Lift {j = ℓ-suc ℓ} Unit
  Arity (compose-kind , _) = Lift {j = ℓ-suc ℓ} Bool
  Arity (higher-kind , _) = Lift {j = ℓ-suc ℓ} Bool
  Arity (reflexivity-kind , _) = Lift {j = ℓ-suc ℓ} Unit
  Arity (path-lift-kind , _) = Lift {j = ℓ-suc ℓ} Unit
  Arity (distribution-kind , I , J , F , v) = Lift {j = ℓ-suc ℓ} (Σ I J) ⊎ Lift {j = ℓ-suc ℓ} Unit
  Arity (E-congruence-kind , I , _) = Lift I
  Arity (P-congruence-kind , I , _) = Lift I
  input : (r : Rule) → Arity r → G.Package
  input (E-kind , I , F , i) (lift j) = F j
  input (P-kind , I , F) (lift i) = F i
  input (compare-kind , a , b , e , p) (lift true) = a
  input (compare-kind , a , b , e , p) (lift false) = b
  input (identity-kind , a) _ = a
  input (inverse-kind , a , b , e , p) _ = comparison-package a b e p
  input (compose-kind , a , b , c , e , f , p , q) (lift true) = comparison-package a b e p
  input (compose-kind , a , b , c , e , f , p , q) (lift false) = comparison-package b c f q
  input (higher-kind , c , x , y , p , q , alpha) (lift true) = path-package c x y p
  input (higher-kind , c , x , y , p , q , alpha) (lift false) = path-package c x y q
  input (reflexivity-kind , a) _ = a
  input (path-lift-kind , c , d , e , x , y) _ = pack (G.equivalences-node (snd c) (snd d)) e
  input (distribution-kind , I , J , F , v) (inl (lift (i , j))) = F i j
  input (distribution-kind , I , J , F , v) (inr _) = Distribution.left I J F , v
  input (E-congruence-kind , I , F , H , (e , p) , i) (lift j) = comparison-package (F j) (H j) (e j) (p j)
  input (P-congruence-kind , I , F , H , e , p) (lift i) = comparison-package (F i) (H i) (e i) (p i)
  output : Rule → G.Package
  output (E-kind , I , F , i) = E-package I F i
  output (P-kind , I , F) = Pi-package I F
  output (compare-kind , a , b , e , p) = comparison-package a b e p
  output (identity-kind , a) = identity-comparison a
  output (inverse-kind , a , b , e , p) = inverse-comparison a b e p
  output (compose-kind , a , b , c , e , f , p , q) = compose-comparisons a b c e f p q
  output (higher-kind , c , x , y , p , q , alpha) = higher-package c x y p q alpha
  output (reflexivity-kind , c , x) = path-package c x x refl
  output (path-lift-kind , c , d , e , x , y) = lift-paths c d e x y
  output (distribution-kind , I , J , F , v) = Distribution.generator I J F v
  output (E-congruence-kind , I , F , H , (e , p) , i) = Congruence.E-comparison I F H e p i
  output (P-congruence-kind , I , F , H , e , p) = Congruence.Pi-comparison I F H e p

  -- Legacy comparison starts here. The operations above do not decode back
  -- to the old system to perform their work.
  module O = Legacy.Universe ℓ
  module R = Resolution.Generators ℓ
  OldTy : O.Complete → Type ℓ
  OldTy a = O.El (O.expression a)
  OldFiller : O.Complete → O.Complete → Type ℓ
  OldFiller a b = Σ (OldTy a ≃ OldTy b) (λ e → equivFun e (O.value a) ≡ O.value b)
  OldComparison : Type (ℓ-suc ℓ)
  OldComparison = Σ O.Complete (λ a → Σ O.Complete (λ b → OldFiller a b))
  OldCongruence : (I : Type ℓ) (F H : I → O.Complete) → Type ℓ
  OldCongruence I F H = Σ ((i : I) → OldTy (F i) ≃ OldTy (H i))
    (λ e → (i : I) → equivFun (e i) (O.value (F i)) ≡ O.value (H i))
  OldParameters : Kind → Type (ℓ-suc ℓ)
  OldParameters E-kind = Σ (Type ℓ) (λ I → Σ (I → O.Complete) (λ _ → I))
  OldParameters P-kind = Σ (Type ℓ) (λ I → I → O.Complete)
  OldParameters compare-kind = OldComparison
  OldParameters identity-kind = O.Complete
  OldParameters inverse-kind = OldComparison
  OldParameters compose-kind = Σ O.Complete (λ a → Σ O.Complete (λ b → Σ O.Complete (λ c →
    Σ (OldTy a ≃ OldTy b) (λ e → Σ (OldTy b ≃ OldTy c) (λ f →
      Σ (equivFun e (O.value a) ≡ O.value b) (λ _ → equivFun f (O.value b) ≡ O.value c))))))
  OldParameters higher-kind = Σ O.Code (λ c → Σ (O.El c) (λ x → Σ (O.El c) (λ y →
    Σ (x ≡ y) (λ p → Σ (x ≡ y) (λ q → p ≡ q)))))
  OldParameters reflexivity-kind = Σ O.Code O.El
  OldParameters path-lift-kind = Σ O.Code (λ c → Σ O.Code (λ d →
    Σ (O.El c ≃ O.El d) (λ _ → Σ (O.El c) (λ _ → O.El c))))
  OldParameters distribution-kind = Σ (Type ℓ) (λ I → Σ (I → Type ℓ) (λ J →
    Σ ((i : I) → J i → O.Complete) (λ F → O.El (O.Distribution.left I J F))))
  OldParameters E-congruence-kind = Σ (Type ℓ) (λ I → Σ (I → O.Complete) (λ F → Σ (I → O.Complete) (λ H →
    Σ (OldCongruence I F H) (λ _ → I))))
  OldParameters P-congruence-kind = Σ (Type ℓ) (λ I → Σ (I → O.Complete) (λ F → Σ (I → O.Complete) (λ H →
    OldCongruence I F H)))
  old-tagged : Iso R.Rule (Σ Kind OldParameters)
  Iso.fun old-tagged (R.E-rule I F i) = E-kind , I , F , i
  Iso.fun old-tagged (R.Pi-rule I F) = P-kind , I , F
  Iso.fun old-tagged (R.compare-rule a b e p) = compare-kind , a , b , e , p
  Iso.fun old-tagged (R.identity-rule a) = identity-kind , a
  Iso.fun old-tagged (R.inverse-rule a b e p) = inverse-kind , a , b , e , p
  Iso.fun old-tagged (R.compose-rule a b c e f p q) = compose-kind , a , b , c , e , f , p , q
  Iso.fun old-tagged (R.higher-rule c x y p q alpha) = higher-kind , c , x , y , p , q , alpha
  Iso.fun old-tagged (R.reflexivity-rule c x) = reflexivity-kind , c , x
  Iso.fun old-tagged (R.path-lift-rule c d e x y) = path-lift-kind , c , d , e , x , y
  Iso.fun old-tagged (R.distribution-rule I J F v) = distribution-kind , I , J , F , v
  Iso.fun old-tagged (R.E-congruence-rule I F H e p i) = E-congruence-kind , I , F , H , (e , p) , i
  Iso.fun old-tagged (R.Pi-congruence-rule I F H e p) = P-congruence-kind , I , F , H , e , p
  Iso.inv old-tagged (E-kind , I , F , i) = R.E-rule I F i
  Iso.inv old-tagged (P-kind , I , F) = R.Pi-rule I F
  Iso.inv old-tagged (compare-kind , a , b , e , p) = R.compare-rule a b e p
  Iso.inv old-tagged (identity-kind , a) = R.identity-rule a
  Iso.inv old-tagged (inverse-kind , a , b , e , p) = R.inverse-rule a b e p
  Iso.inv old-tagged (compose-kind , a , b , c , e , f , p , q) = R.compose-rule a b c e f p q
  Iso.inv old-tagged (higher-kind , c , x , y , p , q , alpha) = R.higher-rule c x y p q alpha
  Iso.inv old-tagged (reflexivity-kind , c , x) = R.reflexivity-rule c x
  Iso.inv old-tagged (path-lift-kind , c , d , e , x , y) = R.path-lift-rule c d e x y
  Iso.inv old-tagged (distribution-kind , I , J , F , v) = R.distribution-rule I J F v
  Iso.inv old-tagged (E-congruence-kind , I , F , H , (e , p) , i) = R.E-congruence-rule I F H e p i
  Iso.inv old-tagged (P-congruence-kind , I , F , H , e , p) = R.Pi-congruence-rule I F H e p
  Iso.leftInv old-tagged (R.E-rule _ _ _) = refl
  Iso.leftInv old-tagged (R.Pi-rule _ _) = refl
  Iso.leftInv old-tagged (R.compare-rule _ _ _ _) = refl
  Iso.leftInv old-tagged (R.identity-rule _) = refl
  Iso.leftInv old-tagged (R.inverse-rule _ _ _ _) = refl
  Iso.leftInv old-tagged (R.compose-rule _ _ _ _ _ _ _) = refl
  Iso.leftInv old-tagged (R.higher-rule _ _ _ _ _ _) = refl
  Iso.leftInv old-tagged (R.reflexivity-rule _ _) = refl
  Iso.leftInv old-tagged (R.path-lift-rule _ _ _ _ _) = refl
  Iso.leftInv old-tagged (R.distribution-rule _ _ _ _) = refl
  Iso.leftInv old-tagged (R.E-congruence-rule _ _ _ _ _ _) = refl
  Iso.leftInv old-tagged (R.Pi-congruence-rule _ _ _ _ _) = refl
  Iso.rightInv old-tagged (E-kind , _) = refl
  Iso.rightInv old-tagged (P-kind , _) = refl
  Iso.rightInv old-tagged (compare-kind , _) = refl
  Iso.rightInv old-tagged (identity-kind , _) = refl
  Iso.rightInv old-tagged (inverse-kind , _) = refl
  Iso.rightInv old-tagged (compose-kind , _) = refl
  Iso.rightInv old-tagged (higher-kind , _) = refl
  Iso.rightInv old-tagged (reflexivity-kind , _) = refl
  Iso.rightInv old-tagged (path-lift-kind , _) = refl
  Iso.rightInv old-tagged (distribution-kind , _) = refl
  Iso.rightInv old-tagged (E-congruence-kind , _) = refl
  Iso.rightInv old-tagged (P-congruence-kind , _) = refl

  family-equivalence : (I : Type ℓ) → (I → O.Complete) ≃ (I → G.Package)
  family-equivalence I = equivΠCod (λ _ → G.complete-equivalence)
  comparison-parameters-equivalence : OldComparison ≃ ComparisonParameters
  comparison-parameters-equivalence = Σ-cong-equiv G.complete-equivalence
    (λ a → Σ-cong-equiv G.complete-equivalence (λ b → idEquiv (OldFiller a b)))
  parameters-equivalence : (k : Kind) → OldParameters k ≃ Parameters k
  parameters-equivalence E-kind = Σ-cong-equiv (idEquiv (Type ℓ))
    (λ I → Σ-cong-equiv (family-equivalence I) (λ F → idEquiv I))
  parameters-equivalence P-kind = Σ-cong-equiv (idEquiv (Type ℓ)) family-equivalence
  parameters-equivalence compare-kind = comparison-parameters-equivalence
  parameters-equivalence identity-kind = G.complete-equivalence
  parameters-equivalence inverse-kind = comparison-parameters-equivalence
  parameters-equivalence compose-kind = Σ-cong-equiv G.complete-equivalence
    (λ a → Σ-cong-equiv G.complete-equivalence (λ b → Σ-cong-equiv G.complete-equivalence
      (λ c → idEquiv (Σ (OldTy a ≃ OldTy b) (λ e → Σ (OldTy b ≃ OldTy c) (λ f →
        Σ (equivFun e (O.value a) ≡ O.value b) (λ _ → equivFun f (O.value b) ≡ O.value c)))))))
  parameters-equivalence higher-kind = Σ-cong-equiv (isoToEquiv G.syntax-iso)
    (λ c → idEquiv (Σ (O.El c) (λ x → Σ (O.El c) (λ y → Σ (x ≡ y) (λ p → Σ (x ≡ y) (λ q → p ≡ q))))))
  parameters-equivalence reflexivity-kind = G.sigma-package-equivalence
  parameters-equivalence path-lift-kind = Σ-cong-equiv (isoToEquiv G.syntax-iso)
    (λ c → Σ-cong-equiv (isoToEquiv G.syntax-iso)
      (λ d → idEquiv (Σ (O.El c ≃ O.El d) (λ _ → Σ (O.El c) (λ _ → O.El c)))))
  parameters-equivalence distribution-kind = Σ-cong-equiv (idEquiv (Type ℓ))
    (λ I → Σ-cong-equiv (idEquiv (I → Type ℓ)) (λ J →
      Σ-cong-equiv (equivΠCod (λ i → family-equivalence (J i)))
        (λ F → idEquiv (O.El (O.Distribution.left I J F)))))
  parameters-equivalence E-congruence-kind = Σ-cong-equiv (idEquiv (Type ℓ))
    (λ I → Σ-cong-equiv (family-equivalence I) (λ F → Σ-cong-equiv (family-equivalence I)
      (λ H → idEquiv (Σ (OldCongruence I F H) (λ _ → I)))))
  parameters-equivalence P-congruence-kind = Σ-cong-equiv (idEquiv (Type ℓ))
    (λ I → Σ-cong-equiv (family-equivalence I) (λ F → Σ-cong-equiv (family-equivalence I)
      (λ H → idEquiv (OldCongruence I F H))))
  rule-equivalence : R.Rule ≃ Rule
  rule-equivalence = compEquiv (isoToEquiv old-tagged) (Σ-cong-equiv-snd parameters-equivalence)
  encode-rule : R.Rule → Rule
  encode-rule = equivFun rule-equivalence
  port-equivalence : (r : R.Rule) → R.Arity r ≃ Arity (encode-rule r)
  port-equivalence (R.E-rule _ _ _) = idEquiv _
  port-equivalence (R.Pi-rule _ _) = idEquiv _
  port-equivalence (R.compare-rule _ _ _ _) = idEquiv _
  port-equivalence (R.identity-rule _) = idEquiv _
  port-equivalence (R.inverse-rule _ _ _ _) = idEquiv _
  port-equivalence (R.compose-rule _ _ _ _ _ _ _) = idEquiv _
  port-equivalence (R.higher-rule _ _ _ _ _ _) = idEquiv _
  port-equivalence (R.reflexivity-rule _ _) = idEquiv _
  port-equivalence (R.path-lift-rule _ _ _ _ _) = idEquiv _
  port-equivalence (R.distribution-rule _ _ _ _) = idEquiv _
  port-equivalence (R.E-congruence-rule _ _ _ _ _ _) = idEquiv _
  port-equivalence (R.Pi-congruence-rule _ _ _ _ _) = idEquiv _
  input-commutes : (r : R.Rule) (i : R.Arity r)
    → G.encode-package (R.input r i) ≡ input (encode-rule r) (equivFun (port-equivalence r) i)
  input-commutes (R.E-rule _ _ _) (lift i) = refl
  input-commutes (R.Pi-rule _ _) (lift i) = refl
  input-commutes (R.compare-rule _ _ _ _) (lift true) = refl
  input-commutes (R.compare-rule _ _ _ _) (lift false) = refl
  input-commutes (R.identity-rule _) _ = refl
  input-commutes (R.inverse-rule _ _ _ _) _ = refl
  input-commutes (R.compose-rule _ _ _ _ _ _ _) (lift true) = refl
  input-commutes (R.compose-rule _ _ _ _ _ _ _) (lift false) = refl
  input-commutes (R.higher-rule _ _ _ _ _ _) (lift true) = refl
  input-commutes (R.higher-rule _ _ _ _ _ _) (lift false) = refl
  input-commutes (R.reflexivity-rule _ _) _ = refl
  input-commutes (R.path-lift-rule _ _ _ _ _) _ = refl
  input-commutes (R.distribution-rule _ _ _ _) (inl (lift (i , j))) = refl
  input-commutes (R.distribution-rule _ _ _ _) (inr _) = refl
  input-commutes (R.E-congruence-rule _ _ _ _ _ _) (lift i) = refl
  input-commutes (R.Pi-congruence-rule _ _ _ _ _) (lift i) = refl
  output-commutes : (r : R.Rule) → G.encode-package (R.output r) ≡ output (encode-rule r)
  output-commutes (R.E-rule _ _ _) = refl
  output-commutes (R.Pi-rule _ _) = refl
  output-commutes (R.compare-rule _ _ _ _) = refl
  output-commutes (R.identity-rule _) = refl
  output-commutes (R.inverse-rule _ _ _ _) = refl
  output-commutes (R.compose-rule _ _ _ _ _ _ _) = refl
  output-commutes (R.higher-rule _ _ _ _ _ _) = refl
  output-commutes (R.reflexivity-rule _ _) = refl
  output-commutes (R.path-lift-rule _ _ _ _ _) = refl
  output-commutes (R.distribution-rule I J F v) i = comparison-package
    (G.encode-package (O.pack (O.Distribution.left I J F) v))
    (G.encode-package (O.pack (O.Distribution.right I J F) (Iso.fun (O.Distribution.law I J F) v)))
    (equivEq {e = isoToEquiv (O.Distribution.law I J F)}
      {f = isoToEquiv (Distribution.law I J (λ i j → G.encode-package (F i j)))} refl i) refl
  output-commutes (R.E-congruence-rule _ _ _ _ _ _) = refl
  output-commutes (R.Pi-congruence-rule _ _ _ _ _) = refl
