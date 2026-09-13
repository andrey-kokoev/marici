{-# OPTIONS --safe --cubical --guardedness #-}
module BoundaryPfaffianResidualFold where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver

module ResidualFold {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  Carrier = fst R

  -- An odd metric word is generated from a singleton by adjoining two gaps.
  data OddMetric : Type ℓ where
    singleton : OddMetric
    extendRight : OddMetric → Carrier → Carrier → OddMetric

  record GapUnit (x : Carrier) : Type ℓ where
    field
      inverse : Carrier
      inverseLaw : inverse · x ≡ 1r

  -- A localized word carries a unit witness for every selected even-indexed
  -- gap.  Unselected odd-indexed gaps need no inverse.
  data LocalizedOddMetric : Type ℓ where
    localizedSingleton : LocalizedOddMetric
    localizedExtendRight :
      LocalizedOddMetric → (evenGap : Carrier) → GapUnit evenGap →
      (oddGap : Carrier) → LocalizedOddMetric

  eraseLocalization : LocalizedOddMetric → OddMetric
  eraseLocalization localizedSingleton = singleton
  eraseLocalization (localizedExtendRight X e ue o) =
    extendRight (eraseLocalization X) e o

  localizedSelectedTorsion : LocalizedOddMetric → Carrier
  localizedSelectedTorsion localizedSingleton = 1r
  localizedSelectedTorsion (localizedExtendRight X e ue o) =
    localizedSelectedTorsion X · e

  outgoing : OddMetric → Carrier
  outgoing singleton = 1r
  outgoing (extendRight X evenGap oddGap) = outgoing X · evenGap

  incoming : OddMetric → Carrier
  incoming singleton = 1r
  incoming (extendRight X evenGap oddGap) = incoming X · oddGap

  localizedTorsionIsOutgoing : (X : LocalizedOddMetric) →
    localizedSelectedTorsion X ≡ outgoing (eraseLocalization X)
  localizedTorsionIsOutgoing localizedSingleton = refl
  localizedTorsionIsOutgoing (localizedExtendRight X e ue o) =
    cong (_· e) (localizedTorsionIsOutgoing X)

  prependPair : Carrier → Carrier → OddMetric → OddMetric
  prependPair evenGap oddGap singleton =
    extendRight singleton evenGap oddGap
  prependPair evenGap oddGap (extendRight X e o) =
    extendRight (prependPair evenGap oddGap X) e o

  prependOutgoing : (e o : Carrier) (X : OddMetric) →
    outgoing (prependPair e o X) ≡ e · outgoing X
  prependOutgoing e o singleton = solve! R
  prependOutgoing e o (extendRight X a b) =
    cong (_· a) (prependOutgoing e o X) ∙ solve! R

  prependIncoming : (e o : Carrier) (X : OddMetric) →
    incoming (prependPair e o X) ≡ o · incoming X
  prependIncoming e o singleton = solve! R
  prependIncoming e o (extendRight X a b) =
    cong (_· b) (prependIncoming e o X) ∙ solve! R

  reverseMetric : OddMetric → OddMetric
  reverseMetric singleton = singleton
  reverseMetric (extendRight X e o) =
    prependPair o e (reverseMetric X)

  reversePrependPair : (e o : Carrier) (X : OddMetric) →
    reverseMetric (prependPair e o X) ≡
    extendRight (reverseMetric X) o e
  reversePrependPair e o singleton = refl
  reversePrependPair e o (extendRight X a b) =
    cong (prependPair b a) (reversePrependPair e o X)

  reverseMetricInvolutive : (X : OddMetric) →
    reverseMetric (reverseMetric X) ≡ X
  reverseMetricInvolutive singleton = refl
  reverseMetricInvolutive (extendRight X e o) =
    reversePrependPair o e (reverseMetric X) ∙
    cong (λ Y → extendRight Y e o) (reverseMetricInvolutive X)

  reverseOutgoing : (X : OddMetric) →
    outgoing (reverseMetric X) ≡ incoming X
  reverseOutgoing singleton = refl
  reverseOutgoing (extendRight X e o) =
    prependOutgoing o e (reverseMetric X) ∙
    cong (o ·_) (reverseOutgoing X) ∙
    solve! R

  reverseIncoming : (X : OddMetric) →
    incoming (reverseMetric X) ≡ outgoing X
  reverseIncoming singleton = refl
  reverseIncoming (extendRight X e o) =
    prependIncoming o e (reverseMetric X) ∙
    cong (e ·_) (reverseIncoming X) ∙
    solve! R

  record ResidualSummary : Type ℓ where
    field
      out inn : Carrier

  open ResidualSummary public

  summarize : OddMetric → ResidualSummary
  summarize X = record { out = outgoing X ; inn = incoming X }

  reverseSummary : ResidualSummary → ResidualSummary
  reverseSummary X = record { out = inn X ; inn = out X }

  reverseSummaryInvolutive : (X : ResidualSummary) →
    reverseSummary (reverseSummary X) ≡ X
  reverseSummaryInvolutive X = refl

  summarizeReversal : (X : OddMetric) →
    summarize (reverseMetric X) ≡ reverseSummary (summarize X)
  summarizeReversal X i = record
    { out = reverseOutgoing X i
    ; inn = reverseIncoming X i
    }

  pairAction : ResidualSummary → Carrier → Carrier → ResidualSummary
  pairAction X evenGap oddGap = record
    { out = out X · evenGap
    ; inn = inn X · oddGap
    }

  summarizeExtend : (X : OddMetric) (evenGap oddGap : Carrier) →
    summarize (extendRight X evenGap oddGap) ≡
    pairAction (summarize X) evenGap oddGap
  summarizeExtend X evenGap oddGap = refl

  -- Adding two pairs in either parenthesization gives the same summary.
  pairActionAssociative :
    (X : ResidualSummary)
    (e₁ o₁ e₂ o₂ : Carrier) →
    pairAction (pairAction X e₁ o₁) e₂ o₂ ≡
    pairAction X (e₁ · e₂) (o₁ · o₂)
  pairActionAssociative X e₁ o₁ e₂ o₂ i = record
    { out = outPath i
    ; inn = inPath i
    }
    where
    outPath : (out X · e₁) · e₂ ≡ out X · (e₁ · e₂)
    outPath = solve! R
    inPath : (inn X · o₁) · o₂ ≡ inn X · (o₁ · o₂)
    inPath = solve! R

  sew : ResidualSummary → Carrier → ResidualSummary → Carrier
  sew X gap Y = out X · gap · inn Y

  sewingReversal : (X Y : ResidualSummary) (gap : Carrier) →
    sew (reverseSummary Y) gap (reverseSummary X) ≡ sew X gap Y
  sewingReversal X Y gap = solve! R

  -- Internal pair growth affects sewing only through the updated boundary
  -- charge, so the residual summary is sufficient under further extension.
  sewAfterLeftExtension :
    (X Y : ResidualSummary) (e o gap : Carrier) →
    sew (pairAction X e o) gap Y ≡
    e · sew X gap Y
  sewAfterLeftExtension X Y e o gap = solve! R

  sewAfterRightExtension :
    (X Y : ResidualSummary) (e o gap : Carrier) →
    sew X gap (pairAction Y e o) ≡
    o · sew X gap Y
  sewAfterRightExtension X Y e o gap = solve! R

  -- Even metric words are obtained by closing an odd word with one gap and
  -- then adjoining gap pairs.  Their torsion is the adjacent even product.
  data EvenMetric : Type ℓ where
    closeOdd : OddMetric → Carrier → EvenMetric
    extendEvenRight : EvenMetric → Carrier → Carrier → EvenMetric

  -- An even localized word additionally requires the final selected closing
  -- gap to be a unit, so every hyperbolic pair can be contracted.
  record LocalizedEvenMetric : Type ℓ where
    field
      oddPart : LocalizedOddMetric
      closingGap : Carrier
      closingGapUnit : GapUnit closingGap

  eraseEvenLocalization : LocalizedEvenMetric → EvenMetric
  eraseEvenLocalization X =
    closeOdd (eraseLocalization (LocalizedEvenMetric.oddPart X))
      (LocalizedEvenMetric.closingGap X)

  localizedEvenTorsion : LocalizedEvenMetric → Carrier
  localizedEvenTorsion X =
    localizedSelectedTorsion (LocalizedEvenMetric.oddPart X) ·
    LocalizedEvenMetric.closingGap X

  evenTorsion : EvenMetric → Carrier
  evenTorsion (closeOdd X closingGap) = outgoing X · closingGap
  evenTorsion (extendEvenRight X ignoredGap selectedGap) =
    evenTorsion X · selectedGap

  localizedEvenTorsionCorrect : (X : LocalizedEvenMetric) →
    localizedEvenTorsion X ≡ evenTorsion (eraseEvenLocalization X)
  localizedEvenTorsionCorrect X =
    cong (_· LocalizedEvenMetric.closingGap X)
      (localizedTorsionIsOutgoing (LocalizedEvenMetric.oddPart X))

  -- Scalar line coordinates for refining one selected gap.  The new selected
  -- factors are the two outer gaps; the old selected factor is rho.
  selectedOldTorsion : Carrier → Carrier → Carrier
  selectedOldTorsion rest rho = rest · rho

  selectedNewTorsion : Carrier → Carrier → Carrier → Carrier
  selectedNewTorsion rest alpha beta = rest · alpha · beta

  selectedRefinementCorrespondence :
    (rest rho alpha gamma beta : Carrier) →
    rho ≡ alpha · gamma · beta →
    rho · selectedNewTorsion rest alpha beta ≡
    (alpha · beta) · selectedOldTorsion rest rho
  selectedRefinementCorrespondence rest rho alpha gamma beta factorization =
    solve! R

  selectedLocalizedTransition :
    (rest rho alpha beta : Carrier) (uRho : GapUnit rho) →
    selectedNewTorsion rest alpha beta ≡
    (alpha · beta · GapUnit.inverse uRho) · selectedOldTorsion rest rho
  selectedLocalizedTransition rest rho alpha beta uRho =
    sym (insertUnit ∙ normalize)
    where
    insertUnit :
      (alpha · beta · GapUnit.inverse uRho) · selectedOldTorsion rest rho ≡
      (rest · alpha · beta) · (GapUnit.inverse uRho · rho)
    insertUnit = solve! R
    normalize :
      (rest · alpha · beta) · (GapUnit.inverse uRho · rho) ≡
      selectedNewTorsion rest alpha beta
    normalize =
      cong ((rest · alpha · beta) ·_) (GapUnit.inverseLaw uRho) ∙
      solve! R

  unselectedRefinementTransition :
    (rest gamma : Carrier) → rest · gamma ≡ gamma · rest
  unselectedRefinementTransition rest gamma = solve! R

  joinOdd : OddMetric → Carrier → OddMetric → EvenMetric
  joinOdd X gap singleton = closeOdd X gap
  joinOdd X gap (extendRight Y e o) =
    extendEvenRight (joinOdd X gap Y) e o

  -- Arbitrary odd--odd sewing computes the adjacent Pfaffian torsion of the
  -- joined even word.  This generalizes the concrete three-plus-three proof.
  joinOddTorsion : (X Y : OddMetric) (gap : Carrier) →
    evenTorsion (joinOdd X gap Y) ≡
    sew (summarize X) gap (summarize Y)
  joinOddTorsion X singleton gap = solve! R
  joinOddTorsion X (extendRight Y e o) gap =
    cong (_· o) (joinOddTorsion X Y gap) ∙ solve! R

  -- Reversing both odd blocks and their order preserves the resulting even
  -- torsion.  This is arbitrary-size Pfaffian reversal at the fold level.
  joinedTorsionReversal : (X Y : OddMetric) (gap : Carrier) →
    evenTorsion (joinOdd (reverseMetric Y) gap (reverseMetric X)) ≡
    evenTorsion (joinOdd X gap Y)
  joinedTorsionReversal X Y gap =
    joinOddTorsion (reverseMetric Y) (reverseMetric X) gap ∙
    cong₂ (λ A B → sew A gap B)
      (summarizeReversal Y) (summarizeReversal X) ∙
    sewingReversal (summarize X) (summarize Y) gap ∙
    sym (joinOddTorsion X Y gap)
