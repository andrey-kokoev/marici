{-# OPTIONS --safe --cubical --no-import-sorts --guardedness --lossy-unification #-}
module CauchyProductWitnessCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (suc; _+_; max)
open import Cubical.Data.Rationals as Q
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Prod
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import RationallyBoundedCauchy
open import CauchyMetricEquivalence
open import CauchyBoundPromotion
open import RationalArchimedean
open import DyadicallyBoundedCauchy
open import DyadicBoundNormalization
open import CauchyProductRegularity
open import CauchyProductCongruence
open import CauchyProductDepthIndependence
open import CanonicalDyadicallyBoundedCauchy

path→metric : (x y : RegularCauchy) → x ≡ y → x ≈metric y
path→metric x y p = subst (λ z → x ≈metric z) p (≈metric-refl x)

presentation-relation :
  {x x′ : RegularCauchy} →
  (p : BoundedPresentation x) (q : BoundedPresentation x′) →
  x ≈metric x′ → regular (fst p) ≈metric regular (fst q)
presentation-relation {x} {x′} (bx , bxPath) (bx′ , bx′Path) relation =
  ≈metric-trans (regular bx) x (regular bx′)
    (path→metric (regular bx) x bxPath)
    (≈metric-trans x x′ (regular bx′) relation
      (path→metric x′ (regular bx′) (sym bx′Path)))

bounded-presentation-value : {x : RegularCauchy} →
  BoundedPresentation x → DyadicallyBoundedRegularCauchy
bounded-presentation-value = fst

BoundedProductWitness : RegularCauchy → RegularCauchy → Type
BoundedProductWitness x y = BoundedPresentation x × BoundedPresentation y

boundedWitnessProductClass :
  {x y : RegularCauchy} →
  BoundedProductWitness x y → MetricCompletionCandidate
boundedWitnessProductClass ((bx , _) , (by , _)) =
  SQ.[ boundedProductRegular bx by ]

boundedWitnessProductClass-2constant :
  {x y : RegularCauchy} →
  (p q : BoundedProductWitness x y) →
  boundedWitnessProductClass p ≡ boundedWitnessProductClass q
boundedWitnessProductClass-2constant {x} {y}
  ((bx , bxPath) , (by , byPath))
  ((bx′ , bx′Path) , (by′ , by′Path)) =
  let ex = commonExponent bx bx′
      ey = commonExponent by by′
      leftProduct = boundedProductRegular
        (normalizeLeft bx bx′) (normalizeLeft by by′)
      rightProduct = boundedProductRegular
        (normalizeRight bx bx′) (normalizeRight by by′)
      original-left-to-normalized = ≈metric-sym
        leftProduct (boundedProductRegular bx by)
        (widened-product-equivalent bx by ex ey
          ℕOrder.left-≤-max ℕOrder.left-≤-max)
      normalized-congruence = normalized-product-congruent
        bx bx′ by by′
        (path→metric (regular bx) (regular bx′)
          (bxPath ∙ sym bx′Path))
        (path→metric (regular by) (regular by′)
          (byPath ∙ sym by′Path))
      normalized-to-original-right = widened-product-equivalent
        bx′ by′ ex ey ℕOrder.right-≤-max ℕOrder.right-≤-max
      productRelation :
        boundedProductRegular bx by ≈metric boundedProductRegular bx′ by′
      productRelation k = ≈metric-trans
        (boundedProductRegular bx by) leftProduct
        (boundedProductRegular bx′ by′)
        original-left-to-normalized
        (≈metric-trans leftProduct rightProduct
          (boundedProductRegular bx′ by′)
          normalized-congruence normalized-to-original-right) k
  in
  SQ.eq/
    (boundedProductRegular bx by)
    (boundedProductRegular bx′ by′)
    productRelation

boundedWitnessProductClass-congruent :
  {x x′ y y′ : RegularCauchy} →
  (px : BoundedPresentation x) (px′ : BoundedPresentation x′) →
  (py : BoundedPresentation y) (py′ : BoundedPresentation y′) →
  x ≈metric x′ → y ≈metric y′ →
  boundedWitnessProductClass {x = x} {y = y} (px , py) ≡
  boundedWitnessProductClass {x = x′} {y = y′} (px′ , py′)
boundedWitnessProductClass-congruent
  {x} {x′} {y} {y′} px px′ py py′ rx ry =
  let bx = fst px
      bx′ = fst px′
      by = fst py
      by′ = fst py′
      ex = commonExponent bx bx′
      ey = commonExponent by by′
      leftProduct = boundedProductRegular
        (normalizeLeft bx bx′) (normalizeLeft by by′)
      rightProduct = boundedProductRegular
        (normalizeRight bx bx′) (normalizeRight by by′)
      relation :
        boundedProductRegular bx by ≈metric boundedProductRegular bx′ by′
      relation k = ≈metric-trans
        (boundedProductRegular bx by) leftProduct
        (boundedProductRegular bx′ by′)
        (≈metric-sym leftProduct (boundedProductRegular bx by)
          (widened-product-equivalent bx by ex ey
            ℕOrder.left-≤-max ℕOrder.left-≤-max))
        (≈metric-trans leftProduct rightProduct
          (boundedProductRegular bx′ by′)
          (normalized-product-congruent bx bx′ by by′
            (presentation-relation {x = x} {x′ = x′} px px′ rx)
            (presentation-relation {x = y} {x′ = y′} py py′ ry))
          (widened-product-equivalent bx′ by′ ex ey
            ℕOrder.right-≤-max ℕOrder.right-≤-max)) k
  in
  SQ.eq/
    (boundedProductRegular bx by)
    (boundedProductRegular bx′ by′)
    relation

truncatedBoundedProductClass :
  {x y : RegularCauchy} →
  ∥ BoundedPresentation x ∥₁ →
  ∥ BoundedPresentation y ∥₁ →
  MetricCompletionCandidate
truncatedBoundedProductClass {x} {y} boundedX boundedY =
  rec→Set metric-candidate-isSet
    boundedWitnessProductClass
    boundedWitnessProductClass-2constant
    (PT.map2 _,_ boundedX boundedY)

truncatedBoundedProductClass-from-presentations :
  {x y : RegularCauchy} →
  (boundedX : ∥ BoundedPresentation x ∥₁) →
  (boundedY : ∥ BoundedPresentation y ∥₁) →
  (px : BoundedPresentation x) →
  (py : BoundedPresentation y) →
  truncatedBoundedProductClass boundedX boundedY ≡
  boundedWitnessProductClass (px , py)
truncatedBoundedProductClass-from-presentations boundedX boundedY px py =
  cong
    (rec→Set metric-candidate-isSet
      boundedWitnessProductClass boundedWitnessProductClass-2constant)
    (squash₁ (PT.map2 _,_ boundedX boundedY) ∣ px , py ∣₁)

truncatedBoundedProductClass-congruent :
  {x x′ y y′ : RegularCauchy} →
  (boundedX : ∥ BoundedPresentation x ∥₁) →
  (boundedX′ : ∥ BoundedPresentation x′ ∥₁) →
  (boundedY : ∥ BoundedPresentation y ∥₁) →
  (boundedY′ : ∥ BoundedPresentation y′ ∥₁) →
  x ≈metric x′ → y ≈metric y′ →
  truncatedBoundedProductClass boundedX boundedY ≡
  truncatedBoundedProductClass boundedX′ boundedY′
truncatedBoundedProductClass-congruent
  {x} {x′} {y} {y′} boundedX boundedX′ boundedY boundedY′ rx ry =
  PT.rec
    (metric-candidate-isSet _ _)
    (λ px → PT.rec
      (metric-candidate-isSet _ _)
      (λ px′ → PT.rec
        (metric-candidate-isSet _ _)
        (λ py → PT.rec
          (metric-candidate-isSet _ _)
          (λ py′ →
            truncatedBoundedProductClass-from-presentations
              boundedX boundedY px py ∙
            boundedWitnessProductClass-congruent px px′ py py′ rx ry ∙
            sym (truncatedBoundedProductClass-from-presentations
              boundedX′ boundedY′ px′ py′))
          boundedY′)
        boundedY)
      boundedX′)
    boundedX

productClassFromDominance :
  (x y : RegularCauchy) →
  DyadicDominates (canonicalRadius x) →
  DyadicDominates (canonicalRadius y) →
  MetricCompletionCandidate
productClassFromDominance x y dominanceX dominanceY =
  truncatedBoundedProductClass
    (promote-regular-presentation-truncated x dominanceX)
    (promote-regular-presentation-truncated y dominanceY)

productClassFromDominance-from-presentations :
  {x y : RegularCauchy} →
  (dominanceX : DyadicDominates (canonicalRadius x)) →
  (dominanceY : DyadicDominates (canonicalRadius y)) →
  (px : BoundedPresentation x) →
  (py : BoundedPresentation y) →
  productClassFromDominance x y dominanceX dominanceY ≡
  boundedWitnessProductClass (px , py)
productClassFromDominance-from-presentations dominanceX dominanceY px py =
  truncatedBoundedProductClass-from-presentations
    (promote-regular-presentation-truncated _ dominanceX)
    (promote-regular-presentation-truncated _ dominanceY) px py

canonical-bounded-product-class-agrees-with-dominance :
  (x y : RegularCauchy) →
  SQ.[ boundedProductRegular
    (canonicalDyadicallyBounded x) (canonicalDyadicallyBounded y) ] ≡
  productClassFromDominance x y
    (witness-gives-truncated (canonicalRadius x)
      (canonicalArchimedeanExponent x))
    (witness-gives-truncated (canonicalRadius y)
      (canonicalArchimedeanExponent y))
canonical-bounded-product-class-agrees-with-dominance x y =
  sym (productClassFromDominance-from-presentations
    (witness-gives-truncated (canonicalRadius x)
      (canonicalArchimedeanExponent x))
    (witness-gives-truncated (canonicalRadius y)
      (canonicalArchimedeanExponent y))
    (canonicalDyadicPresentation x)
    (canonicalDyadicPresentation y))

productClassFromDominance-congruent :
  (x x′ y y′ : RegularCauchy) →
  (dominanceX : DyadicDominates (canonicalRadius x)) →
  (dominanceX′ : DyadicDominates (canonicalRadius x′)) →
  (dominanceY : DyadicDominates (canonicalRadius y)) →
  (dominanceY′ : DyadicDominates (canonicalRadius y′)) →
  x ≈metric x′ → y ≈metric y′ →
  productClassFromDominance x y dominanceX dominanceY ≡
  productClassFromDominance x′ y′ dominanceX′ dominanceY′
productClassFromDominance-congruent x x′ y y′
  dominanceX dominanceX′ dominanceY dominanceY′ rx ry =
  truncatedBoundedProductClass-congruent
    (promote-regular-presentation-truncated x dominanceX)
    (promote-regular-presentation-truncated x′ dominanceX′)
    (promote-regular-presentation-truncated y dominanceY)
    (promote-regular-presentation-truncated y′ dominanceY′)
    rx ry

bounded-presented-constant-product-regular :
  (q r : Q.ℚ) →
  (px : BoundedPresentation (constantCauchy q)) →
  (py : BoundedPresentation (constantCauchy r)) →
  boundedProductRegular (fst px) (fst py) ≡ constantCauchy (q Q.· r)
bounded-presented-constant-product-regular q r
    (bx , bxPath) (by , byPath) =
  regularCauchy-ext _ (constantCauchy (q Q.· r))
    (funExt λ n →
      cong₂ Q._·_
        (cong (λ z → approximation z
          (suc (radius-exponent bx ℕ.+ radius-exponent by) ℕ.+ n)) bxPath)
        (cong (λ z → approximation z
          (suc (radius-exponent bx ℕ.+ radius-exponent by) ℕ.+ n)) byPath))

bounded-presented-constant-product-equivalent :
  (q r : Q.ℚ) →
  (px : BoundedPresentation (constantCauchy q)) →
  (py : BoundedPresentation (constantCauchy r)) →
  boundedProductRegular (fst px) (fst py) ≈metric
  constantCauchy (q Q.· r)
bounded-presented-constant-product-equivalent q r px py =
  subst (boundedProductRegular (fst px) (fst py) ≈metric_)
    (bounded-presented-constant-product-regular q r px py)
    (≈metric-refl (boundedProductRegular (fst px) (fst py)))

bounded-presented-constant-product :
  (q r : Q.ℚ) →
  (px : BoundedPresentation (constantCauchy q)) →
  (py : BoundedPresentation (constantCauchy r)) →
  SQ.[ boundedProductRegular (fst px) (fst py) ] ≡ embedMetricℚ (q Q.· r)
bounded-presented-constant-product q r px py =
  cong SQ.[_] (bounded-presented-constant-product-regular q r px py)

truncated-presented-constant-product :
  (q r : Q.ℚ) →
  (boundedQ : ∥ BoundedPresentation (constantCauchy q) ∥₁) →
  (boundedR : ∥ BoundedPresentation (constantCauchy r) ∥₁) →
  truncatedBoundedProductClass boundedQ boundedR ≡ embedMetricℚ (q Q.· r)
truncated-presented-constant-product q r boundedQ boundedR =
  PT.rec (metric-candidate-isSet _ _)
    (λ px → PT.rec (metric-candidate-isSet _ _)
      (λ py →
        truncatedBoundedProductClass-from-presentations
          boundedQ boundedR px py ∙
        bounded-presented-constant-product q r px py)
      boundedR)
    boundedQ

productClassFromDominance-preserves-rationals :
  (q r : Q.ℚ) →
  (dominanceQ : DyadicDominates (canonicalRadius (constantCauchy q))) →
  (dominanceR : DyadicDominates (canonicalRadius (constantCauchy r))) →
  productClassFromDominance
    (constantCauchy q) (constantCauchy r) dominanceQ dominanceR ≡
  embedMetricℚ (q Q.· r)
productClassFromDominance-preserves-rationals q r dominanceQ dominanceR =
  truncated-presented-constant-product q r
    (promote-regular-presentation-truncated (constantCauchy q) dominanceQ)
    (promote-regular-presentation-truncated (constantCauchy r) dominanceR)
