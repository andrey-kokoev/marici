{-# OPTIONS --safe --cubical --guardedness #-}
module BoundaryExtensionFibres where

open import Cubical.Foundations.Prelude

-- No truncation, setness, or selection of a boundary is assumed.
Extension : {ℓ ℓ' : Level} {Interior : Type ℓ} {Boundary : Type ℓ'}
  → (Interior → Boundary) → Boundary → Type (ℓ-max ℓ ℓ')
Extension {Interior = Interior} restrict b =
  Σ Interior (λ i → restrict i ≡ b)

UniqueExtensions : {ℓ ℓ' : Level} {I : Type ℓ} {B : Type ℓ'}
  → (I → B) → Type (ℓ-max ℓ ℓ')
UniqueExtensions {B = B} restrict = (b : B) → isContr (Extension restrict b)

-- Coherent patch agreement: a path, not definitional equality.
OverlapAssembly : {ℓ : Level} {A B O : Type ℓ}
  → (A → O) → (B → O) → Type ℓ
OverlapAssembly {A = A} {B = B} left right =
  Σ A (λ a → Σ B (λ b → left a ≡ right b))

-- Identity restriction extends every fixed boundary uniquely.
identityExtensions : {ℓ : Level} {B : Type ℓ}
  → UniqueExtensions (λ (b : B) → b)
identityExtensions b = (b , refl) , λ { (x , p) i →
  p (~ i) , (λ j → p (~ i ∨ j)) }

-- Regression objects: these are abstract markings, not physical coefficients.
data Marking : Type where
  first second : Marking

data UnitReadout : Type where
  unit : UnitReadout

data Impossible : Type where

separatingFamily : Marking → Type
separatingFamily first = UnitReadout
separatingFamily second = Impossible

first≠second : first ≡ second → Impossible
first≠second p = transport (cong separatingFamily p) unit

readout : Marking → UnitReadout
readout _ = unit

section : UnitReadout → Marking
section _ = first

readout-section : (u : UnitReadout) → readout (section u) ≡ u
readout-section unit = refl

-- A split readout does not retain all markings.
section-not-inverse : ((m : Marking) → section (readout m) ≡ m) → Impossible
section-not-inverse inverse = first≠second (inverse second)

firstNormalized secondNormalized : Extension readout unit
firstNormalized = first , refl
secondNormalized = second , refl

normalized-markings-distinct : firstNormalized ≡ secondNormalized → Impossible
normalized-markings-distinct p = first≠second (cong fst p)

normalized-fibre-not-contractible : isContr (Extension readout unit) → Impossible
normalized-fibre-not-contractible (center , contraction) =
  normalized-markings-distinct
    (sym (contraction firstNormalized) ∙ contraction secondNormalized)

-- Each boundary extends uniquely, although normalization does not select one.
fixed-boundary-extensions : UniqueExtensions (λ (m : Marking) → m)
fixed-boundary-extensions = identityExtensions

-- Formal counterexample to promoting unique extension into unique selection.
unique-extension-does-not-select :
  (UniqueExtensions (λ (m : Marking) → m)
    → isContr (Extension readout unit)) → Impossible
unique-extension-does-not-select promote =
  normalized-fibre-not-contractible (promote fixed-boundary-extensions)

-- An equivalence certificate must justify every fibre, not just a section.
record FaithfulReadout {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'}
  (r : A → B) : Type (ℓ-max ℓ ℓ') where
  field
    contractibleFibres : UniqueExtensions r

split-readout-not-equivalence : FaithfulReadout readout → Impossible
split-readout-not-equivalence certificate =
  normalized-fibre-not-contractible
    (FaithfulReadout.contractibleFibres certificate unit)
