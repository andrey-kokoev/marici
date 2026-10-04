{-# OPTIONS --safe --cubical --guardedness #-}
module TypedGeneratorLayers where

open import Cubical.Foundations.Prelude hiding (empty)
open import Cubical.Foundations.Equiv using (_≃_; idEquiv; equivFun; invEq; secEq; retEq)
open import Cubical.Foundations.GroupoidLaws using (lUnit; rUnit; assoc)
open import Cubical.Foundations.HLevels using (isPropIsContr)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Bool.Base using (Bool; true; false; not)
open import Cubical.Data.Bool.Properties using (false≢true; true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import MarkedTetrahedronCoherence using (module Tetrahedra)

record Layer1 (ℓ : Level) : Type (ℓ-suc ℓ) where
  field
    State : Type ℓ
    Witness : State → State → Type ℓ
    generate : (s : State) → Σ[ t ∈ State ] Witness s t
  next : State → State
  next s = fst (generate s)
  edge : (s : State) → Witness s (next s)
  edge s = snd (generate s)

module Histories {ℓ : Level} (L : Layer1 ℓ) where
  open Layer1 L

  -- Free finite histories retain intermediate states and original witnesses.
  data History (s : State) : State → Type ℓ where
    empty : History s s
    link : {t u : State} → Witness s t → History t u → History s u

  single : {s t : State} → Witness s t → History s t
  single w = link w empty

  join : {s t u : State} → History s t → History t u → History s u
  join empty k = k
  join (link w h) k = link w (join h k)

  left-unit : {s t : State} (h : History s t) → join empty h ≡ h
  left-unit h = refl

  right-unit : {s t : State} (h : History s t) → join h empty ≡ h
  right-unit empty = refl
  right-unit (link w h) = cong (link w) (right-unit h)

  associative : {s t u v : State} (h : History s t) (k : History t u) (m : History u v)
    → join (join h k) m ≡ join h (join k m)
  associative empty k m = refl
  associative (link w h) k m = cong (link w) (associative h k m)

  length : {s t : State} → History s t → ℕ
  length empty = zero
  length (link w h) = suc (length h)

  at : ℕ → State → State
  at zero s = s
  at (suc n) s = at n (next s)

  generated : (n : ℕ) (s : State) → History s (at n s)
  generated zero s = empty
  generated (suc n) s = link (edge s) (generated n (next s))

  generated-length : (n : ℕ) (s : State) → length (generated n s) ≡ n
  generated-length zero s = refl
  generated-length (suc n) s = cong suc (generated-length n (next s))

-- A Layer 2 representation must retain exactly the free history data.
-- Operations are transported from History, rather than independently chosen.
record Layer2 {ℓ : Level} (L : Layer1 ℓ) : Type (ℓ-suc ℓ) where
  open Layer1 L
  module H = Histories L
  field
    HistoryType : State → State → Type ℓ
    representation : (s t : State) → HistoryType s t ≃ H.History s t

  decode : {s t : State} → HistoryType s t → H.History s t
  decode {s} {t} = equivFun (representation s t)

  encode : {s t : State} → H.History s t → HistoryType s t
  encode {s} {t} = invEq (representation s t)

  decode-encode : {s t : State} (h : H.History s t) → decode (encode h) ≡ h
  decode-encode {s} {t} = secEq (representation s t)

  encode-decode : {s t : State} (h : HistoryType s t) → encode (decode h) ≡ h
  encode-decode {s} {t} = retEq (representation s t)

  identity : (s : State) → HistoryType s s
  identity s = encode H.empty

  single : {s t : State} → Witness s t → HistoryType s t
  single w = encode (H.single w)

  generated : (n : ℕ) (s : State) → HistoryType s (H.at n s)
  generated n s = encode (H.generated n s)

  compose : {s t u : State} → HistoryType s t → HistoryType t u → HistoryType s u
  compose h k = encode (H.join (decode h) (decode k))

  composition-preserved : {s t u : State} (h : HistoryType s t) (k : HistoryType t u)
    → decode (compose h k) ≡ H.join (decode h) (decode k)
  composition-preserved h k = decode-encode (H.join (decode h) (decode k))

  decode-injective : {s t : State} {h k : HistoryType s t} → decode h ≡ decode k → h ≡ k
  decode-injective {h = h} {k = k} p = sym (encode-decode h) ∙ cong encode p ∙ encode-decode k

  left-unit : {s t : State} (h : HistoryType s t) → compose (identity s) h ≡ h
  left-unit {s} h = decode-injective
    (composition-preserved (identity s) h
    ∙ cong (λ x → H.join x (decode h)) (decode-encode H.empty)
    ∙ H.left-unit (decode h))

  right-unit : {s t : State} (h : HistoryType s t) → compose h (identity t) ≡ h
  right-unit {t = t} h = decode-injective
    (composition-preserved h (identity t)
    ∙ cong (H.join (decode h)) (decode-encode H.empty)
    ∙ H.right-unit (decode h))

  associative : {s t u v : State} (h : HistoryType s t) (k : HistoryType t u) (m : HistoryType u v)
    → compose (compose h k) m ≡ compose h (compose k m)
  associative h k m = decode-injective
    (composition-preserved (compose h k) m
    ∙ cong (λ x → H.join x (decode m)) (composition-preserved h k)
    ∙ H.associative (decode h) (decode k) (decode m)
    ∙ sym (cong (H.join (decode h)) (composition-preserved k m))
    ∙ sym (composition-preserved h (compose k m)))

layer2 : {ℓ : Level} (L : Layer1 ℓ) → Layer2 L
layer2 L = record { HistoryType = Histories.History L ; representation = λ s t → idEquiv _ }

Stack : (ℓ : Level) → Type (ℓ-suc ℓ)
Stack ℓ = Σ[ L ∈ Layer1 ℓ ] Layer2 L

extend : {ℓ : Level} → Layer1 ℓ → Stack ℓ
extend L = L , layer2 L

layer1-recovered : {ℓ : Level} (L : Layer1 ℓ) → fst (extend L) ≡ L
layer1-recovered L = refl

-- Collapsing a history into the ORIGINAL witness relation is optional data.
record Composition {ℓ : Level} (L : Layer1 ℓ) : Type ℓ where
  open Layer1 L
  field
    identity : (s : State) → Witness s s
    compose : {s t u : State} → Witness s t → Witness t u → Witness s u
    unit-left : {s t : State} (p : Witness s t) → compose (identity s) p ≡ p
    unit-right : {s t : State} (p : Witness s t) → compose p (identity t) ≡ p
    reassociate : {s t u v : State} (p : Witness s t) (q : Witness t u) (r : Witness u v)
      → compose (compose p q) r ≡ compose p (compose q r)

module Interpret {ℓ : Level} (L : Layer1 ℓ) (C : Composition L) where
  open Layer1 L
  open Composition C
  open Histories L

  fold : {s t : State} → History s t → Witness s t
  fold {s} empty = identity s
  fold (link w h) = compose w (fold h)

  fold-join : {s t u : State} (h : History s t) (k : History t u)
    → fold (join h k) ≡ compose (fold h) (fold k)
  fold-join empty k = sym (unit-left (fold k))
  fold-join (link w h) k = cong (compose w) (fold-join h k)
    ∙ sym (reassociate w (fold h) (fold k))

  fold-single : {s t : State} (w : Witness s t) → fold (single w) ≡ w
  fold-single w = unit-right w

path-layer : {ℓ : Level} (S : Type ℓ) (G : (s : S) → Σ[ t ∈ S ] (s ≡ t)) → Layer1 ℓ
path-layer S G = record { State = S ; Witness = _≡_ ; generate = G }

path-composition : {ℓ : Level} (S : Type ℓ) (G : (s : S) → Σ[ t ∈ S ] (s ≡ t))
  → Composition (path-layer S G)
path-composition S G = record
  { identity = λ s → refl ; compose = _∙_
  ; unit-left = λ p → sym (lUnit p) ; unit-right = λ p → sym (rUnit p)
  ; reassociate = λ p q r → sym (assoc p q r) }

module GeneratedPaths {ℓ : Level} (S : Type ℓ) (G : (s : S) → Σ[ t ∈ S ] (s ≡ t)) where
  L : Layer1 ℓ
  L = path-layer S G
  open Layer1 L
  module T = Tetrahedra S

  -- Three generated edges; all six endpoint marks remain explicit.
  edges : (s : S) → T.Edges s (next s) (next (next s)) (next (next (next s)))
  edges s = record
    { e01 = edge s ; e12 = edge (next s) ; e23 = edge (next (next s))
    ; e02 = edge s ∙ edge (next s)
    ; e13 = edge (next s) ∙ edge (next (next s))
    ; e03 = (edge s ∙ edge (next s)) ∙ edge (next (next s)) }

  module At (s : S) where
    module O = T.Over (edges s)
    face012 : O.Face012
    face012 = refl
    face123 : O.Face123
    face123 = refl
    face023 : O.Face023
    face023 = refl

    -- Recover the fourth face WITH its tetrahedral comparison, keeping
    -- the six edges and the three supplied faces fixed.
    certificate : isContr (O.Missing013 face012 face123 face023)
    certificate = O.unique013 face012 face123 face023

    face013 : O.Face013
    face013 = fst (fst certificate)

    tetrahedron : O.Tetrahedron face012 face123 face013 face023
    tetrahedron = snd (fst certificate)

    higher-certificate : isContr (isContr (O.Missing013 face012 face123 face023))
    higher-certificate = certificate , isPropIsContr certificate

  -- Naturality of the generated path under a supplied comparison.
  naturality : {a b : S} (p : a ≡ b) → p ∙ edge b ≡ edge a ∙ cong next p
  naturality {a} = J (λ b p → p ∙ edge b ≡ edge a ∙ cong next p)
    (sym (lUnit (edge a)) ∙ rUnit (edge a))

-- A valid Layer 1 with a relation that does not admit composition.
flip-layer : Layer1 ℓ-zero
flip-layer = record
  { State = Bool ; Witness = λ s t → t ≡ not s
  ; generate = λ s → not s , refl }

no-flip-composition :
  ({s t u : Bool} → (t ≡ not s) → (u ≡ not t) → (u ≡ not s)) → ⊥
no-flip-composition compose = false≢true (compose {s = false} {t = true} {u = false} refl refl)

no-universal-composition : ((L : Layer1 ℓ-zero) → Composition L) → ⊥
no-universal-composition build = no-flip-composition (Composition.compose (build flip-layer))

flip-history : Histories.History flip-layer false false
flip-history = Histories.generated flip-layer 2 false

-- Retaining a composite alone loses the number of steps even for paths.
id-layer : Layer1 ℓ-zero
id-layer = path-layer Bool (λ b → b , refl)
module IH = Histories id-layer
module IF = Interpret id-layer (path-composition Bool (λ b → b , refl))

is-empty : {s t : Bool} → IH.History s t → Bool
is-empty IH.empty = true
is-empty (IH.link w h) = false

no-history-decoder : (decode : (false ≡ false) → IH.History false false)
  → ((h : IH.History false false) → decode (IF.fold h) ≡ h) → ⊥
no-history-decoder decode recover = true≢false (cong is-empty
  (sym (recover IH.empty) ∙ cong decode (rUnit refl) ∙ recover (IH.single refl)))
