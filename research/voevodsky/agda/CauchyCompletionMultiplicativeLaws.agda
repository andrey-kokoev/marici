{-# OPTIONS --safe --cubical --no-import-sorts --guardedness --lossy-unification #-}
module CauchyCompletionMultiplicativeLaws where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; _+_)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.SetQuotients as SQ
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import RationallyBoundedCauchy
open import RationalArchimedean
open import CauchyMetricEquivalence
open import CauchyBoundPromotion
open import DyadicallyBoundedCauchy
open import DyadicallyBoundedCauchyAddition
open import DyadicallyBoundedCauchyMultiplication
open import DyadicallyBoundedCauchyNegation
open import DyadicallyBoundedCauchyShift
open import CauchyProductBounds
open import CauchyProductRegularity
open import CauchyProductCongruence
open import CauchyRationalDensity
open import CauchyQuantitativeContinuity
open import CauchyProductDepthIndependence
open import DyadicBoundNormalization
open import CauchyProductWitnessCoherence
open import CauchyCompletionMultiplication
open import CauchyAddition
open import CauchyAdditionCongruence
open import CauchyNegation
open import CauchyRationalEmbedding
open import CauchyShift
open import CauchyAdditiveLaws using (pointwise-equivalent)

bounded-product-commutative :
  (x y : DyadicallyBoundedRegularCauchy) →
  boundedProductRegular x y ≈metric boundedProductRegular y x
bounded-product-commutative x y =
  pointwise-equivalent (boundedProductRegular x y) (boundedProductRegular y x)
    (λ n →
      cong₂ Q._·_
        (cong (approximation (regular x))
          (cong (λ d → suc d ℕ.+ n)
            (ℕ.+-comm (radius-exponent x) (radius-exponent y))))
        (cong (approximation (regular y))
          (cong (λ d → suc d ℕ.+ n)
            (ℕ.+-comm (radius-exponent x) (radius-exponent y)))) ∙
      Q.·Comm
        (approximation (regular x)
          (suc (radius-exponent y ℕ.+ radius-exponent x) ℕ.+ n))
        (approximation (regular y)
          (suc (radius-exponent y ℕ.+ radius-exponent x) ℕ.+ n)))

swap-index-prefixes : (a b n : ℕ) →
  b ℕ.+ (a ℕ.+ n) ≡ (a ℕ.+ b) ℕ.+ n
swap-index-prefixes a b n =
  ℕ.+-assoc b a n ∙
  cong (ℕ._+ n) (ℕ.+-comm b a)

reassociate-index-prefixes : (a b n : ℕ) →
  a ℕ.+ (b ℕ.+ n) ≡ (a ℕ.+ b) ℕ.+ n
reassociate-index-prefixes = ℕ.+-assoc

associativity-outer-depth :
  (x y z : DyadicallyBoundedRegularCauchy) →
  suc ((radius-exponent x ℕ.+ radius-exponent y) ℕ.+ radius-exponent z) ≡
  suc (radius-exponent x ℕ.+
    (radius-exponent y ℕ.+ radius-exponent z))
associativity-outer-depth x y z =
  cong suc (sym (ℕ.+-assoc
    (radius-exponent x) (radius-exponent y) (radius-exponent z)))


bounded-presented-constant-product-associative-regular :
  (q r s : Q.ℚ) →
  (px : BoundedPresentation (constantCauchy q)) →
  (py : BoundedPresentation (constantCauchy r)) →
  (pz : BoundedPresentation (constantCauchy s)) →
  boundedProductRegular
    (multiplyDyadicallyBounded (fst px) (fst py)) (fst pz) ≡
  boundedProductRegular
    (fst px) (multiplyDyadicallyBounded (fst py) (fst pz))
bounded-presented-constant-product-associative-regular q r s px py pz =
  let xyPath = bounded-presented-constant-product-regular q r px py
      yzPath = bounded-presented-constant-product-regular r s py pz
      leftPath = bounded-presented-constant-product-regular
        (q Q.· r) s
        (multiplyDyadicallyBounded (fst px) (fst py) , xyPath) pz
      rightPath = bounded-presented-constant-product-regular
        q (r Q.· s) px
        (multiplyDyadicallyBounded (fst py) (fst pz) , yzPath)
  in
  leftPath ∙ cong constantCauchy (sym (Q.·Assoc q r s)) ∙ sym rightPath

bounded-product-associative :
  (x y z : DyadicallyBoundedRegularCauchy) →
  boundedProductRegular (multiplyDyadicallyBounded x y) z ≈metric
  boundedProductRegular x (multiplyDyadicallyBounded y z)
