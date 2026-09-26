{-# OPTIONS --safe --cubical --guardedness #-}
module NormalizationComparisonBasis where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (isContr→isContrPath)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import WholeHistoryComparisons as Comparisons
import DependentResolutionAlgebra as Interpretation

module Basis (ℓ : Level) where
  open Whole.Universe ℓ
  open Resolution.Generators ℓ
  module A = Interpretation.Interpretation ℓ
  module C = Comparisons.Comparisons ℓ A.Seed
  module O = C.Interpreted A.algebra

  canonical-seed : (q : Complete) → A.Seed q
  canonical-seed q = A.H.next {R = A.H.normal (expression q)}
    (A.H.normalize-map (expression q)) A.H.stop

  canonical : (q : Complete) → Resolve A.Seed q
  canonical q = seed (canonical-seed q)

  canonical-children : (r : Rule) → (i : Arity r) → Resolve A.Seed (input r i)
  canonical-children r i = canonical (input r i)

  carrier-contractible : (q : Complete) → isContr (A.U.Algebra.Carrier A.algebra q)
  carrier-contractible q =
    lift (fst h) , (λ f t → lift (snd h (lower f) t))
    where
    h = A.H.map-contractible (expression q)
      (A.H.original (expression q)) (A.H.normal (expression q))

  semantic-contractible : {q : Complete} (d e : Resolve A.Seed q) → isContr (O.Semantic d e)
  semantic-contractible {q} d e = isContr→isContrPath (carrier-contractible q)
    (A.U.evaluate A.algebra d) (A.U.evaluate A.algebra e)

  -- Exactly two law schemas. Neither constructor accepts a semantic path.
  -- The rule schema mentions ONLY canonical children, not arbitrary trees.
  data Law : (q : Complete) → Resolve A.Seed q → Resolve A.Seed q → Type (ℓ-suc ℓ) where
    seed-normalization : (q : Complete) (s : A.Seed q)
      → Law q (seed s) (canonical q)
    rule-normalization : (r : Rule)
      → Law (output r) (apply r (canonical-children r)) (canonical (output r))

  interpret-law : (q : Complete) (d e : Resolve A.Seed q) → Law q d e → O.Semantic d e
  interpret-law q d e (seed-normalization _ _) = fst (semantic-contractible d e)
  interpret-law q d e (rule-normalization _) = fst (semantic-contractible d e)

  module G = O.Structural Law interpret-law

  reduce : {q : Complete} (d : Resolve A.Seed q) → G.Generated d (canonical q)
  reduce (seed {q} s) = G.law (seed-normalization q s)
  reduce (apply r ds) = G.concatenate
    (G.congruence r ds (canonical-children r) (λ i → reduce (ds i)))
    (G.law (rule-normalization r))

  compare : {q : Complete} (d e : Resolve A.Seed q) → G.Generated d e
  compare d e = G.concatenate (reduce d) (G.invert (reduce e))

  -- Completeness concerns the actual supplied witness, not just endpoints.
  completeness : G.Completeness
  completeness q d e p = compare d e ,
    isContr→isProp (semantic-contractible d e) (G.sound (compare d e)) p

  -- Comparisons of witnesses are coherent as well, at every iterated level.
  higher-contractible : {q : Complete} (d e : Resolve A.Seed q)
    (p r : O.Semantic d e) → isContr (p ≡ r)
  higher-contractible d e = isContr→isContrPath (semantic-contractible d e)

  record Requested : Type (ℓ-suc ℓ) where
    constructor requested
    field
      endpoint : Complete
      left right : Resolve A.Seed endpoint
      witness : O.Semantic left right
      derivation : G.Generated left right
      reconstructs : G.sound derivation ≡ witness

  realize : {q : Complete} (d e : Resolve A.Seed q) → O.Semantic d e → Requested
  realize {q} d e p = requested q d e p (fst result) (snd result)
    where
    result = completeness q d e p

  next-Q : Requested → Whole.Universe.Complete (ℓ-suc ℓ)
  next-Q r = Whole.Universe.pack (Whole.Universe.atom Requested) r
