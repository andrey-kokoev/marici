{-# OPTIONS --safe --cubical --guardedness #-}
module TickSourceContractAudit where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.Sigma.Base using (_×_)
import TickRetainedStructure as S
module G = S.G

-- This audits only reconstruction and schedule-swap coherence. It does not
-- refute a lift satisfying further endpoint, analytic or naturality laws.
module AtSource (s : Bool × Bool) {ℓ : Level} (X : Type ℓ) where
  module T = S.AtSource s

  Semantics : Type ℓ
  Semantics = G.Schedule → X

  interpret : Semantics → T.A.Tick → X × X
  interpret f t = f (fst (T.tags t)) , f (snd (T.tags t))

  arbitrary-reconstruction : (f : Semantics) (t : T.A.Tick)
    → interpret f t ≡ interpret f (T.rebuild (T.tags t))
  arbitrary-reconstruction f = T.observation-factors (interpret f)

  swap : X × X → X × X
  swap (x , y) = y , x

  arbitrary-swap : (f : Semantics) (r q : G.Schedule)
    → interpret f (T.rebuild (q , r)) ≡ swap (interpret f (T.rebuild (r , q)))
  arbitrary-swap f r q = refl

  recover-semantics : (f : Semantics) (r : G.Schedule)
    → fst (interpret f (T.rebuild (r , r))) ≡ f r
  recover-semantics f r = refl

  -- Distinct external choices are not collapsed by these coherence laws.
  interpret-injective : (f g : Semantics)
    → interpret f ≡ interpret g → f ≡ g
  interpret-injective f g p = funExt λ r →
    cong (λ h → fst (h (T.rebuild (r , r)))) p