bounded-product-associative x y z k =
  let leftPrecision = suc k
      rightPrecision = suc (suc k)
      xy = multiplyDyadicallyBounded x y
      yz = multiplyDyadicallyBounded y z

      leftOuterTarget = suc (suc (suc leftPrecision))
      leftInnerOutput =
        suc (commonExponent xy xy ℕ.+ commonExponent z z) ℕ.+
        leftOuterTarget
      leftInnerTarget = suc (suc (suc leftInnerOutput))
      leftX = suc (commonExponent x x ℕ.+ commonExponent y y) ℕ.+
        leftInnerTarget
      leftY = suc (commonExponent x x ℕ.+ commonExponent y y) ℕ.+
        leftInnerTarget
      leftZ = suc (commonExponent xy xy ℕ.+ commonExponent z z) ℕ.+
        leftOuterTarget

      rightOuterTarget = suc (suc (suc rightPrecision))
      rightInnerOutput =
        suc (commonExponent x x ℕ.+ commonExponent yz yz) ℕ.+
        rightOuterTarget
      rightInnerTarget = suc (suc (suc rightInnerOutput))
      rightX = suc (commonExponent x x ℕ.+ commonExponent yz yz) ℕ.+
        rightOuterTarget
      rightY = suc (commonExponent y y ℕ.+ commonExponent z z) ℕ.+
        rightInnerTarget
      rightZ = suc (commonExponent y y ℕ.+ commonExponent z z) ℕ.+
        rightInnerTarget

      xRequirement = ℕ.max leftX rightX
      yRequirement = ℕ.max leftY rightY
      zRequirement = ℕ.max leftZ rightZ
      common = ℕ.max xRequirement (ℕ.max yRequirement zRequirement)
      N = suc common
      qx = rationalApproximationDyadicallyBounded x N
      qy = rationalApproximationDyadicallyBounded y N
      qz = rationalApproximationDyadicallyBounded z N
      centers = shared-bounded-rational-centers
        x y z xRequirement yRequirement zRequirement
      qxCloseX = fst centers
      qyCloseY = fst (snd centers)
      qzCloseZ = snd (snd centers)

      xCloseQxLeft = eventuallyWithin-sym (regular qx) (regular x) leftX
        (eventuallyWithin-weaken (regular qx) (regular x)
          leftX xRequirement ℕOrder.left-≤-max qxCloseX)
      yCloseQyLeft = eventuallyWithin-sym (regular qy) (regular y) leftY
        (eventuallyWithin-weaken (regular qy) (regular y)
          leftY yRequirement ℕOrder.left-≤-max qyCloseY)
      zCloseQzLeft = eventuallyWithin-sym (regular qz) (regular z) leftZ
        (eventuallyWithin-weaken (regular qz) (regular z)
          leftZ zRequirement ℕOrder.left-≤-max qzCloseZ)
      leftEdge = bounded-left-nested-product-preserves-eventual
        x qx y qy z qz leftPrecision
        xCloseQxLeft yCloseQyLeft zCloseQzLeft

      qxCloseXRight = eventuallyWithin-weaken (regular qx) (regular x)
        rightX xRequirement ℕOrder.right-≤-max qxCloseX
      qyCloseYRight = eventuallyWithin-weaken (regular qy) (regular y)
        rightY yRequirement ℕOrder.right-≤-max qyCloseY
      qzCloseZRight = eventuallyWithin-weaken (regular qz) (regular z)
        rightZ zRequirement ℕOrder.right-≤-max qzCloseZ
      rightEdge = bounded-right-nested-product-preserves-eventual
        qx x qy y qz z rightPrecision
        qxCloseXRight qyCloseYRight qzCloseZRight

      centerPath = bounded-presented-constant-product-associative-regular
        (approximation (regular x) N)
        (approximation (regular y) N)
        (approximation (regular z) N)
        (qx , refl) (qy , refl) (qz , refl)
      centerEdge = regular-path→metric
        (boundedProductRegular (multiplyDyadicallyBounded qx qy) qz)
        (boundedProductRegular qx (multiplyDyadicallyBounded qy qz))
        centerPath rightPrecision
      centerThenRight = composeEventuallyWithin
        (boundedProductRegular (multiplyDyadicallyBounded qx qy) qz)
        (boundedProductRegular qx (multiplyDyadicallyBounded qy qz))
        (boundedProductRegular x (multiplyDyadicallyBounded y z))
        (suc k) centerEdge rightEdge
  in
  composeEventuallyWithin
    (boundedProductRegular (multiplyDyadicallyBounded x y) z)
    (boundedProductRegular (multiplyDyadicallyBounded qx qy) qz)
    (boundedProductRegular x (multiplyDyadicallyBounded y z))
    k leftEdge centerThenRight

bounded-presented-product-associative :
  {x y z : RegularCauchy} →
  (px : BoundedPresentation x) →
  (py : BoundedPresentation y) →
  (pz : BoundedPresentation z) →
  metricClass (boundedProductRegular
    (multiplyDyadicallyBounded (fst px) (fst py)) (fst pz)) ≡
  metricClass (boundedProductRegular
    (fst px) (multiplyDyadicallyBounded (fst py) (fst pz)))
bounded-presented-product-associative px py pz =
  SQ.eq/ _ _ (bounded-product-associative (fst px) (fst py) (fst pz))

bounded-constant-distributive-right-core :
  (q r s : Q.ℚ) →
  (px : BoundedPresentation (constantCauchy q)) →
  (py : BoundedPresentation (constantCauchy r)) →
  (pz : BoundedPresentation (constantCauchy s)) →
  boundedProductRegular (fst px)
    (addDyadicallyBounded (fst py) (fst pz)) ≡
  regular (addDyadicallyBounded
    (multiplyDyadicallyBounded (fst px) (fst py))
    (multiplyDyadicallyBounded (fst px) (fst pz)))
bounded-constant-distributive-right-core q r s px py pz =
  let yzPath = bounded-presented-constant-addition-regular r s py pz
      qrPath = bounded-presented-constant-product-regular q r px py
      qsPath = bounded-presented-constant-product-regular q s px pz
      leftPath = bounded-presented-constant-product-regular
        q (r Q.+ s) px
        (addDyadicallyBounded (fst py) (fst pz) , yzPath)
      rightPath = bounded-presented-constant-addition-regular
        (q Q.· r) (q Q.· s)
        (multiplyDyadicallyBounded (fst px) (fst py) , qrPath)
        (multiplyDyadicallyBounded (fst px) (fst pz) , qsPath)
  in
  leftPath ∙ cong constantCauchy (Q.·DistL+ q r s) ∙ sym rightPath

bounded-product-distributive-right :
  (x y z : DyadicallyBoundedRegularCauchy) →
  boundedProductRegular x (addDyadicallyBounded y z) ≈metric
  regular (addDyadicallyBounded
    (multiplyDyadicallyBounded x y) (multiplyDyadicallyBounded x z))
