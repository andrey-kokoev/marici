{-# OPTIONS --safe --cubical --guardedness #-}
module negative.SubstitutionBadTruthTest where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Unit using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; false)
open import UniversalSubstitution
-- EXPECTED FAILURE: the constant extension cannot recover an arbitrary
-- Bool-valued continuation, despite passing every propositional target.
bad : Iso (Unit → Bool) (Bool → Bool)
Iso.fun bad = Substitution.pre Bool Unit collapse Bool
Iso.inv bad h tt = h false
Iso.rightInv bad h = funExt (λ b → refl)
Iso.leftInv bad k = funExt (λ { tt → refl })
