{-# OPTIONS --safe --cubical --guardedness #-}
module NativeRetainedProfiles where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Histories
import RetainedObservationFibers as Fibers

module Native (ℓ : Level) where
  module G = Tables.Core ℓ
  module N = Rules.Native ℓ
  module Family {A V : Type ℓ} (source : G.Node A) (r : A → V) where
    module R = Fibers.Retain r
    -- No source point is needed even to represent an entirely empty source.
    fiber-node : (v : V) → G.Node (R.Fiber v)
    fiber-node v = G.E-node A (λ a → G.paths-node (G.atom-node V) (r a) v)
    family-node : G.Node R.Total
    family-node = G.E-node V fiber-node
    family-header : G.header family-node ≡ G.E-header V R.Fiber
    family-header = refl
    reader-node : G.Node R.Total
    reader-node = G.retain-node (G.maps-node source (G.atom-node V)) r family-node
  module Profile {A V : Type ℓ} (source : G.Node A) (a0 : A) (r : A → V) where
    open Family source r public
    node : G.Node R.Total
    node = G.retain-node source a0 reader-node
    source-package package : G.Package
    source-package = N.pack source a0
    package = N.pack node (r a0 , a0 , refl)
    source-header : G.header node ≡ G.retain-header A a0 R.Total
    source-header = refl
    representation : A ≃ R.Total
    representation = isoToEquiv R.reassemble
    recover : R.Total → A
    recover = invEq representation
    source-roundtrip : (a : A) → recover (equivFun representation a) ≡ a
    source-roundtrip = retEq representation
    table-roundtrip : (t : R.Total) → equivFun representation (recover t) ≡ t
    table-roundtrip = secEq representation
    comparison : G.Package
    comparison = N.comparison-package source-package package representation refl
    -- This is a concrete comparison certificate, not a Resolve admission proof.

  module Two {A V W : Type ℓ} (source : G.Node A) (a0 : A)
    (r : A → V) (s : A → W) where
    module First = Profile source a0 r
    module Second = Profile source a0 s
    module Joint = Profile source a0 (λ a → r a , s a)
    first-to-second : First.R.Total ≃ Second.R.Total
    first-to-second = compEquiv (invEquiv First.representation) Second.representation
    joint-to-first : Joint.R.Total ≃ First.R.Total
    joint-to-first = compEquiv (invEquiv Joint.representation) First.representation
    joint-to-second : Joint.R.Total ≃ Second.R.Total
    joint-to-second = compEquiv (invEquiv Joint.representation) Second.representation
    source-unchanged : (t : First.R.Total)
      → Second.recover (equivFun first-to-second t) ≡ First.recover t
    source-unchanged t = refl
    first-reading : (t : Joint.R.Total) → fst (equivFun joint-to-first t) ≡ fst (fst t)
    first-reading ((v , w) , a , p) = cong fst p
    second-reading : (t : Joint.R.Total) → fst (equivFun joint-to-second t) ≡ snd (fst t)
    second-reading ((v , w) , a , p) = cong snd p
    triangle : (t : Joint.R.Total)
      → equivFun first-to-second (equivFun joint-to-first t) ≡ equivFun joint-to-second t
    triangle t = refl
    profiles-comparison : G.Package
    profiles-comparison = N.comparison-package First.package Second.package first-to-second refl
    joint-first-comparison : G.Package
    joint-first-comparison = N.comparison-package Joint.package First.package joint-to-first refl
    joint-second-comparison : G.Package
    joint-second-comparison = N.comparison-package Joint.package Second.package joint-to-second refl
    -- Both observations refer to ONE source value, not independently chosen ones.
    compatible : (v : V) (w : W) → Type ℓ
    compatible v w = Σ A (λ a → (r a ≡ v) × (s a ≡ w))
    joint-witnesses : (v : V) (w : W) → Iso (Joint.R.Fiber (v , w)) (compatible v w)
    Iso.fun (joint-witnesses v w) (a , p) = a , cong fst p , cong snd p
    Iso.inv (joint-witnesses v w) (a , p , q) = a , (λ i → p i , q i)
    Iso.rightInv (joint-witnesses v w) _ = refl
    Iso.leftInv (joint-witnesses v w) _ = refl

  module Coarsen {A V W : Type ℓ} (source : G.Node A) (a0 : A)
    (r : A → V) (q : V → W) where
    module Original = Profile source a0 r
    -- Coarse fiber payload is the ENTIRE old indexed fiber value.
    module Grouped = Profile Original.node (r a0 , a0 , refl) (λ t → q (fst t))
    source-to-groups : A ≃ Grouped.R.Total
    source-to-groups = compEquiv Original.representation Grouped.representation
    original-index : Grouped.R.Total → V
    original-index t = fst (fst (snd t))
    recovered : (a : A) → invEq source-to-groups (equivFun source-to-groups a) ≡ a
    recovered = retEq source-to-groups
    all-data-recovered : (t : Grouped.R.Total)
      → equivFun source-to-groups (invEq source-to-groups t) ≡ t
    all-data-recovered = secEq source-to-groups

-- Instantiate the same native diagram on COMPLETE native resolution histories.
-- The universe is raised because histories include packages and derivations.
-- No new Admit witness is generated for the reorganized representation.
module NativeHistories
  (Admit : Tables.Core.Package ℓ-zero → Type₁)
  (h0 : Histories.Full.Closed ℓ-zero Admit)
  (V W : Type₁)
  (r : Histories.Full.Closed ℓ-zero Admit → V)
  (s : Histories.Full.Closed ℓ-zero Admit → W) where
  module H = Histories.Full ℓ-zero Admit
  module N = Native (ℓ-suc ℓ-zero)
  module Profiles = N.Two (N.G.atom-node H.Closed) h0 r s
  recovered-declaration : (h : H.Closed)
    → H.declaration (Profiles.First.recover (equivFun Profiles.First.representation h)) ≡ H.declaration h
  recovered-declaration h = refl
  recovered-premise : (h : H.Closed) (i : H.Ports h)
    → H.premise (Profiles.First.recover (equivFun Profiles.First.representation h)) i ≡ H.premise h i
  recovered-premise h i = refl

module Test where
  module N = Native ℓ-zero
  module G = N.G
  module Same = N.Two (G.atom-node Bool) false (λ b → b) (λ b → b)
  left-exists : Same.First.R.Fiber false
  left-exists = false , refl
  right-exists : Same.Second.R.Fiber true
  right-exists = true , refl
  no-independent-pairing : Same.Joint.R.Fiber (false , true) → ⊥
  no-independent-pairing (a , p) = false≢true (sym (cong fst p) ∙ cong snd p)
  module Constant = N.Profile (G.atom-node Bool) false (λ _ → false)
  empty-fiber-has-node : G.Node (Constant.R.Fiber true)
  empty-fiber-has-node = Constant.fiber-node true
  no-empty-fiber-value : Constant.R.Fiber true → ⊥
  no-empty-fiber-value (a , p) = false≢true p
  no-all-fibers-pointed : ((v : Bool) → Constant.R.Fiber v) → ⊥
  no-all-fibers-pointed choose = no-empty-fiber-value (choose true)
  module EmptySource = N.Family {V = Bool} (G.atom-node ⊥) (λ ())
  empty-source-has-graph : G.Node EmptySource.R.Total
  empty-source-has-graph = EmptySource.reader-node
  no-marked-empty-source : EmptySource.R.Total → ⊥
  no-marked-empty-source t = fst (snd t)
  module Coarse = N.Coarsen (G.atom-node Bool) false (λ b → b) (λ _ → false)
  original-true-retained : Coarse.original-index (equivFun Coarse.source-to-groups true) ≡ true
  original-true-retained = refl
