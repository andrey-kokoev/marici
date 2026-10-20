{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedReaderClassificationRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import NativeExtensionFamilyAudit using (A; B; C; D; root; sigmaEquiv)
open import InternalSourceComparisons using (Body; exchange; stay; edgeMap)
open import InternalComparisonInterchange using (graphEquiv)
open import GeneratedReaderClassification
open Normal
import RepeatedInterchangeCoherence as R

-- Certify the EXACT previous bodies, not new seeded replacements or merely
-- equal endpoint values. The actual old equivalences/point/port proofs recur.
a0 : Fragment A
a0 = start A (root A)
b0 : Fragment B
b0 = start B (root B)
a1 : Fragment B
a1 = attachF a0 R.first
b1 : Fragment A
b1 = attachF b0 (edgeMap exchange R.first)
a2 : Fragment C
a2 = attachF a1 R.second
b2 : Fragment D
b2 = attachF b1 R.movedSecond
firstComparison : Fragment B
firstComparison = compareF exchange a0 b0 sigmaEquiv refl (λ x → refl)
oldSource : Fragment D
oldSource = compareF exchange a2 b2 (R.Second.attachmentEquiv R.second)
  (R.Second.attachmentPoint R.second) (R.Second.attachmentPorts R.second)
oldTarget : Fragment D
oldTarget = attachF (attachF firstComparison (edgeMap exchange R.first)) R.movedSecond
old-source-exact : body oldSource ≡ R.source
old-source-exact = refl
old-target-exact : body oldTarget ≡ R.target
old-target-exact = refl
module One = Comparisons stay oldSource oldTarget
old-coherence-from-classification : R.sequentialFiller ≡ R.directFiller
old-coherence-from-classification = One.filler-prop R.sequentialFiller R.directFiller
old-witness-recovered : old-coherence-from-classification ≡ R.filler-coherence
old-witness-recovered = isProp→isSet One.filler-prop _ _ _ _

-- Synthesis from image agreement also recovers a complete old filler, not
-- only an equivalent endpoint. No requested equality is imported as a rule.
rebuiltFiller : One.Filler
rebuiltFiller = One.filler-from-images (One.images-from-filler R.sequentialFiller)
rebuilt-exact : rebuiltFiller ≡ R.sequentialFiller
rebuilt-exact = One.filler-prop rebuiltFiller R.sequentialFiller

-- Normal forms are reader images, not merely cardinalities. Both complete
-- source and target of this diagram normalize to Out A with its reader.
source-shape : shape (normal oldSource) ≡ outgoing A
source-shape = refl
target-shape : shape (normal oldTarget) ≡ outgoing A
target-shape = refl
