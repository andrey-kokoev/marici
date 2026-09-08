{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module AbsoluteTaylorSeriesMultiplication where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _∸_; max; isSetℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.NatPlusOne as ℕ₊₁ using (ℕ₊₁; 1+_)
import Cubical.Data.NatPlusOne.Properties as ℕ₊₁Properties
open import Cubical.Data.Int as ℤ using (pos; sucℤ)
import Cubical.Data.Int.Properties as ℤProperties
open import Cubical.Data.Rationals.Order
open import Cubical.Data.Sigma
open import Cubical.Data.FinData using
  (Fin; toℕ; weakenFin; fromℕ; weakenRespToℕ; toFromId)
open import Cubical.Data.Sum
open import Cubical.Data.Empty as ⊥
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Foundations.Isomorphism
open import Cubical.HITs.SetQuotients as SQ using ([_]; eq/)
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.Algebra.CommRing.BinomialThm
open import Cubical.Algebra.Monoid.BigOp
open import Cubical.Algebra.Ring.BigOps
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import Cubical.Tactics.NatSolver
open import Cubical.Tactics.NatSolver renaming (solveℕ! to solveNat!)
open import RationalAnalyticSubstrate using
  (PreferredℚCommRing; halfℚ; half-double)
open import RationalArchimedean
open import RationallyBoundedCauchy
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CauchyProductBounds
open import CauchyProductRegularity
open import CauchyBoundPromotion
open import CauchyMetricEquivalence
open import TaylorRegularityComposition using
  (magnitude-bound-forward; magnitude-bound-backward)
open import CauchyShift using
  (loosen-two-errors; tighten-two-errors; iterateShift;
   iterateShift-approximation; iterateShift-equivalent)
open import CauchyProductWitnessCoherence
open import RationalTaylorApproximants using
  (finiteSum; exponentialTerm; reciprocalSuccessor)
open import TaylorTermBounds using (nonnegative-bound-product)
open import TaylorGeometricTail using
  (termBlock; termBlock-append; geometricBlock; scaledGeometricBlock≤precision)
open import ExponentialTailSchedule using
  (ExponentialTailSeed; baseTaylorCutoff; seedExponent; absorbedTaylorCutoff;
   absorbedExponentialRegular; absorbedExponentialPartialSum;
   exponential-tail-bound-before-absorption)

module RationalBinomial = BinomialThm PreferredℚCommRing
module RationalSum = Sum (CommRing→Ring PreferredℚCommRing)
open CommRingStr (snd PreferredℚCommRing)
  renaming (_+_ to _+R_; _·_ to _·R_)
open Exponentiation PreferredℚCommRing renaming (_^_ to _^R_)

rationalBinomialExpansion : ℕ → Q.ℚ → Q.ℚ → Q.ℚ
rationalBinomialExpansion degree x y =
  let open Sum (CommRing→Ring PreferredℚCommRing)
  in ∑ (RationalBinomial.BinomialVec degree x y)

rational-binomial-theorem : (degree : ℕ) (x y : Q.ℚ) →
  (x +R y) ^R degree ≡ rationalBinomialExpansion degree x y
rational-binomial-theorem = RationalBinomial.BinomialThm

taylorMonomialPower : Q.ℚ → ℕ → Q.ℚ
taylorMonomialPower q zero = 1
taylorMonomialPower q (suc degree) = taylorMonomialPower q degree Q.· q

taylor-monomial-is-ring-power : (q : Q.ℚ) (degree : ℕ) →
  taylorMonomialPower q degree ≡ q ^R degree
taylor-monomial-is-ring-power q zero = refl
taylor-monomial-is-ring-power q (suc degree) =
  cong (Q._· q) (taylor-monomial-is-ring-power q degree) ∙
  Q.·Comm (q ^R degree) q

taylor-monomial-binomial-expansion : (degree : ℕ) (x y : Q.ℚ) →
  taylorMonomialPower (x Q.+ y) degree ≡
    rationalBinomialExpansion degree x y
taylor-monomial-binomial-expansion degree x y =
  taylor-monomial-is-ring-power (x Q.+ y) degree ∙
  rational-binomial-theorem degree x y

reciprocalFactorial : ℕ → Q.ℚ
reciprocalFactorial zero = 1
reciprocalFactorial (suc degree) =
  reciprocalFactorial degree Q.· reciprocalSuccessor degree

positiveFactorial : ℕ → ℕ₊₁
positiveFactorial zero = 1+ zero
positiveFactorial (suc degree) =
  positiveFactorial degree ℕ₊₁Properties.·₊₁ (1+ degree)

naturalFactorial : ℕ → ℕ
naturalFactorial zero = suc zero
naturalFactorial (suc degree) =
  naturalFactorial degree ℕ.· suc degree

positive-product-underlying : (m n : ℕ₊₁) →
  ℕ₊₁.ℕ₊₁→ℕ (m ℕ₊₁Properties.·₊₁ n) ≡
    ℕ₊₁.ℕ₊₁→ℕ m ℕ.· ℕ₊₁.ℕ₊₁→ℕ n
positive-product-underlying (1+ m) (1+ n) = refl

positive-factorial-underlying : (degree : ℕ) →
  ℕ₊₁.ℕ₊₁→ℕ (positiveFactorial degree) ≡ naturalFactorial degree
positive-factorial-underlying zero = refl
positive-factorial-underlying (suc degree) =
  positive-product-underlying (positiveFactorial degree) (1+ degree) ∙
  cong (ℕ._· suc degree) (positive-factorial-underlying degree)

reciprocal-factorial-as-quotient : (degree : ℕ) →
  reciprocalFactorial degree ≡ Q.[ pos 1 / positiveFactorial degree ]
reciprocal-factorial-as-quotient zero = refl
reciprocal-factorial-as-quotient (suc degree) =
  cong (Q._· reciprocalSuccessor degree)
    (reciprocal-factorial-as-quotient degree) ∙
  cong (λ numerator → Q.[ numerator /
    positiveFactorial degree ℕ₊₁Properties.·₊₁ (1+ degree) ])
    (ℤProperties.·IdL (pos 1))

naturalChoose : ℕ → ℕ → ℕ
naturalChoose n zero = suc zero
naturalChoose zero (suc k) = zero
naturalChoose (suc n) (suc k) =
  naturalChoose n (suc k) ℕ.+ naturalChoose n k

natural-choose-above-diagonal-zero : (n k : ℕ) →
  ℕOrder._<_ n k → naturalChoose n k ≡ zero
natural-choose-above-diagonal-zero zero zero n<zero =
  ⊥.rec (ℕOrder.¬-<-zero n<zero)
natural-choose-above-diagonal-zero zero (suc k) n<k = refl
natural-choose-above-diagonal-zero (suc n) (suc k) (distance , path) =
  cong₂ ℕ._+_
    (natural-choose-above-diagonal-zero n (suc k)
      (suc distance , sym (ℕ.+-suc _ _) ∙ path))
    (natural-choose-above-diagonal-zero n k
      (distance , ℕ.injSuc (sym (ℕ.+-suc _ _) ∙ path))) ∙
  ℕ.+-zero zero
natural-choose-above-diagonal-zero (suc n) zero n<zero =
  ⊥.rec (ℕOrder.¬-<-zero n<zero)

natural-choose-diagonal : (n : ℕ) →
  naturalChoose n n ≡ suc zero
natural-choose-diagonal zero = refl
natural-choose-diagonal (suc n) =
  cong₂ ℕ._+_
    (natural-choose-above-diagonal-zero n (suc n) ℕOrder.≤-refl)
    (natural-choose-diagonal n)

natural-factorial-successor-left : (n : ℕ) →
  naturalFactorial (suc n) ≡ suc n ℕ.· naturalFactorial n
natural-factorial-successor-left n =
  ℕ.·-comm (naturalFactorial n) (suc n)

natural-factorial-binomial-zero : (n : ℕ) →
  (naturalChoose n zero ℕ.· naturalFactorial zero) ℕ.·
    naturalFactorial n ≡ naturalFactorial n
natural-factorial-binomial-zero n = ℕ.+-zero (naturalFactorial n)

natural-factorial-binomial-diagonal : (n : ℕ) →
  (naturalChoose n n ℕ.· naturalFactorial n) ℕ.·
    naturalFactorial (n ℕ.∸ n) ≡ naturalFactorial n
subtract-from-left-summand : (left right removed : ℕ) →
  ℕOrder._≤_ removed left →
  (left ℕ.+ right) ℕ.∸ removed ≡ (left ℕ.∸ removed) ℕ.+ right
subtract-from-left-summand zero right zero removed≤left = refl
subtract-from-left-summand zero right (suc removed) removed≤left =
  ⊥.rec (ℕOrder.¬-<-zero removed≤left)
subtract-from-left-summand (suc left) right zero removed≤left = refl
subtract-from-left-summand (suc left) right (suc removed) removed≤left =
  subtract-from-left-summand left right removed
    (ℕOrder.pred-≤-pred removed≤left)

interior-factor-sum : (n k : ℕ) →
  ℕOrder._≤_ (suc k) n →
  suc (n ℕ.∸ suc k) ℕ.+ suc k ≡ suc n
interior-factor-sum n k sucK≤n =
  cong suc (ℕOrder.≤-∸-+-cancel sucK≤n)

natural-factorial-remainder-step : (n k : ℕ) →
  ℕOrder._≤_ (suc k) n →
  naturalFactorial (n ℕ.∸ k) ≡
    naturalFactorial (n ℕ.∸ suc k) ℕ.· suc (n ℕ.∸ suc k)
natural-factorial-remainder-step n k sucK≤n =
  cong naturalFactorial
    (sym (ℕOrder.≤-∸-suc sucK≤n))

pascal-factorial-combine :
  (a b previousIndexFactor previousRemainderFactor
    factorial remainderStep indexStep : ℕ) →
  (a ℕ.· (previousIndexFactor ℕ.· indexStep)) ℕ.·
    previousRemainderFactor ≡ factorial →
  (b ℕ.· previousIndexFactor) ℕ.·
    (previousRemainderFactor ℕ.· remainderStep) ≡ factorial →
  ((a ℕ.+ b) ℕ.· (previousIndexFactor ℕ.· indexStep)) ℕ.·
    (previousRemainderFactor ℕ.· remainderStep) ≡
    factorial ℕ.· (remainderStep ℕ.+ indexStep)
pascal-factorial-combine
  a b previousIndexFactor previousRemainderFactor factorial
  remainderStep indexStep firstHypothesis secondHypothesis =
  rearrange ∙
  cong₂ ℕ._+_
    (cong (ℕ._· remainderStep) firstHypothesis)
    (cong (ℕ._· indexStep) secondHypothesis) ∙
  collect
  where
  rearrange :
    ((a ℕ.+ b) ℕ.· (previousIndexFactor ℕ.· indexStep)) ℕ.·
      (previousRemainderFactor ℕ.· remainderStep) ≡
    (((a ℕ.· (previousIndexFactor ℕ.· indexStep)) ℕ.·
      previousRemainderFactor) ℕ.· remainderStep) ℕ.+
    (((b ℕ.· previousIndexFactor) ℕ.·
      (previousRemainderFactor ℕ.· remainderStep)) ℕ.· indexStep)
  rearrange = solveℕ!

  collect :
    (factorial ℕ.· remainderStep) ℕ.+ (factorial ℕ.· indexStep) ≡
      factorial ℕ.· (remainderStep ℕ.+ indexStep)
  collect = solveℕ!

pascal-factorial-interior-step : (n k a b : ℕ) →
  ℕOrder._≤_ (suc k) n →
  (a ℕ.· naturalFactorial (suc k)) ℕ.· naturalFactorial (n ℕ.∸ suc k) ≡ naturalFactorial n →
  (b ℕ.· naturalFactorial k) ℕ.· naturalFactorial (n ℕ.∸ k) ≡ naturalFactorial n →
  ((a ℕ.+ b) ℕ.· naturalFactorial (suc k)) ℕ.·
    naturalFactorial (suc n ℕ.∸ suc k) ≡ naturalFactorial (suc n)
pascal-factorial-interior-step n k a b sucK≤n firstIH secondIH =
  cong (((a ℕ.+ b) ℕ.· naturalFactorial (suc k)) ℕ.·_)
    (natural-factorial-remainder-step n k sucK≤n) ∙
  pascal-factorial-combine
    a b (naturalFactorial k) (naturalFactorial (n ℕ.∸ suc k))
    (naturalFactorial n) (suc (n ℕ.∸ suc k)) (suc k)
    firstIH
    (cong ((b ℕ.· naturalFactorial k) ℕ.·_)
      (sym (natural-factorial-remainder-step n k sucK≤n)) ∙ secondIH) ∙
  cong (naturalFactorial n ℕ.·_)
    (interior-factor-sum n k sucK≤n)

natural-factorial-binomial : (n k : ℕ) →
  ℕOrder._≤_ k n →
  (naturalChoose n k ℕ.· naturalFactorial k) ℕ.·
    naturalFactorial (n ℕ.∸ k) ≡ naturalFactorial n
natural-factorial-binomial zero zero k≤n =
  natural-factorial-binomial-zero zero
natural-factorial-binomial zero (suc k) k≤n =
  ⊥.rec (ℕOrder.¬-<-zero k≤n)
natural-factorial-binomial (suc n) zero k≤n =
  natural-factorial-binomial-zero (suc n)
natural-factorial-binomial (suc n) (suc k) k≤n with ℕOrder.≤-split k≤n
... | inl strict =
  pascal-factorial-interior-step n k
    (naturalChoose n (suc k)) (naturalChoose n k)
    (ℕOrder.pred-≤-pred strict)
    (natural-factorial-binomial n (suc k) (ℕOrder.pred-≤-pred strict))
    (natural-factorial-binomial n k
      (ℕOrder.≤-trans ℕOrder.≤-sucℕ (ℕOrder.pred-≤-pred strict)))
... | inr diagonal =
  subst (λ index →
    (naturalChoose (suc n) index ℕ.· naturalFactorial index) ℕ.·
      naturalFactorial (suc n ℕ.∸ index) ≡ naturalFactorial (suc n))
    (sym diagonal) (natural-factorial-binomial-diagonal (suc n))

natural-factorial-binomial-diagonal n =
  cong (λ coefficient →
    (coefficient ℕ.· naturalFactorial n) ℕ.· naturalFactorial (n ℕ.∸ n))
    (natural-choose-diagonal n) ∙
  cong (ℕ._· naturalFactorial (n ℕ.∸ n))
    (ℕ.+-zero (naturalFactorial n)) ∙
  cong (λ remainder → naturalFactorial n ℕ.· naturalFactorial remainder)
    (ℕOrder.n∸n≡0 n) ∙
  ℕ.·-identityʳ (naturalFactorial n)

pos-preserves-natural-addition : (m n : ℕ) →
  pos (m ℕ.+ n) ≡ pos m ℤ.+ pos n
pos-preserves-natural-addition = ℤProperties.pos+

rational-natural-addition : (m n : ℕ) →
  Q.[ pos m / 1+ zero ] Q.+ Q.[ pos n / 1+ zero ] ≡
    Q.[ pos (m ℕ.+ n) / 1+ zero ]
rational-natural-addition m n =
  Q.eq/ _ _
    (ℤProperties.·IdR
      ((pos m ℤ.· pos 1) ℤ.+ (pos n ℤ.· pos 1)) ∙
     cong₂ ℤ._+_
      (ℤProperties.·IdR (pos m))
      (ℤProperties.·IdR (pos n)) ∙
     sym (pos-preserves-natural-addition m n) ∙
     sym (ℤProperties.·IdR (pos (m ℕ.+ n))))

rational-choose-is-natural-quotient : (n k : ℕ) →
  RationalBinomial._choose_ n k ≡ Q.[ pos (naturalChoose n k) / 1+ zero ]
rational-choose-is-natural-quotient n zero = refl
rational-choose-is-natural-quotient zero (suc k) = refl
rational-choose-is-natural-quotient (suc n) (suc k) =
  cong₂ Q._+_
    (rational-choose-is-natural-quotient n (suc k))
    (rational-choose-is-natural-quotient n k) ∙
  rational-natural-addition
    (naturalChoose n (suc k)) (naturalChoose n k)

positive-factorial-integer : (n : ℕ) →
  Q.ℕ₊₁→ℤ (positiveFactorial n) ≡ pos (naturalFactorial n)
positive-factorial-integer n =
  cong pos (positive-factorial-underlying n)

positive-factorial-product-integer : (m n : ℕ) →
  Q.ℕ₊₁→ℤ (positiveFactorial m ℕ₊₁Properties.·₊₁ positiveFactorial n) ≡
    pos (naturalFactorial m ℕ.· naturalFactorial n)
positive-factorial-product-integer m n =
  cong pos
    (positive-product-underlying (positiveFactorial m) (positiveFactorial n) ∙
     cong₂ ℕ._·_ (positive-factorial-underlying m)
       (positive-factorial-underlying n))

factorial-cross-product : (degree left : ℕ) → ℕOrder._≤_ left degree →
  ((pos 1 ℤ.· pos 1) ,
      positiveFactorial left ℕ₊₁Properties.·₊₁
        positiveFactorial (degree ℕ.∸ left)) Q.∼
    ((pos (naturalChoose degree left) ℤ.· pos 1) ,
      (1+ zero) ℕ₊₁Properties.·₊₁ positiveFactorial degree)
factorial-cross-product degree left left≤degree =
  ℤProperties.·IdL
    (Q.ℕ₊₁→ℤ ((1+ zero) ℕ₊₁Properties.·₊₁ positiveFactorial degree)) ∙
  positive-factorial-product-integer zero degree ∙
  cong pos (ℕ.+-zero (naturalFactorial degree)) ∙
  cong pos (sym (natural-factorial-binomial degree left left≤degree)) ∙
  ℤProperties.pos·pos
    (naturalChoose degree left ℕ.· naturalFactorial left)
    (naturalFactorial (degree ℕ.∸ left)) ∙
  cong (ℤ._· pos (naturalFactorial (degree ℕ.∸ left)))
    (ℤProperties.pos·pos (naturalChoose degree left) (naturalFactorial left)) ∙
  sym (ℤProperties.·Assoc
    (pos (naturalChoose degree left)) (pos (naturalFactorial left))
    (pos (naturalFactorial (degree ℕ.∸ left)))) ∙
  cong (pos (naturalChoose degree left) ℤ.·_)
    (sym (ℤProperties.pos·pos (naturalFactorial left)
      (naturalFactorial (degree ℕ.∸ left)))) ∙
  sym (cong₂ ℤ._·_
    (ℤProperties.·IdR (pos (naturalChoose degree left)))
    (positive-factorial-product-integer left (degree ℕ.∸ left)))

reciprocal-factorial-split-from-cross-product : (degree left : ℕ) →
  ((pos 1 ℤ.· pos 1) ,
      positiveFactorial left ℕ₊₁Properties.·₊₁
        positiveFactorial (degree ℕ.∸ left)) Q.∼
    ((pos (naturalChoose degree left) ℤ.· pos 1) ,
      (1+ zero) ℕ₊₁Properties.·₊₁ positiveFactorial degree) →
  reciprocalFactorial left Q.· reciprocalFactorial (degree ℕ.∸ left) ≡
    RationalBinomial._choose_ degree left Q.· reciprocalFactorial degree
reciprocal-factorial-split-from-cross-product degree left crossProduct =
  cong₂ Q._·_
    (reciprocal-factorial-as-quotient left)
    (reciprocal-factorial-as-quotient (degree ℕ.∸ left)) ∙
  Q.eq/ _ _ crossProduct ∙
  sym (cong₂ Q._·_
    (rational-choose-is-natural-quotient degree left)
    (reciprocal-factorial-as-quotient degree))

reciprocal-factorial-split : (degree left : ℕ) →
  ℕOrder._≤_ left degree →
  reciprocalFactorial left Q.· reciprocalFactorial (degree ℕ.∸ left) ≡
    RationalBinomial._choose_ degree left Q.· reciprocalFactorial degree
reciprocal-factorial-split degree left left≤degree =
  reciprocal-factorial-split-from-cross-product degree left
    (factorial-cross-product degree left left≤degree)

module ExponentialTermFactorizationPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_·_ to _·S_)

  regroup : (power coefficient argument inverse : fst R) →
    ((power ·S coefficient) ·S argument) ·S inverse ≡
      (power ·S argument) ·S (coefficient ·S inverse)
  regroup power coefficient argument inverse = solve! R

  convolution-regroup :
    (leftPower leftInverse rightPower rightInverse
      choose totalInverse : fst R) →
    leftInverse ·S rightInverse ≡ choose ·S totalInverse →
    (leftPower ·S leftInverse) ·S (rightPower ·S rightInverse) ≡
      ((choose ·S leftPower) ·S rightPower) ·S totalInverse
  convolution-regroup leftPower leftInverse rightPower rightInverse
    choose totalInverse inverseSplit =
    solve! R ∙
    cong ((leftPower ·S rightPower) ·S_) inverseSplit ∙
    solve! R

