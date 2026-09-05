{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyProductCongruence where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; _+_; max)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Data.Sigma
open import Cubical.HITs.PropositionalTruncation as PT
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CauchyProductAlgebra
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import CauchyProductRegularity
open import CauchyMetricEquivalence
open import CauchyRationalDensity
open import CauchyQuantitativeContinuity
open import CauchyProductDepthIndependence
open import DyadicallyBoundedCauchyAddition
open import DyadicallyBoundedCauchyMultiplication
open import CauchyAdditionCongruence
open import DyadicBoundNormalization

pointwise-product-difference-bound :
  (a b c d A B e : Q.ℚ) →
  0 ≤ A → 0 ≤ B → 0 ≤ e →
  MagnitudeBound a A → MagnitudeBound d B →
  MagnitudeBound (b Q.+ (Q.- d)) e →
  MagnitudeBound (a Q.+ (Q.- c)) e →
  MagnitudeBound
    ((a Q.· b) Q.+ (Q.- (c Q.· d)))
    ((A Q.· e) Q.+ (B Q.· e))
pointwise-product-difference-bound a b c d A B e
  0≤A 0≤B 0≤e aBound dBound b-dBound a-cBound =
  transport-magnitude _ _ ((A Q.· e) Q.+ (B Q.· e))
    (product-difference-decomposition a b c d)
    (add-magnitude-bounds _ _ _ _
      (arbitrary-multiplier-bound a A
        (b Q.+ (Q.- d)) e 0≤A 0≤e aBound b-dBound)
      (arbitrary-multiplier-bound d B
        (a Q.+ (Q.- c)) e 0≤B 0≤e dBound a-cBound))

product-congruence-scale-bound : (dx dy k : ℕ) →
  let refinement = suc (dx ℕ.+ dy)
      e = precision (refinement ℕ.+ k)
  in
  (dyadicRadius dx Q.· e) Q.+ (dyadicRadius dy Q.· e) ≤
  precision k
product-congruence-scale-bound dx dy k =
  let refinement = suc (dx ℕ.+ dy)
      e = precision (refinement ℕ.+ k)
  in
  subst2 _≤_
    (sym (ProductScalePaths.factor-right PreferredℚCommRing
      (dyadicRadius dx) (dyadicRadius dy) e))
    (radius-cancels-precision-shift refinement k)
    (≤-·o
      (dyadicRadius dx Q.+ dyadicRadius dy)
      (dyadicRadius refinement) e
      (precision-nonnegative (refinement ℕ.+ k))
      (radius-sum≤successor-combined dx dy))

pointwise-refined-product-congruence-bound :
  (a b c d : Q.ℚ) (dx dy k : ℕ) →
  MagnitudeBound a (dyadicRadius dx) →
  MagnitudeBound d (dyadicRadius dy) →
  MagnitudeBound (b Q.+ (Q.- d))
    (precision (suc (dx ℕ.+ dy) ℕ.+ k)) →
  MagnitudeBound (a Q.+ (Q.- c))
    (precision (suc (dx ℕ.+ dy) ℕ.+ k)) →
  MagnitudeBound ((a Q.· b) Q.+ (Q.- (c Q.· d))) (precision k)
pointwise-refined-product-congruence-bound a b c d dx dy k
  aBound dBound b-dBound a-cBound =
  weaken-magnitude-bound _ _ (precision k)
    (product-congruence-scale-bound dx dy k)
    (pointwise-product-difference-bound a b c d
      (dyadicRadius dx) (dyadicRadius dy)
      (precision (suc (dx ℕ.+ dy) ℕ.+ k))
      (dyadicRadius-nonnegative dx)
      (dyadicRadius-nonnegative dy)
      (precision-nonnegative (suc (dx ℕ.+ dy) ℕ.+ k))
      aBound dBound b-dBound a-cBound)

single-difference-bound→directed : (a b e : Q.ℚ) →
  a Q.+ (Q.- b) ≤ e → a ≤ b Q.+ e
