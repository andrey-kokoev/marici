{-# OPTIONS --safe --cubical --guardedness #-}
module FirstNormalSymbol where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- Coefficient-level first-normal evaluation
-- (I/I²)^dual tensor gr_I^1 C -> C_D.
record FirstNormalSymbolMap {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    ConormalDual FirstGraded TensorSymbol DivisorChain : Type ℓ
    tensorSymbol : ConormalDual → FirstGraded → TensorSymbol
    differentialSymbol : TensorSymbol → TensorSymbol
    differentialDivisor : DivisorChain → DivisorChain
    evaluate : TensorSymbol → DivisorChain
    evaluateChainMap : (z : TensorSymbol) →
      evaluate (differentialSymbol z) ≡ differentialDivisor (evaluate z)

    normalFrame : ConormalDual
    firstGradedComparison : FirstGraded
    fixedSymbol : TensorSymbol
    fixedSymbolDefinition :
      fixedSymbol ≡ tensorSymbol normalFrame firstGradedComparison

-- Naturality is required only for maps preserving the ideal filtration and
-- its framed conormal line.
record FirstSymbolMorphism {ℓ : Level}
  (S T : FirstNormalSymbolMap {ℓ}) : Type (ℓ-suc ℓ) where
  private
    module S = FirstNormalSymbolMap S
    module T = FirstNormalSymbolMap T
  field
    mapConormal : S.ConormalDual → T.ConormalDual
    mapGraded : S.FirstGraded → T.FirstGraded
    mapTensor : S.TensorSymbol → T.TensorSymbol
    mapDivisor : S.DivisorChain → T.DivisorChain
    tensorNatural : (n : S.ConormalDual) (g : S.FirstGraded) →
      mapTensor (S.tensorSymbol n g) ≡
      T.tensorSymbol (mapConormal n) (mapGraded g)
    differentialNatural : (z : S.TensorSymbol) →
      mapTensor (S.differentialSymbol z) ≡
      T.differentialSymbol (mapTensor z)
    evaluationNatural : (z : S.TensorSymbol) →
      mapDivisor (S.evaluate z) ≡ T.evaluate (mapTensor z)

-- The physical D03 comparison is zero in ordinary supported-Hom cohomology,
-- while evaluation of its retained first symbol is nonzero.
record FixedFirstSymbolNonDescent {ℓ : Level}
  (S : FirstNormalSymbolMap {ℓ}) : Type (ℓ-suc ℓ) where
  private module S = FirstNormalSymbolMap S
  field
    OrdinarySupportedClass : Type ℓ
    ordinaryClass : S.TensorSymbol → OrdinarySupportedClass
    zeroSupported : OrdinarySupportedClass
    zeroDivisor : S.DivisorChain
    fixedOrdinaryClassVanishes : ordinaryClass S.fixedSymbol ≡ zeroSupported
    fixedFirstSymbolSurvives : S.evaluate S.fixedSymbol ≡ zeroDivisor → ⊥

-- A descent would factor evaluation through ordinary supported cohomology and
-- preserve its zero class. These two requirements contradict the fixed symbol.
record FirstSymbolDescent {ℓ : Level}
  {S : FirstNormalSymbolMap {ℓ}}
  (N : FixedFirstSymbolNonDescent S) : Type (ℓ-suc ℓ) where
  private
    module S = FirstNormalSymbolMap S
    module N = FixedFirstSymbolNonDescent N
  field
    descend : N.OrdinarySupportedClass → S.DivisorChain
    descendZero : descend N.zeroSupported ≡ N.zeroDivisor
    factorEvaluation : (z : S.TensorSymbol) →
      S.evaluate z ≡ descend (N.ordinaryClass z)

firstSymbolDoesNotDescend : {ℓ : Level}
  {S : FirstNormalSymbolMap {ℓ}}
  (N : FixedFirstSymbolNonDescent S) → FirstSymbolDescent N → ⊥
firstSymbolDoesNotDescend {S = S} N D =
  FixedFirstSymbolNonDescent.fixedFirstSymbolSurvives N
    (FirstSymbolDescent.factorEvaluation D (FirstNormalSymbolMap.fixedSymbol S)
    ∙ cong (FirstSymbolDescent.descend D)
        (FixedFirstSymbolNonDescent.fixedOrdinaryClassVanishes N)
    ∙ FirstSymbolDescent.descendZero D)

record FirstNormalSymbolCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    symbolMap : FirstNormalSymbolMap {ℓ}
    fixedNonDescent : FixedFirstSymbolNonDescent symbolMap
