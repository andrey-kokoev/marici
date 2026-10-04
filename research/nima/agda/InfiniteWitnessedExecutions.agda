{-# OPTIONS --safe --cubical --guardedness #-}
module InfiniteWitnessedExecutions where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (Iso; iso)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Unit.Base using (tt*)
import WitnessedHistories as Finite
import MetaWitnessGenerator as Meta
import NestedWitnessSpecialization as Nested
import WitnessSelectionGenerator as Selection
import ReSpecializeWitnessSelection as First

record Trace {ℓ : Level} (S : Type ℓ) (R : S → S → Type ℓ) (x : S) : Type ℓ where
  coinductive
  field
    next : S
    witness : R x next
    rest : Trace S R next
open Trace

execute : {ℓ : Level} {S : Type ℓ} {R : S → S → Type ℓ}
  → ((x : S) → Σ[ y ∈ S ] R x y) → (x : S) → Trace S R x
next (execute g x) = fst (g x)
witness (execute g x) = snd (g x)
rest (execute g x) = execute g (fst (g x))

prefix : {ℓ : Level} {S : Type ℓ} {R : S → S → Type ℓ}
  → (n : ℕ) {x : S} → Trace S R x → Finite.History S R n x
prefix zero t = tt*
prefix (suc n) t = next t , witness t , prefix n (rest t)

prefix-execute : {ℓ : Level} {S : Type ℓ} {R : S → S → Type ℓ}
  (g : (x : S) → Σ[ y ∈ S ] R x y) (n : ℕ) (x : S)
  → prefix n (execute g x) ≡ Finite.run g n x
prefix-execute g zero x = refl
prefix-execute g (suc n) x =
  cong (λ tail → fst (g x) , snd (g x) , tail) (prefix-execute g n (fst (g x)))

module Specialization {ℓ : Level} (S : Type ℓ) (R : S → S → Type ℓ)
  (first : Meta.Specialize.Compatible S R) where
  module N = Nested.Nested S R first
  module Second (d : N.M2.Domain)
    (a : (v : N.C1.State) → fst (N.C1.generator v) ≡ N.M2.Domain.compute d v)
    (c : (v : N.C1.State) → N.M2.Domain.Allowed d v
      → N.M2.Domain.Allowed d (fst (N.C1.generator v))) where
    module F = Finite.Specialization.Second S R first d a c
    module T = F.T

    flatten : {x : T.C2.State} → Trace T.C2.State T.C2.Relation x
      → Trace T.Flat T.FlatRelation (T.flatten x)
    next (flatten t) = T.flatten (next t)
    witness (flatten t) = witness t
    rest (flatten t) = flatten (rest t)

    unflatten : {x : T.Flat} → Trace T.Flat T.FlatRelation x
      → Trace T.C2.State T.C2.Relation (T.unflatten x)
    next (unflatten t) = T.unflatten (next t)
    witness (unflatten t) = witness t
    rest (unflatten t) = unflatten (rest t)

    flatten-unflatten : {x : T.Flat} (t : Trace T.Flat T.FlatRelation x)
      → flatten (unflatten t) ≡ t
    next (flatten-unflatten t i) = next t
    witness (flatten-unflatten t i) = witness t
    rest (flatten-unflatten t i) = flatten-unflatten (rest t) i

    unflatten-flatten : {x : T.C2.State} (t : Trace T.C2.State T.C2.Relation x)
      → unflatten (flatten t) ≡ t
    next (unflatten-flatten t i) = next t
    witness (unflatten-flatten t i) = witness t
    rest (unflatten-flatten t i) = unflatten-flatten (rest t) i

    trace-iso : (x : T.C2.State)
      → Iso (Trace T.C2.State T.C2.Relation x) (Trace T.Flat T.FlatRelation (T.flatten x))
    trace-iso x = iso flatten unflatten flatten-unflatten unflatten-flatten

    execute-commutes : (x : T.C2.State)
      → flatten (execute T.C2.generator x) ≡ execute T.direct-generator (T.flatten x)
    next (execute-commutes x i) = T.flatten (fst (T.C2.generator x))
    witness (execute-commutes x i) = snd (T.C2.generator x)
    rest (execute-commutes x i) = execute-commutes (fst (T.C2.generator x)) i

    prefix-flatten : (n : ℕ) {x : T.C2.State} (t : Trace T.C2.State T.C2.Relation x)
      → prefix n (flatten t) ≡ F.flatten-history n x (prefix n t)
    prefix-flatten zero t = refl
    prefix-flatten (suc n) t = cong (λ tail → T.flatten (next t) , witness t , tail)
      (prefix-flatten n (rest t))

module SelectionFixture where
  module H = Specialization.Second Selection.State Selection.SelectionWitness
    First.selection-pair Nested.Example.second-domain (λ v → refl) (λ v p → p)
  infinite-agreement : H.flatten (execute H.T.C2.generator Nested.Example.request)
    ≡ execute H.T.direct-generator (H.T.flatten Nested.Example.request)
  infinite-agreement = H.execute-commutes Nested.Example.request
