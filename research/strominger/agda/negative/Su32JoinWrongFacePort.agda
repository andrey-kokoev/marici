{-# OPTIONS --safe --cubical --guardedness #-}
module Su32JoinWrongFacePort where
open import Cubical.Data.Bool.Base using (false)
open import Su32JoinGeometry
bad : Contact comparison target
bad = Frame.toC frame false