bounded-product-distributive-right x y z k =
  let leftPrecision = suc k
      rightPrecision = suc (suc k)
      yz = addDyadicallyBounded y z

      leftOuterTarget = suc (suc (suc leftPrecision))
      leftX = suc (commonExponent x x ℕ.+ commonExponent yz yz) ℕ.+
        leftOuterTarget
      leftSum = suc (commonExponent x x ℕ.+ commonExponent yz yz) ℕ.+
        leftOuterTarget
      leftY = suc leftSum
      leftZ = suc leftSum

      rightProductTarget = suc (suc (suc (suc rightPrecision)))
      rightXYX = suc (commonExponent x x ℕ.+ commonExponent y y) ℕ.+
        rightProductTarget
      rightXZX = suc (commonExponent x x ℕ.+ commonExponent z z) ℕ.+
        rightProductTarget
      rightX = ℕ.max rightXYX rightXZX
      rightY = suc (commonExponent x x ℕ.+ commonExponent y y) ℕ.+
        rightProductTarget
      rightZ = suc (commonExponent x x ℕ.+ commonExponent z z) ℕ.+
        rightProductTarget

      xRequirement = ℕ.max leftX rightX
      yRequirement = ℕ.max leftY rightY
      zRequirement = ℕ.max leftZ rightZ
      common = ℕ.max xRequirement (ℕ.max yRequirement zRequirement)
      N = suc common
      qx = rationalApproximationDyadicallyBounded x N
      qy = rationalApproximationDyadicallyBounded y N
      qz = rationalApproximationDyadicallyBounded z N
      centers = shared-bounded-rational-centers
        x y z xRequirement yRequirement zRequirement
      qxCloseX = fst centers
      qyCloseY = fst (snd centers)
      qzCloseZ = snd (snd centers)

      xCloseQxLeft = eventuallyWithin-sym (regular qx) (regular x) leftX
        (eventuallyWithin-weaken (regular qx) (regular x)
          leftX xRequirement ℕOrder.left-≤-max qxCloseX)
      yCloseQyLeft = eventuallyWithin-sym (regular qy) (regular y) leftY
        (eventuallyWithin-weaken (regular qy) (regular y)
          leftY yRequirement ℕOrder.left-≤-max qyCloseY)
      zCloseQzLeft = eventuallyWithin-sym (regular qz) (regular z) leftZ
        (eventuallyWithin-weaken (regular qz) (regular z)
          leftZ zRequirement ℕOrder.left-≤-max qzCloseZ)
      leftEdge = bounded-product-over-sum-preserves-eventual
        x qx y qy z qz leftPrecision
        xCloseQxLeft yCloseQyLeft zCloseQzLeft

      qxCloseXRight = eventuallyWithin-weaken (regular qx) (regular x)
        rightX xRequirement ℕOrder.right-≤-max qxCloseX
      qyCloseYRight = eventuallyWithin-weaken (regular qy) (regular y)
        rightY yRequirement ℕOrder.right-≤-max qyCloseY
      qzCloseZRight = eventuallyWithin-weaken (regular qz) (regular z)
        rightZ zRequirement ℕOrder.right-≤-max qzCloseZ
      rightEdge = bounded-sum-of-products-preserves-eventual
        qx x qy y qz z rightPrecision
        qxCloseXRight qyCloseYRight qzCloseZRight

      centerPath = bounded-constant-distributive-right-core
        (approximation (regular x) N)
        (approximation (regular y) N)
        (approximation (regular z) N)
        (qx , refl) (qy , refl) (qz , refl)
      centerEdge = regular-path→metric
        (boundedProductRegular qx (addDyadicallyBounded qy qz))
        (regular (addDyadicallyBounded
          (multiplyDyadicallyBounded qx qy)
          (multiplyDyadicallyBounded qx qz)))
        centerPath rightPrecision
      centerThenRight = composeEventuallyWithin
        (boundedProductRegular qx (addDyadicallyBounded qy qz))
        (regular (addDyadicallyBounded
          (multiplyDyadicallyBounded qx qy)
          (multiplyDyadicallyBounded qx qz)))
        (regular (addDyadicallyBounded
          (multiplyDyadicallyBounded x y)
          (multiplyDyadicallyBounded x z)))
        (suc k) centerEdge rightEdge
  in
  composeEventuallyWithin
    (boundedProductRegular x (addDyadicallyBounded y z))
    (boundedProductRegular qx (addDyadicallyBounded qy qz))
    (regular (addDyadicallyBounded
      (multiplyDyadicallyBounded x y) (multiplyDyadicallyBounded x z)))
    k leftEdge centerThenRight

bounded-presented-product-distributive-right :
  {x y z : RegularCauchy} →
  (px : BoundedPresentation x) →
  (py : BoundedPresentation y) →
  (pz : BoundedPresentation z) →
  metricClass (boundedProductRegular (fst px)
    (addDyadicallyBounded (fst py) (fst pz))) ≡
  metricClass (regular (addDyadicallyBounded
    (multiplyDyadicallyBounded (fst px) (fst py))
    (multiplyDyadicallyBounded (fst px) (fst pz))))
bounded-presented-product-distributive-right px py pz =
  SQ.eq/ _ _ (bounded-product-distributive-right
    (fst px) (fst py) (fst pz))

completion-multiplication-representatives-associative :
  (arch : RationalDyadicArchimedean) (x y z : RegularCauchy) →
  completionMultiplication arch
    (completionMultiplication arch SQ.[ x ] SQ.[ y ]) SQ.[ z ] ≡
  completionMultiplication arch SQ.[ x ]
    (completionMultiplication arch SQ.[ y ] SQ.[ z ])
completion-multiplication-representatives-associative arch x y z =
  let boundedX = promote-regular-presentation-truncated x
        (dominates-all arch (canonicalRadius x))
      boundedY = promote-regular-presentation-truncated y
        (dominates-all arch (canonicalRadius y))
      boundedZ = promote-regular-presentation-truncated z
        (dominates-all arch (canonicalRadius z))
  in
  PT.rec (metric-candidate-isSet _ _)
    (λ px → PT.rec (metric-candidate-isSet _ _)
      (λ py → PT.rec (metric-candidate-isSet _ _)
        (λ pz →
          let bxy = multiplyDyadicallyBounded (fst px) (fst py)
              byz = multiplyDyadicallyBounded (fst py) (fst pz)
              xyPath = productClassFromDominance-from-presentations
                (dominates-all arch (canonicalRadius x))
                (dominates-all arch (canonicalRadius y)) px py
              yzPath = productClassFromDominance-from-presentations
                (dominates-all arch (canonicalRadius y))
                (dominates-all arch (canonicalRadius z)) py pz
              leftOuterPath = productClassFromDominance-from-presentations
                (dominates-all arch
                  (canonicalRadius (boundedProductRegular (fst px) (fst py))))
                (dominates-all arch (canonicalRadius z))
                (bxy , refl) pz
              rightOuterPath = productClassFromDominance-from-presentations
                (dominates-all arch (canonicalRadius x))
                (dominates-all arch
                  (canonicalRadius (boundedProductRegular (fst py) (fst pz))))
                px (byz , refl)
          in
          cong (λ a → completionMultiplication arch a SQ.[ z ]) xyPath ∙
          leftOuterPath ∙
          bounded-presented-product-associative px py pz ∙
          sym rightOuterPath ∙
          cong (completionMultiplication arch SQ.[ x ]) (sym yzPath))
        boundedZ)
      boundedY)
    boundedX

