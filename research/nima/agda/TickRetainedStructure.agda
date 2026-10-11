{-# OPTIONS --safe --cubical --guardedness #-}
module TickRetainedStructure where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Isomorphism using (Iso; isoToEquiv)
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.Bool.Properties using (notEquiv; isSetBool)
open import Cubical.Data.Sigma.Base using (_×_)
import RetainedSquareConeClock as Clock
import TickDiscreteReadout as Readout

-- A dependent section over the fixed cubical square is determined, up to
-- path equality, by its value at (1,1). No boundary edges are held fixed
-- here: the section is an unrestricted field of RetainedReturn.
module SectionExt {ℓ : Level} (A : I → I → Type ℓ) where
  Section : Type ℓ
  Section = (i j : I) → A i j

  section-ext : (f g : Section) → f i1 i1 ≡ g i1 i1 → f ≡ g
  section-ext f g corner k i j = pointwise i j k
    where
    pointwise : (i j : I) → f i j ≡ g i j
    pointwise i j =
      sym (fromPathP (λ t → f (i ∨ ~ t) (j ∨ ~ t)))
      ∙ cong (transport (λ t → A (i ∨ ~ t) (j ∨ ~ t))) corner
      ∙ fromPathP (λ t → g (i ∨ ~ t) (j ∨ ~ t))

module T = Clock.Bridge Bool Bool notEquiv
module G = T.G
module R = T.Return
module S = SectionExt R.backward-cell

pair-set : isSet (Bool × Bool)
pair-set = isSet× isSetBool isSetBool

run-normal : (r : G.Schedule) (q : Bool × Bool) → G.run r q ≡ G.run G.leftFirst q
run-normal G.leftFirst q = refl
run-normal G.rightFirst q = refl

module AtSource (s : Bool × Bool) where
  module A = T.AtSource s

  tags : A.Tick → G.Schedule × G.Schedule
  tags t = G.ComparedRoutes.first cmp , G.ComparedRoutes.second cmp
    where
    cmp = G.RealizedSquare.comparison (R.RetainedReturn.original (A.Tick.returned t))

  -- Full record equality, including the entire dependent return section
  -- and every witness field, from equality of the ordered schedule tags.
  tags-injective : (t u : A.Tick) → tags t ≡ tags u → t ≡ u
  tags-injective t u same = tick-path
    where
    rt = A.Tick.returned t
    ru = A.Tick.returned u
    ot = R.RetainedReturn.original rt
    ou = R.RetainedReturn.original ru
    ct = G.RealizedSquare.comparison ot
    cu = G.RealizedSquare.comparison ou

    source-path : G.RealizedSquare.source ot ≡ G.RealizedSquare.source ou
    source-path = A.Tick.attachment t ∙ sym (A.Tick.attachment u)

    comparison-path : ct ≡ cu
    G.ComparedRoutes.first (comparison-path k) = fst (same k)
    G.ComparedRoutes.second (comparison-path k) = snd (same k)
    G.ComparedRoutes.witness (comparison-path k) =
      isProp→PathP (λ k → isSetΠ (λ _ → pair-set)
        (G.run (fst (same k))) (G.run (snd (same k))))
        (G.ComparedRoutes.witness ct) (G.ComparedRoutes.witness cu) k

    target-path : G.RealizedSquare.target ot ≡ G.RealizedSquare.target ou
    target-path = G.RealizedSquare.target-law ot
      ∙ cong₂ G.run (cong fst same) source-path
      ∙ sym (G.RealizedSquare.target-law ou)

    original-path : ot ≡ ou
    G.RealizedSquare.source (original-path k) = source-path k
    G.RealizedSquare.comparison (original-path k) = comparison-path k
    G.RealizedSquare.target (original-path k) = target-path k
    G.RealizedSquare.target-law (original-path k) =
      isProp→PathP (λ k → pair-set (target-path k)
        (G.run (fst (same k)) (source-path k)))
        (G.RealizedSquare.target-law ot) (G.RealizedSquare.target-law ou) k

    section-path : R.RetainedReturn.return-section rt ≡ R.RetainedReturn.return-section ru
    section-path = S.section-ext _ _
      (R.RetainedReturn.end-law rt ∙ source-path ∙ sym (R.RetainedReturn.end-law ru))

    return-path : rt ≡ ru
    R.RetainedReturn.original (return-path k) = original-path k
    R.RetainedReturn.return-section (return-path k) = section-path k
    R.RetainedReturn.start-law (return-path k) =
      isProp→PathP (λ k → pair-set (section-path k i0 i0) (target-path k))
        (R.RetainedReturn.start-law rt) (R.RetainedReturn.start-law ru) k
    R.RetainedReturn.end-law (return-path k) =
      isProp→PathP (λ k → pair-set (section-path k i1 i1) (source-path k))
        (R.RetainedReturn.end-law rt) (R.RetainedReturn.end-law ru) k

    tick-path : t ≡ u
    A.Tick.returned (tick-path k) = return-path k
    A.Tick.attachment (tick-path k) =
      isProp→PathP (λ k → pair-set (source-path k) s)
        (A.Tick.attachment t) (A.Tick.attachment u) k

  rebuild : G.Schedule × G.Schedule → A.Tick
  rebuild (r , q) = A.tick
    (R.retained-return
      (G.realized s
        (G.compared r q (funExt λ x → run-normal r x ∙ sym (run-normal q x)))
        (G.run G.leftFirst s) (sym (run-normal r s)))
      (R.backward-section s) refl refl) refl

  tags-rebuild : (rq : G.Schedule × G.Schedule) → tags (rebuild rq) ≡ rq
  tags-rebuild (r , q) = refl

  rebuild-tags : (t : A.Tick) → rebuild (tags t) ≡ t
  rebuild-tags t = tags-injective (rebuild (tags t)) t (tags-rebuild (tags t))

  tick-iso-tags : Iso A.Tick (G.Schedule × G.Schedule)
  Iso.fun tick-iso-tags = tags
  Iso.inv tick-iso-tags = rebuild
  Iso.rightInv tick-iso-tags = tags-rebuild
  Iso.leftInv tick-iso-tags = rebuild-tags

  tick-equiv-tags : A.Tick ≃ (G.Schedule × G.Schedule)
  tick-equiv-tags = isoToEquiv tick-iso-tags

  canonical-return-section : (t : A.Tick)
    → R.RetainedReturn.return-section (A.Tick.returned t) ≡ R.backward-section s
  canonical-return-section t = S.section-ext _ _
    (R.RetainedReturn.end-law (A.Tick.returned t) ∙ A.Tick.attachment t)

  -- Every ordinary type-theoretic observation of the full Tick factors
  -- through its tags. This is not a theorem selecting an analytic model.
  observation-factors : {ℓ′ : Level} {X : Type ℓ′} (observe : A.Tick → X)
    → (t : A.Tick) → observe t ≡ observe (rebuild (tags t))
  observation-factors observe t = cong observe (sym (rebuild-tags t))

  -- The existing extraction omits fields syntactically, but is injective
  -- on full Bool Tick records at a fixed source, up to path equality.
  module D = Readout.Readout notEquiv s

  readout-injective : (t u : A.Tick) → D.extract t ≡ D.extract u → t ≡ u
  readout-injective t u p = tags-injective t u
    (cong (λ d → D.DiscreteReadout.schedule-first d , D.DiscreteReadout.schedule-second d) p)

