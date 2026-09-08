{-# OPTIONS --safe --cubical --guardedness #-}
module CartierSupportedHomCone where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma

-- Minimal additive chain structure used by the explicit Cartier calculation.
record AdditiveChainData {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Chain Scalar : Type ℓ
    0c : Chain
    _+c_ : Chain → Chain → Chain
    -c_ : Chain → Chain
    d : Chain → Chain
    _·c_ : Scalar → Chain → Chain

    +c-zeroˡ : (a : Chain) → 0c +c a ≡ a
    +c-inverseʳ : (a : Chain) → a +c (-c a) ≡ 0c
    d-square : (a : Chain) → d (d a) ≡ 0c
    d-difference : (x : Scalar) (a b : Chain) →
      d ((x ·c a) +c (-c d b)) ≡ (x ·c d a) +c (-c d (d b))
    scalarZeroDifference : (x : Scalar) (a : Chain) →
      (x ·c a) +c (-c ((x ·c a) +c (-c 0c))) ≡ 0c

private variable ℓ : Level

module CartierCone (A : AdditiveChainData {ℓ}) (x : AdditiveChainData.Scalar A) where
  open AdditiveChainData A

  Cone : Type ℓ
  Cone = AdditiveChainData.Chain A × AdditiveChainData.Chain A

  -- Hom(K(x),C), after the standard degree-dependent sign change.
  D : Cone → Cone
  D (a , b) = d a , (x ·c a) +c (-c d b)

  D-square : (z : Cone) → D (D z) ≡ (0c , 0c)
  D-square (a , b) = cong₂ _,_ (d-square a)
    (cong (λ z → (x ·c d a) +c (-c z)) (d-difference x a b)
    ∙ cong (λ z → (x ·c d a) +c (-c ((x ·c d a) +c (-c z))))
        (d-square b)
    ∙ scalarZeroDifference x (d a))

  counit : Cone → Chain
  counit (a , b) = a

  counitChainMap : (z : Cone) → counit (D z) ≡ d (counit z)
  counitChainMap (a , b) = refl

-- The Cartier quotient kills x. Its target differential is shifted, hence the
-- minus sign in shiftedQuotient.
record CartierPurityData {ℓ : Level} (A : AdditiveChainData {ℓ})
  (x : AdditiveChainData.Scalar A)
  : Type (ℓ-suc ℓ) where
  open AdditiveChainData A
  field
    DivisorChain : Type ℓ
    quotient : Chain → DivisorChain
    _+D_ : DivisorChain → DivisorChain → DivisorChain
    -D_ : DivisorChain → DivisorChain
    0D : DivisorChain
    shiftedDifferential : DivisorChain → DivisorChain
    quotientAdd : (a b : Chain) → quotient (a +c b) ≡ quotient a +D quotient b
    quotientNeg : (a : Chain) → quotient (-c a) ≡ -D quotient a
    quotientX : (a : Chain) → quotient (x ·c a) ≡ 0D
    zeroPlus : (a : DivisorChain) → 0D +D a ≡ a
    shiftedQuotient : (a : Chain) →
      shiftedDifferential (quotient a) ≡ quotient (-c d a)

module CartierPurity
  (A : AdditiveChainData {ℓ}) (x : AdditiveChainData.Scalar A)
  (Q : CartierPurityData A x) where
  open AdditiveChainData A
  open CartierPurityData Q
  open CartierCone A x

  purity : Cone → DivisorChain
  purity (a , b) = quotient b

  purityChainMap : (z : Cone) →
    purity (D z) ≡ shiftedDifferential (purity z)
  purityChainMap (a , b) =
    quotientAdd (x ·c a) (-c d b)
    ∙ cong₂ _+D_ (quotientX a) (quotientNeg (d b))
    ∙ zeroPlus (-D quotient (d b))
    ∙ sym (quotientNeg (d b))
    ∙ sym (shiftedQuotient b)

-- Existential package used by the Marici architecture. Its laws are the
-- derived D-square, counitChainMap, and purityChainMap above, rather than
-- independently supplied assertions.
record CartierSupportedHomConeCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    additiveChain : AdditiveChainData {ℓ}
    cartierParameter : AdditiveChainData.Scalar additiveChain
    cartierQuotient : CartierPurityData additiveChain cartierParameter