completion-multiplication-representatives-distributive-right :
  (arch : RationalDyadicArchimedean) (x y z : RegularCauchy) →
  completionMultiplication arch SQ.[ x ] (SQ.[ y ] +completion SQ.[ z ]) ≡
  completionMultiplication arch SQ.[ x ] SQ.[ y ] +completion
  completionMultiplication arch SQ.[ x ] SQ.[ z ]
completion-multiplication-representatives-distributive-right arch x y z =
  let boundedX = promote-regular-presentation-truncated x
        (dominates-all arch (canonicalRadius x))
      boundedY = promote-regular-presentation-truncated y
        (dominates-all arch (canonicalRadius y))
      boundedZ = promote-regular-presentation-truncated z
        (dominates-all arch (canonicalRadius z))
  in
  PT.rec (metric-candidate-isSet _ _)
    (λ px → PT.rec (metric-candidate-isSet _ _)
      (λ py → PT.rec (metric-candidate-isSet _ _)
        (λ pz →
          let byz = addDyadicallyBounded (fst py) (fst pz)
              pyz : BoundedPresentation (addRegular y z)
              pyz = byz , cong₂ addRegular (snd py) (snd pz)
              leftPath = productClassFromDominance-from-presentations
                (dominates-all arch (canonicalRadius x))
                (dominates-all arch (canonicalRadius (addRegular y z)))
                px pyz
              xyPath = productClassFromDominance-from-presentations
                (dominates-all arch (canonicalRadius x))
                (dominates-all arch (canonicalRadius y)) px py
              xzPath = productClassFromDominance-from-presentations
                (dominates-all arch (canonicalRadius x))
                (dominates-all arch (canonicalRadius z)) px pz
          in
          leftPath ∙
          bounded-presented-product-distributive-right px py pz ∙
          cong₂ _+completion_ (sym xyPath) (sym xzPath))
        boundedZ)
      boundedY)
    boundedX

completion-multiplication-distributive-right :
  (arch : RationalDyadicArchimedean) →
  (a b c : MetricCompletionCandidate) →
  completionMultiplication arch a (b +completion c) ≡
  completionMultiplication arch a b +completion
  completionMultiplication arch a c
completion-multiplication-distributive-right arch =
  SQ.elimProp3
    (λ _ _ _ → metric-candidate-isSet _ _)
    (completion-multiplication-representatives-distributive-right arch)

preferred-completion-multiplication-distributive-right :
  (a b c : MetricCompletionCandidate) →
  preferredCompletionMultiplication a (b +completion c) ≡
  preferredCompletionMultiplication a b +completion
  preferredCompletionMultiplication a c
preferred-completion-multiplication-distributive-right =
  completion-multiplication-distributive-right
    preferredRationalDyadicArchimedean

completion-multiplication-associative :
  (arch : RationalDyadicArchimedean) →
  (a b c : MetricCompletionCandidate) →
  completionMultiplication arch
    (completionMultiplication arch a b) c ≡
  completionMultiplication arch a (completionMultiplication arch b c)
completion-multiplication-associative arch =
  SQ.elimProp3
    (λ _ _ _ → metric-candidate-isSet _ _)
    (completion-multiplication-representatives-associative arch)

preferred-completion-multiplication-associative :
  (a b c : MetricCompletionCandidate) →
  preferredCompletionMultiplication
    (preferredCompletionMultiplication a b) c ≡
  preferredCompletionMultiplication a (preferredCompletionMultiplication b c)
preferred-completion-multiplication-associative =
  completion-multiplication-associative preferredRationalDyadicArchimedean

bounded-presented-constant-product-distributive-right-regular :
  (q r s : Q.ℚ) →
  (px : BoundedPresentation (constantCauchy q)) →
  (py : BoundedPresentation (constantCauchy r)) →
  (pz : BoundedPresentation (constantCauchy s)) →
  boundedProductRegular (fst px)
    (addDyadicallyBounded (fst py) (fst pz)) ≡
  regular (addDyadicallyBounded
    (multiplyDyadicallyBounded (fst px) (fst py))
    (multiplyDyadicallyBounded (fst px) (fst pz)))
bounded-presented-constant-product-distributive-right-regular =
  bounded-constant-distributive-right-core

bounded-presented-constant-product-distributive-left-regular :
  (q r s : Q.ℚ) →
  (px : BoundedPresentation (constantCauchy q)) →
  (py : BoundedPresentation (constantCauchy r)) →
  (pz : BoundedPresentation (constantCauchy s)) →
  boundedProductRegular
    (addDyadicallyBounded (fst px) (fst py)) (fst pz) ≡
  regular (addDyadicallyBounded
    (multiplyDyadicallyBounded (fst px) (fst pz))
    (multiplyDyadicallyBounded (fst py) (fst pz)))
bounded-presented-constant-product-distributive-left-regular
    q r s px py pz =
  let qrPath = bounded-presented-constant-addition-regular q r px py
      qsPath = bounded-presented-constant-product-regular q s px pz
      rsPath = bounded-presented-constant-product-regular r s py pz
      leftPath = bounded-presented-constant-product-regular
        (q Q.+ r) s
        (addDyadicallyBounded (fst px) (fst py) , qrPath) pz
      rightPath = bounded-presented-constant-addition-regular
        (q Q.· s) (r Q.· s)
        (multiplyDyadicallyBounded (fst px) (fst pz) , qsPath)
        (multiplyDyadicallyBounded (fst py) (fst pz) , rsPath)
  in
  leftPath ∙ cong constantCauchy (Q.·DistR+ q r s) ∙ sym rightPath

bounded-product-shift-equivalent :
  (extraX extraY : ℕ) (x y : DyadicallyBoundedRegularCauchy) →
  boundedProductRegular
    (shiftDyadicallyBounded extraX x)
    (shiftDyadicallyBounded extraY y) ≈metric
  boundedProductRegular x y
