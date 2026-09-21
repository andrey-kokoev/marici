{-# OPTIONS --safe --cubical --guardedness #-}
module TypedCutReconstruction where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Base
import EndpointDecoratedHistory as H

module Reconstruction {ℓ : Level} (V : Type ℓ) (E : V → V → Type ℓ) where
  open H.Typed V E

  -- A regrouping retains its cut vertices and the complete records of its leaves.
  data Tree : {x y : V} → Route x y → Type ℓ where
    leaf : {x y : V} {p : Route x y} → Tree p
    fork : {x y : V} {p : Route x y} (c : Cut p) →
      Tree (prefix c) → Tree (suffix c) → Tree p

  Records : {x y : V} {p : Route x y} → Tree p → Type ℓ
  Records {p = p} leaf = Marks p
  Records (fork c l r) = Records l × Records r

  restrict : {x y : V} {p : Route x y} (t : Tree p) → Marks p → Records t
  restrict leaf m = m
  restrict (fork c l r) m = restrict l (fst (split c m)) , restrict r (snd (split c m))

  assemble : {x y : V} {p : Route x y} (t : Tree p) → Records t → Marks p
  assemble leaf m = m
  assemble (fork c l r) mn = merge c (assemble l (fst mn) , assemble r (snd mn))

  assemble-restrict : {x y : V} {p : Route x y} (t : Tree p) (m : Marks p) →
    assemble t (restrict t m) ≡ m
  assemble-restrict leaf m = refl
  assemble-restrict (fork c l r) m =
    cong (merge c) (λ i → assemble-restrict l (fst (split c m)) i ,
                         assemble-restrict r (snd (split c m)) i)
    ∙ merge-split c m

  restrict-assemble : {x y : V} {p : Route x y} (t : Tree p) (m : Records t) →
    restrict t (assemble t m) ≡ m
  restrict-assemble leaf m = refl
  restrict-assemble (fork c l r) (ml , mr) =
    cong (λ z → restrict l (fst z) , restrict r (snd z))
      (split-merge c (assemble l ml , assemble r mr))
    ∙ (λ i → restrict-assemble l ml i , restrict-assemble r mr i)

  reconstruction-iso : {x y : V} {p : Route x y} (t : Tree p) →
    Iso (Marks p) (Records t)
  Iso.fun (reconstruction-iso t) = restrict t
  Iso.inv (reconstruction-iso t) = assemble t
  Iso.rightInv (reconstruction-iso t) = restrict-assemble t
  Iso.leftInv (reconstruction-iso t) = assemble-restrict t

  regroup : {x y : V} {p : Route x y} (s t : Tree p) → Records s → Records t
  regroup s t m = restrict t (assemble s m)

  regroup-id : {x y : V} {p : Route x y} (t : Tree p) (m : Records t) →
    regroup t t m ≡ m
  regroup-id = restrict-assemble

  regroup-compose : {x y : V} {p : Route x y} (s t u : Tree p) (m : Records s) →
    regroup t u (regroup s t m) ≡ regroup s u m
  regroup-compose s t u m = cong (restrict u) (assemble-restrict t (assemble s m))

  -- No faithfulness of a further scalar/analytic observation is assumed here.
  -- Such an observation needs its own injectivity or joint-conservativity proof.
