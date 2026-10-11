{-# OPTIONS --safe --cubical --guardedness #-}
module DisplayedWitnessSpecialization where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (Iso; iso)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Bool.Base using (Bool; true; false; if_then_else_)
open import Cubical.Data.Unit.Base using (Unit*; tt*)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Categories.Category.Base using (Category)
open import Cubical.Categories.Displayed.Base using (Categoryᴰ)
open import Cubical.Categories.Constructions.TotalCategory.Base using (∫C)
open import Cubical.Categories.Functor.Base using (Functor)
open import Cubical.Foundations.HLevels using (isOfHLevelRetractFromIso)
open import TypedGeneratorLayers using (Layer1; module Histories)
open import ComposableWitnessSpecialization using (Refinement; compile; compose; module ProofDependentFixture)

-- No identities/composition are assumed of a WG's original witness relation.
record Graph (ℓ : Level) : Type (ℓ-suc ℓ) where
  field
    Node : Type ℓ
    Edge : Node → Node → Type ℓ

underlying : {ℓ : Level} → Layer1 ℓ → Graph ℓ
underlying L = record { Node = Layer1.State L ; Edge = Layer1.Witness L }

record Display {ℓ : Level} (B : Graph ℓ) : Type (ℓ-suc ℓ) where
  open Graph B
  field
    Fiber : Node → Type ℓ
    Over : {s t : Node} → Edge s t → Fiber s → Fiber t → Type ℓ

total : {ℓ : Level} {B : Graph ℓ} → Display B → Graph ℓ
total {B = B} D = record
  { Node = Σ[ s ∈ Graph.Node B ] Display.Fiber D s
  ; Edge = λ { (s , p) (t , q) → Σ[ r ∈ Graph.Edge B s t ] Display.Over D r p q } }

record ChosenLift {ℓ : Level} (L : Layer1 ℓ) (D : Display (underlying L)) : Type ℓ where
  field
    advance : (s : Layer1.State L) → Display.Fiber D s → Display.Fiber D (Layer1.next L s)
    witness : (s : Layer1.State L) (p : Display.Fiber D s)
      → Display.Over D (Layer1.edge L s) p (advance s p)

total-WG : {ℓ : Level} {L : Layer1 ℓ} (D : Display (underlying L)) → ChosenLift L D → Layer1 ℓ
total-WG {L = L} D K = record
  { State = Graph.Node (total D) ; Witness = Graph.Edge (total D)
  ; generate = λ { (s , p) → (Layer1.next L s , ChosenLift.advance K s p) ,
      Layer1.edge L s , ChosenLift.witness K s p } }

-- Displayed total construction, corresponding to dependent sums of families.
sum-display : {ℓ : Level} {B : Graph ℓ} (D : Display B) → Display (total D) → Display B
sum-display D E = record
  { Fiber = λ s → Σ[ p ∈ Display.Fiber D s ] Display.Fiber E (s , p)
  ; Over = λ r pq uv → Σ[ e ∈ Display.Over D r (fst pq) (fst uv) ]
      Display.Over E (r , e) (snd pq) (snd uv) }

display : {ℓ : Level} {L : Layer1 ℓ} → Refinement L → Display (underlying L)
display F = record
  { Fiber = Refinement.Admit F
  ; Over = λ { {s} {t} r p q → Refinement.Extra F (s , p) (t , q) r } }
chosen : {ℓ : Level} {L : Layer1 ℓ} (F : Refinement L) → ChosenLift L (display F)
chosen F = record
  { advance = Refinement.advance F ; witness = λ s p → Refinement.certify F (s , p) }
compilation-is-total : {ℓ : Level} {L : Layer1 ℓ} (F : Refinement L)
  → compile F ≡ total-WG (display F) (chosen F)
compilation-is-total F = refl
composition-is-displayed-sum : {ℓ : Level} {L : Layer1 ℓ} (F : Refinement L)
  (G : Refinement (compile F)) → display (compose F G) ≡ sum-display (display F) (display G)
composition-is-displayed-sum F G = refl

module HistoryDisplay {ℓ : Level} {L : Layer1 ℓ} (F : Refinement L) where
  open Layer1 L
  module F = Refinement F
  module B = Histories L
  module E = Histories (compile F)

  -- A displayed history lies over a particular base history and retains
  -- each intermediate admission and each proof-dependent witness extension.
  data Lifted : {s t : State} → B.History s t → F.Admit s → F.Admit t → Type ℓ where
    done : {s : State} {p : F.Admit s} → Lifted B.empty p p
    more : {s t u : State} {r : Witness s t} {h : B.History t u}
      {p : F.Admit s} {q : F.Admit t} {z : F.Admit u}
      → F.Extra (s , p) (t , q) r → Lifted h q z → Lifted (B.link r h) p z

  FirstLift : {s t : State} → B.History s t → F.Admit s → Type ℓ
  FirstLift B.empty p = Unit*
  FirstLift {s} (B.link {t = t} r h) p = Σ[ q ∈ F.Admit t ] F.Extra (s , p) (t , q) r
  head-lift : {s t : State} {h : B.History s t} {p : F.Admit s} {q : F.Admit t}
    → Lifted h p q → FirstLift h p
  head-lift done = tt*
  head-lift (more {q = q} e _) = q , e

  TotalHistory : (x y : F.RefinedState) → Type ℓ
  TotalHistory (s , p) (t , q) = Σ[ h ∈ B.History s t ] Lifted h p q

  forget : {x y : F.RefinedState} → E.History x y → B.History (fst x) (fst y)
  forget E.empty = B.empty
  forget (E.link (r , e) h) = B.link r (forget h)
  decorate : {x y : F.RefinedState} (h : E.History x y) → Lifted (forget h) (snd x) (snd y)
  decorate E.empty = done
  decorate (E.link (r , e) h) = more e (decorate h)
  pack : {x y : F.RefinedState} → E.History x y → TotalHistory x y
  pack h = forget h , decorate h
  assemble : {s t : State} {h : B.History s t} {p : F.Admit s} {q : F.Admit t}
    → Lifted h p q → E.History (s , p) (t , q)
  assemble done = E.empty
  assemble (more {r = r} e dh) = E.link (r , e) (assemble dh)
  unpack : {x y : F.RefinedState} → TotalHistory x y → E.History x y
  unpack (h , dh) = assemble dh

  unpack-pack : {x y : F.RefinedState} (h : E.History x y) → unpack (pack h) ≡ h
  unpack-pack E.empty = refl
  unpack-pack (E.link w h) = cong (E.link w) (unpack-pack h)
  pack-assemble : {s t : State} {h : B.History s t} {p : F.Admit s} {q : F.Admit t}
    (dh : Lifted h p q) → pack (assemble dh) ≡ (h , dh)
  pack-assemble done = refl
  pack-assemble (more {r = r} e dh) =
    cong (λ tail → B.link r (fst tail) , more e (snd tail)) (pack-assemble dh)
  total-history-iso : (x y : F.RefinedState) → Iso (E.History x y) (TotalHistory x y)
  total-history-iso x y = iso pack unpack (λ { (h , dh) → pack-assemble dh }) unpack-pack

  join-lift : {s t u : State} {h : B.History s t} {k : B.History t u}
    {p : F.Admit s} {q : F.Admit t} {z : F.Admit u}
    → Lifted h p q → Lifted k q z → Lifted (B.join h k) p z
  join-lift done dk = dk
  join-lift (more e dh) dk = more e (join-lift dh dk)

  forget-join : {x y z : F.RefinedState} (h : E.History x y) (k : E.History y z)
    → forget (E.join h k) ≡ B.join (forget h) (forget k)
  forget-join E.empty k = refl
  forget-join (E.link (r , e) h) k = cong (B.link r) (forget-join h k)
  assemble-join : {s t u : State} {h : B.History s t} {k : B.History t u}
    {p : F.Admit s} {q : F.Admit t} {z : F.Admit u}
    (dh : Lifted h p q) (dk : Lifted k q z)
    → assemble (join-lift dh dk) ≡ E.join (assemble dh) (assemble dk)
  assemble-join done dk = refl
  assemble-join (more {r = r} e dh) dk = cong (E.link (r , e)) (assemble-join dh dk)

  pack-join : {x y z : F.RefinedState} (h : E.History x y) (k : E.History y z)
    → pack (E.join h k) ≡ (B.join (forget h) (forget k) , join-lift (decorate h) (decorate k))
  pack-join E.empty k = refl
  pack-join (E.link (r , e) h) k =
    cong (λ tail → B.link r (fst tail) , more e (snd tail)) (pack-join h k)

  -- Actual dependent category laws over the base's chosen law paths.
  right-unit-lift : {s t : State} {h : B.History s t} {p : F.Admit s} {q : F.Admit t}
    (dh : Lifted h p q)
    → PathP (λ i → Lifted (B.right-unit h i) p q) (join-lift dh done) dh
  right-unit-lift done = refl
  right-unit-lift (more e dh) i = more e (right-unit-lift dh i)
  associative-lift : {s t u v : State}
    {h : B.History s t} {k : B.History t u} {m : B.History u v}
    {p : F.Admit s} {q : F.Admit t} {z : F.Admit u} {a : F.Admit v}
    (dh : Lifted h p q) (dk : Lifted k q z) (dm : Lifted m z a)
    → PathP (λ i → Lifted (B.associative h k m i) p a)
        (join-lift (join-lift dh dk) dm) (join-lift dh (join-lift dk dm))
  associative-lift done dk dm = refl
  associative-lift (more e dh) dk dm i = more e (associative-lift dh dk dm i)

  -- Chosen step lifts extend to every generated base history. No claim that
  -- every arbitrary base edge has a lift, let alone a cartesian lift.
  generated-lift : (n : ℕ) (s : State) (p : F.Admit s)
    → Σ[ q ∈ F.Admit (B.at n s) ] Lifted (B.generated n s) p q
  generated-lift zero s p = p , done
  generated-lift (suc n) s p =
    fst tail , more (F.certify (s , p)) (snd tail)
    where tail = generated-lift n (next s) (F.advance s p)

  -- Cubical's library Category/Categoryᴰ require hom-sets. We do not erase
  -- higher witness structure or silently assume these hypotheses.
  module SetValued
    (base-set : {s t : State} → isSet (B.History s t))
    (lift-set : {s t : State} {h : B.History s t} {p : F.Admit s} {q : F.Admit t}
      → isSet (Lifted h p q)) where
    base-category : Category ℓ ℓ
    base-category = record
      { ob = State ; Hom[_,_] = B.History ; id = B.empty ; _⋆_ = B.join
      ; ⋆IdL = B.left-unit ; ⋆IdR = B.right-unit ; ⋆Assoc = B.associative
      ; isSetHom = base-set }
    displayed-category : Categoryᴰ base-category ℓ ℓ
    displayed-category = record
      { ob[_] = F.Admit ; Hom[_][_,_] = Lifted
      ; idᴰ = done ; _⋆ᴰ_ = join-lift
      ; ⋆IdLᴰ = λ dh → refl ; ⋆IdRᴰ = right-unit-lift
      ; ⋆Assocᴰ = associative-lift ; isSetHomᴰ = lift-set }

    library-total : Category ℓ ℓ
    library-total = ∫C displayed-category
    library-total-homs : (x y : F.RefinedState)
      → Iso (E.History x y) (Category.Hom[_,_] library-total x y)
    library-total-homs = total-history-iso
    compiled-history-category : Category ℓ ℓ
    compiled-history-category = record
      { ob = F.RefinedState ; Hom[_,_] = E.History
      ; id = E.empty ; _⋆_ = E.join
      ; ⋆IdL = E.left-unit ; ⋆IdR = E.right-unit ; ⋆Assoc = E.associative
      ; isSetHom = λ { {x} {y} → isOfHLevelRetractFromIso 2
          (library-total-homs x y) (Category.isSetHom library-total) } }
    pack-functor : Functor compiled-history-category library-total
    pack-functor = record
      { F-ob = λ x → x ; F-hom = pack ; F-id = refl ; F-seq = pack-join }
    unpack-functor : Functor library-total compiled-history-category
    unpack-functor = record
      { F-ob = λ x → x ; F-hom = unpack ; F-id = refl
      ; F-seq = λ h k → assemble-join (snd h) (snd k) }
    -- The homwise inverse laws are exactly pack-assemble and unpack-pack;
    -- both object maps are identities, not merely equivalences of labels.

module ProofSensitiveFixture where
  module P = ProofDependentFixture
  module H = HistoryDisplay P.composite
  three-step-lift = H.generated-lift 3 false (true , false)
  changed-admission : fst three-step-lift ≡ (false , true)
  changed-admission = refl
  recovered : H.pack (H.unpack (H.B.generated 3 false , snd three-step-lift))
    ≡ (H.B.generated 3 false , snd three-step-lift)
  recovered = H.pack-assemble (snd three-step-lift)

-- A counterexample to inferring (op)fibration from chosen-step lifting.
-- There are two base loop witnesses. Only the generated true edge lifts;
-- the ungenerated false edge has no lift, regardless of the target fiber.
module NotAutomaticFibration where
  base : Layer1 ℓ-zero
  base = record { State = Unit* ; Witness = λ _ _ → Bool ; generate = λ _ → tt* , true }
  restricted : Refinement base
  restricted = record
    { Source = Unit* ; source = tt* ; Admit = λ _ → Unit*
    ; advance = λ _ _ → tt*
    ; Extra = λ x y r → if r then Unit* else ⊥
    ; certify = λ _ → tt* }
  module H = HistoryDisplay restricted
  chosen-edge-lifts : Refinement.Extra restricted (tt* , tt*) (tt* , tt*) true
  chosen-edge-lifts = tt*
  no-false-edge-lift : (Σ[ q ∈ Refinement.Admit restricted tt* ]
    Refinement.Extra restricted (tt* , tt*) (tt* , q) false) → ⊥
  no-false-edge-lift (q , e) = e
  no-false-history-lift : {q : Refinement.Admit restricted tt*}
    → H.Lifted (H.B.single false) tt* q → ⊥
  no-false-history-lift dh = no-false-edge-lift (H.head-lift dh)