bounded-product-shift-equivalent extraX extraY x y =
  let sx = shiftDyadicallyBounded extraX x
      sy = shiftDyadicallyBounded extraY y
      ex = commonExponent sx x
      ey = commonExponent sy y
      leftProduct = boundedProductRegular
        (normalizeLeft sx x) (normalizeLeft sy y)
      rightProduct = boundedProductRegular
        (normalizeRight sx x) (normalizeRight sy y)
  in
  ≈metric-trans (boundedProductRegular sx sy) leftProduct
    (boundedProductRegular x y)
    (≈metric-sym leftProduct (boundedProductRegular sx sy)
      (widened-product-equivalent sx sy ex ey
        ℕOrder.left-≤-max ℕOrder.left-≤-max))
    (≈metric-trans leftProduct rightProduct
      (boundedProductRegular x y)
      (normalized-product-congruent sx x sy y
        (shiftDyadicallyBounded-equivalent extraX x)
        (shiftDyadicallyBounded-equivalent extraY y))
      (widened-product-equivalent x y ex ey
        ℕOrder.right-≤-max ℕOrder.right-≤-max))

bounded-product-class-shift-invariant :
  (extraX extraY : ℕ) (x y : DyadicallyBoundedRegularCauchy) →
  SQ.[ boundedProductRegular
    (shiftDyadicallyBounded extraX x)
    (shiftDyadicallyBounded extraY y) ] ≡
  SQ.[ boundedProductRegular x y ]
bounded-product-class-shift-invariant extraX extraY x y =
  boundedWitnessProductClass-congruent
    {x = regular (shiftDyadicallyBounded extraX x)}
    {x′ = regular x}
    {y = regular (shiftDyadicallyBounded extraY y)}
    {y′ = regular y}
    (shiftDyadicallyBounded extraX x , refl) (x , refl)
    (shiftDyadicallyBounded extraY y , refl) (y , refl)
    (shiftDyadicallyBounded-equivalent extraX x)
    (shiftDyadicallyBounded-equivalent extraY y)

bounded-product-negate-right :
  (x y : DyadicallyBoundedRegularCauchy) →
  boundedProductRegular x (negateDyadicallyBounded y) ≈metric
  negateRegular (boundedProductRegular x y)
bounded-product-negate-right x y =
  pointwise-equivalent
    (boundedProductRegular x (negateDyadicallyBounded y))
    (negateRegular (boundedProductRegular x y))
    (λ n →
      Q.·Comm
        (approximation (regular x)
          (suc (radius-exponent x ℕ.+ radius-exponent y) ℕ.+ n))
        (Q.- approximation (regular y)
          (suc (radius-exponent x ℕ.+ radius-exponent y) ℕ.+ n)) ∙
      sym (ProductSignPaths.negative-product PreferredℚCommRing
        (approximation (regular y)
          (suc (radius-exponent x ℕ.+ radius-exponent y) ℕ.+ n))
        (approximation (regular x)
          (suc (radius-exponent x ℕ.+ radius-exponent y) ℕ.+ n))) ∙
      cong Q.-_ (Q.·Comm
        (approximation (regular y)
          (suc (radius-exponent x ℕ.+ radius-exponent y) ℕ.+ n))
        (approximation (regular x)
          (suc (radius-exponent x ℕ.+ radius-exponent y) ℕ.+ n))))

bounded-product-negate-left :
  (x y : DyadicallyBoundedRegularCauchy) →
  boundedProductRegular (negateDyadicallyBounded x) y ≈metric
  negateRegular (boundedProductRegular x y)
bounded-product-negate-left x y =
  pointwise-equivalent
    (boundedProductRegular (negateDyadicallyBounded x) y)
    (negateRegular (boundedProductRegular x y))
    (λ n → sym (ProductSignPaths.negative-product PreferredℚCommRing
      (approximation (regular x)
        (suc (radius-exponent x ℕ.+ radius-exponent y) ℕ.+ n))
      (approximation (regular y)
        (suc (radius-exponent x ℕ.+ radius-exponent y) ℕ.+ n))))

product-class-from-dominance-negate-right :
  (x y : RegularCauchy) →
  (dx : DyadicDominates (canonicalRadius x)) →
  (dy : DyadicDominates (canonicalRadius y)) →
  (dny : DyadicDominates (canonicalRadius (negateRegular y))) →
  productClassFromDominance x (negateRegular y) dx dny ≡
  -completion (productClassFromDominance x y dx dy)
product-class-from-dominance-negate-right x y dx dy dny =
  let boundedX = promote-regular-presentation-truncated x dx
      boundedY = promote-regular-presentation-truncated y dy
      boundedNegY = promote-regular-presentation-truncated (negateRegular y) dny
  in
  PT.rec (metric-candidate-isSet _ _)
    (λ px → PT.rec (metric-candidate-isSet _ _)
      (λ py →
        let pny : BoundedPresentation (negateRegular y)
            pny = negateDyadicallyBounded (fst py) ,
              cong negateRegular (snd py)
        in
        truncatedBoundedProductClass-from-presentations
          boundedX boundedNegY px pny ∙
        SQ.eq/ _ _ (bounded-product-negate-right (fst px) (fst py)) ∙
        sym (cong -completion_
          (truncatedBoundedProductClass-from-presentations
            boundedX boundedY px py)))
      boundedY)
    boundedX

completion-multiplication-negate-right :
  (arch : RationalDyadicArchimedean) →
  (a b : MetricCompletionCandidate) →
  completionMultiplication arch a (-completion b) ≡
  -completion (completionMultiplication arch a b)
completion-multiplication-negate-right arch = SQ.elimProp2
  (λ _ _ → metric-candidate-isSet _ _)
  (λ x y → product-class-from-dominance-negate-right x y
    (dominates-all arch (canonicalRadius x))
    (dominates-all arch (canonicalRadius y))
    (dominates-all arch (canonicalRadius (negateRegular y))))


product-class-from-dominance-commutative :
  (x y : RegularCauchy) →
  (dx : DyadicDominates (canonicalRadius x)) →
  (dy : DyadicDominates (canonicalRadius y)) →
  productClassFromDominance x y dx dy ≡
  productClassFromDominance y x dy dx
