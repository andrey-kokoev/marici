{-# OPTIONS --safe --cubical --guardedness #-}
module IndexIdentityCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (assoc; lUnit; rCancel)
open import Cubical.Foundations.Path using (PathP≃Path)
open import Cubical.Foundations.Transport using (substComposite; subst⁻Subst)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv-fst; Σ-cong-equiv-snd; ΣPath≃PathΣ)
import WholePackageSigmaPi as Whole
import SigmaPiComparisonDecomposition as Decomposition

module Indexed (ℓ : Level) where
  open Whole.Universe ℓ
  module D = Decomposition.Decomposition ℓ

  -- Keep the index's own code, not only its interpreted type.
  record Family : Type (ℓ-suc ℓ) where
    constructor family
    field
      index : Code
      fibre : El index → Code
  open Family public

  Index : Family → Type ℓ
  Index F = El (index F)

  Fibre : (F : Family) → Index F → Type ℓ
  Fibre F i = El (fibre F i)

  Total : Family → Type ℓ
  Total F = Σ (Index F) (Fibre F)

  Sections : Family → Type ℓ
  Sections F = (i : Index F) → Fibre F i

  IndexEvidence : (F : Family) → Index F → Index F → Type ℓ
  IndexEvidence F i j = D.Evidence (index F) i j

  index-path : (F : Family) {i j : Index F} → IndexEvidence F i j → i ≡ j
  index-path F = D.decode (index F)

  identity-index : (F : Family) (i : Index F) → IndexEvidence F i i
  identity-index F i = D.encode (index F) refl

  inverse-index : (F : Family) {i j : Index F}
    → IndexEvidence F i j → IndexEvidence F j i
  inverse-index F c = D.encode (index F) (sym (index-path F c))

  compose-index : (F : Family) {i j k : Index F}
    → IndexEvidence F i j → IndexEvidence F j k → IndexEvidence F i k
  compose-index F c d = D.encode (index F) (index-path F c ∙ index-path F d)

  -- The normalized index witnesses themselves have explicit groupoid laws.
  index-left-unit : (F : Family) {i j : Index F} (c : IndexEvidence F i j)
    → compose-index F (identity-index F i) c ≡ c
  index-left-unit F c =
    cong (D.encode (index F))
      (cong (λ p → p ∙ index-path F c) (D.witness-completeness (index F) refl)
       ∙ sym (lUnit (index-path F c)))
    ∙ D.evidence-recovery (index F) c

  index-cancellation : (F : Family) {i j : Index F} (c : IndexEvidence F i j)
    → compose-index F c (inverse-index F c) ≡ identity-index F i
  index-cancellation F c = cong (D.encode (index F))
    (cong (λ p → index-path F c ∙ p)
       (D.witness-completeness (index F) (sym (index-path F c)))
     ∙ rCancel (index-path F c))

  index-associativity : (F : Family) {i j k m : Index F}
    (c : IndexEvidence F i j) (d : IndexEvidence F j k) (e : IndexEvidence F k m)
    → compose-index F c (compose-index F d e) ≡ compose-index F (compose-index F c d) e
  index-associativity F c d e = cong (D.encode (index F))
    (cong (λ p → index-path F c ∙ p)
       (D.witness-completeness (index F) (index-path F d ∙ index-path F e))
     ∙ assoc (index-path F c) (index-path F d) (index-path F e)
     ∙ sym (cong (λ p → p ∙ index-path F e)
       (D.witness-completeness (index F) (index-path F c ∙ index-path F d))))

  act : (F : Family) {i j : Index F} → IndexEvidence F i j → Fibre F i → Fibre F j
  act F c = subst (Fibre F) (index-path F c)

  identity-action : (F : Family) (i : Index F) (x : Fibre F i)
    → act F (identity-index F i) x ≡ x
  identity-action F i x =
    cong (λ p → subst (Fibre F) p x) (D.witness-completeness (index F) refl)
    ∙ substRefl {B = Fibre F} x

  composite-action : (F : Family) {i j k : Index F}
    (c : IndexEvidence F i j) (d : IndexEvidence F j k) (x : Fibre F i)
    → act F (compose-index F c d) x ≡ act F d (act F c x)
  composite-action F c d x =
    cong (λ p → subst (Fibre F) p x)
      (D.witness-completeness (index F) (index-path F c ∙ index-path F d))
    ∙ substComposite (Fibre F) (index-path F c) (index-path F d) x

  inverse-action : (F : Family) {i j : Index F}
    (c : IndexEvidence F i j) (x : Fibre F i)
    → act F (inverse-index F c) (act F c x) ≡ x
  inverse-action F c x =
    cong (λ p → subst (Fibre F) p (act F c x))
      (D.witness-completeness (index F) (sym (index-path F c)))
    ∙ subst⁻Subst (Fibre F) (index-path F c) x

  higher-action : (F : Family) {i j : Index F}
    {c d : IndexEvidence F i j} → c ≡ d → (x : Fibre F i) → act F c x ≡ act F d x
  higher-action F alpha x = cong (λ c → act F c x) alpha

  record HigherActionCertificate : Type (ℓ-suc ℓ) where
    constructor higher-action-certificate
    field
      family-data : Family
      start end : Index family-data
      first second : IndexEvidence family-data start end
      index-comparison : first ≡ second
      fibre-comparison : (x : Fibre family-data start)
        → act family-data first x ≡ act family-data second x

  retain-higher-action : (F : Family) {i j : Index F}
    {c d : IndexEvidence F i j} → c ≡ d → HigherActionCertificate
  retain-higher-action F {i} {j} {c} {d} alpha =
    higher-action-certificate F i j c d alpha (higher-action F alpha)

  reify-higher-action : HigherActionCertificate → Whole.Universe.Complete (ℓ-suc ℓ)
  reify-higher-action c = Whole.Universe.pack (Whole.Universe.atom HigherActionCertificate) c

  -- A dependent section already carries its compatibility with index paths.
  section-action : (F : Family) (s : Sections F) {i j : Index F}
    (c : IndexEvidence F i j) → act F c (s i) ≡ s j
  section-action F s c = fromPathP (λ t → s (index-path F c t))

  SumEvidence : (F : Family) → Total F → Total F → Type ℓ
  SumEvidence F x y = Σ[ c ∈ IndexEvidence F (fst x) (fst y) ]
    D.Evidence (fibre F (fst y)) (act F c (snd x)) (snd y)

  -- Both the index evidence and fibre evidence are recursively decomposed.
  sum-equiv : (F : Family) (x y : Total F) → SumEvidence F x y ≃ (x ≡ y)
  sum-equiv F x y = compEquiv
    (Σ-cong-equiv-snd (λ c → compEquiv
      (D.decode-equiv (fibre F (fst y)) (act F c (snd x)) (snd y))
      (invEquiv (PathP≃Path (λ t → Fibre F (index-path F c t)) (snd x) (snd y)))))
    (compEquiv
      (Σ-cong-equiv-fst
        {B = λ p → PathP (λ t → Fibre F (p t)) (snd x) (snd y)}
        (D.decode-equiv (index F) (fst x) (fst y)))
      ΣPath≃PathΣ)

  sum-recovery : (F : Family) {x y : Total F} (p : x ≡ y)
    → equivFun (sum-equiv F x y) (invEq (sum-equiv F x y) p) ≡ p
  sum-recovery F = secEq (sum-equiv F _ _)

  -- The complete family description and values survive reification.
  E-whole-indexed : (F : Family) → Total F → Whole.Universe.Complete (ℓ-suc ℓ)
  E-whole-indexed F x = Whole.Universe.pack
    (Whole.Universe.atom (Σ Family Total)) (F , x)

  Pi-whole-indexed : (F : Family) → Sections F → Whole.Universe.Complete (ℓ-suc ℓ)
  Pi-whole-indexed F s = Whole.Universe.pack
    (Whole.Universe.atom (Σ Family Sections)) (F , s)

  record Certificate : Type (ℓ-suc ℓ) where
    constructor certificate
    field
      family-data : Family
      left right : Total family-data
      original : left ≡ right
      decomposed : SumEvidence family-data left right
      reconstruction : equivFun (sum-equiv family-data left right) decomposed ≡ original

  certify : (F : Family) {x y : Total F} → x ≡ y → Certificate
  certify F {x} {y} p = certificate F x y p (invEq (sum-equiv F x y) p) (sum-recovery F p)

  reify-certificate : Certificate → Whole.Universe.Complete (ℓ-suc ℓ)
  reify-certificate c = Whole.Universe.pack (Whole.Universe.atom Certificate) c

  record ActionCertificate : Type (ℓ-suc ℓ) where
    constructor action-certificate
    field
      family-data : Family
      start end : Index family-data
      index-evidence : IndexEvidence family-data start end
      input-value : Fibre family-data start
      output-value : Fibre family-data end
      agrees-with-action : act family-data index-evidence input-value ≡ output-value

  retain-action : (F : Family) {i j : Index F} (c : IndexEvidence F i j)
    (x : Fibre F i) → ActionCertificate
  retain-action F {i} {j} c x = action-certificate F i j c x (act F c x) refl

  reify-action : ActionCertificate → Whole.Universe.Complete (ℓ-suc ℓ)
  reify-action c = Whole.Universe.pack (Whole.Universe.atom ActionCertificate) c
