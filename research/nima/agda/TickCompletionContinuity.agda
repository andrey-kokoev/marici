{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionContinuity where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Nat using (suc)
open import Cubical.Data.Rationals using (fromNatℚ)
open import Cubical.Data.Nat.Literals
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.SetQuotients using ([_])
open import Cubical.Tactics.CommRingSolver
open import Cubical.Algebra.CommRing.Base
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyQuantitativeContinuity
open import CauchyAddition
open import CauchyNegation
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing
open import TickCompletionRealization
import TickEvolutionBridge as EB

-- Quantitative continuity uses eventual rational precision bounds, not
-- Agda path equality as a substitute for analytic continuity.
identity-continuous : QuantitativelyContinuous (λ x → x)
modulus identity-continuous k = k
preservesEventuallyWithin identity-continuous x y k h = h

constant-continuous : (z : RegularCauchy) → QuantitativelyContinuous (λ _ → z)
modulus (constant-continuous z) k = k
preservesEventuallyWithin (constant-continuous z) x y k h = ≈metric-refl z k

negate-continuous : QuantitativelyContinuous negateRegular
modulus negate-continuous k = k
preservesEventuallyWithin negate-continuous x y k = PT.map
  (λ { (N , bounds) → N , λ n N≤n →
    negate-one-error-bound (approximation y n) (approximation x n) (precision k)
      (snd (bounds n N≤n)) ,
    negate-one-error-bound (approximation x n) (approximation y n) (precision k)
      (fst (bounds n N≤n)) })

complement : RegularCauchy → RegularCauchy
complement t = addRegular (constantCauchy 1) (negateRegular t)

complement-continuous : QuantitativelyContinuous complement
complement-continuous = compose-quantitatively-continuous
  (addRegular-right-quantitatively-continuous (constantCauchy 1)) negate-continuous

weight : Bool → Bool → RegularCauchy → RegularCauchy
weight false false = complement
weight false true t = t
weight true false t = t
weight true true = complement

weight-continuous : (u x : Bool) → QuantitativelyContinuous (weight u x)
weight-continuous false false = complement-continuous
weight-continuous false true = identity-continuous
weight-continuous true false = identity-continuous
weight-continuous true true = complement-continuous

-- Coordinate representatives of a single L-leg from any basis vector.
left-coordinate : Bool × Bool → Bool × Bool → RegularCauchy → RegularCauchy
left-coordinate (u , false) (x , false) = weight u x
left-coordinate (u , false) (x , true) t = constantCauchy 0
left-coordinate (u , true) (x , false) t = constantCauchy 0
left-coordinate (u , true) (x , true) = weight u x

left-coordinate-continuous : (q j : Bool × Bool)
  → QuantitativelyContinuous (left-coordinate q j)
left-coordinate-continuous (u , false) (x , false) = weight-continuous u x
left-coordinate-continuous (u , false) (x , true) = constant-continuous (constantCauchy 0)
left-coordinate-continuous (u , true) (x , false) = constant-continuous (constantCauchy 0)
left-coordinate-continuous (u , true) (x , true) = weight-continuous u x

module Algebra (K : CommRing ℓ-zero) where
  open CommRingStr (snd K)
  stay : (a : fst K) → 1r + (- a) ≡ (1r + (- a)) · (1r · 1r) + a · (0r · 1r)
  stay a = solve! K
  move : (a : fst K) → a ≡ (1r + (- a)) · (0r · 1r) + a · (1r · 1r)
  move a = solve! K
  absent : (a d e : fst K) → 0r ≡ (1r + (- a)) · (d · 0r) + a · (e · 0r)
  absent a d e = solve! K

module A = Algebra CompletionCommRing

-- Link those continuous representatives to the SAME completion-valued
-- polynomial operator used by the Tick bridge (not a separate toy curve).
left-coordinate-correct : (q j : Bool × Bool) (t : RegularCauchy)
  → [ left-coordinate q j t ] ≡ Realization.leg Realization.L [ t ] (Realization.basis q) j
left-coordinate-correct (false , false) (false , false) t = A.stay [ t ]
left-coordinate-correct (false , false) (false , true) t = A.absent [ t ] oneCompletion zeroCompletion
left-coordinate-correct (false , false) (true , false) t = A.move [ t ]
left-coordinate-correct (false , false) (true , true) t = A.absent [ t ] zeroCompletion oneCompletion
left-coordinate-correct (false , true) (false , false) t = A.absent [ t ] oneCompletion zeroCompletion
left-coordinate-correct (false , true) (false , true) t = A.stay [ t ]
left-coordinate-correct (false , true) (true , false) t = A.absent [ t ] zeroCompletion oneCompletion
left-coordinate-correct (false , true) (true , true) t = A.move [ t ]
left-coordinate-correct (true , false) (false , false) t = A.move [ t ]
left-coordinate-correct (true , false) (false , true) t = A.absent [ t ] zeroCompletion oneCompletion
left-coordinate-correct (true , false) (true , false) t = A.stay [ t ]
left-coordinate-correct (true , false) (true , true) t = A.absent [ t ] oneCompletion zeroCompletion
left-coordinate-correct (true , true) (false , false) t = A.absent [ t ] zeroCompletion oneCompletion
left-coordinate-correct (true , true) (false , true) t = A.move [ t ]
left-coordinate-correct (true , true) (true , false) t = A.absent [ t ] oneCompletion zeroCompletion
left-coordinate-correct (true , true) (true , true) t = A.stay [ t ]

swap : Bool × Bool → Bool × Bool
swap (x , y) = y , x

right-coordinate : Bool × Bool → Bool × Bool → RegularCauchy → RegularCauchy
right-coordinate q j = left-coordinate (swap q) (swap j)

right-coordinate-continuous : (q j : Bool × Bool)
  → QuantitativelyContinuous (right-coordinate q j)
right-coordinate-continuous q j = left-coordinate-continuous (swap q) (swap j)

module Completion = CommRingStr (snd CompletionCommRing)

transpose-leg : (q j : Bool × Bool) (a : Realization.Scalar)
  → Realization.leg Realization.L a (Realization.basis (swap q)) (swap j)
    ≡ Realization.leg Realization.R a (Realization.basis q) j
transpose-leg (u , v) (x , y) a =
  cong₂ Completion._+_
    (cong (Completion._·_ (Completion._+_ oneCompletion (Completion.-_ a)))
      (Completion.·Comm (Realization.delta v y) (Realization.delta u x)))
    (cong (Completion._·_ a)
      (Completion.·Comm (Realization.delta v (EB.G.expand y)) (Realization.delta u x)))

right-coordinate-correct : (q j : Bool × Bool) (t : RegularCauchy)
  → [ right-coordinate q j t ] ≡ Realization.leg Realization.R [ t ] (Realization.basis q) j
right-coordinate-correct q j t = left-coordinate-correct (swap q) (swap j) t
  ∙ transpose-leg q j [ t ]

-- Both schedule legs start from basis states (including the intermediate
-- corner). These theorems apply to all such states, not just |00>.
-- They prove representative-level quantitative coordinate continuity and
-- exact agreement with the completion-valued operators. A quotient-level
-- joint continuity theorem for U(a,b,v) is still a separate obligation.