exponential-term-factorization : (q : Q.ℚ) (degree : ℕ) →
  exponentialTerm q degree ≡
  taylorMonomialPower q degree Q.· reciprocalFactorial degree
exponential-term-factorization q zero = sym (Q.·IdR 1)
exponential-term-factorization q (suc degree) =
  cong (λ previous → (previous Q.· q) Q.· reciprocalSuccessor degree)
    (exponential-term-factorization q degree) ∙
  ExponentialTermFactorizationPaths.regroup PreferredℚCommRing
    (taylorMonomialPower q degree) (reciprocalFactorial degree) q
    (reciprocalSuccessor degree)

exponential-convolution-summand-from-factorial-split :
  (x y : Q.ℚ) (degree left : ℕ) →
  reciprocalFactorial left Q.· reciprocalFactorial (degree ℕ.∸ left) ≡
    RationalBinomial._choose_ degree left Q.· reciprocalFactorial degree →
  exponentialTerm x left Q.· exponentialTerm y (degree ℕ.∸ left) ≡
    ((RationalBinomial._choose_ degree left Q.·
      taylorMonomialPower x left) Q.·
      taylorMonomialPower y (degree ℕ.∸ left)) Q.·
      reciprocalFactorial degree
exponential-convolution-summand-from-factorial-split
  x y degree left factorialSplit =
  cong₂ Q._·_
    (exponential-term-factorization x left)
    (exponential-term-factorization y (degree ℕ.∸ left)) ∙
  ExponentialTermFactorizationPaths.convolution-regroup PreferredℚCommRing
    (taylorMonomialPower x left) (reciprocalFactorial left)
    (taylorMonomialPower y (degree ℕ.∸ left))
    (reciprocalFactorial (degree ℕ.∸ left))
    (RationalBinomial._choose_ degree left) (reciprocalFactorial degree)
    factorialSplit

rational-choose-diagonal : (degree : ℕ) →
  RationalBinomial._choose_ degree degree ≡ 1
rational-choose-diagonal zero = refl
rational-choose-diagonal (suc degree) =
  cong₂ Q._+_
    (RationalBinomial.nChooseN+1 degree)
    (rational-choose-diagonal degree) ∙
  Q.+IdL 1

reciprocal-factorial-split-zero : (degree : ℕ) →
  reciprocalFactorial zero Q.· reciprocalFactorial degree ≡
  RationalBinomial._choose_ degree zero Q.· reciprocalFactorial degree
reciprocal-factorial-split-zero degree = refl

reciprocal-factorial-split-three-one :
  reciprocalFactorial (suc zero) Q.· reciprocalFactorial (suc (suc zero)) ≡
  RationalBinomial._choose_ (suc (suc (suc zero))) (suc zero) Q.·
    reciprocalFactorial (suc (suc (suc zero)))
reciprocal-factorial-split-three-one = Q.eq/ _ _ refl

reciprocal-factorial-split-three-two :
  reciprocalFactorial (suc (suc zero)) Q.· reciprocalFactorial (suc zero) ≡
  RationalBinomial._choose_ (suc (suc (suc zero))) (suc (suc zero)) Q.·
    reciprocalFactorial (suc (suc (suc zero)))
reciprocal-factorial-split-three-two = Q.eq/ _ _ refl

reciprocal-factorial-split-diagonal : (degree : ℕ) →
  reciprocalFactorial degree Q.· reciprocalFactorial (degree ℕ.∸ degree) ≡
  RationalBinomial._choose_ degree degree Q.· reciprocalFactorial degree
reciprocal-factorial-split-diagonal degree =
  cong (λ index → reciprocalFactorial degree Q.· reciprocalFactorial index)
    (ℕOrder.n∸n≡0 degree) ∙
  Q.·IdR (reciprocalFactorial degree) ∙
  sym (cong (Q._· reciprocalFactorial degree)
    (rational-choose-diagonal degree) ∙
    Q.·IdL (reciprocalFactorial degree))

reciprocal-factorial-splits-three : (left : ℕ) →
  ℕOrder._≤_ left (suc (suc (suc zero))) →
  reciprocalFactorial left Q.·
    reciprocalFactorial (suc (suc (suc zero)) ℕ.∸ left) ≡
  RationalBinomial._choose_ (suc (suc (suc zero))) left Q.·
    reciprocalFactorial (suc (suc (suc zero)))
reciprocal-factorial-splits-three zero left≤three =
  reciprocal-factorial-split-zero (suc (suc (suc zero)))
reciprocal-factorial-splits-three (suc zero) left≤three =
  reciprocal-factorial-split-three-one
reciprocal-factorial-splits-three (suc (suc zero)) left≤three =
  reciprocal-factorial-split-three-two
reciprocal-factorial-splits-three (suc (suc (suc zero))) left≤three =
  reciprocal-factorial-split-diagonal (suc (suc (suc zero)))
reciprocal-factorial-splits-three (suc (suc (suc (suc left))))
  left≤three =
  ⊥.rec (ℕOrder.¬-<-zero
    (ℕOrder.pred-≤-pred
      (ℕOrder.pred-≤-pred
        (ℕOrder.pred-≤-pred left≤three))))

exponential-convolution-summand-zero :
  (x y : Q.ℚ) (degree : ℕ) →
  exponentialTerm x zero Q.· exponentialTerm y degree ≡
    ((RationalBinomial._choose_ degree zero Q.·
      taylorMonomialPower x zero) Q.· taylorMonomialPower y degree) Q.·
      reciprocalFactorial degree
exponential-convolution-summand-zero x y degree =
  exponential-convolution-summand-from-factorial-split
    x y degree zero (reciprocal-factorial-split-zero degree)

exponential-convolution-summand-diagonal :
  (x y : Q.ℚ) (degree : ℕ) →
  exponentialTerm x degree Q.·
    exponentialTerm y (degree ℕ.∸ degree) ≡
  ((RationalBinomial._choose_ degree degree Q.·
    taylorMonomialPower x degree) Q.·
    taylorMonomialPower y (degree ℕ.∸ degree)) Q.·
    reciprocalFactorial degree
exponential-convolution-summand-diagonal x y degree =
  exponential-convolution-summand-from-factorial-split
    x y degree degree (reciprocal-factorial-split-diagonal degree)

finiteSumCongruence : (f g : ℕ → Q.ℚ) →
  ((index : ℕ) → f index ≡ g index) →
  (cutoff : ℕ) → finiteSum f cutoff ≡ finiteSum g cutoff
finiteSumCongruence f g pointwise zero = pointwise zero
finiteSumCongruence f g pointwise (suc cutoff) =
  cong₂ Q._+_
    (finiteSumCongruence f g pointwise cutoff)
    (pointwise (suc cutoff))

finiteSumCongruenceBounded : (f g : ℕ → Q.ℚ) →
  (cutoff : ℕ) →
  ((index : ℕ) → ℕOrder._≤_ index cutoff → f index ≡ g index) →
  finiteSum f cutoff ≡ finiteSum g cutoff
finiteSumCongruenceBounded f g zero pointwise =
  pointwise zero ℕOrder.≤-refl
finiteSumCongruenceBounded f g (suc cutoff) pointwise =
  cong₂ Q._+_
    (finiteSumCongruenceBounded f g cutoff
      (λ index index≤cutoff → pointwise index
        (ℕOrder.≤-trans index≤cutoff ℕOrder.≤-sucℕ)))
    (pointwise (suc cutoff) ℕOrder.≤-refl)

module FiniteSumAddPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_)

  collect : (leftSum rightSum leftLast rightLast : fst R) →
    (leftSum +S rightSum) +S (leftLast +S rightLast) ≡
      (leftSum +S leftLast) +S (rightSum +S rightLast)
  collect leftSum rightSum leftLast rightLast = solve! R

finiteSumAdd : (f g : ℕ → Q.ℚ) (cutoff : ℕ) →
  finiteSum (λ index → f index Q.+ g index) cutoff ≡
    finiteSum f cutoff Q.+ finiteSum g cutoff
finiteSumAdd f g zero = refl
finiteSumAdd f g (suc cutoff) =
  cong₂ Q._+_ (finiteSumAdd f g cutoff) refl ∙
  FiniteSumAddPaths.collect PreferredℚCommRing
    (finiteSum f cutoff) (finiteSum g cutoff)
    (f (suc cutoff)) (g (suc cutoff))

finiteDoubleSumSwap : (f : ℕ → ℕ → Q.ℚ) (leftCutoff rightCutoff : ℕ) →
  finiteSum (λ left → finiteSum (f left) rightCutoff) leftCutoff ≡
    finiteSum (λ right → finiteSum (λ left → f left right) leftCutoff)
      rightCutoff
finiteDoubleSumSwap f zero rightCutoff = refl
finiteDoubleSumSwap f (suc leftCutoff) rightCutoff =
  cong₂ Q._+_
    (finiteDoubleSumSwap f leftCutoff rightCutoff) refl ∙
  sym (finiteSumAdd
    (λ right → finiteSum (λ left → f left right) leftCutoff)
    (λ right → f (suc leftCutoff) right)
    rightCutoff)

finiteSumAsBigOp : (f : ℕ → Q.ℚ) (cutoff : ℕ) →
  finiteSum f cutoff ≡
    RationalSum.∑ {n = suc cutoff} (λ i → f (toℕ i))
finiteSumAsBigOp f zero = sym (Q.+IdR (f zero))
finiteSumAsBigOp f (suc cutoff) =
  cong₂ Q._+_
    (finiteSumAsBigOp f cutoff)
    refl ∙
  cong₂ Q._+_
    (cong (λ (values : Fin (suc cutoff) → Q.ℚ) → RationalSum.∑ values)
      (funExt (λ i → cong f (sym (weakenRespToℕ i)))))
    (cong f (sym (toFromId (suc cutoff)))) ∙
  sym (RationalSum.∑Last {n = suc cutoff}
    (λ i → f (toℕ i)))

exponential-convolution-summands-from-factorial-splits :
  (x y : Q.ℚ) (degree : ℕ) →
  ((left : ℕ) → ℕOrder._≤_ left degree →
    reciprocalFactorial left Q.·
      reciprocalFactorial (degree ℕ.∸ left) ≡
    RationalBinomial._choose_ degree left Q.· reciprocalFactorial degree) →
  (left : ℕ) → ℕOrder._≤_ left degree →
  exponentialTerm x left Q.· exponentialTerm y (degree ℕ.∸ left) ≡
    ((RationalBinomial._choose_ degree left Q.·
      taylorMonomialPower x left) Q.·
      taylorMonomialPower y (degree ℕ.∸ left)) Q.·
      reciprocalFactorial degree
exponential-convolution-summands-from-factorial-splits
  x y degree factorialSplits left left≤degree =
  exponential-convolution-summand-from-factorial-split
    x y degree left (factorialSplits left left≤degree)

completed-product-from-series-representative :
  {x y z : RegularCauchy} →
  (dominanceX : DyadicDominates (canonicalRadius x)) →
  (dominanceY : DyadicDominates (canonicalRadius y)) →
  (px : BoundedPresentation x) →
  (py : BoundedPresentation y) →
  z ≈metric boundedProductRegular (fst px) (fst py) →
  SQ.[ z ] ≡ productClassFromDominance x y dominanceX dominanceY
completed-product-from-series-representative dominanceX dominanceY px py relation =
  SQ.eq/ _ _ relation ∙
  sym (productClassFromDominance-from-presentations
    dominanceX dominanceY px py)

finiteSumInterval : (ℕ → Q.ℚ) → ℕ → ℕ → Q.ℚ
finiteSumInterval terms first count =
  finiteSum (λ offset → terms (first ℕ.+ offset)) count

finiteSumSplit : (terms : ℕ → Q.ℚ) (prefixEnd suffixEnd : ℕ) →
  finiteSum terms (prefixEnd ℕ.+ suc suffixEnd) ≡
  finiteSum terms prefixEnd Q.+
    finiteSumInterval terms (suc prefixEnd) suffixEnd
finiteSumSplit terms prefixEnd zero =
  cong (finiteSum terms)
    (ℕ.+-suc prefixEnd zero ∙ cong suc (ℕ.+-zero prefixEnd)) ∙
  cong (finiteSum terms prefixEnd Q.+_)
    (cong terms (sym (ℕ.+-zero (suc prefixEnd))))
finiteSumSplit terms prefixEnd (suc suffixEnd) =
  cong (finiteSum terms) (ℕ.+-suc prefixEnd (suc suffixEnd)) ∙
  cong (λ previous → previous Q.+ terms (suc (prefixEnd ℕ.+ suc suffixEnd)))
    (finiteSumSplit terms prefixEnd suffixEnd) ∙
  sym (Q.+Assoc
    (finiteSum terms prefixEnd)
    (finiteSumInterval terms (suc prefixEnd) suffixEnd)
    (terms (suc (prefixEnd ℕ.+ suc suffixEnd)))) ∙
  cong (finiteSum terms prefixEnd Q.+_)
    (cong
      (λ last → finiteSumInterval terms (suc prefixEnd) suffixEnd Q.+ last)
      (cong terms endpointPath))
  where
  endpointPath : suc (prefixEnd ℕ.+ suc suffixEnd) ≡
    suc prefixEnd ℕ.+ suc suffixEnd
  endpointPath = cong suc (ℕ.+-suc prefixEnd suffixEnd) ∙
    sym (ℕ.+-suc (suc prefixEnd) suffixEnd)

RectangleIndex : ℕ → Type
RectangleIndex cutoff =
  Σ[ left ∈ ℕ ]
    (ℕOrder._≤_ left cutoff ×
      (Σ[ right ∈ ℕ ] ℕOrder._≤_ right cutoff))

UpperTriangularResidualIndex : ℕ → Type
UpperTriangularResidualIndex cutoff =
  Σ[ left ∈ ℕ ]
    (ℕOrder._≤_ left cutoff ×
      (Σ[ right ∈ ℕ ]
        (ℕOrder._≤_ right cutoff × ℕOrder._<_ cutoff (left ℕ.+ right))))

LowerTriangularIndex : ℕ → Type
LowerTriangularIndex cutoff =
  Σ[ left ∈ ℕ ] Σ[ right ∈ ℕ ]
    ℕOrder._≤_ (left ℕ.+ right) cutoff

lowerIndexToRectangle : (cutoff : ℕ) →
  LowerTriangularIndex cutoff → RectangleIndex cutoff
lowerIndexToRectangle cutoff (left , right , sum≤cutoff) =
  left ,
  ℕOrder.≤-trans ℕOrder.≤SumLeft sum≤cutoff ,
  right ,
  ℕOrder.≤-trans ℕOrder.≤SumRight sum≤cutoff

classifyRectangleIndex : (cutoff : ℕ) → RectangleIndex cutoff →
  LowerTriangularIndex cutoff ⊎ UpperTriangularResidualIndex cutoff
classifyRectangleIndex cutoff
  (left , left≤cutoff , right , right≤cutoff)
  with ℕOrder.splitℕ-≤ (left ℕ.+ right) cutoff
... | inl sum≤cutoff = inl (left , right , sum≤cutoff)
... | inr cutoff<sum =
  inr (left , left≤cutoff , right , right≤cutoff , cutoff<sum)

triangularPartitionToRectangle : (cutoff : ℕ) →
  LowerTriangularIndex cutoff ⊎ UpperTriangularResidualIndex cutoff →
  RectangleIndex cutoff
triangularPartitionToRectangle cutoff (inl lower) =
  lowerIndexToRectangle cutoff lower
triangularPartitionToRectangle cutoff
  (inr (left , left≤cutoff , right , right≤cutoff , cutoff<sum)) =
  left , left≤cutoff , right , right≤cutoff

rectangle-classification-section : (cutoff : ℕ) (index : RectangleIndex cutoff) →
  triangularPartitionToRectangle cutoff
    (classifyRectangleIndex cutoff index) ≡ index
rectangle-classification-section cutoff
  (left , left≤cutoff , right , right≤cutoff)
  with ℕOrder.splitℕ-≤ (left ℕ.+ right) cutoff
... | inl sum≤cutoff =
  ΣPathP (refl ,
    ΣPathP (isProp→PathP (λ _ → ℕOrder.isProp≤) _ _ ,
      ΣPathP (refl , isProp→PathP (λ _ → ℕOrder.isProp≤) _ _)))
... | inr cutoff<sum = refl

lower-classification-retract : (cutoff : ℕ)
  (index : LowerTriangularIndex cutoff) →
  classifyRectangleIndex cutoff (lowerIndexToRectangle cutoff index) ≡ inl index
lower-classification-retract cutoff (left , right , sum≤cutoff)
  with ℕOrder.splitℕ-≤ (left ℕ.+ right) cutoff
... | inl anotherSum≤ =
  cong inl
    (ΣPathP (refl ,
      ΣPathP (refl , isProp→PathP (λ _ → ℕOrder.isProp≤) _ _)))
... | inr cutoff<sum = ⊥.rec (ℕOrder.<-asym cutoff<sum sum≤cutoff)

upper-classification-retract : (cutoff : ℕ)
  (index : UpperTriangularResidualIndex cutoff) →
  classifyRectangleIndex cutoff
    (triangularPartitionToRectangle cutoff (inr index)) ≡ inr index
upper-classification-retract cutoff
  (left , left≤cutoff , right , right≤cutoff , cutoff<sum)
  with ℕOrder.splitℕ-≤ (left ℕ.+ right) cutoff
... | inl sum≤cutoff = ⊥.rec (ℕOrder.<-asym cutoff<sum sum≤cutoff)
... | inr anotherCutoff<sum =
  cong inr
    (ΣPathP (refl ,
      ΣPathP (isProp→PathP (λ _ → ℕOrder.isProp≤) _ _ ,
        ΣPathP (refl ,
          ΣPathP (isProp→PathP (λ _ → ℕOrder.isProp≤) _ _ ,
            isProp→PathP (λ _ → ℕOrder.isProp≤) _ _)))))

rectanglePartitionIso : (cutoff : ℕ) →
  Iso (RectangleIndex cutoff)
    (LowerTriangularIndex cutoff ⊎ UpperTriangularResidualIndex cutoff)
rectanglePartitionIso cutoff .Iso.fun = classifyRectangleIndex cutoff
rectanglePartitionIso cutoff .Iso.inv = triangularPartitionToRectangle cutoff
rectanglePartitionIso cutoff .Iso.rightInv (inl index) =
  lower-classification-retract cutoff index
rectanglePartitionIso cutoff .Iso.rightInv (inr index) =
  upper-classification-retract cutoff index
rectanglePartitionIso cutoff .Iso.leftInv =
  rectangle-classification-section cutoff

residualLeft : {cutoff : ℕ} → UpperTriangularResidualIndex cutoff → ℕ
residualLeft (left , _) = left

residualRight : {cutoff : ℕ} → UpperTriangularResidualIndex cutoff → ℕ
residualRight (_ , _ , right , _) = right

upperResidualCrossesSplit :
  (cutoff leftSplit rightSplit : ℕ) →
  cutoff ≡ leftSplit ℕ.+ rightSplit →
  (index : UpperTriangularResidualIndex cutoff) →
  ℕOrder._<_ leftSplit (residualLeft index) ⊎
    ℕOrder._<_ rightSplit (residualRight index)
upperResidualCrossesSplit cutoff leftSplit rightSplit cutoffPath
  (left , left≤cutoff , right , right≤cutoff , cutoff<sum)
  with ℕOrder.splitℕ-≤ left leftSplit
... | inr leftSplit<left = inl leftSplit<left
... | inl left≤leftSplit with ℕOrder.splitℕ-≤ right rightSplit
...   | inr rightSplit<right = inr rightSplit<right
...   | inl right≤rightSplit =
  ⊥.rec
    (ℕOrder.<-asym cutoff<sum
      (subst (ℕOrder._≤_ (left ℕ.+ right)) (sym cutoffPath)
        (ℕOrder.≤-+-≤ left≤leftSplit right≤rightSplit)))

upperResidualCrossesBalancedSplit :
  (halfCutoff : ℕ) →
  (index : UpperTriangularResidualIndex (halfCutoff ℕ.+ halfCutoff)) →
  ℕOrder._<_ halfCutoff (residualLeft index) ⊎
    ℕOrder._<_ halfCutoff (residualRight index)
upperResidualCrossesBalancedSplit halfCutoff index =
  upperResidualCrossesSplit
    (halfCutoff ℕ.+ halfCutoff) halfCutoff halfCutoff refl index

upperResidualCrossesDyadicPredecessorSplit :
  (halfCutoff : ℕ) →
  (index : UpperTriangularResidualIndex
    (halfCutoff ℕ.+ suc halfCutoff)) →
  ℕOrder._<_ halfCutoff (residualLeft index) ⊎
    ℕOrder._<_ (suc halfCutoff) (residualRight index)
