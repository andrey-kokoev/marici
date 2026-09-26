{-# OPTIONS --safe --cubical --guardedness #-}
module SourceAnchoredTidalOverlap where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc; _·_)
import NewtonianTidalKernel as K
import NativeTidalTableReadout as NT

-- New explicitly declared source data; NOT the owner's fixed a,b seed policy.
x-axis z-axis : K.Vec
x-axis K.x = pos 1
x-axis K.y = pos 0
x-axis K.z = pos 0
z-axis K.x = pos 0
z-axis K.y = pos 0
z-axis K.z = pos 1
source-x source-z : K.Source
source-x = K.source (pos 36) (pos 12) (pos 1) x-axis
source-z = K.source (pos 18) (pos 12) (pos 1) z-axis
D : ℤ
D = pos 1728
x-unit : K.normSquared x-axis ≡ pos 1
x-unit = refl
z-unit : K.normSquared z-axis ≡ pos 1
z-unit = refl
x-reciprocal : K.reciprocalCheck source-x ≡ D
x-reciprocal = refl
z-reciprocal : K.reciprocalCheck source-z ≡ D
z-reciprocal = refl

-- The common E is diag(-1/32,+1/32,0), represented over denominator D.
common : K.Tensor
common K.x K.x = negsuc 53
common K.y K.y = pos 54
common _ _ = pos 0
point-tensor : K.Tensor
point-tensor = K.tidal source-x source-z
point-component : (i j : K.Axis) → point-tensor i j ≡ common i j
point-component K.x K.x = refl
point-component K.x K.y = refl
point-component K.x K.z = refl
point-component K.y K.x = refl
point-component K.y K.y = refl
point-component K.y K.z = refl
point-component K.z K.x = refl
point-component K.z K.y = refl
point-component K.z K.z = refl
point-agrees : point-tensor ≡ common
point-agrees = funExt (λ i → funExt (point-component i))
negative-unit : pos 32 · common K.x K.x ≡ negsuc 1727
negative-unit = refl
positive-unit : pos 32 · common K.y K.y ≡ D
positive-unit = refl

-- Actual independent native second-jet arithmetic, not a readout after decode.
native-jet : NT.JetTable
native-jet = NT.add (NT.source-jet source-x) (NT.source-jet source-z)
native-tensor : K.Tensor
native-tensor = NT.read-tensor native-jet
native-component : (i j : K.Axis) → native-tensor i j ≡ pos 8 · common i j
native-component K.x K.x = refl
native-component K.x K.y = refl
native-component K.x K.z = refl
native-component K.y K.x = refl
native-component K.y K.y = refl
native-component K.y K.z = refl
native-component K.z K.x = refl
native-component K.z K.y = refl
native-component K.z K.z = refl
native-agrees : native-tensor ≡ (λ i j → pos 8 · common i j)
native-agrees = funExt (λ i → funExt (native-component i))

-- Physical potential jet over D, calculated analytically from the two masses.
-- The lower entries are not confused with NT's per-source normalized u-jets.
physical-gradient : K.Vec
physical-gradient K.x = negsuc 431
physical-gradient K.y = pos 0
physical-gradient K.z = negsuc 215
cancel-gradient : K.Vec
cancel-gradient K.x = pos 432
cancel-gradient K.y = pos 0
cancel-gradient K.z = pos 216
physical-jet : K.Jet
physical-jet = K.jet (negsuc 7775) physical-gradient point-tensor
freefall-jet : K.Jet
freefall-jet = K.addAffine (pos 7776) cancel-gradient physical-jet
common-jet : K.Jet
common-jet = K.jet (pos 0) (λ _ → pos 0) common
value-zero : K.potential freefall-jet ≡ pos 0
value-zero = refl
gradient-zero : K.gradient freefall-jet ≡ (λ _ → pos 0)
gradient-zero = funExt λ { K.x → refl ; K.y → refl ; K.z → refl }
local-jet-agrees : freefall-jet ≡ common-jet
local-jet-agrees i = K.jet (value-zero i) (gradient-zero i) (point-agrees i)
