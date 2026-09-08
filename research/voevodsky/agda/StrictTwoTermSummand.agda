{-# OPTIONS --safe --cubical --guardedness #-}
module StrictTwoTermSummand where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- A strict chain retract onto [R --(-x)--> R]. Both grades are retained.
record StrictTwoTermSummand {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    AmbientChain Ring : Type ℓ
    differential : AmbientChain → AmbientChain
    scale : Ring → AmbientChain → AmbientChain
    x : Ring
    upper lower : AmbientChain
    zeroChain : AmbientChain

    twoTermDifferential : differential upper ≡ scale x lower
    lowerClosed : differential lower ≡ zeroChain

    TwoTerm : Type ℓ
    project : AmbientChain → TwoTerm
    section : TwoTerm → AmbientChain
    projectSection : (z : TwoTerm) → project (section z) ≡ z
    differentialTwoTerm : TwoTerm → TwoTerm
    projectChainMap : (z : AmbientChain) →
      project (differential z) ≡ differentialTwoTerm (project z)
    sectionChainMap : (z : TwoTerm) →
      differential (section z) ≡ section (differentialTwoTerm z)

    upperTerm lowerTerm : TwoTerm
    sectionUpper : section upperTerm ≡ upper
    sectionLower : section lowerTerm ≡ lower
    strictArrow : differentialTwoTerm upperTerm ≡ project (scale x lower)
    strictLowerClosed : differentialTwoTerm lowerTerm ≡ project zeroChain

    LowerHomology UpperHomology : Type ℓ
    lowerClass : LowerHomology
    upperAnnihilatorClass : UpperHomology
    zeroLower : LowerHomology
    zeroUpper : UpperHomology
    lowerClassNonzero : lowerClass ≡ zeroLower → ⊥
    upperAnnihilatorNonzero : upperAnnihilatorClass ≡ zeroUpper → ⊥

    annihilator : Ring
    annihilatorNonzero : Type ℓ
    annihilatorWitness : annihilatorNonzero
    annihilatorKillsX : scale annihilator (scale x upper) ≡ zeroChain

-- The homology-module truncation keeps R/(x) below but declares its upper
-- homology trivial. It therefore forgets Ann(x), which is nonzero here.
record LowerHomologyTruncation {ℓ : Level}
  (S : StrictTwoTermSummand {ℓ}) : Type (ℓ-suc ℓ) where
  private module S = StrictTwoTermSummand S
  field
    LowerOnly : Type ℓ
    upperHomologyLowerOnly : Type ℓ
    zeroUpperLowerOnly : upperHomologyLowerOnly
    upperLowerOnlyContractible : (z : upperHomologyLowerOnly) →
      z ≡ zeroUpperLowerOnly
    identifyLower : S.LowerHomology → LowerOnly

-- A quasi-isomorphism would in particular give mutually inverse maps on upper
-- homology. This package isolates exactly that impossible consequence.
record UpperHomologyEquivalence {ℓ : Level}
  {S : StrictTwoTermSummand {ℓ}}
  (T : LowerHomologyTruncation S) : Type (ℓ-suc ℓ) where
  private
    module S = StrictTwoTermSummand S
    module T = LowerHomologyTruncation T
  field
    forwardUpper : S.UpperHomology → T.upperHomologyLowerOnly
    backwardUpper : T.upperHomologyLowerOnly → S.UpperHomology
    backwardZero : backwardUpper T.zeroUpperLowerOnly ≡ S.zeroUpper
    upperSection : (z : S.UpperHomology) →
      backwardUpper (forwardUpper z) ≡ z

strictSummandNotEquivalentToLowerTruncation : {ℓ : Level}
  {S : StrictTwoTermSummand {ℓ}}
  (T : LowerHomologyTruncation S) → UpperHomologyEquivalence T → ⊥
strictSummandNotEquivalentToLowerTruncation {S = S} T E =
  StrictTwoTermSummand.upperAnnihilatorNonzero S
    (sym (UpperHomologyEquivalence.upperSection E upper)
    ∙ cong (UpperHomologyEquivalence.backwardUpper E)
        (LowerHomologyTruncation.upperLowerOnlyContractible T
          (UpperHomologyEquivalence.forwardUpper E upper))
    ∙ UpperHomologyEquivalence.backwardZero E)
  where
  upper : StrictTwoTermSummand.UpperHomology S
  upper = StrictTwoTermSummand.upperAnnihilatorClass S

record StrictSummandTruncationCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    strictSummand : StrictTwoTermSummand {ℓ}
    lowerTruncation : LowerHomologyTruncation strictSummand
