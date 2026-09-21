{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureSelectedHigherAdmission where

open import Cubical.Foundations.Prelude hiding (Lift)
open import Cubical.Data.Unit
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Sigma.Base using (_×_)
open import ClosureAllDimensionalCutCoherence using (module ContractibleTower)

-- Unlike ContractibleTower, the target has NO contraction assumption.
module UnrestrictedTower (T : Type) where
  mutual
    Boundary : ℕ → Type
    Boundary zero = Unit
    Boundary (suc n) = Σ[ b ∈ Boundary n ] (Cell n b × Cell n b)

    Cell : (n : ℕ) → Boundary n → Type
    Cell zero _ = T
    Cell (suc n) (b , (x , y)) = x ≡ y

module Projection (T : Type) (contract : isContr T) (U : Type) (forget : T → U) where
  module Source = ContractibleTower T contract
  module Target = UnrestrictedTower U

  mutual
    forgetBoundary : (n : ℕ) → Source.Boundary n → Target.Boundary n
    forgetBoundary zero _ = tt
    forgetBoundary (suc n) (b , (x , y)) =
      forgetBoundary n b , (forgetCell n b x , forgetCell n b y)

    forgetCell : (n : ℕ) (b : Source.Boundary n) →
      Source.Cell n b → Target.Cell n (forgetBoundary n b)
    forgetCell zero _ = forget
    forgetCell (suc n) (b , (x , y)) = cong (forgetCell n b)

  generated : (n : ℕ) (b : Source.Boundary n) → Target.Cell n (forgetBoundary n b)
  generated n b = forgetCell n b (Source.fillCell n b)

  -- Boundaries are already lifted. The selected top cell is not replaced.
  Lift : (n : ℕ) (b : Source.Boundary n) → Target.Cell n (forgetBoundary n b) → Type
  Lift n b h = Σ[ α ∈ Source.Cell n b ] (forgetCell n b α ≡ h)

  fromGenerated : (n : ℕ) (b : Source.Boundary n)
    (h : Target.Cell n (forgetBoundary n b)) → h ≡ generated n b → Lift n b h
  fromGenerated n b h equality = Source.fillCell n b , sym equality

  toGenerated : (n : ℕ) (b : Source.Boundary n)
    (h : Target.Cell n (forgetBoundary n b)) → Lift n b h → h ≡ generated n b
  toGenerated n b h (α , equality) = sym equality
    ∙ cong (forgetCell n b)
      (isContr→isProp (Source.allCellsContractible n b) α (Source.fillCell n b))

  -- These implications are an exact existence criterion, NOT a claim
  -- that Lift is contractible. Its projection equality is extra data.

module Fiber {X B : Type} (post : X → B) (target : B)
  (contract : isContr (Σ[ x ∈ X ] (post x ≡ target))) where
  Presentation : Type
  Presentation = Σ[ x ∈ X ] (post x ≡ target)

  module Cells = Projection Presentation contract X fst

  module Between (p q : Presentation) where
    boundary : Cells.Source.Boundary 1
    boundary = tt , (p , q)

    -- This is precisely the missing higher normalization square.
    Coherence : fst p ≡ fst q → Type
    Coherence h = PathP (λ i → post (h i) ≡ target) (snd p) (snd q)

    admit : (h : fst p ≡ fst q) → Coherence h → p ≡ q
    admit h coherence i = h i , coherence i

    extract : (α : p ≡ q) → Coherence (cong fst α)
    extract α i = snd (α i)

    retainsSelected : (h : fst p ≡ fst q) (coherence : Coherence h) →
      cong fst (admit h coherence) ≡ h
    retainsSelected h coherence = refl

    toLift : (h : fst p ≡ fst q) → Coherence h → Cells.Lift 1 boundary h
    toLift h coherence = admit h coherence , refl

    fromLift : (h : fst p ≡ fst q) → Cells.Lift 1 boundary h → Coherence h
    fromLift h (α , equality) = subst Coherence equality (extract α)

    toGenerated : (h : fst p ≡ fst q) → Coherence h → h ≡ Cells.generated 1 boundary
    toGenerated h coherence = Cells.toGenerated 1 boundary h (toLift h coherence)

    fromGenerated : (h : fst p ≡ fst q) → h ≡ Cells.generated 1 boundary → Coherence h
    fromGenerated h equality = fromLift h (Cells.fromGenerated 1 boundary h equality)
