{-# OPTIONS --safe --cubical --guardedness #-}
module PyramidObstructionTriangle where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver

-- Minimal support triangle from filtered_q_comparison, uniformly over R.
module Minimal {ℓ} (R : CommRing ℓ) (Δ : fst R) where
  open CommRingStr (snd R)
  Carrier = fst R

  -- A_min: k --Δ--> b in homological degrees 3 and 2.
  ASupported3 = Carrier
  ASupported2 = Carrier
  dA : ASupported3 → ASupported2
  dA k = Δ · k

  -- E_min adds a relative generic lift a with d(a)=b.
  ERelative3 = Σ Carrier (λ _ → Carrier)
  ERelative2 = Carrier
  dE : ERelative3 → ERelative2
  dE (a , k) = a + Δ · k

  -- Quotient generic line Q in degree 3.
  QGeneric3 = Carrier
  include3 : ASupported3 → ERelative3
  include3 k = 0r , k
  include2 : ASupported2 → ERelative2
  include2 b = b
  quotient3 : ERelative3 → QGeneric3
  quotient3 (a , k) = a

  inclusionChainLaw : (k : ASupported3) → dE (include3 k) ≡ include2 (dA k)
  inclusionChainLaw k = solve! R

  quotientKillsSupport : (k : ASupported3) → quotient3 (include3 k) ≡ 0r
  quotientKillsSupport k = refl

  -- The quotient unit has no closed lift: every lift (1,k) has d=1+Δk.
  unitLiftBoundary : (k : Carrier) → dE (1r , k) ≡ 1r + Δ · k
  unitLiftBoundary k = refl

  record UnitClosedLift : Type ℓ where
    field
      correction : Carrier
      closes : 1r + Δ · correction ≡ 0r

  -- A closed multiple always exists without dividing by Δ.
  globalCycle : Carrier → ERelative3
  globalCycle c = (Δ · c) , (- c)

  globalCycleClosed : (c : Carrier) → dE (globalCycle c) ≡ 0r
  globalCycleClosed c = solve! R

  globalCycleQuotient : (c : Carrier) → quotient3 (globalCycle c) ≡ Δ · c
  globalCycleQuotient c = refl

  -- A target boundary complex and the exact data needed for a chain map.
  -- This does not assert that a physical target supplies these fields.
  record TargetBoundary : Type (ℓ-suc ℓ) where
    field
      Target3 Target2 : Type ℓ
      zero2 : Target2
      add3 : Target3 → Target3 → Target3
      scale3 : Carrier → Target3 → Target3
      scale2 : Carrier → Target2 → Target2
      dTarget : Target3 → Target2
      addTarget2 : Target2 → Target2 → Target2
      dAdd : (x y : Target3) → dTarget (add3 x y)
        ≡ addTarget2 (dTarget x) (dTarget y)
      dScale : (c : Carrier) (x : Target3)
        → dTarget (scale3 c x) ≡ scale2 c (dTarget x)
      scaleAdd : (a b : Carrier) (x : Target2)
        → addTarget2 (scale2 a x) (scale2 b x) ≡ scale2 (a + b) x
      scaleMul : (a b : Carrier) (x : Target2)
        → scale2 a (scale2 b x) ≡ scale2 (a · b) x
      genericLift supportedLift : Target3
      boundaryClass : Target2
      genericBoundary : dTarget genericLift ≡ boundaryClass
      supportedBoundary : dTarget supportedLift ≡ scale2 Δ boundaryClass

  module MapToTarget (T : TargetBoundary) where
    open TargetBoundary T

    map3 : ERelative3 → Target3
    map3 (a , k) = add3 (scale3 a genericLift) (scale3 k supportedLift)

    map2 : ERelative2 → Target2
    map2 b = scale2 b boundaryClass

    chainLaw : (v : ERelative3) → dTarget (map3 v) ≡ map2 (dE v)
    chainLaw (a , k) =
      dAdd (scale3 a genericLift) (scale3 k supportedLift)
      ∙ cong₂ addTarget2
          (dScale a genericLift ∙ cong (scale2 a) genericBoundary)
          (dScale k supportedLift ∙ cong (scale2 k) supportedBoundary
            ∙ scaleMul k Δ boundaryClass)
      ∙ scaleAdd a (k · Δ) boundaryClass
      ∙ cong (λ c → scale2 c boundaryClass) (solve! R)

-- Interpretation: a relative generic lift maps to theta with d theta=beta;
-- its support correction maps to W with d W=Δ beta. The nonzero beta is
-- retained. This is not a closed lift of the generic unit and does not
-- identify this target-derived source with Marici's normalization source.
