{-# OPTIONS --safe --cubical --guardedness #-}
module SourceRelativeComparisonCompleteness where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Base using (_×_)
import WholePackageSigmaPi as Whole
import SigmaPiComparisonDecomposition as Decomposition
import IndexIdentityCoherence as Indexed

-- A source comparison theory may have many derivations of the same path.
-- Its decoder is required, but neither injectivity nor completeness is
-- assumed until named explicitly below.
module Relative (ℓ : Level)
  (Generator : (A : Type ℓ) → A → A → Type ℓ)
  (interpret : (A : Type ℓ) (x y : A) → Generator A x y → x ≡ y) where
  open Whole.Universe ℓ
  module D = Decomposition.Decomposition ℓ
  module IX = Indexed.Indexed ℓ

  Represents : (A : Type ℓ) (x y : A) → x ≡ y → Type ℓ
  Represents A x y p = Σ[ g ∈ Generator A x y ] (interpret A x y g ≡ p)

  BoundaryComplete : Type ℓ → Type ℓ
  BoundaryComplete A = (x y : A) (p : x ≡ y) → Represents A x y p

  SourceComplete : Type (ℓ-suc ℓ)
  SourceComplete = (A : Type ℓ) → BoundaryComplete A

  -- For one frozen code, require only its actual residual boundaries.
  -- This is the local theorem's premise, not completeness for all types.
  Requirements : Code → Type ℓ
  Requirements (atom A) = BoundaryComplete A
  Requirements (E I F) = BoundaryComplete I × ((i : I) → Requirements (F i))
  Requirements (Pi I F) = (i : I) → Requirements (F i)
  Requirements (retain Q q R) = Requirements R
  Requirements (maps Q R) = Requirements R
  Requirements (paths Q a b) = BoundaryComplete (D.Evidence Q a b)
  Requirements (equivalences Q R) = Requirements R
  Requirements (comparison Q R e) = Requirements Q

  -- Audit every residual boundary in the actual recursive decomposition.
  -- Composite E/Pi/equivalence/comparison nodes have no whole-witness escape.
  Supports : (Q : Code) (x y : El Q) → D.Evidence Q x y → Type ℓ
  Supports (atom A) x y c = Represents A x y c
  Supports (E I F) x y (p , c) =
    Represents I (fst x) (fst y) p ×
    Supports (F (fst y)) (transport (λ t → El (F (p t))) (snd x)) (snd y) c
  Supports (Pi I F) x y cs = (i : I) → Supports (F i) (x i) (y i) (cs i)
  Supports (retain Q q R) x y c = Supports R x y c
  Supports (maps Q R) x y cs = (i : El Q) → Supports R (x i) (y i) (cs i)
  Supports (paths Q a b) p q c = Represents (D.Evidence Q a b)
    (invEq (D.decode-equiv Q a b) p) (invEq (D.decode-equiv Q a b) q) c
  Supports (equivalences Q R) e f cs =
    (a : El Q) → Supports R (equivFun e a) (equivFun f a) (cs a)
  Supports (comparison Q R e) x y c = Supports Q (fst x) (fst y) c

  support-local : (Q : Code) → Requirements Q → (x y : El Q)
    (c : D.Evidence Q x y) → Supports Q x y c
  support-local (atom A) complete x y c = complete x y c
  support-local (E I F) (indices , fibres) x y (p , c) =
    indices (fst x) (fst y) p ,
    support-local (F (fst y)) (fibres (fst y))
      (transport (λ t → El (F (p t))) (snd x)) (snd y) c
  support-local (Pi I F) complete x y cs = λ i → support-local (F i) (complete i) (x i) (y i) (cs i)
  support-local (retain Q q R) complete x y c = support-local R complete x y c
  support-local (maps Q R) complete x y cs = λ i → support-local R complete (x i) (y i) (cs i)
  support-local (paths Q a b) complete p q c = complete
    (invEq (D.decode-equiv Q a b) p) (invEq (D.decode-equiv Q a b) q) c
  support-local (equivalences Q R) complete e f cs =
    λ a → support-local R complete (equivFun e a) (equivFun f a) (cs a)
  support-local (comparison Q R e) complete x y c = support-local Q complete (fst x) (fst y) c

  requirements-from-source : SourceComplete → (Q : Code) → Requirements Q
  requirements-from-source complete (atom A) = complete A
  requirements-from-source complete (E I F) = complete I , (λ i → requirements-from-source complete (F i))
  requirements-from-source complete (Pi I F) = λ i → requirements-from-source complete (F i)
  requirements-from-source complete (retain Q q R) = requirements-from-source complete R
  requirements-from-source complete (maps Q R) = requirements-from-source complete R
  requirements-from-source complete (paths Q a b) = complete (D.Evidence Q a b)
  requirements-from-source complete (equivalences Q R) = requirements-from-source complete R
  requirements-from-source complete (comparison Q R e) = requirements-from-source complete Q

  support-all : SourceComplete → (Q : Code) (x y : El Q)
    (c : D.Evidence Q x y) → Supports Q x y c
  support-all complete Q = support-local Q (requirements-from-source complete Q)

  Supported : (Q : Code) → El Q → El Q → Type ℓ
  Supported Q x y = Σ[ c ∈ D.Evidence Q x y ] Supports Q x y c

  sound : (Q : Code) {x y : El Q} → Supported Q x y → x ≡ y
  sound Q c = D.decode Q (fst c)

  StructuralComplete : Type (ℓ-suc ℓ)
  StructuralComplete = (Q : Code) (x y : El Q) (p : x ≡ y)
    → Σ[ c ∈ Supported Q x y ] (sound Q c ≡ p)

  local-completeness : (Q : Code) → Requirements Q → (x y : El Q) (p : x ≡ y)
    → Σ[ c ∈ Supported Q x y ] (sound Q c ≡ p)
  local-completeness Q requirements x y p =
    (D.encode Q p , support-local Q requirements x y (D.encode Q p)) , D.witness-completeness Q p

  source-to-structural : SourceComplete → StructuralComplete
  source-to-structural complete Q x y p =
    (D.encode Q p , support-all complete Q x y (D.encode Q p)) , D.witness-completeness Q p

  structural-to-source : StructuralComplete → SourceComplete
  structural-to-source complete A x y p with complete (atom A) x y p
  ... | ((c , (g , gp)) , cp) = g , gp ∙ cp

  -- Logical equivalence of completeness obligations, not a claim that the
  -- two proof types have unique inhabitants or equivalent higher structure.
  completeness-reduction :
    (SourceComplete → StructuralComplete) × (StructuralComplete → SourceComplete)
  completeness-reduction = source-to-structural , structural-to-source

  -- The explicitly coded index interface receives the same theorem:
  -- both its index evidence and its fibre evidence have source derivations.
  FamilySupported : (F : IX.Family) (x y : IX.Total F) → Type ℓ
  FamilySupported F x y = Σ[ c ∈ IX.SumEvidence F x y ]
    (Supports (IX.index F) (fst x) (fst y) (fst c) ×
     Supports (IX.fibre F (fst y)) (IX.act F (fst c) (snd x)) (snd y) (snd c))

  FamilyRequirements : IX.Family → Type ℓ
  FamilyRequirements F = Requirements (IX.index F) × ((i : IX.Index F) → Requirements (IX.fibre F i))

  local-family-completeness : (F : IX.Family) → FamilyRequirements F
    → (x y : IX.Total F) (p : x ≡ y)
    → Σ[ c ∈ FamilySupported F x y ] (equivFun (IX.sum-equiv F x y) (fst c) ≡ p)
  local-family-completeness F (indices , fibres) x y p =
    (c , (support-local (IX.index F) indices (fst x) (fst y) (fst c) ,
          support-local (IX.fibre F (fst y)) (fibres (fst y))
            (IX.act F (fst c) (snd x)) (snd y) (snd c))) , IX.sum-recovery F p
    where
    c : IX.SumEvidence F x y
    c = invEq (IX.sum-equiv F x y) p

  family-completeness : SourceComplete → (F : IX.Family) (x y : IX.Total F) (p : x ≡ y)
    → Σ[ c ∈ FamilySupported F x y ] (equivFun (IX.sum-equiv F x y) (fst c) ≡ p)
  family-completeness complete F = local-family-completeness F
    (requirements-from-source complete (IX.index F) ,
     (λ i → requirements-from-source complete (IX.fibre F i)))

  record Certificate : Type (ℓ-suc ℓ) where
    constructor certificate
    field
      source : Code
      left right : El source
      original : left ≡ right
      supported : Supported source left right
      reconstruction : sound source supported ≡ original

  certify : SourceComplete → (Q : Code) {x y : El Q} → x ≡ y → Certificate
  certify complete Q {x} {y} p with source-to-structural complete Q x y p
  ... | c , proof = certificate Q x y p c proof

  reify-certificate : Certificate → Whole.Universe.Complete (ℓ-suc ℓ)
  reify-certificate c = Whole.Universe.pack (Whole.Universe.atom Certificate) c
