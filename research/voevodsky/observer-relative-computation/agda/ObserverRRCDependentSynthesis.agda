{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverRRCDependentSynthesis where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence using (uaβ)
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Sigma.Properties using (ΣPathP)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (notEquiv; true≢false)
open import Cubical.Data.Empty.Base using (⊥) renaming (rec to absurd)
open import Cubical.Relation.Nullary.Base using (Dec; yes; no)
import WholePackageSigmaPi as W
import WholePackageResolution as RRC
import IndexIdentityCoherence as Indexed
import IndexIdentityCoherenceRegression as Cover
import ObserverRRCWitnessSynthesis as Finite

module U = W.Universe ℓ-zero
module R = RRC.Generators ℓ-zero
module Ix = Indexed.Indexed ℓ-zero

-- Two canonical path codes in a genuinely dependent, nontrivial family.
index-path : Finite.Mode → Cover.base-index ≡ Cover.base-index
index-path Finite.identity = refl
index-path Finite.swap = Cover.index-loop

normalizes : (m : Finite.Mode) (x : Bool)
  → subst (Ix.Fibre Cover.F) (index-path m) x ≡ equivFun (Finite.equivalence m) x
normalizes Finite.identity x = substRefl {B = Ix.Fibre Cover.F} {x = Cover.base-index} x
normalizes Finite.swap x = uaβ notEquiv x

Boundary : Finite.Mode → Bool → Bool → Type
Boundary m x y = subst (Ix.Fibre Cover.F) (index-path m) x ≡ y

point : Bool → Ix.Total Cover.F
point x = Cover.base-index , x

total-witness : (m : Finite.Mode) (x y : Bool) → Boundary m x y → point x ≡ point y
total-witness m x y p = ΣPathP (index-path m , toPathP p)

index-retained : (m : Finite.Mode) (x y : Bool) (p : Boundary m x y)
  → cong fst (total-witness m x y p) ≡ index-path m
index-retained m x y p = refl

packet : Bool → U.Complete
packet x = U.pack (U.atom (Ix.Total Cover.F)) (point x)

Source : U.Complete → Type₁
Source q = Lift {j = ℓ-zero} (Σ Bool (λ b → packet b ≡ q))

source : (x : Bool) → R.Resolve Source (packet x)
source x = R.seed (lift (x , refl))

record Solution (m : Finite.Mode) (x y : Bool) : Type₁ where
  constructor solved
  field
    fibre-witness : Boundary m x y
    history : R.Resolve Source (U.comparison-package (packet x) (packet y)
      (idEquiv (Ix.Total Cover.F)) (total-witness m x y fibre-witness))
open Solution public

construct : (m : Finite.Mode) (x y : Bool) → Boundary m x y → Solution m x y
construct m x y p = solved p (R.apply rule premises)
  where
  rule = R.compare-rule (packet x) (packet y) (idEquiv (Ix.Total Cover.F)) (total-witness m x y p)
  premises : (i : R.Arity rule) → R.Resolve Source (R.input rule i)
  premises (lift true) = source x
  premises (lift false) = source y

output-packet : (m : Finite.Mode) (x y : Bool) → Solution m x y → U.Complete
output-packet m x y s = U.comparison-package (packet x) (packet y)
  (idEquiv (Ix.Total Cover.F)) (total-witness m x y (fibre-witness s))

recover-index : (m : Finite.Mode) (x y : Bool) (s : Solution m x y)
  → Cover.base-index ≡ Cover.base-index
recover-index m x y s = cong fst (snd (snd (U.value (output-packet m x y s))))

recovery-exact : (m : Finite.Mode) (x y : Bool) (s : Solution m x y)
  → recover-index m x y s ≡ index-path m
recovery-exact m x y s = refl

-- Computes the fibre action; produces its actual transport witness and
-- an RRC history retaining the resulting total-space comparison path.
synthesize : (m : Finite.Mode) (x y : Bool) → Dec (Solution m x y)
synthesize m x y with Finite.decideBool (equivFun (Finite.equivalence m) x) y
... | yes p = yes (construct m x y (normalizes m x ∙ p))
... | no impossible = no (λ s → impossible (sym (normalizes m x) ∙ fibre-witness s))

complete : (m : Finite.Mode) (x y : Bool) → Solution m x y
  → Σ (Solution m x y) (λ result → synthesize m x y ≡ yes result)
complete m x y candidate with synthesize m x y
... | yes result = result , refl
... | no impossible = absurd (impossible candidate)

loop-solution : Solution Finite.swap true false
loop-solution = construct Finite.swap true false (normalizes Finite.swap true)

reflexive-request-impossible : Solution Finite.identity true false → ⊥
reflexive-request-impossible s = true≢false
  (sym (normalizes Finite.identity true) ∙ fibre-witness s)

-- The successful loop comparison cannot be relabelled as reflexive.
loop-index-not-erased : cong fst (total-witness Finite.swap true false
  (fibre-witness loop-solution)) ≡ refl → ⊥
loop-index-not-erased = Cover.loop-is-not-reflexive
