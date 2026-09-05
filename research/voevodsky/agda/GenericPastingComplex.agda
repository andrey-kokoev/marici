{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module GenericPastingComplex where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.AbGroup
open import Cubical.Algebra.Group.Properties

private variable ℓ : Level

module Triangle (M : AbGroup ℓ) where
  open AbGroupStr (snd M)

  record M³ : Type ℓ where
    constructor triple
    field x y z : fst M
  open M³

  -- The normalized boundary presentation uses its first two cyclic
  -- differences as coordinates and defines the third by closure.
  ∂₁ : M³ → M³
  ∂₁ v = triple ((- x v) + y v)
                ((- y v) + z v)
                (- (((- x v) + y v) + ((- y v) + z v)))

  -- Original cyclic incidence boundary.
  ∂₁-cyclic : M³ → M³
  ∂₁-cyclic v = triple ((- x v) + y v)
                       ((- y v) + z v)
                       ((- z v) + x v)

  cyclic-interior : (v : M³) →
    (((- x v) + y v) + ((- y v) + z v)) ≡ (- x v) + z v
  cyclic-interior v =
    sym (+Assoc (- x v) (y v) ((- y v) + z v)) ∙
    cong ((- x v) +_) (+Assoc (y v) (- y v) (z v)) ∙
    cong ((- x v) +_) (cong (_+ z v) (+InvR (y v)) ∙ +IdL (z v))

  normalized-third-is-cyclic : (v : M³) →
    - (((- x v) + y v) + ((- y v) + z v)) ≡ (- z v) + x v
  normalized-third-is-cyclic v =
    cong -_ (cyclic-interior v) ∙
    GroupTheory.invDistr (AbGroup→Group M) (- x v) (z v) ∙
    cong ((- z v) +_) (GroupTheory.invInv (AbGroup→Group M) (x v))

  normalized-is-cyclic : (v : M³) → ∂₁ v ≡ ∂₁-cyclic v
  normalized-is-cyclic v i =
    triple ((- x v) + y v) ((- y v) + z v)
      (normalized-third-is-cyclic v i)

  ∂₂ : M³ → fst M
  ∂₂ v = (x v + y v) + z v

  chain : (v : M³) → ∂₂ (∂₁ v) ≡ 0g
  chain v = +InvR (((- x v) + y v) + ((- y v) + z v))

  chain-cyclic : (v : M³) → ∂₂ (∂₁-cyclic v) ≡ 0g
  chain-cyclic v = sym (cong ∂₂ (normalized-is-cyclic v)) ∙ chain v

  cycle : fst M → fst M → M³
  cycle p q = triple p q (- (p + q))

  cycle-closed : (p q : fst M) → ∂₂ (cycle p q) ≡ 0g
  cycle-closed p q = +InvR (p + q)

  preimage : fst M → fst M → M³
  preimage p q = triple 0g p (p + q)

  inv-zero : - 0g ≡ 0g
  inv-zero = GroupTheory.inv1g (AbGroup→Group M)

  exact-x : (p q : fst M) → (- 0g) + p ≡ p
  exact-x p q = cong (_+ p) inv-zero ∙ +IdL p

  exact-y : (p q : fst M) → (- p) + (p + q) ≡ q
  exact-y p q = +Assoc (- p) p q ∙ cong (_+ q) (+InvL p) ∙ +IdL q

  exact-z : (p q : fst M) →
    - (((- 0g) + p) + ((- p) + (p + q))) ≡ - (p + q)
  exact-z p q = cong -_ (cong₂ _+_ (exact-x p q) (exact-y p q))

  exact-normalized : (p q : fst M) → ∂₁ (preimage p q) ≡ cycle p q
  exact-normalized p q i = triple (exact-x p q i) (exact-y p q i) (exact-z p q i)

  closed-third : (v : M³) → ∂₂ v ≡ 0g → z v ≡ - (x v + y v)
  closed-third v h =
    sym (+IdL (z v))
    ∙ cong (_+ z v) (sym (+InvL (x v + y v)))
    ∙ sym (+Assoc (- (x v + y v)) (x v + y v) (z v))
    ∙ cong ((- (x v + y v)) +_) h
    ∙ +IdR (- (x v + y v))

  closed-normal-form : (v : M³) → ∂₂ v ≡ 0g → v ≡ cycle (x v) (y v)
  closed-normal-form v h i = triple (x v) (y v) (closed-third v h i)

  middle-exact : (v : M³) → ∂₂ v ≡ 0g → Σ[ u ∈ M³ ] ∂₁ u ≡ v
  middle-exact v h =
    preimage (x v) (y v) ,
    exact-normalized (x v) (y v) ∙ sym (closed-normal-form v h)

  ∂₂-preimage : fst M → M³
  ∂₂-preimage m = triple m 0g 0g

  ∂₂-surjective : (m : fst M) → ∂₂ (∂₂-preimage m) ≡ m
  ∂₂-surjective m = +IdR (m + 0g) ∙ +IdR m
