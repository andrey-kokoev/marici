{-# OPTIONS --safe --cubical --guardedness #-}
module TickInterpretationBoundary where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.Sigma using (_×_; Σ-syntax)
open import Cubical.Data.Empty.Base using (⊥)
import TickEvolutionBridge as Evolution
import TickRetainedStructure as Structure

-- An endpoint-compatible external model. Analytic continuity, probability
-- preservation, and an interval parameter are additional obligations; the
-- EndpointModel type alone does not assert them.
module RetainedInterpretation {V P : Type}
  (model : Evolution.EndpointModel V P) (s : Bool × Bool) where
  module B = Evolution.Bridge model s
  module C = Structure.AtSource s

  -- The entire source Tick is retained and recoverable, rather than
  -- pretending that the continuous evolution encodes every source field.
  record Interpretation : Type where
    constructor interpreted
    field
      source-tick : B.D.ATick
      evolution : P → P → V
      agrees : evolution ≡ B.realization source-tick

  interpret : B.D.ATick → Interpretation
  interpret t = interpreted t (B.realization t) refl

  recover : Interpretation → B.D.ATick
  recover = Interpretation.source-tick

  recover-interpret : (t : B.D.ATick) → recover (interpret t) ≡ t
  recover-interpret t = refl

  -- Classification applies to the whole construction, including the
  -- retained record. It does NOT force the externally chosen model.
  interpretation-factors : (t : B.D.ATick)
    → interpret t ≡ interpret (C.rebuild (C.tags t))
  interpretation-factors = C.observation-factors interpret

-- A deliberately stronger obstruction than failure of monotone time
-- reparameterization: rule out ANY parameter substitution at all.
Substitution : {V P Q : Type} → (P → V) → (Q → V) → Type
Substitution {P = P} {Q = Q} f g = Σ[ ρ ∈ (Q → P) ] ((q : Q) → f (ρ q) ≡ g q)

image-obstruction : {V P Q : Type} (f : P → V) (g : Q → V)
  (Invariant : V → Type)
  → ((p : P) → Invariant (f p))
  → (q : Q) → (Invariant (g q) → ⊥)
  → Substitution f g → ⊥
image-obstruction f g Invariant all-f q not-g (ρ , agrees) =
  not-g (subst Invariant (agrees q) (all-f (ρ q)))

-- Any equivalence of parameter domains entails such a substitution.
-- Thus the obstruction also excludes endpoint-preserving increasing
-- homeomorphisms, without needing to formalize them to prove this stronger
-- sufficient criterion. A concrete invariant and witness must still be
-- supplied for each analytic counterexample.
