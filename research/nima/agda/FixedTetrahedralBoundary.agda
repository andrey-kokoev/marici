{-# OPTIONS --safe --cubical --guardedness #-}
module FixedTetrahedralBoundary where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Equiv.Properties using (congEquiv)
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Path using (symIso)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import MarkedTetrahedronCoherence using (module Tetrahedra)
open import GradedBoundaryCoherence using (twisted-filler; marked-fillers-distinct)
open import PathIndexedExtension using (module PathYoneda; module FiberYoneda; module Parallel)
import RetainedComparisonStructure as Retained

module OnEdges {ℓ : Level} (A : Type ℓ) {x0 x1 x2 x3 : A}
  (edges : Tetrahedra.Edges A x0 x1 x2 x3) where
  module T = Tetrahedra.Over A edges

  -- The earlier missing-face horn is an instance of dependent path Yoneda,
  -- now allowing the interpreted type to depend on the missing face itself.
  module MissingFaceInterpretation (a : T.Face012) (b : T.Face123) (c : T.Face013) =
    FiberYoneda (T.route023 a) (T.right-route b c)

  -- ALL faces are parameters here, not variables moved by horn contraction.
  module OnFaces (a : T.Face012) (b : T.Face123) (c : T.Face013) (d : T.Face023) where
    Filler : Type ℓ
    Filler = T.Tetrahedron a b c d

    Comparison : Filler → Filler → Type ℓ
    Comparison s t = s ≡ t

    module Residual = Parallel T.Route (T.left-route a d) (T.right-route b c)

    grade-four-boundary : Filler → Filler → T.G.Boundary 4
    grade-four-boundary s t = T.globular-boundary a b c d , s , t

    grade-four-equivalence : (s t : Filler)
      → Comparison s t ≃ T.G.Fill 4 (grade-four-boundary s t)
    grade-four-equivalence s t = idEquiv _

    -- The four previous face descriptions lift to equivalences of comparison
    -- witnesses. These are chart changes, not an asserted vertex-rotation cycle.
    compare023 : (s t : Filler)
      → Comparison s t ≃ (equivFun (T.solve023 a b c d) s ≡ equivFun (T.solve023 a b c d) t)
    compare023 s t = congEquiv (T.solve023 a b c d)

    compare012 : (s t : Filler)
      → Comparison s t ≃ (equivFun (T.solve012 a b c d) s ≡ equivFun (T.solve012 a b c d) t)
    compare012 s t = congEquiv (T.solve012 a b c d)

    compare013 : (s t : Filler)
      → Comparison s t ≃ (equivFun (T.solve013 a b c d) s ≡ equivFun (T.solve013 a b c d) t)
    compare013 s t = congEquiv (T.solve013 a b c d)

    compare123 : (s t : Filler)
      → Comparison s t ≃ (equivFun (T.solve123 a b c d) s ≡ equivFun (T.solve123 a b c d) t)
    compare123 s t = congEquiv (T.solve123 a b c d)

    reverse-comparison : (s t : Filler) → Comparison s t ≃ (sym s ≡ sym t)
    reverse-comparison s t = congEquiv (isoToEquiv symIso)

    module At (base : Filler) where
      module Interpret = PathYoneda Filler base

      -- Only the second tetrahedral filler varies in this contraction.
      -- All four faces stay fixed, but fixing BOTH fillers is a different fiber.
      ComparisonPackage : Type ℓ
      ComparisonPackage = Σ[ t ∈ Filler ] Comparison base t

      comparison-package-contractible : isContr ComparisonPackage
      comparison-package-contractible = Interpret.based-contractible

      loop-classification : Filler ≃ Residual.Loops
      loop-classification = Residual.coordinates base

      fixed-boundary-uniqueness : isContr Filler ≃ isContr Residual.Loops
      fixed-boundary-uniqueness = Residual.uniqueness-criterion base

-- Concrete hostile against deleting the path argument from the universal
-- property. It is a universe-level test, not a claim of distinct tetrahedral
-- fillers at one fixed boundary.
module UniverseInterpret = PathYoneda (Type ℓ-zero) Bool

false-section : UniverseInterpret.Sections (λ X → X)
false-section = UniverseInterpret.extend (λ X → X) false

ordinary-value : false-section Bool refl ≡ false
ordinary-value = refl

twisted-value : false-section Bool twisted-filler ≡ true
twisted-value = refl

no-loop-erasure : (v : Bool)
  → ((p : Bool ≡ Bool) → false-section Bool p ≡ v) → ⊥
no-loop-erasure v law = false≢true
  (sym ordinary-value ∙ law refl ∙ sym (law twisted-filler) ∙ twisted-value)

-- Even a contractible based-comparison package does not imply that its
-- ambient fixed-endpoint path space is contractible.
module LoopComparison = PathYoneda (Bool ≡ Bool) refl

fixed-paths-not-contractible : isContr (Bool ≡ Bool) → ⊥
fixed-paths-not-contractible c = marked-fillers-distinct
  (isContr→isProp c refl twisted-filler)

-- Outward test against the original structure, not an identification of its
-- E-arrows with identity paths of P. The family q |-> (false = q) has a value
-- refl at false but cannot extend along the retained change false -> true.
no-naive-retained-extension :
  ((q : Retained.Example.P) → Retained.Example.E false q → (false ≡ q)) → ⊥
no-naive-retained-extension f = false≢true (f true Retained.change0)

no-native-path-realization :
  ((p q : Retained.Example.P) → Retained.Example.E p q → (p ≡ q)) → ⊥
no-native-path-realization f = no-naive-retained-extension (f false)
