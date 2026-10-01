{-# OPTIONS --safe --cubical --guardedness #-}
module SeedAttachedObserver where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Unit.Base using (Unit; tt)
import ObserverCoherenceCube as Observer
import WholePackageSigmaPi as Whole

-- Actual six-arrow seed, with outgoing fibers indexed by source.
data Vertex : Type where
  A B C D : Vertex

data Out : Vertex → Type where
  AB AD : Out A
  BC BA : Out B
  CA : Out C
  DB : Out D

target : {v : Vertex} → Out v → Vertex
target AB = B
target AD = D
target BC = C
target BA = A
target CA = A
target DB = B

-- Minimal adapter: no extra nested choices are introduced.
module O = Observer.FromSource Vertex Out
  (λ _ _ → Unit) (λ _ _ _ → Unit) (λ _ _ _ _ → Unit)

-- Two explicit source sections, not assigned particle identities.
cycle : O.S.X
cycle A = AD , (λ _ → tt , tt)
cycle B = BC , (λ _ → tt , tt)
cycle C = CA , (λ _ → tt , tt)
cycle D = DB , (λ _ → tt , tt)

other : O.S.X
other A = AB , (λ _ → tt , tt)
other B = BC , (λ _ → tt , tt)
other C = CA , (λ _ → tt , tt)
other D = DB , (λ _ → tt , tt)

attach : (q : O.S.X) → O.AttachedObserver
attach q = Iso.inv O.expansionIso (q , q) , O.diagonal-attaches q

next : Whole.Universe.Complete ℓ-zero
next = O.nextAttachedQ (attach cycle , attach other)

recover : O.AttachedSquare.observers (Whole.Universe.value next)
  ≡ (attach cycle , attach other)
recover = O.recover-attachments (attach cycle , attach other)

-- Attachment within one observer identifies its two source sections.
-- It is not an extra coupling between the two observers passed to nextAttachedQ.
attachment-implies-source-equality : (u v : O.CanonicalTrace)
  → O.Attach (u , v) → fst u ≡ fst v
attachment-implies-source-equality u v p =
  sym (Iso.leftInv O.S.routeA (fst u))
  ∙ cong (Iso.inv O.S.routeA) (p ∙ sym (O.S.route-comparison (fst v)))
  ∙ Iso.leftInv O.S.routeA (fst v)
