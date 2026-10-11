{-# OPTIONS --safe --cubical --guardedness #-}
module TickJointEvolutionContinuity where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Sigma.Base using (_×_)
open import CauchyMetricEquivalence using (MetricCompletionCandidate)
open import TickCompletionRealization
open import TickPolynomialContinuity
open import TickBoundedProductContinuity using (BoundedNear; forget-bound)
open import TickQuotientContinuity using (CompletionNear)
import TickEvolutionBridge as EB

-- All six inputs may vary: two evolution parameters and four amplitudes.
data Input : Type where
  alpha beta : Input
  amplitude : Bool × Bool → Input

module C = Circuit Input
open C

left-expression : Bool × Bool → Expr
left-expression (x , y) = plus
  (times (plus one (negative (input alpha))) (input (amplitude (x , y))))
  (times (input alpha) (input (amplitude (EB.G.expand x , y))))

evolution-expression : Bool × Bool → Expr
evolution-expression (x , y) = plus
  (times (plus one (negative (input beta))) (left-expression (x , y)))
  (times (input beta) (left-expression (x , EB.G.expand y)))

environment : Realization.Scalar → Realization.Scalar → Realization.Vector
  → Input → MetricCompletionCandidate
environment a b v alpha = a
environment a b v beta = b
environment a b v (amplitude j) = v j

-- Definitional agreement with the previously implemented evolution;
-- this is not a different polynomial sharing just its endpoint values.
evolution-expression-correct : (a b : Realization.Scalar)
  (v : Realization.Vector) (j : Bool × Bool)
  → eval (evolution-expression j) (environment a b v) ≡ Realization.U a b v j
evolution-expression-correct a b v (x , y) = refl

-- Joint quantitative continuity on explicit bounded regions, coordinatewise.
-- The expression computes both an output bound and input precision demands.
evolution-continuous : (bounds : Input → ℕ) (k : ℕ)
  (a a′ b b′ : Realization.Scalar) (v v′ : Realization.Vector) (j : Bool × Bool)
  → ((i : Input) → BoundedNear (bounds i)
      (demand (evolution-expression j) bounds k i)
      (environment a b v i) (environment a′ b′ v′ i))
  → BoundedNear (radius (evolution-expression j) bounds) k
      (Realization.U a b v j) (Realization.U a′ b′ v′ j)
evolution-continuous bounds k a a′ b b′ v v′ (x , y) =
  continuous (evolution-expression (x , y)) bounds k
    (environment a b v) (environment a′ b′ v′)

-- All output coordinates at once; no amplitude is assumed to be a basis
-- vector, and neither evolution parameter is held fixed.
evolution-vector-continuous : (bounds : Input → ℕ) (k : ℕ)
  (a a′ b b′ : Realization.Scalar) (v v′ : Realization.Vector)
  → ((j : Bool × Bool) (i : Input) → BoundedNear (bounds i)
      (demand (evolution-expression j) bounds k i)
      (environment a b v i) (environment a′ b′ v′ i))
  → ((j : Bool × Bool) → CompletionNear k
      (Realization.U a b v j) (Realization.U a′ b′ v′ j))
evolution-vector-continuous bounds k a a′ b b′ v v′ h j =
  forget-bound {d = radius (evolution-expression j) bounds} {k = k}
    (evolution-continuous bounds k a a′ b b′ v v′ j (h j))
