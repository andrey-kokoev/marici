{-# OPTIONS --safe --cubical --guardedness #-}
module negative.FibrationBadProductDecoder where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Unit.Properties using (isPropUnit)
open import Cubical.Data.Sigma.Base using (_×_)
-- EXPECTED FAILURE: regrouped rows do not have the product's value type.
bad : Iso (Bool × Unit) (Bool → Unit)
Iso.fun bad r b = tt
Iso.inv bad f = false , tt
Iso.rightInv bad f = funExt (λ b → isPropUnit tt (f b))
Iso.leftInv bad (b , tt) = refl
