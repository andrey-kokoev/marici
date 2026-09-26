{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverCoherenceCube where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (ua; uaβ; ua-gluePath)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (notEquiv; false≢true)
open import Cubical.Data.Empty.Base using (⊥)
import DependentSigmaPiCoherence as Ground
import WholePackageSigmaPi as Whole

-- A finite higher-groupoid fragment in the universe of types. The square
-- and cube are actual interval-indexed type families, not just edge counts.
module Geometry {ℓ : Level} (O R : Type ℓ) (e : O ≃ R) where
  expand : O → R
  expand = equivFun e
  axis : O ≡ R
  axis = ua e
  axis-computes : (u : O) → transport axis u ≡ expand u
  axis-computes = uaβ e
  square : I → I → Type ℓ
  square i j = axis i × axis j
  cube : I → I → I → Type ℓ
  cube i j k = axis i × (axis j × axis k)

  -- Actual source values extend to compatible sections of the whole cell.
  carry : (u : O) → PathP (λ i → axis i) u (expand u)
  carry u = ua-gluePath e refl
  square-section : O × O → (i j : I) → square i j
  square-section (u , v) i j = carry u i , carry v j
  cube-section : O × (O × O) → (i j k : I) → cube i j k
  cube-section (u , v , w) i j k = carry u i , carry v j , carry w k
  square-source : (u v : O) → square-section (u , v) i0 i0 ≡ (u , v)
  square-source u v = refl
  square-target : (u v : O) → square-section (u , v) i1 i1 ≡ (expand u , expand v)
  square-target u v = refl

  -- All square presentations have paths from the same origin.
  to10 : (O × O) ≡ (R × O)
  to10 i = square i i0
  to01 : (O × O) ≡ (O × R)
  to01 i = square i0 i
  to11 : (O × O) ≡ (R × R)
  to11 i = square i i

  -- The six faces are restrictions of ONE cube, fixing their shared edges.
  face000 : (j k : I) → cube i0 j k ≡ (O × (axis j × axis k))
  face000 j k = refl
  face100 : (j k : I) → cube i1 j k ≡ (R × (axis j × axis k))
  face100 j k = refl
  face010 : (i k : I) → cube i i0 k ≡ (axis i × (O × axis k))
  face010 i k = refl
  face110 : (i k : I) → cube i i1 k ≡ (axis i × (R × axis k))
  face110 i k = refl
  face001 : (i j : I) → cube i j i0 ≡ (axis i × (axis j × O))
  face001 i j = refl
  face111 : (i j : I) → cube i j i1 ≡ (axis i × (axis j × R))
  face111 i j = refl

  -- Retain the two schedules separately, even though their maps agree.
  data Schedule : Type where
    leftFirst rightFirst : Schedule
  expandLeft : O × O → R × O
  expandLeft (u , v) = expand u , v
  expandRight : O × O → O × R
  expandRight (u , v) = u , expand v
  finishRight : R × O → R × R
  finishRight (r , v) = r , expand v
  finishLeft : O × R → R × R
  finishLeft (u , r) = expand u , r
  run : Schedule → O × O → R × R
  run leftFirst uv = finishRight (expandLeft uv)
  run rightFirst uv = finishLeft (expandRight uv)
  route-homotopy : run leftFirst ≡ run rightFirst
  route-homotopy = refl
  tag : Schedule → Bool
  tag leftFirst = false
  tag rightFirst = true
  routes-distinct : leftFirst ≡ rightFirst → ⊥
  routes-distinct p = false≢true (cong tag p)
  record ComparedRoutes : Type ℓ where
    constructor compared
    field
      first second : Schedule
      witness : run first ≡ run second
  retainedSquare : ComparedRoutes
  retainedSquare = compared leftFirst rightFirst route-homotopy

  record RealizedSquare : Type ℓ where
    constructor realized
    field
      source : O × O
      comparison : ComparedRoutes
      target : R × R
      target-law : target ≡ run (ComparedRoutes.first comparison) source
  nextQ : O × O → Whole.Universe.Complete ℓ
  nextQ s = Whole.Universe.pack (Whole.Universe.atom RealizedSquare)
    (realized s retainedSquare (run leftFirst s) refl)
  recover-source : (s : O × O)
    → RealizedSquare.source (Whole.Universe.value (nextQ s)) ≡ s
  recover-source s = refl

-- Actual source: previous dependent EP/PE chains, with ALL intermediate
-- values and links. Restrict to their declared canonical traces, as in the
-- earlier free-observer construction. Arbitrary trace choices are not erased.
module FromSource {ℓ : Level}
  (I₀ : Type ℓ) (J : I₀ → Type ℓ)
  (K : (i : I₀) → J i → Type ℓ)
  (L : (i : I₀) (j : J i) → K i j → Type ℓ)
  (B : (i : I₀) (j : J i) (k : K i j) → L i j k → Type ℓ) where
  module S = Ground.Construction I₀ J K L B
  CanonicalTrace : Type ℓ
  CanonicalTrace = Σ[ q ∈ S.X ] Σ[ t ∈ S.Trace q ] (t ≡ S.canonicalTrace q)
  traceIso : Iso CanonicalTrace S.X
  Iso.fun traceIso = fst
  Iso.inv traceIso q = q , S.canonicalTrace q , refl
  Iso.rightInv traceIso q = refl
  Iso.leftInv traceIso (q , t , p) i = q , p (~ i) , (λ j → p (~ i ∨ j))

  Observer : Type ℓ
  Observer = CanonicalTrace × CanonicalTrace
  expansionIso : Iso Observer (S.X × S.X)
  Iso.fun expansionIso (u , v) = Iso.fun traceIso u , Iso.fun traceIso v
  Iso.inv expansionIso (x , y) = Iso.inv traceIso x , Iso.inv traceIso y
  Iso.rightInv expansionIso (x , y) i = Iso.rightInv traceIso x i , Iso.rightInv traceIso y i
  Iso.leftInv expansionIso (u , v) i = Iso.leftInv traceIso u i , Iso.leftInv traceIso v i
  module Cells = Geometry Observer (S.X × S.X) (isoToEquiv expansionIso)

  -- Attachment is independent of having a free observer vertex.
  Attach : Observer → Type ℓ
  Attach (u , v) = Iso.fun S.routeA (fst u) ≡ Iso.fun S.routeB (fst v)
  diagonal-attaches : (q : S.X) → Attach (Iso.inv expansionIso (q , q))
  diagonal-attaches = S.route-comparison

  AttachedObserver : Type ℓ
  AttachedObserver = Σ Observer Attach
  record AttachedSquare : Type ℓ where
    constructor attached-square
    field
      observers : AttachedObserver × AttachedObserver
      presentation : Cells.RealizedSquare
      source-link : Cells.RealizedSquare.source presentation
        ≡ (fst (fst observers) , fst (snd observers))
  nextAttachedQ : AttachedObserver × AttachedObserver → Whole.Universe.Complete ℓ
  nextAttachedQ s = Whole.Universe.pack (Whole.Universe.atom AttachedSquare)
    (attached-square s
      (Whole.Universe.value (Cells.nextQ (fst (fst s) , fst (snd s)))) refl)
  recover-attachments : (s : AttachedObserver × AttachedObserver)
    → AttachedSquare.observers (Whole.Universe.value (nextAttachedQ s)) ≡ s
  recover-attachments s = refl

-- Hostile to the inference "connected means every loop is filled".
-- An actual path in the type universe can have observable nontrivial transport.
twist : Bool ≡ Bool
twist = ua notEquiv
twist-not-refl : twist ≡ refl → ⊥
twist-not-refl p = false≢true
  (sym (uaβ notEquiv true)
   ∙ cong (λ path → transport path true) p
   ∙ transportRefl true)
