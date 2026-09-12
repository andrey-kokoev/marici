{-# OPTIONS --safe --cubical --guardedness #-}
module BoundaryPfaffianFiniteChain where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver

module Chain {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  Carrier = fst R

  -- Three-point multiplicative chain kernel with adjacent weights x and y.
  -- Its canonical Pfaffian-cofactor residual is (y , -xy , x).
  residual₀ : Carrier → Carrier → Carrier
  residual₀ x y = y

  residual₁ : Carrier → Carrier → Carrier
  residual₁ x y = - (x · y)

  residual₂ : Carrier → Carrier → Carrier
  residual₂ x y = x

  row₀Vanishes : (x y : Carrier) →
    x · residual₁ x y + (x · y) · residual₂ x y ≡ 0r
  row₀Vanishes x y = solve! R

  row₁Vanishes : (x y : Carrier) →
    (- x) · residual₀ x y + y · residual₂ x y ≡ 0r
  row₁Vanishes x y = solve! R

  row₂Vanishes : (x y : Carrier) →
    (- (x · y)) · residual₀ x y +
      (- y) · residual₁ x y ≡ 0r
  row₂Vanishes x y = solve! R

  record ThreeChainResidual (x y : Carrier) : Type ℓ where
    field
      v₀ v₁ v₂ : Carrier
      coordinate₀ : v₀ ≡ residual₀ x y
      coordinate₁ : v₁ ≡ residual₁ x y
      coordinate₂ : v₂ ≡ residual₂ x y
      kernelRow₀ : x · v₁ + (x · y) · v₂ ≡ 0r
      kernelRow₁ : (- x) · v₀ + y · v₂ ≡ 0r
      kernelRow₂ : (- (x · y)) · v₀ + (- y) · v₁ ≡ 0r

  canonicalThreeResidual : (x y : Carrier) → ThreeChainResidual x y
  canonicalThreeResidual x y = record
    { v₀ = residual₀ x y
    ; v₁ = residual₁ x y
    ; v₂ = residual₂ x y
    ; coordinate₀ = refl
    ; coordinate₁ = refl
    ; coordinate₂ = refl
    ; kernelRow₀ = row₀Vanishes x y
    ; kernelRow₁ = row₁Vanishes x y
    ; kernelRow₂ = row₂Vanishes x y
    }

  -- Four-point Pfaffian.  The two non-adjacent matching terms cancel.
  fourChainPfaffian : Carrier → Carrier → Carrier → Carrier
  fourChainPfaffian x y z =
    x · z + (- ((x · y) · (y · z))) + (x · y · z) · y

  adjacentFourAmplitude : Carrier → Carrier → Carrier → Carrier
  adjacentFourAmplitude x y z = x · z

  fourPfaffianIsAdjacent : (x y z : Carrier) →
    fourChainPfaffian x y z ≡ adjacentFourAmplitude x y z
  fourPfaffianIsAdjacent x y z = solve! R

  -- Sewing the odd three-chain residual to a fourth singleton uses the
  -- cross-block column (xyz , yz , z).  It reconstructs the even amplitude.
  sewThreeResidualToSingleton : Carrier → Carrier → Carrier → Carrier
  sewThreeResidualToSingleton x y z =
    residual₀ x y · (x · y · z) +
    residual₁ x y · (y · z) +
    residual₂ x y · z

  oddOddSewingIsFourAmplitude : (x y z : Carrier) →
    sewThreeResidualToSingleton x y z ≡ adjacentFourAmplitude x y z
  oddOddSewingIsFourAmplitude x y z = solve! R

  -- The concrete triangle commutes: microscopic four-point Pfaffian and
  -- residual-to-singleton sewing give the same certificate.
  finiteRankResetTriangle : (x y z : Carrier) →
    fourChainPfaffian x y z ≡ sewThreeResidualToSingleton x y z
  finiteRankResetTriangle x y z =
    fourPfaffianIsAdjacent x y z ∙
    sym (oddOddSewingIsFourAmplitude x y z)

  -- Two odd three-point residuals, separated by gap g.  The nine terms are
  -- the complete rank-one cross-block contraction before simplification.
  sewThreeResiduals : Carrier → Carrier → Carrier → Carrier → Carrier → Carrier
  sewThreeResiduals x y g u v =
    residual₀ x y ·
      ((x · y · g) · residual₀ u v +
       (x · y · g · u) · residual₁ u v +
       (x · y · g · u · v) · residual₂ u v) +
    residual₁ x y ·
      ((y · g) · residual₀ u v +
       (y · g · u) · residual₁ u v +
       (y · g · u · v) · residual₂ u v) +
    residual₂ x y ·
      (g · residual₀ u v +
       (g · u) · residual₁ u v +
       (g · u · v) · residual₂ u v)

  sixAdjacentAmplitude : Carrier → Carrier → Carrier → Carrier → Carrier → Carrier
  sixAdjacentAmplitude x y g u v = x · g · v

  twoOddResidualsGiveSixAmplitude : (x y g u v : Carrier) →
    sewThreeResiduals x y g u v ≡ sixAdjacentAmplitude x y g u v
  twoOddResidualsGiveSixAmplitude x y g u v = solve! R
