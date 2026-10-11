{-# OPTIONS --safe --cubical --guardedness #-}
module ComposableWitnessSpecialization where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (Iso; iso)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Unit.Base using (Unit*; tt*)
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import TypedGeneratorLayers using (Layer1)
import MetaWitnessGenerator as Meta

-- A refinement extends states AND individual edge witnesses. The second
-- extension can depend on the first proof, not just its endpoints.
-- Source data live one universe higher so an original Domain is retained.
record Refinement {ℓ : Level} (L : Layer1 ℓ) : Type (ℓ-suc (ℓ-suc ℓ)) where
  open Layer1 L
  field
    Source : Type (ℓ-suc ℓ)
    source : Source
    Admit : State → Type ℓ
    advance : (s : State) → Admit s → Admit (next s)
  RefinedState : Type ℓ
  RefinedState = Σ[ s ∈ State ] Admit s
  field
    Extra : (x y : RefinedState) → Witness (fst x) (fst y) → Type ℓ
    certify : (x : RefinedState)
      → Extra x (next (fst x) , advance (fst x) (snd x)) (edge (fst x))

compile : {ℓ : Level} {L : Layer1 ℓ} → Refinement L → Layer1 ℓ
compile {L = L} F = record
  { State = F.RefinedState
  ; Witness = λ x y → Σ[ r ∈ Layer1.Witness L (fst x) (fst y) ] F.Extra x y r
  ; generate = λ { (s , p) →
      (Layer1.next L s , F.advance s p) , (Layer1.edge L s , F.certify (s , p)) } }
  where module F = Refinement F

-- Closed indexed operation: the result has exactly the same Refinement L
-- type as the first operand. No composite or composite certificate is input.
compose : {ℓ : Level} {L : Layer1 ℓ} (F : Refinement L)
  → Refinement (compile F) → Refinement L
compose F G = record
  { Source = F.Source × G.Source
  ; source = F.source , G.source
  ; Admit = λ s → Σ[ p ∈ F.Admit s ] G.Admit (s , p)
  ; advance = λ { s (p , q) → F.advance s p , G.advance (s , p) q }
  ; Extra = λ { (s , p , q) (t , p' , q') r →
      Σ[ e ∈ F.Extra (s , p) (t , p') r ] G.Extra ((s , p) , q) ((t , p') , q') (r , e) }
  ; certify = λ { (s , p , q) → F.certify (s , p) , G.certify ((s , p) , q) } }
  where
    module F = Refinement F
    module G = Refinement G

Step : {ℓ : Level} (L : Layer1 ℓ) → Layer1.State L → Type ℓ
Step L x = Σ[ y ∈ Layer1.State L ] Layer1.Witness L x y

-- Certificate compares all steps, not just the generated one; endpoint
-- compatibility prevents an arbitrary step-type bijection from sufficing.
record Realization {ℓ : Level} (L K : Layer1 ℓ) : Type ℓ where
  field
    states : Iso (Layer1.State L) (Layer1.State K)
    steps : (x : Layer1.State L) → Iso (Step L x) (Step K (Iso.fun states x))
    endpoints : (x : Layer1.State L) (z : Step L x)
      → fst (Iso.fun (steps x) z) ≡ Iso.fun states (fst z)
    generated : (x : Layer1.State L)
      → Iso.fun (steps x) (Layer1.generate L x)
        ≡ Layer1.generate K (Iso.fun states x)

module Composite {ℓ : Level} {L : Layer1 ℓ} (F : Refinement L)
  (G : Refinement (compile F)) where
  module N = Layer1 (compile G)
  module C = Layer1 (compile (compose F G))

  flatten : N.State → C.State
  flatten ((s , p) , q) = s , p , q
  unflatten : C.State → N.State
  unflatten (s , p , q) = (s , p) , q
  flatten-edge : {x y : N.State} → N.Witness x y → C.Witness (flatten x) (flatten y)
  flatten-edge ((r , e) , f) = r , e , f
  unflatten-edge : {x y : C.State} → C.Witness x y → N.Witness (unflatten x) (unflatten y)
  unflatten-edge (r , e , f) = (r , e) , f

  correct : Realization (compile G) (compile (compose F G))
  correct = record
    { states = iso flatten unflatten (λ _ → refl) (λ _ → refl)
    ; steps = λ x → iso
        (λ { (y , w) → flatten y , flatten-edge w })
        (λ { (y , w) → unflatten y , unflatten-edge w })
        (λ _ → refl) (λ _ → refl)
    ; endpoints = λ x z → refl
    ; generated = λ x → refl }

  recover-first-source : fst (Refinement.source (compose F G)) ≡ Refinement.source F
  recover-first-source = refl
  recover-second-source : snd (Refinement.source (compose F G)) ≡ Refinement.source G
  recover-second-source = refl

  -- A next refinement on the nested target is pulled back to the compiled
  -- composite. Both state and proof indices are changed; laws aren't projected.
  rebase : Refinement (compile G) → Refinement (compile (compose F G))
  rebase H = record
    { Source = H.Source ; source = H.source
    ; Admit = λ x → H.Admit (unflatten x)
    ; advance = λ x p → H.advance (unflatten x) p
    ; Extra = λ { (x , p) (y , q) w →
        H.Extra (unflatten x , p) (unflatten y , q) (unflatten-edge w) }
    ; certify = λ { (x , p) → H.certify (unflatten x , p) } }
    where module H = Refinement H

-- Existing domain specializations embed without changing their compiled WG.
module FromDomain {ℓ : Level} (S : Type ℓ) (R : S → S → Type ℓ)
  (input : Meta.Specialize.Compatible S R) where
  module M = Meta.Specialize S R
  module C = M.Compiled input
  open M.Compatible input
  open M.Domain domain
  base-WG : Layer1 ℓ
  base-WG = record { State = S ; Witness = R ; generate = base }
  refinement : Refinement base-WG
  refinement = record
    { Source = M.Compatible ; source = input
    ; Admit = Allowed ; advance = closed
    ; Extra = λ x y r → (fst y ≡ compute (fst x)) × C.LawEvidence (fst x)
    ; certify = λ x → agrees (fst x) , C.evidence (fst x) }
  compiler-agrees : compile refinement ≡ C.domain-WG
  compiler-agrees = refl

-- Empty refinement has a behavioral unit certificate. It retains a Unit
-- source; no equality of arbitrary source-record types is asserted.
identity : {ℓ : Level} (L : Layer1 ℓ) → Refinement L
identity L = record
  { Source = Unit* ; source = tt* ; Admit = λ _ → Unit*
  ; advance = λ _ _ → tt* ; Extra = λ _ _ _ → Unit* ; certify = λ _ → tt* }

identity-correct : {ℓ : Level} (L : Layer1 ℓ) → Realization (compile (identity L)) L
identity-correct L = record
  { states = iso fst (λ s → s , tt*) (λ _ → refl) (λ _ → refl)
  ; steps = λ x → iso (λ { ((t , _) , r , _) → t , r })
      (λ { (t , r) → (t , tt*) , r , tt* }) (λ _ → refl) (λ _ → refl)
  ; endpoints = λ x z → refl ; generated = λ x → refl }

-- Associator of the actual closed operation. The left grouping needs the
-- constructed rebase because H was originally typed over compile G.
module Associativity {ℓ : Level} {L : Layer1 ℓ} (F : Refinement L)
  (G : Refinement (compile F)) (H : Refinement (compile G)) where
  left right : Refinement L
  left = compose (compose F G) (Composite.rebase F G H)
  right = compose F (compose G H)
  module A = Layer1 (compile left)
  module B = Layer1 (compile right)
  forward : A.State → B.State
  forward (s , (p , q) , r) = s , p , q , r
  backward : B.State → A.State
  backward (s , p , q , r) = s , (p , q) , r
  edge-forward : {x y : A.State} → A.Witness x y → B.Witness (forward x) (forward y)
  edge-forward (r , (e , f) , h) = r , e , f , h
  edge-backward : {x y : B.State} → B.Witness x y → A.Witness (backward x) (backward y)
  edge-backward (r , e , f , h) = r , (e , f) , h
  associator : Realization (compile left) (compile right)
  associator = record
    { states = iso forward backward (λ _ → refl) (λ _ → refl)
    ; steps = λ x → iso (λ { (y , w) → forward y , edge-forward w })
        (λ { (y , w) → backward y , edge-backward w }) (λ _ → refl) (λ _ → refl)
    ; endpoints = λ x z → refl ; generated = λ x → refl }
  source-associator : Iso (Refinement.Source left) (Refinement.Source right)
  source-associator = iso (λ { ((a , b) , c) → a , b , c })
    (λ { (a , b , c) → (a , b) , c }) (λ _ → refl) (λ _ → refl)
  source-preserved : Iso.fun source-associator (Refinement.source left) ≡ Refinement.source right
  source-preserved = refl

module Units {ℓ : Level} {L : Layer1 ℓ} (F : Refinement L) where
  module F = Refinement F
  -- Pull back F along the empty refinement's projection.
  after-identity : Refinement (compile (identity L))
  after-identity = record
    { Source = F.Source ; source = F.source
    ; Admit = λ x → F.Admit (fst x)
    ; advance = λ x p → F.advance (fst x) p
    ; Extra = λ { (x , p) (y , q) w → F.Extra (fst x , p) (fst y , q) (fst w) }
    ; certify = λ { (x , p) → F.certify (fst x , p) } }
  left-unit : Realization (compile (compose (identity L) after-identity)) (compile F)
  left-unit = record
    { states = iso (λ { (s , _ , p) → s , p }) (λ { (s , p) → s , tt* , p })
        (λ _ → refl) (λ _ → refl)
    ; steps = λ x → iso (λ { ((s , _ , p) , r , _ , e) → (s , p) , r , e })
        (λ { ((s , p) , r , e) → (s , tt* , p) , r , tt* , e })
        (λ _ → refl) (λ _ → refl)
    ; endpoints = λ x z → refl ; generated = λ x → refl }
  right-unit : Realization (compile (compose F (identity (compile F)))) (compile F)
  right-unit = record
    { states = iso (λ { (s , p , _) → s , p }) (λ { (s , p) → s , p , tt* })
        (λ _ → refl) (λ _ → refl)
    ; steps = λ x → iso (λ { ((s , p , _) , r , e , _) → (s , p) , r , e })
        (λ { ((s , p) , r , e) → (s , p , tt*) , r , e , tt* })
        (λ _ → refl) (λ _ → refl)
    ; endpoints = λ x z → refl ; generated = λ x → refl }

-- Composition itself is a WG over requests and certified answers.
module Composer (ℓ : Level) where
  record Request : Type (ℓ-suc (ℓ-suc ℓ)) where
    field
      base : Layer1 ℓ
      first : Refinement base
      second : Refinement (compile first)
  Answer : Request → Type (ℓ-suc (ℓ-suc ℓ))
  Answer q = Σ[ C ∈ Refinement (Request.base q) ]
    Realization (compile (Request.second q)) (compile C)
  solve : (q : Request) → Answer q
  solve q = compose (Request.first q) (Request.second q) ,
    Composite.correct (Request.first q) (Request.second q)

  State : Type (ℓ-suc (ℓ-suc ℓ))
  State = Request ⊎ (Σ[ q ∈ Request ] Answer q)
  data Witness : State → State → Type (ℓ-suc (ℓ-suc ℓ)) where
    composed : (q : Request) → Witness (inl q) (inr (q , solve q))
    retained : (q : Request) (a : Answer q) → Witness (inr (q , a)) (inr (q , a))
  generate : (x : State) → Σ[ y ∈ State ] Witness x y
  generate (inl q) = inr (q , solve q) , composed q
  generate (inr (q , a)) = inr (q , a) , retained q a
  WG : Layer1 (ℓ-suc (ℓ-suc ℓ))
  WG = record { State = State ; Witness = Witness ; generate = generate }

module ProofDependentFixture where
  base : Layer1 ℓ-zero
  base = record { State = Bool ; Witness = λ s t → t ≡ not s ; generate = λ s → not s , refl }
  first : Refinement base
  first = record
    { Source = Lift {j = ℓ-suc ℓ-zero} Bool ; source = lift true
    ; Admit = λ _ → Bool ; advance = λ s p → not p
    ; Extra = λ x y r → Bool ; certify = snd }
  second : Refinement (compile first)
  second = record
    { Source = Lift {j = ℓ-suc ℓ-zero} Bool ; source = lift false
    ; Admit = λ _ → Bool ; advance = λ x q → not q
    ; Extra = λ x y w → snd w ≡ snd (fst x)
    ; certify = λ x → refl }
  composite : Refinement base
  composite = compose first second
  generated : Layer1.generate (compile composite) (false , true , false)
    ≡ ((true , false , true) , refl , true , refl)
  generated = refl

  -- Same endpoints and original R witness, wrong first-layer proof:
  -- the second layer cannot certify the changed payload.
  rejects-erasure : Refinement.Extra second
    ((false , true) , false) ((true , false) , true) (refl , false) → ⊥
  rejects-erasure = false≢true

  third : Refinement (compile second)
  third = record
    { Source = Lift {j = ℓ-suc ℓ-zero} Bool ; source = lift true
    ; Admit = λ _ → Bool ; advance = λ x p → not p
    ; Extra = λ x y w → snd (fst w) ≡ snd (fst (fst x))
    ; certify = λ x → refl }
  module A = Associativity first second third
  reused : Refinement base
  reused = compose composite (Composite.rebase first second third)
  reused-is-left : reused ≡ A.left
  reused-is-left = refl
  generated-associator :
    Iso.fun (Realization.steps A.associator (false , (true , false) , true))
      (Layer1.generate (compile reused) (false , (true , false) , true))
      ≡ Layer1.generate (compile A.right) (false , true , false , true)
  generated-associator = refl

  module C = Composer ℓ-zero
  request : C.Request
  request = record { base = base ; first = first ; second = second }
  returned-composite : fst (C.solve request) ≡ composite
  returned-composite = refl
