{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPassiveEPPort where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Agda.Builtin.String using (String)
import RamseyExternalPE as External
import RamseyExternalPEPolicy as Policy

-- E is a retained contextual input, never falsely typed as a PN permit.
-- PN requests use the existing selected-span constructor on the target P chart.
module Passive (Chart Face : Type) (Permit : Chart → Face → Type)
  (packet : (c : Chart) (f : Face) → Permit c f → String)
  (electron : Chart → String) where
  module S = External.TracedSpans Chart Face Permit packet
  data Source : Type where
    e : Chart → Source
    p : S.S.InputIndex → Source
  payload : Source → String
  payload (e c) = electron c
  payload (p (c , (f , witness))) = packet c f witness
  module T = External.Trees Source payload
  embed : S.T.Tree → T.Tree
  embed (S.T.leaf s) = T.leaf (p s)
  embed (S.T.product I f) = T.product I (λ i → embed (f i))
  embed (S.T.selection I f i) = T.selection I (λ j → embed (f j)) i
  embed-cell : (t : S.T.Tree) → T.encode (embed t) ≡ S.T.encode t
  embed-cell (S.T.leaf s) = refl
  embed-cell (S.T.product I f) = cong (External.N.Pi-package I) (funExt (λ i → embed-cell (f i)))
  embed-cell (S.T.selection I f i) = cong (λ g → External.N.E-package I g i) (funExt (λ j → embed-cell (f j)))
  branch : (c : Chart) (f : Face) → Permit c f → Bool → T.Tree
  branch c f witness false = T.leaf (e c)
  branch c f witness true = embed (S.selected c c (f , (witness , witness)))
  context : (c : Chart) (f : Face) → Permit c f → T.Tree
  context c f witness = T.product Bool (branch c f witness)
  pn-package-cell : (c : Chart) (f : Face) (witness : Permit c f)
    → T.encode (branch c f witness true) ≡ S.S.selected-package c c (f , (witness , witness))
  pn-package-cell c f witness = embed-cell (S.selected c c (f , (witness , witness))) ∙ S.selected-cell c c (f , (witness , witness))
  module Both = Policy.Policy Source payload (λ _ → Unit)
  good : (t : T.Tree) → Both.Good t
  good (T.leaf s) = tt
  good (T.product I f) = λ i → good (f i)
  good (T.selection I f i) = λ j → good (f j)
  native : (c : Chart) (f : Face) (witness : Permit c f)
    → Both.R.Resolve (T.encode (context c f witness))
  native c f witness = Both.realize (context c f witness) (good (context c f witness))
  EOnly : Source → Type
  EOnly (e c) = Unit
  EOnly (p i) = ⊥
  module Only = Policy.Policy Source payload EOnly
  -- Necessity for this explicit external compiler, not all possible Resolve proofs.
  needs-target : (c : Chart) (f : Face) (witness : Permit c f)
    → Only.Good (context c f witness) → ⊥
  needs-target c f witness admitted = admitted true (f , (witness , witness)) S.S.source-leg
  retained-E : (c : Chart) (f : Face) (witness : Permit c f)
    → T.origin (context c f witness) (false , tt) ≡ e c
  retained-E c f witness = refl
  retained-PN : (c : Chart) (f : Face) (witness : Permit c f)
    → T.origin (context c f witness) (true , ((f , (witness , witness)) , (S.S.target-leg , tt))) ≡ p (c , (f , witness))
  retained-PN c f witness = refl
