{-# OPTIONS --safe --cubical --guardedness #-}
module TickPolynomialRealization where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Algebra.Ring.Base
open import Cubical.Algebra.Ring.Properties using (module RingTheory)
open import TickEvolutionBridge

-- Exact four-coordinate algebra, not floating-point validation.
-- For a topological ring this formula is polynomial and hence continuous,
-- but topology/continuity and unitarity are NOT proved in this module.
module Polynomial (K : Ring ℓ-zero) where
  open RingStr (snd K)
  open RingTheory K
  Scalar = fst K
  Vector = Bool × Bool → Scalar

  delta : Bool → Bool → Scalar
  delta false false = 1r
  delta false true = 0r
  delta true false = 0r
  delta true true = 1r

  basis : Bool × Bool → Vector
  basis (u , v) (x , y) = delta u x · delta v y

  delta-flip : (u x : Bool) → delta u (G.expand x) ≡ delta (G.expand u) x
  delta-flip false false = refl
  delta-flip false true = refl
  delta-flip true false = refl
  delta-flip true true = refl

  L R : Vector → Vector
  L v (x , y) = v (G.expand x , y)
  R v (x , y) = v (x , G.expand y)

  L-basis : (q : Bool × Bool) → L (basis q) ≡ basis (G.expandLeft q)
  L-basis (u , v) = funExt λ { (x , y) → cong (_· delta v y) (delta-flip u x) }

  R-basis : (q : Bool × Bool) → R (basis q) ≡ basis (G.expandRight q)
  R-basis (u , v) = funExt λ { (x , y) → cong (delta u x ·_) (delta-flip v y) }

  -- T_A(a) = (1-a) I + a A. Unlike the phase/exponential checker,
  -- this is generally not norm preserving.
  leg : (Vector → Vector) → Scalar → Vector → Vector
  leg A a v q = (1r + (- a)) · v q + a · A v q

  leg-zero : (A : Vector → Vector) (v : Vector) → leg A 0r v ≡ v
  leg-zero A v = funExt λ q →
    cong₂ _+_
      (cong (_· v q) (cong (1r +_) 0Selfinverse ∙ +IdR 1r) ∙ ·IdL (v q))
      (0LeftAnnihilates (A v q)) ∙ +IdR (v q)

  leg-one : (A : Vector → Vector) (v : Vector) → leg A 1r v ≡ A v
  leg-one A v = funExt λ q →
    cong₂ _+_
      (cong (_· v q) (+InvR 1r) ∙ 0LeftAnnihilates (v q))
      (·IdL (A v q)) ∙ +IdL (A v q)

  U : Scalar → Scalar → Vector → Vector
  U a b v = leg R b (leg L a v)

  model : EndpointModel Vector Scalar
  EndpointModel.encode model = basis
  EndpointModel.zero model = 0r
  EndpointModel.end model = 1r
  EndpointModel.evolve model = U
  EndpointModel.at00 model q = leg-zero R _ ∙ leg-zero L _
  EndpointModel.at10 model q = leg-zero R _ ∙ leg-one L _ ∙ L-basis q
  EndpointModel.at01 model q = cong (leg R 1r) (leg-zero L _) ∙ leg-one R _ ∙ R-basis q
  EndpointModel.at11 model q = leg-one R (leg L 1r (basis q)) ∙ cong R (leg-one L (basis q) ∙ L-basis q)
    ∙ R-basis (G.expandLeft q)

  -- These instantiate the bridge for ALL actual Bool-valued Ticks at s.
  module ForSource (s : Bool × Bool) = Bridge model s
