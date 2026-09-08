{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidFiller where

open import Cubical.Foundations.Prelude
open import DGPyramidBoundary

-- Degree-zero candidates and their boundary into Hom^1(J,F) are deliberately
-- separate from the boundary record, which remains filler-free.
record PyramidFrame {ℓ : Level} (P : DGPyramidBoundary {ℓ})
  : Type (ℓ-suc ℓ) where
  field
    JFzero : Type ℓ
    deltaFiller : JFzero → JFone P

    -- Four independent source-derived conditions. No implication among them
    -- is built into the interface.
    PreservesSupport : JFzero → Type ℓ
    PreservesEndpoints : JFzero → Type ℓ
    PreservesGenericQ : JFzero → Type ℓ
    PreservesReesCartier : JFzero → Type ℓ

open PyramidFrame public

-- Mathematical spelling of the bounded Hom⁰(J,F) supplied by a frame.
Hom⁰JF : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  (Frame : PyramidFrame P) → Type ℓ
Hom⁰JF = JFzero

-- Explicit conjunction without importing a product whose fields could hide
-- which physical condition failed.
PreservesFrame : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  (Frame : PyramidFrame P) → JFzero Frame → Type ℓ
PreservesFrame Frame K =
  Σ (PreservesSupport Frame K) λ _ →
  Σ (PreservesEndpoints Frame K) λ _ →
  Σ (PreservesGenericQ Frame K) λ _ →
      PreservesReesCartier Frame K

-- The requested framed homotopy fibre over the derived closed discrepancy.
-- Its equality is a boundary equation; it is not judgmental equality and it
-- does not imply any frame condition.
AdmissibleFiller : {ℓ : Level} (P : DGPyramidBoundary {ℓ})
  (Frame : PyramidFrame P) → Type ℓ
AdmissibleFiller P Frame =
  Σ (JFzero Frame) λ K →
  Σ (deltaFiller Frame K ≡ pyramidDiscrepancy P) λ _ →
      PreservesFrame Frame K

-- Checked expansion of the requested Σ-fibre spelling.
admissibleFillerShape : {ℓ : Level} (P : DGPyramidBoundary {ℓ})
  (Frame : PyramidFrame P) →
  AdmissibleFiller P Frame ≡
  (Σ (Hom⁰JF Frame) λ K →
    Σ (deltaFiller Frame K ≡ pyramidDiscrepancy P) λ _ →
      PreservesFrame Frame K)
admissibleFillerShape P Frame = refl

-- The unframed fibre is useful as a negative control: forgetting constraints
-- can create candidates but can never certify physical admissibility.
BoundaryFiller : {ℓ : Level} (P : DGPyramidBoundary {ℓ})
  (Frame : PyramidFrame P) → Type ℓ
BoundaryFiller P Frame =
  Σ (JFzero Frame) λ K → deltaFiller Frame K ≡ pyramidDiscrepancy P

forgetFrame : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  {Frame : PyramidFrame P} → AdmissibleFiller P Frame → BoundaryFiller P Frame
forgetFrame (K , boundary , conditions) = K , boundary

fillerCandidate : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  {Frame : PyramidFrame P} → AdmissibleFiller P Frame → JFzero Frame
fillerCandidate = fst

fillerBoundary : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  {Frame : PyramidFrame P} (filler : AdmissibleFiller P Frame)
  → deltaFiller Frame (fillerCandidate {P = P} {Frame = Frame} filler)
    ≡ pyramidDiscrepancy P
fillerBoundary filler = fst (snd filler)

fillerSupport : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  {Frame : PyramidFrame P} (filler : AdmissibleFiller P Frame)
  → PreservesSupport Frame (fillerCandidate {P = P} {Frame = Frame} filler)
fillerSupport filler = fst (snd (snd filler))

fillerEndpoints : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  {Frame : PyramidFrame P} (filler : AdmissibleFiller P Frame)
  → PreservesEndpoints Frame (fillerCandidate {P = P} {Frame = Frame} filler)
fillerEndpoints filler = fst (snd (snd (snd filler)))

fillerGenericQ : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  {Frame : PyramidFrame P} (filler : AdmissibleFiller P Frame)
  → PreservesGenericQ Frame (fillerCandidate {P = P} {Frame = Frame} filler)
fillerGenericQ filler = fst (snd (snd (snd (snd filler))))

fillerReesCartier : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  {Frame : PyramidFrame P} (filler : AdmissibleFiller P Frame)
  → PreservesReesCartier Frame
    (fillerCandidate {P = P} {Frame = Frame} filler)
fillerReesCartier filler = snd (snd (snd (snd (snd filler))))

-- A frame refinement transports an admissible filler only when every refined
-- condition is explicitly obtained. Equality of boundary equations is reused;
-- physical conditions are not transported automatically.
refineFrame : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  (Old New : PyramidFrame P)
  (candidateMap : JFzero Old → JFzero New)
  (boundaryMap : (K : JFzero Old) →
    deltaFiller New (candidateMap K) ≡ deltaFiller Old K)
  (conditionsMap : (K : JFzero Old) → PreservesFrame Old K
    → PreservesFrame New (candidateMap K))
  → AdmissibleFiller P Old → AdmissibleFiller P New
refineFrame Old New candidateMap boundaryMap conditionsMap
  (K , boundary , conditions) =
  candidateMap K , (boundaryMap K ∙ boundary) , conditionsMap K conditions

-- No constructor from BoundaryFiller to AdmissibleFiller is provided.