upperResidualCrossesDyadicPredecessorSplit halfCutoff index =
  upperResidualCrossesSplit
    (halfCutoff ℕ.+ suc halfCutoff) halfCutoff (suc halfCutoff) refl index

DiagonalTriangularIndex : ℕ → Type
DiagonalTriangularIndex cutoff =
  Σ[ degree ∈ ℕ ]
    (ℕOrder._≤_ degree cutoff ×
      (Σ[ left ∈ ℕ ] Σ[ right ∈ ℕ ] (left ℕ.+ right ≡ degree)))

lowerToDiagonal : (cutoff : ℕ) →
  LowerTriangularIndex cutoff → DiagonalTriangularIndex cutoff
lowerToDiagonal cutoff (left , right , sum≤cutoff) =
  left ℕ.+ right , sum≤cutoff , left , right , refl

diagonalToLower : (cutoff : ℕ) →
  DiagonalTriangularIndex cutoff → LowerTriangularIndex cutoff
diagonalToLower cutoff (degree , degree≤cutoff , left , right , sumPath) =
  left , right , subst (λ value → ℕOrder._≤_ value cutoff) (sym sumPath) degree≤cutoff

lower-diagonal-section : (cutoff : ℕ) (index : LowerTriangularIndex cutoff) →
  diagonalToLower cutoff (lowerToDiagonal cutoff index) ≡ index
lower-diagonal-section cutoff (left , right , sum≤cutoff) =
  ΣPathP (refl , ΣPathP (refl , isProp→PathP (λ _ → ℕOrder.isProp≤) _ _))

lower-diagonal-retract : (cutoff : ℕ) (index : DiagonalTriangularIndex cutoff) →
  lowerToDiagonal cutoff (diagonalToLower cutoff index) ≡ index
lower-diagonal-retract cutoff (degree , degree≤cutoff , left , right , sumPath) =
  retractByPath degree sumPath degree≤cutoff
  where
  retractByPath : (target : ℕ) → (targetPath : left ℕ.+ right ≡ target) →
    (target≤cutoff : ℕOrder._≤_ target cutoff) →
    lowerToDiagonal cutoff
      (diagonalToLower cutoff
        (target , target≤cutoff , left , right , targetPath)) ≡
      (target , target≤cutoff , left , right , targetPath)
  retractByPath target targetPath =
    J (λ target targetPath →
        (target≤cutoff : ℕOrder._≤_ target cutoff) →
        lowerToDiagonal cutoff
          (diagonalToLower cutoff
            (target , target≤cutoff , left , right , targetPath)) ≡
          (target , target≤cutoff , left , right , targetPath))
      (λ target≤cutoff →
        ΣPathP (refl ,
          ΣPathP (isProp→PathP (λ _ → ℕOrder.isProp≤) _ _ ,
            ΣPathP (refl ,
              ΣPathP (refl , isProp→PathP (λ _ → isSetℕ _ _) _ _)))))
      targetPath

lowerDiagonalIso : (cutoff : ℕ) →
  Iso (LowerTriangularIndex cutoff) (DiagonalTriangularIndex cutoff)
lowerDiagonalIso cutoff .Iso.fun = lowerToDiagonal cutoff
lowerDiagonalIso cutoff .Iso.inv = diagonalToLower cutoff
lowerDiagonalIso cutoff .Iso.rightInv = lower-diagonal-retract cutoff
lowerDiagonalIso cutoff .Iso.leftInv = lower-diagonal-section cutoff

lowerTriangularSummand : (a b : ℕ → Q.ℚ) {cutoff : ℕ} →
  LowerTriangularIndex cutoff → Q.ℚ
lowerTriangularSummand a b (left , right , _) = a left Q.· b right

diagonalTriangularSummand : (a b : ℕ → Q.ℚ) {cutoff : ℕ} →
  DiagonalTriangularIndex cutoff → Q.ℚ
diagonalTriangularSummand a b
  (degree , _ , left , right , sumPath) =
  a left Q.· b (degree ℕ.∸ left)

lower-to-diagonal-preserves-summand :
  (a b : ℕ → Q.ℚ) (cutoff : ℕ) →
  (index : LowerTriangularIndex cutoff) →
  diagonalTriangularSummand a b (lowerToDiagonal cutoff index) ≡
    lowerTriangularSummand a b index
lower-to-diagonal-preserves-summand a b cutoff
  (left , right , sum≤cutoff) =
  cong (a left Q.·_) (cong b (ℕ.∸+ right left))

diagonal-to-lower-preserves-summand :
  (a b : ℕ → Q.ℚ) (cutoff : ℕ) →
  (index : DiagonalTriangularIndex cutoff) →
  lowerTriangularSummand a b (diagonalToLower cutoff index) ≡
    diagonalTriangularSummand a b index
diagonal-to-lower-preserves-summand a b cutoff
  (degree , degree≤cutoff , left , right , sumPath) =
  cong (a left Q.·_)
    (sym (cong b
      (cong (λ value → value ℕ.∸ left) (sym sumPath) ∙
        ℕ.∸+ right left)))

record SummandPreservingIso {ℓ₁ ℓ₂} (A : Type ℓ₁) (B : Type ℓ₂)
  (leftWeight : A → Q.ℚ) (rightWeight : B → Q.ℚ) :
  Type (ℓ-max ℓ₁ ℓ₂) where
  field
    indexIso : Iso A B
    preserves : (index : A) →
      rightWeight (Iso.fun indexIso index) ≡ leftWeight index

lowerDiagonalSummandIso : (a b : ℕ → Q.ℚ) (cutoff : ℕ) →
  SummandPreservingIso
    (LowerTriangularIndex cutoff) (DiagonalTriangularIndex cutoff)
    (lowerTriangularSummand a b) (diagonalTriangularSummand a b)
lowerDiagonalSummandIso a b cutoff .SummandPreservingIso.indexIso =
  lowerDiagonalIso cutoff
lowerDiagonalSummandIso a b cutoff .SummandPreservingIso.preserves =
  lower-to-diagonal-preserves-summand a b cutoff

cauchyProductCoefficient : (ℕ → Q.ℚ) → (ℕ → Q.ℚ) → ℕ → Q.ℚ
cauchyProductCoefficient a b degree =
  finiteSum (λ leftDegree →
    a leftDegree Q.· b (degree ℕ.∸ leftDegree)) degree

exponential-coefficient-to-binomial-sum :
  (x y : Q.ℚ) (degree : ℕ) →
  ((left : ℕ) → ℕOrder._≤_ left degree →
    reciprocalFactorial left Q.· reciprocalFactorial (degree ℕ.∸ left) ≡
    RationalBinomial._choose_ degree left Q.· reciprocalFactorial degree) →
  cauchyProductCoefficient (exponentialTerm x) (exponentialTerm y) degree ≡
  finiteSum (λ left →
    ((RationalBinomial._choose_ degree left Q.· taylorMonomialPower x left) Q.·
      taylorMonomialPower y (degree ℕ.∸ left)) Q.·
      reciprocalFactorial degree) degree
exponential-coefficient-to-binomial-sum x y degree factorialSplits =
  finiteSumCongruenceBounded _ _ degree
    (exponential-convolution-summands-from-factorial-splits
      x y degree factorialSplits)

finiteTriangularCauchyProduct :
  (ℕ → Q.ℚ) → (ℕ → Q.ℚ) → ℕ → Q.ℚ
finiteTriangularCauchyProduct a b cutoff =
  finiteSum (cauchyProductCoefficient a b) cutoff

cauchy-product-coefficient-zero : (a b : ℕ → Q.ℚ) →
  cauchyProductCoefficient a b zero ≡ a zero Q.· b zero
cauchy-product-coefficient-zero a b = refl

cauchy-product-coefficient-one : (a b : ℕ → Q.ℚ) →
  cauchyProductCoefficient a b (suc zero) ≡
  (a zero Q.· b (suc zero)) Q.+ (a (suc zero) Q.· b zero)
cauchy-product-coefficient-one a b = refl

exponential-convolution-degree-zero : (x y : Q.ℚ) →
  cauchyProductCoefficient (exponentialTerm x) (exponentialTerm y) zero ≡
  exponentialTerm (x Q.+ y) zero
exponential-convolution-degree-zero x y = Q.·IdR 1

reciprocalSuccessor-zero : reciprocalSuccessor zero ≡ 1
reciprocalSuccessor-zero = refl

exponentialTerm-one : (q : Q.ℚ) →
  exponentialTerm q (suc zero) ≡ q
exponentialTerm-one q =
  cong (λ inverse → ((1 Q.· q) Q.· inverse)) reciprocalSuccessor-zero ∙
  Q.·IdR (1 Q.· q) ∙
  Q.·IdL q

reciprocalSuccessor-one : reciprocalSuccessor (suc zero) ≡ halfℚ 1
reciprocalSuccessor-one = refl

exponentialTerm-two : (q : Q.ℚ) →
  exponentialTerm q (suc (suc zero)) ≡
  (q Q.· q) Q.· halfℚ 1
exponentialTerm-two q =
  cong (λ previous → (previous Q.· q) Q.· reciprocalSuccessor (suc zero))
    (exponentialTerm-one q) ∙
  cong ((q Q.· q) Q.·_) reciprocalSuccessor-one

exponential-convolution-degree-one : (x y : Q.ℚ) →
  cauchyProductCoefficient (exponentialTerm x) (exponentialTerm y) (suc zero) ≡
  exponentialTerm (x Q.+ y) (suc zero)
exponential-convolution-degree-one x y =
  cong₂ Q._+_
    (Q.·IdL (exponentialTerm y (suc zero)) ∙ exponentialTerm-one y)
    (Q.·IdR (exponentialTerm x (suc zero)) ∙ exponentialTerm-one x) ∙
  Q.+Comm y x ∙
  sym (exponentialTerm-one (x Q.+ y))

module DegreeTwoConvolutionPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
    renaming (_+_ to _+S_; _·_ to _·S_; ·IdR to ·IdRS; 1r to 1S)

  distribute-half : (x y half : fst R) → half +S half ≡ 1S →
    ((y ·S y) ·S half +S x ·S y) +S (x ·S x) ·S half ≡
    ((x +S y) ·S (x +S y)) ·S half
  distribute-half x y half half+half=1 =
    cong (λ middle → ((y ·S y) ·S half +S middle) +S
      (x ·S x) ·S half)
      (sym (·IdRS (x ·S y)) ∙
       cong ((x ·S y) ·S_) (sym half+half=1)) ∙
    solve! R

exponential-convolution-degree-two : (x y : Q.ℚ) →
  cauchyProductCoefficient (exponentialTerm x) (exponentialTerm y)
    (suc (suc zero)) ≡
  exponentialTerm (x Q.+ y) (suc (suc zero))
exponential-convolution-degree-two x y =
  cong₂ Q._+_
    (cong₂ Q._+_
      (Q.·IdL (exponentialTerm y 2) ∙ exponentialTerm-two y)
      (cong₂ Q._·_ (exponentialTerm-one x) (exponentialTerm-one y)))
    (Q.·IdR (exponentialTerm x 2) ∙ exponentialTerm-two x) ∙
  DegreeTwoConvolutionPaths.distribute-half PreferredℚCommRing
    x y (halfℚ 1) (half-double 1) ∙
  sym (exponentialTerm-two (x Q.+ y))

finite-triangular-cauchy-product-step :
  (a b : ℕ → Q.ℚ) (cutoff : ℕ) →
  finiteTriangularCauchyProduct a b (suc cutoff) ≡
  finiteTriangularCauchyProduct a b cutoff Q.+
    cauchyProductCoefficient a b (suc cutoff)
finite-triangular-cauchy-product-step a b cutoff = refl

finiteSumNonnegative : (terms : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ terms i) → (cutoff : ℕ) →
  0 ≤ finiteSum terms cutoff
finiteSumNonnegative terms terms≥0 zero = terms≥0 zero
finiteSumNonnegative terms terms≥0 (suc cutoff) =
  subst (_≤ finiteSum terms cutoff Q.+ terms (suc cutoff))
    (Q.+IdL 0)
    (≤Monotone+
      0 (finiteSum terms cutoff) 0 (terms (suc cutoff))
      (finiteSumNonnegative terms terms≥0 cutoff)
      (terms≥0 (suc cutoff)))

interval-last-index : (start count : ℕ) →
  suc start ℕ.+ suc count ≡ suc (start ℕ.+ suc count)
interval-last-index start count = solveℕ!

finiteSumIntervalAsTermBlock : (term : ℕ → Q.ℚ) (start count : ℕ) →
  finiteSumInterval term (suc start) count ≡ termBlock term start (suc count)
finiteSumIntervalAsTermBlock term start zero =
  cong term (ℕ.+-zero (suc start)) ∙
  sym (Q.+IdR (term (suc start)))
finiteSumIntervalAsTermBlock term start (suc count) =
  cong₂ Q._+_ (finiteSumIntervalAsTermBlock term start count)
    (cong term (interval-last-index start count)) ∙
  sym (termBlock-append term start (suc count))

scaledPrecisionMajorant : Q.ℚ → ℕ → Q.ℚ
scaledPrecisionMajorant T index = T Q.· precision index

scaledPrecisionMajorantNonnegative : (T : Q.ℚ) → 0 ≤ T →
  (index : ℕ) → 0 ≤ scaledPrecisionMajorant T index
scaledPrecisionMajorantNonnegative T 0≤T index =
  nonnegative-bound-product T (precision index)
    0≤T (precision-nonnegative index)

nonnegativeProductMonotone : (a b A B : Q.ℚ) →
  0 ≤ b → 0 ≤ A → a ≤ A → b ≤ B → a Q.· b ≤ A Q.· B
nonnegativeProductMonotone a b A B 0≤b 0≤A a≤A b≤B =
  isTrans≤ (a Q.· b) (A Q.· b) (A Q.· B)
    (subst2 _≤_ (Q.·Comm b a) (Q.·Comm b A)
      (left-multiply-monotone b a A 0≤b a≤A))
    (left-multiply-monotone A b B 0≤A b≤B)

scaled-precision-term-block : (T : Q.ℚ) (start count : ℕ) →
  termBlock (scaledPrecisionMajorant T) start count ≡
    T Q.· geometricBlock start count
scaled-precision-term-block T start zero = sym (Q.·AnnihilR T)
scaled-precision-term-block T start (suc count) =
  cong (T Q.· precision (suc start) Q.+_)
    (scaled-precision-term-block T (suc start) count) ∙
  sym (Q.·DistL+ T
    (precision (suc start)) (geometricBlock (suc start) count))

scaledPrecisionTailIntervalBound : (T : Q.ℚ) → 0 ≤ T →
  (start count : ℕ) →
  finiteSumInterval (scaledPrecisionMajorant T) (suc start) count ≤
    T Q.· precision start
scaledPrecisionTailIntervalBound T 0≤T start count =
  transport (λ i → tailPath (~ i) ≤ T Q.· precision start)
    (scaledGeometricBlock≤precision T start (suc count) 0≤T)
  where
  tailPath :
    finiteSumInterval (scaledPrecisionMajorant T) (suc start) count ≡
      T Q.· geometricBlock start (suc count)
  tailPath =
    finiteSumIntervalAsTermBlock (scaledPrecisionMajorant T) start count ∙
    scaled-precision-term-block T start (suc count)

scaledPrecisionBasePath : (T : Q.ℚ) →
  scaledPrecisionMajorant T zero ≡ T
scaledPrecisionBasePath T = Q.·IdR T

scaledPrecisionFiniteSumBound : (T : Q.ℚ) → 0 ≤ T → (cutoff : ℕ) →
  finiteSum (scaledPrecisionMajorant T) cutoff ≤ T Q.+ T
scaledPrecisionFiniteSumBound T 0≤T zero =
  transport (λ i → scaledPrecisionBasePath T (~ i) ≤ T Q.+ T)
    (≤-add-nonnegative T T 0≤T)
scaledPrecisionFiniteSumBound T 0≤T (suc cutoff) =
  subst (_≤ T Q.+ T)
    (sym (finiteSumSplit (scaledPrecisionMajorant T) zero cutoff))
    (≤Monotone+
      (scaledPrecisionMajorant T zero) T
      (finiteSumInterval (scaledPrecisionMajorant T) (suc zero) cutoff) T
      (subst (_≤ T) (sym (scaledPrecisionBasePath T)) (isRefl≤ T))
      (subst
        (finiteSumInterval (scaledPrecisionMajorant T) (suc zero) cutoff ≤_)
        (scaledPrecisionBasePath T)
        (scaledPrecisionTailIntervalBound T 0≤T zero cutoff)))

finiteSumIntervalNonnegative : (terms : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ terms i) → (first count : ℕ) →
  0 ≤ finiteSumInterval terms first count
finiteSumIntervalNonnegative terms terms≥0 first count =
  finiteSumNonnegative
    (λ offset → terms (first ℕ.+ offset))
    (λ offset → terms≥0 (first ℕ.+ offset)) count

finiteSumMonotone : (lower upper : ℕ → Q.ℚ) →
  ((index : ℕ) → lower index ≤ upper index) →
  (cutoff : ℕ) → finiteSum lower cutoff ≤ finiteSum upper cutoff
finiteSumMonotone lower upper pointwise zero = pointwise zero
finiteSumMonotone lower upper pointwise (suc cutoff) =
  ≤Monotone+
    (finiteSum lower cutoff) (finiteSum upper cutoff)
    (lower (suc cutoff)) (upper (suc cutoff))
    (finiteSumMonotone lower upper pointwise cutoff)
    (pointwise (suc cutoff))

finiteSumIntervalMonotone : (lower upper : ℕ → Q.ℚ) →
  ((index : ℕ) → lower index ≤ upper index) →
  (first count : ℕ) →
  finiteSumInterval lower first count ≤ finiteSumInterval upper first count
finiteSumIntervalMonotone lower upper pointwise first count =
  finiteSumMonotone
    (λ offset → lower (first ℕ.+ offset))
    (λ offset → upper (first ℕ.+ offset))
    (λ offset → pointwise (first ℕ.+ offset)) count

finiteSumIntervalCountMonotone :
  (terms : ℕ → Q.ℚ) → ((index : ℕ) → 0 ≤ terms index) →
  (first count extra : ℕ) →
  finiteSumInterval terms first count ≤
    finiteSumInterval terms first (count ℕ.+ suc extra)
finiteSumIntervalCountMonotone terms terms≥0 first count extra =
  subst (finiteSumInterval terms first count ≤_)
    (sym (finiteSumSplit
      (λ offset → terms (first ℕ.+ offset)) count extra))
    (≤-add-nonnegative
      (finiteSumInterval terms first count)
      (finiteSumInterval
        (λ offset → terms (first ℕ.+ offset)) (suc count) extra)
      (finiteSumIntervalNonnegative
        (λ offset → terms (first ℕ.+ offset))
        (λ offset → terms≥0 (first ℕ.+ offset))
        (suc count) extra))

finiteSumIntervalShiftedSuffixBelowWhole :
  (terms : ℕ → Q.ℚ) → ((index : ℕ) → 0 ≤ terms index) →
  (first prefix count : ℕ) →
  finiteSumInterval terms (first ℕ.+ suc prefix) count ≤
    finiteSumInterval terms first (prefix ℕ.+ suc count)
finiteSumIntervalShiftedSuffixBelowWhole terms terms≥0 first prefix count =
  subst (_≤ finiteSumInterval terms first (prefix ℕ.+ suc count))
    (finiteSumCongruence _ _
      (λ offset → cong terms (ℕ.+-assoc first (suc prefix) offset))
      count)
    (subst
      (finiteSumInterval (λ offset → terms (first ℕ.+ offset))
        (suc prefix) count ≤_)
      (Q.+Comm
        (finiteSumInterval (λ offset → terms (first ℕ.+ offset))
          (suc prefix) count)
        (finiteSumInterval terms first prefix) ∙
       sym (finiteSumSplit (λ offset → terms (first ℕ.+ offset)) prefix count))
      (≤-add-nonnegative
        (finiteSumInterval (λ offset → terms (first ℕ.+ offset))
          (suc prefix) count)
        (finiteSumInterval terms first prefix)
        (finiteSumIntervalNonnegative terms terms≥0 first prefix)))

finiteSumMonotoneBounded : (lower upper : ℕ → Q.ℚ) →
  (cutoff : ℕ) →
  ((index : ℕ) → ℕOrder._≤_ index cutoff → lower index ≤ upper index) →
  finiteSum lower cutoff ≤ finiteSum upper cutoff
finiteSumMonotoneBounded lower upper zero pointwise =
  pointwise zero ℕOrder.≤-refl
