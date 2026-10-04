{-# OPTIONS --safe --cubical --guardedness #-}
module FiniteStoneAdapter where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
import BooleanNandEquivalence as Boolean
open import FiniteStoneDomain
import IndexedConstructorTables as Tables
import NativeTableRules as Rules

module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero

-- Only existing atom, Sigma, Pi, maps, equivalences, retain, comparison and
-- path constructors occur here. The domain-specific theorems live next door.
bool-node : G.Node Bool
bool-node = G.atom-node Bool
algebra-node : G.Node A
algebra-node = G.E-node Bool (λ _ → bool-node)
atom-node : G.Node Atom
atom-node = G.E-node A (λ a → G.atom-node (IsAtom a))
subset-node : G.Node (Atom → Bool)
subset-node = G.P-node Atom (λ _ → bool-node)
laws : G.Package
laws = N.pack (G.atom-node (Boolean.BooleanStructure A)) boolean
source : A → G.Package
source a = N.remember laws (N.pack algebra-node a)
target : A → G.Package
target a = N.Pi-package Atom (λ p → N.pack bool-node (represent a p))
reconstruction-equivalence : G.Package
reconstruction-equivalence = N.pack (G.equivalences-node algebra-node subset-node) (isoToEquiv stone)
adapt : A → G.Package
adapt a = N.remember reconstruction-equivalence
  (N.comparison-package (source a) (target a) (isoToEquiv stone) refl)
selected-source : (a : A) → fst (N.value (adapt a)) ≡ a
selected-source a = refl
selected-subset : (a : A) → fst (snd (N.value (adapt a))) ≡ represent a
selected-subset a = refl

-- Use the actual original native composition rule, not a local replacement.
roundtrip-package : A → G.Package
roundtrip-package a = N.compose-comparisons (source a) (target a) (source a)
  (isoToEquiv stone) (invEquiv (isoToEquiv stone)) refl (retEq (isoToEquiv stone) a)
roundtrip-source : (a : A) → fst (N.value (roundtrip-package a)) ≡ a
roundtrip-source a = refl
roundtrip-target : (a : A) → fst (snd (N.value (roundtrip-package a))) ≡ a
roundtrip-target a = refl

-- A recovered witness can itself be retained as typed data; its next identity
-- witness is explicit. This is not a general certificate-discovery algorithm.
recovery-witness : A → G.Package
recovery-witness a = N.path-package (A , algebra-node) (reconstruct (represent a)) a (Iso.leftInv stone a)
witness-of-witness : A → G.Package
witness-of-witness a = N.higher-package (A , algebra-node) (reconstruct (represent a)) a
  (Iso.leftInv stone a) (Iso.leftInv stone a) refl

hom-node : G.Node Hom
hom-node = G.E-node (A → A) (λ h → G.atom-node (Preserves h))
point-map-node : G.Node (Bool → Bool)
point-map-node = G.P-node Bool (λ _ → bool-node)
hom-source : Hom → G.Package
hom-source h = N.remember (N.pack (G.maps-node algebra-node algebra-node) (fst h)) (N.pack hom-node h)
hom-target : Hom → G.Package
hom-target h = N.Pi-package Bool (λ p → N.pack bool-node (select h p))
adapt-arrow : Hom → G.Package
adapt-arrow h = N.comparison-package (hom-source h) (hom-target h) (isoToEquiv arrows-iso) refl
selected-arrow : (h : Hom) → fst (N.value (adapt-arrow h)) ≡ h
selected-arrow h = refl
selected-point-map : (h : Hom) → fst (snd (N.value (adapt-arrow h))) ≡ select h
selected-point-map h = refl

naturality-package : Hom → G.Package
naturality-package h = N.Pi-package A (λ a → N.Pi-package Atom (λ p →
  N.path-package (Bool , bool-node) (represent (fst h a) p) (represent a (atom-map h p)) (atom-naturality h a p)))
variance-package : (Bool → Bool) → (Bool → Bool) → G.Package
variance-package f g = N.Pi-package A (λ a → N.path-package (A , algebra-node)
  (pull (λ i → f (g i)) a) (pull g (pull f a)) (pull-compose f g a))

arrow-composition-package : Hom → Hom → G.Package
arrow-composition-package k h = N.path-package ((Bool → Bool) , point-map-node)
  (select (compose-hom k h)) (λ i → select h (select k i)) (select-compose k h)
arrow-identity-package : G.Package
arrow-identity-package = N.path-package ((Bool → Bool) , point-map-node)
  (select identity-hom) (λ i → i) select-identity

-- The atom swap is visible after adaptation. Its point map is not erased.
adapted-swap : fst (snd (N.value (adapt-arrow (arrow not)))) ≡ not
adapted-swap = select-arrow not
