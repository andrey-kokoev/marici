{-# OPTIONS --safe --cubical --guardedness #-}
module PhaseLiftCocycle where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Algebra.CommRing.Base
open import Cubical.Tactics.CommRingSolver

-- Algebra of the proposed Hamiltonian translation-phase exponent.
-- The coefficient ring, symplectic coordinates and rate are explicit inputs.
-- No complex exponential or physical value of hbar is constructed here.
module Exponent (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  Scalar = fst R
  Point = Scalar × Scalar
  add : Point → Point → Point
  add (q , p) (r , s) = (q + r) , (p + s)
  negate : Point → Point
  negate (q , p) = (- q) , (- p)
  area : Point → Point → Scalar
  area (q , p) (r , s) = q · s + (- (p · r))
  phase : Scalar → Point → Point → Scalar
  phase rate u v = rate · area u v

  cocycle : (rate : Scalar) (u v w : Point)
    → phase rate u v + phase rate (add u v) w
      ≡ phase rate v w + phase rate u (add v w)
  cocycle rate (q , p) (r , s) (t , v) = solve! R
  normalized : (rate : Scalar) (u : Point) → phase rate (0r , 0r) u ≡ 0r
  normalized rate (q , p) = solve! R
  zero-rate : (u v : Point) → phase 0r u v ≡ 0r
  zero-rate (q , p) (r , s) = solve! R
  inverse-unit : (rate : Scalar) (u : Point) → phase rate u (negate u) ≡ 0r
  inverse-unit rate (q , p) = solve! R
  reversal : (rate : Scalar) (u v : Point)
    → phase rate (negate v) (negate u) ≡ - phase rate u v
  reversal rate (q , p) (r , s) = solve! R
  commutator-exponent : (rate : Scalar) (u v : Point)
    → phase rate u v + (- phase rate v u) ≡ (1r + 1r) · phase rate u v
  commutator-exponent rate (q , p) (r , s) = solve! R

  matrix : Scalar → Scalar → Scalar → Scalar → Point → Point
  matrix a b c d (q , p) = (a · q + b · p) , (c · q + d · p)
  covariance : (a b c d : Scalar) (u v : Point)
    → area (matrix a b c d u) (matrix a b c d v)
      ≡ (a · d + (- (b · c))) · area u v
  covariance a b c d (q , p) (r , s) = solve! R
