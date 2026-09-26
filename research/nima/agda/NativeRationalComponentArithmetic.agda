{-# OPTIONS --safe --cubical --guardedness #-}
module NativeRationalComponentArithmetic where
open import Cubical.Foundations.Prelude
open import Cubical.Data.List.Base using (List; []; _∷_)
import Cubical.Data.Int as Z
import Cubical.Data.NatPlusOne as P
import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing.Base using (CommRing→Ring)
open import Cubical.Algebra.Ring.Properties using (Ring→Semiring)
import SignedComponentArithmetic as S
import RationalComponentArithmetic as R
import NativeCoefficientTransport as T
import AmplitudeDiagramExpansion as Expansion
import NativeScalarFiberFixture as Scalar
import ScalarSixFixture as Export

module SignedBridge (A : Type) (weight : A → S.Signed) where
  module Native = T.Transport A S.Signed Z.ℤ weight S.asInt
    S.zero S.one S.add S.multiply (Z.pos 0) (Z.pos 1) Z._+_ Z._·_
    refl refl S.Add.preserves S.Multiply.preserves
  module Diagrams = Expansion.Expansion A (Ring→Semiring (CommRing→Ring S.signedRing)) weight

module FractionBridge (A : Type) (weight : A → R.Rational) where
  module Native = T.Transport A R.Rational Q.ℚ weight R.asRational
    R.zero R.one R.add R.multiply Q.[ Z.pos 0 / P.1+ 0 ] Q.[ Z.pos 1 / P.1+ 0 ] Q._+_ Q._·_
    refl refl R.Add.preserves R.Multiply.preserves
  module Diagrams = Expansion.Expansion A (Ring→Semiring (CommRing→Ring R.rationalRing)) weight

-- The existing source table supplies channel weights, not new physics.
-- Normalization is a marked factor, with a positive denominator constructor.
module ScalarFixture where
  data Factor : Type where
    channel : Scalar.Channel → Factor
    normalization : Factor
  weight : Factor → R.Rational
  weight (channel c) = R.fraction (S.fromInt (Scalar.weight c)) (P.1+ 0)
  weight normalization = R.fraction S.one (P.1+ 599)
  module B = FractionBridge Factor weight
  module E = B.Native.E
  sum-channels : List Scalar.Channel → E.Expr
  sum-channels [] = E.zero-expr
  sum-channels (c ∷ cs) = E.binary E.sum-mode (E.factor (channel c)) (sum-channels cs)
  expression : E.Expr
  expression = E.binary E.product-mode (sum-channels Scalar.enumeration) (E.factor normalization)
  execution : E.Run.Resolve (E.package expression)
  execution = E.native-run expression
  denominator-from-source : Z.pos 600 ≡ Scalar.common-denominator
  denominator-from-source = refl
  numerator-from-export : Z.pos 6 ≡ Export.exportedNumerator
  numerator-from-export = refl
  denominator-from-export : Z.pos 25 ≡ Export.exportedDenominator
  denominator-from-export = refl
  computed : R.asRational (E.readout expression (snd (E.package expression))) ≡ Q.[ Z.pos 6 / P.1+ 24 ]
  computed = Q.eq/ _ _ refl
  translated : R.asRational (E.readout expression (E.aligned-value expression)) ≡ Q.[ Z.pos 6 / P.1+ 24 ]
  translated = sym (cong R.asRational (E.direct-and-translated expression)) ∙ computed
  expanded : R.asRational (B.Diagrams.sum-words (B.Diagrams.diagrams expression)) ≡ Q.[ Z.pos 6 / P.1+ 24 ]
  expanded = cong R.asRational (sym (B.Diagrams.native-diagram-sum expression)) ∙ computed

-- The quotient construction really cancels signed pairs and common factors.
signed-cancellation : S.add (S.fromInt (Z.pos 3)) (S.fromInt (Z.negsuc 2)) ≡ S.zero
signed-cancellation = S.faithful refl
fraction-cancellation : R.fraction (S.fromInt (Z.pos 2)) (P.1+ 3) ≡ R.fraction S.one (P.1+ 1)
fraction-cancellation = R.faithful (Q.eq/ _ _ refl)
