{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyNativeDerivedComparison where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution
module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero

module Presentations (Root Frame View : Type) (Valid : Root → Type)
  (view : Frame → Root → View) where
  Parent : Type
  Parent = Σ Root Valid
  base : (a : Root) → Valid a → G.Package
  base a v = N.pack (G.atom-node Parent) (a , v)
  Admit : G.Package → Type (ℓ-suc ℓ-zero)
  Admit q = Σ Root (λ a → Σ (Valid a) (λ v → q ≡ base a v))
  module R = Resolution.Full ℓ-zero Admit
  base-proof : (a : Root) (v : Valid a) → R.Resolve (base a v)
  base-proof a v = R.seed (a , (v , refl))
  display : (a : Root) → Valid a → Frame → G.Package
  display a v f = N.E-package (singl (view f a)) (λ _ → base a v) (view f a , refl)
  display-proof : (a : Root) (v : Valid a) (f : Frame) → R.Resolve (display a v f)
  display-proof a v f = R.apply (N.E-kind , singl (view f a) , (λ _ → base a v) , (view f a , refl))
    (λ { (lift _) → base-proof a v })
  change : (a : Root) (v : Valid a) (f g : Frame)
    → Iso (N.Ty (display a v f)) (N.Ty (display a v g))
  Iso.fun (change a v f g) (s , parent) = (view g a , refl) , parent
  Iso.inv (change a v f g) (s , parent) = (view f a , refl) , parent
  Iso.rightInv (change a v f g) (s , parent) i = snd (isContrSingl (view g a)) s i , parent
  Iso.leftInv (change a v f g) (s , parent) i = snd (isContrSingl (view f a)) s i , parent
  equivalence : (a : Root) (v : Valid a) (f g : Frame)
    → N.Ty (display a v f) ≃ N.Ty (display a v g)
  equivalence a v f g = isoToEquiv (change a v f g)
  aligned : (a : Root) (v : Valid a) (f g : Frame)
    → equivFun (equivalence a v f g) (N.value (display a v f)) ≡ N.value (display a v g)
  aligned a v f g = refl
  comparison : (a : Root) → Valid a → Frame → Frame → G.Package
  comparison a v f g = N.comparison-package (display a v f) (display a v g) (equivalence a v f g) refl
  comparison-proof : (a : Root) (v : Valid a) (f g : Frame) → R.Resolve (comparison a v f g)
  comparison-proof a v f g = R.apply
    (N.compare-kind , display a v f , display a v g , equivalence a v f g , refl)
    (λ { (lift true) → display-proof a v f ; (lift false) → display-proof a v g })
  retains-parent : (a : Root) (v : Valid a) (f g : Frame) (x : N.Ty (display a v f))
    → snd (equivFun (equivalence a v f g) x) ≡ snd x
  retains-parent a v f g x = refl
  action-composes : (a : Root) (v : Valid a) (f g h : Frame) (x : N.Ty (display a v f))
    → equivFun (equivalence a v g h) (equivFun (equivalence a v f g) x)
      ≡ equivFun (equivalence a v f h) x
  action-composes a v f g h x = refl
  composed : (a : Root) → Valid a → Frame → Frame → Frame → G.Package
  composed a v f g h = N.compose-comparisons (display a v f) (display a v g) (display a v h)
    (equivalence a v f g) (equivalence a v g h) refl refl
  composed-proof : (a : Root) (v : Valid a) (f g h : Frame) → R.Resolve (composed a v f g h)
  composed-proof a v f g h = R.apply
    (N.compose-kind , display a v f , display a v g , display a v h ,
     equivalence a v f g , equivalence a v g h , refl , refl)
    (λ { (lift true) → comparison-proof a v f g ; (lift false) → comparison-proof a v g h })
  retains-first-route : (a : Root) (v : Valid a) (f g h : Frame)
    → R.premise (composed a v f g h , composed-proof a v f g h) (lift true)
      ≡ (comparison a v f g , comparison-proof a v f g)
  retains-first-route a v f g h = refl
  retains-second-route : (a : Root) (v : Valid a) (f g h : Frame)
    → R.premise (composed a v f g h , composed-proof a v f g h) (lift false)
      ≡ (comparison a v g h , comparison-proof a v g h)
  retains-second-route a v f g h = refl
