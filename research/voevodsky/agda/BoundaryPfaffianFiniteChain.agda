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

  record SelectedGapUnit (x : Carrier) : Type ℓ where
    field
      inverse : Carrier
      inverseLaw : inverse · x ≡ 1r

  open SelectedGapUnit public

  -- The determinant-one triangular basis change fixes e0,e1 and replaces
  -- e2 by e2 + x^-1 y e0 - y e1.  Its last vector is orthogonal to the pair.
  localizedThirdCoefficient₀ : (x y : Carrier) → SelectedGapUnit x → Carrier
  localizedThirdCoefficient₀ x y ux = inverse ux · y

  localizedThirdCoefficient₁ : Carrier → Carrier
  localizedThirdCoefficient₁ y = - y

  localizedPairingWith₀ : (x y : Carrier) → SelectedGapUnit x → Carrier
  localizedPairingWith₀ x y ux =
    x · y + localizedThirdCoefficient₁ y · x

  localizedPairingWith₁ : (x y : Carrier) → SelectedGapUnit x → Carrier
  localizedPairingWith₁ x y ux =
    y + localizedThirdCoefficient₀ x y ux · (- x)

  localizedPairingWith₀Vanishes :
    (x y : Carrier) (ux : SelectedGapUnit x) →
    localizedPairingWith₀ x y ux ≡ 0r
  localizedPairingWith₀Vanishes x y ux = solve! R

  localizedPairingWith₁Vanishes :
    (x y : Carrier) (ux : SelectedGapUnit x) →
    localizedPairingWith₁ x y ux ≡ 0r
  localizedPairingWith₁Vanishes x y ux =
    normalize ∙ useInverse ∙ cancel
    where
    normalize : localizedPairingWith₁ x y ux ≡
      y + (- (y · (inverse ux · x)))
    normalize = solve! R
    useInverse : y + (- (y · (inverse ux · x))) ≡
      y + (- (y · 1r))
    useInverse = cong (λ z → y + (- (y · z))) (inverseLaw ux)
    cancel : y + (- (y · 1r)) ≡ 0r
    cancel = solve! R

  record LocalizedThreeNormalForm (x y : Carrier) (ux : SelectedGapUnit x) :
    Type ℓ where
    field
      survivingBlockWeight : Carrier
      blockIsSelectedGap : survivingBlockWeight ≡ x
      thirdPairing₀Vanishes : localizedPairingWith₀ x y ux ≡ 0r
      thirdPairing₁Vanishes : localizedPairingWith₁ x y ux ≡ 0r

  localizedThreeNormalForm :
    (x y : Carrier) (ux : SelectedGapUnit x) →
    LocalizedThreeNormalForm x y ux
  localizedThreeNormalForm x y ux = record
    { survivingBlockWeight = x
    ; blockIsSelectedGap = refl
    ; thirdPairing₀Vanishes = localizedPairingWith₀Vanishes x y ux
    ; thirdPairing₁Vanishes = localizedPairingWith₁Vanishes x y ux
    }

  -- Generic first-pair elimination for a remote chain vector with suffix
  -- profile s.  The same formulas used at size three work at every size.
  remoteCoefficient₀ : (x s : Carrier) → SelectedGapUnit x → Carrier
  remoteCoefficient₀ x s ux = inverse ux · s

  remoteCoefficient₁ : Carrier → Carrier
  remoteCoefficient₁ s = - s

  remotePairingWith₀Vanishes :
    (x s : Carrier) (ux : SelectedGapUnit x) →
    x · s + remoteCoefficient₁ s · x ≡ 0r
  remotePairingWith₀Vanishes x s ux = solve! R

  remotePairingWith₁Vanishes :
    (x s : Carrier) (ux : SelectedGapUnit x) →
    s + remoteCoefficient₀ x s ux · (- x) ≡ 0r
  remotePairingWith₁Vanishes x s ux =
    normalize ∙ useInverse ∙ cancel
    where
    normalize : s + remoteCoefficient₀ x s ux · (- x) ≡
      s + (- (s · (inverse ux · x)))
    normalize = solve! R
    useInverse : s + (- (s · (inverse ux · x))) ≡
      s + (- (s · 1r))
    useInverse = cong (λ z → s + (- (s · z))) (inverseLaw ux)
    cancel : s + (- (s · 1r)) ≡ 0r
    cancel = solve! R

  -- Expanding the pairing of two transformed remote vectors shows that all
  -- correction terms cancel, so the untouched suffix chain form survives.
  transformedRemotePairing :
    (x sᵢ sⱼ aᵢⱼ : Carrier) → SelectedGapUnit x → Carrier
  transformedRemotePairing x sᵢ sⱼ aᵢⱼ ux =
    aᵢⱼ +
    remoteCoefficient₀ x sⱼ ux · (- (x · sᵢ)) +
    remoteCoefficient₁ sⱼ · (- sᵢ) +
    remoteCoefficient₀ x sᵢ ux · (x · sⱼ) +
    remoteCoefficient₁ sᵢ · sⱼ +
    remoteCoefficient₀ x sᵢ ux · remoteCoefficient₁ sⱼ · x +
    remoteCoefficient₁ sᵢ · remoteCoefficient₀ x sⱼ ux · (- x)

  transformedRemotePairingPreserved :
    (x sᵢ sⱼ aᵢⱼ : Carrier) (ux : SelectedGapUnit x) →
    transformedRemotePairing x sᵢ sⱼ aᵢⱼ ux ≡ aᵢⱼ
  transformedRemotePairingPreserved x sᵢ sⱼ aᵢⱼ ux = solve! R

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

  -- Full first-row Pfaffian expansion of the six-point chain.  Each grouped
  -- parenthesis is the four-point Pfaffian of the corresponding minor.
  sixChainPfaffian : Carrier → Carrier → Carrier → Carrier → Carrier → Carrier
  sixChainPfaffian x y g u v =
    x · (g · v + (- ((g · u) · (u · v))) + (g · u · v) · u) +
    (- ((x · y) ·
      ((y · g) · v + (- ((y · g · u) · (u · v))) +
       (y · g · u · v) · u))) +
    (x · y · g) ·
      (y · v + (- ((y · g · u) · (g · u · v))) +
       (y · g · u · v) · (g · u)) +
    (- ((x · y · g · u) ·
      (y · (u · v) + (- ((y · g) · (g · u · v))) +
       (y · g · u · v) · g))) +
    (x · y · g · u · v) ·
      (y · u + (- ((y · g) · (g · u))) + (y · g · u) · g)

  sixPfaffianIsAdjacent : (x y g u v : Carrier) →
    sixChainPfaffian x y g u v ≡ sixAdjacentAmplitude x y g u v
  sixPfaffianIsAdjacent x y g u v = solve! R

  sixRankResetTriangle : (x y g u v : Carrier) →
    sixChainPfaffian x y g u v ≡ sewThreeResiduals x y g u v
  sixRankResetTriangle x y g u v =
    sixPfaffianIsAdjacent x y g u v ∙
    sym (twoOddResidualsGiveSixAmplitude x y g u v)
