{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverRRCInternalInterface where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Base using (_,_; fst; snd)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as W
import WholePackageResolution as RRC
import ObserverRRCRecursiveBridge as Recursive
import ObserverInternalInterface as O
import ObserverNonuniqueHistory as H

module U = W.Universe ℓ-zero
module R = RRC.Generators ℓ-zero
module B = Recursive.Bridge ℓ-zero

-- Fixed primitive access capabilities. These source constructors retain
-- the actual observed history; they are NOT derived from bare composition.
data Source : U.Complete → Type₁ where
  result-access : (h : H.History) → Source (U.pack (U.atom Unit) tt)
  rule-access : (h : H.History) → Source (U.pack (U.atom Bool) (H.rule-observer h))

pair-family : U.Complete → U.Complete → Bool → U.Complete
pair-family a b true = a
pair-family a b false = b

compile : O.Code → H.History → U.Complete
compile O.result h = U.pack (U.atom Unit) tt
compile O.rule h = U.pack (U.atom Bool) (H.rule-observer h)
compile (O.both c d) h = U.Pi-package Bool (pair-family (compile c h) (compile d h))

build : (c : O.Code) (h : H.History) → R.Resolve Source (compile c h)
build O.result h = R.seed (result-access h)
build O.rule h = R.seed (rule-access h)
build (O.both c d) h = R.apply
  (R.Pi-rule Bool (pair-family (compile c h) (compile d h)))
  (λ { (lift true) → build c h ; (lift false) → build d h })

readback : (c : O.Code) (h : H.History) → U.El (U.expression (compile c h)) → O.Reply c
readback O.result h v = v
readback O.rule h v = v
readback (O.both c d) h v = readback c h (v true) , readback d h (v false)

write-reply : (c : O.Code) (h : H.History) → O.Reply c → U.El (U.expression (compile c h))
write-reply O.result h v = v
write-reply O.rule h v = v
write-reply (O.both c d) h v true = write-reply c h (fst v)
write-reply (O.both c d) h v false = write-reply d h (snd v)

reply-roundtrip : (c : O.Code) (h : H.History) (v : O.Reply c)
  → readback c h (write-reply c h v) ≡ v
reply-roundtrip O.result h v = refl
reply-roundtrip O.rule h v = refl
reply-roundtrip (O.both c d) h v i = reply-roundtrip c h (fst v) i , reply-roundtrip d h (snd v) i

native-roundtrip : (c : O.Code) (h : H.History) (v : U.El (U.expression (compile c h)))
  → write-reply c h (readback c h v) ≡ v
native-roundtrip O.result h v = refl
native-roundtrip O.rule h v = refl
native-roundtrip (O.both c d) h v = funExt λ
  { true → native-roundtrip c h (v true) ; false → native-roundtrip d h (v false) }

reply-equivalence : (c : O.Code) (h : H.History) → U.El (U.expression (compile c h)) ≃ O.Reply c
reply-equivalence c h = isoToEquiv
  (iso (readback c h) (write-reply c h) (reply-roundtrip c h) (native-roundtrip c h))

view : (c : O.Code) → H.History → O.Reply c
view c h = readback c h (U.value (compile c h))

view-agrees : (c : O.Code) (h : H.History) → view c h ≡ O.readout c h
view-agrees O.result h = refl
view-agrees O.rule h = refl
view-agrees (O.both c d) h i = view-agrees c h i , view-agrees d h i

faithful : {c : O.Code} (access : O.RuleAccess c) (h : H.History)
  → O.recover access (view c h) ≡ h
faithful {c} access h = cong (O.recover access) (view-agrees c h) ∙ O.faithful access h

noninterference : {c : O.Code} → O.ResultOnly c → (h k : H.History) → view c h ≡ view c k
noninterference {c} access h k = view-agrees c h ∙ O.noninterference access h k ∙ sym (view-agrees c k)

no-result-only-recovery : {c : O.Code} (access : O.ResultOnly c) (recover : O.Reply c → H.History)
  → ((h : H.History) → recover (view c h) ≡ h) → ⊥
no-result-only-recovery access recover exact = H.histories-distinct
  (sym (exact H.red-history) ∙ cong recover (noninterference access H.red-history H.blue-history)
    ∙ exact H.blue-history)

-- The actual native premise histories survive the recursive DSC syntax.
translated : (c : O.Code) (h : H.History) → B.Term Source (compile c h)
translated c h = B.encode (build c h)

history-roundtrip : (c : O.Code) (h : H.History) → B.decode (translated c h) ≡ build c h
history-roundtrip c h = B.decode-encode (build c h)

-- Noninterference is for the declared Reply view, NOT an assertion that
-- arbitrary inspection of the retained source-history provenance is blind.
