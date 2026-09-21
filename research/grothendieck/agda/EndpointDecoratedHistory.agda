{-# OPTIONS --safe --cubical --guardedness #-}
module EndpointDecoratedHistory where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Base
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)

-- Arbitrary typed source graph. No endpoint quotient is imposed.
module Typed {ℓ : Level} (V : Type ℓ) (E : V → V → Type ℓ) where
  data Route : V → V → Type ℓ where
    nil : {x : V} → Route x x
    step : {x y z : V} → E x y → Route y z → Route x z

  append : {x y z : V} → Route x y → Route y z → Route x z
  append nil q = q
  append (step e p) q = step e (append p q)

  append-unit : {x y : V} (p : Route x y) → append p nil ≡ p
  append-unit nil = refl
  append-unit (step e p) = cong (step e) (append-unit p)

  append-assoc : {w x y z : V} (p : Route w x) (q : Route x y) (r : Route y z) →
    append (append p q) r ≡ append p (append q r)
  append-assoc nil q r = refl
  append-assoc (step e p) q r = cong (step e) (append-assoc p q r)

  data Marks : {x y : V} → Route x y → Type ℓ where
    no-marks : {x : V} → Marks (nil {x})
    mark : {x y z : V} {e : E x y} {p : Route y z} →
      Bool → Marks p → Marks (step e p)

  keep : {x y : V} (p : Route x y) → Marks p
  keep nil = no-marks
  keep (step e p) = mark true (keep p)

  Decorated : V → V → Type ℓ
  Decorated x y = Σ (Route x y) Marks

  lift-kept : {x y : V} → Route x y → Decorated x y
  lift-kept p = p , keep p

  erase : {x y : V} → Decorated x y → Route x y
  erase = fst

  erase-kept : {x y : V} (p : Route x y) → erase (lift-kept p) ≡ p
  erase-kept p = refl

  -- The additive lift is the family indexed by ALL Marks p.
  -- Exactly one family member survives the all-retained extraction.
  AllKept : {x y : V} {p : Route x y} → Marks p → Type
  AllKept no-marks = Unit
  AllKept (mark false m) = ⊥
  AllKept (mark true m) = AllKept m

  keep-proof : {x y : V} (p : Route x y) → AllKept (keep p)
  keep-proof nil = tt
  keep-proof (step e p) = keep-proof p

  unique-kept : {x y : V} {p : Route x y}
    (m : Marks p) (a : AllKept m) →
    (m , a) ≡ (keep p , keep-proof p)
  unique-kept no-marks tt = refl
  unique-kept (mark false m) ()
  unique-kept (mark true m) a =
    cong (λ z → mark true (fst z) , snd z) (unique-kept m a)

  kept-fiber-contractible : {x y : V} (p : Route x y) →
    isContr (Σ (Marks p) AllKept)
  kept-fiber-contractible p =
    (keep p , keep-proof p) , λ z → sym (unique-kept (fst z) (snd z))

  append-marks : {x y z : V} {p : Route x y} {q : Route y z} →
    Marks p → Marks q → Marks (append p q)
  append-marks no-marks n = n
  append-marks (mark b m) n = mark b (append-marks m n)

  keep-append : {x y z : V} (p : Route x y) (q : Route y z) →
    keep (append p q) ≡ append-marks (keep p) (keep q)
  keep-append nil q = refl
  keep-append (step e p) q = cong (mark true) (keep-append p q)

  split-append : {x y z : V} (p : Route x y) (q : Route y z) →
    Marks (append p q) → Marks p × Marks q
  split-append nil q m = no-marks , m
  split-append (step e p) q (mark b m) =
    mark b (fst (split-append p q m)) , snd (split-append p q m)

  append-split : {x y z : V} (p : Route x y) (q : Route y z)
    (m : Marks (append p q)) →
    append-marks (fst (split-append p q m)) (snd (split-append p q m)) ≡ m
  append-split nil q m = refl
  append-split (step e p) q (mark b m) = cong (mark b) (append-split p q m)

  split-appended : {x y z : V} {p : Route x y} {q : Route y z}
    (m : Marks p) (n : Marks q) →
    split-append p q (append-marks m n) ≡ (m , n)
  split-appended no-marks n = refl
  split-appended (mark b m) n =
    cong (λ z → mark b (fst z) , snd z) (split-appended m n)

  composition-mark-iso : {x y z : V} (p : Route x y) (q : Route y z) →
    Iso (Marks (append p q)) (Marks p × Marks q)
  Iso.fun (composition-mark-iso p q) = split-append p q
  Iso.inv (composition-mark-iso p q) mn = append-marks (fst mn) (snd mn)
  Iso.rightInv (composition-mark-iso p q) mn = split-appended (fst mn) (snd mn)
  Iso.leftInv (composition-mark-iso p q) = append-split p q

  data Cut : {x y : V} → Route x y → Type ℓ where
    first : {x y : V} {p : Route x y} → Cut p
    next : {x y z : V} {e : E x y} {p : Route y z} → Cut p → Cut (step e p)

  middle : {x y : V} {p : Route x y} → Cut p → V
  middle {x = x} first = x
  middle (next c) = middle c

  prefix : {x y : V} {p : Route x y} (c : Cut p) → Route x (middle c)
  prefix first = nil
  prefix {p = step e p} (next c) = step e (prefix c)

  suffix : {x y : V} {p : Route x y} (c : Cut p) → Route (middle c) y
  suffix {p = p} first = p
  suffix (next c) = suffix c

  rejoin : {x y : V} {p : Route x y} (c : Cut p) →
    append (prefix c) (suffix c) ≡ p
  rejoin first = refl
  rejoin {p = step e p} (next c) = cong (step e) (rejoin c)

  split : {x y : V} {p : Route x y} (c : Cut p) →
    Marks p → Marks (prefix c) × Marks (suffix c)
  split first m = no-marks , m
  split (next c) (mark b m) = mark b (fst (split c m)) , snd (split c m)

  merge : {x y : V} {p : Route x y} (c : Cut p) →
    Marks (prefix c) × Marks (suffix c) → Marks p
  merge first (no-marks , n) = n
  merge (next c) (mark b m , n) = mark b (merge c (m , n))

  merge-split : {x y : V} {p : Route x y} (c : Cut p) (m : Marks p) →
    merge c (split c m) ≡ m
  merge-split first m = refl
  merge-split (next c) (mark b m) = cong (mark b) (merge-split c m)

  split-merge : {x y : V} {p : Route x y} (c : Cut p)
    (mn : Marks (prefix c) × Marks (suffix c)) → split c (merge c mn) ≡ mn
  split-merge first (no-marks , n) = refl
  split-merge (next c) (mark b m , n) =
    cong (λ z → mark b (fst z) , snd z) (split-merge c (m , n))

  cut-mark-iso : {x y : V} {p : Route x y} (c : Cut p) →
    Iso (Marks p) (Marks (prefix c) × Marks (suffix c))
  Iso.fun (cut-mark-iso c) = split c
  Iso.inv (cut-mark-iso c) = merge c
  Iso.rightInv (cut-mark-iso c) = split-merge c
  Iso.leftInv (cut-mark-iso c) = merge-split c

  -- Bijection of the summand indices of Delta L and (L tensor L) Delta.
  full-cut-iso : {x y : V} (p : Route x y) →
    Iso (Σ (Cut p) (λ _ → Marks p))
        (Σ (Cut p) (λ c → Marks (prefix c) × Marks (suffix c)))
  Iso.fun (full-cut-iso p) (c , m) = c , split c m
  Iso.inv (full-cut-iso p) (c , mn) = c , merge c mn
  Iso.rightInv (full-cut-iso p) (c , mn) =
    cong (λ z → c , z) (split-merge c mn)
  Iso.leftInv (full-cut-iso p) (c , m) =
    cong (λ z → c , z) (merge-split c m)
