{-# OPTIONS --safe --cubical --guardedness #-}
module WholePackageSigmaPi where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.GroupoidLaws using (assoc; rUnit; lUnit; rCancel)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv-snd)
open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)
import ProofRelevantCoherenceClosure as Witness

-- An inductive-recursive universe of retained presentations. El is a view
-- of a package, never a replacement for its retained Code and witnesses.
module Universe (ℓ : Level) where
  mutual
    data Code : Type (ℓ-suc ℓ) where
      atom : Type ℓ → Code
      E : (I : Type ℓ) → (I → Code) → Code
      Pi : (I : Type ℓ) → (I → Code) → Code
      paths : (Q : Code) → El Q → El Q → Code
      maps : Code → Code → Code
      equivalences : Code → Code → Code
      -- Retain an actual value of a prior expression as provenance.
      -- In particular this can retain a whole previous chain or proof.
      retain : (Q : Code) → El Q → Code → Code
      comparison : (Q R : Code) → El Q ≃ El R → Code

    El : Code → Type ℓ
    El (atom A) = A
    El (E I F) = Σ I (λ i → El (F i))
    El (Pi I F) = (i : I) → El (F i)
    El (paths Q x y) = x ≡ y
    El (maps Q R) = El Q → El R
    El (equivalences Q R) = El Q ≃ El R
    El (retain Q q R) = El R
    El (comparison Q R e) = Σ[ x ∈ El Q ] Σ[ y ∈ El R ] (equivFun e x ≡ y)

  record Complete : Type (ℓ-suc ℓ) where
    constructor pack
    field
      expression : Code
      value : El expression
  open Complete public

  -- Whole input family retained, including every supplied value. A sum
  -- resolution selects a fibre; it does not discard the other provenance.
  retained : Complete → Code
  retained (pack Q q) = retain Q q Q

  E-package : (I : Type ℓ) → (F : I → Complete) → I → Complete
  E-package I F i = pack (E I (λ j → retained (F j))) (i , value (F i))

  Pi-package : (I : Type ℓ) → (F : I → Complete) → Complete
  Pi-package I F = pack (Pi I (λ i → retained (F i))) (λ i → value (F i))

  recover : Code → Maybe Complete
  recover (retain Q q R) = just (pack Q q)
  recover _ = nothing

  recover-retained : (a : Complete) → recover (retained a) ≡ just a
  recover-retained a = refl

  input-family : Code → Maybe (Σ[ I ∈ Type ℓ ] (I → Maybe Complete))
  input-family (E I F) = just (I , (λ i → recover (F i)))
  input-family (Pi I F) = just (I , (λ i → recover (F i)))
  input-family _ = nothing

  E-retains-family : (I : Type ℓ) (F : I → Complete) (i : I)
    → input-family (expression (E-package I F i)) ≡ just (I , (λ j → just (F j)))
  E-retains-family I F i = refl

  Pi-retains-family : (I : Type ℓ) (F : I → Complete)
    → input-family (expression (Pi-package I F)) ≡ just (I , (λ j → just (F j)))
  Pi-retains-family I F = refl

  remember : Complete → Complete → Complete
  remember a b = pack (retain (expression a) (value a) (expression b)) (value b)

  -- Comparisons keep both complete endpoints, their equivalence and the
  -- actual boundary witness. No proof is replaced by mere existence.
  comparison-package : (a b : Complete)
    → (e : El (expression a) ≃ El (expression b))
    → equivFun e (value a) ≡ value b → Complete
  comparison-package a b e p =
    pack (comparison (retained a) (retained b) e) (value a , value b , p)

  path-package : (Q : Code) (x y : El Q) → x ≡ y → Complete
  path-package Q x y p = pack (paths Q x y) p

  identity-comparison : (a : Complete) → Complete
  identity-comparison a = comparison-package a a (idEquiv _) refl

  inverse-comparison : (a b : Complete)
    (e : El (expression a) ≃ El (expression b))
    (p : equivFun e (value a) ≡ value b) → Complete
  inverse-comparison a b e p = remember (comparison-package a b e p)
    (comparison-package b a (invEquiv e)
      (sym (cong (invEq e) p) ∙ retEq e (value a)))

  compose-comparisons : (a b c : Complete)
    (e : El (expression a) ≃ El (expression b))
    (f : El (expression b) ≃ El (expression c))
    (p : equivFun e (value a) ≡ value b)
    (q : equivFun f (value b) ≡ value c) → Complete
  compose-comparisons a b c e f p q =
    remember (comparison-package a b e p)
    (remember (comparison-package b c f q)
      (comparison-package a c (compEquiv e f) (cong (equivFun f) p ∙ q)))

  -- E/Pi act on the comparison witnesses as well as the endpoints.
  module Congruence (I : Type ℓ) (F G : I → Complete)
    (e : (i : I) → El (expression (F i)) ≃ El (expression (G i)))
    (p : (i : I) → equivFun (e i) (value (F i)) ≡ value (G i)) where

    all-comparisons : Complete
    all-comparisons = Pi-package I (λ i → comparison-package (F i) (G i) (e i) (p i))

    E-comparison : (i : I) → Complete
    E-comparison i = remember all-comparisons
      (comparison-package (E-package I F i) (E-package I G i)
        (Σ-cong-equiv-snd e) (λ j → i , p i j))

    Pi-comparison : Complete
    Pi-comparison = remember all-comparisons
      (comparison-package (Pi-package I F) (Pi-package I G)
        (equivΠCod e) (funExt p))

  -- A witness of equality between paths has its complete boundary in Code.
  higher-package : (Q : Code) (x y : El Q) (p q : x ≡ y)
                 → p ≡ q → Complete
  higher-package Q x y p q alpha = path-package (paths Q x y) p q alpha

  associative-paths : (Q : Code) {w x y z : El Q}
    (p : w ≡ x) (q : x ≡ y) (r : y ≡ z) → Complete
  associative-paths Q {w} {z = z} p q r =
    higher-package Q w z (p ∙ (q ∙ r)) ((p ∙ q) ∙ r) (assoc p q r)

  right-unit-path : (Q : Code) {x y : El Q} (p : x ≡ y) → Complete
  right-unit-path Q {x} {y} p = higher-package Q x y p (p ∙ refl) (rUnit p)

  cancellation-path : (Q : Code) {x y : El Q} (p : x ≡ y) → Complete
  cancellation-path Q {x} p = higher-package Q x x (p ∙ sym p) refl (rCancel p)

  map-package : (Q R : Code) → (El Q → El R) → Complete
  map-package Q R f = pack (maps Q R) f

  compose-maps : (Q R T : Code) → (El Q → El R) → (El R → El T) → Complete
  compose-maps Q R T f g =
    pack (retain (maps Q R) f (retain (maps R T) g (maps Q T))) (λ x → g (f x))

  lift-paths : (Q R : Code) (e : El Q ≃ El R) (x y : El Q) → Complete
  lift-paths Q R e x y = pack
    (retain (equivalences Q R) e
      (equivalences (paths Q x y) (paths R (equivFun e x) (equivFun e y))))
    (Witness.pathLift e)

  -- Package-valued dependent distributivity; each leaf retains its input.
  module Distribution (I : Type ℓ) (J : I → Type ℓ)
                      (F : (i : I) → J i → Complete) where
    left : Code
    left = Pi I (λ i → E (J i) (λ j → retained (F i j)))

    right : Code
    right = E ((i : I) → J i)
              (λ f → Pi I (λ i → retained (F i (f i))))

    law : Iso (El left) (El right)
    Iso.fun law v = (λ i → fst (v i)) , (λ i → snd (v i))
    Iso.inv law (f , w) i = f i , w i
    Iso.rightInv law _ = refl
    Iso.leftInv law _ = refl

    -- The full generating comparison is itself an admissible Complete.
    generator : (v : El left) → Complete
    generator v = comparison-package
      (pack left v) (pack right (Iso.fun law v)) (isoToEquiv law) refl

