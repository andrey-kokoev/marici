{-# OPTIONS --safe --cubical --guardedness #-}
module MetaWitnessNativeBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true; false)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeApplicationExtension as Application
import GeneratingGrammarMacros as Macros
import NativeApplicationGate as Gate
import MetaWitnessGenerator as Meta
open import TypedGeneratorLayers using (Layer1)

-- Any compiled WG may be executed through the separately admitted native
-- application extension. This does not assert a derivation in the old 12 rules.
module Bridge (ℓ : Level) (L : Layer1 ℓ) where
  module G = Tables.Core ℓ
  module N = Rules.Native ℓ
  module E = Application.Extension ℓ
  open Layer1 L

  output-type : State → Type ℓ
  output-type s = Σ[ t ∈ State ] Witness s t

  -- The WG is represented as a native P-family of pointwise result packages.
  -- Constructing the *syntax* of this family does not derive its components.
  component : State → G.Package
  component s = N.pack (G.atom-node (output-type s)) (generate s)

  application : State → E.Application
  application s = record
    { A = State ; B = output-type
    ; argument-code = G.atom-node State
    ; result-code = λ x → G.atom-node (output-type x)
    ; function-code = G.P-node State (λ x → N.retained (component x))
    ; function = generate ; argument = s }

  function-is-certified-family-shape : (s : State)
    → E.function-input (application s) ≡ N.Pi-package State component
  function-is-certified-family-shape s = refl

  module Runtime (Admit : G.Package → Type (ℓ-suc ℓ)) where
    module RT = E.Runtime Admit
    witnessed-step : (s : State)
      → RT.New.Resolve (E.function-input (application s))
      → RT.New.Resolve (E.argument-input (application s))
      → RT.New.Resolve (E.result (application s))
    witnessed-step s df ds = RT.execute (application s) df ds

    beta-witness : (s : State)
      (df : RT.New.Resolve (E.function-input (application s)))
      (ds : RT.New.Resolve (E.argument-input (application s)))
      → RT.New.Resolve (E.beta-package (application s))
    beta-witness s df ds = RT.coherencer (application s) (witnessed-step s df ds)

    retained-derivation : (s : State)
      (df : RT.New.Resolve (E.function-input (application s)))
      (ds : RT.New.Resolve (E.argument-input (application s)))
      → RT.New.Resolve (E.combined (application s))
    retained-derivation s df ds = RT.assemble (application s) (witnessed-step s df ds)

    step-value : (s : State)
      → N.value (E.result (application s)) ≡ generate s
    step-value s = refl

module Boolean = Bridge ℓ-zero Meta.BooleanSpecialized.domain-WG

module BooleanFixture where
  module E = Application.Extension ℓ-zero
  module G = Tables.Core ℓ-zero
  state : Meta.BooleanSpecialized.State
  state = true , true

  data Seed : G.Package → Type (ℓ-suc ℓ-zero) where
    function-seed : Seed (E.function-input (Boolean.application state))
    argument-seed : Seed (E.argument-input (Boolean.application state))

  module Run = Boolean.Runtime Seed
  function-derivation : Run.RT.New.Resolve (E.function-input (Boolean.application state))
  function-derivation = Run.RT.New.seed function-seed
  argument-derivation : Run.RT.New.Resolve (E.argument-input (Boolean.application state))
  argument-derivation = Run.RT.New.seed argument-seed
  result-derivation : Run.RT.New.Resolve (E.result (Boolean.application state))
  result-derivation = Run.witnessed-step state function-derivation argument-derivation
  law-and-step-derivation : Run.RT.New.Resolve (E.combined (Boolean.application state))
  law-and-step-derivation = Run.retained-derivation state function-derivation argument-derivation
  native-law-readout :
    fst (fst (Boolean.N.value (E.result (Boolean.application state)))) ≡ false
  native-law-readout = Meta.BooleanSpecialized.law-from-step false true

  -- The old-rule invariant makes the cost of any purported old derivation
  -- explicit: it must yield an admission proof for this principal atom.
  module Old = Gate.Invariant ℓ-zero
  module OldPolicy = Old.Policy Seed
  old-step-needs-result-seed :
    OldPolicy.Run.Resolve (E.result (Boolean.application state))
    → Seed (E.result (Boolean.application state))
  old-step-needs-result-seed d = OldPolicy.atomic-needs-admission d refl

-- The only old-rule alternative is to start with a *certified family of
-- outputs*. Its selected premise is already a derivation of the result;
-- Pi packaging does not compute it from an opaque WG seed.
module CertifiedFamilyAlternative
  (Admit : Tables.Core.Package ℓ-zero → Type (ℓ-suc ℓ-zero)) where
  module E = Application.Extension ℓ-zero
  module G = Tables.Core ℓ-zero
  module Old = Macros.Retained ℓ-zero Admit
  State = Meta.BooleanSpecialized.State
  outputs : State → G.Package
  outputs = Boolean.component
  module Family (all-results : (s : State) → Old.Run.Resolve (outputs s)) where
    stored : Old.Run.Resolve (Old.family State outputs)
    stored = Old.family-run State outputs all-results
    matches-function-input : (s : State)
      → Old.family State outputs ≡ E.function-input (Boolean.application s)
    matches-function-input s = refl
    selected : (s : State)
      → Old.Run.premise (Old.family State outputs , stored) (lift s)
        ≡ (outputs s , all-results s)
    selected s = Old.family-premise State outputs all-results s
