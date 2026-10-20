{-# OPTIONS --safe --cubical --guardedness #-}
module ForwardForwardBodyBinding where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma using (_×_)
open import Cubical.Data.Bool using (true)
open import Cubical.Data.List using (List; []; _∷_)
open import NativeExtensionFamilyAudit using
  (Vertex; A; B; C; D; AB; BC; BA; AD; Seeds; pointQ; root)
open import SourceIndexedExtensionFamilies using (Out)
open import InternalSourceComparisons using
  (Body; Mode; stay; exchange; act; edgeMap; package; reader; derivation)
open import InternalComparisonInterchange using (graphEquiv; module Interchange)
open import GeneratedReaderClassification
import CanonicalComparisonSynthesis as Compiler
import RetainedFeedbackCovariance as Move
import ForwardSourceLiftComposition as Forward
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

cmp : (m : Mode) {v : Vertex} (a : Fragment v) (b : Fragment (act m v))
  → Comparisons.Filler m a b → Fragment (act m v)
cmp m a b f = compareF m a b (fst f) (fst (snd f)) (snd (snd f))

composeStay : {v : Vertex} (a b c : Fragment v)
  → Comparisons.Filler stay a b → Comparisons.Filler stay b c
  → Comparisons.Filler stay a c
composeStay a b c (e , p , h) (e' , p' , h') = compEquiv e e'
  , (cong (equivFun e') p ∙ p') , (λ x → h x ∙ h' (equivFun e x))
precomposeStay : (m : Mode) {v : Vertex} (a b : Fragment v) (c : Fragment (act m v))
  → Comparisons.Filler stay a b → Comparisons.Filler m b c
  → Comparisons.Filler m a c
precomposeStay m a b c (e , p , h) (e' , p' , h') = compEquiv e e'
  , (cong (equivFun e') p ∙ p') , (λ x → cong (act m) (h x) ∙ h' (equivFun e x))
inverseStay : {v : Vertex} (a b : Fragment v)
  → Comparisons.Filler stay a b → Comparisons.Filler stay b a
inverseStay a b (e , p , h) = invEquiv e
  , (cong (invEq e) (sym p) ∙ retEq e (point (body a)))
  , (λ y → sym (h (invEq e y) ∙ cong (reader (body b)) (secEq e y)))
targetProjection : (m : Mode) {v : Vertex} (a : Fragment v) (b : Fragment (act m v))
  (f : Comparisons.Filler m a b) → Comparisons.Filler stay (cmp m a b f) b
targetProjection m a b f = compEquiv (graphEquiv (fst f)) (fst f)
  , fst (snd f) , (λ z → sym (cong (reader (body b)) (snd (snd z))))

-- Generic two-attachment row using the EXISTING interchange constructors.
-- Its first and second cells, whiskering and every operand are explicit.
module Row (m : Mode) {v : Vertex} (a : Fragment v) (b : Fragment (act m v))
  (f : Comparisons.Filler m a b) (o : Out v) (p : Out (fst o)) where
  base = cmp m a b f
  module First = Interchange m v (body a) (body b) (fst f) (fst (snd f)) (snd (snd f))
  aFirst = attachF a o
  bFirst = attachF b (edgeMap m o)
  firstFiller : Comparisons.Filler m aFirst bFirst
  firstFiller = First.attachmentEquiv o , First.attachmentPoint o , First.attachmentPorts o
  firstCompare = cmp m aFirst bFirst firstFiller
  afterFirst = attachF base (edgeMap m o)
  firstCell : Comparisons.Filler stay firstCompare afterFirst
  firstCell = First.interchangeEquiv o , First.interchangePoint o , First.interchangePorts o
  module Second = Interchange m (fst o) (body aFirst) (body bFirst)
    (fst firstFiller) (fst (snd firstFiller)) (snd (snd firstFiller))
  leftFinal = attachF aFirst p
  rightFinal = attachF bFirst (edgeMap m p)
  finalFiller : Comparisons.Filler m leftFinal rightFinal
  finalFiller = Second.attachmentEquiv p , Second.attachmentPoint p , Second.attachmentPorts p
  source = cmp m leftFinal rightFinal finalFiller
  middle = attachF firstCompare (edgeMap m p)
  target = attachF afterFirst (edgeMap m p)
  secondCell : Comparisons.Filler stay source middle
  secondCell = Second.interchangeEquiv p , Second.interchangePoint p , Second.interchangePorts p
  module Whisker = Interchange stay (act m (fst o)) (body firstCompare) (body afterFirst)
    (fst firstCell) (fst (snd firstCell)) (snd (snd firstCell))
  whiskeredFirst : Comparisons.Filler stay middle target
  whiskeredFirst = Whisker.attachmentEquiv (edgeMap m p)
    , Whisker.attachmentPoint (edgeMap m p) , Whisker.attachmentPorts (edgeMap m p)
  sequential : Comparisons.Filler stay source target
  sequential = composeStay source middle target secondCell whiskeredFirst
  firstCellTerm = cmp stay firstCompare afterFirst firstCell
  secondCellTerm = cmp stay source middle secondCell

module Diagram (d : Resolve Seeds (pointQ A)) where
  d1 : Resolve Seeds (pointQ B)
  d1 = Move.moveInitial A d
  d2 : Resolve Seeds (pointQ A)
  d2 = Move.moveInitial B d1
  a0 = start A d
  a1 = start B d1
  a2 = start A d2

  -- Bind the actual proof-level forward square to Body/Fragment, rather than
  -- replacing the second forward proof by the old seed at definition time.
  initial-forward-square : a2 ≡ a0
  initial-forward-square = cong (start A) (Forward.forward-square-initial A d)
  body-forward-square : body a2 ≡ body a0
  body-forward-square = cong body initial-forward-square
  attached-forward-square : attachF (attachF a2 (B , AB)) (C , BC)
    ≡ attachF (attachF a0 (B , AB)) (C , BC)
  attached-forward-square = cong (λ a → attachF (attachF a (B , AB)) (C , BC)) initial-forward-square
  attached-native-square : PathP
    (λ i → Resolve Seeds (package (body (attached-forward-square i))))
    (native (attachF (attachF a2 (B , AB)) (C , BC)))
    (native (attachF (attachF a0 (B , AB)) (C , BC)))
  attached-native-square i = native (attached-forward-square i)

  module FirstCompile = Compiler.Compile exchange a0 a1
  first-accepted : FirstCompile.accepted FirstCompile.compile ≡ true
  first-accepted = refl
  f1 = FirstCompile.require-success FirstCompile.compile first-accepted
  q1 = cmp exchange a0 a1 f1
  module SecondCompile = Compiler.Compile exchange q1 a2
  second-accepted : SecondCompile.accepted SecondCompile.compile ≡ true
  second-accepted = refl
  f2 = SecondCompile.require-success SecondCompile.compile second-accepted
  q2 = cmp exchange q1 a2 f2

  module FirstRow = Row exchange a0 a1 f1 (B , AB) (C , BC)
  module SecondRow = Row exchange q1 a2 f2 (A , BA) (D , AD)
  -- Exact common interface: no fresh seed or new independently chosen Body.
  rows-meet : FirstRow.target ≡ SecondRow.leftFinal
  rows-meet = refl
  outerFiller : Comparisons.Filler exchange FirstRow.source SecondRow.rightFinal
  outerFiller = precomposeStay exchange FirstRow.source FirstRow.target SecondRow.rightFinal
    FirstRow.sequential SecondRow.finalFiller
  source = cmp exchange FirstRow.source SecondRow.rightFinal outerFiller
  target = SecondRow.target

  -- Rebase the outer comparison to the second row using their common right
  -- operand and actual graph equivalences; outerFiller retains the first row.
  outerProjection = targetProjection exchange FirstRow.source SecondRow.rightFinal outerFiller
  rowProjection = targetProjection exchange SecondRow.leftFinal SecondRow.rightFinal SecondRow.finalFiller
  rebase : Comparisons.Filler stay source SecondRow.source
  rebase = composeStay source SecondRow.rightFinal SecondRow.source outerProjection
    (inverseStay SecondRow.source SecondRow.rightFinal rowProjection)
  sequential : Comparisons.Filler stay source target
  sequential = composeStay source SecondRow.source target rebase SecondRow.sequential

  -- Distinct fused route: contract the outer comparison to its right operand,
  -- then lift the inverse BASE comparison graph through both attachments.
  baseProjection = targetProjection exchange q1 a2 f2
  baseInverse = inverseStay q2 a2 baseProjection
  module Fused = Row stay a2 q2 baseInverse (B , AB) (C , BC)
  direct : Comparisons.Filler stay source target
  direct = composeStay source SecondRow.rightFinal target outerProjection Fused.finalFiller

  module Final = Compiler.Compile stay source target
  final-accepted : Final.accepted Final.compile ≡ true
  final-accepted = Final.complete sequential
  canonical = Final.require-success Final.compile final-accepted
  sequential-is-canonical : sequential ≡ canonical
  sequential-is-canonical = Final.agrees-with-existing sequential canonical
  direct-is-canonical : direct ≡ canonical
  direct-is-canonical = Final.agrees-with-existing direct canonical
  filler-coherence : sequential ≡ direct
  filler-coherence = sequential-is-canonical ∙ sym direct-is-canonical
  sequentialTerm = cmp stay source target sequential
  directTerm = cmp stay source target direct
  native-history-coherence : PathP
    (λ i → Resolve Seeds (package (body (cmp stay source target (filler-coherence i)))))
    (native sequentialTerm) (native directTerm)
  native-history-coherence i = native (cmp stay source target (filler-coherence i))

  -- Four actual interchange cells plus original/intermediate terms remain
  -- available; equality of their full output fillers does not erase this list.
  diagram : List (Σ Vertex Body)
  diagram = (A , body a0) ∷ (B , body a1) ∷ (A , body a2)
    ∷ (B , body q1) ∷ (A , body q2)
    ∷ (A , body FirstRow.firstCellTerm) ∷ (D , body FirstRow.secondCellTerm)
    ∷ (B , body SecondRow.firstCellTerm) ∷ (C , body SecondRow.secondCellTerm)
    ∷ (D , body FirstRow.source) ∷ (D , body FirstRow.target)
    ∷ (C , body source) ∷ (C , body SecondRow.source) ∷ (C , body target)
    ∷ (C , body sequentialTerm) ∷ (C , body directTerm) ∷ []

module Regression = Diagram (root A)
