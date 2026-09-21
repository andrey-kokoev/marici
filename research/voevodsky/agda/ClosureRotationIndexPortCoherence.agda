{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureRotationIndexPortCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (assoc; rUnit)
open import Cubical.Foundations.Path using (compPath→Square)
open import ClosureDependentEndpointNaturality using (module Along)
open import ClosureRotationAppendReduction using (module Reduction)

module IndexPorts (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module D = Reduction K Piece Boundary attachL attachR
  open D.G.G.A.N

  module Trees {a b c d e f : K}
    {u : Word a b} {v : Word c d} {w : Word e f}
    (p : Bracket u) (q : Bracket v) (r : Bracket w) where
    module T = D.Trees p q r
    module R = T.Indexed

    -- This is precisely the first segment of T.rotationSquare.
    reindexSquare : (x : Realize R.leftTree) →
      equivFun (normalize R.rightTree) (equivFun R.nativeEquivalence x) ≡
      T.W.returnIndex (equivFun (normalize R.nativeRight) (R.Raw.associate x))
    reindexSquare x = sym (fromPathP (λ i → equivFun (R.normalizationPath i)
      (transport-filler R.realizationPath (R.Raw.associate x) i)))

    module First (x : Piece a) where
      module N = Along (λ i → Realize (R.treePath i))
        (λ i → Normal (sym R.association i))
        (λ i → equivFun (R.normalizationPath i))
        (λ i → firstAt (R.treePath i) x)
      module B = N.Port (λ i → first (sym R.association i) x)
        (λ i → normalizeFirst (R.treePath i) x)

      port : equivFun R.nativeEquivalence (firstAt R.leftTree x) ≡ firstAt R.rightTree x
      port = N.endpoint

      before : T.W.returnIndex (equivFun (normalize R.nativeRight) (firstAt R.nativeRight x)) ≡
        first ((u ++ v) ++ w) x
      before = B.source ∙ fromPathP (λ i → first (sym R.association i) x)

      after : equivFun (normalize R.rightTree) (equivFun R.nativeEquivalence (firstAt R.leftTree x)) ≡
        first ((u ++ v) ++ w) x
      after = cong (equivFun (normalize R.rightTree)) port ∙ normalizeFirst R.rightTree x

      coherence : PathP (λ i → reindexSquare (firstAt R.leftTree x) i ≡ first ((u ++ v) ++ w) x)
        after before
      coherence i = compPath→Square
        (assoc N.frame (cong (equivFun (normalize R.rightTree)) port) B.target
          ∙ B.boundary ∙ rUnit before) (~ i)

    module Last (x : Piece f) where
      module N = Along (λ i → Realize (R.treePath i))
        (λ i → Normal (sym R.association i))
        (λ i → equivFun (R.normalizationPath i))
        (λ i → lastAt (R.treePath i) x)
      module B = N.Port (λ i → last (sym R.association i) x)
        (λ i → normalizeLast (R.treePath i) x)

      port : equivFun R.nativeEquivalence (lastAt R.leftTree x) ≡ lastAt R.rightTree x
      port = N.endpoint

      before : T.W.returnIndex (equivFun (normalize R.nativeRight) (lastAt R.nativeRight x)) ≡
        last ((u ++ v) ++ w) x
      before = B.source ∙ fromPathP (λ i → last (sym R.association i) x)

      after : equivFun (normalize R.rightTree) (equivFun R.nativeEquivalence (lastAt R.leftTree x)) ≡
        last ((u ++ v) ++ w) x
      after = cong (equivFun (normalize R.rightTree)) port ∙ normalizeLast R.rightTree x

      coherence : PathP (λ i → reindexSquare (lastAt R.leftTree x) i ≡ last ((u ++ v) ++ w) x)
        after before
      coherence i = compPath→Square
        (assoc N.frame (cong (equivFun (normalize R.rightTree)) port) B.target
          ∙ B.boundary ∙ rUnit before) (~ i)

-- Both ports are those of the actual reindexed native equivalence. These
-- cells handle index transport only; subtree factorization and the paired
-- word square still have to be composed with them.
