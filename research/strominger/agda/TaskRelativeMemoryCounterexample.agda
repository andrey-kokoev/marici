{-# OPTIONS --safe --cubical --guardedness #-}
module TaskRelativeMemoryCounterexample where

open import Cubical.Foundations.Prelude hiding (Path)
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool using (Bool; true; false; notEquiv; false≢true)
open import Cubical.Data.Empty using (⊥)
open import ActualSeedEndpointTable
import SeedSeamPathComparisonBoundary as W
import SeedFirstReturnActions as Actions
import SeedGeometricResponseInterpretation as Interpret
import OriginalRuleGeometricCompiler as Compiler

-- Two closed policies in the SAME permitted Boolean-permutation grammar.
-- No fitted real coefficient, new edge, or added observation is involved.
data Policy : Type where
  red green : Policy
edgeEquiv : Policy → (e : Occurrence) → Bool ≃ Bool
edgeEquiv red AB = notEquiv
edgeEquiv red BA = notEquiv
edgeEquiv red BC = idEquiv Bool
edgeEquiv red CA = idEquiv Bool
edgeEquiv red AD = idEquiv Bool
edgeEquiv red DB = idEquiv Bool
edgeEquiv green BC = notEquiv
edgeEquiv green AD = notEquiv
edgeEquiv green AB = idEquiv Bool
edgeEquiv green BA = idEquiv Bool
edgeEquiv green CA = idEquiv Bool
edgeEquiv green DB = idEquiv Bool

swap : Occurrence → Occurrence
swap AB = BA
swap BA = AB
swap BC = AD
swap AD = BC
swap CA = DB
swap DB = CA
covariant : (p : Policy) (e : Occurrence) (b : Bool)
  → equivFun (edgeEquiv p (swap e)) b ≡ equivFun (edgeEquiv p e) b
covariant red AB b = refl
covariant red BA b = refl
covariant red BC b = refl
covariant red AD b = refl
covariant red CA b = refl
covariant red DB b = refl
covariant green AB b = refl
covariant green BA b = refl
covariant green BC b = refl
covariant green AD b = refl
covariant green CA b = refl
covariant green DB b = refl

module Model (p : Policy) where
  module I = Interpret.Interpret (λ _ → Bool) (edgeEquiv p) false
  read : {v : Vertex} → W.Path A v → Bool
  read w = I.read (Compiler.current (Compiler.compile w))
  -- This is a comparison to actual ORIGINAL-rule compilation, not merely
  -- evaluation of a freely supplied matrix or extension derivation.
  native-agrees : {v : Vertex} (w : W.Path A v) → read w ≡ I.E.run w false
  native-agrees w = cong I.read (Compiler.extension-agrees w) ∙ I.native-square w
  composition : {s m t : Vertex} (a : W.Path s m) (b : W.Path m t) (x : Bool)
    → I.E.run (Actions.append a b) x ≡ I.E.run b (I.E.run a x)
  composition = I.E.run-append

module R = Model red
module G = Model green
prefix : W.Path A A
prefix = W.step AB (W.step BC (W.step CA W.stop))
continuation : W.Path A B
continuation = W.x0
later : W.Path A B
later = Actions.append prefix continuation

-- Both have a nontrivial closed write cycle, not an inert countermodel.
red-cycle : R.read prefix ≡ true
red-cycle = R.native-agrees prefix
green-cycle : G.read prefix ≡ true
green-cycle = G.native-agrees prefix
same-present : R.read prefix ≡ G.read prefix
same-present = red-cycle ∙ sym green-cycle
red-later : R.read later ≡ false
red-later = R.native-agrees later
green-later : G.read later ≡ true
green-later = G.native-agrees later
future-distinct : R.read later ≡ G.read later → ⊥
future-distinct p = false≢true (sym red-later ∙ p ∙ green-later)

-- Every vertex/bit configuration is realized by an actual compiled word.
toC : W.Path A C
toC = W.step AB (W.step BC W.stop)
toD : W.Path A D
toD = W.step AD W.stop
witness : Policy → (v : Vertex) → Bool → W.Path A v
witness red A false = W.stop
witness red A true = prefix
witness red B false = later
witness red B true = continuation
witness red C false = Actions.append prefix toC
witness red C true = toC
witness red D false = toD
witness red D true = Actions.append prefix toD
witness green A false = W.stop
witness green A true = prefix
witness green B false = continuation
witness green B true = later
witness green C false = Actions.append prefix toC
witness green C true = toC
witness green D false = Actions.append prefix toD
witness green D true = toD
witness-value : (p : Policy) (v : Vertex) (b : Bool)
  → Model.I.E.run p (witness p v b) false ≡ b
witness-value red A false = refl
witness-value red A true = refl
witness-value red B false = refl
witness-value red B true = refl
witness-value red C false = refl
witness-value red C true = refl
witness-value red D false = refl
witness-value red D true = refl
witness-value green A false = refl
witness-value green A true = refl
witness-value green B false = refl
witness-value green B true = refl
witness-value green C false = refl
witness-value green C true = refl
witness-value green D false = refl
witness-value green D true = refl
reachable : (p : Policy) (v : Vertex) (b : Bool)
  → Σ (W.Path A v) (λ w → Model.read p w ≡ b)
reachable p v b = witness p v b ,
  (Model.native-agrees p (witness p v b) ∙ witness-value p v b)

ContextuallyEqual : Type
ContextuallyEqual = (v : Vertex) (w : W.Path A v) → R.read w ≡ G.read w
not-contextually-equal : ContextuallyEqual → ⊥
not-contextually-equal agrees = future-distinct (agrees B later)
