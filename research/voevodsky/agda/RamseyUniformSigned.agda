{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyUniformSigned where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (zero; suc)
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc; _+_)
import Cubical.Data.Int.Properties as Z
open import Cubical.Relation.Nullary using (Discrete; yes; no)
open import Agda.Builtin.String using (String)
open import RamseyUniformRelative

Point3 : Type
Point3 = Σ ℤ (λ _ → Σ ℤ (λ _ → ℤ))
zero3 : Point3
zero3 = pos zero , (pos zero , pos zero)
add3 : Point3 → Point3 → Point3
add3 (x , (y , z)) (u , (v , w)) = (x + u) , ((y + v) , (z + w))
discrete3 : Discrete Point3
discrete3 (x , (y , z)) (u , (v , w)) with Z.discreteℤ x u | Z.discreteℤ y v | Z.discreteℤ z w
... | yes p | yes q | yes r = yes (λ i → p i , (q i , r i))
... | no p | _ | _ = no (λ h → p (cong fst h))
... | _ | no q | _ = no (λ h → q (cong (λ a → fst (snd a)) h))
... | _ | _ | no r = no (λ h → r (cong (λ a → snd (snd a)) h))
signed-geometry : Geometry
Geometry.Point signed-geometry = Point3
Geometry.origin signed-geometry = zero3
Geometry.add signed-geometry = add3
Geometry.decide signed-geometry = discrete3
Geometry.unit-left signed-geometry (x , (y , z)) i = sym (Z.pos0+ x) i , (sym (Z.pos0+ y) i , sym (Z.pos0+ z) i)
Geometry.assoc signed-geometry (x , (y , z)) (u , (v , w)) (a , (b , c)) i =
  sym (Z.+Assoc x u a) i , (sym (Z.+Assoc y v b) i , sym (Z.+Assoc z w c) i)
Geometry.comm signed-geometry (x , (y , z)) (u , (v , w)) i = Z.+Comm x u i , (Z.+Comm y v i , Z.+Comm z w i)

-- A radius-zero input list, a negative letter, and arbitrary n are all legal.
negative-letter : Slot 1 → Point3
negative-letter first = negsuc zero , (negsuc zero , pos zero)
origin-list : Slot 1 → Point3
origin-list first = zero3
context-list : Slot 1 → String
context-list first = "opaque-origin-context"
color-list : Slot 1 → Slot 2
color-list first = next first
module ZeroWord = Compiler signed-geometry 1 1 0 2 negative-letter origin-list context-list color-list
zero-word-derivation : ZeroWord.R.Resolve (ZeroWord.result-package nil)
zero-word-derivation = ZeroWord.result nil
module NegativeWord = Compiler signed-geometry 1 1 1 2 negative-letter origin-list context-list color-list
negative-request : NegativeWord.Request
negative-request = cons first nil
negative-word-derivation : NegativeWord.R.Resolve (NegativeWord.result-package negative-request)
negative-word-derivation = NegativeWord.result negative-request
negative-refusal : NegativeWord.L.Missing origin-list (NegativeWord.A.phi negative-request)
negative-refusal first p = Z.posNotnegsuc 0 0 (cong fst p)
