{-# OPTIONS --safe --cubical --guardedness #-}
module NewtonianTidalCertificate where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (idEquiv)
open import Cubical.Data.Int.Base using (pos; negsuc; _+_)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Sigma.Base using (_×_)
open import NewtonianTidalKernel
open import NewtonianTidalFixture
import WholePackageSigmaPi as Whole
import WholePackageResolution as RRC

-- Pins the live fixture and the common-denominator interpretation.
a-fixed : a ≡ source (pos 2) (pos 3) (pos 64) (delta x)
a-fixed = cong (source (pos 2) (pos 3) (pos 64))
  (funExt λ { x → refl ; y → refl ; z → refl })
b-fixed : b ≡ source (pos 1) (pos 4) (pos 27) (delta y)
b-fixed = cong (source (pos 1) (pos 4) (pos 27))
  (funExt λ { x → refl ; y → refl ; z → refl })
radii-checked : (reciprocalCheck a ≡ denominator) × (reciprocalCheck b ≡ denominator)
radii-checked = refl , refl
directions-checked : (normSquared (direction a) ≡ pos 1) × (normSquared (direction b) ≡ pos 1)
directions-checked = refl , refl

component-check : (i j : Axis) → tidal a b i j ≡ exportedTensor i j
component-check x x = refl
component-check x y = refl
component-check x z = refl
component-check y x = refl
component-check y y = refl
component-check y z = refl
component-check z x = refl
component-check z y = refl
component-check z z = refl
calculation : tidal a b ≡ exportedTensor
calculation = funExt (λ i → funExt (component-check i))
vacuum-trace : tidal a b x x + tidal a b y y + tidal a b z z ≡ pos 0
vacuum-trace = refl
x-separation-readout : relativeAcceleration (tidal a b) (delta x) x ≡ pos 229
x-separation-readout = refl

shifted : Jet
shifted = addAffine (pos 7) (delta y) exportedJet
tidalComparison : tidal a b ≡ hessian shifted
tidalComparison = calculation

-- Actual existing RRC generators, not a parallel invented history type.
-- All calculations are proved ABOVE. RRC retains them; it does not invent
-- Newton's law or synthesize this proof from the bare masses.
open Whole.Universe ℓ-zero
open RRC.Generators ℓ-zero

before after : Complete
before = pack (atom Tensor) (tidal a b)
after = pack (atom Tensor) (hessian shifted)

record Evidence : Type where
  constructor evidence
  field
    radii : (reciprocalCheck a ≡ denominator) × (reciprocalCheck b ≡ denominator)
    unitDirections : (normSquared (direction a) ≡ pos 1) × (normSquared (direction b) ≡ pos 1)
    tensorCalculation : tidal a b ≡ exportedTensor
    affineLaw : (c : _) (v : Vec) (j : Jet) → hessian (addAffine c v j) ≡ hessian j

sourcePackage evidencePackage : Complete
sourcePackage = pack (atom (Source × Source)) (a , b)
evidencePackage = pack (atom Evidence)
  (evidence radii-checked directions-checked calculation affine-invariance)

-- Four explicit admitted seeds, not arbitrary packages as seeds.
data Seeds : Complete → Type₁ where
  source-seed : Seeds sourcePackage
  evidence-seed : Seeds evidencePackage
  before-seed : Seeds before
  after-seed : Seeds after

comparisonRule : Rule
comparisonRule = compare-rule before after (idEquiv Tensor) tidalComparison
comparisonHistory : Resolve Seeds (output comparisonRule)
comparisonHistory = apply comparisonRule λ { (lift true) → seed before-seed ; (lift false) → seed after-seed }

family : Bool → Complete
family true = sourcePackage
family false = evidencePackage
inputHistory : Resolve Seeds (Pi-package Bool family)
inputHistory = apply (Pi-rule Bool family)
  λ { (lift true) → seed source-seed ; (lift false) → seed evidence-seed }

wholeFamily : Bool → Complete
wholeFamily true = Pi-package Bool family
wholeFamily false = output comparisonRule
history : Resolve Seeds (Pi-package Bool wholeFamily)
history = apply (Pi-rule Bool wholeFamily)
  λ { (lift true) → inputHistory ; (lift false) → comparisonHistory }

retainedHistory : Whole.Universe.Complete (ℓ-suc ℓ-zero)
retainedHistory = reify-history history
retains-history : snd (Whole.Universe.value retainedHistory) ≡ history
retains-history = refl
