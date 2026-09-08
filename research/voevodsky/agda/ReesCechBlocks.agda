{-# OPTIONS --safe --cubical --guardedness #-}
module ReesCechBlocks where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import ReesTwoChartMonomials

-- Differential convention: u-chart restriction minus X-chart restriction.
data ChartKind : Type where
  xOnly uOnly common : ChartKind

kindOf : (m : OverlapMonomial) → ChartCover m → ChartKind
kindOf _ (negativeU a j) = uOnly
kindOf _ (nonnegative a n (onlyX gap equation)) = xOnly
kindOf _ (nonnegative a n (both k equation)) = common

monomialKind : OverlapMonomial → ChartKind
monomialKind m = kindOf m (coverEveryMonomial m)

module Block {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  Carrier = fst R

  C0 : ChartKind → Type ℓ
  C0 xOnly = Carrier
  C0 uOnly = Carrier
  C0 common = Σ Carrier (λ _ → Carrier)

  zeroV : (k : ChartKind) → C0 k
  zeroV xOnly = 0r
  zeroV uOnly = 0r
  zeroV common = 0r , 0r

  addV : (k : ChartKind) → C0 k → C0 k → C0 k
  addV xOnly a b = a + b
  addV uOnly a b = a + b
  addV common (a , b) (c , d) = (a + c) , (b + d)

  differential : (k : ChartKind) → C0 k → Carrier
  differential xOnly a = - a
  differential uOnly b = b
  differential common (a , b) = b + (- a)

  homotopy : (k : ChartKind) → Carrier → C0 k
  homotopy xOnly c = - c
  homotopy uOnly c = c
  homotopy common c = 0r , c

  -- This is a coefficient-block trace, NOT an S-linear projection of the
  -- geometric Cech complex. Multiplication by X,u can change the block kind.
  trace : (k : ChartKind) → C0 k → Carrier
  trace xOnly _ = 0r
  trace uOnly _ = 0r
  trace common (a , b) = a

  include : (k : ChartKind) → Carrier → C0 k
  include xOnly _ = 0r
  include uOnly _ = 0r
  include common c = c , c

  dH : (k : ChartKind) (c : Carrier) → differential k (homotopy k c) ≡ c
  dH xOnly c = solve! R
  dH uOnly c = refl
  dH common c = solve! R

  HdPlusProjection : (k : ChartKind) (v : C0 k)
    → addV k (homotopy k (differential k v)) (include k (trace k v)) ≡ v
  HdPlusProjection xOnly v = solve! R
  HdPlusProjection uOnly v = solve! R
  HdPlusProjection common (a , b) = λ i → left i , right i
    where
    left : 0r + a ≡ a
    left = solve! R
    right : (b + (- a)) + a ≡ b
    right = solve! R

  dInclude : (k : ChartKind) (c : Carrier) → differential k (include k c) ≡ 0r
  dInclude xOnly c = solve! R
  dInclude uOnly c = refl
  dInclude common c = solve! R

  traceHomotopy : (k : ChartKind) (c : Carrier) → trace k (homotopy k c) ≡ 0r
  traceHomotopy xOnly c = refl
  traceHomotopy uOnly c = refl
  traceHomotopy common c = refl

  commonTraceInclude : (c : Carrier) → trace common (include common c) ≡ c
  commonTraceInclude c = refl

  -- Degree-one differential is zero: these are two-term Cech complexes.
  nextDifferential : Carrier → Carrier
  nextDifferential _ = 0r

  dSquared : (k : ChartKind) (v : C0 k)
    → nextDifferential (differential k v) ≡ 0r
  dSquared k v = refl

  -- Specialization to every exponent descriptor uses the proved cover.
  monomialSurjectivity : (m : OverlapMonomial) (c : Carrier)
    → differential (monomialKind m) (homotopy (monomialKind m) c) ≡ c
  monomialSurjectivity m = dH (monomialKind m)

-- Actual coefficient-map hypotheses, not a postulated base-change square.
record CoefficientMap {ℓ ℓ'} (R : CommRing ℓ) (S : CommRing ℓ')
  : Type (ℓ-max ℓ ℓ') where
  private
    module R = CommRingStr (snd R)
    module S = CommRingStr (snd S)
  field
    map : fst R → fst S
    preservesZero : map R.0r ≡ S.0r
    preservesAdd : (a b : fst R) → map (a R.+ b) ≡ (map a S.+ map b)
    preservesNeg : (a : fst R) → map (R.- a) ≡ S.- (map a)

module CoefficientNaturality {ℓ ℓ'} {R : CommRing ℓ} {S : CommRing ℓ'}
  (f : CoefficientMap R S) where
  open CoefficientMap f
  module RB = Block R
  module SB = Block S
  module SO = CommRingStr (snd S)

  mapV : (k : ChartKind) → RB.C0 k → SB.C0 k
  mapV xOnly a = map a
  mapV uOnly b = map b
  mapV common (a , b) = map a , map b

  differentialNatural : (k : ChartKind) (v : RB.C0 k)
    → map (RB.differential k v) ≡ SB.differential k (mapV k v)
  differentialNatural xOnly a = preservesNeg a
  differentialNatural uOnly b = refl
  differentialNatural common (a , b) =
    preservesAdd b (CommRingStr.-_ (snd R) a)
      ∙ cong (λ c → map b SO.+ c) (preservesNeg a)

  homotopyNatural : (k : ChartKind) (c : fst R)
    → mapV k (RB.homotopy k c) ≡ SB.homotopy k (map c)
  homotopyNatural xOnly c = preservesNeg c
  homotopyNatural uOnly c = refl
  homotopyNatural common c = λ i → preservesZero i , map c

  traceNatural : (k : ChartKind) (v : RB.C0 k)
    → map (RB.trace k v) ≡ SB.trace k (mapV k v)
  traceNatural xOnly v = preservesZero
  traceNatural uOnly v = preservesZero
  traceNatural common v = refl

  includeNatural : (k : ChartKind) (c : fst R)
    → mapV k (RB.include k c) ≡ SB.include k (map c)
  includeNatural xOnly c = preservesZero
  includeNatural uOnly c = preservesZero
  includeNatural common c = refl

-- Assemble any declared family of blocks, with no finite-cutoff inference.
-- This is a product of coefficient blocks; identifying a finite-support
-- polynomial direct sum or a sheaf Cech model is a separate construction.
module Families {ℓ ℓ'} (R : CommRing ℓ) (Index : Type ℓ')
  (kind : Index → ChartKind) where
  module B = Block R

  DegreeZero = (i : Index) → B.C0 (kind i)
  DegreeOne = Index → fst R

  d : DegreeZero → DegreeOne
  d v i = B.differential (kind i) (v i)

  H : DegreeOne → DegreeZero
  H c i = B.homotopy (kind i) (c i)

  projection : DegreeZero → DegreeZero
  projection v i = B.include (kind i) (B.trace (kind i) (v i))

  addZero : DegreeZero → DegreeZero → DegreeZero
  addZero v w i = B.addV (kind i) (v i) (w i)

  dHIdentity : (c : DegreeOne) → d (H c) ≡ c
  dHIdentity c = funExt λ i → B.dH (kind i) (c i)

  contraction : (v : DegreeZero) → addZero (H (d v)) (projection v) ≡ v
  contraction v = funExt λ i → B.HdPlusProjection (kind i) (v i)

-- The additive coefficient-change theorem above is not geometric proper
-- duality base change, derived tensor base change, or an S-linear trace roof.