-- Reifying a whole package (including its syntax and prior witnesses)
-- uses the next universe. This makes the full package, not just El, the
-- input of subsequent E/Pi or path constructions.
reify : {ℓ : Level} → Universe.Complete ℓ → Universe.Complete (ℓ-suc ℓ)
reify {ℓ} q = Universe.pack (Universe.atom (Universe.Complete ℓ)) q

reify-retains-all : {ℓ : Level} (q : Universe.Complete ℓ)
  → Universe.value (reify q) ≡ q
reify-retains-all q = refl

-- Strict whole-package operations: the resolved entries themselves are
-- complete previous packages, not merely their El projections.
E-whole : {ℓ : Level} (I : Type ℓ) → (I → Universe.Complete ℓ)
        → I → Universe.Complete (ℓ-suc ℓ)
E-whole {ℓ} I F i = Universe.E-package (ℓ-suc ℓ)
  (Lift {j = ℓ-suc ℓ} I) (λ j → reify (F (lower j))) (lift i)

Pi-whole : {ℓ : Level} (I : Type ℓ) → (I → Universe.Complete ℓ)
         → Universe.Complete (ℓ-suc ℓ)
Pi-whole {ℓ} I F = Universe.Pi-package (ℓ-suc ℓ)
  (Lift {j = ℓ-suc ℓ} I) (λ j → reify (F (lower j)))

E-whole-entry : {ℓ : Level} (I : Type ℓ) (F : I → Universe.Complete ℓ) (i : I)
  → snd (Universe.value (E-whole I F i)) ≡ F i
E-whole-entry I F i = refl

Pi-whole-entry : {ℓ : Level} (I : Type ℓ) (F : I → Universe.Complete ℓ) (i : I)
  → Universe.value (Pi-whole I F) (lift i) ≡ F i
Pi-whole-entry I F i = refl

whole-path : {ℓ : Level} (a b : Universe.Complete ℓ) → a ≡ b
           → Universe.Complete (ℓ-suc ℓ)
whole-path {ℓ} a b p = Universe.path-package (ℓ-suc ℓ) (Universe.atom (Universe.Complete ℓ)) a b p

whole-higher : {ℓ : Level} (a b : Universe.Complete ℓ) (p q : a ≡ b)
             → p ≡ q → Universe.Complete (ℓ-suc ℓ)
whole-higher {ℓ} a b p q alpha =
  Universe.higher-package (ℓ-suc ℓ) (Universe.atom (Universe.Complete ℓ)) a b p q alpha
