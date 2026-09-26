{-# OPTIONS --safe --cubical --guardedness #-}
module NativeComponentArithmetic where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Algebra.Semiring.Base
import ComponentArithmetic as C
import NativeAmplitudeResolution as Resolution
import AmplitudeDiagramExpansion as Expansion

-- The old conditional geometric theorem must supply this normal-form
-- equivalence; it is not inferred from arbitrary native packages.
module ComponentPort (M : Type) (normal-form : M ≃ C.Word) where
  zeroM oneM : M
  zeroM = invEq normal-form C.empty
  oneM = invEq normal-form C.unit
  addM multiplyM : M → M → M
  addM a b = invEq normal-form (C.append (equivFun normal-form a) (equivFun normal-form b))
  multiplyM a b = invEq normal-form (C.multiply (equivFun normal-form a) (equivFun normal-form b))
  product-descends : (a b : M) → equivFun normal-form (multiplyM a b)
    ≡ C.multiply (equivFun normal-form a) (equivFun normal-form b)
  product-descends a b = secEq normal-form _
  sum-descends : (a b : M) → equivFun normal-form (addM a b)
    ≡ C.append (equivFun normal-form a) (equivFun normal-form b)
  sum-descends a b = secEq normal-form _

module Bridge (A : Type) (weight : A → C.Word) where
  module D = Expansion.Expansion A C.componentSemiring weight
  module E = D.E
  -- D already builds actual native Resolve derivations and diagram expansion
  -- using the newly constructed semiring, not a supplied multiplication.
  execution : (e : E.Expr) → E.Run.Resolve (E.package e)
  execution = E.native-run
  expanded-readout : (e : E.Expr) → E.readout e (snd (E.package e)) ≡ D.sum-words (D.diagrams e)
  expanded-readout = D.native-diagram-sum

  module CoefficientReadout (S : Semiring ℓ-zero) where
    module R = C.Readout S
    open SemiringStr (snd S)
    module T = Resolution.Algebra A (fst S) (λ a → R.numeral (weight a)) 0r 1r _+_ _·_
    mode : E.Mode → T.Mode
    mode E.sum-mode = T.sum-mode
    mode E.product-mode = T.product-mode
    expression : E.Expr → T.Expr
    expression E.zero-expr = T.zero-expr
    expression E.one-expr = T.one-expr
    expression (E.factor a) = T.factor a
    expression (E.binary m l r) = T.binary (mode m) (expression l) (expression r)
    evaluate-commutes : (e : E.Expr) → R.numeral (E.evaluate e) ≡ T.evaluate (expression e)
    evaluate-commutes E.zero-expr = refl
    evaluate-commutes E.one-expr = R.numeral-unit
    evaluate-commutes (E.factor a) = refl
    evaluate-commutes (E.binary E.sum-mode l r) = R.numeral-add (E.evaluate l) (E.evaluate r)
      ∙ cong₂ _+_ (evaluate-commutes l) (evaluate-commutes r)
    evaluate-commutes (E.binary E.product-mode l r) = R.numeral-multiply (E.evaluate l) (E.evaluate r)
      ∙ cong₂ _·_ (evaluate-commutes l) (evaluate-commutes r)
    native-readout-commutes : (e : E.Expr) → R.numeral (E.readout e (snd (E.package e)))
      ≡ T.readout (expression e) (snd (T.package (expression e)))
    native-readout-commutes e = cong R.numeral (E.native-correct e)
      ∙ evaluate-commutes e ∙ sym (T.native-correct (expression e))
    translated-readout-commutes : (e : E.Expr) → R.numeral (E.readout e (E.aligned-value e))
      ≡ T.readout (expression e) (T.aligned-value (expression e))
    translated-readout-commutes e = cong R.numeral (E.translated-amplitude e)
      ∙ evaluate-commutes e ∙ sym (T.translated-amplitude (expression e))

-- A product with a genuine sum: 2 * (3 + 4) = 14, not an amplitude seed.
module Fixture where
  data Factor : Type where two three four : Factor
  weight : Factor → C.Word
  weight two = 2
  weight three = 3
  weight four = 4
  module B = Bridge Factor weight
  module E = B.E
  expression : E.Expr
  expression = E.binary E.product-mode (E.factor two)
    (E.binary E.sum-mode (E.factor three) (E.factor four))
  run : E.Run.Resolve (E.package expression)
  run = B.execution expression
  computed : E.readout expression (snd (E.package expression)) ≡ 14
  computed = refl
  expanded : B.D.sum-words (B.D.diagrams expression) ≡ 14
  expanded = refl
  translated : E.readout expression (E.aligned-value expression) ≡ 14
  translated = E.translated-amplitude expression
