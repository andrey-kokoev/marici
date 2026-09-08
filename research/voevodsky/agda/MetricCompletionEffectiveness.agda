{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module MetricCompletionEffectiveness where

open import Cubical.Foundations.Prelude
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import CauchyMetricEquivalence

quotientPathToMetric : (x y : RegularCauchy) →
  Path MetricCompletionCandidate SQ.[ x ] SQ.[ y ] → x ≈metric y
quotientPathToMetric x y = SQ.effective ≈metric-isProp ≈metric-isEquivRel x y
