{-# OPTIONS --safe --cubical --guardedness #-}
module SourceCertifiedPrograms where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism using (isoToEquiv)
open import Cubical.Foundations.GroupoidLaws using (rUnit)
open import Cubical.Data.Bool using (Bool; true; false; false≢true; isSetBool)
open import Cubical.Data.Sum using (_⊎_; inl; inr)
open import Cubical.Data.Empty using (⊥)
open import NativeExtensionFamilyAudit using (Vertex; A; B; C; AB; CA; Seeds; root; pointQ)
open import SourceIndexedExtensionFamilies using (Out)
open import InternalSourceComparisons using (Mode; stay; exchange; act; package; derivation)
import GeneratedReaderClassification as G
import CanonicalComparisonSynthesis as Compile
import HigherWitnessAdmission as H
import CoherentDependentExtensions as General
import ResolutionMapIntroductionGap as Gap
import GeneratedContinuationContexts as Contexts
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero hiding (output)

-- CLOSED relative to the declared four-point seed policy. No arbitrary
-- Resolve proof, Body, Type, function, equivalence or family import constructor.
-- Control choices (vertex, edge, mode, program tree) remain explicit inputs.
mutual
  data Program : Vertex → Type₁ where
    seedP : (v : Vertex) → Program v
    attachP : {v : Vertex} (p : Program v) (o : Out v) → Program (fst o)
    compareP : (m : Mode) {v : Vertex} (p : Program v) (q : Program (act m v))
      → Compile.Compile.accepted m (decode p) (decode q)
          (Compile.Compile.compile m (decode p) (decode q)) ≡ true
      → Program (act m v)

  decode : {v : Vertex} → Program v → G.Fragment v
  decode (seedP v) = G.start v (root v)
  decode (attachP p o) = G.attachF (decode p) o
  decode (compareP m p q ok) = K.next (K.require-success K.compile ok)
    where module K = Compile.Compile m (decode p) (decode q)

native : {v : Vertex} (p : Program v) → Resolve Seeds (package (G.body (decode p)))
native p = G.native (decode p)

module Pair (m : Mode) {v : Vertex} (p : Program v) (q : Program (act m v)) where
  module K = Compile.Compile m (decode p) (decode q)
  Guard = K.accepted K.compile ≡ true
  -- A checked success guard is proposition-valued, not a hidden payload port.
  guard-prop : isProp Guard
  guard-prop = isSetBool _ _
  guard-irrelevant : (u w : Guard) → compareP m p q u ≡ compareP m p q w
  guard-irrelevant u w = cong (compareP m p q) (guard-prop u w)
  build : Program (act m v) ⊎ K.Refusal
  build with K.compile
  ... | inl f = inl (compareP m p q (K.complete f))
  ... | inr bad = inr bad

-- Higher-family producer: all decisive parameters are computed from TWO
-- certified operands and a checked guard. No arbitrary filler/path/alpha input.
module Higher (m : Mode) {v : Vertex} (p : Program v) (q : Program (act m v))
  (ok : Pair.Guard m p q) where
  module K = Compile.Compile m (decode p) (decode q)
  module Cmp = K.C
  Filler = Cmp.Filler
  leftFiller : Filler
  leftFiller = K.require-success K.compile ok
  -- A second explicitly generated construction: right-unit normalization of
  -- the pointed witness. The full e and reader witness are retained.
  rightFiller : Filler
  rightFiller = fst leftFiller , (fst (snd leftFiller) ∙ refl) , snd (snd leftFiller)
  coherence : leftFiller ≡ rightFiller
  coherence = Cmp.filler-prop leftFiller rightFiller
  term : Filler → G.Fragment (act m v)
  term = K.next
  branch : Filler → Complete
  branch f = path-package (expression (package (G.body (term f))))
    (value (package (G.body (term f)))) (value (package (G.body (term f)))) refl
  branch-derived : (f : Filler) → Resolve Seeds (branch f)
  branch-derived f = apply
    (reflexivity-rule (expression (package (G.body (term f)))) (value (package (G.body (term f)))))
    (λ _ → G.native (term f))
  EnvelopeCode : Code
  EnvelopeCode = E Filler (λ f → retained (branch f))
  envelope : Filler → Complete
  envelope f = E-package Filler branch f
  envelope-derived : (f : Filler) → Resolve Seeds (envelope f)
  envelope-derived f = apply (E-rule Filler branch f) (λ { (lift g) → branch-derived g })
  branch-contractible : (f : Filler) → isContr (El (retained (branch f)))
  branch-contractible f = refl , (λ loop → G.carrier-set (G.normal (term f)) _ _ refl loop)
  module Projection = General.Projection Filler (λ f → El (retained (branch f)))
  envelopeEquiv : El EnvelopeCode ≃ Filler
  envelopeEquiv = isoToEquiv (Projection.contractible-projection branch-contractible)
  left right : El EnvelopeCode
  left = value (envelope leftFiller)
  right = value (envelope rightFiller)
  path : left ≡ right
  path i = coherence i , refl
  recovered-path : cong fst path ≡ coherence
  recovered-path = refl
  output : Complete
  output = path-package EnvelopeCode left right path
  module Admit = H.PathAdmission Seeds
  admitted : Resolve Seeds output
  admitted = Admit.from-derived-point EnvelopeCode left (envelope-derived leftFiller) path
  normalizedPath = path ∙ refl
  normalized-derived : Resolve Seeds (path-package EnvelopeCode left right normalizedPath)
  normalized-derived = Admit.from-derived-point EnvelopeCode left (envelope-derived leftFiller) normalizedPath
  alpha : path ≡ normalizedPath
  alpha = rUnit path
  higherOutput : Complete
  higherOutput = higher-package EnvelopeCode left right path normalizedPath alpha
  higher-admitted : Resolve Seeds higherOutput
  higher-admitted = apply (higher-rule EnvelopeCode left right path normalizedPath alpha)
    (λ { (lift true) → admitted ; (lift false) → normalized-derived })

-- The higher producers are explicit syntax, not an arbitrary Complete/Resolve
-- escape hatch. In particular no raw-path constructor delegates origin to J.
data Command : Type₁ where
  bodyP : {v : Vertex} → Program v → Command
  coherenceP unitHigherP : (m : Mode) {v : Vertex} (p : Program v) (q : Program (act m v))
    → Pair.Guard m p q → Command
output : Command → Complete
output (bodyP p) = package (G.body (decode p))
output (coherenceP m p q ok) = Higher.output m p q ok
output (unitHigherP m p q ok) = Higher.higherOutput m p q ok
derive : (c : Command) → Resolve Seeds (output c)
derive (bodyP p) = native p
derive (coherenceP m p q ok) = Higher.admitted m p q ok
derive (unitHigherP m p q ok) = Higher.higher-admitted m p q ok

-- A producer certificate identifies BOTH the output and its actual native
-- derivation, up to the explicitly recorded dependent equality. Existence
-- does not establish a unique historical producer of an arbitrary old proof.
Produced : (q : Complete) → Resolve Seeds q → Type₁
Produced q d = Σ[ c ∈ Command ] Σ[ same ∈ (output c ≡ q) ]
  PathP (λ i → Resolve Seeds (same i)) (derive c) d
produced : (c : Command) → Produced (output c) (derive c)
produced c = c , refl , refl

-- Exact-presentation hostile: replay arbitrary function injection using the
-- ORIGINAL graph seeds, not the predecessor's separately declared Unit seed.
piRoot : Code → Bool
piRoot (Pi _ _) = true
piRoot _ = false
comparison-no-pi : (m : Mode) {v : Vertex} (a : G.Fragment v) (b : G.Fragment (act m v))
  (f : G.Comparisons.Filler m a b)
  → piRoot (expression (package (G.body (Compile.Compile.next m a b f)))) ≡ false
comparison-no-pi m a b (e , point , ports) = refl
program-no-pi : {v : Vertex} (p : Program v) → piRoot (expression (package (G.body (decode p)))) ≡ false
program-no-pi (seedP v) = refl
program-no-pi (attachP p o) = refl
program-no-pi (compareP m p q ok) = comparison-no-pi m (decode p) (decode q)
  (Compile.Compile.require-success m (decode p) (decode q)
    (Compile.Compile.compile m (decode p) (decode q)) ok)
command-no-pi : (c : Command) → piRoot (expression (output c)) ≡ false
command-no-pi (bodyP p) = program-no-pi p
command-no-pi (coherenceP m p q ok) = refl
command-no-pi (unitHigherP m p q ok) = refl

module SuppliedFunction (X Y : Type) (f : X → Y) where
  family : X → Complete
  family x = E-package Y (λ _ → pointQ A) (f x)
  family-derived : (x : X) → Resolve Seeds (family x)
  family-derived x = apply (E-rule Y (λ _ → pointQ A) (f x)) (λ _ → root A)
  encoded : Complete
  encoded = Pi-package X family
  admitted : Resolve Seeds encoded
  admitted = apply (Pi-rule X family) (λ { (lift x) → family-derived x })
  recovered : (x : X) → fst (value encoded x) ≡ f x
  recovered x = refl
  not-produced : Produced encoded admitted → ⊥
  not-produced (c , same , history) = false≢true
    (sym (command-no-pi c) ∙ cong (λ q → piRoot (expression q)) same)

-- Reuse both predecessor boundaries. Their generated-map extension is NOT
-- installed in this evaluator; derive above targets original Resolve Seeds.
old-map-introduction-boundary = Gap.Gap.no-unseeded-map-package ℓ-zero
context-extension-boundary = Contexts.not-old-generated

-- Concrete generated producer and genuinely higher-rule output.
module Example = Pair exchange (seedP A) (seedP B)
example-ok : Example.Guard
example-ok = refl
example : Program B
example = compareP exchange (seedP A) (seedP B) example-ok
example-certificate = produced (bodyP example)
higher-certificate = produced (unitHigherP exchange (seedP A) (seedP B) example-ok)
module Mismatch = Pair stay (seedP A) (attachP (seedP C) (A , CA))
mismatch-rejected : Mismatch.K.accepted Mismatch.K.compile ≡ false
mismatch-rejected = refl