product-class-from-dominance-commutative x y dx dy =
  let boundedX = promote-regular-presentation-truncated x dx
      boundedY = promote-regular-presentation-truncated y dy
  in
  PT.rec (metric-candidate-isSet _ _)
    (λ px → PT.rec (metric-candidate-isSet _ _)
      (λ py →
        truncatedBoundedProductClass-from-presentations
          boundedX boundedY px py ∙
        SQ.eq/ _ _ (bounded-product-commutative (fst px) (fst py)) ∙
        sym (truncatedBoundedProductClass-from-presentations
          boundedY boundedX py px))
      boundedY)
    boundedX

completion-multiplication-commutative :
  (arch : RationalDyadicArchimedean) →
  (a b : MetricCompletionCandidate) →
  completionMultiplication arch a b ≡ completionMultiplication arch b a
completion-multiplication-commutative arch = SQ.elimProp2
  (λ _ _ → metric-candidate-isSet _ _)
  (λ x y → product-class-from-dominance-commutative x y
    (dominates-all arch (canonicalRadius x))
    (dominates-all arch (canonicalRadius y)))

preferred-completion-multiplication-commutative :
  (a b : MetricCompletionCandidate) →
  preferredCompletionMultiplication a b ≡
  preferredCompletionMultiplication b a
preferred-completion-multiplication-commutative =
  completion-multiplication-commutative preferredRationalDyadicArchimedean

completion-multiplication-distributive-left :
  (arch : RationalDyadicArchimedean) →
  (a b c : MetricCompletionCandidate) →
  completionMultiplication arch (a +completion b) c ≡
  completionMultiplication arch a c +completion
  completionMultiplication arch b c
completion-multiplication-distributive-left arch a b c =
  completion-multiplication-commutative arch (a +completion b) c ∙
  completion-multiplication-distributive-right arch c a b ∙
  cong₂ _+completion_
    (completion-multiplication-commutative arch c a)
    (completion-multiplication-commutative arch c b)

preferred-completion-multiplication-distributive-left :
  (a b c : MetricCompletionCandidate) →
  preferredCompletionMultiplication (a +completion b) c ≡
  preferredCompletionMultiplication a c +completion
  preferredCompletionMultiplication b c
preferred-completion-multiplication-distributive-left =
  completion-multiplication-distributive-left
    preferredRationalDyadicArchimedean

completion-multiplication-negate-left :
  (arch : RationalDyadicArchimedean) →
  (a b : MetricCompletionCandidate) →
  completionMultiplication arch (-completion a) b ≡
  -completion (completionMultiplication arch a b)
completion-multiplication-negate-left arch a b =
  completion-multiplication-commutative arch (-completion a) b ∙
  completion-multiplication-negate-right arch b a ∙
  cong -completion_ (completion-multiplication-commutative arch b a)

preferred-completion-multiplication-negate-right :
  (a b : MetricCompletionCandidate) →
  preferredCompletionMultiplication a (-completion b) ≡
  -completion (preferredCompletionMultiplication a b)
preferred-completion-multiplication-negate-right =
  completion-multiplication-negate-right preferredRationalDyadicArchimedean

preferred-completion-multiplication-negate-left :
  (a b : MetricCompletionCandidate) →
  preferredCompletionMultiplication (-completion a) b ≡
  -completion (preferredCompletionMultiplication a b)
preferred-completion-multiplication-negate-left =
  completion-multiplication-negate-left preferredRationalDyadicArchimedean

completion-negate-involutive : (a : MetricCompletionCandidate) →
  -completion (-completion a) ≡ a
completion-negate-involutive = SQ.elimProp
  (λ _ → metric-candidate-isSet _ _)
  (λ x → SQ.eq/ _ _
    (pointwise-equivalent
      (negateRegular (negateRegular x)) x
      (λ n → Q.-Invol (approximation x n))))

completion-multiplication-double-negate :
  (arch : RationalDyadicArchimedean) →
  (a b : MetricCompletionCandidate) →
  completionMultiplication arch (-completion a) (-completion b) ≡
  completionMultiplication arch a b
completion-multiplication-double-negate arch a b =
  completion-multiplication-negate-right arch (-completion a) b ∙
  cong -completion_ (completion-multiplication-negate-left arch a b) ∙
  completion-negate-involutive (completionMultiplication arch a b)

preferred-completion-multiplication-double-negate :
  (a b : MetricCompletionCandidate) →
  preferredCompletionMultiplication (-completion a) (-completion b) ≡
  preferredCompletionMultiplication a b
preferred-completion-multiplication-double-negate =
  completion-multiplication-double-negate preferredRationalDyadicArchimedean


bounded-presented-product-right-one :
  {x : RegularCauchy} →
  (px : BoundedPresentation x) →
  (pone : BoundedPresentation (constantCauchy 1)) →
  boundedProductRegular (fst px) (fst pone) ≈metric x
bounded-presented-product-right-one {x} (bx , bxPath) (bone , bonePath) =
  let depth = suc (radius-exponent bx ℕ.+ radius-exponent bone)
      product-to-shift :
        boundedProductRegular bx bone ≈metric iterateShift depth (regular bx)
      product-to-shift = pointwise-equivalent
        (boundedProductRegular bx bone) (iterateShift depth (regular bx))
        (λ n →
          cong₂ Q._·_ refl
            (cong (λ z → approximation z (depth ℕ.+ n)) bonePath) ∙
          Q.·IdR (approximation (regular bx) (depth ℕ.+ n)) ∙
          sym (iterateShift-approximation depth n (regular bx)))
  in
  ≈metric-trans (boundedProductRegular bx bone)
    (iterateShift depth (regular bx)) x product-to-shift
    (≈metric-trans (iterateShift depth (regular bx)) (regular bx) x
      (iterateShift-equivalent depth (regular bx))
      (path→metric (regular bx) x bxPath))

product-class-from-dominance-right-unit :
  (x : RegularCauchy) →
  (dx : DyadicDominates (canonicalRadius x)) →
  (done : DyadicDominates (canonicalRadius (constantCauchy 1))) →
  productClassFromDominance x (constantCauchy 1) dx done ≡ SQ.[ x ]
