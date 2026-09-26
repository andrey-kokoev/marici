{-# OPTIONS --safe --cubical --guardedness #-}
module ComparisonMixedResidual where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool.Base using (false; true)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Algebra.CommRing.Base
open import Cubical.Tactics.CommRingSolver
import BoundaryGeneratedQuestions as B
import ObserverCoherenceCube as Observer
import RetainedComparisonSeries as Source

-- Use the existing independent-expansion construction, with its actual swap.
module Cells = Observer.Geometry Source.Point Source.Point (fst B.swap-filler)
Pair = Source.Point × Source.Point
left right both : Pair → Pair
left = Cells.expandLeft
right = Cells.expandRight
both = Cells.run Cells.leftFirst
routes-agree : both ≡ Cells.run Cells.rightFirst
routes-agree = Cells.route-homotopy
copy : Source.Point → Pair
copy x = x , x
copy-compatible : (x : Source.Point)
  → both (copy x) ≡ copy (equivFun (fst B.swap-filler) x)
copy-compatible (x , y) = refl

module Algebra (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  Scalar = fst R
  Field = Source.Point → Scalar
  JointField = Pair → Scalar
  difference : Scalar → Scalar → Scalar
  difference x y = x + (- y)
  residual : Field → Field
  residual phi x = difference (phi x) (Source.pull B.swap-filler phi x)
  residual-left residual-right residual-both : JointField → JointField
  residual-left h x = difference (h x) (h (left x))
  residual-right h x = difference (h x) (h (right x))
  residual-both h x = difference (h x) (h (both x))
  mixed : JointField → JointField
  mixed h = residual-left (residual-right h)

  -- Nonzero mixed composition defect is NOT the route commutator.
  composition-defect : (h : JointField) (x y : Source.Point)
    → difference (residual-left h (x , y) + residual-right h (x , y))
        (residual-both h (x , y)) ≡ mixed h (x , y)
  composition-defect h x y = solve! R
  mixed-order : (h : JointField) (x y : Source.Point)
    → mixed h (x , y) ≡ residual-right (residual-left h) (x , y)
  mixed-order h x y = solve! R

  -- Product of probe VALUES is an explicit readout choice, not source copying.
  product-probe : Field → Field → JointField
  product-probe phi psi (x , y) = phi x · psi y
  mixed-factor : (phi psi : Field) (x y : Source.Point)
    → mixed (product-probe phi psi) (x , y) ≡ residual phi x · residual psi y
  mixed-factor phi psi x y = solve! R
  sum-points : Field → Scalar
  sum-points f = f (false , false) + f (false , true) + f (true , false) + f (true , true)
  sum-pairs : JointField → Scalar
  sum-pairs h = sum-points (λ x → sum-points (λ y → h (x , y)))
  energy2 : Field → Scalar
  energy2 phi = sum-points (λ x → phi x · residual phi x)
  energy4 : Field → Scalar
  energy4 phi = sum-pairs (λ xy → product-probe phi phi xy · mixed (product-probe phi phi) xy)
  contrast : Field → Scalar
  contrast phi = difference (phi (false , true)) (phi (true , false))
  quadratic-numerator : (phi : Field) → energy2 phi ≡ contrast phi · contrast phi
  quadratic-numerator phi = solve! R
  quartic-numerator : (phi : Field)
    → energy4 phi ≡ (contrast phi · contrast phi) · (contrast phi · contrast phi)
  quartic-numerator phi = solve! R
  energy-factor : (phi : Field) → energy4 phi ≡ energy2 phi · energy2 phi
  energy-factor phi = solve! R

-- With an inverse of 2, half these numerators gives the counting-pairing
-- action. No physical diagonal-state preparation or interaction coefficient
-- is selected by these polynomial identities.
