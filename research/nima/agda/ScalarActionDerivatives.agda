{-# OPTIONS --safe --cubical --guardedness #-}
module ScalarActionDerivatives where
open import Cubical.Foundations.Prelude
open import Cubical.Data.List.Base using (List; []; _∷_)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Algebra.CommRing.Base
open import Cubical.Algebra.Ring.Properties using (Ring→Semiring)
open import Cubical.Tactics.CommRingSolver
import ComponentArithmetic as C

-- Formal polynomial differentiation, not a derived variational/quantum law.
module Action (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  module W = C.Readout (Ring→Semiring (CommRing→Ring R))
  Polynomial = List (fst R)
  from-degree : ℕ → Polynomial → Polynomial
  from-degree n [] = []
  from-degree n (a ∷ as) = (W.numeral n · a) ∷ from-degree (suc n) as
  derivative : Polynomial → Polynomial
  derivative [] = []
  derivative (a ∷ as) = from-degree 1 as
  at-zero : Polynomial → fst R
  at-zero [] = 0r
  at-zero (a ∷ as) = a
  quadratic : fst R → fst R → Polynomial
  quadratic kernel half = 0r ∷ 0r ∷ (kernel · half) ∷ []
  quartic : fst R → fst R → Polynomial
  quartic coupling inv24 = 0r ∷ 0r ∷ 0r ∷ 0r ∷ ((- coupling) · inv24) ∷ []
  quadratic-factor : (k h : fst R) → at-zero (derivative (derivative (quadratic k h))) ≡ k · (W.numeral 2 · h)
  quadratic-factor k h = solve! R
  quartic-factor : (g u : fst R) → at-zero (derivative (derivative (derivative (derivative (quartic g u)))))
    ≡ (- g) · (W.numeral 24 · u)
  quartic-factor g u = solve! R
  hessian : (k h : fst R) → W.numeral 2 · h ≡ 1r
    → at-zero (derivative (derivative (quadratic k h))) ≡ k
  hessian k h inverse = quadratic-factor k h ∙ cong (k ·_) inverse ∙ ·IdR k
  vertex : (g u : fst R) → W.numeral 24 · u ≡ 1r
    → at-zero (derivative (derivative (derivative (derivative (quartic g u))))) ≡ - g
  vertex g u inverse = quartic-factor g u ∙ cong ((- g) ·_) inverse ∙ ·IdR (- g)
