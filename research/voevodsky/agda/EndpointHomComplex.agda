{-# OPTIONS --safe --cubical --guardedness #-}
module EndpointHomComplex where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import HomComplexSigns

-- Coefficient realization of the endpoint-hull/localized-collar calculation.
-- Intended instance: R=Z[x1,x5,X,U], L=R[U^-1], y=X/U.
-- Regular and localized slots remain different types. No surjectivity of iota
-- or occurrence-variable inverse is assumed.
module Calculation {ℓ} (R L : CommRing ℓ)
  (iota : fst R → fst L)
  (iotaZero : iota (CommRingStr.0r (snd R)) ≡ CommRingStr.0r (snd L))
  (iotaOne : iota (CommRingStr.1r (snd R)) ≡ CommRingStr.1r (snd L))
  (iotaAdd : (a b : fst R) → iota (CommRingStr._+_ (snd R) a b)
    ≡ CommRingStr._+_ (snd L) (iota a) (iota b))
  (iotaNeg : (a : fst R) → iota (CommRingStr.-_ (snd R) a)
    ≡ CommRingStr.-_ (snd L) (iota a))
  (iotaMul : (a b : fst R) → iota (CommRingStr._·_ (snd R) a b)
    ≡ CommRingStr._·_ (snd L) (iota a) (iota b))
  (x1 x5 : fst R) (y : fst L) where

  module RR = CommRingStr (snd R)
  open CommRingStr (snd L)
  A = fst R
  V = fst L
  a1 = iota x1
  a5 = iota x5

  difference : A → A → A
  difference a b = a RR.+ (RR.- b)

  iotaDifference : (a b : A) → iota (difference a b) ≡ iota a + (- iota b)
  iotaDifference a b = iotaAdd a (RR.- b) ∙ cong (λ t → iota a + t) (iotaNeg b)

  iotaWeightedDifference : (a b : A)
    → iota (difference (x1 RR.· a) (x5 RR.· b))
      ≡ a1 · iota a + (- (a5 · iota b))
  iotaWeightedDifference a b =
    iotaDifference (x1 RR.· a) (x5 RR.· b)
    ∙ (λ i → iotaMul x1 a i + (- iotaMul x5 b i))

  -- Actual source P2=R, P1=R^2, P0=R; B retains P1 and P0.
  sourceD2 : A → Σ A (λ _ → A)
  sourceD2 c = (RR.- (x1 RR.· c)) , (x5 RR.· c)

  sourceD1 : Σ A (λ _ → A) → A
  sourceD1 (b , c) = (x5 RR.· b) RR.+ (x1 RR.· c)

  sourceSquared : (c : A) → sourceD1 (sourceD2 c) ≡ RR.0r
  sourceSquared c = solve! R

  -- Actual target C3=R^2, C2=L; all other target degrees vanish.
  targetD3 : Σ A (λ _ → A) → V
  targetD3 (a , b) = y · iota a + iota b

  record M3 : Type ℓ where
    constructor m3
    field topA topB : A
  record M2 : Type ℓ where
    constructor m2
    field A0 B0 A2 B2 : A
          aug : V
  record M1 : Type ℓ where
    constructor m1
    field topK topN : A
          end0 end2 : V
  record N1 : Type ℓ where
    constructor n1
    field end0 end2 : V

  -- Subscripts denote minus the Hom cochain degree: M3 is Hom^-3.
  d3 : M3 → M2
  d3 (m3 a b) = m2 (x5 RR.· a) (x5 RR.· b)
    (x1 RR.· a) (x1 RR.· b) (y · iota a + iota b)

  d2 : M2 → M1
  d2 (m2 a b c d z) =
    m1 (difference (x1 RR.· a) (x5 RR.· c))
       (difference (x1 RR.· b) (x5 RR.· d))
       (y · iota a + iota b + (- (a5 · z)))
       (y · iota c + iota d + (- (a1 · z)))

  d1 : M1 → V
  d1 (m1 a b c d) = y · iota a + iota b + (- (a1 · c)) + a5 · d

  restrict1 : M1 → N1
  restrict1 (m1 a b c d) = n1 c d

  boundaryD2 : M2 → N1
  boundaryD2 t = restrict1 (d2 t)

  zeroM1 : M1
  zeroM1 = m1 RR.0r RR.0r 0r 0r

  d1d2 : (t : M2) → d1 (d2 t) ≡ 0r
  d1d2 (m2 a b c d z) =
    (λ i → y · iotaWeightedDifference a c i
      + iotaWeightedDifference b d i
      + (- (a1 · (y · iota a + iota b + (- (a5 · z)))))
      + a5 · (y · iota c + iota d + (- (a1 · z))))
    ∙ (solve! L)

  d2d3 : (t : M3) → d2 (d3 t) ≡ zeroM1
  d2d3 (m3 a b) = λ i → m1 (regA i) (regB i) (loc0 i) (loc2 i)
    where
    regA : difference (x1 RR.· (x5 RR.· a)) (x5 RR.· (x1 RR.· a)) ≡ RR.0r
    regA = solve! R
    regB : difference (x1 RR.· (x5 RR.· b)) (x5 RR.· (x1 RR.· b)) ≡ RR.0r
    regB = solve! R
    loc0 : y · iota (x5 RR.· a) + iota (x5 RR.· b)
      + (- (a5 · (y · iota a + iota b))) ≡ 0r
    loc0 = (λ i → y · iotaMul x5 a i + iotaMul x5 b i
      + (- (a5 · (y · iota a + iota b)))) ∙ (solve! L)
    loc2 : y · iota (x1 RR.· a) + iota (x1 RR.· b)
      + (- (a1 · (y · iota a + iota b))) ≡ 0r
    loc2 = (λ i → y · iotaMul x1 a i + iotaMul x1 b i
      + (- (a1 · (y · iota a + iota b)))) ∙ (solve! L)

  restrictionChainLaw : (t : M2) → restrict1 (d2 t) ≡ boundaryD2 t
  restrictionChainLaw t = refl

  boundarySquared : (t : M3) → boundaryD2 (d3 t) ≡ n1 0r 0r
  boundarySquared t = cong restrict1 (d2d3 t)

  -- The minus-one sign is odd; the source contribution is added.
  minusOneDifferentialSign : (a b : A) (c d : V)
    → d1 (m1 a b c d)
      ≡ Signs.homBoundary L odd (y · iota a + iota b)
        ((- (a1 · c)) + a5 · d)
  minusOneDifferentialSign a b c d = solve! L

  unitPrimitive : M1
  unitPrimitive = m1 RR.0r RR.1r 0r 0r

  unitPrimitiveLaw : d1 unitPrimitive ≡ 1r
  unitPrimitiveLaw = (λ i → y · iotaZero i + iotaOne i
    + (- (a1 · 0r)) + a5 · 0r) ∙ (solve! L)

  unitPrimitiveRestriction : restrict1 unitPrimitive ≡ n1 0r 0r
  unitPrimitiveRestriction = refl

  -- The supplied connector pair is an INPUT, never selected by endpoint maps.
  invariantRepresentative : V → N1 → V
  invariantRepresentative f (n1 h0 h2) = f + a1 · h0 + (- (a5 · h2))

  -- Quotient as an additive coset type: K=iota(R)+y*iota(R), NOT an L-ideal.
  data Residue : Type ℓ where
    residue : V → Residue
    regularRelation : (v : V) (a b : A)
      → residue (v + (y · iota a + iota b)) ≡ residue v
    residueSet : isSet Residue

  relativeClass : V → N1 → Residue
  relativeClass f h = residue (invariantRepresentative f h)

  zeroClass : Residue
  zeroClass = residue 0r

  -- Computed class for the ACTUAL f(e)=p attachment, for any prescribed h.
  unitRelativeClass : (h0 h2 : V)
    → relativeClass 1r (n1 h0 h2) ≡ residue (a1 · h0 + (- (a5 · h2)))
  unitRelativeClass h0 h2 = cong residue rearrange
    ∙ regularRelation (a1 · h0 + (- (a5 · h2))) RR.0r RR.1r
    where
    rearrange : 1r + a1 · h0 + (- (a5 · h2))
      ≡ (a1 · h0 + (- (a5 · h2))) + (y · iota RR.0r + iota RR.1r)
    rearrange = (solve! L) ∙ sym (λ i →
      (a1 · h0 + (- (a5 · h2))) + (y · iotaZero i + iotaOne i))

  zeroConnectorClass : relativeClass 1r (n1 0r 0r) ≡ zeroClass
  zeroConnectorClass = unitRelativeClass 0r 0r ∙ cong residue zeroWeighted
    where
    zeroWeighted : a1 · 0r + (- (a5 · 0r)) ≡ 0r
    zeroWeighted = solve! L

  -- Boundary of a relative primitive (s,0), with the sign convention
  -- D(s,t)=(d_M s, r(s)-d_N t).
  primitiveInvariant : (s : M1)
    → invariantRepresentative (d1 s) (restrict1 s)
      ≡ y · iota (M1.topK s) + iota (M1.topN s)
  primitiveInvariant (m1 a b c d) = solve! L

  primitiveClassZero : (s : M1) → relativeClass (d1 s) (restrict1 s) ≡ zeroClass
  primitiveClassZero (m1 a b c d) =
    cong residue (primitiveInvariant (m1 a b c d))
    ∙ cong residue (sym (plusZero (y · iota a + iota b)))
    ∙ regularRelation 0r a b
    where
    plusZero : (v : V) → 0r + v ≡ v
    plusZero v = solve! L

  -- A supplied decomposition in K constructs the actual framed primitive.
  fillFromDecomposition : (f : V) (h : N1) (a b : A)
    → invariantRepresentative f h ≡ y · iota a + iota b
    → Σ M1 (λ s → Σ (d1 s ≡ f) (λ _ → restrict1 s ≡ h))
  fillFromDecomposition f (n1 h0 h2) a b equation =
    m1 a b h0 h2 ,
    ((cong (λ v → v + (- (a1 · h0)) + a5 · h2) (sym equation)
      ∙ (solve! L)) , refl)

  addRestrictedPrimitive : (h : N1) → M1 → N1
  addRestrictedPrimitive (n1 h0 h2) (m1 a b c d) = n1 (h0 + c) (h2 + d)

  relativeBoundaryInvariance : (f : V) (h : N1) (s : M1)
    → relativeClass (f + d1 s) (addRestrictedPrimitive h s) ≡ relativeClass f h
  relativeBoundaryInvariance f (n1 h0 h2) (m1 a b c d) =
    cong residue rearrange ∙ regularRelation
      (invariantRepresentative f (n1 h0 h2)) a b
    where
    rearrange : invariantRepresentative (f + d1 (m1 a b c d))
        (addRestrictedPrimitive (n1 h0 h2) (m1 a b c d))
      ≡ invariantRepresentative f (n1 h0 h2) + (y · iota a + iota b)
    rearrange = solve! L

  -- Higher endpoint changes alter the invariant only by a regular relation.
  endpointChange : (h : N1) (t : M2) → N1
  endpointChange (n1 h0 h2) t = n1
    (h0 + N1.end0 (boundaryD2 t)) (h2 + N1.end2 (boundaryD2 t))

  endpointChangeFormula : (f : V) (h : N1) (t : M2)
    → invariantRepresentative f (endpointChange h t)
      ≡ invariantRepresentative f h
        + (y · iota (M1.topK (d2 t)) + iota (M1.topN (d2 t)))
  endpointChangeFormula f (n1 h0 h2) (m2 a b c d z) =
    (solve! L) ∙ sym (λ i →
      (f + a1 · h0 + (- (a5 · h2)))
      + (y · iotaWeightedDifference a c i + iotaWeightedDifference b d i))

  higherConnectorInvariance : (f : V) (h : N1) (t : M2)
    → relativeClass f (endpointChange h t) ≡ relativeClass f h
  higherConnectorInvariance f h t =
    cong residue (endpointChangeFormula f h t)
    ∙ regularRelation (invariantRepresentative f h)
      (M1.topK (d2 t)) (M1.topN (d2 t))
