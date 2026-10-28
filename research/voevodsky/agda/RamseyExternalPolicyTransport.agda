{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyExternalPolicyTransport where
open import Cubical.Foundations.Prelude
open import Agda.Builtin.String using (String)
import RamseyExternalPE as External
import RamseyExternalPEPolicy as Policy

module Transfer (Source : Type) (payload : Source → String)
  (Allowed Before : Source → Type) where
  module T = External.Trees Source payload
  module A = Policy.Policy Source payload Allowed
  module B = Policy.Policy Source payload Before
  -- Every target occurrence must have an admitted source occurrence.
  -- This does not omit unselected E prerequisites.
  transfer : (s t : T.Tree)
    (back : T.Occurrence t → T.Occurrence s)
    (admission : (o : T.Occurrence t) → Allowed (T.origin s (back o)) → Before (T.origin t o))
    → A.Good s → B.Good t
  transfer s t back admission good =
    B.from-leaves t (λ o → admission o (A.all-leaves s good (back o)))