finiteSumMonotoneBounded lower upper (suc cutoff) pointwise =
  ≤Monotone+
    (finiteSum lower cutoff) (finiteSum upper cutoff)
    (lower (suc cutoff)) (upper (suc cutoff))
    (finiteSumMonotoneBounded lower upper cutoff
      (λ index index≤cutoff → pointwise index
        (ℕOrder.≤-trans index≤cutoff ℕOrder.≤-sucℕ)))
    (pointwise (suc cutoff) ℕOrder.≤-refl)

finiteSumMagnitudeBound :
  (term majorant : ℕ → Q.ℚ) →
  ((index : ℕ) → MagnitudeBound (term index) (majorant index)) →
  (cutoff : ℕ) →
  MagnitudeBound (finiteSum term cutoff) (finiteSum majorant cutoff)
finiteSumMagnitudeBound term majorant pointBound zero = pointBound zero
finiteSumMagnitudeBound term majorant pointBound (suc cutoff) =
  add-magnitude-bounds _ _ _ _
    (finiteSumMagnitudeBound term majorant pointBound cutoff)
    (pointBound (suc cutoff))

cauchyProductCoefficientMagnitudeBound :
  (a A b B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  ((i : ℕ) → MagnitudeBound (a i) (A i)) →
  ((j : ℕ) → MagnitudeBound (b j) (B j)) →
  (degree : ℕ) →
  MagnitudeBound
    (cauchyProductCoefficient a b degree)
    (cauchyProductCoefficient A B degree)
cauchyProductCoefficientMagnitudeBound a A b B A≥0 B≥0 aBound bBound degree =
  finiteSumMagnitudeBound
    (λ i → a i Q.· b (degree ∸ i))
    (λ i → A i Q.· B (degree ∸ i))
    (λ i → arbitrary-multiplier-bound
      (a i) (A i) (b (degree ∸ i)) (B (degree ∸ i))
      (A≥0 i) (B≥0 (degree ∸ i))
      (aBound i) (bBound (degree ∸ i)))
    degree

finiteTriangularCauchyProductMagnitudeBound :
  (a A b B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  ((i : ℕ) → MagnitudeBound (a i) (A i)) →
  ((j : ℕ) → MagnitudeBound (b j) (B j)) →
  (cutoff : ℕ) →
  MagnitudeBound
    (finiteTriangularCauchyProduct a b cutoff)
    (finiteTriangularCauchyProduct A B cutoff)
finiteTriangularCauchyProductMagnitudeBound
  a A b B A≥0 B≥0 aBound bBound cutoff =
  finiteSumMagnitudeBound
    (cauchyProductCoefficient a b)
    (cauchyProductCoefficient A B)
    (cauchyProductCoefficientMagnitudeBound
      a A b B A≥0 B≥0 aBound bBound)
    cutoff

finiteSumIntervalMagnitudeBound :
  (term majorant : ℕ → Q.ℚ) →
  ((index : ℕ) → MagnitudeBound (term index) (majorant index)) →
  (first count : ℕ) →
  MagnitudeBound
    (finiteSumInterval term first count)
    (finiteSumInterval majorant first count)
finiteSumIntervalMagnitudeBound term majorant pointBound first count =
  finiteSumMagnitudeBound
    (λ offset → term (first ℕ.+ offset))
    (λ offset → majorant (first ℕ.+ offset))
    (λ offset → pointBound (first ℕ.+ offset))
    count

finiteSumRightScale : (a : ℕ → Q.ℚ) (factor : Q.ℚ) (cutoff : ℕ) →
  finiteSum (λ i → a i Q.· factor) cutoff ≡
  finiteSum a cutoff Q.· factor
finiteSumRightScale a factor zero = refl
finiteSumRightScale a factor (suc cutoff) =
  cong (Q._+ (a (suc cutoff) Q.· factor))
    (finiteSumRightScale a factor cutoff) ∙
  sym (Q.·DistR+ (finiteSum a cutoff) (a (suc cutoff)) factor)

finiteSumIntervalRightScale :
  (a : ℕ → Q.ℚ) (factor : Q.ℚ) (first count : ℕ) →
  finiteSumInterval (λ index → a index Q.· factor) first count ≡
    finiteSumInterval a first count Q.· factor
finiteSumIntervalRightScale a factor first count =
  finiteSumRightScale (λ offset → a (first ℕ.+ offset)) factor count

finiteSumLeftScale : (factor : Q.ℚ) (b : ℕ → Q.ℚ) (cutoff : ℕ) →
  finiteSum (λ index → factor Q.· b index) cutoff ≡
    factor Q.· finiteSum b cutoff
finiteSumLeftScale factor b cutoff =
  finiteSumCongruence _ _ (λ index → Q.·Comm factor (b index)) cutoff ∙
  finiteSumRightScale b factor cutoff ∙
  Q.·Comm (finiteSum b cutoff) factor

finiteSumIntervalLeftScale :
  (factor : Q.ℚ) (b : ℕ → Q.ℚ) (first count : ℕ) →
  finiteSumInterval (λ index → factor Q.· b index) first count ≡
    factor Q.· finiteSumInterval b first count
finiteSumIntervalLeftScale factor b first count =
  finiteSumLeftScale factor (λ offset → b (first ℕ.+ offset)) count

finite-binomial-monomial-sum : (degree : ℕ) (x y : Q.ℚ) →
  finiteSum (λ left →
    (RationalBinomial._choose_ degree left Q.·
      taylorMonomialPower x left) Q.·
      taylorMonomialPower y (degree ℕ.∸ left)) degree ≡
    rationalBinomialExpansion degree x y
finite-binomial-monomial-sum degree x y =
  finiteSumAsBigOp _ degree ∙
  RationalSum.∑Ext {n = suc degree} (λ i →
    cong₂ Q._·_
      (cong (RationalBinomial._choose_ degree (toℕ i) Q.·_)
        (taylor-monomial-is-ring-power x (toℕ i)))
      (taylor-monomial-is-ring-power y (degree ℕ.∸ toℕ i)))

exponential-coefficient-convolution-from-factorial-splits :
  (x y : Q.ℚ) (degree : ℕ) →
  ((left : ℕ) → ℕOrder._≤_ left degree →
    reciprocalFactorial left Q.·
      reciprocalFactorial (degree ℕ.∸ left) ≡
    RationalBinomial._choose_ degree left Q.· reciprocalFactorial degree) →
  cauchyProductCoefficient (exponentialTerm x) (exponentialTerm y) degree ≡
    exponentialTerm (x Q.+ y) degree
exponential-coefficient-convolution-from-factorial-splits
  x y degree factorialSplits =
  exponential-coefficient-to-binomial-sum x y degree factorialSplits ∙
  finiteSumRightScale _ (reciprocalFactorial degree) degree ∙
  cong (Q._· reciprocalFactorial degree)
    (finite-binomial-monomial-sum degree x y) ∙
  cong (Q._· reciprocalFactorial degree)
    (sym (taylor-monomial-binomial-expansion degree x y)) ∙
  sym (exponential-term-factorization (x Q.+ y) degree)

exponential-coefficient-convolution : (x y : Q.ℚ) (degree : ℕ) →
  cauchyProductCoefficient (exponentialTerm x) (exponentialTerm y) degree ≡
    exponentialTerm (x Q.+ y) degree
exponential-coefficient-convolution x y degree =
  exponential-coefficient-convolution-from-factorial-splits
    x y degree (reciprocal-factorial-split degree)

finite-triangular-exponential-product : (x y : Q.ℚ) (cutoff : ℕ) →
  finiteTriangularCauchyProduct
    (exponentialTerm x) (exponentialTerm y) cutoff ≡
  finiteSum (exponentialTerm (x Q.+ y)) cutoff
finite-triangular-exponential-product x y cutoff =
  finiteSumCongruence _ _
    (exponential-coefficient-convolution x y) cutoff

exponential-convolution-degree-three : (x y : Q.ℚ) →
  cauchyProductCoefficient (exponentialTerm x) (exponentialTerm y)
    (suc (suc (suc zero))) ≡
  exponentialTerm (x Q.+ y) (suc (suc (suc zero)))
exponential-convolution-degree-three x y =
  exponential-coefficient-convolution-from-factorial-splits
    x y (suc (suc (suc zero))) reciprocal-factorial-splits-three

finiteRectangularCauchyProduct :
  (a b : ℕ → Q.ℚ) → ℕ → ℕ → Q.ℚ
finiteRectangularCauchyProduct a b leftCutoff rightCutoff =
  finiteSum (λ i → a i Q.· finiteSum b rightCutoff) leftCutoff

finite-sum-product-is-rectangular-cauchy-product :
  (a b : ℕ → Q.ℚ) (leftCutoff rightCutoff : ℕ) →
  finiteSum a leftCutoff Q.· finiteSum b rightCutoff ≡
  finiteRectangularCauchyProduct a b leftCutoff rightCutoff
finite-sum-product-is-rectangular-cauchy-product a b leftCutoff rightCutoff =
  sym (finiteSumRightScale a (finiteSum b rightCutoff) leftCutoff)

finiteRectangularCauchyProductByRows :
  (a b : ℕ → Q.ℚ) (leftCutoff rightCutoff : ℕ) →
  finiteRectangularCauchyProduct a b leftCutoff rightCutoff ≡
  finiteSum (λ i → finiteSum (λ j → a i Q.· b j) rightCutoff)
    leftCutoff
finiteRectangularCauchyProductByRows a b leftCutoff rightCutoff =
  cong finiteSumFunction (funExt rowPath)
  where
  finiteSumFunction : (ℕ → Q.ℚ) → Q.ℚ
  finiteSumFunction terms = finiteSum terms leftCutoff

  rowPath : (i : ℕ) →
    a i Q.· finiteSum b rightCutoff ≡
    finiteSum (λ j → a i Q.· b j) rightCutoff
  rowPath i =
    Q.·Comm (a i) (finiteSum b rightCutoff) ∙
    sym (finiteSumRightScale b (a i) rightCutoff) ∙
    cong (λ value → finiteSum value rightCutoff)
      (funExt (λ j → Q.·Comm (b j) (a i)))

finiteTriangularResidual : (ℕ → Q.ℚ) → (ℕ → Q.ℚ) → ℕ → Q.ℚ
finiteTriangularResidual a b cutoff =
  finiteRectangularCauchyProduct a b cutoff cutoff Q.+
    (Q.- finiteTriangularCauchyProduct a b cutoff)

triangularRow : (ℕ → ℕ → Q.ℚ) → ℕ → ℕ → Q.ℚ
triangularRow f cutoff left = finiteSum (f left) (cutoff ℕ.∸ left)

triangular-row-successor : (f : ℕ → ℕ → Q.ℚ) (cutoff left : ℕ) →
  ℕOrder._≤_ left cutoff →
  triangularRow f (suc cutoff) left ≡
    triangularRow f cutoff left Q.+ f left (suc (cutoff ℕ.∸ left))
triangular-row-successor f cutoff left left≤cutoff =
  cong (finiteSum (f left)) (sym (ℕOrder.≤-∸-suc left≤cutoff))

triangular-old-rows-successor : (f : ℕ → ℕ → Q.ℚ) (cutoff : ℕ) →
  finiteSum (triangularRow f (suc cutoff)) cutoff ≡
    finiteSum (triangularRow f cutoff) cutoff Q.+
      finiteSum (λ left → f left (suc (cutoff ℕ.∸ left))) cutoff
triangular-old-rows-successor f cutoff =
  finiteSumCongruenceBounded _ _ cutoff
    (triangular-row-successor f cutoff) ∙
  finiteSumAdd (triangularRow f cutoff)
    (λ left → f left (suc (cutoff ℕ.∸ left))) cutoff

finiteTriangleByRows : (ℕ → ℕ → Q.ℚ) → ℕ → Q.ℚ
finiteTriangleByRows f cutoff = finiteSum (triangularRow f cutoff) cutoff

finiteDiagonal : (ℕ → ℕ → Q.ℚ) → ℕ → Q.ℚ
finiteDiagonal f degree =
  finiteSum (λ left → f left (degree ℕ.∸ left)) degree

triangular-corner-row : (f : ℕ → ℕ → Q.ℚ) (cutoff : ℕ) →
  triangularRow f (suc cutoff) (suc cutoff) ≡ f (suc cutoff) zero
triangular-corner-row f cutoff =
  cong (finiteSum (f (suc cutoff))) (ℕOrder.n∸n≡0 cutoff)

module TriangleStepPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_)
  reassociate : (triangle endpoints corner : fst R) →
    (triangle +S endpoints) +S corner ≡ triangle +S (endpoints +S corner)
  reassociate triangle endpoints corner = solve! R

finite-triangle-outer-step : (f : ℕ → ℕ → Q.ℚ) (cutoff : ℕ) →
  finiteTriangleByRows f (suc cutoff) ≡
    finiteSum (triangularRow f (suc cutoff)) cutoff Q.+
      triangularRow f (suc cutoff) (suc cutoff)
finite-triangle-outer-step f cutoff = refl

finite-diagonal-step : (f : ℕ → ℕ → Q.ℚ) (cutoff : ℕ) →
  finiteDiagonal f (suc cutoff) ≡
    finiteSum (λ left → f left (suc cutoff ℕ.∸ left)) cutoff Q.+
      f (suc cutoff) zero
finite-diagonal-step f cutoff =
  cong (finiteSum (λ left → f left (suc cutoff ℕ.∸ left)) cutoff Q.+_)
    (cong (f (suc cutoff)) (ℕOrder.n∸n≡0 cutoff))

finite-triangle-by-rows-step : (f : ℕ → ℕ → Q.ℚ) (cutoff : ℕ) →
  finiteTriangleByRows f (suc cutoff) ≡
    finiteTriangleByRows f cutoff Q.+ finiteDiagonal f (suc cutoff)
finite-triangle-by-rows-step f cutoff =
  finite-triangle-outer-step f cutoff ∙
  cong₂ Q._+_ (triangular-old-rows-successor f cutoff)
    (triangular-corner-row f cutoff) ∙
  TriangleStepPaths.reassociate PreferredℚCommRing
    (finiteTriangleByRows f cutoff)
    (finiteSum (λ left → f left (suc (cutoff ℕ.∸ left))) cutoff)
    (f (suc cutoff) zero) ∙
  cong (finiteTriangleByRows f cutoff Q.+_)
    (cong₂ Q._+_
      (finiteSumCongruenceBounded _ _ cutoff
        (λ left left≤cutoff →
          cong (f left) (ℕOrder.≤-∸-suc left≤cutoff))) refl ∙
     sym (finite-diagonal-step f cutoff))

finiteTriangleByDiagonals : (ℕ → ℕ → Q.ℚ) → ℕ → Q.ℚ
finiteTriangleByDiagonals f cutoff = finiteSum (finiteDiagonal f) cutoff

finite-triangle-rows-equal-diagonals :
  (f : ℕ → ℕ → Q.ℚ) (cutoff : ℕ) →
  finiteTriangleByRows f cutoff ≡ finiteTriangleByDiagonals f cutoff
finite-triangle-rows-equal-diagonals f zero = refl
finite-triangle-rows-equal-diagonals f (suc cutoff) =
  finite-triangle-by-rows-step f cutoff ∙
  cong₂ Q._+_ (finite-triangle-rows-equal-diagonals f cutoff) refl

finite-triangle-by-rows-is-diagonal :
  (f : ℕ → ℕ → Q.ℚ) (cutoff : ℕ) →
  finiteTriangleByRows f cutoff ≡ finiteSum (finiteDiagonal f) cutoff
finite-triangle-by-rows-is-diagonal f zero = refl
finite-triangle-by-rows-is-diagonal f (suc cutoff) =
  finite-triangle-by-rows-step f cutoff ∙
  cong₂ Q._+_ (finite-triangle-by-rows-is-diagonal f cutoff) refl

lowerTriangularRow : (ℕ → Q.ℚ) → (ℕ → Q.ℚ) → ℕ → ℕ → Q.ℚ
lowerTriangularRow a b cutoff left =
  finiteSum (λ right → a left Q.· b right) (cutoff ∸ left)

successor-sum-reorder : (x y : ℕ) →
  suc (x ℕ.+ suc y) ≡ suc y ℕ.+ suc x
successor-sum-reorder x y = solveℕ!

lowResidualStartPath : (halfCutoff left : ℕ) →
  ℕOrder._≤_ left halfCutoff →
  suc ((halfCutoff ℕ.+ suc halfCutoff) ℕ.∸ left) ≡
    suc halfCutoff ℕ.+ suc (halfCutoff ℕ.∸ left)
lowResidualStartPath halfCutoff left left≤half =
  cong suc
    (subtract-from-left-summand halfCutoff (suc halfCutoff) left left≤half) ∙
  successor-sum-reorder (halfCutoff ℕ.∸ left) halfCutoff

lowResidualCountPath : (halfCutoff leftPredecessor : ℕ) →
  ℕOrder._≤_ (suc leftPredecessor) halfCutoff →
  (halfCutoff ℕ.∸ suc leftPredecessor) ℕ.+ suc leftPredecessor ≡
    halfCutoff
lowResidualCountPath halfCutoff leftPredecessor left≤half =
  ℕOrder.≤-∸-+-cancel left≤half

upperResidualRow : (ℕ → Q.ℚ) → (ℕ → Q.ℚ) → ℕ → ℕ → Q.ℚ
upperResidualRow a b cutoff zero = 0
upperResidualRow a b cutoff (suc leftPredecessor) =
  finiteSumInterval
    (λ right → a (suc leftPredecessor) Q.· b right)
    (suc (cutoff ∸ suc leftPredecessor))
    leftPredecessor

finiteUpperResidualByRows :
  (ℕ → Q.ℚ) → (ℕ → Q.ℚ) → ℕ → Q.ℚ
finiteUpperResidualByRows a b cutoff =
  finiteSum (upperResidualRow a b cutoff) cutoff

upperResidualRowNonnegative :
  (A B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  (cutoff left : ℕ) → 0 ≤ upperResidualRow A B cutoff left
upperResidualRowNonnegative A B A≥0 B≥0 cutoff zero = isRefl≤ 0
upperResidualRowNonnegative A B A≥0 B≥0 cutoff (suc leftPredecessor) =
  finiteSumIntervalNonnegative
    (λ right → A (suc leftPredecessor) Q.· B right)
    (λ right → nonnegative-bound-product
      (A (suc leftPredecessor)) (B right)
      (A≥0 (suc leftPredecessor)) (B≥0 right))
    (suc (cutoff ℕ.∸ suc leftPredecessor)) leftPredecessor

lowUpperResidualRowTailBound :
  (A B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  (halfCutoff left : ℕ) → ℕOrder._≤_ left halfCutoff →
  upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff) left ≤
    A left Q.· finiteSumInterval B (suc halfCutoff) halfCutoff
lowUpperResidualRowTailBound A B A≥0 B≥0 halfCutoff zero left≤half =
  nonnegative-bound-product
    (A zero) (finiteSumInterval B (suc halfCutoff) halfCutoff)
    (A≥0 zero)
    (finiteSumIntervalNonnegative B B≥0 (suc halfCutoff) halfCutoff)
lowUpperResidualRowTailBound A B A≥0 B≥0 halfCutoff
  (suc leftPredecessor) left≤half =
  transport
    (λ i → sourcePath (~ i) ≤ targetPath i)
    (finiteSumIntervalShiftedSuffixBelowWhole
      (λ right → A (suc leftPredecessor) Q.· B right)
      (λ right → nonnegative-bound-product
        (A (suc leftPredecessor)) (B right)
        (A≥0 (suc leftPredecessor)) (B≥0 right))
      (suc halfCutoff) (halfCutoff ℕ.∸ suc leftPredecessor)
      leftPredecessor)
  where
  sourcePath :
    upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff)
      (suc leftPredecessor) ≡
    finiteSumInterval
      (λ right → A (suc leftPredecessor) Q.· B right)
      (suc halfCutoff ℕ.+ suc (halfCutoff ℕ.∸ suc leftPredecessor))
      leftPredecessor
  sourcePath = cong
    (λ first → finiteSumInterval
      (λ right → A (suc leftPredecessor) Q.· B right)
      first leftPredecessor)
    (lowResidualStartPath halfCutoff (suc leftPredecessor) left≤half)

  targetPath :
    finiteSumInterval
      (λ right → A (suc leftPredecessor) Q.· B right)
      (suc halfCutoff)
      ((halfCutoff ℕ.∸ suc leftPredecessor) ℕ.+ suc leftPredecessor) ≡
    A (suc leftPredecessor) Q.·
      finiteSumInterval B (suc halfCutoff) halfCutoff
  targetPath =
    cong (finiteSumInterval
      (λ right → A (suc leftPredecessor) Q.· B right)
      (suc halfCutoff))
      (lowResidualCountPath halfCutoff leftPredecessor left≤half) ∙
    finiteSumIntervalLeftScale
      (A (suc leftPredecessor)) B (suc halfCutoff) halfCutoff

finiteUpperLowRowsTailProductBound :
  (A B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  (halfCutoff : ℕ) →
  finiteSum
    (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff)) halfCutoff ≤
  finiteSum A halfCutoff Q.·
    finiteSumInterval B (suc halfCutoff) halfCutoff
finiteUpperLowRowsTailProductBound A B A≥0 B≥0 halfCutoff =
  subst
    (finiteSum
      (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff)) halfCutoff ≤_)
    (finiteSumRightScale A
      (finiteSumInterval B (suc halfCutoff) halfCutoff) halfCutoff)
    (finiteSumMonotoneBounded _ _ halfCutoff
      (λ left left≤half →
        lowUpperResidualRowTailBound
          A B A≥0 B≥0 halfCutoff left left≤half))

