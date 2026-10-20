{-# OPTIONS --safe --cubical --guardedness #-}
module NativeComposeHistoryBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Relation.Nullary.Base using (¬_)
open import NativeExtensionFamilyAudit using (Seeds)
open import SourceIndexedExtensionFamilies using (Out)
open import InternalSourceComparisons using (Mode; stay; Body; prepared; compare; package; derivation; aligned)
import FiniteComparisonTrees as F
import GeneratedReaderClassification as G
import InternalComparisonInterchange as Native
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

composeOperands : Closure Seeds → Maybe (Closure Seeds × Closure Seeds)
composeOperands (_ , apply (compose-rule a b c e f p q) ds) =
  just ((comparison-package a b e p , ds (lift true))
       , (comparison-package b c f q , ds (lift false)))
composeOperands _ = nothing
retainedTag : Code → Bool
retainedTag (retain _ _ _) = true
retainedTag _ = false

module Bridge {m n : Mode} {a b c : F.Object} (f : F.Full m a b) (g : F.Full n b c) where
  e = fst (F.Full.payload f)
  e' = fst (F.Full.payload g)
  p = fst (snd (F.Full.payload f))
  p' = fst (snd (F.Full.payload g))
  qa = package (G.body (snd a))
  qb = package (G.body (snd b))
  qc = package (G.body (snd c))
  retainedPackage = compose-comparisons qa qb qc e e' p p'
  retained-native : Resolve Seeds retainedPackage
  retained-native = apply (compose-rule qa qb qc e e' p p')
    (λ { (lift true) → F.admitted f ; (lift false) → F.admitted g })
  compiledPackage = F.asPackage (F.compose f g)
  compiled-native : Resolve Seeds compiledPackage
  compiled-native = F.admitted (F.compose f g)
  premises-retained : composeOperands (retainedPackage , retained-native)
    ≡ just ((F.asPackage f , F.admitted f) , (F.asPackage g , F.admitted g))
  premises-retained = refl
  carrierEquiv : El (expression retainedPackage) ≃ El (expression compiledPackage)
  carrierEquiv = idEquiv _
  selected : equivFun carrierEquiv (value retainedPackage) ≡ value compiledPackage
  selected = refl
  packages-not-equal : ¬ (retainedPackage ≡ compiledPackage)
  packages-not-equal q = true≢false (cong (λ z → retainedTag (expression z)) q)

  -- Reframe neither endpoint history: these are explicit prepared views of
  -- the two ACTUALLY derived packages, with the same existing target reader.
  retainedBody compiledBody : Body (fst c)
  retainedBody = prepared (fst c) retainedPackage retained-native
    (λ z → F.readPort c (fst (snd z))) (aligned (G.body (snd c)))
  compiledBody = prepared (fst c) compiledPackage compiled-native
    (λ z → F.readPort c (fst (snd z))) (aligned (G.body (snd c)))
  bridgeBody : Body (fst c)
  bridgeBody = compare stay retainedBody compiledBody carrierEquiv selected (λ _ → refl)
  bridge-native : Resolve Seeds (package bridgeBody)
  bridge-native = derivation bridgeBody
  both-histories-retained : Native.comparisonOperands (Native.closure (fst c , bridgeBody))
    ≡ just ((retainedPackage , retained-native) , (compiledPackage , compiled-native))
  both-histories-retained = refl
  module Continued = Native.Interchange stay (fst c) retainedBody compiledBody carrierEquiv selected (λ _ → refl)
  continued-native : (o : Out (fst c)) → Resolve Seeds (package (Continued.interchange o))
  continued-native o = derivation (Continued.interchange o)
