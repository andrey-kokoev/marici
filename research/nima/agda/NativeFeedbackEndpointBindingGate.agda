{-# OPTIONS --safe --cubical --guardedness #-}
module NativeFeedbackEndpointBindingGate where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
import NativePromotionConstructorTrace as Trace
import NativeFeedbackRouteReadout as Source

module F = Trace.F
module Before = Trace.Before
module After = Trace.After

-- The actual constructor's outer presentation endpoints. They are NOT
-- labels or the enclosed payload's record ports.
from : Before.Compared → After.H.Presentation
from c = After.Compared.source (F.run c)
to : Before.Compared → After.H.Presentation
to c = After.Compared.target (F.run c)

from-equal : (c d : Before.Compared) → from c ≡ from d
from-equal c d = F.run-source c ∙ sym (F.run-source d)
to-equal : (c d : Before.Compared) → to c ≡ to d
to-equal c d = F.run-target c ∙ sym (F.run-target d)

-- Exactly the endpoint-uniqueness condition used by TableFibrationCycle,
-- specialized without forcing unrelated universes into one Table signature.
UniqueOuterEndpoints : Type _
UniqueOuterEndpoints = (c d : Before.Compared)
  → from c ≡ from d → to c ≡ to d → c ≡ d

unique-forces-all-inputs-equal : UniqueOuterEndpoints
  → (c d : Before.Compared) → c ≡ d
unique-forces-all-inputs-equal unique c d = unique c d (from-equal c d) (to-equal c d)

-- Use an EXISTING distinguishable native pair, not a new numerical fixture.
outer-endpoint-binding-rejected : UniqueOuterEndpoints → ⊥
outer-endpoint-binding-rejected unique = Source.reading-changes
  (cong Source.reading (unique-forces-all-inputs-equal unique
    (F.exchange Trace.input) Trace.input))

-- The distinction survives the actual native promotion. Thus its retention
-- theorem does not repair the collision of its outer endpoint fields.
promoted-pair-distinct : F.run (F.exchange Trace.input) ≡ F.run Trace.input → ⊥
promoted-pair-distinct p = Trace.inherited-distinction (cong Trace.inherited-question p)

-- A constructive endpoint refinement uses the ACTUAL decoded payload, not
-- an arbitrary fresh identifier. It exposes retained information as wiring.
RefinedPort : Type _
RefinedPort = Σ After.H.Presentation (λ _ → Before.Compared)

refined-from refined-to : Before.Compared → RefinedPort
refined-from c = from c , F.decode (F.run c)
refined-to c = to c , F.decode (F.run c)

UniqueRefinedEndpoints : Type _
UniqueRefinedEndpoints = (c d : Before.Compared)
  → refined-from c ≡ refined-from d → refined-to c ≡ refined-to d → c ≡ d

refined-endpoints-unique : UniqueRefinedEndpoints
refined-endpoints-unique c d ps pt = sym (F.decode-run c)
  ∙ cong snd ps ∙ F.decode-run d

refined-payload-recovered : (c : Before.Compared) → snd (refined-from c) ≡ c
refined-payload-recovered = F.decode-run

-- The refined ports distinguish full payloads and therefore change context
-- incidence. Their selection as physical/table endpoints is NOT automatic.
-- No rejection of Feedback.run without endpoint uniqueness is claimed.
