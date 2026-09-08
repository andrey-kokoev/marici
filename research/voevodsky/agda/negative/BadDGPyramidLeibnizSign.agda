{-# OPTIONS --safe --cubical --guardedness #-}
module BadDGPyramidLeibnizSign where

open import Cubical.Foundations.Prelude
open import DGPyramidBoundary

-- EXPECTED FAILURE: degree(e)=2 is even. The e∘δ(hM) Leibniz term is
-- positive, but this attempted interface gives it the odd-degree minus sign.
badEvenLeibnizSign : {ℓ : Level} (P : DGPyramidBoundary {ℓ}) →
  deltaJF P (compose2minus1 P (e P) (hM P)) ≡
  addJFtwo P
    (compose3minus1 P (deltaQF P (e P)) (hM P))
    (negJFtwo P (compose20 P (e P) (deltaJQ P (hM P))))
badEvenLeibnizSign P = compositionBoundary P
