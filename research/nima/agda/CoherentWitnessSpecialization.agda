{-# OPTIONS --safe --cubical --guardedness #-}
module CoherentWitnessSpecialization where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (Iso; iso)
open import Cubical.Data.Unit.Base using (tt*)
open import Cubical.Data.Bool.Base using (Bool; true; false; not)
open import TypedGeneratorLayers using (Layer1)
open import ComposableWitnessSpecialization

-- Extend the canonical composite rebase through one more refinement. The
-- second tail can depend on every retained proof in the first tail.
module Tail {ℓ : Level} {L : Layer1 ℓ} (F : Refinement L)
  (G : Refinement (compile F)) (H : Refinement (compile G)) where
  module C = Composite F G
  rebased : Refinement (compile (compose F G))
  rebased = C.rebase H
  module N = Layer1 (compile H)
  module B = Layer1 (compile rebased)
  unflatten : B.State → N.State
  unflatten (x , p) = C.unflatten x , p
  unflatten-edge : {x y : B.State} → B.Witness x y → N.Witness (unflatten x) (unflatten y)
  unflatten-edge (w , e) = C.unflatten-edge w , e
  rebase-next : Refinement (compile H) → Refinement (compile rebased)
  rebase-next J = record
    { Source = J.Source ; source = J.source
    ; Admit = λ x → J.Admit (unflatten x)
    ; advance = λ x p → J.advance (unflatten x) p
    ; Extra = λ { (x , p) (y , q) w →
        J.Extra (unflatten x , p) (unflatten y , q) (unflatten-edge w) }
    ; certify = λ { (x , p) → J.certify (unflatten x , p) } }
    where module J = Refinement J

  -- This is the typing gate for the (FG)(HJ) vertex, not an assumed law.
  rebase-compose : (J : Refinement (compile H))
    → C.rebase (compose H J) ≡ compose rebased (rebase-next J)
  rebase-compose J = refl

module Pentagon {ℓ : Level} {L : Layer1 ℓ} (F : Refinement L)
  (G : Refinement (compile F)) (H : Refinement (compile G))
  (J : Refinement (compile H)) where
  module T = Tail F G H
  FG = compose F G
  GH = compose G H
  H' = T.rebased
  J' = T.rebase-next J
  JGH = Composite.rebase G H J

  -- Five genuinely composed operands of the same Refinement L family.
  P0 P1 P2 P3 P4 : Refinement L
  P0 = compose (compose FG H') (Composite.rebase FG H' J')
  P1 = compose (compose F GH) (Composite.rebase F GH JGH)
  P2 = compose F (compose GH JGH)
  P3 = compose F (compose G (compose H J))
  P4 = compose FG (compose H' J')
  module V0 = Layer1 (compile P0)
  module V1 = Layer1 (compile P1)
  module V2 = Layer1 (compile P2)
  module V3 = Layer1 (compile P3)
  module V4 = Layer1 (compile P4)

  module AFGH = Associativity F G H
  module AGHJ = Associativity G H J
  module A12 = Associativity F GH JGH
  module A04 = Associativity FG H' J'
  module A43 = Associativity F G (compose H J)

  -- Right whiskering of the actual F,G,H associator through J.
  f01 : V0.State → V1.State
  f01 (s , ((p , q) , r) , z) = s , (p , q , r) , z
  b01 : V1.State → V0.State
  b01 (s , (p , q , r) , z) = s , ((p , q) , r) , z
  w01 : {x y : V0.State} → V0.Witness x y → V1.Witness (f01 x) (f01 y)
  w01 (w , ((e , f) , h) , k) = w , (e , f , h) , k
  v01 : {x y : V1.State} → V1.Witness x y → V0.Witness (b01 x) (b01 y)
  v01 (w , (e , f , h) , k) = w , ((e , f) , h) , k
  e01 : Realization (compile P0) (compile P1)
  e01 = record
    { states = iso f01 b01 (λ _ → refl) (λ _ → refl)
    ; steps = λ x → iso (λ { (y , w) → f01 y , w01 w })
        (λ { (y , w) → b01 y , v01 w }) (λ _ → refl) (λ _ → refl)
    ; endpoints = λ x z → refl ; generated = λ x → refl }

  -- Check the right-whiskered state map restricts to the supplied associator.
  prefix0 : V0.State → AFGH.A.State
  prefix0 (s , pqr , z) = s , pqr
  prefix1 : V1.State → AFGH.B.State
  prefix1 (s , pqr , z) = s , pqr
  right-whiskering : (x : V0.State) → prefix1 (f01 x) ≡ AFGH.forward (prefix0 x)
  right-whiskering x = refl
  right-whiskering-witness : {x y : V0.State} (w : V0.Witness x y)
    → (fst (w01 w) , fst (snd (w01 w)))
      ≡ AFGH.edge-forward {x = prefix0 x} {y = prefix0 y} (fst w , fst (snd w))
  right-whiskering-witness w = refl

  e12 : Realization (compile P1) (compile P2)
  e12 = A12.associator

  -- Left whiskering of the actual G,H,J associator by F.
  f23 : V2.State → V3.State
  f23 (s , p , (q , r) , z) = s , p , q , r , z
  b23 : V3.State → V2.State
  b23 (s , p , q , r , z) = s , p , (q , r) , z
  w23 : {x y : V2.State} → V2.Witness x y → V3.Witness (f23 x) (f23 y)
  w23 (w , e , (f , h) , k) = w , e , f , h , k
  v23 : {x y : V3.State} → V3.Witness x y → V2.Witness (b23 x) (b23 y)
  v23 (w , e , f , h , k) = w , e , (f , h) , k
  e23 : Realization (compile P2) (compile P3)
  e23 = record
    { states = iso f23 b23 (λ _ → refl) (λ _ → refl)
    ; steps = λ x → iso (λ { (y , w) → f23 y , w23 w })
        (λ { (y , w) → b23 y , v23 w }) (λ _ → refl) (λ _ → refl)
    ; endpoints = λ x z → refl ; generated = λ x → refl }
  expand2 : V2.State → AGHJ.A.State
  expand2 (s , p , rest) = (s , p) , rest
  expand3 : V3.State → AGHJ.B.State
  expand3 (s , p , rest) = (s , p) , rest
  left-whiskering : (x : V2.State) → expand3 (f23 x) ≡ AGHJ.forward (expand2 x)
  left-whiskering x = refl
  left-whiskering-witness : {x y : V2.State} (w : V2.Witness x y)
    → ((fst (w23 w) , fst (snd (w23 w))) , snd (snd (w23 w)))
      ≡ AGHJ.edge-forward {x = expand2 x} {y = expand2 y}
        ((fst w , fst (snd w)) , snd (snd w))
  left-whiskering-witness w = refl

  e04 : Realization (compile P0) (compile P4)
  e04 = A04.associator
  e43 : Realization (compile P4) (compile P3)
  e43 = A43.associator

  long-state short-state : V0.State → V3.State
  long-state x = Iso.fun (Realization.states e23)
    (Iso.fun (Realization.states e12) (Iso.fun (Realization.states e01) x))
  short-state x = Iso.fun (Realization.states e43) (Iso.fun (Realization.states e04) x)
  state-pentagon : long-state ≡ short-state
  state-pentagon = refl

  long-step short-step : (x : V0.State) → Step (compile P0) x → Step (compile P3) (short-state x)
  long-step x z = Iso.fun (Realization.steps e23 _)
    (Iso.fun (Realization.steps e12 _) (Iso.fun (Realization.steps e01 x) z))
  short-step x z = Iso.fun (Realization.steps e43 _) (Iso.fun (Realization.steps e04 x) z)
  step-pentagon : long-step ≡ short-step
  step-pentagon = refl
  generated-pentagon : (x : V0.State)
    → long-step x (V0.generate x) ≡ V3.generate (short-state x)
  generated-pentagon x = refl

  -- Source associators use the same operands and retain the original records.
  source01 : Refinement.Source P0 → Refinement.Source P1
  source01 (abc , d) = Iso.fun AFGH.source-associator abc , d
  source23 : Refinement.Source P2 → Refinement.Source P3
  source23 (a , bcd) = a , Iso.fun AGHJ.source-associator bcd
  long-source short-source : Refinement.Source P0 → Refinement.Source P3
  long-source x = source23 (Iso.fun A12.source-associator (source01 x))
  short-source x = Iso.fun A43.source-associator (Iso.fun A04.source-associator x)
  source-pentagon : long-source ≡ short-source
  source-pentagon = refl
  sources-preserved : long-source (Refinement.source P0) ≡ Refinement.source P3
  sources-preserved = refl

module Triangle {ℓ : Level} {L : Layer1 ℓ} (F : Refinement L)
  (G : Refinement (compile F)) where
  unit = identity (compile F)
  module UF = Units F
  module UG = Units G
  module A = Associativity F unit UG.after-identity
  target = compose F G
  module V0 = Layer1 (compile A.left)
  module V1 = Layer1 (compile A.right)
  module V2 = Layer1 (compile target)

  -- Right unitor on F, whiskered by G.
  direct-state : V0.State → V2.State
  direct-state (s , (p , _) , q) = s , p , q
  direct : Realization (compile A.left) (compile target)
  direct = record
    { states = iso direct-state (λ { (s , p , q) → s , (p , tt*) , q })
        (λ _ → refl) (λ _ → refl)
    ; steps = λ x → iso (λ { ((s , (p , _) , q) , w , (e , _) , f) → (s , p , q) , w , e , f })
        (λ { ((s , p , q) , w , e , f) → (s , (p , tt*) , q) , w , (e , tt*) , f })
        (λ _ → refl) (λ _ → refl)
    ; endpoints = λ x z → refl ; generated = λ x → refl }
  -- Left unitor on G, whiskered by F.
  finish : Realization (compile A.right) (compile target)
  finish = record
    { states = iso (λ { (s , p , _ , q) → s , p , q })
        (λ { (s , p , q) → s , p , tt* , q }) (λ _ → refl) (λ _ → refl)
    ; steps = λ x → iso (λ { ((s , p , _ , q) , w , e , _ , f) → (s , p , q) , w , e , f })
        (λ { ((s , p , q) , w , e , f) → (s , p , tt* , q) , w , e , tt* , f })
        (λ _ → refl) (λ _ → refl)
    ; endpoints = λ x z → refl ; generated = λ x → refl }

  -- These are whiskerings of the previously constructed unitors, including
  -- their full step maps, rather than new unrelated deletion functions.
  prefix0 : V0.State → Layer1.State (compile (compose F unit))
  prefix0 (s , pu , q) = s , pu
  prefix2 : V2.State → Layer1.State (compile F)
  prefix2 (s , p , q) = s , p
  restrict0 : (x : V0.State) → Step (compile A.left) x → Step (compile (compose F unit)) (prefix0 x)
  restrict0 x (y , w) = prefix0 y , fst w , fst (snd w)
  restrict2 : (x : V2.State) → Step (compile target) x → Step (compile F) (prefix2 x)
  restrict2 x (y , w) = prefix2 y , fst w , fst (snd w)
  right-unit-whiskering : (x : V0.State) (z : Step (compile A.left) x)
    → restrict2 (direct-state x) (Iso.fun (Realization.steps direct x) z)
      ≡ Iso.fun (Realization.steps UF.right-unit (prefix0 x)) (restrict0 x z)
  right-unit-whiskering x z = refl

  expand1 : V1.State → Layer1.State (compile (compose unit UG.after-identity))
  expand1 (s , p , uq) = (s , p) , uq
  expand2 : V2.State → Layer1.State (compile G)
  expand2 (s , p , q) = (s , p) , q
  expand-step1 : (x : V1.State) → Step (compile A.right) x
    → Step (compile (compose unit UG.after-identity)) (expand1 x)
  expand-step1 x (y , w) = expand1 y , (fst w , fst (snd w)) , snd (snd w)
  expand-step2 : (x : V2.State) → Step (compile target) x → Step (compile G) (expand2 x)
  expand-step2 x (y , w) = expand2 y , (fst w , fst (snd w)) , snd (snd w)
  left-unit-whiskering : (x : V1.State) (z : Step (compile A.right) x)
    → expand-step2 (Iso.fun (Realization.states finish) x) (Iso.fun (Realization.steps finish x) z)
      ≡ Iso.fun (Realization.steps UG.left-unit (expand1 x)) (expand-step1 x z)
  left-unit-whiskering x z = refl

  long-state : V0.State → V2.State
  long-state x = Iso.fun (Realization.states finish) (A.forward x)
  state-triangle : long-state ≡ direct-state
  state-triangle = refl
  long-step short-step : (x : V0.State) → Step (compile A.left) x → Step (compile target) (direct-state x)
  long-step x z = Iso.fun (Realization.steps finish _) (Iso.fun (Realization.steps A.associator x) z)
  short-step x z = Iso.fun (Realization.steps direct x) z
  step-triangle : long-step ≡ short-step
  step-triangle = refl
  generated-triangle : (x : V0.State) → long-step x (V0.generate x) ≡ V2.generate (direct-state x)
  generated-triangle x = refl

  long-source short-source : Refinement.Source A.left → Refinement.Source target
  long-source x = fst (Iso.fun A.source-associator x) , snd (snd (Iso.fun A.source-associator x))
  short-source ((a , _) , b) = a , b
  source-triangle : long-source ≡ short-source
  source-triangle = refl
  sources-preserved : long-source (Refinement.source A.left) ≡ Refinement.source target
  sources-preserved = refl

module Fixture where
  module F = ProofDependentFixture
  fourth : Refinement (compile F.third)
  fourth = record
    { Source = Lift {j = ℓ-suc ℓ-zero} Bool ; source = lift false
    ; Admit = λ _ → Bool ; advance = λ x p → not p
    ; Extra = λ x y w → snd (fst (fst w)) ≡ snd (fst (fst (fst x)))
    ; certify = λ x → refl }
  module P = Pentagon F.first F.second F.third fourth
  input : P.V0.State
  input = false , ((true , false) , true) , false
  generated : P.long-step input (P.V0.generate input)
    ≡ P.V3.generate (false , true , false , true , false)
  generated = refl
  changed-output : fst (P.long-step input (P.V0.generate input))
    ≡ (true , false , true , false , true)
  changed-output = refl
  module T = Triangle F.first F.second
  triangle-input : T.V0.State
  triangle-input = false , (true , tt*) , false
  triangle-generated : T.long-step triangle-input (T.V0.generate triangle-input)
    ≡ T.V2.generate (false , true , false)
  triangle-generated = refl