single-difference-bound→directed a b e bound =
  subst2 _≤_
    (DirectedPaths.restore-right PreferredℚCommRing a b)
    (Q.+Comm e b)
    (≤-+o (a Q.+ (Q.- b)) e b bound)

CombinedEventually : RegularCauchy → RegularCauchy →
  RegularCauchy → RegularCauchy → ℕ → Type
CombinedEventually x x′ y y′ k =
  ∥ Σ[ N ∈ ℕ ] ((n : ℕ) → ℕOrder._≤_ N n →
      ((approximation x n ≤ approximation x′ n Q.+ precision k) ×
       (approximation x′ n ≤ approximation x n Q.+ precision k)) ×
      ((approximation y n ≤ approximation y′ n Q.+ precision k) ×
       (approximation y′ n ≤ approximation y n Q.+ precision k))) ∥₁

combine-eventual-thresholds :
  (x x′ y y′ : RegularCauchy) (k : ℕ) →
  EventuallyWithin x x′ k → EventuallyWithin y y′ k →
  CombinedEventually x x′ y y′ k
combine-eventual-thresholds x x′ y y′ k rx ry =
  PT.rec isPropPropTrunc
    (λ { (Nx , xBounds) →
      PT.rec isPropPropTrunc
        (λ { (Ny , yBounds) →
          ∣ (ℕ.max Nx Ny , λ n max≤n →
            xBounds n (ℕOrder.≤-trans ℕOrder.left-≤-max max≤n) ,
            yBounds n (ℕOrder.≤-trans ℕOrder.right-≤-max max≤n)) ∣₁ })
        ry })
    rx

