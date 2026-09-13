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

  outgoing : OddMetric → Carrier
  outgoing singleton = 1r
  outgoing (extendRight X evenGap oddGap) = outgoing X · evenGap

  incoming : OddMetric → Carrier
  incoming singleton = 1r
  incoming (extendRight X evenGap oddGap) = incoming X · oddGap

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
