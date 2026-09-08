{-# OPTIONS --safe --cubical --guardedness #-}
module CartierNormalSymbol where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Int using (ℤ; pos)

-- Coefficientwise formal series, indexed first by t degree, then x degree.
-- Polynomial arrays embed, but no finite-support or analytic convergence
-- assertion is inferred. Only multiplication by monomials is needed here.
Series : Type
Series = ℕ → ℕ → ℤ

zeroSeries : Series
zeroSeries _ _ = pos zero

unitSeries : Series
unitSeries zero zero = pos (suc zero)
unitSeries zero (suc _) = pos zero
unitSeries (suc _) _ = pos zero

mulT mulX : Series → Series
mulT a zero j = pos zero
mulT a (suc i) j = a i j
mulX a i zero = pos zero
mulX a i (suc j) = a i j

mulTX : Series → Series
mulTX a = mulT (mulX a)

-- Independent monomial actions commute on EVERY coefficient.
monomialsCommute : (a : Series) → mulX (mulT a) ≡ mulT (mulX a)
monomialsCommute a = funExt λ { zero → funExt λ { zero → refl ; (suc j) → refl }
  ; (suc i) → funExt λ { zero → refl ; (suc j) → refl } }

-- The source normal block has h in degree 1 and p in degree 0.
record H1 : Type where
  constructor h
  field coefficientsH : Series
record P0 : Type where
  constructor p
  field coefficientsP : Series

normalDifferential : H1 → P0
normalDifferential (h a) = p (mulTX a)

-- Cartier fibre coefficients and framed t-conormal coefficients are distinct.
TSeries : Type
TSeries = ℕ → ℤ

restrictX : Series → TSeries
restrictX a i = a i zero

record TConormal : Type where
  constructor conormalT
  field symbolCoefficient : ℤ

-- beta_x: lift, apply d=tx, extract the coefficient of x^1.
-- This is division on the known ideal x*(...), NOT inversion of x.
connecting : H1 → TSeries
connecting (h a) i = P0.coefficientsP (normalDifferential (h a)) i (suc zero)

mulTOnFibre : TSeries → TSeries
mulTOnFibre a zero = pos zero
mulTOnFibre a (suc i) = a i

connectingFormula : (a : Series) → connecting (h a) ≡ mulTOnFibre (restrictX a)
connectingFormula a = funExt λ { zero → refl ; (suc i) → refl }

-- The connecting map has order at least one in t.
connectingHasNoConstant : (a : Series) → connecting (h a) zero ≡ pos zero
connectingHasNoConstant a = refl

-- Two lifts of the same Cartier coefficient give the same connecting map.
connectingLiftIndependent : (a b : Series) → restrictX a ≡ restrictX b
  → connecting (h a) ≡ connecting (h b)
connectingLiftIndependent a b same =
  connectingFormula a ∙ cong mulTOnFibre same ∙ sym (connectingFormula b)

firstSymbol : H1 → TConormal
firstSymbol v = conormalT (connecting v (suc zero))

-- Evaluation uses the specified t-frame; not an unframed scalar deletion.
thetaT : TConormal → ℤ
thetaT (conormalT c) = c

symbolFormula : (a : Series) → firstSymbol (h a) ≡ conormalT (a zero zero)
symbolFormula a = refl

symbolRepresentativeIndependent : (a b : Series) → a zero zero ≡ b zero zero
  → firstSymbol (h a) ≡ firstSymbol (h b)
symbolRepresentativeIndependent a b same = cong conormalT same

framedEvaluation : (a : Series) → thetaT (firstSymbol (h a)) ≡ a zero zero
framedEvaluation a = refl

unitSymbol : thetaT (firstSymbol (h unitSeries)) ≡ pos (suc zero)
unitSymbol = refl

-- Negative control: ordinary Cartier restriction loses the raw multiplier.
rawRestrictionZero : (a : Series) → restrictX (mulTX a) ≡ (λ _ → pos zero)
rawRestrictionZero a = funExt λ { zero → refl ; (suc i) → refl }

rawUnitRestriction : restrictX (mulTX unitSeries) zero ≡ pos zero
rawUnitRestriction = refl

-- K_x=[A e --x--> A]. Distinct degree types prevent a hidden degree-zero H.
record K1 : Type where
  constructor e
  field coefficientsE : Series
record K0 : Type where
  constructor k
  field coefficientsK : Series

dX : K1 → K0
dX (e a) = k (mulX a)

nullHomotopy : K0 → K1
nullHomotopy (k a) = e (mulT a)

rawOnK0 : K0 → K0
rawOnK0 (k a) = k (mulTX a)
rawOnK1 : K1 → K1
rawOnK1 (e a) = e (mulTX a)

-- These are the two nonzero components of dH+Hd=tx id.
-- The omitted compositions are zero since K_x has only degrees 1 and 0.
nullDegreeZero : (v : K0) → dX (nullHomotopy v) ≡ rawOnK0 v
nullDegreeZero (k a) = cong k (monomialsCommute a)

nullDegreeOne : (v : K1) → nullHomotopy (dX v) ≡ rawOnK1 v
nullDegreeOne (e a) = refl

-- No identification with the full spatial Gysin functor, a generic-Q map,
-- an analytic residue, or the localized source ring is supplied here.
