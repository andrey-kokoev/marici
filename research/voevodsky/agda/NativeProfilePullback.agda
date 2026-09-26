{-# OPTIONS --safe --cubical --guardedness #-}
module NativeProfilePullback where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
import NativeRetainedProfiles as Profiles

module Gluing (ℓ : Level) {A V W : Type ℓ}
  (source : Profiles.Native.G.Node ℓ A) (a0 : A)
  (r : A → V) (s : A → W) where
  module Native = Profiles.Native ℓ
  module G = Native.G
  module N = Native.N
  module D = Native.Two source a0 r s
  X = D.First.R.Total
  Y = D.Second.R.Total
  left-source : X → A
  left-source = D.First.recover
  right-source : Y → A
  right-source = D.Second.recover
  Pullback : Type ℓ
  Pullback = Σ X (λ x → Σ Y (λ y → right-source y ≡ left-source x))

  -- The right recovery map is an equivalence, so this fiber is contractible.
  -- Its contraction retains paths; it does not assert that A is a set.
  compatible-fiber : (x : X) → isContr (Σ Y (λ y → right-source y ≡ left-source x))
  compatible-fiber x = equiv-proof (snd (invEquiv D.Second.representation)) (left-source x)
  preferred : (x : X) → Σ Y (λ y → right-source y ≡ left-source x)
  preferred x = equivFun D.Second.representation (left-source x) , refl
  contraction : (x : X) (yp : Σ Y (λ y → right-source y ≡ left-source x))
    → preferred x ≡ yp
  contraction x yp = sym (snd (compatible-fiber x) (preferred x)) ∙ snd (compatible-fiber x) yp
  projection-iso : Iso Pullback X
  Iso.fun projection-iso = fst
  Iso.inv projection-iso x = x , preferred x
  Iso.rightInv projection-iso x = refl
  Iso.leftInv projection-iso (x , yp) i = x , contraction x yp i
  joint-equivalence : D.Joint.R.Total ≃ Pullback
  joint-equivalence = compEquiv D.joint-to-first (invEquiv (isoToEquiv projection-iso))
  recover-source : Pullback → A
  recover-source t = left-source (fst t)
  source-preserved : (j : D.Joint.R.Total)
    → recover-source (equivFun joint-equivalence j) ≡ D.Joint.recover j
  source-preserved j = refl
  joint-recovered : (j : D.Joint.R.Total)
    → invEq joint-equivalence (equivFun joint-equivalence j) ≡ j
  joint-recovered = retEq joint-equivalence
  gluing-data-recovered : (t : Pullback)
    → equivFun joint-equivalence (invEq joint-equivalence t) ≡ t
  gluing-data-recovered = secEq joint-equivalence

  -- Mapping-space universal property, including the supplied square witness.
  Cone : Type ℓ → Type ℓ
  Cone T = Σ (T → X) (λ f → Σ (T → Y)
    (λ g → (t : T) → right-source (g t) ≡ left-source (f t)))
  universal : (T : Type ℓ) → Iso (T → Pullback) (Cone T)
  Iso.fun (universal T) h = (λ t → fst (h t)) ,
    (λ t → fst (snd (h t))) , (λ t → snd (snd (h t)))
  Iso.inv (universal T) (f , g , p) t = f t , g t , p t
  Iso.rightInv (universal T) _ = refl
  Iso.leftInv (universal T) _ = refl
  joint-universal : (T : Type ℓ) → Iso (T → D.Joint.R.Total) (Cone T)
  Iso.fun (joint-universal T) h = Iso.fun (universal T) (λ t → equivFun joint-equivalence (h t))
  Iso.inv (joint-universal T) c t = invEq joint-equivalence (Iso.inv (universal T) c t)
  Iso.rightInv (joint-universal T) c = cong (Iso.fun (universal T))
    (funExt (λ t → secEq joint-equivalence (Iso.inv (universal T) c t)))
    ∙ Iso.rightInv (universal T) c
  Iso.leftInv (joint-universal T) h = funExt (λ t → retEq joint-equivalence (h t))
  factorization-contractible : (T : Type ℓ) (c : Cone T)
    → isContr (fiber (Iso.fun (joint-universal T)) c)
  factorization-contractible T c = equiv-proof (snd (isoToEquiv (joint-universal T))) c

  -- Concrete native graph: both original profile graphs and both recovery
  -- functions remain attached; the equality is an actual paths-node.
  raw-node : G.Node Pullback
  raw-node = G.E-node X λ x → G.E-node Y λ y →
    G.paths-node source (right-source y) (left-source x)
  node : G.Node Pullback
  node = G.retain-node (G.maps-node D.First.node source) left-source
    (G.retain-node (G.maps-node D.Second.node source) right-source raw-node)
  package : G.Package
  package = N.pack node ((r a0 , a0 , refl) , (s a0 , a0 , refl) , refl)
  native-comparison : G.Package
  native-comparison = N.comparison-package D.Joint.package package joint-equivalence refl
  -- No Resolve admission or chosen inhabitant of every branch is inferred.

module Control where
  module N = Profiles.Native ℓ-zero
  module P = Gluing ℓ-zero (N.G.atom-node Bool) false (λ _ → false) (λ _ → false)
  x : P.X
  x = false , false , refl
  y : P.Y
  y = false , true , refl
  readings-agree : fst x ≡ fst y
  readings-agree = refl
  no-source-glue : P.right-source y ≡ P.left-source x → ⊥
  no-source-glue p = false≢true (sym p)
