{-# OPTIONS --safe --cubical --guardedness #-}
module SeedNativePromotionBindingGate where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
import ActualSeedEndpointTable as Seed
import TableFibrationCycle as Table
import SeedTetrahedronBridge as Bridge
import SeedFaceObstruction as Obstruction
import SeedSeamPathComparisonBoundary as Questions

-- Use the actual six-occurrence table, not a numerical or filled fixture.
source-table = Seed.seed
source-index-recovery = Seed.source-recovery
target-index-recovery = Table.restore-correct Seed.seed Table.to-column

module C = Bridge.C
module At = C.Over Bridge.vertices

-- Exact boundary required before the inspected filled-tetrahedron feedback
-- adapter can run. A surface already suffices for the obstruction; the
-- tetrahedral filler is not the first missing piece.
SourceSurface : Type
SourceSurface = Σ[ s ∈ At.Surface ] (At.Surface.edges s ≡ Bridge.skeleton)

surface-forward : SourceSurface → Bridge.ForwardFace
surface-forward (s , same) = subst C.T.Over.Face012 same (At.Surface.face012 s)

surface-abc : SourceSurface → Bridge.TriangleABC
surface-abc (s , same) = subst C.T.Over.Face023 same (At.Surface.face023 s)

no-source-surface : SourceSurface → ⊥
no-source-surface s = Obstruction.no-forward-face (surface-forward s)

no-source-surface-abc : SourceSurface → ⊥
no-source-surface-abc s = Obstruction.no-abc-face (surface-abc s)

SourceHorn : Type
SourceHorn = Σ[ h ∈ At.Horn ] (At.Horn.edges h ≡ Bridge.skeleton)

no-source-horn : SourceHorn → ⊥
no-source-horn (h , same) = Obstruction.no-forward-face
  (subst C.T.Over.Face012 same (At.Horn.face012 h))

SourcePackage : Type
SourcePackage = Σ[ p ∈ At.Package ] (At.Surface.edges (fst p) ≡ Bridge.skeleton)

no-source-package : SourcePackage → ⊥
no-source-package (p , same) = no-source-surface (fst p , same)

-- Allow a propositional vertex identification, not just definitionally
-- fixed vertices. Transport the actual package before comparing edges.
SourceFull : Type
SourceFull = Σ[ p ∈ C.Full ] Σ[ same-vertices ∈ (fst p ≡ Bridge.vertices) ]
  (At.Surface.edges (fst (subst C.Over.Package same-vertices (snd p))) ≡ Bridge.skeleton)

no-source-full : SourceFull → ⊥
no-source-full (p , same-vertices , same-edges) = no-source-package
  (subst C.Over.Package same-vertices (snd p) , same-edges)

-- The existing spine control is inhabited, but does NOT bind the supplied
-- edge skeleton. Its changed diagonal cannot be hidden by its filler.
spine-not-source : Bridge.spine-edges ≡ Bridge.skeleton → ⊥
spine-not-source same = no-source-horn (Bridge.spine-horn , same)

-- What IS already source-inhabited: retained parallel-path questions.
-- No equality between their direct and indirect paths is asserted here.
forward-question : Questions.ForwardQuestion
forward-question = Questions.forward-boundary

return-question : Questions.ReturnQuestion
return-question = Questions.return-boundary

forward-paths-remain-distinct : Questions.ForwardQuestion.direct forward-question
  ≡ Questions.ForwardQuestion.indirect forward-question → ⊥
forward-paths-remain-distinct = Questions.forward-distinct

return-paths-remain-distinct : Questions.ReturnQuestion.direct return-question
  ≡ Questions.ReturnQuestion.indirect return-question → ⊥
return-paths-remain-distinct = Questions.return-distinct

-- Scope: this rejects the specified source-preserving binding in the FREE
-- path realization. It neither rejects native feedback on a different
-- admitted payload nor invents the intended T9 on the question objects.
