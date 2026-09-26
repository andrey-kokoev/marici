{-# OPTIONS --safe --cubical --guardedness #-}
module ComparisonTensorSewing where
open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing.Base
open import Cubical.Tactics.CommRingSolver
import ComparisonMixedResidual as Mixed
import RetainedComparisonSeries as Source
import BoundaryGeneratedQuestions as B

module Algebra (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  module M = Mixed.Algebra R
  open M using (Scalar; Field; JointField; difference; product-probe; sum-points; sum-pairs; energy2)
  norm pairing : Field → Scalar
  norm phi = sum-points (λ x → phi x · phi x)
  pairing phi = sum-points (λ x → phi x · Source.pull B.swap-filler phi x)
  joint-norm joint-overlap : JointField → Scalar
  joint-norm h = sum-pairs (λ xy → h xy · h xy)
  joint-overlap h = sum-pairs (λ xy → h xy · h (Mixed.both xy))
  norm-product : (phi psi : Field)
    → joint-norm (product-probe phi psi) ≡ norm phi · norm psi
  norm-product phi psi = solve! R
  overlap-product : (phi psi : Field)
    → joint-overlap (product-probe phi psi) ≡ pairing phi · pairing psi
  overlap-product phi psi = solve! R
  energy-overlap : (phi : Field) → energy2 phi ≡ difference (norm phi) (pairing phi)
  energy-overlap phi = solve! R

  -- After dividing by nonzero norms in a suitable field, c=1-2e.
  -- These formal ring identities do not postulate division or a logarithm.
  two : Scalar
  two = 1r + 1r
  character : Scalar → Scalar
  character e = 1r + (- (two · e))
  sew : Scalar → Scalar → Scalar
  sew e f = e + f + (- ((two · e) · f))
  character-sews : (e f : Scalar) → character (sew e f) ≡ character e · character f
  character-sews e f = solve! R
  sew-associative : (e f g : Scalar) → sew (sew e f) g ≡ sew e (sew f g)
  sew-associative e f g = solve! R
  sew-unit : (e : Scalar) → sew e 0r ≡ e
  sew-unit e = solve! R

  -- The quartic-in-field truncation is only quadratic in normalized energy.
  truncated : Scalar → Scalar
  truncated e = e + e · e
  truncation-defect : (e f : Scalar)
    → difference (truncated (sew e f)) (truncated e + truncated f)
      ≡ (((two · two) · e) · f) · ((e · f) + (- e) + (- f))
  truncation-defect e f = solve! R
