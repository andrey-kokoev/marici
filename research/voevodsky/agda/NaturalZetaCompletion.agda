{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module NaturalZetaCompletion where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyCompletionAbGroup
open import ConstructiveNaturalZeta
open import ConstructiveZetaTwo
open import ConstructiveComplexCompletion
open import RegularCauchyTriangularEmbedding

naturalZetaValue : NaturalZetaExponent → MetricCompletionCandidate
naturalZetaValue input = SQ.[ naturalZetaRegular input ]

naturalZetaTriangularValue : NaturalZetaExponent → ComplexCompletion
naturalZetaTriangularValue input =
  shiftedRealRegularTriangularValue (naturalZetaRegular input)

natural-zeta-triangular-agrees-with-direct : (input : NaturalZetaExponent) →
  naturalZetaTriangularValue input ≡
  complex (naturalZetaValue input) zeroCompletion
natural-zeta-triangular-agrees-with-direct input =
  shiftedRealRegularTriangularValueAgrees (naturalZetaRegular input)

zetaTwoExponent : NaturalZetaExponent
zetaTwoExponent .exponent = 2
zetaTwoExponent .exponentAtLeastTwo = ℕOrder.≤-refl

natural-zeta-two-regular-agrees :
  naturalZetaRegular zetaTwoExponent ≡ zetaTwoRegular
natural-zeta-two-regular-agrees =
  regularCauchy-ext _ _ refl

natural-zeta-two-value-agrees :
  naturalZetaValue zetaTwoExponent ≡ SQ.[ zetaTwoRegular ]
natural-zeta-two-value-agrees =
  cong SQ.[_] natural-zeta-two-regular-agrees
