{-# OPTIONS --safe --cubical --guardedness #-}
module HomComplexSigns where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver

-- Degree parity only; no identification of distinct integer degrees.
data Parity : Type where
  even odd : Parity

flip : Parity → Parity
flip even = odd
flip odd = even

paritySum : Parity → Parity → Parity
paritySum even q = q
paritySum odd q = flip q

module Signs {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  V = fst R

  signed : Parity → V → V
  signed even x = x
  signed odd x = - x

  signProduct : (p q : Parity) (x : V)
    → signed p (signed q x) ≡ signed (paritySum p q) x
  signProduct even q x = refl
  signProduct odd even x = refl
  signProduct odd odd x = solve! R

  homBoundary : Parity → V → V → V
  homBoundary p targetTerm sourceTerm = targetTerm + (- signed p sourceTerm)

  -- Pointwise expansion of d(g f)=(dg)f+(-1)^p g(df).
  -- a=d_N g f, b=g d_M f, c=g f d_L. These terms are NOT commuted
  -- as operators: only their values in the additive target are combined.
  compositionSignLaw : (p q : Parity) (a b c : V)
    → homBoundary (paritySum p q) a c
      ≡ homBoundary p a b + signed p (homBoundary q b c)
  compositionSignLaw even even a b c = solve! R
  compositionSignLaw even odd a b c = solve! R
  compositionSignLaw odd even a b c = solve! R
  compositionSignLaw odd odd a b c = solve! R

  -- After d_M^2=d_L^2=0, the two middle terms in d_Hom^2 cancel.
  differentialSquareSigns : (p : Parity) (middle : V)
    → (- signed p middle) + (- signed (flip p) middle) ≡ 0r
  differentialSquareSigns even middle = solve! R
  differentialSquareSigns odd middle = solve! R

-- These are universal expanded sign identities. A DG-category implementation
-- must additionally type composition across every homogeneous degree and
-- supply additivity. EndpointHomComplex checks actual coordinate d^2 laws.
