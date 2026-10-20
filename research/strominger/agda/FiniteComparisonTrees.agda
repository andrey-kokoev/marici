{-# OPTIONS --safe --cubical --guardedness #-}
module FiniteComparisonTrees where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels using (isProp×; isPropΠ)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (true; false)
open import NativeExtensionFamilyAudit using (Vertex; Seeds; sigma²)
open import SourceIndexedExtensionFamilies using (vertex-is-set)
open import InternalSourceComparisons using (Mode; stay; exchange; act; reader; package; aligned)
import GeneratedReaderClassification as G
import ForwardSourceLiftComposition as Modes
import SourceModeCoherence as Laws
import NonsetWitnessEnvelopes as Envelope
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

Object : Type₁
Object = Σ Vertex G.Fragment
Carrier : Object → Type
Carrier a = G.Carrier (G.body (snd a))
point : (a : Object) → Carrier a
point a = G.point (G.body (snd a))
readPort : (a : Object) → Carrier a → Vertex
readPort a = reader (G.body (snd a))

-- Endpoints have arbitrary explicit vertex indices. No implicit transport of
-- a whole native history is hidden in a mode-product associativity cast.
Payload : Mode → Object → Object → Type
Payload m a b = Σ[ e ∈ (Carrier a ≃ Carrier b) ]
  (equivFun e (point a) ≡ point b) × ((x : Carrier a) → act m (readPort a x) ≡ readPort b (equivFun e x))
record Full (m : Mode) (a b : Object) : Type where
  constructor full
  field payload : Payload m a b
abstract
  full-prop : (m : Mode) (a b : Object) → isProp (Full m a b)
  full-prop m a b (full (e , p , h)) (full (e' , p' , h')) = cong full (Σ≡Prop
    (λ e → isProp× (G.carrier-set (G.normal (snd b)) _ _)
      (isPropΠ (λ x → vertex-is-set _ _)))
    (equivEq (funExt (λ x → G.reader-injective (G.normal (snd b)) _ _ (sym (h x) ∙ h' x)))))

frame : {m : Mode} {a b : Object} → Full m a b → act m (fst a) ≡ fst b
frame {m} {a} {b} (full (e , p , h)) = sym (cong (act m) (aligned (G.body (snd a))))
  ∙ h (point a) ∙ cong (readPort b) p ∙ aligned (G.body (snd b))

act-product : (m n : Mode) (v : Vertex) → act m (act n v) ≡ act (Modes.product m n) v
act-product stay n v = refl
act-product exchange stay v = refl
act-product exchange exchange v = sigma² v
identity : (a : Object) → Full stay a a
identity a = full (idEquiv _ , refl , (λ _ → refl))
compose : {m n : Mode} {a b c : Object} → Full m a b → Full n b c → Full (Modes.product n m) a c
compose {m} {n} {a} (full (e , p , h)) (full (f , q , k)) = full (compEquiv e f ,
  (cong (equivFun f) p ∙ q) , (λ x → sym (act-product n m (readPort a x))
    ∙ cong (act n) (h x) ∙ k (equivFun e x)))

-- This syntax retains its actual supplied cells and intermediate objects.
-- No assertion that distinct syntax trees or native histories are equal.
data Tree : Mode → Object → Object → Type₁ where
  cell : {m : Mode} {a b : Object} → Full m a b → Tree m a b
  unit : (a : Object) → Tree stay a a
  then : {m n : Mode} {a b c : Object}
    → Tree m a b → Tree n b c → Tree (Modes.product n m) a c
fold : {m : Mode} {a b : Object} → Tree m a b → Full m a b
fold (cell f) = f
fold (unit a) = identity a
fold (then r s) = compose (fold r) (fold s)
coherence : {m : Mode} {a b : Object} (r s : Tree m a b) → fold r ≡ fold s
coherence {m} {a} {b} r s = full-prop m a b (fold r) (fold s)
contractible-evaluations : {m : Mode} {a b : Object} → Tree m a b → isContr (Full m a b)
contractible-evaluations {m} {a} {b} t = fold t , full-prop m a b (fold t)

from-generated : (m : Mode) {v : Vertex} (a : G.Fragment v) (b : G.Fragment (act m v))
  → G.Comparisons.Filler m a b → Full m (v , a) (act m v , b)
from-generated m a b f = full f

asPackage : {m : Mode} {a b : Object} → Full m a b → Complete
asPackage {a = a} {b} (full (e , p , h)) = comparison-package (package (G.body (snd a))) (package (G.body (snd b))) e p
admitted : {m : Mode} {a b : Object} (f : Full m a b) → Resolve Seeds (asPackage f)
admitted {a = a} {b} (full (e , p , h)) = apply
  (compare-rule (package (G.body (snd a))) (package (G.body (snd b))) e p)
  (λ { (lift true) → G.native (snd a) ; (lift false) → G.native (snd b) })
generated-admission-binding : (m : Mode) {v : Vertex} (a : G.Fragment v) (b : G.Fragment (act m v))
  (f : G.Comparisons.Filler m a b)
  → admitted (from-generated m a b f) ≡ G.Comparisons.admitted m a b f
generated-admission-binding m a b (e , p , h) =
  cong (apply (compare-rule (package (G.body a)) (package (G.body b)) e p))
    (funExt (λ { (lift true) → refl ; (lift false) → refl }))

native-coherence : {m : Mode} {a b : Object} (r s : Tree m a b)
  → PathP (λ i → Resolve Seeds (asPackage (coherence r s i))) (admitted (fold r)) (admitted (fold s))
native-coherence r s i = admitted (coherence r s i)

-- Retain the complete tree alongside its evaluated comparison and derivation.
record Certificate {m : Mode} {a b : Object} (t : Tree m a b) : Type₁ where
  field
    retainedTree : Tree m a b
    treeRecovery : retainedTree ≡ t
    evaluated : Full m a b
    evaluationRecovery : evaluated ≡ fold t
    nativeWitness : Resolve Seeds (asPackage evaluated)
certificate : {m : Mode} {a b : Object} (t : Tree m a b) → Certificate t
Certificate.retainedTree (certificate t) = t
Certificate.treeRecovery (certificate t) = refl
Certificate.evaluated (certificate t) = fold t
Certificate.evaluationRecovery (certificate t) = refl
Certificate.nativeWitness (certificate t) = admitted (fold t)

-- Associativity explicitly accounts for the mode-product endpoint path.
associativity : {m n k : Mode} {a b c d : Object}
  (r : Tree m a b) (s : Tree n b c) (t : Tree k c d)
  → transport (λ i → Full (Laws.product-assoc k n m i) a d) (fold (then r (then s t)))
    ≡ fold (then (then r s) t)
associativity {m} {n} {k} {a} {d = d} r s t = full-prop (Modes.product k (Modes.product n m)) a d _ _

right-unit : {m : Mode} {a b : Object} (r : Tree m a b)
  → fold (then r (unit b)) ≡ fold r
right-unit {b = b} r = coherence (then r (unit b)) r
left-unit : {m : Mode} {a b : Object} (r : Tree m a b)
  → PathP (λ i → Full (Laws.right-unit-product m i) a b) (fold (then (unit a) r)) (fold r)
left-unit {m} {a} {b} r = isProp→PathP (λ i → full-prop (Laws.right-unit-product m i) a b) _ _

module Higher (m : Mode) (a b : Object) where
  module E = Envelope.Envelope (Full m a b) asPackage admitted
  path-native : (r s : Tree m a b)
    → Resolve Seeds (path-package E.CodeE (E.section (fold r)) (E.section (fold s)) (E.liftPath (coherence r s)))
  path-native r s = E.path-native (coherence r s)
  square : (r s : Tree m a b) (p q : fold r ≡ fold s) → p ≡ q
  square r s = isProp→isSet (full-prop m a b) (fold r) (fold s)
  square-native : (r s : Tree m a b) (p q : fold r ≡ fold s)
    → Resolve Seeds (higher-package E.CodeE (E.section (fold r)) (E.section (fold s))
      (E.liftPath p) (E.liftPath q) (E.liftHigher (square r s p q)))
  square-native r s p q = E.higher-native (square r s p q)
