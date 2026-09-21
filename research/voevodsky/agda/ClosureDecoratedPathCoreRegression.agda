{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureDecoratedPathCoreRegression where

open import Cubical.Foundations.Prelude using (Type; _≡_; refl)
open import Agda.Builtin.Nat using (suc; zero)
open import Agda.Builtin.Sigma using (_,_)
open import ClosureDecoratedPathCore

data Vertex : Type where
  n2 n4 n6 n12 : Vertex

data Edge : Vertex → Vertex → Type where
  add2-at2 : Edge n2 n4
  add3-at4 : Edge n4 n12
  add3-at2 : Edge n2 n6
  add2-at6 : Edge n6 n12

open Source Vertex Edge

via4 via6 : Path n2 n12
via4 = add2-at2 ▷ add3-at4 ▷ identity
via6 = add3-at2 ▷ add2-at6 ▷ identity

forgotten4 : Decoration via4
forgotten4 = forgotten , forgotten , empty
forgotten6 : Decoration via6
forgotten6 = forgotten , forgotten , empty

middle4 : Cut via4
middle4 = next start
middle6 : Cut via6
middle6 = next start

keeps-four : vertex via4 middle4 ≡ n4
keeps-four = refl
keeps-six : vertex via6 middle6 ≡ n6
keeps-six = refl

split-four : join via4 middle4 (split via4 middle4 forgotten4) ≡ forgotten4
split-four = join-split via4 middle4 forgotten4
split-six : join via6 middle6 (split via6 middle6 forgotten6) ≡ forgotten6
split-six = join-split via6 middle6 forgotten6

lift-four : mass via4 (lift via4) ≡ suc zero
lift-four = split-lift-coefficient via4
lift-six : mass via6 (lift via6) ≡ suc zero
lift-six = split-lift-coefficient via6

empty-lift : mass (identity {n4}) (lift (identity {n4})) ≡ suc zero
empty-lift = split-lift-coefficient (identity {n4})

forgotten-is-not-all-retained : weight via4 forgotten4 ≡ zero
forgotten-is-not-all-retained = refl
