{-# OPTIONS --safe --cubical --guardedness #-}
module RamseySingleFrameBadRoleChange where
open import Cubical.Foundations.Prelude
open import RamseySingleFrameFaces
swap : Vertex → Vertex
swap c0 = m0
swap m0 = c0
swap c1 = c1
swap m1 = m1
bad : M-role (swap c0) ≡ M-role c0
bad = refl
