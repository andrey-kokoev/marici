{-# OPTIONS --safe --cubical --guardedness #-}
module TypedGeneratorTransport where

open import Cubical.Foundations.Prelude hiding (empty)
open import Cubical.Foundations.Transport using (substComposite)
open import Cubical.Foundations.GroupoidLaws using (lUnit; rUnit)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sigma.Base using (_×_)
open import TypedGeneratorLayers hiding (is-empty)
import DependentTransportMachine as M
import IndexIdentityCoherenceRegression as C
import IndexIdentityCoherence as I
open I.Indexed ℓ-zero using (Index; Fibre)

-- Layer 3 is data OVER the existing Layer 2, not a replacement for it.
-- The general interface only assumes typed movement along individual edges.
record Layer3 {ℓ : Level} (L : Layer1 ℓ) (K : Layer2 L) (ℓP : Level)
  : Type (ℓ-max ℓ (ℓ-suc ℓP)) where
  open Layer1 L
  module H = Histories L
  field
    Payload : State → Type ℓP
    move : {s t : State} → Witness s t → Payload s → Payload t

  walk : {s t : State} → H.History s t → Payload s → Payload t
  walk H.empty x = x
  walk (H.link w h) x = walk h (move w x)

  walk-join : {s t u : State} (h : H.History s t) (k : H.History t u) (x : Payload s)
    → walk (H.join h k) x ≡ walk k (walk h x)
  walk-join H.empty k x = refl
  walk-join (H.link w h) k x = walk-join h k (move w x)

  execute : {s t : State} → Layer2.HistoryType K s t → Payload s → Payload t
  execute h x = walk (Layer2.decode K h) x

  execute-compose : {s t u : State} (h : Layer2.HistoryType K s t)
    (k : Layer2.HistoryType K t u) (x : Payload s)
    → execute (Layer2.compose K h k) x ≡ execute k (execute h x)
  execute-compose h k x = cong (λ z → walk z x) (Layer2.composition-preserved K h k)
    ∙ walk-join (Layer2.decode K h) (Layer2.decode K k) x

  execute-identity : (s : State) (x : Payload s) → execute (Layer2.identity K s) x ≡ x
  execute-identity s x = cong (λ z → walk z x) (Layer2.decode-encode K H.empty)

  execute-single : {s t : State} (w : Witness s t) (x : Payload s)
    → execute (Layer2.single K w) x ≡ move w x
  execute-single w x = cong (λ z → walk z x) (Layer2.decode-encode K (H.single w))

  -- Fixed history and input; the output remains in its endpoint-dependent type.
  Output : {s t : State} (h : Layer2.HistoryType K s t) (x : Payload s) → Type ℓP
  Output {t = t} h x = Σ[ y ∈ Payload t ] (execute h x ≡ y)

  output-certificate : {s t : State} (h : Layer2.HistoryType K s t) (x : Payload s)
    → isContr (Output h x)
  output-certificate h x = (execute h x , refl) , λ { (y , p) i → p i , (λ j → p (i ∧ j)) }

  higher-certificate : {s t : State} (h : Layer2.HistoryType K s t) (x : Payload s)
    → isContr (isContr (Output h x))
  higher-certificate h x = output-certificate h x , isPropIsContr (output-certificate h x)

  Retained : (s t : State) → Type (ℓ-max ℓ ℓP)
  Retained s t = Σ[ h ∈ Layer2.HistoryType K s t ] Σ[ x ∈ Payload s ] Output h x

  retain : {s t : State} (h : Layer2.HistoryType K s t) (x : Payload s) → Retained s t
  retain h x = h , x , execute h x , refl

  history-recovered : {s t : State} (h : Layer2.HistoryType K s t) (x : Payload s)
    → fst (retain h x) ≡ h
  history-recovered h x = refl

  input-recovered : {s t : State} (h : Layer2.HistoryType K s t) (x : Payload s)
    → fst (snd (retain h x)) ≡ x
  input-recovered h x = refl

Stack3 : (ℓ ℓP : Level) → Type (ℓ-max (ℓ-suc ℓ) (ℓ-suc ℓP))
Stack3 ℓ ℓP = Σ[ L ∈ Layer1 ℓ ] Σ[ K ∈ Layer2 L ] Layer3 L K ℓP

extend3 : {ℓ ℓP : Level} {L : Layer1 ℓ} {K : Layer2 L} → Layer3 L K ℓP → Stack3 ℓ ℓP
extend3 {L = L} {K = K} T = L , K , T

layers-recovered : {ℓ ℓP : Level} {L : Layer1 ℓ} {K : Layer2 L} (T : Layer3 L K ℓP)
  → Path (Stack ℓ) (fst (extend3 T) , fst (snd (extend3 T))) (L , K)
layers-recovered T = refl

-- Path specialization: arbitrary dependent fibers, with no set truncation.
module PathTransport {ℓ ℓP : Level} (S : Type ℓ)
  (G : (s : S) → Σ[ t ∈ S ] (s ≡ t))
  (K : Layer2 (path-layer S G)) (F : S → Type ℓP) where
  L : Layer1 ℓ
  L = path-layer S G
  module H = Histories L
  module Fold = Interpret L (path-composition S G)

  transport-layer : Layer3 L K ℓP
  transport-layer = record { Payload = F ; move = λ p x → subst F p x }
  open Layer3 transport-layer using (walk; execute)

  fold-agreement : {s t : S} (h : H.History s t) (x : F s)
    → subst F (Fold.fold h) x ≡ walk h x
  fold-agreement {s} H.empty x = substRefl {B = F} {x = s} x
  fold-agreement (H.link p h) x = substComposite F p (Fold.fold h) x
    ∙ fold-agreement h (subst F p x)

  composite : {s t : S} → Layer2.HistoryType K s t → s ≡ t
  composite h = Fold.fold (Layer2.decode K h)

  agreement : {s t : S} (h : Layer2.HistoryType K s t) (x : F s)
    → subst F (composite h) x ≡ execute h x
  agreement h x = fold-agreement (Layer2.decode K h) x

  -- Higher compatibility: transporting a history comparison commutes with
  -- the agreement witness. Applies to Layer 2 unit and associativity paths.
  agreement-natural : {s t : S} {h k : Layer2.HistoryType K s t}
    (e : h ≡ k) (x : F s)
    → agreement h x ∙ cong (λ z → execute z x) e
      ≡ cong (λ z → subst F (composite z) x) e ∙ agreement k x
  agreement-natural {h = h} e x = J
    (λ k e → agreement h x ∙ cong (λ z → execute z x) e
      ≡ cong (λ z → subst F (composite z) x) e ∙ agreement k x)
    (sym (rUnit (agreement h x)) ∙ lUnit (agreement h x)) e

  -- Correctness against independent composite-path semantics, centered on
  -- the history executor's result. Works for higher-valued fibers too.
  CorrectOutput : {s t : S} (h : Layer2.HistoryType K s t) (x : F s) → Type ℓP
  CorrectOutput {t = t} h x = Σ[ y ∈ F t ] (subst F (composite h) x ≡ y)

  semantic-certificate : {s t : S} (h : Layer2.HistoryType K s t) (x : F s)
    → isContr (CorrectOutput h x)
  semantic-certificate h x = chosen , λ y → sym (snd singleton chosen) ∙ snd singleton y
    where
    chosen : CorrectOutput h x
    chosen = execute h x , agreement h x
    singleton : isContr (CorrectOutput h x)
    singleton = (subst F (composite h) x , refl) , λ { (y , p) i → p i , (λ j → p (i ∧ j)) }

-- Integration with the previously checked object-language machine.
module MachineBridge where
  S : Type
  S = Index C.F
  G : (s : S) → Σ[ t ∈ S ] (s ≡ t)
  G s = s , refl
  L : Layer1 ℓ-zero
  L = path-layer S G
  K : Layer2 L
  K = layer2 L
  module P = PathTransport S G K (Fibre C.F)
  module H = Histories L
  open Layer3 P.transport-layer using (walk; walk-join)

  -- The benchmark supplies histories with loop edges. G above is the default
  -- identity generator; these histories are not claimed to arise by iterating G.
  history : M.Route ⊥ → H.History C.base-index C.base-index
  history (M.slot ())
  history M.stay = H.empty
  history M.turn = H.single C.index-loop
  history (M.follow p q) = H.join (history p) (history q)

  route-agreement : (p : M.Route ⊥) (b : Bool) → walk (history p) b ≡ M.run-route p b
  route-agreement (M.slot ()) b
  route-agreement M.stay b = refl
  route-agreement M.turn b = M.turn-sound b
  route-agreement (M.follow p q) b = walk-join (history p) (history q) b
    ∙ cong (walk (history q)) (route-agreement p b)
    ∙ route-agreement q (M.run-route p b)

  compile : M.Term ⊥ → Bool × H.History C.base-index C.base-index
  compile (M.bit b) = b , H.empty
  compile (M.carry p t) with compile t
  ... | b , h = b , H.join h (history p)

  compiler-agreement : (t : M.Term ⊥) → walk (snd (compile t)) (fst (compile t)) ≡ M.run t
  compiler-agreement (M.bit b) = refl
  compiler-agreement (M.carry p t) with compile t | compiler-agreement t
  ... | b , h | ih = walk-join h (history p) b
    ∙ cong (walk (history p)) ih ∙ route-agreement p (M.run t)

  run-compiled : M.Term ⊥ → Bool
  run-compiled t = walk (snd (compile t)) (fst (compile t))

  step-preserved : {t u : M.Term ⊥} → M.Step t u → run-compiled t ≡ run-compiled u
  step-preserved {t} {u} step = compiler-agreement t ∙ sym (M.run-sound t)
    ∙ M.step-sound step M.empty-env ∙ M.run-sound u ∙ sym (compiler-agreement u)

  one-turn : walk (history M.turn) true ≡ false
  one-turn = route-agreement M.turn true

  two-turns : (b : Bool) → walk (history (M.follow M.turn M.turn)) b ≡ b
  two-turns b = route-agreement (M.follow M.turn M.turn) b ∙ M.twice-restores b

  no-endpoint-only-action : (f : Bool → Bool)
    → ((p : M.Route ⊥) (b : Bool) → f b ≡ walk (history p) b) → ⊥
  no-endpoint-only-action f law = M.no-endpoint-only-action f
    (λ p b → law p b ∙ route-agreement p b)

  is-empty : {s t : S} → H.History s t → Bool
  is-empty H.empty = true
  is-empty (H.link w h) = false

  two-histories-distinct : history M.stay ≡ history (M.follow M.turn M.turn) → ⊥
  two-histories-distinct e = true≢false (cong is-empty e)

  no-output-history-decoder : (decode : Bool → H.History C.base-index C.base-index)
    → ((p : M.Route ⊥) → decode (walk (history p) true) ≡ history p) → ⊥
  no-output-history-decoder decode recover = two-histories-distinct
    (sym (recover M.stay) ∙ cong decode (sym (two-turns true)) ∙ recover (M.follow M.turn M.turn))

  no-action-history-decoder : (decode : (Bool → Bool) → H.History C.base-index C.base-index)
    → ((p : M.Route ⊥) → decode (walk (history p)) ≡ history p) → ⊥
  no-action-history-decoder decode recover = two-histories-distinct
    (sym (recover M.stay) ∙ cong decode (sym (funExt two-turns)) ∙ recover (M.follow M.turn M.turn))

  -- Transport takes an initial value; it does not supply values globally.
  no-total-payloads : ((s : S) → Fibre C.F s) → ⊥
  no-total-payloads = C.no-section

  -- Compilation flattens syntax. Its retained result keeps the original term.
  Compilation : Type
  Compilation = Σ[ t ∈ M.Term ⊥ ] Σ[ bh ∈ Bool × H.History C.base-index C.base-index ]
    (walk (snd bh) (fst bh) ≡ M.run t)

  retain-compilation : M.Term ⊥ → Compilation
  retain-compilation t = t , compile t , compiler-agreement t

  program-recovered : (t : M.Term ⊥) → fst (retain-compilation t) ≡ t
  program-recovered t = refl
