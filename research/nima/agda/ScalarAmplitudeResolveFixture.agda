{-# OPTIONS --safe --cubical --guardedness #-}
module ScalarAmplitudeResolveFixture where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (ℤ; pos; _+_; _·_)
open import Cubical.Data.List.Base using (List; []; _∷_)
import NativeAmplitudeResolution as Resolution
import AmplitudeDiagramExpansion as Expansion
open import Cubical.Algebra.CommRing.Instances.Int using (ℤCommRing)
open import Cubical.Algebra.CommRing.Base using (CommRing→Ring)
open import Cubical.Algebra.Ring.Properties using (Ring→Semiring)
import NativeScalarFiberFixture as Scalar
import ScalarSixFixture as Source

-- The existing exact channel weights become marked source factors. Only
-- those factors, algebra constants and operation tokens are literal seeds.
module E = Resolution.Algebra Scalar.Channel ℤ Scalar.weight (pos 0) (pos 1) _+_ _·_
add-channels : List Scalar.Channel → E.Expr
add-channels [] = E.zero-expr
add-channels (c ∷ cs) = E.binary E.sum-mode (E.factor c) (add-channels cs)
expression : E.Expr
expression = add-channels Scalar.enumeration
history : E.Run.Resolve (E.package expression)
history = E.native-run expression
computed-readout : E.readout expression (snd (E.package expression)) ≡ pos 144
computed-readout = refl
same-native-table-sum : E.readout expression (snd (E.package expression)) ≡ Scalar.native-numerator
same-native-table-sum = refl
actual-translated-history-readout : E.readout expression (E.aligned-value expression) ≡ pos 144
actual-translated-history-readout = E.translated-amplitude expression
amplitude-agrees : E.readout expression (E.aligned-value expression) · Source.exportedDenominator
  ≡ Source.exportedNumerator · Scalar.common-denominator
amplitude-agrees = cong (_· Source.exportedDenominator) actual-translated-history-readout
  ∙ Scalar.export-agrees

module D = Expansion.Expansion Scalar.Channel (Ring→Semiring (CommRing→Ring ℤCommRing)) Scalar.weight
actual-diagram-expansion : D.sum-words (D.diagrams expression) ≡ pos 144
actual-diagram-expansion = D.expansion-correct expression
sum-sample product-sample : E.Expr
sum-sample = E.binary E.sum-mode (E.factor Scalar.c12) (E.factor Scalar.c13)
product-sample = E.binary E.product-mode (E.factor Scalar.c12) (E.factor Scalar.c13)
-- The reader uses the operator in its supplied value, not merely the mode
-- written in the expression schema. This altered value is not a new run.
operator-read-from-value : E.readout sum-sample
  (λ { E.operator → E.product-mode ; E.left → Scalar.weight Scalar.c12 ; E.right → Scalar.weight Scalar.c13 }) ≡ pos 729
operator-read-from-value = refl
