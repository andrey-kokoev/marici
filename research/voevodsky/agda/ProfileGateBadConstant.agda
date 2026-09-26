{-# OPTIONS --safe --cubical --guardedness #-}
module ProfileGateBadConstant where
open import Cubical.Foundations.Prelude
import ProfileBoundNativeGate as P
import RetainedLocalTidalOverlap as L
-- Required component of authorizing the wave-valued constant reader at NEW.
bad : snd (L.fine-reading L.rosen) ≡ snd (L.fine-reading L.newtonian)
bad = refl
