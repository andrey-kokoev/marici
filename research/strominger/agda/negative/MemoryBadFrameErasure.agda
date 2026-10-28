{-# OPTIONS --safe --cubical --guardedness #-}
module MemoryBadFrameErasure where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (Bool; not)
import TaskRelativeMemoryCounterexample
-- Red and green differ by such a frame at B. It is not a morphism of
-- the frozen current-bit observation interface.
bad : (b : Bool) → not b ≡ b
bad b = refl
