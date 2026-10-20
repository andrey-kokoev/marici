{-# OPTIONS --safe --cubical --guardedness #-}
module InterchangeHiddenFiberObstruction where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Relation.Nullary.Base using (¬_)
open import NativeExtensionFamilyAudit using (Vertex; A; B; D; AB; AD)
open import SourceIndexedExtensionFamilies using (Out)

-- A different contract with extra noncontractible witness content. This is NOT
-- a counterexample to the exact outgoing-edge family used in the positive test.
Carrier : Type
Carrier = Out A × (Bool × Bool)
readPort : Carrier → Vertex
readPort z = fst (fst z)
swap : Carrier → Carrier
swap (edge , x , y) = edge , y , x
swap² : (z : Carrier) → swap (swap z) ≡ z
swap² z = refl
identityEquiv swapEquiv : Carrier ≃ Carrier
identityEquiv = idEquiv Carrier
swapEquiv = isoToEquiv (iso swap swap swap² swap²)
selected : Carrier
selected = (D , AD) , false , false
selected-fixed : equivFun swapEquiv selected ≡ selected
selected-fixed = refl
ports-fixed : (z : Carrier) → readPort (equivFun swapEquiv z) ≡ readPort z
ports-fixed z = refl
no-higher-comparison : ¬ (identityEquiv ≡ swapEquiv)
no-higher-comparison p = false≢true
  (cong (λ e → fst (snd (equivFun e ((B , AB) , false , true)))) p)
