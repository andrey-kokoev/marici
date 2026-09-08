{-# OPTIONS --safe --cubical --guardedness #-}
module SupportTriangleDualReversal where

open import Cubical.Foundations.Prelude

-- A degreewise-split short exact sequence modelling the support triangle
-- V -> E -> Q -> V[1]. Exactness itself is retained as data because concrete
-- instances use chain complexes, not bare types.
record SplitSupportTriangle {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Supported Total Generic : Type ℓ
    zeroSupported : Supported
    zeroTotal : Total
    zeroGeneric : Generic
    -- Keeping the carriers separate avoids identifying support and quotient
    -- classes.
    include : Supported → Total
    project : Total → Generic
    section : Generic → Total
    retract : Total → Supported

    projectIncludeZero : (v : Supported) → project (include v) ≡ zeroGeneric
    projectSection : (q : Generic) → project (section q) ≡ q
    retractInclude : (v : Supported) → retract (include v) ≡ v

    ExactAtTotal : Type ℓ
    exactAtTotal : ExactAtTotal
    DegreewiseSplit : Type ℓ
    degreewiseSplit : DegreewiseSplit

    SupportedHomology GenericHomology ShiftedSupportedHomology : Type ℓ
    classSupported : Supported → SupportedHomology
    classGeneric : Generic → GenericHomology
    connecting : GenericHomology → ShiftedSupportedHomology

-- A map of support triangles includes all three vertical maps. Naturality of
-- the long connecting morphism is an explicit square, not inferred from names.
record SupportTriangleMorphism {ℓ : Level}
  (S T : SplitSupportTriangle {ℓ}) : Type (ℓ-suc ℓ) where
  private
    module S = SplitSupportTriangle S
    module T = SplitSupportTriangle T
  field
    mapSupported : S.Supported → T.Supported
    mapTotal : S.Total → T.Total
    mapGeneric : S.Generic → T.Generic
    includeSquare : (v : S.Supported) →
      mapTotal (S.include v) ≡ T.include (mapSupported v)
    projectSquare : (e : S.Total) →
      mapGeneric (S.project e) ≡ T.project (mapTotal e)

    mapGenericHomology : S.GenericHomology → T.GenericHomology
    mapShiftedSupportedHomology :
      S.ShiftedSupportedHomology → T.ShiftedSupportedHomology
    connectingNatural : (q : S.GenericHomology) →
      mapShiftedSupportedHomology (S.connecting q) ≡
      T.connecting (mapGenericHomology q)

-- Finite homogeneous duality is contravariant: the support triangle reverses
-- from V -> E -> Q to Q# -> E# -> V#. The dual connecting map therefore has
-- the opposite direction.
record FiniteDualSupportReversal {ℓ : Level}
  (T : SplitSupportTriangle {ℓ}) : Type (ℓ-suc ℓ) where
  private module T = SplitSupportTriangle T
  field
    DualSupported DualTotal DualGeneric : Type ℓ
    dualizeSupported : T.Supported → DualSupported
    dualizeTotal : T.Total → DualTotal
    dualizeGeneric : T.Generic → DualGeneric

    dualProject : DualGeneric → DualTotal
    dualInclude : DualTotal → DualSupported
    dualProjectIsTranspose : Type ℓ
    dualProjectTransposeWitness : dualProjectIsTranspose
    dualIncludeIsTranspose : Type ℓ
    dualIncludeTransposeWitness : dualIncludeIsTranspose

    DualShiftedGenericHomology DualSupportedHomology : Type ℓ
    reverseConnecting : DualSupportedHomology → DualShiftedGenericHomology
    pairGeneric : DualShiftedGenericHomology → T.GenericHomology → Type ℓ
    pairSupport : DualSupportedHomology → T.ShiftedSupportedHomology → Type ℓ

    -- This is the naturality/transpose square for the long connecting map.
    connectingPairingCompatibility :
      (v# : DualSupportedHomology) (q : T.GenericHomology) →
      pairGeneric (reverseConnecting v#) q ≡ pairSupport v# (T.connecting q)

    ReversedTriangleExact : Type ℓ
    reversedTriangleExact : ReversedTriangleExact

record SupportTriangleDualityCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    supportTriangle : SplitSupportTriangle {ℓ}
    finiteDualReversal : FiniteDualSupportReversal supportTriangle
