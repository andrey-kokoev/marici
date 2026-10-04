{-# OPTIONS --safe --cubical --guardedness #-}
module NativeYoneda where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
open import OrdinaryYoneda

module Adapter (C : Category ℓ-zero ℓ-zero) where
  module Y = Theorem C
  module G = Tables.Core ℓ-zero
  module N = Rules.Native ℓ-zero
  open Category C
  module At (F : Y.Presheaf ℓ-zero) (a : Ob) where
    module T = Y.At F a
    open Y.Presheaf F
    raw-node : G.Node T.Raw
    raw-node = G.P-node Ob (λ x → G.maps-node (G.atom-node (Hom x a)) (G.atom-node (Obj x)))
    natural-node : G.Node T.Natural
    natural-node = G.E-node T.Raw (λ α → G.atom-node (T.NaturalLaw α))
    source : T.Natural → G.Package
    source α = N.remember (N.pack raw-node (fst α)) (N.pack natural-node α)
    recover : T.Natural → G.Package
    recover α = N.comparison-package (source α)
      (N.pack (G.atom-node (Obj a)) (T.evaluate α)) (isoToEquiv T.yoneda) refl
    retained-natural-transformation : (α : T.Natural) → fst (N.value (recover α)) ≡ α
    retained-natural-transformation α = refl
    recovered-value : (α : T.Natural) → fst (snd (N.value (recover α))) ≡ T.evaluate α
    recovered-value α = refl
    reconstruction-witness : T.Natural → G.Package
    reconstruction-witness α = N.path-package (T.Natural , natural-node)
      (T.extend (T.evaluate α)) α (T.extend-evaluate α)
