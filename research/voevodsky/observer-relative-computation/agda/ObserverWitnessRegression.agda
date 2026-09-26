{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverWitnessRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (lUnit; rUnit)
open import Cubical.Foundations.Univalence using (uaβ)
open import Cubical.Data.Sigma.Base using (_,_; fst)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (notEquiv; true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.HITs.PropositionalTruncation.Base using (squash₁)
open import ObserverAdmissibleImages
import ObserverEndpointAction as Action
import ObserverGroupoidDescentEquivalence as Descent
open import Cubical.Foundations.HLevels using (isGroupoidRetract; isGroupoidΣ; isSet→isGroupoid)
import Cubical.HITs.S1.Base as S1
import Cubical.HITs.S1.Properties as S1P
import IndexIdentityCoherenceRegression as Cover
import IndexIdentityCoherence as Indexed
module Ix = Indexed.Indexed ℓ-zero

f : Bool → Unit
f _ = tt
g : Bool → Ix.Index Cover.F
g _ = Cover.base-index

post : Image f → Image g
post _ = arrive g true

flat-arrival : (b : Bool) → post (arrive f b) ≡ arrive g b
flat-arrival _ = Σ≡Prop (λ _ → squash₁) refl

twisted-arrival : (b : Bool) → post (arrive f b) ≡ arrive g b
twisted-arrival true = flat-arrival true
twisted-arrival false = Σ≡Prop (λ _ → squash₁) Cover.index-loop

flat twisted : ImageFactors f g
flat = post , flat-arrival
twisted = post , twisted-arrival

same-visible-postprocessor : fst flat ≡ fst twisted
same-visible-postprocessor = refl

-- This observation asks for the induced comparison, not just a value.
comparison : ImageFactors f g → Cover.base-index ≡ Cover.base-index
comparison factor = Action.Endpoint.act f g factor {true} {false} refl

reduce-units : {A : Type} {x y : A} (p : x ≡ y) → refl ∙ refl ∙ p ≡ p
reduce-units p = sym (lUnit (refl ∙ p)) ∙ sym (lUnit p)

flat-comparison : comparison flat ≡ refl
flat-comparison = reduce-units refl

twisted-comparison : comparison twisted ≡ Cover.index-loop
twisted-comparison = reduce-units Cover.index-loop

factors-distinct : flat ≡ twisted → ⊥
factors-distinct e = Cover.loop-is-not-reflexive
  (sym twisted-comparison ∙ sym (cong comparison e) ∙ flat-comparison)

-- Unlike the earlier deliberately invalid loop-on-identity assignment,
-- both factors have coherent actions, including the twisted one.
module T = Action.Endpoint f g twisted

twisted-unit : (b : Bool) → T.act {b} {b} refl ≡ refl
twisted-unit = T.act-unit

twisted-route-cancels : T.act {true} {false} refl ∙ T.act {false} {true} refl ≡ refl
twisted-route-cancels = sym (T.act-compose {true} {false} {true} refl refl)
  ∙ cong (T.act {true} {true}) (sym (rUnit refl)) ∙ T.act-unit true

-- The witness distinction has an actual Bool readout through the cover.
-- This is mathematical transport, not an asserted temporal process.
readout : ImageFactors f g → Bool
readout factor = subst (Ix.Fibre Cover.F) (comparison factor) true

flat-readout : readout flat ≡ true
flat-readout = cong (λ p → subst (Ix.Fibre Cover.F) p true) flat-comparison
  ∙ substRefl {B = Ix.Fibre Cover.F} {x = Cover.base-index} true

twisted-readout : readout twisted ≡ false
twisted-readout = cong (λ p → subst (Ix.Fibre Cover.F) p true) twisted-comparison
  ∙ uaβ notEquiv true

readouts-distinct : readout flat ≡ readout twisted → ⊥
readouts-distinct e = true≢false (sym flat-readout ∙ e ∙ twisted-readout)

-- Verify that this concrete target is within the groupoid theorem's
-- scope, rather than assuming its truncation level from its name.
to-library : Cover.Circle → S1.S¹
to-library Cover.base = S1.base
to-library (Cover.loop i) = S1.loop i

from-library : S1.S¹ → Cover.Circle
from-library S1.base = Cover.base
from-library (S1.loop i) = Cover.loop i

circle-retract : (x : Cover.Circle) → from-library (to-library x) ≡ x
circle-retract Cover.base = refl
circle-retract (Cover.loop i) j = Cover.loop i

target-groupoid : isGroupoid (Ix.Index Cover.F)
target-groupoid = isGroupoidΣ
  (isSet→isGroupoid (isProp→isSet (λ _ _ → refl)))
  (λ _ → isGroupoidRetract to-library from-library circle-retract S1P.isGroupoidS¹)

module D = Descent.Descent f g target-groupoid

coherences-distinct : D.encode flat ≡ D.encode twisted → ⊥
coherences-distinct e = factors-distinct
  (sym (D.factor-roundtrip flat) ∙ cong D.decode e ∙ D.factor-roundtrip twisted)
