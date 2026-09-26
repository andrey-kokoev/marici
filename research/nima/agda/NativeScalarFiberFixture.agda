{-# OPTIONS --safe --cubical --guardedness #-}
module NativeScalarFiberFixture where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc; _+_; _-_; _·_)
open import Cubical.Data.List.Base using (List; []; _∷_; map)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (true)
import TableFibrationCycle as Kernel
import FiniteFiberAmplitude as Fiber
import ScalarSixKernel as K
import ScalarSixFixture as F
import ScalarSixCertificate as Old

-- A native ten-row channel table, evaluated from the actual source momenta.
-- Source data and conventions are shared; the old square/amplitude functions
-- are used only in comparison statements below, not in the native evaluator.
data Channel : Type where
  c12 c13 c14 c15 c23 c24 c25 c34 c35 c45 : Channel
enumeration : List Channel
enumeration = c12 ∷ c13 ∷ c14 ∷ c15 ∷ c23 ∷ c24 ∷ c25 ∷ c34 ∷ c35 ∷ c45 ∷ []
attachment : Channel → K.Pair
attachment c12 = K.pair K.l1 K.l2
attachment c13 = K.pair K.l1 K.l3
attachment c14 = K.pair K.l1 K.l4
attachment c15 = K.pair K.l1 K.l5
attachment c23 = K.pair K.l2 K.l3
attachment c24 = K.pair K.l2 K.l4
attachment c25 = K.pair K.l2 K.l5
attachment c34 = K.pair K.l3 K.l4
attachment c35 = K.pair K.l3 K.l5
attachment c45 = K.pair K.l4 K.l5
sum-component : (K.Momentum → ℤ) → Channel → ℤ
sum-component component c = component (F.momenta K.l0) +
  (component (F.momenta (K.Pair.left (attachment c))) + component (F.momenta (K.Pair.right (attachment c))))
channel-denominator : Channel → ℤ
channel-denominator c = let
    e = sum-component K.Momentum.e c
    x = sum-component K.Momentum.x c
    y = sum-component K.Momentum.y c
    z = sum-component K.Momentum.z c
  in e · e - x · x - y · y - z · z
reciprocal-units : ℤ → ℤ
reciprocal-units (pos 8) = pos 3
reciprocal-units (negsuc 3) = negsuc 5
reciprocal-units (negsuc 5) = negsuc 3
reciprocal-units _ = pos 0
weight : Channel → ℤ
weight c = (pos 0 - F.couplingNumerator · F.couplingNumerator) · reciprocal-units (channel-denominator c)
channel-table : Kernel.Table ℤ Unit Channel
channel-table = Kernel.table Channel weight (λ _ → tt) (λ c → c)
unique : Kernel.UniqueEndpoints channel-table
unique a b from-eq to-eq = to-eq
module Sum = Fiber.Weighted ℤ (pos 0) _+_
native-numerator : ℤ
native-numerator = Sum.amplitude channel-table enumeration (λ _ → true) (λ z → z)
common-denominator : ℤ
common-denominator = (F.couplingDenominator · F.couplingDenominator) · pos 24

-- Exhaustive agreement with the actual independently generated old census.
channel-census-commutes : map attachment enumeration ≡ K.channels
channel-census-commutes = refl
denominators-commute : map channel-denominator enumeration ≡ K.denominators F.momenta
denominators-commute = refl
reciprocal-valid : (c : Channel) → channel-denominator c · reciprocal-units (channel-denominator c) ≡ pos 24
reciprocal-valid c12 = refl
reciprocal-valid c13 = refl
reciprocal-valid c14 = refl
reciprocal-valid c15 = refl
reciprocal-valid c23 = refl
reciprocal-valid c24 = refl
reciprocal-valid c25 = refl
reciprocal-valid c34 = refl
reciprocal-valid c35 = refl
reciprocal-valid c45 = refl
numerator-commutes : native-numerator ≡ Old.numerator
numerator-commutes = refl
denominator-commutes : common-denominator ≡ Old.denominator
denominator-commutes = refl
computed : native-numerator ≡ pos 144
computed = refl
export-agrees : native-numerator · F.exportedDenominator ≡ F.exportedNumerator · common-denominator
export-agrees = refl
