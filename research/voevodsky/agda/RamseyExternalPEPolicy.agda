{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyExternalPEPolicy where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (tt)
open import Agda.Builtin.String using (String)
import RamseyExternalPE as External
import NativeTableResolution as Resolution

module Policy (Source : Type) (payload : Source → String) (Allowed : Source → Type) where
  module T = External.Trees Source payload
  module G = External.G
  module N = External.N
  Good : T.Tree → Type
  Good (T.leaf s) = Allowed s
  Good (T.product I f) = (i : I) → Good (f i)
  Good (T.selection I f selected) = (i : I) → Good (f i)
  all-leaves : (t : T.Tree) → Good t → (o : T.Occurrence t) → Allowed (T.origin t o)
  all-leaves (T.leaf s) allowed tt = allowed
  all-leaves (T.product I f) good (i , o) = all-leaves (f i) (good i) o
  all-leaves (T.selection I f selected) good (i , o) = all-leaves (f i) (good i) o
  from-leaves : (t : T.Tree) → ((o : T.Occurrence t) → Allowed (T.origin t o)) → Good t
  from-leaves (T.leaf s) allowed = allowed tt
  from-leaves (T.product I f) allowed i = from-leaves (f i) (λ o → allowed (i , o))
  from-leaves (T.selection I f selected) allowed i = from-leaves (f i) (λ o → allowed (i , o))
  Admit : G.Package → Type (ℓ-suc ℓ-zero)
  Admit q = Σ Source (λ s → Σ (Allowed s) (λ _ → q ≡ T.encode (T.leaf s)))
  module R = Resolution.Full ℓ-zero Admit
  realize : (t : T.Tree) → Good t → R.Resolve (T.encode t)
  realize (T.leaf s) allowed = R.seed (s , (allowed , refl))
  realize (T.product I f) good = R.apply (N.P-kind , I , (λ i → T.encode (f i)))
    (λ { (lift i) → realize (f i) (good i) })
  realize (T.selection I f selected) good = R.apply (N.E-kind , I , (λ i → T.encode (f i)) , selected)
    (λ { (lift i) → realize (f i) (good i) })
