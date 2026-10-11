{-# OPTIONS --safe --cubical --guardedness #-}
module TickMachinPiCandidate where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyAddition using (addRegular)
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (negateRegular; -completion_)
open import TickMachinInputs public

atanFifth atan239th : MetricCompletionCandidate
atanFifth = SQ.[ atanFifthRegular ]
atan239th = SQ.[ atan239thRegular ]

-- Integer scaling by addition avoids a needlessly expensive radius search
-- on closed rational presentations. four(four(x)) is exactly 16*x.
fourRegular : RegularCauchy → RegularCauchy
fourRegular x = addRegular (addRegular x x) (addRegular x x)

fourCompletion : MetricCompletionCandidate → MetricCompletionCandidate
fourCompletion x = (x +completion x) +completion (x +completion x)

machinPiRegular : RegularCauchy
machinPiRegular = addRegular (fourRegular (fourRegular atanFifthRegular))
  (negateRegular (fourRegular atan239thRegular))

-- Construction only: no inverse-trig law or identification with pi is
-- assumed. Those and the operational endpoint laws remain obligations.
machinPi : MetricCompletionCandidate
machinPi = SQ.[ machinPiRegular ]

abstract
  four-regular-class : (x : RegularCauchy) → SQ.[ fourRegular x ] ≡ fourCompletion SQ.[ x ]
  four-regular-class x = refl

  machin-pi-formula : machinPi ≡
    fourCompletion (fourCompletion atanFifth) +completion (-completion (fourCompletion atan239th))
  machin-pi-formula = cong₂ _+completion_
    (four-regular-class (fourRegular atanFifthRegular) ∙ cong fourCompletion (four-regular-class atanFifthRegular))
    (cong -completion_ (four-regular-class atan239thRegular))