product-class-from-dominance-right-unit x dx done =
  let boundedX = promote-regular-presentation-truncated x dx
      boundedOne = promote-regular-presentation-truncated (constantCauchy 1) done
  in
  PT.rec (metric-candidate-isSet _ _)
    (λ px → PT.rec (metric-candidate-isSet _ _)
      (λ pone →
        truncatedBoundedProductClass-from-presentations
          boundedX boundedOne px pone ∙
        SQ.eq/ _ _ (bounded-presented-product-right-one px pone))
      boundedOne)
    boundedX

completion-multiplication-right-unit :
  (arch : RationalDyadicArchimedean) →
  (a : MetricCompletionCandidate) →
  completionMultiplication arch a (embedMetricℚ 1) ≡ a
completion-multiplication-right-unit arch = SQ.elimProp
  (λ _ → metric-candidate-isSet _ _)
  (λ x → product-class-from-dominance-right-unit x
    (dominates-all arch (canonicalRadius x))
    (dominates-all arch (canonicalRadius (constantCauchy 1))))

completion-multiplication-left-unit :
  (arch : RationalDyadicArchimedean) →
  (a : MetricCompletionCandidate) →
  completionMultiplication arch (embedMetricℚ 1) a ≡ a
completion-multiplication-left-unit arch a =
  completion-multiplication-commutative arch (embedMetricℚ 1) a ∙
  completion-multiplication-right-unit arch a

preferred-completion-multiplication-right-unit :
  (a : MetricCompletionCandidate) →
  preferredCompletionMultiplication a (embedMetricℚ 1) ≡ a
preferred-completion-multiplication-right-unit =
  completion-multiplication-right-unit preferredRationalDyadicArchimedean

preferred-completion-multiplication-left-unit :
  (a : MetricCompletionCandidate) →
  preferredCompletionMultiplication (embedMetricℚ 1) a ≡ a
preferred-completion-multiplication-left-unit =
  completion-multiplication-left-unit preferredRationalDyadicArchimedean

negativeOneCompletion : MetricCompletionCandidate
negativeOneCompletion = -completion (embedMetricℚ 1)

negativeOneCompletion-is-embedded :
  negativeOneCompletion ≡ embedMetricℚ (Q.- 1)
negativeOneCompletion-is-embedded = embedℚ-preserves-negation 1

completion-multiplication-right-negative-one :
  (arch : RationalDyadicArchimedean) →
  (a : MetricCompletionCandidate) →
  completionMultiplication arch a negativeOneCompletion ≡ -completion a
completion-multiplication-right-negative-one arch a =
  completion-multiplication-negate-right arch a (embedMetricℚ 1) ∙
  cong -completion_ (completion-multiplication-right-unit arch a)

completion-multiplication-left-negative-one :
  (arch : RationalDyadicArchimedean) →
  (a : MetricCompletionCandidate) →
  completionMultiplication arch negativeOneCompletion a ≡ -completion a
completion-multiplication-left-negative-one arch a =
  completion-multiplication-commutative arch negativeOneCompletion a ∙
  completion-multiplication-right-negative-one arch a

preferred-completion-multiplication-right-negative-one :
  (a : MetricCompletionCandidate) →
  preferredCompletionMultiplication a negativeOneCompletion ≡ -completion a
preferred-completion-multiplication-right-negative-one =
  completion-multiplication-right-negative-one preferredRationalDyadicArchimedean

preferred-completion-multiplication-left-negative-one :
  (a : MetricCompletionCandidate) →
  preferredCompletionMultiplication negativeOneCompletion a ≡ -completion a
preferred-completion-multiplication-left-negative-one =
  completion-multiplication-left-negative-one preferredRationalDyadicArchimedean

preferred-completion-multiplication-right-embedded-negative-one :
  (a : MetricCompletionCandidate) →
  preferredCompletionMultiplication a (embedMetricℚ (Q.- 1)) ≡
  -completion a
preferred-completion-multiplication-right-embedded-negative-one a =
  cong (preferredCompletionMultiplication a)
    (sym negativeOneCompletion-is-embedded) ∙
  preferred-completion-multiplication-right-negative-one a

preferred-completion-multiplication-left-embedded-negative-one :
  (a : MetricCompletionCandidate) →
  preferredCompletionMultiplication (embedMetricℚ (Q.- 1)) a ≡
  -completion a
preferred-completion-multiplication-left-embedded-negative-one a =
  cong (λ z → preferredCompletionMultiplication z a)
    (sym negativeOneCompletion-is-embedded) ∙
  preferred-completion-multiplication-left-negative-one a

bounded-presented-product-right-zero :
  {x : RegularCauchy} →
  (px : BoundedPresentation x) →
  (pzero : BoundedPresentation (constantCauchy 0)) →
  boundedProductRegular (fst px) (fst pzero) ≈metric constantCauchy 0
bounded-presented-product-right-zero (bx , bxPath) (bzero , bzeroPath) =
  pointwise-equivalent (boundedProductRegular bx bzero) (constantCauchy 0)
    (λ n →
      cong₂ Q._·_ refl
        (cong (λ z → approximation z
          (suc (radius-exponent bx ℕ.+ radius-exponent bzero) ℕ.+ n))
          bzeroPath) ∙
      Q.·AnnihilR (approximation (regular bx)
        (suc (radius-exponent bx ℕ.+ radius-exponent bzero) ℕ.+ n)))

product-class-from-dominance-right-zero :
  (x : RegularCauchy) →
  (dx : DyadicDominates (canonicalRadius x)) →
  (dzero : DyadicDominates (canonicalRadius (constantCauchy 0))) →
  productClassFromDominance x (constantCauchy 0) dx dzero ≡
  embedMetricℚ 0
product-class-from-dominance-right-zero x dx dzero =
  let boundedX = promote-regular-presentation-truncated x dx
      boundedZero = promote-regular-presentation-truncated
        (constantCauchy 0) dzero
  in
  PT.rec (metric-candidate-isSet _ _)
    (λ px → PT.rec (metric-candidate-isSet _ _)
      (λ pzero →
        truncatedBoundedProductClass-from-presentations
          boundedX boundedZero px pzero ∙
        SQ.eq/ _ _ (bounded-presented-product-right-zero px pzero))
      boundedZero)
    boundedX

