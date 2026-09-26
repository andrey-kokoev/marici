{-# OPTIONS --safe --cubical --guardedness #-}
module FibrationSigmaPiBridge where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism hiding (iso)
open import Cubical.Foundations.Univalence using (ua; pathToEquiv)
open import Cubical.Foundations.HLevels using (isPropΠ; isContr→isProp)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Unit.Properties using (isPropUnit)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Relation.Nullary.Base using (Stable; ¬_)
import TableFibrationCycle as Table
import WholePackageSigmaPi as Old
import NandConstructions as Nand
import QBooleanity as Boolean

-- The universe-polymorphic display-map construction underlying the table view.
module Family {ℓ : Level} (I : Type ℓ) (F : I → Type ℓ) where
  Rows : Type ℓ
  Rows = Σ I F
  Fiber : I → Type ℓ
  Fiber i = Σ Rows (λ r → fst r ≡ i)
  Total : Type ℓ
  Total = Σ I Fiber
  Sections : Type ℓ
  Sections = (i : I) → Fiber i

  total-iso : Iso Rows Total
  Iso.fun total-iso (i , x) = i , (i , x) , refl
  Iso.inv total-iso (i , r , p) = r
  Iso.leftInv total-iso r = refl
  Iso.rightInv total-iso (i , r , p) k = p k , r , (λ j → p (k ∧ j))

  fiber-iso : (i : I) → Iso (F i) (Fiber i)
  Iso.fun (fiber-iso i) x = (i , x) , refl
  Iso.inv (fiber-iso i) ((j , x) , p) = transport (cong F p) x
  Iso.leftInv (fiber-iso i) x = transportRefl x
  Iso.rightInv (fiber-iso i) ((j , x) , p) k =
    (p (~ k) , transport-filler (cong F p) x (~ k)) , (λ l → p ((~ k) ∨ l))

  sections-iso : Iso ((i : I) → F i) Sections
  Iso.fun sections-iso f i = Iso.fun (fiber-iso i) (f i)
  Iso.inv sections-iso s i = Iso.inv (fiber-iso i) (s i)
  Iso.leftInv sections-iso f = funExt (λ i → Iso.leftInv (fiber-iso i) (f i))
  Iso.rightInv sections-iso s = funExt (λ i → Iso.rightInv (fiber-iso i) (s i))

-- Actual three-column incidence table. The target is a typed row address;
-- its use guarantees unique endpoint pairs without truncating values.
incidence : (I : Type) (F : I → Type) → Table.Table (Σ I F) I (Σ I F)
Table.Table.Rows (incidence I F) = Σ I F
Table.Table.label (incidence I F) r = r
Table.Table.from (incidence I F) = fst
Table.Table.to (incidence I F) r = r
incidence-unique : (I : Type) (F : I → Type) → Table.UniqueEndpoints (incidence I F)
incidence-unique I F x y ps pt = pt

module Codes (I : Type) (F : I → Old.Universe.Code ℓ-zero) where
  open Old.Universe ℓ-zero
  module D = Family I (λ i → El (F i))
  E-equivalence : El (E I F) ≃ D.Total
  E-equivalence = isoToEquiv D.total-iso
  P-equivalence : El (Pi I F) ≃ D.Sections
  P-equivalence = isoToEquiv D.sections-iso

-- The old selected E/P values map to the canonical row and section.
module Selected (I : Type) (F : I → Old.Universe.Complete ℓ-zero) where
  open Old.Universe ℓ-zero
  module D = Family I (λ i → El (expression (F i)))
  E-selected : (i : I) → Iso.fun D.total-iso (value (E-package I F i))
    ≡ (i , (i , value (F i)) , refl)
  E-selected i = refl
  P-selected : Iso.fun D.sections-iso (value (Pi-package I F))
    ≡ (λ i → ((i , value (F i)) , refl))
  P-selected = refl

-- Simply decoding a regrouped table as its rows does NOT give old Pi.
row-type-not-product : ¬ ((Bool × Unit) ≃ (Bool → Unit))
row-type-not-product e = false≢true (cong fst
  (sym (Iso.leftInv iso (false , tt))
    ∙ cong (Iso.inv iso) (isPropΠ (λ _ → isPropUnit)
        (Iso.fun iso (false , tt)) (Iso.fun iso (true , tt)))
    ∙ Iso.leftInv iso (true , tt)))
  where iso = equivToIso e

-- Nor does selecting sections of the OTHER endpoint automatically fix it.
identity-sections-contractible : {E : Type} → isContr ((r : E) → Σ E (λ e → e ≡ r))
fst identity-sections-contractible r = r , refl
snd identity-sections-contractible h = funExt λ r k →
  snd (h r) (~ k) , (λ j → snd (h r) ((~ k) ∨ j))
wrong-endpoint-sections : ¬ ((Bool → Bool) ≃ ((r : Bool × Bool) → Σ (Bool × Bool) (λ e → e ≡ r)))
wrong-endpoint-sections e = false≢true (cong (λ f → f false)
  (sym (Iso.leftInv iso (λ _ → false))
    ∙ cong (Iso.inv iso) (isContr→isProp identity-sections-contractible
        (Iso.fun iso (λ _ → false)) (Iso.fun iso (λ _ → true)))
    ∙ Iso.leftInv iso (λ _ → true)))
  where iso = equivToIso e

-- Empty rows do not determine the active index domain. This distinction is
-- essential to NAND: zero indices give a section; an empty fiber at an
-- existing index prevents one.
empty-row-equivalence : Family.Rows ⊥ (λ ()) ≃ Family.Rows Unit (λ _ → ⊥)
empty-row-equivalence = isoToEquiv record
  { fun = λ { (() , x) }
  ; inv = λ { (u , ()) }
  ; rightInv = λ { (u , ()) }
  ; leftInv = λ { (() , x) } }
empty-sections-distinct : ¬ (Family.Sections ⊥ (λ ()) ≃ Family.Sections Unit (λ _ → ⊥))
empty-sections-distinct e = snd (fst (equivFun e (λ ()) tt))

-- Re-run the actual NAND/Wolfram construction through section semantics.
TableN : Type → Type → Type
TableN A B = Family.Sections (A × B) (λ _ → ⊥)
nand-equivalence : (A B : Type) → TableN A B ≃ Old.Universe.El ℓ-zero (Nand.nandCode A B)
nand-equivalence A B = isoToEquiv (invIso (Family.sections-iso (A × B) (λ _ → ⊥)))
nand-operation-path : TableN ≡ Boolean.N
nand-operation-path = funExt λ A → funExt λ B → ua (nand-equivalence A B)
Word : (Type → Type → Type) → Type → Type → Type → Type
Word n A B C = n (n (n A B) C) (n A (n (n A C) A))
table-word-path : (A B C : Type) → Word TableN A B C ≡ Boolean.W A B C
table-word-path A B C = cong (λ n → Word n A B C) nand-operation-path
wolfram-table-double : (A B C : Type) → Word TableN A B C ≃ Boolean.D C
wolfram-table-double A B C = compEquiv (pathToEquiv (table-word-path A B C)) (Boolean.wolfram-double A B C)
wolfram-table-stable : (A B C : Type) → isProp C → Stable C → Word TableN A B C ≃ C
wolfram-table-stable A B C prop stable = compEquiv
  (pathToEquiv (table-word-path A B C)) (Boolean.wolfram-stable A B C prop stable)
