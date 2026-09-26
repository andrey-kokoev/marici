{-# OPTIONS --safe --cubical --guardedness #-}
module NativeCoefficientTransport where
open import Cubical.Foundations.Prelude
import NativeAmplitudeResolution as Resolution

-- Coefficient homomorphisms act on expressions while retaining factor labels.
module Transport (A W V : Type) (weight : A → W) (f : W → V)
  (z u : W) (add mul : W → W → W)
  (z' u' : V) (add' mul' : V → V → V)
  (pz : f z ≡ z') (pu : f u ≡ u')
  (pa : (x y : W) → f (add x y) ≡ add' (f x) (f y))
  (pm : (x y : W) → f (mul x y) ≡ mul' (f x) (f y)) where
  module E = Resolution.Algebra A W weight z u add mul
  module T = Resolution.Algebra A V (λ a → f (weight a)) z' u' add' mul'
  mode : E.Mode → T.Mode
  mode E.sum-mode = T.sum-mode
  mode E.product-mode = T.product-mode
  expression : E.Expr → T.Expr
  expression E.zero-expr = T.zero-expr
  expression E.one-expr = T.one-expr
  expression (E.factor a) = T.factor a
  expression (E.binary m l r) = T.binary (mode m) (expression l) (expression r)
  evaluate-commutes : (e : E.Expr) → f (E.evaluate e) ≡ T.evaluate (expression e)
  evaluate-commutes E.zero-expr = pz
  evaluate-commutes E.one-expr = pu
  evaluate-commutes (E.factor a) = refl
  evaluate-commutes (E.binary E.sum-mode l r) = pa (E.evaluate l) (E.evaluate r)
    ∙ cong₂ add' (evaluate-commutes l) (evaluate-commutes r)
  evaluate-commutes (E.binary E.product-mode l r) = pm (E.evaluate l) (E.evaluate r)
    ∙ cong₂ mul' (evaluate-commutes l) (evaluate-commutes r)
  native-readout-commutes : (e : E.Expr) → f (E.readout e (snd (E.package e)))
    ≡ T.readout (expression e) (snd (T.package (expression e)))
  native-readout-commutes e = cong f (E.native-correct e)
    ∙ evaluate-commutes e ∙ sym (T.native-correct (expression e))
  translated-readout-commutes : (e : E.Expr) → f (E.readout e (E.aligned-value e))
    ≡ T.readout (expression e) (T.aligned-value (expression e))
  translated-readout-commutes e = cong f (E.translated-amplitude e)
    ∙ evaluate-commutes e ∙ sym (T.translated-amplitude (expression e))
