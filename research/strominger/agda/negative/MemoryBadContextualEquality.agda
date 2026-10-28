{-# OPTIONS --safe --cubical --guardedness #-}
module MemoryBadContextualEquality where
open import Cubical.Foundations.Prelude
import TaskRelativeMemoryCounterexample as M
bad : M.ContextuallyEqual
bad v w = refl
