{-# OPTIONS --safe --cubical --guardedness #-}
module WitnessHigherControls where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels using (isProp×; isPropΠ)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty using (⊥)
open import NativeExtensionFamilyAudit using (Vertex; A; B; C; D; AB; BC; AD; Seeds; root; pointQ; sigmaEquiv; tauEquiv; PreservesEdges; tau-breaks-incidence)
open import SourceIndexedExtensionFamilies using (Out; vertex-is-set)
open import InternalSourceComparisons
open import WitnessContinuationHistories
open State
import GeneratedReaderClassification as G
import InterchangeHiddenFiberObstruction as Hidden
import RepeatedInterchangeCoherence as Prior
import InternalComparisonInterchange as Native
import ForwardCertifiedPrograms as Producer
import ContinuationPolicyFamily as Policy
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- Reuse the existing theorem and actual path of native derivations. No
-- reconstruction of the earlier two-step interchange diagram.
existing-higher = Prior.filler-coherence
existing-native-path = Prior.native-history-coherence

-- An explicit sufficient hypothesis for automatic comparison of independent
-- COMPLETE fillers. This is not assumed for all Body or all native rules.
module Faithful {v : Vertex} (a b : Body v) (normal : G.Normal b) where
  filler-prop : isProp (Filler stay a b)
  filler-prop (e , p , h) (f , q , k) = Σ≡Prop
    (λ e → isProp× (G.carrier-set normal _ _) (isPropΠ (λ x → vertex-is-set _ _)))
    (equivEq (funExt (λ x → G.reader-injective normal _ _ (sym (h x) ∙ k x))))
  asBody : Filler stay a b → Body v
  asBody (e , p , h) = compare stay a b e p h
  native-path : (f g : Filler stay a b) → PathP
    (λ i → Resolve Seeds (package (asBody (filler-prop f g i))))
    (derivation (asBody f)) (derivation (asBody g))
  native-path f g i = derivation (asBody (filler-prop f g i))
  higher-unique : {f g : Filler stay a b} (p q : f ≡ g) → p ≡ q
  higher-unique = isProp→isSet filler-prop _ _

runFragment : {v t : Vertex} → History v t → G.Fragment v → G.Fragment t
runFragment done a = a
runFragment (next o h) a = runFragment h (G.attachF a o)
body-run : {v t : Vertex} (h : History v t) (a : G.Fragment v)
  → G.body (runFragment h a) ≡ runBody h (G.body a)
body-run done a = refl
body-run (next o h) a = body-run h (G.attachF a o)
chosenFragment : G.Fragment B
chosenFragment = G.compareF exchange (G.start A (root A)) (G.start B (root B))
  sigmaEquiv refl (λ x → refl)
chosen-normal : {t : Vertex} (h : History B t) → G.Normal (runBody h (witness chosen))
chosen-normal h = subst G.Normal (body-run h chosenFragment) (G.normal (runFragment h chosenFragment))

-- Closure of the existing reader classification under the actual source
-- operations, even when a policy source presentation is not a Fragment.
attach-normal : {v : Vertex} (a : Body v) (o : Out v) → G.Normal a → G.Normal (attach a o)
G.Normal.shape (attach-normal {v} a o n) = G.outgoing v
G.Normal.equivalence (attach-normal a o n) = isoToEquiv (G.attachmentIso a o (G.carrier-set n))
G.Normal.ports (attach-normal a o n) x = refl
run-normal : {v t : Vertex} (h : History v t) (a : Body v) → G.Normal a → G.Normal (runBody h a)
run-normal done a n = n
run-normal (next o h) a n = run-normal h (attach a o) (attach-normal a o n)
witness-normal : {m : Mode} {v : Vertex} (s : State m v) → G.Normal (right s) → G.Normal (witness s)
G.Normal.shape (witness-normal s n) = G.Normal.shape n
G.Normal.equivalence (witness-normal s n) = compEquiv (Native.graphEquiv (fst (selected s)))
  (compEquiv (fst (selected s)) (G.Normal.equivalence n))
G.Normal.ports (witness-normal s n) (x , y , p) = sym (cong (reader (right s)) p)
  ∙ G.Normal.ports n (equivFun (fst (selected s)) x)
module AllHigher {m : Mode} {v : Vertex} (s : State m v) (normal : G.Normal (witness s)) where
  module At {t : Vertex} (h : History v t) = Faithful (witness (run h s))
    (runBody (mapHistory m h) (witness s)) (run-normal (mapHistory m h) (witness s) normal)
  direct-staged : {u t : Vertex} (h : History v u) (k : History u t)
    → finiteSquare (h ++ k) s ≡ stagedSquare h k s
  direct-staged h k = At.filler-prop (h ++ k) (finiteSquare (h ++ k) s) (stagedSquare h k s)
source-normal : (r : Source.Request) → G.Normal (witness (sourceState r))
source-normal r = witness-normal (sourceState r)
  (attach-normal (witness chosen) (Source.route r) (G.normal chosenFragment))
module SourceHigher (r : Source.Request) = AllHigher (sourceState r) (source-normal r)
module PolicyHigher (m : Mode) {v : Vertex} (p : Producer.Program v) (q : Producer.Program (act m v))
  (ok : Producer.Pair.Guard m p q) where
  module C = CertifiedFamily m p q ok
  normal : (control : C.C.Control) (k : Policy.Presentation) → G.Normal (witness (C.state control k))
  normal control k = witness-normal (C.state control k)
    (G.normal (C.C.R.targetFragment (C.C.R.synchronize control)))
  module For (control : C.C.Control) (k : Policy.Presentation) = AllHigher (C.state control k) (normal control k)

-- No history was removed: every Out history of the SAME chosen witness has
-- a faithful target, derived from the existing classification theorem.
module ChosenHigher {t : Vertex} (h : History A t) where
  module F = Faithful (witness (run h chosen))
    (runBody (mapHistory exchange h) (witness chosen)) (chosen-normal (mapHistory exchange h))
  all-fillers-cohere = F.filler-prop
  complete-native-history = F.native-path
  all-higher-pastings-cohere = F.higher-unique

chosen-direct-staged : {v t : Vertex} (h : History A v) (k : History v t)
  → finiteSquare (h ++ k) chosen ≡ stagedSquare h k chosen
chosen-direct-staged h k = ChosenHigher.all-fillers-cohere (h ++ k)
  (finiteSquare (h ++ k) chosen) (stagedSquare h k chosen)
chosen-direct-staged-native : {v t : Vertex} (h : History A v) (k : History v t)
  → PathP (λ i → Resolve Seeds
      (package (ChosenHigher.F.asBody (h ++ k) (chosen-direct-staged h k i))))
    (derivation (ChosenHigher.F.asBody (h ++ k) (finiteSquare (h ++ k) chosen)))
    (derivation (ChosenHigher.F.asBody (h ++ k) (stagedSquare h k chosen)))
chosen-direct-staged-native h k i = derivation
  (ChosenHigher.F.asBody (h ++ k) (chosen-direct-staged h k i))

-- Bind the quantified theorem back to the unchanged named two-step source
-- diagram. Reuse its higher witness for the second equality.
existingHistory : History A C
existingHistory = next (B , AB) (next (C , BC) done)
existing-sequential-agrees : Prior.sequentialFiller ≡ finiteSquare existingHistory chosen
existing-sequential-agrees = ChosenHigher.all-fillers-cohere existingHistory
  Prior.sequentialFiller (finiteSquare existingHistory chosen)
existing-direct-agrees : Prior.directFiller ≡ finiteSquare existingHistory chosen
existing-direct-agrees = sym Prior.filler-coherence ∙ existing-sequential-agrees

-- The original hidden-fiber control, retaining the WHOLE filler, not merely
-- endpoints or port readings. Both complete fillers satisfy those tests.
HiddenFiller : Type
HiddenFiller = Σ (Hidden.Carrier ≃ Hidden.Carrier) (λ e →
  (equivFun e Hidden.selected ≡ Hidden.selected)
  × ((x : Hidden.Carrier) → Hidden.readPort x ≡ Hidden.readPort (equivFun e x)))
hiddenId hiddenSwap : HiddenFiller
hiddenId = Hidden.identityEquiv , refl , (λ x → refl)
hiddenSwap = Hidden.swapEquiv , Hidden.selected-fixed , (λ x → refl)
no-hidden-filler-equality : hiddenId ≡ hiddenSwap → ⊥
no-hidden-filler-equality p = Hidden.no-higher-comparison (cong fst p)
no-observational-uniqueness : isProp HiddenFiller → ⊥
no-observational-uniqueness unique = no-hidden-filler-equality (unique hiddenId hiddenSwap)

-- Strengthen the control without adding seeds: native E rules generate the
-- independent Boolean fields over an admitted reflexivity package.
loopQ = path-package (expression (pointQ A)) (value (pointQ A)) (value (pointQ A)) refl
loopD : Resolve Seeds loopQ
loopD = apply (reflexivity-rule (expression (pointQ A)) (value (pointQ A))) (λ _ → root A)
innerQ = E-package Bool (λ _ → loopQ) false
innerD : Resolve Seeds innerQ
innerD = apply (E-rule Bool (λ _ → loopQ) false) (λ _ → loopD)
bitsQ = E-package Bool (λ _ → innerQ) false
bitsD : Resolve Seeds bitsQ
bitsD = apply (E-rule Bool (λ _ → innerQ) false) (λ _ → innerD)
nativeHiddenQ = E-package (Out A) (λ _ → bitsQ) (D , AD)
nativeHiddenD : Resolve Seeds nativeHiddenQ
nativeHiddenD = apply (E-rule (Out A) (λ _ → bitsQ) (D , AD)) (λ _ → bitsD)
nativeHidden : Body D
nativeHidden = prepared D nativeHiddenQ nativeHiddenD (λ x → fst (fst x)) refl
swapBits : Carrier nativeHidden → Carrier nativeHidden
swapBits (edge , x , y , loop) = edge , y , x , loop
swapBits² : (x : Carrier nativeHidden) → swapBits (swapBits x) ≡ x
swapBits² x = refl
swapBitsEquiv : Carrier nativeHidden ≃ Carrier nativeHidden
swapBitsEquiv = isoToEquiv (iso swapBits swapBits swapBits² swapBits²)
nativeId nativeSwap : State stay D
nativeId = cell nativeHidden nativeHidden (idEquiv _ , refl , (λ x → refl))
nativeSwap = cell nativeHidden nativeHidden (swapBitsEquiv , refl , (λ x → refl))
no-native-hidden-filler-equality : selected nativeId ≡ selected nativeSwap → ⊥
no-native-hidden-filler-equality p = false≢true
  (cong (λ f → fst (snd (equivFun (fst f) ((B , AB) , false , true , refl)))) p)
-- Our canonical continuation theorem still works for the hidden witness;
-- it does not equate independently selected initial fillers.
hidden-continuations : {t : Vertex} (h : History D t)
  → Resolve Seeds (package (witness (squareState h nativeSwap)))
hidden-continuations h = finite-native h nativeSwap
hidden-canonical-pasting : {u v t : Vertex}
  (h : History D u) (k : History u v) (l : History v t)
  → paste-left h k l nativeSwap ≡ paste-right h k l nativeSwap
hidden-canonical-pasting h k l = higher-pasting h k l nativeSwap

-- Even a natively admitted comparison need not preserve continuation
-- incidence. The native compare-rule itself is not a universal router.
no-automatic-incidence : PreservesEdges tauEquiv → ⊥
no-automatic-incidence = tau-breaks-incidence
