{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureDecoratedPathCore where

open import Cubical.Foundations.Prelude using (Type; _≡_; refl; cong; cong₂; sym; _∙_)
open import Agda.Builtin.Nat using (Nat; zero; suc; _+_)
open import Agda.Builtin.List using (List; []; _∷_)
open import Agda.Builtin.Sigma using (Σ; _,_; fst; snd)

data Mark : Type where
  forgotten retained : Mark

data Unit : Type where
  empty : Unit

data Void : Type where

data Position (A : Type) : Type where
  start : Position A
  next : A → Position A

module Source (Vertex : Type) (Edge : Vertex → Vertex → Type) where
  infixr 5 _▷_
  data Path : Vertex → Vertex → Type where
    identity : {a : Vertex} → Path a a
    _▷_ : {a b c : Vertex} → Edge a b → Path b c → Path a c

  -- Recursive families avoid forced constructor-injectivity matches.
  Decoration : {a b : Vertex} → Path a b → Type
  Decoration identity = Unit
  Decoration (e ▷ w) = Σ Mark (λ _ → Decoration w)

  allRetained : {a b : Vertex} (w : Path a b) → Decoration w
  allRetained identity = empty
  allRetained (e ▷ w) = retained , allRetained w

  Survives : {a b : Vertex} (w : Path a b) → Decoration w → Type
  Survives identity empty = Unit
  Survives (e ▷ w) (forgotten , m) = Void
  Survives (e ▷ w) (retained , m) = Survives w m

  all-survives : {a b : Vertex} (w : Path a b) → Survives w (allRetained w)
  all-survives identity = empty
  all-survives (e ▷ w) = all-survives w

  unique-survivor : {a b : Vertex} (w : Path a b) (m : Decoration w) →
    Survives w m → m ≡ allRetained w
  unique-survivor identity empty p = refl
  unique-survivor (e ▷ w) (forgotten , m) ()
  unique-survivor (e ▷ w) (retained , m) p =
    cong (retained ,_) (unique-survivor w m p)

  append : {A : Type} → List A → List A → List A
  append [] ys = ys
  append (x ∷ xs) ys = x ∷ append xs ys

  prefix : {A : Type} → Mark → List A → List (Σ Mark (λ _ → A))
  prefix k [] = []
  prefix k (m ∷ ms) = (k , m) ∷ prefix k ms

  lift : {a b : Vertex} (w : Path a b) → List (Decoration w)
  lift identity = empty ∷ []
  lift (e ▷ w) = append (prefix forgotten (lift w)) (prefix retained (lift w))

  weight : {a b : Vertex} (w : Path a b) → Decoration w → Nat
  weight identity empty = suc zero
  weight (e ▷ w) (forgotten , m) = zero
  weight (e ▷ w) (retained , m) = weight w m

  mass : {a b : Vertex} (w : Path a b) → List (Decoration w) → Nat
  mass w [] = zero
  mass w (m ∷ ms) = weight w m + mass w ms

  plus-assoc : (a b c : Nat) → (a + b) + c ≡ a + (b + c)
  plus-assoc zero b c = refl
  plus-assoc (suc a) b c = cong suc (plus-assoc a b c)

  mass-append : {a b : Vertex} (w : Path a b) (xs ys : List (Decoration w)) →
    mass w (append xs ys) ≡ mass w xs + mass w ys
  mass-append w [] ys = refl
  mass-append w (x ∷ xs) ys = cong (weight w x +_) (mass-append w xs ys)
    ∙ sym (plus-assoc (weight w x) (mass w xs) (mass w ys))

  mass-forgotten : {a b c : Vertex} (e : Edge a b) (w : Path b c)
    (ms : List (Decoration w)) → mass (e ▷ w) (prefix forgotten ms) ≡ zero
  mass-forgotten e w [] = refl
  mass-forgotten e w (m ∷ ms) = mass-forgotten e w ms

  mass-retained : {a b c : Vertex} (e : Edge a b) (w : Path b c)
    (ms : List (Decoration w)) → mass (e ▷ w) (prefix retained ms) ≡ mass w ms
  mass-retained e w [] = refl
  mass-retained e w (m ∷ ms) = cong (weight w m +_) (mass-retained e w ms)

  split-lift-coefficient : {a b : Vertex} (w : Path a b) → mass w (lift w) ≡ suc zero
  split-lift-coefficient identity = refl
  split-lift-coefficient (e ▷ w) =
    mass-append (e ▷ w) (prefix forgotten (lift w)) (prefix retained (lift w))
    ∙ cong₂ _+_ (mass-forgotten e w (lift w)) (mass-retained e w (lift w))
    ∙ split-lift-coefficient w

  Cut : {a b : Vertex} → Path a b → Type
  Cut identity = Unit
  Cut (e ▷ w) = Position (Cut w)

  vertex : {a b : Vertex} (w : Path a b) → Cut w → Vertex
  vertex {a = a} identity empty = a
  vertex {a = a} (e ▷ w) start = a
  vertex (e ▷ w) (next c) = vertex w c

  before : {a b : Vertex} (w : Path a b) (c : Cut w) → Path a (vertex w c)
  before identity empty = identity
  before (e ▷ w) start = identity
  before (e ▷ w) (next c) = e ▷ before w c

  after : {a b : Vertex} (w : Path a b) (c : Cut w) → Path (vertex w c) b
  after identity empty = identity
  after (e ▷ w) start = e ▷ w
  after (e ▷ w) (next c) = after w c

  Pieces : {a b : Vertex} (w : Path a b) → Cut w → Type
  Pieces w c = Σ (Decoration (before w c)) (λ _ → Decoration (after w c))

  split : {a b : Vertex} (w : Path a b) (c : Cut w) → Decoration w → Pieces w c
  split identity empty empty = empty , empty
  split (e ▷ w) start m = empty , m
  split (e ▷ w) (next c) (k , m) = (k , fst (split w c m)) , snd (split w c m)

  join : {a b : Vertex} (w : Path a b) (c : Cut w) → Pieces w c → Decoration w
  join identity empty (empty , empty) = empty
  join (e ▷ w) start (empty , m) = m
  join (e ▷ w) (next c) ((k , l) , r) = k , join w c (l , r)

  join-split : {a b : Vertex} (w : Path a b) (c : Cut w) (m : Decoration w) →
    join w c (split w c m) ≡ m
  join-split identity empty empty = refl
  join-split (e ▷ w) start m = refl
  join-split (e ▷ w) (next c) (k , m) = cong (k ,_) (join-split w c m)

  split-join : {a b : Vertex} (w : Path a b) (c : Cut w) (p : Pieces w c) →
    split w c (join w c p) ≡ p
  split-join identity empty (empty , empty) = refl
  split-join (e ▷ w) start (empty , m) = refl
  split-join (e ▷ w) (next c) ((k , l) , r) =
    cong (λ p → (k , fst p) , snd p) (split-join w c (l , r))

  compose : {a b c : Vertex} → Path a b → Path b c → Path a c
  compose identity q = q
  compose (e ▷ p) q = e ▷ compose p q

  composeMarks : {a b c : Vertex} (p : Path a b) (q : Path b c) →
    Decoration p → Decoration q → Decoration (compose p q)
  composeMarks identity q empty n = n
  composeMarks (e ▷ p) q (k , m) n = k , composeMarks p q m n

  compose-retained : {a b c : Vertex} (p : Path a b) (q : Path b c) →
    composeMarks p q (allRetained p) (allRetained q) ≡ allRetained (compose p q)
  compose-retained identity q = refl
  compose-retained (e ▷ p) q = cong (retained ,_) (compose-retained p q)

  -- Dependent associativity: the marks move along the actual path equality.
  compose-assoc : {a b c d : Vertex} (p : Path a b) (q : Path b c) (r : Path c d) →
    compose (compose p q) r ≡ compose p (compose q r)
  compose-assoc identity q r = refl
  compose-assoc (e ▷ p) q r = cong (e ▷_) (compose-assoc p q r)