finiteUpperResidualByRowsNonnegative :
  (A B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  (cutoff : ℕ) → 0 ≤ finiteUpperResidualByRows A B cutoff
finiteUpperResidualByRowsNonnegative A B A≥0 B≥0 cutoff =
  finiteSumNonnegative (upperResidualRow A B cutoff)
    (upperResidualRowNonnegative A B A≥0 B≥0 cutoff) cutoff

finiteUpperResidualDyadicPredecessorSplit :
  (A B : ℕ → Q.ℚ) (halfCutoff : ℕ) →
  finiteUpperResidualByRows A B (halfCutoff ℕ.+ suc halfCutoff) ≡
    finiteSum
      (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff)) halfCutoff Q.+
    finiteSumInterval
      (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff))
      (suc halfCutoff) halfCutoff
finiteUpperResidualDyadicPredecessorSplit A B halfCutoff =
  finiteSumSplit
    (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff))
    halfCutoff halfCutoff

rectangular-row-splits-at-diagonal :
  (a b : ℕ → Q.ℚ) (cutoff leftPredecessor : ℕ) →
  (cutoff ∸ suc leftPredecessor) ℕ.+ suc leftPredecessor ≡ cutoff →
  finiteSum (λ right → a (suc leftPredecessor) Q.· b right) cutoff ≡
    lowerTriangularRow a b cutoff (suc leftPredecessor) Q.+
    upperResidualRow a b cutoff (suc leftPredecessor)
rectangular-row-splits-at-diagonal
  a b cutoff leftPredecessor cutoffPath =
  cong (finiteSum (λ right → a (suc leftPredecessor) Q.· b right))
    (sym cutoffPath) ∙
  finiteSumSplit
    (λ right → a (suc leftPredecessor) Q.· b right)
    (cutoff ∸ suc leftPredecessor) leftPredecessor

upper-residual-row-split :
  (a b : ℕ → Q.ℚ) (cutoff left : ℕ) →
  ℕOrder._≤_ left cutoff →
  finiteSum (λ right → a left Q.· b right) cutoff ≡
    finiteSum (λ right → a left Q.· b right) (cutoff ∸ left) Q.+
      upperResidualRow a b cutoff left
upper-residual-row-split a b cutoff zero zero≤cutoff =
  sym (Q.+IdR (finiteSum (λ right → a zero Q.· b right) cutoff))
upper-residual-row-split a b cutoff (suc leftPredecessor) left≤cutoff =
  rectangular-row-splits-at-diagonal a b cutoff leftPredecessor
    (ℕOrder.≤-∸-+-cancel left≤cutoff)

upperResidualRowBelowFullRow :
  (A B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  (cutoff left : ℕ) → ℕOrder._≤_ left cutoff →
  upperResidualRow A B cutoff left ≤
    finiteSum (λ right → A left Q.· B right) cutoff
upperResidualRowBelowFullRow A B A≥0 B≥0 cutoff left left≤cutoff =
  subst (upperResidualRow A B cutoff left ≤_)
    (Q.+Comm
      (upperResidualRow A B cutoff left)
      (finiteSum (λ right → A left Q.· B right) (cutoff ℕ.∸ left)) ∙
     sym (upper-residual-row-split A B cutoff left left≤cutoff))
    (≤-add-nonnegative
      (upperResidualRow A B cutoff left)
      (finiteSum (λ right → A left Q.· B right) (cutoff ℕ.∸ left))
      (finiteSumNonnegative (λ right → A left Q.· B right)
        (λ right → nonnegative-bound-product
          (A left) (B right) (A≥0 left) (B≥0 right))
        (cutoff ℕ.∸ left)))

finiteUpperHighRowsBelowFullRows :
  (A B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  (halfCutoff : ℕ) →
  finiteSumInterval
    (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff))
    (suc halfCutoff) halfCutoff ≤
  finiteSumInterval
    (λ left → finiteSum
      (λ right → A left Q.· B right)
      (halfCutoff ℕ.+ suc halfCutoff))
    (suc halfCutoff) halfCutoff
finiteUpperHighRowsBelowFullRows A B A≥0 B≥0 halfCutoff =
  finiteSumMonotoneBounded _ _ halfCutoff
    (λ offset offset≤half →
      upperResidualRowBelowFullRow A B A≥0 B≥0
        (halfCutoff ℕ.+ suc halfCutoff) (suc halfCutoff ℕ.+ offset)
        (subst (ℕOrder._≤_ (suc halfCutoff ℕ.+ offset))
          (ℕ.+-comm (suc halfCutoff) halfCutoff)
          (ℕOrder.≤-+-≤ ℕOrder.≤-refl offset≤half)))

finiteUpperHighRowsTailProductBound :
  (A B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  (halfCutoff : ℕ) →
  finiteSumInterval
    (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff))
    (suc halfCutoff) halfCutoff ≤
  finiteSumInterval A (suc halfCutoff) halfCutoff Q.·
    finiteSum B (halfCutoff ℕ.+ suc halfCutoff)
finiteUpperHighRowsTailProductBound A B A≥0 B≥0 halfCutoff =
  subst
    (finiteSumInterval
      (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff))
      (suc halfCutoff) halfCutoff ≤_)
    (finiteSumCongruence _ _
      (λ offset → finiteSumLeftScale
        (A (suc halfCutoff ℕ.+ offset)) B
        (halfCutoff ℕ.+ suc halfCutoff)) halfCutoff ∙
     finiteSumIntervalRightScale A
      (finiteSum B (halfCutoff ℕ.+ suc halfCutoff))
      (suc halfCutoff) halfCutoff)
    (finiteUpperHighRowsBelowFullRows A B A≥0 B≥0 halfCutoff)

finiteUpperResidualSplitTailProductBound :
  (A B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  (halfCutoff : ℕ) →
  finiteUpperResidualByRows A B (halfCutoff ℕ.+ suc halfCutoff) ≤
    (finiteSum A halfCutoff Q.·
      finiteSumInterval B (suc halfCutoff) halfCutoff) Q.+
    (finiteSumInterval A (suc halfCutoff) halfCutoff Q.·
      finiteSum B (halfCutoff ℕ.+ suc halfCutoff))
finiteUpperResidualSplitTailProductBound A B A≥0 B≥0 halfCutoff =
  subst (_≤
    ((finiteSum A halfCutoff Q.·
       finiteSumInterval B (suc halfCutoff) halfCutoff) Q.+
     (finiteSumInterval A (suc halfCutoff) halfCutoff Q.·
       finiteSum B (halfCutoff ℕ.+ suc halfCutoff))))
    (sym (finiteUpperResidualDyadicPredecessorSplit A B halfCutoff))
    (≤Monotone+
      (finiteSum
        (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff)) halfCutoff)
      (finiteSum A halfCutoff Q.·
        finiteSumInterval B (suc halfCutoff) halfCutoff)
      (finiteSumInterval
        (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff))
        (suc halfCutoff) halfCutoff)
      (finiteSumInterval A (suc halfCutoff) halfCutoff Q.·
        finiteSum B (halfCutoff ℕ.+ suc halfCutoff))
      (finiteUpperLowRowsTailProductBound A B A≥0 B≥0 halfCutoff)
      (finiteUpperHighRowsTailProductBound A B A≥0 B≥0 halfCutoff))

scaledPrecisionUpperResidualBound :
  (TA TB : Q.ℚ) → 0 ≤ TA → 0 ≤ TB → (halfCutoff : ℕ) →
  finiteUpperResidualByRows
    (scaledPrecisionMajorant TA) (scaledPrecisionMajorant TB)
    (halfCutoff ℕ.+ suc halfCutoff) ≤
  ((TA Q.+ TA) Q.· (TB Q.· precision halfCutoff)) Q.+
    ((TA Q.· precision halfCutoff) Q.· (TB Q.+ TB))
scaledPrecisionUpperResidualBound TA TB 0≤TA 0≤TB halfCutoff =
  isTrans≤
    (finiteUpperResidualByRows
      (scaledPrecisionMajorant TA) (scaledPrecisionMajorant TB)
      (halfCutoff ℕ.+ suc halfCutoff))
    ((finiteSum (scaledPrecisionMajorant TA) halfCutoff Q.·
       finiteSumInterval (scaledPrecisionMajorant TB)
         (suc halfCutoff) halfCutoff) Q.+
     (finiteSumInterval (scaledPrecisionMajorant TA)
         (suc halfCutoff) halfCutoff Q.·
       finiteSum (scaledPrecisionMajorant TB)
         (halfCutoff ℕ.+ suc halfCutoff)))
    (((TA Q.+ TA) Q.· (TB Q.· precision halfCutoff)) Q.+
      ((TA Q.· precision halfCutoff) Q.· (TB Q.+ TB)))
    (finiteUpperResidualSplitTailProductBound
      (scaledPrecisionMajorant TA) (scaledPrecisionMajorant TB)
      (scaledPrecisionMajorantNonnegative TA 0≤TA)
      (scaledPrecisionMajorantNonnegative TB 0≤TB) halfCutoff)
    (≤Monotone+
      (finiteSum (scaledPrecisionMajorant TA) halfCutoff Q.·
        finiteSumInterval (scaledPrecisionMajorant TB)
          (suc halfCutoff) halfCutoff)
      ((TA Q.+ TA) Q.· (TB Q.· precision halfCutoff))
      (finiteSumInterval (scaledPrecisionMajorant TA)
          (suc halfCutoff) halfCutoff Q.·
        finiteSum (scaledPrecisionMajorant TB)
          (halfCutoff ℕ.+ suc halfCutoff))
      ((TA Q.· precision halfCutoff) Q.· (TB Q.+ TB))
      (nonnegativeProductMonotone
        (finiteSum (scaledPrecisionMajorant TA) halfCutoff)
        (finiteSumInterval (scaledPrecisionMajorant TB)
          (suc halfCutoff) halfCutoff)
        (TA Q.+ TA) (TB Q.· precision halfCutoff)
        (finiteSumIntervalNonnegative (scaledPrecisionMajorant TB)
          (scaledPrecisionMajorantNonnegative TB 0≤TB)
          (suc halfCutoff) halfCutoff)
        (≤Monotone+ 0 TA 0 TA 0≤TA 0≤TA)
        (scaledPrecisionFiniteSumBound TA 0≤TA halfCutoff)
        (scaledPrecisionTailIntervalBound TB 0≤TB halfCutoff halfCutoff))
      (nonnegativeProductMonotone
        (finiteSumInterval (scaledPrecisionMajorant TA)
          (suc halfCutoff) halfCutoff)
        (finiteSum (scaledPrecisionMajorant TB)
          (halfCutoff ℕ.+ suc halfCutoff))
        (TA Q.· precision halfCutoff) (TB Q.+ TB)
        (finiteSumNonnegative (scaledPrecisionMajorant TB)
          (scaledPrecisionMajorantNonnegative TB 0≤TB)
          (halfCutoff ℕ.+ suc halfCutoff))
        (scaledPrecisionMajorantNonnegative TA 0≤TA halfCutoff)
        (scaledPrecisionTailIntervalBound TA 0≤TA halfCutoff halfCutoff)
        (scaledPrecisionFiniteSumBound TB 0≤TB
          (halfCutoff ℕ.+ suc halfCutoff))))

fourfoldProductCoefficient : Q.ℚ → Q.ℚ → Q.ℚ
fourfoldProductCoefficient TA TB =
  ((TA Q.· TB) Q.+ (TA Q.· TB)) Q.+
    ((TA Q.· TB) Q.+ (TA Q.· TB))

module ScaledResidualPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)

  collect : (TA TB p : fst R) →
    ((TA +S TA) ·S (TB ·S p)) +S ((TA ·S p) ·S (TB +S TB)) ≡
      (((TA ·S TB) +S (TA ·S TB)) +S
        ((TA ·S TB) +S (TA ·S TB))) ·S p
  collect TA TB p = solve! R

scaledPrecisionUpperResidualCollectedBound :
  (TA TB : Q.ℚ) → 0 ≤ TA → 0 ≤ TB → (halfCutoff : ℕ) →
  finiteUpperResidualByRows
    (scaledPrecisionMajorant TA) (scaledPrecisionMajorant TB)
    (halfCutoff ℕ.+ suc halfCutoff) ≤
  fourfoldProductCoefficient TA TB Q.· precision halfCutoff
scaledPrecisionUpperResidualCollectedBound TA TB 0≤TA 0≤TB halfCutoff =
  subst
    (finiteUpperResidualByRows
      (scaledPrecisionMajorant TA) (scaledPrecisionMajorant TB)
      (halfCutoff ℕ.+ suc halfCutoff) ≤_)
    (ScaledResidualPaths.collect PreferredℚCommRing
      TA TB (precision halfCutoff))
    (scaledPrecisionUpperResidualBound TA TB 0≤TA 0≤TB halfCutoff)

finiteUpperResidualBelowLowPlusHighTail :
  (A B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  (halfCutoff : ℕ) →
  finiteUpperResidualByRows A B (halfCutoff ℕ.+ suc halfCutoff) ≤
    finiteSum
      (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff)) halfCutoff Q.+
    (finiteSumInterval A (suc halfCutoff) halfCutoff Q.·
      finiteSum B (halfCutoff ℕ.+ suc halfCutoff))
finiteUpperResidualBelowLowPlusHighTail A B A≥0 B≥0 halfCutoff =
  subst (_≤
    (finiteSum
      (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff)) halfCutoff Q.+
     (finiteSumInterval A (suc halfCutoff) halfCutoff Q.·
      finiteSum B (halfCutoff ℕ.+ suc halfCutoff))))
    (sym (finiteUpperResidualDyadicPredecessorSplit A B halfCutoff))
    (≤Monotone+
      (finiteSum
        (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff)) halfCutoff)
      (finiteSum
        (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff)) halfCutoff)
      (finiteSumInterval
        (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff))
        (suc halfCutoff) halfCutoff)
      (finiteSumInterval A (suc halfCutoff) halfCutoff Q.·
        finiteSum B (halfCutoff ℕ.+ suc halfCutoff))
      (isRefl≤
        (finiteSum
          (upperResidualRow A B (halfCutoff ℕ.+ suc halfCutoff))
          halfCutoff))
      (finiteUpperHighRowsTailProductBound A B A≥0 B≥0 halfCutoff))

module RowSplitPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_)

  collect : (lower residual nextLower nextResidual : fst R) →
    (lower +S residual) +S (nextLower +S nextResidual) ≡
      (lower +S nextLower) +S (residual +S nextResidual)
  collect lower residual nextLower nextResidual = solve! R

finite-rows-split : (a b : ℕ → Q.ℚ) (cutoff rowEnd : ℕ) →
  ℕOrder._≤_ rowEnd cutoff →
  finiteSum (λ left →
    finiteSum (λ right → a left Q.· b right) cutoff) rowEnd ≡
  finiteSum (λ left →
    finiteSum (λ right → a left Q.· b right) (cutoff ∸ left)) rowEnd Q.+
  finiteSum (upperResidualRow a b cutoff) rowEnd
finite-rows-split a b cutoff zero zero≤cutoff =
  upper-residual-row-split a b cutoff zero zero≤cutoff
finite-rows-split a b cutoff (suc rowEnd) sucRowEnd≤cutoff =
  cong₂ Q._+_
    (finite-rows-split a b cutoff rowEnd
      (ℕOrder.≤-trans ℕOrder.≤-sucℕ sucRowEnd≤cutoff))
    (upper-residual-row-split a b cutoff (suc rowEnd) sucRowEnd≤cutoff) ∙
  RowSplitPaths.collect PreferredℚCommRing
    (finiteSum (λ left →
      finiteSum (λ right → a left Q.· b right) (cutoff ∸ left)) rowEnd)
    (finiteSum (upperResidualRow a b cutoff) rowEnd)
    (finiteSum (λ right → a (suc rowEnd) Q.· b right)
      (cutoff ∸ suc rowEnd))
    (upperResidualRow a b cutoff (suc rowEnd))

finiteLowerTriangleByRows :
  (ℕ → Q.ℚ) → (ℕ → Q.ℚ) → ℕ → Q.ℚ
finiteLowerTriangleByRows a b cutoff =
  finiteSum (λ left →
    finiteSum (λ right → a left Q.· b right) (cutoff ∸ left)) cutoff

