{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverSignedNormalization where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.GroupoidLaws using (cong-∙; rCancel; lCancel)
open import Cubical.Data.Sigma.Base using (_,_; snd)
open import Cubical.Data.Unit.Base using (tt)
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc; _+_)
import Cubical.HITs.S1.Base as S1
import ObserverInternalComparison as C
import ObserverSignedCyclicCover as S
import ObserverWitnessRegression as W
import IndexIdentityCoherenceRegression as Cover

point : C.Reply → S1.S¹
point x = W.to-library (snd x)

back : S1.S¹ → C.Reply
back x = tt , W.from-library x

point-back : (x : S1.S¹) → point (back x) ≡ x
point-back S1.base = refl
point-back (S1.loop i) j = S1.loop i

Loop = C.base ≡ C.base
forward : Loop → S1.ΩS¹
forward = cong point
backward : S1.ΩS¹ → Loop
backward = cong back

forward-backward : (p : S1.ΩS¹) → forward (backward p) ≡ p
forward-backward p j i = point-back (p i) j

backward-forward : (p : Loop) → backward (forward p) ≡ p
backward-forward p j i = tt , W.circle-retract (snd (p i)) j

loop-integer-iso : Iso Loop ℤ
loop-integer-iso = compIso (iso forward backward forward-backward backward-forward) S1.ΩS¹Isoℤ

loop-integer-equivalence : Loop ≃ ℤ
loop-integer-equivalence = isoToEquiv loop-integer-iso

integer : Loop → ℤ
integer = Iso.fun loop-integer-iso
represent : ℤ → Loop
represent = Iso.inv loop-integer-iso

semantic-roundtrip : (p : Loop) → represent (integer p) ≡ p
semantic-roundtrip = Iso.leftInv loop-integer-iso
integer-roundtrip : (z : ℤ) → integer (represent z) ≡ z
integer-roundtrip = Iso.rightInv loop-integer-iso

composition : (p q : Loop) → integer (p ∙ q) ≡ integer p + integer q
composition p q = cong S1.winding (cong-∙ point p q) ∙ S1.winding-hom (forward p) (forward q)

evaluate : S.Signed → ℤ
evaluate S.stay = pos 0
evaluate S.up = pos 1
evaluate S.down = negsuc 0
evaluate (S.then u v) = evaluate u + evaluate v

code-correct : (w : S.Signed) → integer (S.path w) ≡ evaluate w
code-correct S.stay = refl
code-correct S.up = refl
code-correct S.down = refl
code-correct (S.then u v) = composition (S.path u) (S.path v)
  ∙ cong₂ _+_ (code-correct u) (code-correct v)

normalize : (w : S.Signed) → represent (evaluate w) ≡ S.path w
normalize w = sym (cong represent (code-correct w)) ∙ semantic-roundtrip (S.path w)

complete : (p q : Loop) → integer p ≡ integer q → p ≡ q
complete p q e = sym (semantic-roundtrip p) ∙ cong represent e ∙ semantic-roundtrip q

code-complete : (u v : S.Signed) → evaluate u ≡ evaluate v → S.path u ≡ S.path v
code-complete u v e = complete (S.path u) (S.path v)
  (code-correct u ∙ e ∙ sym (code-correct v))

code-necessary : (u v : S.Signed) → S.path u ≡ S.path v → evaluate u ≡ evaluate v
code-necessary u v e = sym (code-correct u) ∙ cong integer e ∙ code-correct v

cancel-up-down : S.path (S.then S.up S.down) ≡ S.path S.stay
cancel-up-down = rCancel (S.path S.up)
cancel-down-up : S.path (S.then S.down S.up) ≡ S.path S.stay
cancel-down-up = lCancel (S.path S.up)
