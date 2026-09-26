{-# OPTIONS --safe --cubical --guardedness #-}
module negative.QBooleanityBadInverse where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false)
open import Cubical.Relation.Nullary.Base using (¬_)
open import Cubical.Relation.Nullary.Properties using (isProp¬)
open import QBooleanity using (D; eta)
-- EXPECTED FAILURE: truth reflection cannot recover the retained Bool choice.
bad : Iso Bool (D Bool)
Iso.fun bad = eta
Iso.inv bad d = false
Iso.rightInv bad d = isProp¬ (¬ Bool) _ d
Iso.leftInv bad x = refl
