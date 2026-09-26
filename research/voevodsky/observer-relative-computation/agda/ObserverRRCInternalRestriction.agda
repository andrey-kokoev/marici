{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverRRCInternalRestriction where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Bool.Base using (true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Unit.Base using (tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.HITs.PropositionalTruncation.Base using (∥_∥₁; squash₁)
import Cubical.HITs.PropositionalTruncation.Properties as Trunc
import ObserverInternalInterface as O
import ObserverInternalRestriction as Restriction
import ObserverAccessClassification as Access
import ObserverNonuniqueHistory as H
import ObserverRRCInternalInterface as Native
import ResolutionNetDependentSubstitution as DSC
module D = DSC.Dependent {ℓ-zero}
module U = Native.U

Reply : O.Code → H.History → Type
Reply c h = U.El (U.expression (Native.compile c h))

-- Structural compilation, not an arbitrary reply-function field.
run : {c d : O.Code} → Restriction.Restrict c d → (h : H.History) → Reply c h → Reply d h
run Restriction.identity h v = v
run Restriction.discard h v = tt
run Restriction.left h v = v true
run Restriction.right h v = v false
run (Restriction.pair r s) h v true = run r h v
run (Restriction.pair r s) h v false = run s h v
run (Restriction.then r s) h = D.compose (run s h) (run r h)

correct : {c d : O.Code} (r : Restriction.Restrict c d) (h : H.History) (v : Reply c h)
  → Native.readback d h (run r h v) ≡ Restriction.run r (Native.readback c h v)
correct Restriction.identity h v = refl
correct Restriction.discard h v = refl
correct Restriction.left h v = refl
correct Restriction.right h v = refl
correct (Restriction.pair r s) h v i = correct r h v i , correct s h v i
correct (Restriction.then r s) h v = correct s h (run r h v) ∙ cong (Restriction.run s) (correct r h v)

preserves : {c d : O.Code} (r : Restriction.Restrict c d) (h : H.History)
  → run r h (U.value (Native.compile c h)) ≡ U.value (Native.compile d h)
preserves Restriction.identity h = refl
preserves Restriction.discard h = refl
preserves Restriction.left h = refl
preserves Restriction.right h = refl
preserves (Restriction.pair r s) h = funExt λ { true → preserves r h ; false → preserves s h }
preserves (Restriction.then r s) h = cong (run s h) (preserves r h) ∙ preserves s h

readback-injective : (c : O.Code) (h : H.History) (v w : Reply c h)
  → Native.readback c h v ≡ Native.readback c h w → v ≡ w
readback-injective c h v w p = sym (Native.native-roundtrip c h v)
  ∙ cong (Native.write-reply c h) p ∙ Native.native-roundtrip c h w

-- Certificates concern the reply image, NOT validation of all metadata
-- or authority to inspect the full retained history indexed by h.
Image : O.Code → H.History → Type
Image c h = Σ (Reply c h) (λ v → ∥ Σ H.History (λ k → O.readout c k ≡ Native.readback c h v) ∥₁)

to-image : {c : O.Code} {h : H.History} → Image c h → Access.Image c
to-image {c} {h} (v , origin) = Native.readback c h v , origin

image-map : {c d : O.Code} (r : Restriction.Restrict c d) (h : H.History) → Image c h → Image d h
image-map r h (v , origin) = run r h v , Trunc.map
  (λ { (k , e) → k , sym (Restriction.preserves r k) ∙ cong (Restriction.run r) e ∙ sym (correct r h v) }) origin

coherent : {c d : O.Code} (r s : Restriction.Restrict c d) (h : H.History) (v : Image c h)
  → image-map r h v ≡ image-map s h v
coherent {d = d} r s h v = Σ≡Prop (λ _ → squash₁)
  (readback-injective d h (run r h (fst v)) (run s h (fst v))
    (correct r h (fst v) ∙ cong fst (Restriction.coherent r s (to-image v)) ∙ sym (correct s h (fst v))))

image-identity : {c : O.Code} (h : H.History) (v : Image c h) → image-map Restriction.identity h v ≡ v
image-identity h v = Σ≡Prop (λ _ → squash₁) refl

image-composition : {c d e : O.Code} (r : Restriction.Restrict c d) (s : Restriction.Restrict d e)
  (h : H.History) (v : Image c h)
  → image-map (Restriction.then r s) h v ≡ image-map s h (image-map r h v)
image-composition r s h v = Σ≡Prop (λ _ → squash₁) refl

raw : (h : H.History) → Reply (O.both O.rule O.rule) h
raw h true = true
raw h false = false

raw-projections-differ : (h : H.History)
  → run (Restriction.left {O.rule} {O.rule}) h (raw h)
    ≡ run (Restriction.right {O.rule} {O.rule}) h (raw h) → ⊥
raw-projections-differ h = true≢false

no-raw-origin : (h : H.History)
  → ∥ Σ H.History (λ k → O.readout (O.both O.rule O.rule) k
      ≡ Native.readback (O.both O.rule O.rule) h (raw h)) ∥₁ → ⊥
no-raw-origin h origin = raw-projections-differ h
  (cong fst (coherent (Restriction.left {O.rule} {O.rule})
    (Restriction.right {O.rule} {O.rule}) h (raw h , origin)))

no-information-gain : Restriction.Restrict O.result O.rule → ⊥
no-information-gain = Restriction.no-information-gain