completion-multiplication-right-zero :
  (arch : RationalDyadicArchimedean) →
  (a : MetricCompletionCandidate) →
  completionMultiplication arch a (embedMetricℚ 0) ≡ embedMetricℚ 0
completion-multiplication-right-zero arch = SQ.elimProp
  (λ _ → metric-candidate-isSet _ _)
  (λ x → product-class-from-dominance-right-zero x
    (dominates-all arch (canonicalRadius x))
    (dominates-all arch (canonicalRadius (constantCauchy 0))))

completion-multiplication-left-zero :
  (arch : RationalDyadicArchimedean) →
  (a : MetricCompletionCandidate) →
  completionMultiplication arch (embedMetricℚ 0) a ≡ embedMetricℚ 0
completion-multiplication-left-zero arch a =
  completion-multiplication-commutative arch (embedMetricℚ 0) a ∙
  completion-multiplication-right-zero arch a

preferred-completion-multiplication-right-zero :
  (a : MetricCompletionCandidate) →
  preferredCompletionMultiplication a (embedMetricℚ 0) ≡ embedMetricℚ 0
preferred-completion-multiplication-right-zero =
  completion-multiplication-right-zero preferredRationalDyadicArchimedean

preferred-completion-multiplication-left-zero :
  (a : MetricCompletionCandidate) →
  preferredCompletionMultiplication (embedMetricℚ 0) a ≡ embedMetricℚ 0
preferred-completion-multiplication-left-zero =
  completion-multiplication-left-zero preferredRationalDyadicArchimedean

record CompletionMultiplicativeLawFragment
  (multiply : MetricCompletionCandidate → MetricCompletionCandidate →
    MetricCompletionCandidate) : Type where
  field
    multiply-commutative : (a b : MetricCompletionCandidate) →
      multiply a b ≡ multiply b a
    multiply-right-unit : (a : MetricCompletionCandidate) →
      multiply a (embedMetricℚ 1) ≡ a
    multiply-left-unit : (a : MetricCompletionCandidate) →
      multiply (embedMetricℚ 1) a ≡ a
    multiply-right-zero : (a : MetricCompletionCandidate) →
      multiply a (embedMetricℚ 0) ≡ embedMetricℚ 0
    multiply-left-zero : (a : MetricCompletionCandidate) →
      multiply (embedMetricℚ 0) a ≡ embedMetricℚ 0
open CompletionMultiplicativeLawFragment public

completion-multiplicative-law-fragment :
  (arch : RationalDyadicArchimedean) →
  CompletionMultiplicativeLawFragment (completionMultiplication arch)
completion-multiplicative-law-fragment arch = record
  { multiply-commutative = completion-multiplication-commutative arch
  ; multiply-right-unit = completion-multiplication-right-unit arch
  ; multiply-left-unit = completion-multiplication-left-unit arch
  ; multiply-right-zero = completion-multiplication-right-zero arch
  ; multiply-left-zero = completion-multiplication-left-zero arch
  }

preferred-completion-multiplicative-law-fragment :
  CompletionMultiplicativeLawFragment preferredCompletionMultiplication
preferred-completion-multiplicative-law-fragment =
  completion-multiplicative-law-fragment preferredRationalDyadicArchimedean

preferred-multiplication-rational-associative : (q r s : Q.ℚ) →
  preferredCompletionMultiplication (embedMetricℚ q)
    (preferredCompletionMultiplication (embedMetricℚ r) (embedMetricℚ s)) ≡
  preferredCompletionMultiplication
    (preferredCompletionMultiplication (embedMetricℚ q) (embedMetricℚ r))
    (embedMetricℚ s)
preferred-multiplication-rational-associative q r s =
  cong (preferredCompletionMultiplication (embedMetricℚ q))
    (preferredCompletionMultiplication-preserves-rationals r s) ∙
  preferredCompletionMultiplication-preserves-rationals q (r Q.· s) ∙
  cong embedMetricℚ (Q.·Assoc q r s) ∙
  sym (preferredCompletionMultiplication-preserves-rationals (q Q.· r) s) ∙
  cong (λ z → preferredCompletionMultiplication z (embedMetricℚ s))
    (sym (preferredCompletionMultiplication-preserves-rationals q r))

preferred-multiplication-rational-distributive-right : (q r s : Q.ℚ) →
  preferredCompletionMultiplication (embedMetricℚ q)
    (embedMetricℚ r +completion embedMetricℚ s) ≡
  preferredCompletionMultiplication (embedMetricℚ q) (embedMetricℚ r)
    +completion
  preferredCompletionMultiplication (embedMetricℚ q) (embedMetricℚ s)
preferred-multiplication-rational-distributive-right q r s =
  cong (preferredCompletionMultiplication (embedMetricℚ q))
    (sym (embedℚ-preserves-sum r s)) ∙
  preferredCompletionMultiplication-preserves-rationals q (r Q.+ s) ∙
  cong embedMetricℚ (Q.·DistL+ q r s) ∙
  embedℚ-preserves-sum (q Q.· r) (q Q.· s) ∙
  cong₂ _+completion_
    (sym (preferredCompletionMultiplication-preserves-rationals q r))
    (sym (preferredCompletionMultiplication-preserves-rationals q s))

preferred-multiplication-rational-distributive-left : (q r s : Q.ℚ) →
  preferredCompletionMultiplication
    (embedMetricℚ q +completion embedMetricℚ r) (embedMetricℚ s) ≡
  preferredCompletionMultiplication (embedMetricℚ q) (embedMetricℚ s)
    +completion
  preferredCompletionMultiplication (embedMetricℚ r) (embedMetricℚ s)
preferred-multiplication-rational-distributive-left q r s =
  preferred-completion-multiplication-commutative
    (embedMetricℚ q +completion embedMetricℚ r) (embedMetricℚ s) ∙
  preferred-multiplication-rational-distributive-right s q r ∙
  cong₂ _+completion_
    (preferred-completion-multiplication-commutative
      (embedMetricℚ s) (embedMetricℚ q))
    (preferred-completion-multiplication-commutative
      (embedMetricℚ s) (embedMetricℚ r))

