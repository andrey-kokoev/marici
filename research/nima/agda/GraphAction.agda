{-# OPTIONS --safe --cubical --guardedness #-}
module GraphAction where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (idEquiv)
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc; _+_; _·_)
open import Cubical.Data.Int.Properties using (+Comm)
open import Cubical.Data.Nat.Base using (ℕ; suc)
open import Cubical.Data.List.Base using (List; []; _∷_; map)
open import Cubical.Data.Bool.Base using (Bool; true; false)
import WholePackageSigmaPi as Whole
import WholePackageResolution as RRC

-- Ascending coefficients. These are formal polynomials over integers, not
-- real-valued actions or a formal real differentiation implementation.
Poly = List ℤ
pAdd : Poly → Poly → Poly
pAdd [] q = q
pAdd p [] = p
pAdd (a ∷ p) (b ∷ q) = (a + b) ∷ pAdd p q
pScale : ℤ → Poly → Poly
pScale c = map (λ a → c · a)
pMultiply : Poly → Poly → Poly
pMultiply [] q = []
pMultiply (a ∷ p) q = pAdd (pScale a q) (pos 0 ∷ pMultiply p q)
pEval : Poly → ℤ → ℤ
pEval [] q = pos 0
pEval (a ∷ p) q = a + q · pEval p q
weightedTail : ℕ → Poly → Poly
weightedTail n [] = []
weightedTail n (a ∷ p) = (pos n · a) ∷ weightedTail (suc n) p
pDerivative : Poly → Poly
pDerivative [] = []
pDerivative (a ∷ p) = weightedTail 1 p

-- This compositional equality is generic, not just a numerical test.
pAdd-comm : (p q : Poly) → pAdd p q ≡ pAdd q p
pAdd-comm [] [] = refl
pAdd-comm [] (b ∷ q) = refl
pAdd-comm (a ∷ p) [] = refl
pAdd-comm (a ∷ p) (b ∷ q) = cong₂ _∷_ (+Comm a b) (pAdd-comm p q)

coordinatePolynomial : Poly
coordinatePolynomial = pos 0 ∷ pos 1 ∷ []

-- Path 0--1--2, weights (1,3), j=(0,2,0), endpoints fixed at zero.
-- q=2*phi_1. Store 8*S = q^2 + 3*q^2 - 8*q.
data Part : Type where
  leftEdge rightEdge sourceTerm : Part
piece : Part → Poly
piece leftEdge = pMultiply coordinatePolynomial coordinatePolynomial
piece rightEdge = pScale (pos 3) (pMultiply coordinatePolynomial coordinatePolynomial)
piece sourceTerm = pScale (negsuc 7) coordinatePolynomial
assemble : (Part → Poly) → Poly
assemble f = pAdd (f leftEdge) (pAdd (f rightEdge) (f sourceTerm))
action : Poly
action = assemble piece

-- Independently assembled incidence residual: L*q-2*j = 4*q-4.
poissonResidual : Poly
poissonResidual = negsuc 3 ∷ (pos 1 + pos 3) ∷ []
variation-is-poisson : pDerivative action ≡ pScale (pos 2) poissonResidual
variation-is-poisson = refl
stationary : pEval (pDerivative action) (pos 1) ≡ pos 0
stationary = refl

-- Edge orientation reversal changes q to -q, not its square.
orientation-invariant : pMultiply (pScale (negsuc 0) coordinatePolynomial) (pScale (negsuc 0) coordinatePolynomial)
  ≡ piece leftEdge
orientation-invariant = refl
reordered : Poly
reordered = pAdd (piece rightEdge) (pAdd (piece leftEdge) (piece sourceTerm))
reordering-invariant : action ≡ reordered
reordering-invariant = refl

-- mu^2=2 adds 2*q^2 to 8*S: still local and quadratic, not shift covariant.
screened : Poly
screened = pAdd action (pScale (pos 2) (piece leftEdge))
screened-residual : pEval (pDerivative screened) (pos 1) ≡ pos 4
screened-residual = refl
-- Add (1/4) sum_edges (phi_i-phi_j)^4. In q units store 32*S:
-- 4*(8*S_quadratic)+q^4. It preserves shift covariance but is nonlinear.
quartic : Poly
quartic = pAdd (pScale (pos 4) action)
  (pMultiply (piece leftEdge) (piece leftEdge))
quartic-residual : pEval (pDerivative quartic) (pos 1) ≡ pos 4
quartic-residual = refl

open Whole.Universe ℓ-zero
open RRC.Generators ℓ-zero
parts : Part → Complete
parts i = pack (atom Poly) (piece i)
assembled-from-package : assemble (value (Pi-package Part parts)) ≡ action
assembled-from-package = refl

-- Compare the action derivative to twice the incidence equation. The action
-- coefficients and both scale factors are retained, not just the zero output.
actionDerivative incidenceDerivative : Complete
actionDerivative = pack
  (retain (atom ℤ) (pos 8)
    (retain (atom ℤ) (pos 2) (retain (atom Poly) action (atom Poly))))
  (pDerivative action)
incidenceDerivative = pack
  (retain (atom Poly) poissonResidual (atom Poly))
  (pScale (pos 2) poissonResidual)

data Seeds : Complete → Type₁ where
  part-seed : (i : Part) → Seeds (parts i)
  derivative-seed : Seeds actionDerivative
  incidence-seed : Seeds incidenceDerivative

partsHistory : Resolve Seeds (Pi-package Part parts)
partsHistory = apply (Pi-rule Part parts) (λ { (lift i) → seed (part-seed i) })
-- A bounded readout of this typed retained history's endpoint family.
-- It is NOT an action assignment on arbitrary RRC histories.
actionOfHistory : Resolve Seeds (Pi-package Part parts) → Poly
actionOfHistory h = assemble
  (Whole.Universe.value (fst (Whole.Universe.value (reify-history h))))
retained-action : actionOfHistory partsHistory ≡ action
retained-action = refl
comparisonRule : Rule
comparisonRule = compare-rule actionDerivative incidenceDerivative
  (idEquiv Poly) variation-is-poisson
comparisonHistory : Resolve Seeds (output comparisonRule)
comparisonHistory = apply comparisonRule
  λ { (lift true) → seed derivative-seed ; (lift false) → seed incidence-seed }
family : Bool → Complete
family true = Pi-package Part parts
family false = output comparisonRule
history : Resolve Seeds (Pi-package Bool family)
history = apply (Pi-rule Bool family)
  λ { (lift true) → partsHistory ; (lift false) → comparisonHistory }
retainedHistory : Whole.Universe.Complete (ℓ-suc ℓ-zero)
retainedHistory = reify-history history
retains-history : snd (Whole.Universe.value retainedHistory) ≡ history
retains-history = refl
