{-# OPTIONS --safe --cubical --guardedness #-}
module TypedGeneratorPresentation where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_; equivFun; invEq; secEq; retEq; idEquiv; compEquiv; equivCtr; equivCtrPath)
open import Cubical.Foundations.Isomorphism using (iso; isoToEquiv)
open import TypedGeneratorLayers using (Layer1; Layer2)
open import TypedGeneratorTransport using (Layer3; Stack3; extend3)

-- A declared presentation of A, with a fixed retained boundary B.
-- Only its certified dependent remainder may be omitted from the view.
record Reduction {ℓA ℓB ℓF : Level} (A : Type ℓA) (B : Type ℓB)
  : Type (ℓ-max ℓA (ℓ-max ℓB (ℓ-suc ℓF))) where
  field
    Hidden : B → Type ℓF
    presentation : A ≃ Σ B Hidden
    completed : (b : B) → isContr (Hidden b)

  compact : A → B
  compact a = fst (equivFun presentation a)

  recover : B → A
  recover b = invEq presentation (b , fst (completed b))

  boundary-recovered : (b : B) → compact (recover b) ≡ b
  boundary-recovered b = cong fst (secEq presentation (b , fst (completed b)))

  source-recovered : (a : A) → recover (compact a) ≡ a
  source-recovered a =
    cong (invEq presentation)
      (λ i → compact a , snd (completed (compact a)) (snd (equivFun presentation a)) i)
    ∙ retEq presentation a

  equivalence : A ≃ B
  equivalence = isoToEquiv (iso compact recover boundary-recovered source-recovered)

  injective : {a a' : A} → compact a ≡ compact a' → a ≡ a'
  injective {a} {a'} p = sym (source-recovered a) ∙ cong recover p ∙ source-recovered a'

  observations-preserved : {ℓX : Level} {X : Type ℓX} (observe : A → X) (a : A)
    → observe (recover (compact a)) ≡ observe a
  observations-preserved observe a = cong observe (source-recovered a)

  -- Source and recovery comparison vary together in this complete package.
  Recovery : B → Type (ℓ-max ℓA ℓB)
  Recovery b = Σ[ a ∈ A ] (compact a ≡ b)

  recovery-certificate : (b : B) → isContr (Recovery b)
  recovery-certificate b = equivCtr equivalence b , equivCtrPath equivalence b

  recovery-comparisons : (b : B) (r s : Recovery b) → isContr (r ≡ s)
  recovery-comparisons b r s = p , isProp→isSet h r s p
    where
    h : isProp (Recovery b)
    h = isContr→isProp (recovery-certificate b)
    p : r ≡ s
    p = h r s

  higher-certificate : (b : B) → isContr (isContr (Hidden b))
  higher-certificate b = completed b , isPropIsContr (completed b)

contractRemainder : {ℓB ℓF : Level} {B : Type ℓB} (F : B → Type ℓF)
  → ((b : B) → isContr (F b)) → Reduction {ℓF = ℓF} (Σ B F) B
contractRemainder F c = record
  { Hidden = F ; presentation = idEquiv _ ; completed = c }

-- Any already certified equivalence has a fiber presentation. This supplies
-- identity and successive reductions without assuming any new erasure rule.
fromEquivalence : {ℓA ℓB : Level} {A : Type ℓA} {B : Type ℓB}
  → A ≃ B → Reduction {ℓF = ℓ-max ℓA ℓB} A B
fromEquivalence {A = A} {B = B} e = record
  { Hidden = F
  ; presentation = isoToEquiv (iso pack unpack unpack-pack pack-unpack)
  ; completed = λ b → equivCtr e b , equivCtrPath e b
  }
  where
  F : B → Type _
  F b = Σ[ a ∈ A ] (equivFun e a ≡ b)
  pack : A → Σ B F
  pack a = equivFun e a , a , refl
  unpack : Σ B F → A
  unpack z = fst (snd z)
  unpack-pack : (z : Σ B F) → pack (unpack z) ≡ z
  unpack-pack (b , a , p) i = p i , a , λ j → p (i ∧ j)
  pack-unpack : (a : A) → unpack (pack a) ≡ a
  pack-unpack a = refl

identity-reduction : {ℓ : Level} (A : Type ℓ) → Reduction {ℓF = ℓ} A A
identity-reduction A = fromEquivalence (idEquiv A)

compact-identity : {ℓ : Level} {A : Type ℓ} (a : A)
  → Reduction.compact (identity-reduction A) a ≡ a
compact-identity a = refl

then : {ℓA ℓB ℓC ℓF ℓG : Level} {A : Type ℓA} {B : Type ℓB} {C : Type ℓC}
  → Reduction {ℓF = ℓF} A B → Reduction {ℓF = ℓG} B C
  → Reduction {ℓF = ℓ-max ℓA ℓC} A C
then p q = fromEquivalence (compEquiv (Reduction.equivalence p) (Reduction.equivalence q))

compact-composes : {ℓA ℓB ℓC ℓF ℓG : Level} {A : Type ℓA} {B : Type ℓB} {C : Type ℓC}
  (p : Reduction {ℓF = ℓF} A B) (q : Reduction {ℓF = ℓG} B C) (a : A)
  → Reduction.compact (then p q) a ≡ Reduction.compact q (Reduction.compact p a)
compact-composes p q a = refl

recover-composes : {ℓA ℓB ℓC ℓF ℓG : Level} {A : Type ℓA} {B : Type ℓB} {C : Type ℓC}
  (p : Reduction {ℓF = ℓF} A B) (q : Reduction {ℓF = ℓG} B C) (c : C)
  → Reduction.recover (then p q) c ≡ Reduction.recover p (Reduction.recover q c)
recover-composes p q c = Reduction.injective (then p q)
  (Reduction.boundary-recovered (then p q) c ∙ sym
    (cong (Reduction.compact q) (Reduction.boundary-recovered p (Reduction.recover q c))
      ∙ Reduction.boundary-recovered q c))

compact-associative : {ℓA ℓB ℓC ℓD ℓF ℓG ℓH : Level}
  {A : Type ℓA} {B : Type ℓB} {C : Type ℓC} {D : Type ℓD}
  (p : Reduction {ℓF = ℓF} A B) (q : Reduction {ℓF = ℓG} B C)
  (r : Reduction {ℓF = ℓH} C D) (a : A)
  → Reduction.compact (then (then p q) r) a ≡ Reduction.compact (then p (then q r)) a
compact-associative p q r a = refl

module Associativity {ℓA ℓB ℓC ℓD ℓF ℓG ℓH : Level}
  {A : Type ℓA} {B : Type ℓB} {C : Type ℓC} {D : Type ℓD}
  (p : Reduction {ℓF = ℓF} A B) (q : Reduction {ℓF = ℓG} B C)
  (r : Reduction {ℓF = ℓH} C D) where
  left = then (then p q) r
  right = then p (then q r)

  -- The two recoveries agree as complete source-and-comparison packages.
  recovery-agreement : (d : D) → Path (Reduction.Recovery left d)
    (Reduction.recover left d , Reduction.boundary-recovered left d)
    (Reduction.recover right d , Reduction.boundary-recovered right d)
  recovery-agreement d = isContr→isProp (Reduction.recovery-certificate left d) _ _

-- Layer 4 is data OVER a fixed Layer 3, not a replacement for its histories.
record Layer4 {ℓ ℓP : Level} {L : Layer1 ℓ} {K : Layer2 L}
  (T : Layer3 L K ℓP) (ℓB ℓF : Level)
  : Type (ℓ-max ℓ (ℓ-max ℓP (ℓ-max (ℓ-suc ℓB) (ℓ-suc ℓF)))) where
  open Layer1 L using (State)
  module E = Layer3 T
  field
    View : State → State → Type ℓB
    reduction : (s t : State) → Reduction {ℓF = ℓF} (E.Retained s t) (View s t)

  compact : {s t : State} → E.Retained s t → View s t
  compact {s} {t} = Reduction.compact (reduction s t)
  recover : {s t : State} → View s t → E.Retained s t
  recover {s} {t} = Reduction.recover (reduction s t)
  source-recovered : {s t : State} (r : E.Retained s t) → recover (compact r) ≡ r
  source-recovered {s} {t} = Reduction.source-recovered (reduction s t)
  boundary-recovered : {s t : State} (v : View s t) → compact (recover v) ≡ v
  boundary-recovered {s} {t} = Reduction.boundary-recovered (reduction s t)

  history-recovered : {s t : State} (r : E.Retained s t) → fst (recover (compact r)) ≡ fst r
  history-recovered r = cong fst (source-recovered r)
  input-recovered : {s t : State} (r : E.Retained s t)
    → fst (snd (recover (compact r))) ≡ fst (snd r)
  input-recovered r = cong (λ p → fst (snd p)) (source-recovered r)
  output-recovered : {s t : State} (r : E.Retained s t)
    → fst (snd (snd (recover (compact r)))) ≡ fst (snd (snd r))
  output-recovered r = cong (λ p → fst (snd (snd p))) (source-recovered r)

-- Further simplify a Layer 4 view without changing its underlying stack.
after4 : {ℓ ℓP ℓB ℓF ℓC ℓG : Level} {L : Layer1 ℓ} {K : Layer2 L}
  {T : Layer3 L K ℓP} (Q : Layer4 T ℓB ℓF)
  (W : Layer1.State L → Layer1.State L → Type ℓC)
  → ((s t : Layer1.State L) → Reduction {ℓF = ℓG} (Layer4.View Q s t) (W s t))
  → Layer4 T ℓC (ℓ-max (ℓ-max ℓ ℓP) ℓC)
after4 Q W step = record
  { View = W ; reduction = λ s t → then (Layer4.reduction Q s t) (step s t) }

-- Canonical policy: retain history and input; omit the recomputable output
-- TOGETHER WITH its agreement witness, using Layer 3's output certificate.
module Canonical {ℓ ℓP : Level} {L : Layer1 ℓ} {K : Layer2 L} (T : Layer3 L K ℓP) where
  open Layer1 L using (State)
  module E = Layer3 T
  Request : State → State → Type (ℓ-max ℓ ℓP)
  Request s t = Σ[ h ∈ Layer2.HistoryType K s t ] E.Payload s

  output-reduction : (s t : State) → Reduction {ℓF = ℓP} (E.Retained s t) (Request s t)
  output-reduction s t = record
    { Hidden = λ r → E.Output (fst r) (snd r)
    ; presentation = isoToEquiv (iso
        (λ r → (fst r , fst (snd r)) , snd (snd r))
        (λ r → fst (fst r) , snd (fst r) , snd r)
        (λ r → refl) (λ r → refl))
    ; completed = λ r → E.output-certificate (fst r) (snd r)
    }

  layer4 : Layer4 T (ℓ-max ℓ ℓP) ℓP
  layer4 = record { View = Request ; reduction = output-reduction }

  compact-retained : {s t : State} (h : Layer2.HistoryType K s t) (x : E.Payload s)
    → Layer4.compact layer4 (E.retain h x) ≡ (h , x)
  compact-retained h x = refl

  recover-request : {s t : State} (h : Layer2.HistoryType K s t) (x : E.Payload s)
    → Layer4.recover layer4 (h , x) ≡ E.retain h x
  recover-request h x = refl

Stack4 : (ℓ ℓP ℓB ℓF : Level) → Type (ℓ-suc (ℓ-max ℓ (ℓ-max ℓP (ℓ-max ℓB ℓF))))
Stack4 ℓ ℓP ℓB ℓF = Σ[ L ∈ Layer1 ℓ ] Σ[ K ∈ Layer2 L ]
  Σ[ T ∈ Layer3 L K ℓP ] Layer4 T ℓB ℓF

extend4 : {ℓ ℓP ℓB ℓF : Level} {L : Layer1 ℓ} {K : Layer2 L} {T : Layer3 L K ℓP}
  → Layer4 T ℓB ℓF → Stack4 ℓ ℓP ℓB ℓF
extend4 {L = L} {K = K} {T = T} Q = L , K , T , Q

layers-recovered : {ℓ ℓP ℓB ℓF : Level} {L : Layer1 ℓ} {K : Layer2 L} {T : Layer3 L K ℓP}
  (Q : Layer4 T ℓB ℓF) → Path (Stack3 ℓ ℓP)
    (fst (extend4 Q) , fst (snd (extend4 Q)) , fst (snd (snd (extend4 Q)))) (extend3 T)
layers-recovered Q = refl

module Controls where
  open import Cubical.Data.Bool.Base using (Bool; false; true)
  open import Cubical.Data.Bool.Properties using (false≢true)
  open import Cubical.Data.Empty.Base using (⊥)
  import TypedGeneratorTransport as D
  import DependentTransportMachine as M
  import IndexIdentityCoherenceRegression as C
  module MB = D.MachineBridge
  module E = Layer3 MB.P.transport-layer
  module Policy = Canonical MB.P.transport-layer
  module Q = Layer4 Policy.layer4

  Run : Type
  Run = E.Retained C.base-index C.base-index

  idle twice : Run
  idle = E.retain (MB.history M.stay) true
  twice = E.retain (MB.history (M.follow M.turn M.turn)) true

  score : Run → Bool
  score r = fst (snd (snd r))

  same-score : score idle ≡ score twice
  same-score = sym (MB.two-turns true)

  runs-distinct : idle ≡ twice → ⊥
  runs-distinct p = MB.two-histories-distinct (cong fst p)

  views-distinct : Q.compact idle ≡ Q.compact twice → ⊥
  views-distinct p = MB.two-histories-distinct (cong fst p)

  no-score-recovery : (decode : Bool → Run) → ((r : Run) → decode (score r) ≡ r) → ⊥
  no-score-recovery decode law = runs-distinct
    (sym (law idle) ∙ cong decode same-score ∙ law twice)

  no-score-reduction : {ℓF : Level} (q : Reduction {ℓF = ℓF} Run Bool)
    → ((r : Run) → Reduction.compact q r ≡ score r) → ⊥
  no-score-reduction q law = no-score-recovery (Reduction.recover q)
    (λ r → cong (Reduction.recover q) (sym (law r)) ∙ Reduction.source-recovered q r)

  no-bool-completion : isContr Bool → ⊥
  no-bool-completion c = false≢true (sym (snd c false) ∙ snd c true)

  -- A genuine two-stage reduction: first omit an extra completion certificate,
  -- then omit the output/agreement package while retaining history and input.
  Extra : Run → Type
  Extra r = isContr (E.Output (fst r) (fst (snd r)))
  Wrapped : Type
  Wrapped = Σ Run Extra
  first : Reduction {ℓF = ℓ-zero} Wrapped Run
  first = contractRemainder Extra (λ r → E.higher-certificate (fst r) (fst (snd r)))
  combined : Reduction {ℓF = ℓ-zero} Wrapped (Policy.Request C.base-index C.base-index)
  combined = then first (Policy.output-reduction C.base-index C.base-index)
  wrapped : Wrapped
  wrapped = twice , E.output-certificate (fst twice) (fst (snd twice))

  two-stage-view : Reduction.compact combined wrapped
    ≡ (MB.history (M.follow M.turn M.turn) , true)
  two-stage-view = refl
  two-stage-recovery : Reduction.recover combined (Reduction.compact combined wrapped) ≡ wrapped
  two-stage-recovery = Reduction.source-recovered combined wrapped
