{-# OPTIONS --safe --cubical --guardedness #-}
module MixedRootHistoryCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels using (isProp×; isPropΠ)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Maybe.Base using (just)
open import Cubical.Relation.Nullary.Base using (¬_)
open import NativeExtensionFamilyAudit using (Seeds)
open import SourceIndexedExtensionFamilies using (Out; vertex-is-set)
open import InternalSourceComparisons using (Mode; stay; Body; package; reader; compare; derivation)
import GeneratedReaderClassification as G
import FiniteComparisonTrees as F
import MixedComparisonTrees as M
import MixedHistoryCertificates as C
import NativeComposeHistoryBridge as Join
import NativeAttachmentHistoryBridge as Attach
import InternalComparisonInterchange as Native
import NonsetWitnessEnvelopes as Envelope
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- A reader-preserving pointed view to the ACTUAL target endpoint carrier.
-- This does not identify Complete codes or their native derivations.
record View (b : F.Object) (body : Body (fst b)) : Type where
  constructor view
  field
    equivalence : G.Carrier body ≃ F.Carrier b
    point : equivFun equivalence (G.point body) ≡ F.point b
    ports : (x : G.Carrier body) → reader body x ≡ F.readPort b (equivFun equivalence x)
precompose : {b : F.Object} {u v : Body (fst b)}
  (e : G.Carrier u ≃ G.Carrier v) (p : equivFun e (G.point u) ≡ G.point v)
  (h : (x : G.Carrier u) → reader u x ≡ reader v (equivFun e x))
  → View b v → View b u
precompose e p h (view f q k) = view (compEquiv e f) (cong (equivFun f) p ∙ q)
  (λ x → h x ∙ k (equivFun e x))
compiledView : {m : Mode} {a b : F.Object} (f : F.Full m a b) → View b (C.compiledView f)
compiledView {b = b} (F.full (e , p , h)) = view (compEquiv (Native.graphEquiv e) e) p
  (λ { (x , y , w) → sym (cong (F.readPort b) w) })
joinView : {m n : Mode} {a b c : F.Object} (f : F.Full m a b) (g : F.Full n b c)
  → View c (Join.Bridge.retainedBody f g)
joinView f g = precompose (Join.Bridge.carrierEquiv f g) (Join.Bridge.selected f g)
  (λ _ → refl) (compiledView (F.compose f g))
attachView : {m : Mode} {a b : F.Object} (f : F.Full m a b) (o : Out (fst a))
  → View (M.attachObject b (M.route f o)) (Attach.Bridge.retainedBody f o)
attachView f o = precompose (invEquiv e)
  (sym (cong (invEq e) (Attach.Bridge.selected f o)) ∙ retEq e (G.point (Attach.Bridge.compiledBody f o)))
  (λ y → sym (Attach.Bridge.ports f o (invEq e y)
    ∙ cong (reader (Attach.Bridge.retainedBody f o)) (secEq e y)))
  (compiledView (M.attachment f o))
  where e = Attach.Bridge.carrierEquiv f o
coreView : {m : Mode} {a b : F.Object} (t : F.Tree m a b) → View b (C.coreRoot t)
coreView (F.cell f) = compiledView f
coreView (F.unit a) = compiledView (F.identity a)
coreView (F.then r s) = joinView (F.fold r) (F.fold s)
rootView : {m : Mode} {a b : F.Object} (t : M.Tree m a b) → View b (C.root t)
rootView (M.old t) = coreView t
rootView (M.join r s) = joinView (M.fold r) (M.fold s)
rootView (M.attach r o) = attachView (M.fold r) o

rootNormal : {m : Mode} {a b : F.Object} (t : M.Tree m a b) → G.Normal (C.root t)
G.Normal.shape (rootNormal {b = b} t) = G.Normal.shape (G.normal (snd b))
G.Normal.equivalence (rootNormal {b = b} t) = compEquiv (View.equivalence (rootView t))
  (G.Normal.equivalence (G.normal (snd b)))
G.Normal.ports (rootNormal {b = b} t) x = View.ports (rootView t) x
  ∙ G.Normal.ports (G.normal (snd b)) (equivFun (View.equivalence (rootView t)) x)

root-boundary : {m : Mode} {a b : F.Object} (r s : M.Tree m a b) → C.RootBoundary r s
root-boundary {b = b} r s = compEquiv er (invEquiv es)
  , (cong (invEq es) (View.point (rootView r))
    ∙ sym (cong (invEq es) (View.point (rootView s))) ∙ retEq es (G.point (C.root s)))
  , (λ x → View.ports (rootView r) x
    ∙ sym (View.ports (rootView s) (invEq es (equivFun er x))
      ∙ cong (F.readPort b) (secEq es (equivFun er x))))
  where
  er = View.equivalence (rootView r)
  es = View.equivalence (rootView s)
abstract
  boundary-prop : {m : Mode} {a b : F.Object} (r s : M.Tree m a b) → isProp (C.RootBoundary r s)
  boundary-prop r s (e , p , h) (e' , p' , h') = Σ≡Prop
    (λ e → isProp× (G.carrier-set (rootNormal s) _ _) (isPropΠ (λ _ → vertex-is-set _ _)))
    (equivEq (funExt (λ x → G.reader-injective (rootNormal s) _ _ (sym (h x) ∙ h' x))))
boundary-contractible : {m : Mode} {a b : F.Object} (r s : M.Tree m a b) → isContr (C.RootBoundary r s)
boundary-contractible r s = root-boundary r s , boundary-prop r s (root-boundary r s)

asBody : {m : Mode} {a b : F.Object} (r s : M.Tree m a b) → C.RootBoundary r s → Body (fst b)
asBody r s (e , p , h) = compare stay (C.root r) (C.root s) e p h
native : {m : Mode} {a b : F.Object} (r s : M.Tree m a b) (w : C.RootBoundary r s)
  → Resolve Seeds (package (asBody r s w))
native r s w = derivation (asBody r s w)
root-operands-recovered : {m : Mode} {a b : F.Object} (r s : M.Tree m a b) (w : C.RootBoundary r s)
  → Native.comparisonOperands (Native.closure (fst b , asBody r s w))
    ≡ just (Native.closure (fst b , C.root r) , Native.closure (fst b , C.root s))
root-operands-recovered r s (e , p , h) = refl
full-value-recovered : {m : Mode} {a b : F.Object} (r s : M.Tree m a b) (x : G.Carrier (C.root r))
  → invEq (fst (root-boundary r s)) (equivFun (fst (root-boundary r s)) x) ≡ x
full-value-recovered r s = retEq (fst (root-boundary r s))
composeBoundary : {m : Mode} {a b : F.Object} {r s t : M.Tree m a b}
  → C.RootBoundary r s → C.RootBoundary s t → C.RootBoundary r t
composeBoundary (e , p , h) (f , q , k) = compEquiv e f , (cong (equivFun f) p ∙ q)
  , (λ x → h x ∙ k (equivFun e x))
triangle : {m : Mode} {a b : F.Object} (r s t : M.Tree m a b)
  → composeBoundary {r = r} {s} {t} (root-boundary r s) (root-boundary s t) ≡ root-boundary r t
triangle r s t = boundary-prop r t _ _

module Higher {m : Mode} {a b : F.Object} (r s : M.Tree m a b) where
  module E = Envelope.Envelope (C.RootBoundary r s) (λ w → package (asBody r s w)) (native r s)
  coherence : (u v : C.RootBoundary r s) → u ≡ v
  coherence = boundary-prop r s
  path-native : (u v : C.RootBoundary r s)
    → Resolve Seeds (path-package E.CodeE (E.section u) (E.section v) (E.liftPath (coherence u v)))
  path-native u v = E.path-native (coherence u v)
  square : {u v : C.RootBoundary r s} (p q : u ≡ v) → p ≡ q
  square {u} {v} = isProp→isSet (boundary-prop r s) u v
  square-native : {u v : C.RootBoundary r s} (p q : u ≡ v)
    → Resolve Seeds (higher-package E.CodeE (E.section u) (E.section v)
      (E.liftPath p) (E.liftPath q) (E.liftHigher (square p q)))
  square-native p q = E.higher-native (square p q)

unrestricted-normalization-refused : ¬ G.Normal G.hidden
unrestricted-normalization-refused n = G.hidden-not-injective (G.reader-injective n)

module TriangleAdmission {m : Mode} {a b : F.Object} (r s t : M.Tree m a b) where
  module H = Higher r t
  composed = composeBoundary {r = r} {s} {t} (root-boundary r s) (root-boundary s t)
  admitted-triangle : Resolve Seeds (path-package H.E.CodeE
    (H.E.section composed) (H.E.section (root-boundary r t)) (H.E.liftPath (triangle r s t)))
  admitted-triangle = H.E.path-native (triangle r s t)
