{-# OPTIONS --safe --cubical --guardedness #-}
module DSCActionCountermodels where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc)
open import Cubical.Data.List.Base using ([]; _∷_)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
import GraphAction as G
-- Import the actual DSC semantic core, not a copied substitute.
import ResolutionNetDependentSubstitution as DSC
module D = DSC.Dependent {ℓ = ℓ-zero}

data Model : Type where
  quadratic quartic : Model
polynomial : Model → G.Poly
polynomial quadratic = G.action
polynomial quartic = G.quartic

-- Same dependent interface for both models. It retains the supplied point
-- and the evidence for its action evaluation, NOT a stationarity assumption.
record Input (m : Model) : Type where
  constructor input
  field
    point actionValue : ℤ
    evaluation : actionValue ≡ G.pEval (polynomial m) point
open Input

Boundary : Type
Boundary = Σ Model Input
record Output (b : Boundary) : Type where
  constructor output
  field
    residual : ℤ
    residual-law : residual ≡ G.pEval (G.pDerivative (polynomial (fst b))) (point (snd b))
open Output

Environment : Type
Environment = Σ Model (λ _ → ℤ)
chooseModel : Environment → Model
chooseModel = fst
supplyInput : (e : Environment) → Input (chooseModel e)
supplyInput (m , q) = input q (G.pEval (polynomial m) q) refl
continuation : (b : Boundary) → Output b
continuation (m , i) = output (G.pEval (G.pDerivative (polynomial m)) (point i)) refl
run : (e : Environment) → Output (D.extend chooseModel supplyInput e)
run = D.execute Output continuation chooseModel supplyInput

-- Existing DSC laws apply to this EXACT interface, including both models.
substitution-law : (σ : Environment → Environment)
  → D.execute Output continuation (D.compose chooseModel σ) (λ e → supplyInput (σ e))
    ≡ (λ e → run (σ e))
substitution-law σ = D.execute-substitution Output continuation chooseModel supplyInput σ
extension-law : (σ : Environment → Environment)
  → D.extend (D.compose chooseModel σ) (λ e → supplyInput (σ e))
    ≡ D.compose (D.extend chooseModel supplyInput) σ
extension-law σ = D.extend-substitution chooseModel supplyInput σ
composition-law : (f g h : Environment → Environment)
  → D.compose h (D.compose g f) ≡ D.compose (D.compose h g) f
composition-law f g h = D.associative h g f
left-unit-law : (f : Environment → Environment) → D.compose D.identity f ≡ f
left-unit-law = D.left-unit
right-unit-law : (f : Environment → Environment) → D.compose f D.identity ≡ f
right-unit-law = D.right-unit

quadratic-stationary-example : residual (run (quadratic , pos 1)) ≡ pos 0
quadratic-stationary-example = refl
-- This successfully executed point is NOT stationary. DSC does not reject it.
nonstationary-output : residual (run (quadratic , pos 2)) ≡ pos 8
nonstationary-output = refl
quartic-output : residual (run (quartic , pos 1)) ≡ pos 4
quartic-output = refl

isZero : ℤ → Bool
isZero (pos 0) = true
isZero _ = false
stationarity-not-automatic : ((e : Environment) → residual (run e) ≡ pos 0) → ⊥
stationarity-not-automatic claim = false≢true (cong isZero (claim (quadratic , pos 2)))

fourthCoefficient : G.Poly → ℤ
fourthCoefficient (_ ∷ _ ∷ _ ∷ _ ∷ c ∷ _) = c
fourthCoefficient _ = pos 0
quartic-coefficient : fourthCoefficient (polynomial quartic) ≡ pos 1
quartic-coefficient = refl
-- Absence of the fourth-degree term is necessary for quadraticity. The
-- typeable quartic model falsifies even this necessary universal conclusion.
quadraticity-not-automatic : ((m : Model) → fourthCoefficient (polynomial m) ≡ pos 0) → ⊥
quadraticity-not-automatic claim = false≢true (cong isZero (claim quartic))

-- Stationarity can be demanded as an EXTRA dependent input. This does not
-- construct such a witness from an arbitrary well-typed environment.
StationaryInput : Model → Type
StationaryInput m = Σ (Input m) (λ i → G.pEval (G.pDerivative (polynomial m)) (point i) ≡ pos 0)
stationaryWitness : StationaryInput quadratic
stationaryWitness = supplyInput (quadratic , pos 1) , refl
bad-point-cannot-be-admitted : G.pEval (G.pDerivative (polynomial quadratic)) (pos 2) ≡ pos 0 → ⊥
bad-point-cannot-be-admitted p = false≢true (cong isZero p)