lowerTriangularRowNonnegative :
  (A B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  (cutoff left : ℕ) → 0 ≤ lowerTriangularRow A B cutoff left
lowerTriangularRowNonnegative A B A≥0 B≥0 cutoff left =
  finiteSumNonnegative (λ right → A left Q.· B right)
    (λ right → nonnegative-bound-product
      (A left) (B right) (A≥0 left) (B≥0 right))
    (cutoff ℕ.∸ left)

finiteLowerTriangleByRowsNonnegative :
  (A B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  (cutoff : ℕ) → 0 ≤ finiteLowerTriangleByRows A B cutoff
finiteLowerTriangleByRowsNonnegative A B A≥0 B≥0 cutoff =
  finiteSumNonnegative (lowerTriangularRow A B cutoff)
    (lowerTriangularRowNonnegative A B A≥0 B≥0 cutoff) cutoff

finite-lower-triangle-by-rows-is-diagonal :
  (a b : ℕ → Q.ℚ) (cutoff : ℕ) →
  finiteLowerTriangleByRows a b cutoff ≡
    finiteTriangularCauchyProduct a b cutoff
finite-lower-triangle-by-rows-is-diagonal a b cutoff =
  finite-triangle-by-rows-is-diagonal
    (λ left right → a left Q.· b right) cutoff

finite-rectangle-splits-into-lower-and-upper-rows :
  (a b : ℕ → Q.ℚ) (cutoff : ℕ) →
  finiteRectangularCauchyProduct a b cutoff cutoff ≡
    finiteLowerTriangleByRows a b cutoff Q.+
      finiteUpperResidualByRows a b cutoff
finite-rectangle-splits-into-lower-and-upper-rows a b cutoff =
  finiteRectangularCauchyProductByRows a b cutoff cutoff ∙
  finite-rows-split a b cutoff cutoff (ℕOrder.≤-refl)

finiteUpperResidualByRowsBelowRectangle :
  (A B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  (cutoff : ℕ) →
  finiteUpperResidualByRows A B cutoff ≤
    finiteRectangularCauchyProduct A B cutoff cutoff
finiteUpperResidualByRowsBelowRectangle A B A≥0 B≥0 cutoff =
  subst (finiteUpperResidualByRows A B cutoff ≤_)
    (Q.+Comm
      (finiteUpperResidualByRows A B cutoff)
      (finiteLowerTriangleByRows A B cutoff) ∙
     sym (finite-rectangle-splits-into-lower-and-upper-rows A B cutoff))
    (≤-add-nonnegative
      (finiteUpperResidualByRows A B cutoff)
      (finiteLowerTriangleByRows A B cutoff)
      (finiteLowerTriangleByRowsNonnegative A B A≥0 B≥0 cutoff))

finite-upper-residual-by-rows-zero : (a b : ℕ → Q.ℚ) →
  finiteUpperResidualByRows a b zero ≡ 0
finite-upper-residual-by-rows-zero a b = refl

finite-upper-residual-by-rows-one : (a b : ℕ → Q.ℚ) →
  finiteUpperResidualByRows a b (suc zero) ≡
  a (suc zero) Q.· b (suc zero)
finite-upper-residual-by-rows-one a b =
  Q.+IdL (a (suc zero) Q.· b (suc zero))

upperResidualRowMagnitudeBound :
  (a A b B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  ((i : ℕ) → MagnitudeBound (a i) (A i)) →
  ((j : ℕ) → MagnitudeBound (b j) (B j)) →
  (cutoff left : ℕ) →
  MagnitudeBound (upperResidualRow a b cutoff left)
    (upperResidualRow A B cutoff left)
upperResidualRowMagnitudeBound a A b B A≥0 B≥0 aBound bBound cutoff zero =
  record { positive-upper = isRefl≤ 0 ; negative-upper = isRefl≤ 0 }
upperResidualRowMagnitudeBound
  a A b B A≥0 B≥0 aBound bBound cutoff (suc leftPredecessor) =
  finiteSumIntervalMagnitudeBound _ _
    (λ right → arbitrary-multiplier-bound
      (a (suc leftPredecessor)) (A (suc leftPredecessor))
      (b right) (B right) (A≥0 (suc leftPredecessor)) (B≥0 right)
      (aBound (suc leftPredecessor)) (bBound right))
    (suc (cutoff ∸ suc leftPredecessor)) leftPredecessor

finiteUpperResidualByRowsMagnitudeBound :
  (a A b B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  ((i : ℕ) → MagnitudeBound (a i) (A i)) →
  ((j : ℕ) → MagnitudeBound (b j) (B j)) →
  (cutoff : ℕ) →
  MagnitudeBound (finiteUpperResidualByRows a b cutoff)
    (finiteUpperResidualByRows A B cutoff)
finiteUpperResidualByRowsMagnitudeBound
  a A b B A≥0 B≥0 aBound bBound cutoff =
  finiteSumMagnitudeBound _ _
    (upperResidualRowMagnitudeBound
      a A b B A≥0 B≥0 aBound bBound cutoff) cutoff

upperRowsComparisonGivesResidualMagnitudeBound :
  (a A b B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  ((i : ℕ) → MagnitudeBound (a i) (A i)) →
  ((j : ℕ) → MagnitudeBound (b j) (B j)) →
  (cutoff : ℕ) →
  finiteTriangularResidual a b cutoff ≡
    finiteUpperResidualByRows a b cutoff →
  MagnitudeBound (finiteTriangularResidual a b cutoff)
    (finiteUpperResidualByRows A B cutoff)
upperRowsComparisonGivesResidualMagnitudeBound
  a A b B A≥0 B≥0 aBound bBound cutoff comparison =
  transport-magnitude _ _ _ comparison
    (finiteUpperResidualByRowsMagnitudeBound
      a A b B A≥0 B≥0 aBound bBound cutoff)

finite-triangular-residual-zero : (a b : ℕ → Q.ℚ) →
  finiteTriangularResidual a b zero ≡ 0
finite-triangular-residual-zero a b =
  cong (Q._+ (Q.- (a zero Q.· b zero)))
    (sym (Q.+IdR (a zero Q.· b zero))) ∙
  ProductSignPaths.cancel-translated PreferredℚCommRing
    (a zero Q.· b zero) 0

module ResidualDifferencePaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
    renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)

  restore-rectangle : (rectangle triangle : fst R) →
    triangle +S (rectangle +S (-S triangle)) ≡ rectangle
  restore-rectangle rectangle triangle = solve! R

  remove-retained-triangle : (triangle residual : fst R) →
    (triangle +S residual) +S (-S triangle) ≡ residual
  remove-retained-triangle triangle residual = solve! R

  degree-one-residual : (a0 a1 b0 b1 : fst R) →
    (a0 ·S (b0 +S b1) +S a1 ·S (b0 +S b1)) +S
      (-S (a0 ·S b0 +S (a0 ·S b1 +S a1 ·S b0))) ≡
    a1 ·S b1
  degree-one-residual a0 a1 b0 b1 = solve! R

  degree-two-residual : (a0 a1 a2 b0 b1 b2 : fst R) →
    ((a0 ·S ((b0 +S b1) +S b2) +S
       a1 ·S ((b0 +S b1) +S b2)) +S
       a2 ·S ((b0 +S b1) +S b2)) +S
      (-S ((a0 ·S b0 +S (a0 ·S b1 +S a1 ·S b0)) +S
        ((a0 ·S b2 +S a1 ·S b1) +S a2 ·S b0))) ≡
    a1 ·S b2 +S ((a2 ·S b1) +S a2 ·S b2)
  degree-two-residual a0 a1 a2 b0 b1 b2 = solve! R

finite-triangular-residual-one : (a b : ℕ → Q.ℚ) →
  finiteTriangularResidual a b (suc zero) ≡
  a (suc zero) Q.· b (suc zero)
finite-triangular-residual-one a b =
  ResidualDifferencePaths.degree-one-residual PreferredℚCommRing
    (a zero) (a (suc zero)) (b zero) (b (suc zero))

finite-residual-is-upper-rows-zero : (a b : ℕ → Q.ℚ) →
  finiteTriangularResidual a b zero ≡ finiteUpperResidualByRows a b zero
finite-residual-is-upper-rows-zero a b =
  finite-triangular-residual-zero a b ∙
  sym (finite-upper-residual-by-rows-zero a b)

finite-residual-is-upper-rows-one : (a b : ℕ → Q.ℚ) →
  finiteTriangularResidual a b (suc zero) ≡
    finiteUpperResidualByRows a b (suc zero)
finite-residual-is-upper-rows-one a b =
  finite-triangular-residual-one a b ∙
  sym (finite-upper-residual-by-rows-one a b)

finite-residual-is-upper-rows-two : (a b : ℕ → Q.ℚ) →
  finiteTriangularResidual a b (suc (suc zero)) ≡
    finiteUpperResidualByRows a b (suc (suc zero))
finite-residual-is-upper-rows-two a b =
  ResidualDifferencePaths.degree-two-residual PreferredℚCommRing
    (a zero) (a 1) (a 2) (b zero) (b 1) (b 2) ∙
  sym (cong (Q._+ ((a 2 Q.· b 1) Q.+ a 2 Q.· b 2))
    (Q.+IdL (a 1 Q.· b 2)))

lower-row-comparison-gives-residual-comparison :
  (a b : ℕ → Q.ℚ) (cutoff : ℕ) →
  finiteLowerTriangleByRows a b cutoff ≡
    finiteTriangularCauchyProduct a b cutoff →
  finiteTriangularResidual a b cutoff ≡
    finiteUpperResidualByRows a b cutoff
lower-row-comparison-gives-residual-comparison a b cutoff lower≡triangle =
  cong (Q._+ (Q.- finiteTriangularCauchyProduct a b cutoff))
    (finite-rectangle-splits-into-lower-and-upper-rows a b cutoff) ∙
  cong (λ lower →
    (lower Q.+ finiteUpperResidualByRows a b cutoff) Q.+
      (Q.- finiteTriangularCauchyProduct a b cutoff))
    lower≡triangle ∙
  ResidualDifferencePaths.remove-retained-triangle PreferredℚCommRing
    (finiteTriangularCauchyProduct a b cutoff)
    (finiteUpperResidualByRows a b cutoff)

finite-residual-is-upper-rows :
  (a b : ℕ → Q.ℚ) (cutoff : ℕ) →
  finiteTriangularResidual a b cutoff ≡
    finiteUpperResidualByRows a b cutoff
finite-residual-is-upper-rows a b cutoff =
  lower-row-comparison-gives-residual-comparison a b cutoff
    (finite-lower-triangle-by-rows-is-diagonal a b cutoff)

finite-triangular-residual-sharp-magnitude-bound :
  (a A b B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  ((i : ℕ) → MagnitudeBound (a i) (A i)) →
  ((j : ℕ) → MagnitudeBound (b j) (B j)) →
  (cutoff : ℕ) →
  MagnitudeBound (finiteTriangularResidual a b cutoff)
    (finiteUpperResidualByRows A B cutoff)
finite-triangular-residual-sharp-magnitude-bound
  a A b B A≥0 B≥0 aBound bBound cutoff =
  upperRowsComparisonGivesResidualMagnitudeBound
    a A b B A≥0 B≥0 aBound bBound cutoff
    (finite-residual-is-upper-rows a b cutoff)

finite-rectangle-decomposes-into-triangle-and-residual :
  (a b : ℕ → Q.ℚ) (cutoff : ℕ) →
  finiteRectangularCauchyProduct a b cutoff cutoff ≡
  finiteTriangularCauchyProduct a b cutoff Q.+
    finiteTriangularResidual a b cutoff
finite-rectangle-decomposes-into-triangle-and-residual a b cutoff =
  sym (ResidualDifferencePaths.restore-rectangle PreferredℚCommRing
    (finiteRectangularCauchyProduct a b cutoff cutoff)
    (finiteTriangularCauchyProduct a b cutoff))

finite-product-minus-triangle-is-residual :
  (a b : ℕ → Q.ℚ) (cutoff : ℕ) →
  (finiteSum a cutoff Q.· finiteSum b cutoff) Q.+
    (Q.- finiteTriangularCauchyProduct a b cutoff) ≡
  finiteTriangularResidual a b cutoff
finite-product-minus-triangle-is-residual a b cutoff =
  cong (Q._+ (Q.- finiteTriangularCauchyProduct a b cutoff))
    (finite-sum-product-is-rectangular-cauchy-product a b cutoff cutoff)

rectangular-decomposition-gives-product-difference-bound :
  (a b : ℕ → Q.ℚ) (leftCutoff rightCutoff : ℕ) →
  (triangle residual bound : Q.ℚ) →
  finiteRectangularCauchyProduct a b leftCutoff rightCutoff ≡
    triangle Q.+ residual →
  MagnitudeBound residual bound →
  MagnitudeBound
    ((finiteSum a leftCutoff Q.· finiteSum b rightCutoff) Q.+
      (Q.- triangle))
    bound
rectangular-decomposition-gives-product-difference-bound
  a b leftCutoff rightCutoff triangle residual bound decomposition residualBound =
  transport-magnitude _ residual bound differencePath residualBound
  where
  differencePath :
    (finiteSum a leftCutoff Q.· finiteSum b rightCutoff) Q.+
      (Q.- triangle) ≡ residual
  differencePath =
    cong (Q._+ (Q.- triangle))
      (finite-sum-product-is-rectangular-cauchy-product
        a b leftCutoff rightCutoff ∙ decomposition) ∙
    ResidualDifferencePaths.remove-retained-triangle
      PreferredℚCommRing triangle residual

finiteRectangularMagnitudeBound :
  (a A b B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  ((i : ℕ) → MagnitudeBound (a i) (A i)) →
  ((j : ℕ) → MagnitudeBound (b j) (B j)) →
  (leftCutoff rightCutoff : ℕ) →
  MagnitudeBound
    (finiteRectangularCauchyProduct a b leftCutoff rightCutoff)
    (finiteRectangularCauchyProduct A B leftCutoff rightCutoff)
finiteProductOfSumsMagnitudeBound :
  (a A b B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  ((i : ℕ) → MagnitudeBound (a i) (A i)) →
  ((j : ℕ) → MagnitudeBound (b j) (B j)) →
  (leftCutoff rightCutoff : ℕ) →
  MagnitudeBound
    (finiteSum a leftCutoff Q.· finiteSum b rightCutoff)
    (finiteSum A leftCutoff Q.· finiteSum B rightCutoff)
finiteProductOfSumsMagnitudeBound a A b B A≥0 B≥0 aBound bBound
  leftCutoff rightCutoff =
  transport-magnitude _ _ _
    (finite-sum-product-is-rectangular-cauchy-product
      a b leftCutoff rightCutoff)
    (subst
      (MagnitudeBound
        (finiteRectangularCauchyProduct a b leftCutoff rightCutoff))
      (sym (finite-sum-product-is-rectangular-cauchy-product
        A B leftCutoff rightCutoff))
      (finiteRectangularMagnitudeBound
        a A b B A≥0 B≥0 aBound bBound leftCutoff rightCutoff))

finiteTriangularResidualCoarseMagnitudeBound :
  (a A b B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  ((i : ℕ) → MagnitudeBound (a i) (A i)) →
  ((j : ℕ) → MagnitudeBound (b j) (B j)) →
  (cutoff : ℕ) (triangleBound : Q.ℚ) →
  MagnitudeBound (finiteTriangularCauchyProduct a b cutoff)
    triangleBound →
  MagnitudeBound
    (finiteTriangularResidual a b cutoff)
    (finiteRectangularCauchyProduct A B cutoff cutoff Q.+
      triangleBound)
finiteTriangularResidualCoarseMagnitudeBound
  a A b B A≥0 B≥0 aBound bBound cutoff triangleBound triangleMagnitude =
  add-magnitude-bounds _ _ _ _
    (finiteRectangularMagnitudeBound
      a A b B A≥0 B≥0 aBound bBound cutoff cutoff)
    (negate-magnitude-bound _ _ triangleMagnitude)

finiteTriangularResidualMajorantBound :
  (a A b B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  ((i : ℕ) → MagnitudeBound (a i) (A i)) →
  ((j : ℕ) → MagnitudeBound (b j) (B j)) →
  (cutoff : ℕ) →
  MagnitudeBound
    (finiteTriangularResidual a b cutoff)
    (finiteRectangularCauchyProduct A B cutoff cutoff Q.+
      finiteTriangularCauchyProduct A B cutoff)
finiteTriangularResidualMajorantBound
  a A b B A≥0 B≥0 aBound bBound cutoff =
  finiteTriangularResidualCoarseMagnitudeBound
    a A b B A≥0 B≥0 aBound bBound cutoff
    (finiteTriangularCauchyProduct A B cutoff)
    (finiteTriangularCauchyProductMagnitudeBound
      a A b B A≥0 B≥0 aBound bBound cutoff)

weakenMagnitudeBound : (value small large : Q.ℚ) →
  MagnitudeBound value small → small ≤ large → MagnitudeBound value large
weakenMagnitudeBound value small large bound small≤large .positive-upper =
  isTrans≤ value small large (positive-upper bound) small≤large
weakenMagnitudeBound value small large bound small≤large .negative-upper =
  isTrans≤ (Q.- value) small large (negative-upper bound) small≤large

scaledCoefficientAbsorption : (coefficient : Q.ℚ) (exponent n : ℕ) →
  coefficient ≤ dyadicRadius exponent →
  coefficient Q.· precision (exponent ℕ.+ n) ≤ precision n
scaledCoefficientAbsorption coefficient exponent n coefficient≤radius =
  subst (coefficient Q.· precision (exponent ℕ.+ n) ≤_)
    (radius-cancels-precision-shift exponent n)
    (nonnegativeProductMonotone
      coefficient (precision (exponent ℕ.+ n))
      (dyadicRadius exponent) (precision (exponent ℕ.+ n))
      (precision-nonnegative (exponent ℕ.+ n))
      (dyadicRadius-nonnegative exponent)
      coefficient≤radius (isRefl≤ (precision (exponent ℕ.+ n))))

scaledPrecisionTriangularResidualMagnitudeBound :
  (a b : ℕ → Q.ℚ) (TA TB : Q.ℚ) →
  0 ≤ TA → 0 ≤ TB →
  ((i : ℕ) → MagnitudeBound (a i) (scaledPrecisionMajorant TA i)) →
  ((j : ℕ) → MagnitudeBound (b j) (scaledPrecisionMajorant TB j)) →
  (halfCutoff : ℕ) →
  MagnitudeBound
    (finiteTriangularResidual a b (halfCutoff ℕ.+ suc halfCutoff))
    (fourfoldProductCoefficient TA TB Q.· precision halfCutoff)
scaledPrecisionTriangularResidualMagnitudeBound
  a b TA TB 0≤TA 0≤TB aBound bBound halfCutoff =
  weakenMagnitudeBound _ _ _
    (finite-triangular-residual-sharp-magnitude-bound
      a (scaledPrecisionMajorant TA) b (scaledPrecisionMajorant TB)
      (scaledPrecisionMajorantNonnegative TA 0≤TA)
      (scaledPrecisionMajorantNonnegative TB 0≤TB)
      aBound bBound (halfCutoff ℕ.+ suc halfCutoff))
    (scaledPrecisionUpperResidualCollectedBound
      TA TB 0≤TA 0≤TB halfCutoff)

absorbedScaledPrecisionTriangularResidualBound :
  (a b : ℕ → Q.ℚ) (TA TB : Q.ℚ) →
  0 ≤ TA → 0 ≤ TB →
  ((i : ℕ) → MagnitudeBound (a i) (scaledPrecisionMajorant TA i)) →
  ((j : ℕ) → MagnitudeBound (b j) (scaledPrecisionMajorant TB j)) →
  (absorptionExponent : ℕ) →
  fourfoldProductCoefficient TA TB ≤ dyadicRadius absorptionExponent →
  (n : ℕ) →
  MagnitudeBound
    (finiteTriangularResidual a b
      ((absorptionExponent ℕ.+ n) ℕ.+ suc (absorptionExponent ℕ.+ n)))
    (precision n)
absorbedScaledPrecisionTriangularResidualBound
  a b TA TB 0≤TA 0≤TB aBound bBound absorptionExponent
  coefficientBound n =
  weakenMagnitudeBound _ _ (precision n)
    (scaledPrecisionTriangularResidualMagnitudeBound
      a b TA TB 0≤TA 0≤TB aBound bBound (absorptionExponent ℕ.+ n))
    (scaledCoefficientAbsorption
      (fourfoldProductCoefficient TA TB) absorptionExponent n coefficientBound)

absorbedResidualCutoff : ℕ → ℕ → ℕ
absorbedResidualCutoff absorptionExponent n =
  (absorptionExponent ℕ.+ n) ℕ.+ suc (absorptionExponent ℕ.+ n)

absorbedFiniteProductDifferenceMagnitudeBound :
  (a b : ℕ → Q.ℚ) (TA TB : Q.ℚ) →
  0 ≤ TA → 0 ≤ TB →
  ((i : ℕ) → MagnitudeBound (a i) (scaledPrecisionMajorant TA i)) →
  ((j : ℕ) → MagnitudeBound (b j) (scaledPrecisionMajorant TB j)) →
  (absorptionExponent : ℕ) →
  fourfoldProductCoefficient TA TB ≤ dyadicRadius absorptionExponent →
  (n : ℕ) →
  MagnitudeBound
    ((finiteSum a (absorbedResidualCutoff absorptionExponent n) Q.·
      finiteSum b (absorbedResidualCutoff absorptionExponent n)) Q.+
     (Q.- finiteTriangularCauchyProduct a b
      (absorbedResidualCutoff absorptionExponent n)))
    (precision n)
absorbedFiniteProductDifferenceMagnitudeBound
  a b TA TB 0≤TA 0≤TB aBound bBound absorptionExponent
  coefficientBound n =
  transport-magnitude _ _ (precision n)
    (finite-product-minus-triangle-is-residual
      a b (absorbedResidualCutoff absorptionExponent n))
    (absorbedScaledPrecisionTriangularResidualBound
      a b TA TB 0≤TA 0≤TB aBound bBound absorptionExponent
      coefficientBound n)

absorbedExponentialProductSumDifferenceMagnitudeBound :
  (x y TA TB : Q.ℚ) → 0 ≤ TA → 0 ≤ TB →
  ((i : ℕ) → MagnitudeBound
    (exponentialTerm x i) (scaledPrecisionMajorant TA i)) →
  ((j : ℕ) → MagnitudeBound
    (exponentialTerm y j) (scaledPrecisionMajorant TB j)) →
  (absorptionExponent : ℕ) →
  fourfoldProductCoefficient TA TB ≤ dyadicRadius absorptionExponent →
  (n : ℕ) →
  MagnitudeBound
    ((finiteSum (exponentialTerm x)
        (absorbedResidualCutoff absorptionExponent n) Q.·
      finiteSum (exponentialTerm y)
        (absorbedResidualCutoff absorptionExponent n)) Q.+
     (Q.- finiteSum (exponentialTerm (x Q.+ y))
        (absorbedResidualCutoff absorptionExponent n)))
    (precision n)
absorbedExponentialProductSumDifferenceMagnitudeBound
  x y TA TB 0≤TA 0≤TB xBound yBound absorptionExponent
  coefficientBound n =
  transport-magnitude _ _ (precision n)
    (sym (cong
      (λ triangle →
        (finiteSum (exponentialTerm x) cutoff Q.·
         finiteSum (exponentialTerm y) cutoff) Q.+ Q.- triangle)
      (finite-triangular-exponential-product x y cutoff)))
    (absorbedFiniteProductDifferenceMagnitudeBound
      (exponentialTerm x) (exponentialTerm y) TA TB
      0≤TA 0≤TB xBound yBound absorptionExponent coefficientBound n)
  where
  cutoff = absorbedResidualCutoff absorptionExponent n

record ExponentialGlobalMajorant (q : Q.ℚ) : Type where
  field
    globalScale : Q.ℚ
    globalScaleNonnegative : 0 ≤ globalScale
    globalTermBound : (index : ℕ) →
      MagnitudeBound (exponentialTerm q index)
        (scaledPrecisionMajorant globalScale index)
open ExponentialGlobalMajorant public

dyadicExpandedScaleAtBase : (scaleExponent base : ℕ) →
  dyadicRadius (scaleExponent ℕ.+ base) Q.· precision base ≡
    dyadicRadius scaleExponent
dyadicExpandedScaleAtBase scaleExponent base =
  cong (Q._· precision base) (dyadicRadius-add scaleExponent base) ∙
  sym (Q.·Assoc (dyadicRadius scaleExponent)
    (dyadicRadius base) (precision base)) ∙
  cong (dyadicRadius scaleExponent Q.·_)
    (dyadicRadius-times-precision base) ∙
  Q.·IdR (dyadicRadius scaleExponent)

dyadicExpandedScaleDominatesEarlyRadius :
  (scaleExponent base index : ℕ) →
  ℕOrder._≤_ index base →
  dyadicRadius scaleExponent ≤
    dyadicRadius (scaleExponent ℕ.+ base) Q.· precision index
dyadicExpandedScaleDominatesEarlyRadius scaleExponent base index index≤base =
  subst (_≤ dyadicRadius (scaleExponent ℕ.+ base) Q.· precision index)
    (dyadicExpandedScaleAtBase scaleExponent base)
    (left-multiply-monotone
      (dyadicRadius (scaleExponent ℕ.+ base))
      (precision base) (precision index)
      (dyadicRadius-nonnegative (scaleExponent ℕ.+ base))
      (precision-antitone index base index≤base))

record ExponentialGlobalMajorantData (q : Q.ℚ) : Type where
  field
    tailSeed : ExponentialTailSeed q
    majorantScale : Q.ℚ
    majorantScaleNonnegative : 0 ≤ majorantScale
    earlyTermBound : (index : ℕ) →
      ℕOrder._<_ index (baseTaylorCutoff tailSeed) →
      MagnitudeBound (exponentialTerm q index)
        (scaledPrecisionMajorant majorantScale index)
    tailScaleCompatibility :
      dyadicRadius (seedExponent tailSeed) ≤
        majorantScale Q.· precision (baseTaylorCutoff tailSeed)
open ExponentialGlobalMajorantData public

finitePrefixMaximum : (ℕ → ℕ) → ℕ → ℕ
finitePrefixMaximum values zero = values zero
finitePrefixMaximum values (suc cutoff) =
  ℕ.max (finitePrefixMaximum values cutoff) (values (suc cutoff))

finitePrefixMaximumDominates : (values : ℕ → ℕ) (cutoff index : ℕ) →
  ℕOrder._≤_ index cutoff →
  ℕOrder._≤_ (values index) (finitePrefixMaximum values cutoff)
finitePrefixMaximumDominates values zero zero index≤cutoff = ℕOrder.≤-refl
finitePrefixMaximumDominates values zero (suc index) index≤cutoff =
  ⊥.rec (ℕOrder.¬-<-zero index≤cutoff)
finitePrefixMaximumDominates values (suc cutoff) index index≤cutoff
  with ℕOrder.≤-split index≤cutoff
... | inl index<successor =
  ℕOrder.≤-trans
    (finitePrefixMaximumDominates values cutoff index
      (ℕOrder.pred-≤-pred index<successor))
    ℕOrder.left-≤-max
... | inr indexPath =
  subst (λ selected →
    ℕOrder._≤_ (values selected)
      (finitePrefixMaximum values (suc cutoff)))
    (sym indexPath) ℕOrder.right-≤-max

signedArchimedeanExponentsGiveMagnitudeBound : (q : Q.ℚ) →
  (positive : ArchimedeanExponent q) →
  (negative : ArchimedeanExponent (Q.- q)) →
  MagnitudeBound q
    (dyadicRadius (ℕ.max (exponent positive) (exponent negative)))
signedArchimedeanExponentsGiveMagnitudeBound q positive negative = record
  { positive-upper =
      isTrans≤ q (dyadicRadius (exponent positive))
        (dyadicRadius (ℕ.max (exponent positive) (exponent negative)))
        (dominates positive)
        (dyadicRadius-monotone
          (exponent positive)
          (ℕ.max (exponent positive) (exponent negative))
          ℕOrder.left-≤-max)
  ; negative-upper =
      isTrans≤ (Q.- q) (dyadicRadius (exponent negative))
        (dyadicRadius (ℕ.max (exponent positive) (exponent negative)))
        (dominates negative)
        (dyadicRadius-monotone
          (exponent negative)
          (ℕ.max (exponent positive) (exponent negative))
          ℕOrder.right-≤-max)
  }

record SignedArchimedeanFamily (term : ℕ → Q.ℚ) : Type where
  field
    positiveExponent : (index : ℕ) → ArchimedeanExponent (term index)
    negativeExponent : (index : ℕ) → ArchimedeanExponent (Q.- term index)
open SignedArchimedeanFamily public

naturalCeilingPrincipleGivesSignedArchimedeanFamily :
  RationalNaturalCeilingPrinciple →
  (term : ℕ → Q.ℚ) → SignedArchimedeanFamily term
naturalCeilingPrincipleGivesSignedArchimedeanFamily principle term
  .positiveExponent index =
  natural-ceiling-gives-exponent (term index) (ceiling principle (term index))
naturalCeilingPrincipleGivesSignedArchimedeanFamily principle term
  .negativeExponent index =
  natural-ceiling-gives-exponent (Q.- term index)
    (ceiling principle (Q.- term index))

signedMagnitudeExponent : {term : ℕ → Q.ℚ} →
  SignedArchimedeanFamily term → ℕ → ℕ
signedMagnitudeExponent witnesses index =
  ℕ.max (exponent (positiveExponent witnesses index))
    (exponent (negativeExponent witnesses index))

finitePrefixSignedMagnitudeBound : (term : ℕ → Q.ℚ) →
  (witnesses : SignedArchimedeanFamily term) →
  (cutoff index : ℕ) → ℕOrder._≤_ index cutoff →
  MagnitudeBound (term index)
    (dyadicRadius (finitePrefixMaximum
      (signedMagnitudeExponent witnesses) cutoff))
finitePrefixSignedMagnitudeBound term witnesses cutoff index index≤cutoff =
  weakenMagnitudeBound _ _ _
    (signedArchimedeanExponentsGiveMagnitudeBound (term index)
      (positiveExponent witnesses index) (negativeExponent witnesses index))
    (dyadicRadius-monotone _ _
      (finitePrefixMaximumDominates
        (signedMagnitudeExponent witnesses) cutoff index index≤cutoff))

record ExponentialUniformEarlyRadiusData (q : Q.ℚ) : Type where
  field
    uniformTailSeed : ExponentialTailSeed q
    uniformRadiusExponent : ℕ
    uniformEarlyBound : (index : ℕ) →
      ℕOrder._<_ index (baseTaylorCutoff uniformTailSeed) →
      MagnitudeBound (exponentialTerm q index)
        (dyadicRadius uniformRadiusExponent)
    uniformTailBound :
      dyadicRadius (seedExponent uniformTailSeed) ≤
        dyadicRadius uniformRadiusExponent
open ExponentialUniformEarlyRadiusData public

tailSeedAndSignedTermsGiveUniformEarlyRadiusData : (q : Q.ℚ) →
  (seed : ExponentialTailSeed q) →
  SignedArchimedeanFamily (exponentialTerm q) →
  ExponentialUniformEarlyRadiusData q
tailSeedAndSignedTermsGiveUniformEarlyRadiusData q seed witnesses =
  record
    { uniformTailSeed = seed
    ; uniformRadiusExponent = ℕ.max prefixExponent (seedExponent seed)
    ; uniformEarlyBound = λ index index<base →
        weakenMagnitudeBound _ _ _
          (finitePrefixSignedMagnitudeBound
            (exponentialTerm q) witnesses base index
            (ℕOrder.<-weaken index<base))
          (dyadicRadius-monotone
            prefixExponent (ℕ.max prefixExponent (seedExponent seed))
            ℕOrder.left-≤-max)
    ; uniformTailBound =
        dyadicRadius-monotone
          (seedExponent seed) (ℕ.max prefixExponent (seedExponent seed))
          ℕOrder.right-≤-max
    }
  where
  base = baseTaylorCutoff seed
  prefixExponent = finitePrefixMaximum
    (signedMagnitudeExponent witnesses) base

uniformEarlyRadiusGivesGlobalMajorantData : (q : Q.ℚ) →
  ExponentialUniformEarlyRadiusData q → ExponentialGlobalMajorantData q
uniformEarlyRadiusGivesGlobalMajorantData q uniform =
  record
    { tailSeed = uniformTailSeed uniform
    ; majorantScale = dyadicRadius
        (uniformRadiusExponent uniform ℕ.+
          baseTaylorCutoff (uniformTailSeed uniform))
    ; majorantScaleNonnegative = dyadicRadius-nonnegative
        (uniformRadiusExponent uniform ℕ.+
          baseTaylorCutoff (uniformTailSeed uniform))
    ; earlyTermBound = λ index index<base →
        weakenMagnitudeBound _ _ _
          (uniformEarlyBound uniform index index<base)
          (dyadicExpandedScaleDominatesEarlyRadius
            (uniformRadiusExponent uniform)
            (baseTaylorCutoff (uniformTailSeed uniform)) index
            (ℕOrder.<-weaken index<base))
    ; tailScaleCompatibility =

        subst
          (dyadicRadius (seedExponent (uniformTailSeed uniform)) ≤_)
          (sym (dyadicExpandedScaleAtBase
            (uniformRadiusExponent uniform)
            (baseTaylorCutoff (uniformTailSeed uniform))))
          (uniformTailBound uniform)
    }

exponentialGlobalMajorantFromData : (q : Q.ℚ) →
  ExponentialGlobalMajorantData q → ExponentialGlobalMajorant q
exponentialGlobalMajorantFromData q datum .globalScale = majorantScale datum
exponentialGlobalMajorantFromData q datum .globalScaleNonnegative =
  majorantScaleNonnegative datum
exponentialGlobalMajorantFromData q datum .globalTermBound index
  with ℕOrder.splitℕ-< index (baseTaylorCutoff (tailSeed datum))
... | inl index<base = earlyTermBound datum index index<base
... | inr (distance , distance+base≡index) =
  weakenMagnitudeBound _ _ _
    (transport-magnitude _ _ _
      (cong (exponentialTerm q)
        (sym (ℕ.+-comm (baseTaylorCutoff (tailSeed datum)) distance ∙
          distance+base≡index)))
      (exponential-tail-bound-before-absorption (tailSeed datum) distance))
    (subst
      (dyadicRadius (seedExponent (tailSeed datum)) Q.· precision distance ≤_)
      (sym (Q.·Assoc (majorantScale datum)
        (precision (baseTaylorCutoff (tailSeed datum))) (precision distance)) ∙
       cong (majorantScale datum Q.·_)
         (sym (precision-add (baseTaylorCutoff (tailSeed datum)) distance)) ∙
       cong (scaledPrecisionMajorant (majorantScale datum))
         (ℕ.+-comm (baseTaylorCutoff (tailSeed datum)) distance ∙
          distance+base≡index))
      (nonnegativeProductMonotone
        (dyadicRadius (seedExponent (tailSeed datum))) (precision distance)
        (majorantScale datum Q.· precision (baseTaylorCutoff (tailSeed datum)))
        (precision distance)
        (precision-nonnegative distance)
        (nonnegative-bound-product (majorantScale datum)
          (precision (baseTaylorCutoff (tailSeed datum)))
          (majorantScaleNonnegative datum)
          (precision-nonnegative (baseTaylorCutoff (tailSeed datum))))
        (tailScaleCompatibility datum) (isRefl≤ (precision distance))))

tailSeedAndCeilingPrincipleGiveGlobalMajorant :
  RationalNaturalCeilingPrinciple → (q : Q.ℚ) →
  ExponentialTailSeed q → ExponentialGlobalMajorant q
tailSeedAndCeilingPrincipleGiveGlobalMajorant principle q seed =
  exponentialGlobalMajorantFromData q
    (uniformEarlyRadiusGivesGlobalMajorantData q
      (tailSeedAndSignedTermsGiveUniformEarlyRadiusData q seed
        (naturalCeilingPrincipleGivesSignedArchimedeanFamily
          principle (exponentialTerm q))))

record ExponentialMultiplicationSeed (x y : Q.ℚ) : Type where
  field
    leftScale : Q.ℚ
    rightScale : Q.ℚ
    leftScaleNonnegative : 0 ≤ leftScale
    rightScaleNonnegative : 0 ≤ rightScale
    leftTermBound : (i : ℕ) → MagnitudeBound
      (exponentialTerm x i) (scaledPrecisionMajorant leftScale i)
    rightTermBound : (j : ℕ) → MagnitudeBound
      (exponentialTerm y j) (scaledPrecisionMajorant rightScale j)
    absorptionExponent : ℕ
    coefficientBound :
      fourfoldProductCoefficient leftScale rightScale ≤
        dyadicRadius absorptionExponent
open ExponentialMultiplicationSeed public

globalMajorantsGiveMultiplicationSeed : (x y : Q.ℚ) →
  (xMajorant : ExponentialGlobalMajorant x) →
  (yMajorant : ExponentialGlobalMajorant y) →
  ArchimedeanExponent
    (fourfoldProductCoefficient
      (globalScale xMajorant) (globalScale yMajorant)) →
  ExponentialMultiplicationSeed x y
globalMajorantsGiveMultiplicationSeed x y xMajorant yMajorant coefficientWitness =
  record
    { leftScale = globalScale xMajorant
    ; rightScale = globalScale yMajorant
    ; leftScaleNonnegative = globalScaleNonnegative xMajorant
    ; rightScaleNonnegative = globalScaleNonnegative yMajorant
    ; leftTermBound = globalTermBound xMajorant
    ; rightTermBound = globalTermBound yMajorant
    ; absorptionExponent = exponent coefficientWitness
    ; coefficientBound = dominates coefficientWitness
    }

globalMajorantsAndCoefficientCeilingGiveMultiplicationSeed :
  (x y : Q.ℚ) →
  (xMajorant : ExponentialGlobalMajorant x) →
  (yMajorant : ExponentialGlobalMajorant y) →
  NaturalCeiling
    (fourfoldProductCoefficient
      (globalScale xMajorant) (globalScale yMajorant)) →
  ExponentialMultiplicationSeed x y
globalMajorantsAndCoefficientCeilingGiveMultiplicationSeed
  x y xMajorant yMajorant coefficientCeiling =
  globalMajorantsGiveMultiplicationSeed x y xMajorant yMajorant
    (natural-ceiling-gives-exponent _ coefficientCeiling)

tailSeedsAndCeilingPrincipleGiveMultiplicationSeed :
  RationalNaturalCeilingPrinciple → (x y : Q.ℚ) →
  ExponentialTailSeed x → ExponentialTailSeed y →
  ExponentialMultiplicationSeed x y
tailSeedsAndCeilingPrincipleGiveMultiplicationSeed principle x y xSeed ySeed =
  globalMajorantsAndCoefficientCeilingGiveMultiplicationSeed
    x y xMajorant yMajorant
    (ceiling principle
      (fourfoldProductCoefficient
        (globalScale xMajorant) (globalScale yMajorant)))
  where
  xMajorant = tailSeedAndCeilingPrincipleGiveGlobalMajorant principle x xSeed
  yMajorant = tailSeedAndCeilingPrincipleGiveGlobalMajorant principle y ySeed

seededExponentialComparisonCutoff : {x y : Q.ℚ} →
  ExponentialMultiplicationSeed x y → ℕ → ℕ
seededExponentialComparisonCutoff seed =
  absorbedResidualCutoff (absorptionExponent seed)

seededExponentialProductSumDifferenceMagnitudeBound :
  {x y : Q.ℚ} (seed : ExponentialMultiplicationSeed x y) (n : ℕ) →
  let cutoff = seededExponentialComparisonCutoff seed n
  in MagnitudeBound
    ((finiteSum (exponentialTerm x) cutoff Q.·
      finiteSum (exponentialTerm y) cutoff) Q.+
     (Q.- finiteSum (exponentialTerm (x Q.+ y)) cutoff))
    (precision n)
seededExponentialProductSumDifferenceMagnitudeBound seed n =
  absorbedExponentialProductSumDifferenceMagnitudeBound
    _ _ (leftScale seed) (rightScale seed)
    (leftScaleNonnegative seed) (rightScaleNonnegative seed)
    (leftTermBound seed) (rightTermBound seed)
    (absorptionExponent seed) (coefficientBound seed) n

absorbedScheduleBase : {q : Q.ℚ} → ExponentialTailSeed q → ℕ
absorbedScheduleBase seed =
  baseTaylorCutoff seed ℕ.+ seedExponent seed

module AlignmentIndexPaths where
  absorbed-offset : (base offset extra : ℕ) →
    base ℕ.+ (offset ℕ.+ extra) ≡ (offset ℕ.+ base) ℕ.+ extra
  absorbed-offset base offset extra =
    ℕ.+-assoc base offset extra ∙
    cong (ℕ._+ extra) (ℕ.+-comm base offset)

commonAlignmentShift : ℕ → ℕ → ℕ → ℕ
commonAlignmentShift leftBase rightBase sumBase =
  ℕ.max leftBase (ℕ.max rightBase sumBase)

commonAlignedResidualCutoff : ℕ → ℕ → ℕ → ℕ → ℕ
commonAlignedResidualCutoff absorptionExponent leftBase rightBase sumBase =
  absorbedResidualCutoff absorptionExponent
    (commonAlignmentShift leftBase rightBase sumBase)

alignmentShift≤commonCutoff :
  (absorptionExponent leftBase rightBase sumBase : ℕ) →
  ℕOrder._≤_
    (commonAlignmentShift leftBase rightBase sumBase)
    (commonAlignedResidualCutoff
      absorptionExponent leftBase rightBase sumBase)
alignmentShift≤commonCutoff absorptionExponent leftBase rightBase sumBase =
  ℕOrder.≤-trans
    (absorptionExponent , refl)
    (suc (absorptionExponent ℕ.+ alignment) ,
      ℕ.+-comm (suc (absorptionExponent ℕ.+ alignment))
        (absorptionExponent ℕ.+ alignment))
  where
  alignment = commonAlignmentShift leftBase rightBase sumBase

leftBase≤commonAlignedResidualCutoff :
  (absorptionExponent leftBase rightBase sumBase : ℕ) →
  ℕOrder._≤_ leftBase
    (commonAlignedResidualCutoff
      absorptionExponent leftBase rightBase sumBase)
leftBase≤commonAlignedResidualCutoff absorptionExponent leftBase rightBase sumBase =
  ℕOrder.≤-trans ℕOrder.left-≤-max
    (alignmentShift≤commonCutoff
      absorptionExponent leftBase rightBase sumBase)

rightBase≤commonAlignedResidualCutoff :
  (absorptionExponent leftBase rightBase sumBase : ℕ) →
  ℕOrder._≤_ rightBase
    (commonAlignedResidualCutoff
      absorptionExponent leftBase rightBase sumBase)
rightBase≤commonAlignedResidualCutoff absorptionExponent leftBase rightBase sumBase =
  ℕOrder.≤-trans rightBase≤alignment
    (alignmentShift≤commonCutoff
      absorptionExponent leftBase rightBase sumBase)
  where
  rightBase≤inner : ℕOrder._≤_ rightBase (ℕ.max rightBase sumBase)
  rightBase≤inner =
    ℕOrder.left-≤-max {m = rightBase} {n = sumBase}
  inner≤alignment : ℕOrder._≤_ (ℕ.max rightBase sumBase)
    (commonAlignmentShift leftBase rightBase sumBase)
  inner≤alignment =
    ℕOrder.right-≤-max
      {n = ℕ.max rightBase sumBase} {m = leftBase}
  rightBase≤alignment = ℕOrder.≤-trans rightBase≤inner inner≤alignment

sumBase≤commonAlignedResidualCutoff :
  (absorptionExponent leftBase rightBase sumBase : ℕ) →
  ℕOrder._≤_ sumBase
    (commonAlignedResidualCutoff
      absorptionExponent leftBase rightBase sumBase)
sumBase≤commonAlignedResidualCutoff absorptionExponent leftBase rightBase sumBase =
  ℕOrder.≤-trans sumBase≤alignment
    (alignmentShift≤commonCutoff
      absorptionExponent leftBase rightBase sumBase)
  where
  sumBase≤inner : ℕOrder._≤_ sumBase (ℕ.max rightBase sumBase)
  sumBase≤inner =
    ℕOrder.right-≤-max {n = sumBase} {m = rightBase}
  inner≤alignment : ℕOrder._≤_ (ℕ.max rightBase sumBase)
    (commonAlignmentShift leftBase rightBase sumBase)
  inner≤alignment =
    ℕOrder.right-≤-max
      {n = ℕ.max rightBase sumBase} {m = leftBase}
  sumBase≤alignment = ℕOrder.≤-trans sumBase≤inner inner≤alignment

alignedResidualCutoffShiftPath :
  (absorptionExponent alignment shift n : ℕ) →
  absorbedResidualCutoff absorptionExponent alignment ℕ.+
    ((shift ℕ.+ n) ℕ.+ (shift ℕ.+ n)) ≡
  absorbedResidualCutoff absorptionExponent
    (alignment ℕ.+ (shift ℕ.+ n))
alignedResidualCutoffShiftPath absorptionExponent alignment shift n = solveNat!

doubleIndexRegular : RegularCauchy → RegularCauchy
doubleIndexRegular regular .approximation n =
  approximation regular (n ℕ.+ n)
doubleIndexRegular regular .close-forward m n =
  loosen-two-errors
    (approximation regular (m ℕ.+ m))
    (approximation regular (n ℕ.+ n))
    (precision (m ℕ.+ m)) (precision (n ℕ.+ n))
    (precision m) (precision n)
    (precision-antitone m (m ℕ.+ m) (m , refl))
    (precision-antitone n (n ℕ.+ n) (n , refl))
    (close-forward regular (m ℕ.+ m) (n ℕ.+ n))
doubleIndexRegular regular .close-backward m n =
  loosen-two-errors
    (approximation regular (n ℕ.+ n))
    (approximation regular (m ℕ.+ m))
    (precision (m ℕ.+ m)) (precision (n ℕ.+ n))
    (precision m) (precision n)
    (precision-antitone m (m ℕ.+ m) (m , refl))
    (precision-antitone n (n ℕ.+ n) (n , refl))
    (close-backward regular (m ℕ.+ m) (n ℕ.+ n))

doubleIndexRegularEquivalent : (r : RegularCauchy) →
  doubleIndexRegular r ≈metric r
doubleIndexRegularEquivalent r k =
  ∣ (suc k , λ n sk≤n →
    tighten-two-errors (approximation r (n ℕ.+ n)) (approximation r n)
      (precision n) (precision (n ℕ.+ n)) (precision k)
      (errors n sk≤n) (close-backward r n (n ℕ.+ n)) ,
    tighten-two-errors (approximation r n) (approximation r (n ℕ.+ n))
      (precision n) (precision (n ℕ.+ n)) (precision k)
      (errors n sk≤n) (close-forward r n (n ℕ.+ n))) ∣₁
  where
  errors : (n : ℕ) → ℕOrder._≤_ (suc k) n →
    precision n Q.+ precision (n ℕ.+ n) ≤ precision k
  errors n sk≤n = subst (precision n Q.+ precision (n ℕ.+ n) ≤_)
    (precision-refines-double k)
    (≤Monotone+ (precision n) (precision (suc k))
      (precision (n ℕ.+ n)) (precision (suc k))
      (precision-antitone (suc k) n sk≤n)
      (precision-antitone (suc k) (n ℕ.+ n)
        (ℕOrder.≤-trans sk≤n (n , refl))))

alignedAbsorbedExponentialRegular : {q : Q.ℚ} →
  (seed : ExponentialTailSeed q) (commonBase : ℕ) →
  ℕOrder._≤_ (absorbedScheduleBase seed) commonBase →
  RegularCauchy
alignedAbsorbedExponentialRegular seed commonBase base≤common =
  doubleIndexRegular
    (iterateShift (fst base≤common) (absorbedExponentialRegular seed))

alignedAbsorbedExponentialEquivalent : {q : Q.ℚ} →
  (seed : ExponentialTailSeed q) (commonBase : ℕ) →
  (dominance : ℕOrder._≤_ (absorbedScheduleBase seed) commonBase) →
  alignedAbsorbedExponentialRegular seed commonBase dominance ≈metric
    absorbedExponentialRegular seed
alignedAbsorbedExponentialEquivalent seed commonBase dominance =
  ≈metric-trans
    (alignedAbsorbedExponentialRegular seed commonBase dominance)
    (iterateShift (fst dominance) (absorbedExponentialRegular seed))
    (absorbedExponentialRegular seed)
    (doubleIndexRegularEquivalent
      (iterateShift (fst dominance) (absorbedExponentialRegular seed)))
    (iterateShift-equivalent (fst dominance) (absorbedExponentialRegular seed))

alignedAbsorbedExponentialApproximation : {q : Q.ℚ} →
  (seed : ExponentialTailSeed q) (commonBase : ℕ) →
  (base≤common : ℕOrder._≤_ (absorbedScheduleBase seed) commonBase) →
  (n : ℕ) →
  approximation
    (alignedAbsorbedExponentialRegular seed commonBase base≤common) n ≡
  absorbedExponentialPartialSum seed
    ((fst base≤common) ℕ.+ (n ℕ.+ n))
alignedAbsorbedExponentialApproximation seed commonBase base≤common n =
  iterateShift-approximation
    (fst base≤common) (n ℕ.+ n) (absorbedExponentialRegular seed)

alignedAbsorbedCutoffPath : {q : Q.ℚ} →
  (seed : ExponentialTailSeed q) (commonBase : ℕ) →
  (base≤common : ℕOrder._≤_ (absorbedScheduleBase seed) commonBase) →
  (n : ℕ) →
  absorbedTaylorCutoff seed ((fst base≤common) ℕ.+ (n ℕ.+ n)) ≡
    commonBase ℕ.+ (n ℕ.+ n)
alignedAbsorbedCutoffPath seed commonBase (offset , offset+base≡common) n =
  ℕ.+-assoc (baseTaylorCutoff seed) (seedExponent seed)
    (offset ℕ.+ (n ℕ.+ n)) ∙
  AlignmentIndexPaths.absorbed-offset
    (absorbedScheduleBase seed) offset (n ℕ.+ n) ∙
  cong (ℕ._+ (n ℕ.+ n)) offset+base≡common

alignedAbsorbedExponentialMagnitudeBound : {q : Q.ℚ} →
  (majorant : ExponentialGlobalMajorant q) →
  (seed : ExponentialTailSeed q) (commonBase : ℕ) →
  (base≤common : ℕOrder._≤_ (absorbedScheduleBase seed) commonBase) →
  (n : ℕ) →
  MagnitudeBound
    (approximation
      (alignedAbsorbedExponentialRegular seed commonBase base≤common) n)
    (globalScale majorant Q.+ globalScale majorant)
alignedAbsorbedExponentialMagnitudeBound majorant seed commonBase
  base≤common n =
  transport-magnitude _ _ _
    (alignedAbsorbedExponentialApproximation seed commonBase base≤common n)
    (weakenMagnitudeBound _ _ _
      (finiteSumMagnitudeBound
        (exponentialTerm _)
        (scaledPrecisionMajorant (globalScale majorant))
        (globalTermBound majorant)
        (absorbedTaylorCutoff seed
          ((fst base≤common) ℕ.+ (n ℕ.+ n))))
      (scaledPrecisionFiniteSumBound
        (globalScale majorant) (globalScaleNonnegative majorant)
        (absorbedTaylorCutoff seed
          ((fst base≤common) ℕ.+ (n ℕ.+ n)))))

module MagnitudeLowerPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)

  left : (a bound : fst R) →
    (-S bound) +S ((-S a) +S a) ≡ -S bound
  left a bound = solve! R

  right : (a bound : fst R) →
    (-S bound) +S (bound +S a) ≡ a
  right a bound = solve! R

negativeUpperGivesLower : (a bound : Q.ℚ) →
  Q.- a ≤ bound → Q.- bound ≤ a
negativeUpperGivesLower a bound negativeUpper =
  subst2 _≤_
    (MagnitudeLowerPaths.left PreferredℚCommRing a bound)
    (MagnitudeLowerPaths.right PreferredℚCommRing a bound)
    (≤-o+ ((Q.- a) Q.+ a) (bound Q.+ a) (Q.- bound)
      (≤-+o (Q.- a) bound a negativeUpper))

alignedAbsorbedExponentialDyadicallyBounded : {q : Q.ℚ} →
  (majorant : ExponentialGlobalMajorant q) →
  (scaleWitness : ArchimedeanExponent
    (globalScale majorant Q.+ globalScale majorant)) →
  (seed : ExponentialTailSeed q) (commonBase : ℕ) →
  (base≤common : ℕOrder._≤_ (absorbedScheduleBase seed) commonBase) →
  DyadicallyBoundedRegularCauchy
alignedAbsorbedExponentialDyadicallyBounded majorant scaleWitness
  seed commonBase base≤common .regular =
  alignedAbsorbedExponentialRegular seed commonBase base≤common
alignedAbsorbedExponentialDyadicallyBounded majorant scaleWitness
  seed commonBase base≤common .radius-exponent = exponent scaleWitness
alignedAbsorbedExponentialDyadicallyBounded majorant scaleWitness
  seed commonBase base≤common .lower-bound n =
  negativeUpperGivesLower approximationAtN targetRadius (negative-upper bounded)
  where
  approximationAtN = approximation
    (alignedAbsorbedExponentialRegular seed commonBase base≤common) n
  targetRadius = dyadicRadius (exponent scaleWitness)
  bounded : MagnitudeBound approximationAtN targetRadius
  bounded = weakenMagnitudeBound approximationAtN
    (globalScale majorant Q.+ globalScale majorant) targetRadius
    (alignedAbsorbedExponentialMagnitudeBound
      majorant seed commonBase base≤common n)
    (dominates scaleWitness)
alignedAbsorbedExponentialDyadicallyBounded majorant scaleWitness
  seed commonBase base≤common .upper-bound n = positive-upper bounded
  where
  approximationAtN = approximation
    (alignedAbsorbedExponentialRegular seed commonBase base≤common) n
  targetRadius = dyadicRadius (exponent scaleWitness)
  bounded : MagnitudeBound approximationAtN targetRadius
  bounded = weakenMagnitudeBound approximationAtN
    (globalScale majorant Q.+ globalScale majorant) targetRadius
    (alignedAbsorbedExponentialMagnitudeBound
      majorant seed commonBase base≤common n)
    (dominates scaleWitness)

shiftedSeededExponentialProductSumDifferenceMagnitudeBound :
  {x y : Q.ℚ} (seed : ExponentialMultiplicationSeed x y) →
  (shift n : ℕ) →
  MagnitudeBound
    ((finiteSum (exponentialTerm x)
        (absorbedResidualCutoff
          (absorptionExponent seed) (shift ℕ.+ n)) Q.·
      finiteSum (exponentialTerm y)
        (absorbedResidualCutoff
          (absorptionExponent seed) (shift ℕ.+ n))) Q.+
     (Q.- finiteSum (exponentialTerm (x Q.+ y))
        (absorbedResidualCutoff
          (absorptionExponent seed) (shift ℕ.+ n))))
    (precision n)
shiftedSeededExponentialProductSumDifferenceMagnitudeBound seed shift n =
  weakenMagnitudeBound _ _ _
    (seededExponentialProductSumDifferenceMagnitudeBound seed (shift ℕ.+ n))
    (precision-antitone n (shift ℕ.+ n) (shift , refl))

pointwisePrecisionDifferenceBoundGivesMetric :
  (left right : RegularCauchy) →
  ((n : ℕ) → MagnitudeBound
    (approximation left n Q.+ (Q.- approximation right n))
    (precision n)) →
  left ≈metric right
pointwisePrecisionDifferenceBoundGivesMetric left right differenceBound k =
  ∣ (k , λ n k≤n →
    let weakened = weakenMagnitudeBound _ _ _ (differenceBound n)
          (precision-antitone k n k≤n)
    in (magnitude-bound-forward
          (approximation left n) (approximation right n) (precision k) weakened ,
        magnitude-bound-backward
          (approximation left n) (approximation right n) (precision k) weakened)) ∣₁

module IdentifiedExponentialProduct
  {x y : Q.ℚ} (seed : ExponentialMultiplicationSeed x y)
  (alignment : ℕ)
  (left right : DyadicallyBoundedRegularCauchy) (sum : RegularCauchy)
  (leftPath : (k : ℕ) → approximation (regular left) k ≡
    finiteSum (exponentialTerm x)
      (absorbedResidualCutoff (absorptionExponent seed) (alignment ℕ.+ k)))
  (rightPath : (k : ℕ) → approximation (regular right) k ≡
    finiteSum (exponentialTerm y)
      (absorbedResidualCutoff (absorptionExponent seed) (alignment ℕ.+ k)))
  (sumPath : (k : ℕ) → approximation sum k ≡
    finiteSum (exponentialTerm (x Q.+ y))
      (absorbedResidualCutoff (absorptionExponent seed) (alignment ℕ.+ k)))
  where

  productDepth : ℕ
  productDepth = suc (radius-exponent left ℕ.+ radius-exponent right)

  shiftedSum : RegularCauchy
  shiftedSum = iterateShift productDepth sum

  pointwiseBound : (n : ℕ) → MagnitudeBound
    (approximation (boundedProductRegular left right) n Q.+
      (Q.- approximation shiftedSum n)) (precision n)
  pointwiseBound n =
    subst (λ value → MagnitudeBound value (precision n))
      (sym differencePath)
      (weakenMagnitudeBound _ _ _
        (seededExponentialProductSumDifferenceMagnitudeBound seed
          (alignment ℕ.+ (productDepth ℕ.+ n)))
        (precision-antitone n (alignment ℕ.+ (productDepth ℕ.+ n))
          ((alignment ℕ.+ productDepth) ,
            sym (ℕ.+-assoc alignment productDepth n))))
    where
    cutoff = absorbedResidualCutoff (absorptionExponent seed)
      (alignment ℕ.+ (productDepth ℕ.+ n))
    differencePath :
      approximation (boundedProductRegular left right) n Q.+
        (Q.- approximation shiftedSum n) ≡
      (finiteSum (exponentialTerm x) cutoff Q.·
        finiteSum (exponentialTerm y) cutoff) Q.+
        (Q.- finiteSum (exponentialTerm (x Q.+ y)) cutoff)
    differencePath = cong₂ (λ a b → a Q.+ (Q.- b))
      (cong₂ Q._·_ (leftPath (productDepth ℕ.+ n))
        (rightPath (productDepth ℕ.+ n)))
      (iterateShift-approximation productDepth n sum ∙
        sumPath (productDepth ℕ.+ n))

  metricComparison : boundedProductRegular left right ≈metric shiftedSum
  metricComparison = pointwisePrecisionDifferenceBoundGivesMetric
    (boundedProductRegular left right) shiftedSum pointwiseBound

module AlignedExponentialProduct
  {x y : Q.ℚ} (seed : ExponentialMultiplicationSeed x y)
  (xTail : ExponentialTailSeed x) (yTail : ExponentialTailSeed y)
  (sumTail : ExponentialTailSeed (x Q.+ y))
  (xRadius : ArchimedeanExponent (leftScale seed Q.+ leftScale seed))
  (yRadius : ArchimedeanExponent (rightScale seed Q.+ rightScale seed))
  where

  xMajorant : ExponentialGlobalMajorant x
  xMajorant = record
    { globalScale = leftScale seed
    ; globalScaleNonnegative = leftScaleNonnegative seed
    ; globalTermBound = leftTermBound seed }

  yMajorant : ExponentialGlobalMajorant y
  yMajorant = record
    { globalScale = rightScale seed
    ; globalScaleNonnegative = rightScaleNonnegative seed
    ; globalTermBound = rightTermBound seed }

  xBase = absorbedScheduleBase xTail
  yBase = absorbedScheduleBase yTail
  sumBase = absorbedScheduleBase sumTail
  alignment = commonAlignmentShift xBase yBase sumBase
  commonBase = commonAlignedResidualCutoff
    (absorptionExponent seed) xBase yBase sumBase

  xDominance = leftBase≤commonAlignedResidualCutoff
    (absorptionExponent seed) xBase yBase sumBase
  yDominance = rightBase≤commonAlignedResidualCutoff
    (absorptionExponent seed) xBase yBase sumBase
  sumDominance = sumBase≤commonAlignedResidualCutoff
    (absorptionExponent seed) xBase yBase sumBase

  leftFactor = alignedAbsorbedExponentialDyadicallyBounded
    xMajorant xRadius xTail commonBase xDominance
  rightFactor = alignedAbsorbedExponentialDyadicallyBounded
    yMajorant yRadius yTail commonBase yDominance
  sumRegular = alignedAbsorbedExponentialRegular
    sumTail commonBase sumDominance

  identify : {q : Q.ℚ} (tail : ExponentialTailSeed q)
    (dominance : ℕOrder._≤_ (absorbedScheduleBase tail) commonBase)
    (k : ℕ) →
    approximation (alignedAbsorbedExponentialRegular tail commonBase dominance) k ≡
    finiteSum (exponentialTerm q)
      (absorbedResidualCutoff (absorptionExponent seed) (alignment ℕ.+ k))
  identify {q} tail dominance k =
    alignedAbsorbedExponentialApproximation tail commonBase dominance k ∙
    cong (finiteSum (exponentialTerm q))
      (alignedAbsorbedCutoffPath tail commonBase dominance k ∙
        alignedResidualCutoffShiftPath (absorptionExponent seed) alignment zero k)

  module Comparison = IdentifiedExponentialProduct seed alignment
    leftFactor rightFactor sumRegular
    (identify xTail xDominance) (identify yTail yDominance)
    (identify sumTail sumDominance)

  open Comparison public using (pointwiseBound; metricComparison; shiftedSum)

  productToAbsorbedSum : boundedProductRegular leftFactor rightFactor ≈metric
    absorbedExponentialRegular sumTail
  productToAbsorbedSum = ≈metric-trans
    (boundedProductRegular leftFactor rightFactor) shiftedSum
    (absorbedExponentialRegular sumTail) metricComparison
    (≈metric-trans shiftedSum sumRegular (absorbedExponentialRegular sumTail)
      (iterateShift-equivalent Comparison.productDepth sumRegular)
      (alignedAbsorbedExponentialEquivalent sumTail commonBase sumDominance))

finiteTriangularResidualBelowTarget :
  (a A b B : ℕ → Q.ℚ) →
  ((i : ℕ) → 0 ≤ A i) → ((j : ℕ) → 0 ≤ B j) →
  ((i : ℕ) → MagnitudeBound (a i) (A i)) →
  ((j : ℕ) → MagnitudeBound (b j) (B j)) →
  (cutoff : ℕ) (target : Q.ℚ) →
  finiteRectangularCauchyProduct A B cutoff cutoff Q.+
    finiteTriangularCauchyProduct A B cutoff ≤ target →
  MagnitudeBound (finiteTriangularResidual a b cutoff) target
finiteTriangularResidualBelowTarget
  a A b B A≥0 B≥0 aBound bBound cutoff target majorant≤target =
  weakenMagnitudeBound _ _ target
    (finiteTriangularResidualMajorantBound
      a A b B A≥0 B≥0 aBound bBound cutoff)
    majorant≤target

TriangularResidualVanishes : (ℕ → Q.ℚ) → (ℕ → Q.ℚ) → Type
TriangularResidualVanishes a b =
  (tolerance : Q.ℚ) → Σ[ start ∈ ℕ ]
    ((cutoff : ℕ) → ℕOrder._≤_ start cutoff →
      MagnitudeBound (finiteTriangularResidual a b cutoff) tolerance)

BoundSequenceVanishes : (ℕ → Q.ℚ) → Type
BoundSequenceVanishes bound =
  (tolerance : Q.ℚ) → Σ[ start ∈ ℕ ]
    ((cutoff : ℕ) → ℕOrder._≤_ start cutoff → bound cutoff ≤ tolerance)

vanishingBoundImpliesResidualVanishing :
  (a b : ℕ → Q.ℚ) (bound : ℕ → Q.ℚ) →
  ((cutoff : ℕ) →
    MagnitudeBound (finiteTriangularResidual a b cutoff) (bound cutoff)) →
  BoundSequenceVanishes bound → TriangularResidualVanishes a b
vanishingBoundImpliesResidualVanishing a b bound residualBound boundVanishes
  tolerance =
  fst witness , λ cutoff start≤cutoff →
    weakenMagnitudeBound _ (bound cutoff) tolerance
      (residualBound cutoff) (snd witness cutoff start≤cutoff)
  where
  witness = boundVanishes tolerance

finiteRectangularMagnitudeBound a A b B A≥0 B≥0 aBound bBound
  leftCutoff rightCutoff =
  transport-magnitude _ _ _
    (finiteRectangularCauchyProductByRows
      a b leftCutoff rightCutoff)
    (subst
      (MagnitudeBound
        (finiteSum (λ i → finiteSum (λ j → a i Q.· b j) rightCutoff)
          leftCutoff))
      (sym (finiteRectangularCauchyProductByRows
        A B leftCutoff rightCutoff))
      (finiteSumMagnitudeBound
        (λ i → finiteSum (λ j → a i Q.· b j) rightCutoff)
        (λ i → finiteSum (λ j → A i Q.· B j) rightCutoff)
        (λ i → finiteSumMagnitudeBound
          (λ j → a i Q.· b j)
          (λ j → A i Q.· B j)
          (λ j → arbitrary-multiplier-bound
            (a i) (A i) (b j) (B j)
            (A≥0 i) (B≥0 j) (aBound i) (bBound j))
          rightCutoff)
        leftCutoff))
