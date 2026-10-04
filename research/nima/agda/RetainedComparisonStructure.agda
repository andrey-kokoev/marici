{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedComparisonStructure where

open import Cubical.Foundations.Prelude hiding (transport)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Sigma.Base using (_×_; fst; snd)
open import Cubical.Data.Empty.Base using (⊥)

-- The candidate table, with its law witnesses retained as fields.
-- No truncation or faithfulness of realization is assumed.
record Structure (ℓ : Level) : Type (ℓ-suc ℓ) where
  field
    P : Type ℓ
    K E : P → P → Type ℓ
    idK : {p : P} → K p p
    compK : {p q r : P} → K q r → K p q → K p r
    unitLK : {p q : P} (a : K p q) → compK idK a ≡ a
    unitRK : {p q : P} (a : K p q) → compK a idK ≡ a
    assocK : {p q r s : P} (c : K r s) (b : K q r) (a : K p q)
      → compK c (compK b a) ≡ compK (compK c b) a
    idE : {p : P} → E p p
    compE : {p q r : P} → E q r → E p q → E p r
    invE : {p q : P} → E p q → E q p
    unitLE : {p q : P} (e : E p q) → compE idE e ≡ e
    unitRE : {p q : P} (e : E p q) → compE e idE ≡ e
    assocE : {p q r s : P} (h : E r s) (d : E q r) (e : E p q)
      → compE h (compE d e) ≡ compE (compE h d) e
    inverseLE : {p q : P} (e : E p q) → compE (invE e) e ≡ idE
    inverseRE : {p q : P} (e : E p q) → compE e (invE e) ≡ idE
    realize : {p q : P} → E p q → K p q
    realize-id : {p : P} → realize (idE {p}) ≡ idK
    realize-comp : {p q r : P} (d : E q r) (e : E p q)
      → realize (compE d e) ≡ compK (realize d) (realize e)

  -- Transport is derived, not an additional field.
  transport : {p p' q q' : P} → E p p' → E q q' → K p q → K p' q'
  transport e d a = compK (compK (realize d) a) (realize (invE e))

  realized-inverseL : {p q : P} (e : E p q)
    → compK (realize (invE e)) (realize e) ≡ idK
  realized-inverseL e = sym (realize-comp (invE e) e)
    ∙ cong realize (inverseLE e) ∙ realize-id

  realized-inverseR : {p q : P} (e : E p q)
    → compK (realize e) (realize (invE e)) ≡ idK
  realized-inverseR e = sym (realize-comp e (invE e))
    ∙ cong realize (inverseRE e) ∙ realize-id

-- An explicit inhabitant: two objects, two comparisons per ordered pair,
-- four retained changes per ordered pair. Composition is XOR.
xor : Bool → Bool → Bool
xor false b = b
xor true false = true
xor true true = false

xor-unitR : (a : Bool) → xor a false ≡ a
xor-unitR false = refl
xor-unitR true = refl

xor-assoc : (c b a : Bool) → xor c (xor b a) ≡ xor (xor c b) a
xor-assoc false b a = refl
xor-assoc true false a = refl
xor-assoc true true false = refl
xor-assoc true true true = refl

xor-self : (a : Bool) → xor a a ≡ false
xor-self false = refl
xor-self true = refl

pairXor : Bool × Bool → Bool × Bool → Bool × Bool
pairXor (b , h) (a , k) = xor b a , xor h k

example : Structure ℓ-zero
example = record
  { P = Bool
  ; K = λ _ _ → Bool
  ; E = λ _ _ → Bool × Bool
  ; idK = false
  ; compK = xor
  ; unitLK = λ a → refl
  ; unitRK = xor-unitR
  ; assocK = xor-assoc
  ; idE = false , false
  ; compE = pairXor
  ; invE = λ e → e
  ; unitLE = λ e → refl
  ; unitRE = λ e i → xor-unitR (fst e) i , xor-unitR (snd e) i
  ; assocE = λ h d e i → xor-assoc (fst h) (fst d) (fst e) i , xor-assoc (snd h) (snd d) (snd e) i
  ; inverseLE = λ e i → xor-self (fst e) i , xor-self (snd e) i
  ; inverseRE = λ e i → xor-self (fst e) i , xor-self (snd e) i
  ; realize = fst
  ; realize-id = refl
  ; realize-comp = λ d e → refl
  }

module Example = Structure example

-- Distinct retained changes with identical realized comparison.
change0 change1 : Example.E false true
change0 = false , false
change1 = false , true

changes-distinct : change0 ≡ change1 → ⊥
changes-distinct p = false≢true (cong snd p)

same-realization : Example.realize {false} {true} change0 ≡ Example.realize {false} {true} change1
same-realization = refl

-- No decoder from comparisons can recover every retained change.
no-recovery : (recover : Example.K false true → Example.E false true)
  → ((e : Example.E false true) → recover (Example.realize {false} {true} e) ≡ e)
  → ⊥
no-recovery recover law = changes-distinct (sym (law change0) ∙ law change1)

-- Neither the object carrier nor the comparison carrier is trivial.
objects-distinct : (false ≡ true) → ⊥
objects-distinct = false≢true

comparisons-distinct : (false ≡ true) → ⊥
comparisons-distinct = false≢true

-- The hidden change remains available, although induced transport cannot see it.
same-transport : (d : Example.E false true) (a : Example.K false false)
  → Example.transport {false} {true} {false} {true} change0 d a
    ≡ Example.transport {false} {true} {false} {true} change1 d a
same-transport d a = refl
