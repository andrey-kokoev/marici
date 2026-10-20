{-# OPTIONS --safe --cubical --guardedness #-}
module MixedComparisonTrees where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence using (pathToEquiv)
open import Cubical.Foundations.Transport using (substEquiv)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv)
open import Cubical.Data.Maybe.Base using (just)
open import NativeExtensionFamilyAudit using (Seeds)
open import SourceIndexedExtensionFamilies using (Out)
open import InternalSourceComparisons using (Mode; act; edgeEquiv; edge-target; loopEquiv; loop-refl; Body; prepared; compare; stay; package; derivation)
import GeneratedReaderClassification as G
import FiniteComparisonTrees as F
import ForwardSourceLiftComposition as Modes
import SourceIndexedContinuationAdapter as Adapter
import NativeComposeHistoryBridge as History
import InternalComparisonInterchange as Native
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

attachObject : (a : F.Object) → Out (fst a) → F.Object
attachObject a o = fst o , G.attachF (snd a) o
requests : {m : Mode} {a b : F.Object} → F.Full m a b → Out (fst a) ≃ Out (fst b)
requests {m} {a} f = compEquiv (edgeEquiv m (fst a)) (substEquiv Out (F.frame f))
route : {m : Mode} {a b : F.Object} → F.Full m a b → Out (fst a) → Out (fst b)
route f = equivFun (requests f)
return-port : {m : Mode} {a b : F.Object} (f : F.Full m a b) (o : Out (fst a))
  → act m (fst o) ≡ fst (route f o)
return-port {m} {a} f o = edge-target m (fst a) o
  ∙ sym (Adapter.transport-target (F.frame f) (equivFun (edgeEquiv m (fst a)) o))
attachment : {m : Mode} {a b : F.Object} (f : F.Full m a b) (o : Out (fst a))
  → F.Full m (attachObject a o) (attachObject b (route f o))
attachment {m} {a} {b} f@(F.full (e , p , h)) o = F.full
  (Σ-cong-equiv (requests f) (λ _ → loopEquiv e p)
  , (λ i → route f o , loop-refl e {x = F.point a} {y = F.point b} p i)
  , (λ q → return-port f (fst q)))

-- The whole subtree is retained by the attachment constructor. Routing is
-- computed from its fold: no independently selected target request/filler.
mutual
  data Tree : Mode → F.Object → F.Object → Type₁ where
    old : {m : Mode} {a b : F.Object} → F.Tree m a b → Tree m a b
    join : {m n : Mode} {a b c : F.Object}
      → Tree m a b → Tree n b c → Tree (Modes.product n m) a c
    attach : {m : Mode} {a b : F.Object} (t : Tree m a b) (o : Out (fst a))
      → Tree m (attachObject a o) (attachObject b (route (fold t) o))
  fold : {m : Mode} {a b : F.Object} → Tree m a b → F.Full m a b
  fold (old t) = F.fold t
  fold (join r s) = F.compose (fold r) (fold s)
  fold (attach t o) = attachment (fold t) o

coherence : {m : Mode} {a b : F.Object} (r s : Tree m a b) → fold r ≡ fold s
coherence {m} {a} {b} r s = F.full-prop m a b (fold r) (fold s)
native-coherence : {m : Mode} {a b : F.Object} (r s : Tree m a b)
  → PathP (λ i → Resolve Seeds (F.asPackage (coherence r s i)))
      (F.admitted (fold r)) (F.admitted (fold s))
native-coherence r s i = F.admitted (coherence r s i)

-- Endpoint labels agree by mode composition and the actual return laws.
-- Reader injectivity for this declared Out carrier then recovers the edge.
route-composition : {m n : Mode} {a b c : F.Object}
  (f : F.Full m a b) (g : F.Full n b c) (o : Out (fst a))
  → route (F.compose f g) o ≡ route g (route f o)
route-composition {m} {n} {a} {c = c} f g o = G.port-injective (G.outgoing (fst c)) _ _
  (sym (return-port (F.compose f g) o) ∙ sym (F.act-product n m (fst o))
    ∙ cong (act n) (return-port f o) ∙ return-port g (route f o))

mixed-boundary : {m n : Mode} {a b c : F.Object}
  (f : F.Full m a b) (g : F.Full n b c) (o : Out (fst a))
  → PathP (λ i → F.Full (Modes.product n m) (attachObject a o)
      (attachObject c (route-composition f g o i)))
      (attachment (F.compose f g) o)
      (F.compose (attachment f o) (attachment g (route f o)))
mixed-boundary {m} {n} {a} {c = c} f g o = isProp→PathP
  (λ i → F.full-prop (Modes.product n m) (attachObject a o)
    (attachObject c (route-composition f g o i))) _ _
mixed-native : {m n : Mode} {a b c : F.Object}
  (f : F.Full m a b) (g : F.Full n b c) (o : Out (fst a))
  → PathP (λ i → Resolve Seeds (F.asPackage (mixed-boundary f g o i)))
      (F.admitted (attachment (F.compose f g) o))
      (F.admitted (F.compose (attachment f o) (attachment g (route f o))))
mixed-native f g o i = F.admitted (mixed-boundary f g o i)

-- The actual retained sequential compose-rule history is compared to the
-- fused attachment, not substituted for its endpoint-comparison derivation.
module MixedHistory {m n : Mode} {a b c : F.Object}
  (f : F.Full m a b) (g : F.Full n b c) (o : Out (fst a)) where
  module H = History.Bridge (attachment f o) (attachment g (route f o))
  packagePath : F.asPackage (attachment (F.compose f g) o)
    ≡ F.asPackage (F.compose (attachment f o) (attachment g (route f o)))
  packagePath i = F.asPackage (mixed-boundary f g o i)
  carrierPath : El (expression H.retainedPackage)
    ≡ El (expression (F.asPackage (attachment (F.compose f g) o)))
  carrierPath i = El (expression (packagePath (~ i)))
  bridgeEquiv = pathToEquiv carrierPath
  bridgePoint : equivFun bridgeEquiv (value H.retainedPackage)
    ≡ value (F.asPackage (attachment (F.compose f g) o))
  bridgePoint = fromPathP (λ i → value (packagePath (~ i)))
  readAt : (i : I) → El (expression (packagePath i)) → NativeExtensionFamilyAudit.Vertex
  readAt i z = F.readPort (attachObject c (route-composition f g o i)) (fst (snd z))
  fusedBody : Body (fst (route g (route f o)))
  fusedBody = prepared _ (F.asPackage (attachment (F.compose f g) o))
    (F.admitted (attachment (F.compose f g) o)) (readAt i0)
    (cong fst (route-composition f g o))
  bridgePorts : (z : El (expression H.retainedPackage))
    → readAt i1 z ≡ readAt i0 (equivFun bridgeEquiv z)
  bridgePorts z i = readAt (~ i) (transport-filler carrierPath z i)
  bridgeBody : Body (fst (route g (route f o)))
  bridgeBody = compare stay H.retainedBody fusedBody bridgeEquiv bridgePoint bridgePorts
  bridge-native : Resolve Seeds (package bridgeBody)
  bridge-native = derivation bridgeBody
  both-histories-retained : Native.comparisonOperands
      (Native.closure (fst (route g (route f o)) , bridgeBody))
    ≡ just ((H.retainedPackage , H.retained-native) , (package fusedBody , derivation fusedBody))
  both-histories-retained = refl
  sequential-premises-retained = H.premises-retained