normalized-product-preserves-eventual :
  (x x′ y y′ : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  let refinement = suc (commonExponent x x′ ℕ.+ commonExponent y y′)
  in
  EventuallyWithin (regular x) (regular x′) (refinement ℕ.+ k) →
  EventuallyWithin (regular y) (regular y′) (refinement ℕ.+ k) →
  EventuallyWithin
    (boundedProductRegular (normalizeLeft x x′) (normalizeLeft y y′))
    (boundedProductRegular (normalizeRight x x′) (normalizeRight y y′)) k
normalized-product-preserves-eventual x x′ y y′ k rx ry =
  let nx = normalizeLeft x x′
      nx′ = normalizeRight x x′
      ny = normalizeLeft y y′
      ny′ = normalizeRight y y′
      dx = commonExponent x x′
      dy = commonExponent y y′
      refinement = suc (dx ℕ.+ dy)
      query = refinement ℕ.+ k
  in
  PT.map
    (λ { (N , bounds) →
      N , λ n N≤n →
        let N≤shifted = ℕOrder.≤-trans N≤n ℕOrder.≤SumRight
            both = bounds (refinement ℕ.+ n) N≤shifted
            xb = fst both
            yb = snd both
            productBound = pointwise-refined-product-congruence-bound
              (approximation (regular nx) (refinement ℕ.+ n))
              (approximation (regular ny) (refinement ℕ.+ n))
              (approximation (regular nx′) (refinement ℕ.+ n))
              (approximation (regular ny′) (refinement ℕ.+ n))
              dx dy k
              (bounded-value nx (refinement ℕ.+ n))
              (bounded-value ny′ (refinement ℕ.+ n))
              (difference-magnitude-bound
                (approximation (regular ny) (refinement ℕ.+ n))
                (approximation (regular ny′) (refinement ℕ.+ n))
                (precision query) (fst yb) (snd yb))
              (difference-magnitude-bound
                (approximation (regular nx) (refinement ℕ.+ n))
                (approximation (regular nx′) (refinement ℕ.+ n))
                (precision query) (fst xb) (snd xb))
            leftProduct = approximation (boundedProductRegular nx ny) n
            rightProduct = approximation (boundedProductRegular nx′ ny′) n
        in
        single-difference-bound→directed leftProduct rightProduct
          (precision k) (positive-upper productBound) ,
        single-difference-bound→directed rightProduct leftProduct
          (precision k)
          (subst (λ z → z ≤ precision k)
            (ProductSignPaths.negative-difference PreferredℚCommRing
              leftProduct rightProduct)
            (negative-upper productBound)) })
    (combine-eventual-thresholds
      (regular x) (regular x′) (regular y) (regular y′) query rx ry)

normalized-product-preserves-right-eventual :
  (x y y′ : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  let refinement = suc (commonExponent x x ℕ.+ commonExponent y y′)
  in
  EventuallyWithin (regular y) (regular y′) (refinement ℕ.+ k) →
  EventuallyWithin
    (boundedProductRegular (normalizeLeft x x) (normalizeLeft y y′))
    (boundedProductRegular (normalizeRight x x) (normalizeRight y y′)) k
normalized-product-preserves-right-eventual x y y′ k relation =
  let refinement = suc (commonExponent x x ℕ.+ commonExponent y y′)
  in
  normalized-product-preserves-eventual x x y y′ k
    (≈metric-refl (regular x) (refinement ℕ.+ k)) relation

normalized-product-preserves-left-eventual :
  (x x′ y : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  let refinement = suc (commonExponent x x′ ℕ.+ commonExponent y y)
  in
  EventuallyWithin (regular x) (regular x′) (refinement ℕ.+ k) →
  EventuallyWithin
    (boundedProductRegular (normalizeLeft x x′) (normalizeLeft y y))
    (boundedProductRegular (normalizeRight x x′) (normalizeRight y y)) k
normalized-product-preserves-left-eventual x x′ y k relation =
  let refinement = suc (commonExponent x x′ ℕ.+ commonExponent y y)
  in
  normalized-product-preserves-eventual x x′ y y k relation
    (≈metric-refl (regular y) (refinement ℕ.+ k))

normalized-product-rational-right-dense :
  (x y : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  let refinement = suc (commonExponent x x ℕ.+ commonExponent y y)
      N = suc (refinement ℕ.+ k)
      qy = rationalApproximationDyadicallyBounded y N
  in
  EventuallyWithin
    (boundedProductRegular (normalizeLeft x x) (normalizeLeft y qy))
    (boundedProductRegular (normalizeRight x x) (normalizeRight y qy)) k
normalized-product-rational-right-dense x y k =
  let refinement = suc (commonExponent x x ℕ.+ commonExponent y y)
      N = suc (refinement ℕ.+ k)
      qy = rationalApproximationDyadicallyBounded y N
      qyCloseY = bounded-rational-approximation-dense y (refinement ℕ.+ k)
      yCloseQy = PT.map
        (λ { (threshold , bounds) →
          threshold , λ n threshold≤n →
            snd (bounds n threshold≤n) , fst (bounds n threshold≤n) })
        qyCloseY
  in
  normalized-product-preserves-right-eventual x y qy k yCloseQy

bounded-product-preserves-right-eventual :
  (x y y′ : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  let target = suc (suc k)
      refinement = suc (commonExponent x x ℕ.+ commonExponent y y′)
  in
  EventuallyWithin (regular y) (regular y′) (refinement ℕ.+ target) →
  EventuallyWithin
    (boundedProductRegular x y) (boundedProductRegular x y′) k
bounded-product-preserves-right-eventual x y y′ k relation =
  let target = suc (suc k)
      ex = commonExponent x x
      ey = commonExponent y y′
      leftWidened = widened-product-equivalent x y ex ey
        ℕOrder.left-≤-max ℕOrder.left-≤-max
      rightWidened = widened-product-equivalent x y′ ex ey
        ℕOrder.right-≤-max ℕOrder.right-≤-max
      firstEdge = eventuallyWithin-sym
        (boundedProductRegular (normalizeLeft x x) (normalizeLeft y y′))
        (boundedProductRegular x y) (suc k) (leftWidened (suc k))
      middleEdge = normalized-product-preserves-right-eventual
        x y y′ target relation
      lastTwo = composeEventuallyWithin
        (boundedProductRegular (normalizeLeft x x) (normalizeLeft y y′))
        (boundedProductRegular (normalizeRight x x) (normalizeRight y y′))
        (boundedProductRegular x y′) (suc k)
        middleEdge (rightWidened target)
  in
  composeEventuallyWithin
    (boundedProductRegular x y)
    (boundedProductRegular (normalizeLeft x x) (normalizeLeft y y′))
    (boundedProductRegular x y′) k firstEdge lastTwo

bounded-product-rational-right-dense :
  (x y : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  let target = suc (suc k)
      refinement = suc (commonExponent x x ℕ.+ commonExponent y y)
      N = suc (refinement ℕ.+ target)
      qy = rationalApproximationDyadicallyBounded y N
  in
  EventuallyWithin
    (boundedProductRegular x y) (boundedProductRegular x qy) k
bounded-product-rational-right-dense x y k =
  let target = suc (suc k)
      refinement = suc (commonExponent x x ℕ.+ commonExponent y y)
      N = suc (refinement ℕ.+ target)
      qy = rationalApproximationDyadicallyBounded y N
      yCloseQy = eventuallyWithin-sym
        (regular qy) (regular y) (refinement ℕ.+ target)
        (bounded-rational-approximation-dense y (refinement ℕ.+ target))
  in
  bounded-product-preserves-right-eventual x y qy k yCloseQy

normalized-product-rational-left-dense :
  (x y : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  let refinement = suc (commonExponent x x ℕ.+ commonExponent y y)
      N = suc (refinement ℕ.+ k)
      qx = rationalApproximationDyadicallyBounded x N
  in
  EventuallyWithin
    (boundedProductRegular (normalizeLeft x qx) (normalizeLeft y y))
    (boundedProductRegular (normalizeRight x qx) (normalizeRight y y)) k
normalized-product-rational-left-dense x y k =
  let refinement = suc (commonExponent x x ℕ.+ commonExponent y y)
      N = suc (refinement ℕ.+ k)
      qx = rationalApproximationDyadicallyBounded x N
      qxCloseX = bounded-rational-approximation-dense x (refinement ℕ.+ k)
      xCloseQx = PT.map
        (λ { (threshold , bounds) →
          threshold , λ n threshold≤n →
            snd (bounds n threshold≤n) , fst (bounds n threshold≤n) })
        qxCloseX
  in
  normalized-product-preserves-left-eventual x qx y k xCloseQx

bounded-product-preserves-left-eventual :
  (x x′ y : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  let target = suc (suc k)
      refinement = suc (commonExponent x x′ ℕ.+ commonExponent y y)
  in
  EventuallyWithin (regular x) (regular x′) (refinement ℕ.+ target) →
  EventuallyWithin
    (boundedProductRegular x y) (boundedProductRegular x′ y) k
bounded-product-preserves-left-eventual x x′ y k relation =
  let target = suc (suc k)
      ex = commonExponent x x′
      ey = commonExponent y y
      leftWidened = widened-product-equivalent x y ex ey
        ℕOrder.left-≤-max ℕOrder.left-≤-max
      rightWidened = widened-product-equivalent x′ y ex ey
        ℕOrder.right-≤-max ℕOrder.right-≤-max
      firstEdge = eventuallyWithin-sym
        (boundedProductRegular (normalizeLeft x x′) (normalizeLeft y y))
        (boundedProductRegular x y) (suc k) (leftWidened (suc k))
      middleEdge = normalized-product-preserves-left-eventual
        x x′ y target relation
      lastTwo = composeEventuallyWithin
        (boundedProductRegular (normalizeLeft x x′) (normalizeLeft y y))
        (boundedProductRegular (normalizeRight x x′) (normalizeRight y y))
        (boundedProductRegular x′ y) (suc k)
        middleEdge (rightWidened target)
  in
  composeEventuallyWithin
    (boundedProductRegular x y)
    (boundedProductRegular (normalizeLeft x x′) (normalizeLeft y y))
    (boundedProductRegular x′ y) k firstEdge lastTwo

bounded-product-rational-left-dense :
  (x y : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  let target = suc (suc k)
      refinement = suc (commonExponent x x ℕ.+ commonExponent y y)
      N = suc (refinement ℕ.+ target)
      qx = rationalApproximationDyadicallyBounded x N
  in
  EventuallyWithin
    (boundedProductRegular x y) (boundedProductRegular qx y) k
bounded-product-rational-left-dense x y k =
  let target = suc (suc k)
      refinement = suc (commonExponent x x ℕ.+ commonExponent y y)
      N = suc (refinement ℕ.+ target)
      qx = rationalApproximationDyadicallyBounded x N
      xCloseQx = eventuallyWithin-sym
        (regular qx) (regular x) (refinement ℕ.+ target)
        (bounded-rational-approximation-dense x (refinement ℕ.+ target))
  in
  bounded-product-preserves-left-eventual x qx y k xCloseQx

bounded-product-preserves-eventual :
  (x x′ y y′ : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  let edgeTarget = suc k
      innerTarget = suc (suc edgeTarget)
      xRefinement = suc (commonExponent x x′ ℕ.+ commonExponent y y)
      yRefinement = suc (commonExponent x′ x′ ℕ.+ commonExponent y y′)
  in
  EventuallyWithin (regular x) (regular x′)
    (xRefinement ℕ.+ innerTarget) →
  EventuallyWithin (regular y) (regular y′)
    (yRefinement ℕ.+ innerTarget) →
  EventuallyWithin
    (boundedProductRegular x y) (boundedProductRegular x′ y′) k
bounded-product-preserves-eventual x x′ y y′ k xRelation yRelation =
  composeEventuallyWithin
    (boundedProductRegular x y)
    (boundedProductRegular x′ y)
    (boundedProductRegular x′ y′) k
    (bounded-product-preserves-left-eventual x x′ y (suc k) xRelation)
    (bounded-product-preserves-right-eventual x′ y y′ (suc k) yRelation)

bounded-product-rational-dense :
  (x y : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  let target = suc (suc (suc k))
      refinement = suc (commonExponent x x ℕ.+ commonExponent y y)
      N = suc (refinement ℕ.+ target)
      qx = rationalApproximationDyadicallyBounded x N
      qy = rationalApproximationDyadicallyBounded y N
  in
  EventuallyWithin
    (boundedProductRegular x y) (boundedProductRegular qx qy) k
bounded-product-rational-dense x y k =
  let target = suc (suc (suc k))
      refinement = suc (commonExponent x x ℕ.+ commonExponent y y)
      query = refinement ℕ.+ target
      N = suc query
      qx = rationalApproximationDyadicallyBounded x N
      qy = rationalApproximationDyadicallyBounded y N
      xCloseQx = eventuallyWithin-sym (regular qx) (regular x) query
        (bounded-rational-approximation-dense x query)
      yCloseQy = eventuallyWithin-sym (regular qy) (regular y) query
        (bounded-rational-approximation-dense y query)
  in
  bounded-product-preserves-eventual x qx y qy k xCloseQx yCloseQy

bounded-left-nested-product-preserves-eventual :
  (x x′ y y′ z z′ : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  let xy = multiplyDyadicallyBounded x y
      x′y′ = multiplyDyadicallyBounded x′ y′
      outerTarget = suc (suc (suc k))
      innerOutput =
        suc (commonExponent xy x′y′ ℕ.+ commonExponent z z) ℕ.+
        outerTarget
      innerTarget = suc (suc (suc innerOutput))
      xRefinement = suc (commonExponent x x′ ℕ.+ commonExponent y y)
      yRefinement = suc (commonExponent x′ x′ ℕ.+ commonExponent y y′)
      zRefinement = suc
        (commonExponent x′y′ x′y′ ℕ.+ commonExponent z z′)
  in
  EventuallyWithin (regular x) (regular x′)
    (xRefinement ℕ.+ innerTarget) →
  EventuallyWithin (regular y) (regular y′)
    (yRefinement ℕ.+ innerTarget) →
  EventuallyWithin (regular z) (regular z′)
    (zRefinement ℕ.+ outerTarget) →
  EventuallyWithin
    (boundedProductRegular xy z) (boundedProductRegular x′y′ z′) k
bounded-left-nested-product-preserves-eventual
    x x′ y y′ z z′ k xRelation yRelation zRelation =
  let xy = multiplyDyadicallyBounded x y
      x′y′ = multiplyDyadicallyBounded x′ y′
      outerTarget = suc (suc (suc k))
      innerOutput =
        suc (commonExponent xy x′y′ ℕ.+ commonExponent z z) ℕ.+
        outerTarget
      innerRelation = bounded-product-preserves-eventual
        x x′ y y′ innerOutput xRelation yRelation
  in
  bounded-product-preserves-eventual
    xy x′y′ z z′ k innerRelation zRelation

bounded-right-nested-product-preserves-eventual :
  (x x′ y y′ z z′ : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  let yz = multiplyDyadicallyBounded y z
      y′z′ = multiplyDyadicallyBounded y′ z′
      outerTarget = suc (suc (suc k))
      innerOutput =
        suc (commonExponent x′ x′ ℕ.+ commonExponent yz y′z′) ℕ.+
        outerTarget
      innerTarget = suc (suc (suc innerOutput))
      xRefinement = suc (commonExponent x x′ ℕ.+ commonExponent yz yz)
      yRefinement = suc (commonExponent y y′ ℕ.+ commonExponent z z)
      zRefinement = suc
        (commonExponent y′ y′ ℕ.+ commonExponent z z′)
  in
  EventuallyWithin (regular x) (regular x′)
    (xRefinement ℕ.+ outerTarget) →
  EventuallyWithin (regular y) (regular y′)
    (yRefinement ℕ.+ innerTarget) →
  EventuallyWithin (regular z) (regular z′)
    (zRefinement ℕ.+ innerTarget) →
  EventuallyWithin
    (boundedProductRegular x yz) (boundedProductRegular x′ y′z′) k
bounded-right-nested-product-preserves-eventual
    x x′ y y′ z z′ k xRelation yRelation zRelation =
  let yz = multiplyDyadicallyBounded y z
      y′z′ = multiplyDyadicallyBounded y′ z′
      outerTarget = suc (suc (suc k))
      innerOutput =
        suc (commonExponent x′ x′ ℕ.+ commonExponent yz y′z′) ℕ.+
        outerTarget
      innerRelation = bounded-product-preserves-eventual
        y y′ z z′ innerOutput yRelation zRelation
  in
  bounded-product-preserves-eventual
    x x′ yz y′z′ k xRelation innerRelation

bounded-product-over-sum-preserves-eventual :
  (x x′ y y′ z z′ : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  let yz = addDyadicallyBounded y z
      y′z′ = addDyadicallyBounded y′ z′
      outerTarget = suc (suc (suc k))
      xRefinement = suc (commonExponent x x′ ℕ.+ commonExponent yz yz)
      sumRefinement = suc
        (commonExponent x′ x′ ℕ.+ commonExponent yz y′z′)
      sumInput = sumRefinement ℕ.+ outerTarget
  in
  EventuallyWithin (regular x) (regular x′)
    (xRefinement ℕ.+ outerTarget) →
  EventuallyWithin (regular y) (regular y′) (suc sumInput) →
  EventuallyWithin (regular z) (regular z′) (suc sumInput) →
  EventuallyWithin
    (boundedProductRegular x yz) (boundedProductRegular x′ y′z′) k
bounded-product-over-sum-preserves-eventual
    x x′ y y′ z z′ k xRelation yRelation zRelation =
  let yz = addDyadicallyBounded y z
      y′z′ = addDyadicallyBounded y′ z′
      outerTarget = suc (suc (suc k))
      sumInput =
        suc (commonExponent x′ x′ ℕ.+ commonExponent yz y′z′) ℕ.+
        outerTarget
      sumRelation = addRegular-preserves-eventual
        (regular y) (regular y′) (regular z) (regular z′)
        sumInput yRelation zRelation
  in
  bounded-product-preserves-eventual
    x x′ yz y′z′ k xRelation sumRelation

bounded-sum-of-products-preserves-eventual :
  (x x′ y y′ z z′ : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  let productTarget = suc (suc (suc (suc k)))
      xyX = suc (commonExponent x x′ ℕ.+ commonExponent y y) ℕ.+
        productTarget
      xzX = suc (commonExponent x x′ ℕ.+ commonExponent z z) ℕ.+
        productTarget
      xInput = ℕ.max xyX xzX
      yInput = suc (commonExponent x′ x′ ℕ.+ commonExponent y y′) ℕ.+
        productTarget
      zInput = suc (commonExponent x′ x′ ℕ.+ commonExponent z z′) ℕ.+
        productTarget
  in
  EventuallyWithin (regular x) (regular x′) xInput →
  EventuallyWithin (regular y) (regular y′) yInput →
  EventuallyWithin (regular z) (regular z′) zInput →
  EventuallyWithin
    (regular (addDyadicallyBounded
      (multiplyDyadicallyBounded x y) (multiplyDyadicallyBounded x z)))
    (regular (addDyadicallyBounded
      (multiplyDyadicallyBounded x′ y′) (multiplyDyadicallyBounded x′ z′))) k
bounded-sum-of-products-preserves-eventual
    x x′ y y′ z z′ k xRelation yRelation zRelation =
  let productTarget = suc (suc (suc (suc k)))
      xyX = suc (commonExponent x x′ ℕ.+ commonExponent y y) ℕ.+
        productTarget
      xzX = suc (commonExponent x x′ ℕ.+ commonExponent z z) ℕ.+
        productTarget
      xInput = ℕ.max xyX xzX
      xyX≤input : ℕOrder._≤_ xyX (ℕ.max xyX xzX)
      xyX≤input = ℕOrder.left-≤-max {n = xzX}
      xzX≤input : ℕOrder._≤_ xzX (ℕ.max xyX xzX)
      xzX≤input = ℕOrder.right-≤-max {m = xyX}
      xForY = eventuallyWithin-weaken (regular x) (regular x′)
        xyX xInput xyX≤input xRelation
      xForZ = eventuallyWithin-weaken (regular x) (regular x′)
        xzX xInput xzX≤input xRelation
      xyRelation = bounded-product-preserves-eventual
        x x′ y y′ (suc k) xForY yRelation
      xzRelation = bounded-product-preserves-eventual
        x x′ z z′ (suc k) xForZ zRelation
  in
  addRegular-preserves-eventual
    (boundedProductRegular x y) (boundedProductRegular x′ y′)
    (boundedProductRegular x z) (boundedProductRegular x′ z′)
    k xyRelation xzRelation

normalized-product-congruent :
  (x x′ y y′ : DyadicallyBoundedRegularCauchy) →
  regular x ≈metric regular x′ → regular y ≈metric regular y′ →
  boundedProductRegular (normalizeLeft x x′) (normalizeLeft y y′) ≈metric
  boundedProductRegular (normalizeRight x x′) (normalizeRight y y′)
normalized-product-congruent x x′ y y′ rx ry k =
  let refinement = suc (commonExponent x x′ ℕ.+ commonExponent y y′)
  in
  normalized-product-preserves-eventual x x′ y y′ k
    (rx (refinement ℕ.+ k)) (ry (refinement ℕ.+ k))
