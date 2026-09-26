{-# OPTIONS --safe --cubical --guardedness #-}
module ComparisonKineticReadout where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import Cubical.Algebra.CommRing.Base
open import Cubical.Tactics.CommRingSolver
import ComparisonMixedResidual as Mixed
import ComparisonTensorSewing as Sewing
import RetainedComparisonSeries as Source
import BoundaryGeneratedQuestions as B

module Algebra (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  module M = Mixed.Algebra R
  module S = Sewing.Algebra R
  open M using (Scalar; Field; sum-points)
  open S using (two)

  -- Plane spanned by the selected-point basis vector and the swap-odd line.
  plane : Scalar → Scalar → Field
  plane a b (false , false) = a
  plane a b (false , true) = b
  plane a b (true , false) = - b
  plane a b (true , true) = 0r
  plane-stable : (a b : Scalar) (x : Source.Point)
    → Source.pull B.swap-filler (plane a b) x ≡ plane a (- b) x
  plane-stable a b (false , false) = refl
  plane-stable a b (false , true) = refl
  plane-stable a b (true , false) = solve! R
  plane-stable a b (true , true) = refl
  plane-norm : (a b : Scalar) → S.norm (plane a b) ≡ a · a + two · (b · b)
  plane-norm a b = solve! R
  plane-pairing : (a b : Scalar)
    → S.pairing (plane a b) ≡ a · a + (- (two · (b · b)))
  plane-pairing a b = solve! R
  plane-tangent-pairing : (a b c d : Scalar)
    → sum-points (λ x → plane a b x · plane c d x) ≡ a · c + two · (b · d)
  plane-tangent-pairing a b c d = solve! R

  -- Conditional quartic on-shell combination in a quadratically canonical,
  -- parity-even scalar chart: L4 = a field^2 (d field)^2 - lambda field^4/24.
  -- m denotes mass SQUARED. The kinematic interpretation is external to this
  -- generic ring identity; no Lorentz geometry or propagator is postulated here.
  three eight twenty-four : Scalar
  three = two + 1r
  eight = two · (two · two)
  twenty-four = three · eight
  effective : Scalar → Scalar → Scalar → Scalar
  effective lambda a m = lambda + (- ((eight · a) · m))
  cubic-chart-invariant : (lambda a m beta : Scalar)
    → effective (lambda + (twenty-four · m) · beta) (a + three · beta) m
      ≡ effective lambda a m
  cubic-chart-invariant lambda a m beta = solve! R
