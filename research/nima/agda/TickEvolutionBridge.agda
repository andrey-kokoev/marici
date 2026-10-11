{-# OPTIONS --safe --cubical --guardedness #-}
module TickEvolutionBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (notEquiv)
open import Cubical.Data.Sigma.Base using (_×_)
import ObserverCoherenceCube as Source
import TickDiscreteReadout as Readout

module G = Source.Geometry Bool Bool notEquiv

-- An external realization contract, not an assertion of continuity.
-- To instantiate with real time and complex vectors, supply those types,
-- an evolution, and exact endpoint proofs (numerical tests do not suffice).
record EndpointModel (V P : Type) : Type where
  field
    encode : Bool × Bool → V
    zero end : P
    evolve : P → P → V → V
    at00 : (q : Bool × Bool) → evolve zero zero (encode q) ≡ encode q
    at10 : (q : Bool × Bool) → evolve end zero (encode q) ≡ encode (G.expandLeft q)
    at01 : (q : Bool × Bool) → evolve zero end (encode q) ≡ encode (G.expandRight q)
    at11 : (q : Bool × Bool) → evolve end end (encode q) ≡ encode (G.run G.leftFirst q)

module Bridge {V P : Type} (model : EndpointModel V P) (s : Bool × Bool) where
  open EndpointModel model
  module D = Readout.Readout notEquiv s
  open D.DiscreteReadout

  -- This function consumes an actual retained Tick, not hand-entered corners.
  realization : D.ATick → P → P → V
  realization t a b = evolve a b (encode (src (D.extract t)))

  source-preserved : (t : D.ATick) → realization t zero zero ≡ encode s
  source-preserved t = at00 (src (D.extract t)) ∙ cong encode (D.extract-source-attached t)

  left-preserved : (t : D.ATick) → realization t end zero ≡ encode (left-int (D.extract t))
  left-preserved t = at10 (src (D.extract t))

  right-preserved : (t : D.ATick) → realization t zero end ≡ encode (right-int (D.extract t))
  right-preserved t = at01 (src (D.extract t))

  run-independent : (r : G.Schedule) (q : Bool × Bool) → G.run G.leftFirst q ≡ G.run r q
  run-independent G.leftFirst q = refl
  run-independent G.rightFirst q = refl

  target-preserved : (t : D.ATick) → realization t end end ≡ encode (tgt (D.extract t))
  target-preserved t = at11 (src (D.extract t)) ∙ cong encode
    (run-independent (schedule-first (D.extract t)) (src (D.extract t))
      ∙ fst (D.extract-target-equals-run t))

  -- Only the return section's endpoints are interpreted here. Its dependent
  -- interior is not identified with evolve or with a real-time return path.
  return-start-preserved : (t : D.ATick)
    → encode (D.Ret.RetainedReturn.return-section (D.ATick.returned t) i0 i0)
      ≡ encode (return-starts-at (D.extract t))
  return-start-preserved t = cong encode (D.extract-return-starts-at-target t)

  return-end-preserved : (t : D.ATick)
    → encode (D.Ret.RetainedReturn.return-section (D.ATick.returned t) i1 i1)
      ≡ encode (return-ends-at (D.extract t))
  return-end-preserved t = cong encode (D.extract-return-ends-at-source t)

  -- Execute the actual retained schedule, including its intermediate corner.
  execute : G.Schedule → V → V
  execute G.leftFirst v = evolve zero end (evolve end zero v)
  execute G.rightFirst v = evolve end zero (evolve zero end v)

  execute-law : (r : G.Schedule) (q : Bool × Bool) → execute r (encode q) ≡ encode (G.run r q)
  execute-law G.leftFirst q = cong (evolve zero end) (at10 q) ∙ at01 (G.expandLeft q)
  execute-law G.rightFirst q = cong (evolve end zero) (at01 q) ∙ at10 (G.expandRight q)

  first-preserved : (t : D.ATick)
    → execute (schedule-first (D.extract t)) (encode (src (D.extract t))) ≡ encode (tgt (D.extract t))
  first-preserved t = execute-law (schedule-first (D.extract t)) (src (D.extract t))
    ∙ cong encode (fst (D.extract-target-equals-run t))

  second-preserved : (t : D.ATick)
    → execute (schedule-second (D.extract t)) (encode (src (D.extract t))) ≡ encode (tgt (D.extract t))
  second-preserved t = execute-law (schedule-second (D.extract t)) (src (D.extract t))
    ∙ cong encode (snd (D.extract-target-equals-run t))

-- A concrete exact finite instance establishes that the contract is inhabited.
-- It is NOT a continuous matrix model.
finiteEvolution : Bool → Bool → Bool × Bool → Bool × Bool
finiteEvolution false false q = q
finiteEvolution true false q = G.expandLeft q
finiteEvolution false true q = G.expandRight q
finiteEvolution true true q = G.run G.leftFirst q

finiteModel : EndpointModel (Bool × Bool) Bool
EndpointModel.encode finiteModel q = q
EndpointModel.zero finiteModel = false
EndpointModel.end finiteModel = true
EndpointModel.evolve finiteModel = finiteEvolution
EndpointModel.at00 finiteModel q = refl
EndpointModel.at10 finiteModel q = refl
EndpointModel.at01 finiteModel q = refl
EndpointModel.at11 finiteModel q = refl

module FiniteBridge = Bridge finiteModel (false , false)

fresh-target : FiniteBridge.realization FiniteBridge.D.fresh true true ≡ (true , true)
fresh-target = refl

swapped-target : FiniteBridge.realization FiniteBridge.D.swapped true true ≡ (true , true)
swapped-target = refl
