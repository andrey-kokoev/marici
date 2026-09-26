{-# OPTIONS --safe --cubical --guardedness #-}
module CoherenceResolutionClosureRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
import CoherenceResolutionClosure as Free

module C = Free.Closure Unit (λ _ _ → Unit) (λ _ _ _ → ⊥)

S : Unit → Type₀
S _ = Unit

original : C.Resolve S tt
original = C.seed tt

inner-step : C.Resolve (C.Resolve S) tt
inner-step = C.seed (C.unary tt original)

outer-step : C.Resolve (C.Resolve S) tt
outer-step = C.unary tt (C.seed original)

same-flattening : C.flatten inner-step ≡ C.flatten outer-step
same-flattening = refl

RootSeed : C.Resolve (C.Resolve S) tt → Type₀
RootSeed (C.seed _) = Unit
RootSeed (C.unary _ _) = ⊥
RootSeed (C.binary () _ _)

-- Flattening retains the rule step but forgets which closure layer added it.
-- It is therefore not an equivalence of raw resolution histories.
distinct-layering : inner-step ≡ outer-step → ⊥
distinct-layering p = subst RootSeed p tt
