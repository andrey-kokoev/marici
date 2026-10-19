{-# OPTIONS --safe --cubical --guardedness #-}
module SpokeBadDirectedCompletion where

open import Cubical.Foundations.Prelude

data Vertex : Type where
  A B C D : Vertex

data Arrow : Vertex → Vertex → Type where
  AB : Arrow A B
  AC : Arrow A C
  AD : Arrow A D

-- Deliberate rejection control: a directed spoke is not a branch comparison.
badBC : Arrow B C
badBC = AB
