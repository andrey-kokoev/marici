# Finite coefficient presentations

Finite integral sums, not arbitrary infinite coefficient functions. Equality is
an explicit setoid relation: every integer-valued basis probe has equal linear
evaluation. This retains finite support without assuming function extensionality
or a quotient-type axiom. Subsequent polynomial/localized bases are concrete.
A setoid presentation is not silently identified with Rzk identity types.

```rzk
#lang rzk-1

#data NimaZSum (A : U)
  := nima-sum-zero
  | nima-sum-atom (a : A)
  | nima-sum-add (p q : NimaZSum A)
  | nima-sum-neg (p : NimaZSum A)
  | nima-sum-scale (c : MariciInt) (p : NimaZSum A)

#define nima-sum-eval (A : U) (probe : A -> MariciInt) (p : NimaZSum A) : MariciInt
  := match p
       (nima-sum-zero => marici-int-zero
       | nima-sum-atom a => probe a
       | nima-sum-add x ihx y ihy => marici-int-add ihx ihy
       | nima-sum-neg x ih => marici-int-negate ih
       | nima-sum-scale c x ih => marici-int-mul c ih)

#define nima-sum-equal (A : U) (p q : NimaZSum A) : U
  := (probe : A -> MariciInt) -> nima-sum-eval A probe p = nima-sum-eval A probe q

#define nima-sum-equal-refl (A : U) (p : NimaZSum A) : nima-sum-equal A p p := \ probe -> refl
#define nima-sum-equal-rev (A : U) (p q : NimaZSum A) (h : nima-sum-equal A p q) : nima-sum-equal A q p
  := \ probe -> nima-frame-rev MariciInt (nima-sum-eval A probe p) (nima-sum-eval A probe q) (h probe)
#define nima-sum-equal-trans (A : U) (p q r : NimaZSum A)
  (h : nima-sum-equal A p q) (k : nima-sum-equal A q r) : nima-sum-equal A p r
  := \ probe -> nima-frame-concat MariciInt (nima-sum-eval A probe p) (nima-sum-eval A probe q) (nima-sum-eval A probe r) (h probe) (k probe)

#define nima-sum-add-assoc (A : U) (p q r : NimaZSum A)
  : nima-sum-equal A (nima-sum-add A (nima-sum-add A p q) r) (nima-sum-add A p (nima-sum-add A q r))
  := \ probe -> marici-int-add-assoc (nima-sum-eval A probe p) (nima-sum-eval A probe q) (nima-sum-eval A probe r)
#define nima-sum-add-comm (A : U) (p q : NimaZSum A)
  : nima-sum-equal A (nima-sum-add A p q) (nima-sum-add A q p)
  := \ probe -> marici-int-add-comm (nima-sum-eval A probe p) (nima-sum-eval A probe q)
#define nima-sum-add-left-zero (A : U) (p : NimaZSum A)
  : nima-sum-equal A (nima-sum-add A (nima-sum-zero A) p) p := \ probe -> refl
#define nima-sum-add-right-zero (A : U) (p : NimaZSum A)
  : nima-sum-equal A (nima-sum-add A p (nima-sum-zero A)) p
  := \ probe -> marici-int-add-zero-right (nima-sum-eval A probe p)
#define nima-sum-add-inverse (A : U) (p : NimaZSum A)
  : nima-sum-equal A (nima-sum-add A p (nima-sum-neg A p)) (nima-sum-zero A)
  := \ probe -> marici-int-add-inverse-right (nima-sum-eval A probe p)
#define nima-sum-scale-one (A : U) (p : NimaZSum A)
  : nima-sum-equal A (nima-sum-scale A marici-int-one p) p
  := \ probe -> marici-int-mul-one-left (nima-sum-eval A probe p)
#define nima-sum-scale-assoc (A : U) (a b : MariciInt) (p : NimaZSum A)
  : nima-sum-equal A (nima-sum-scale A (marici-int-mul a b) p) (nima-sum-scale A a (nima-sum-scale A b p))
  := \ probe -> marici-int-mul-assoc a b (nima-sum-eval A probe p)
#define nima-sum-scale-add (A : U) (a : MariciInt) (p q : NimaZSum A)
  : nima-sum-equal A (nima-sum-scale A a (nima-sum-add A p q)) (nima-sum-add A (nima-sum-scale A a p) (nima-sum-scale A a q))
  := \ probe -> marici-int-mul-add-left-distrib a (nima-sum-eval A probe p) (nima-sum-eval A probe q)
#define nima-sum-add-scale (A : U) (a b : MariciInt) (p : NimaZSum A)
  : nima-sum-equal A (nima-sum-scale A (marici-int-add a b) p) (nima-sum-add A (nima-sum-scale A a p) (nima-sum-scale A b p))
  := \ probe -> marici-int-mul-add-right-distrib a b (nima-sum-eval A probe p)

#define nima-sum-bind (A B : U) (column : A -> NimaZSum B) (p : NimaZSum A) : NimaZSum B
  := match p
       (nima-sum-zero => nima-sum-zero B
       | nima-sum-atom a => column a
       | nima-sum-add x ihx y ihy => nima-sum-add B ihx ihy
       | nima-sum-neg x ih => nima-sum-neg B ih
       | nima-sum-scale c x ih => nima-sum-scale B c ih)
#define nima-sum-map (A B : U) (f : A -> B) (p : NimaZSum A) : NimaZSum B
  := nima-sum-bind A B (\ a -> nima-sum-atom B (f a)) p

#define nima-sum-eval-bind (A B : U) (column : A -> NimaZSum B) (probe : B -> MariciInt) (p : NimaZSum A)
  : nima-sum-eval B probe (nima-sum-bind A B column p)
    = nima-sum-eval A (\ a -> nima-sum-eval B probe (column a)) p
  := match p
       (nima-sum-zero => refl
       | nima-sum-atom a => refl
       | nima-sum-add x ihx y ihy => nima-cochain-ap2 MariciInt MariciInt MariciInt marici-int-add
           (nima-sum-eval B probe (nima-sum-bind A B column x)) (nima-sum-eval A (\ a -> nima-sum-eval B probe (column a)) x)
           (nima-sum-eval B probe (nima-sum-bind A B column y)) (nima-sum-eval A (\ a -> nima-sum-eval B probe (column a)) y) ihx ihy
       | nima-sum-neg x ih => nima-frame-ap MariciInt MariciInt marici-int-negate
           (nima-sum-eval B probe (nima-sum-bind A B column x)) (nima-sum-eval A (\ a -> nima-sum-eval B probe (column a)) x) ih
       | nima-sum-scale c x ih => nima-frame-ap MariciInt MariciInt (marici-int-mul c)
           (nima-sum-eval B probe (nima-sum-bind A B column x)) (nima-sum-eval A (\ a -> nima-sum-eval B probe (column a)) x) ih)

#define nima-sum-bind-cong (A B : U) (column : A -> NimaZSum B) (p q : NimaZSum A)
  (equal : nima-sum-equal A p q) : nima-sum-equal B (nima-sum-bind A B column p) (nima-sum-bind A B column q)
  := \ probe -> nima-frame-concat MariciInt
       (nima-sum-eval B probe (nima-sum-bind A B column p))
       (nima-sum-eval A (\ a -> nima-sum-eval B probe (column a)) p)
       (nima-sum-eval B probe (nima-sum-bind A B column q))
       (nima-sum-eval-bind A B column probe p)
       (nima-frame-concat MariciInt
         (nima-sum-eval A (\ a -> nima-sum-eval B probe (column a)) p)
         (nima-sum-eval A (\ a -> nima-sum-eval B probe (column a)) q)
         (nima-sum-eval B probe (nima-sum-bind A B column q))
         (equal (\ a -> nima-sum-eval B probe (column a)))
         (nima-frame-rev MariciInt (nima-sum-eval B probe (nima-sum-bind A B column q))
           (nima-sum-eval A (\ a -> nima-sum-eval B probe (column a)) q) (nima-sum-eval-bind A B column probe q)))

#define nima-sum-bind-assoc (A B C : U) (f : A -> NimaZSum B) (g : B -> NimaZSum C) (p : NimaZSum A)
  : nima-sum-bind B C g (nima-sum-bind A B f p) = nima-sum-bind A C (\ a -> nima-sum-bind B C g (f a)) p
  := match p
       (nima-sum-zero => refl
       | nima-sum-atom a => refl
       | nima-sum-add x ihx y ihy => nima-cochain-ap2 (NimaZSum C) (NimaZSum C) (NimaZSum C) (nima-sum-add C)
           (nima-sum-bind B C g (nima-sum-bind A B f x)) (nima-sum-bind A C (\ a -> nima-sum-bind B C g (f a)) x)
           (nima-sum-bind B C g (nima-sum-bind A B f y)) (nima-sum-bind A C (\ a -> nima-sum-bind B C g (f a)) y) ihx ihy
       | nima-sum-neg x ih => nima-frame-ap (NimaZSum C) (NimaZSum C) (nima-sum-neg C)
           (nima-sum-bind B C g (nima-sum-bind A B f x)) (nima-sum-bind A C (\ a -> nima-sum-bind B C g (f a)) x) ih
       | nima-sum-scale c x ih => nima-frame-ap (NimaZSum C) (NimaZSum C) (nima-sum-scale C c)
           (nima-sum-bind B C g (nima-sum-bind A B f x)) (nima-sum-bind A C (\ a -> nima-sum-bind B C g (f a)) x) ih)

#define nima-sum-bind-zero (A B : U) (column : A -> NimaZSum B)
  (vanishes : (a : A) -> nima-sum-equal B (column a) (nima-sum-zero B)) (p : NimaZSum A)
  : nima-sum-equal B (nima-sum-bind A B column p) (nima-sum-zero B)
  := match p
       (nima-sum-zero => \ probe -> refl
       | nima-sum-atom a => vanishes a
       | nima-sum-add x ihx y ihy => \ probe -> nima-cochain-ap2 MariciInt MariciInt MariciInt marici-int-add
           (nima-sum-eval B probe (nima-sum-bind A B column x)) marici-int-zero
           (nima-sum-eval B probe (nima-sum-bind A B column y)) marici-int-zero (ihx probe) (ihy probe)
       | nima-sum-neg x ih => \ probe -> nima-frame-ap MariciInt MariciInt marici-int-negate
           (nima-sum-eval B probe (nima-sum-bind A B column x)) marici-int-zero (ih probe)
       | nima-sum-scale c x ih => \ probe -> nima-frame-concat MariciInt
           (marici-int-mul c (nima-sum-eval B probe (nima-sum-bind A B column x)))
           (marici-int-mul c marici-int-zero) marici-int-zero
           (nima-frame-ap MariciInt MariciInt (marici-int-mul c)
             (nima-sum-eval B probe (nima-sum-bind A B column x)) marici-int-zero (ih probe))
           (marici-int-mul-zero-right c))

#define nima-sum-column-square (A : U) (column : A -> NimaZSum A)
  (square : (a : A) -> nima-sum-equal A (nima-sum-bind A A column (column a)) (nima-sum-zero A)) (p : NimaZSum A)
  : nima-sum-equal A (nima-sum-bind A A column (nima-sum-bind A A column p)) (nima-sum-zero A)
  := \ probe -> nima-frame-concat MariciInt
       (nima-sum-eval A probe (nima-sum-bind A A column (nima-sum-bind A A column p)))
       (nima-sum-eval A probe (nima-sum-bind A A (\ a -> nima-sum-bind A A column (column a)) p)) marici-int-zero
       (nima-frame-ap (NimaZSum A) MariciInt (nima-sum-eval A probe)
         (nima-sum-bind A A column (nima-sum-bind A A column p))
         (nima-sum-bind A A (\ a -> nima-sum-bind A A column (column a)) p)
         (nima-sum-bind-assoc A A A column column p))
       (nima-sum-bind-zero A A (\ a -> nima-sum-bind A A column (column a)) square p probe)

#define nima-int-swap-prefix (a b c : MariciInt)
  : marici-int-add a (marici-int-add b c) = marici-int-add b (marici-int-add a c)
  := nima-frame-concat MariciInt
       (marici-int-add a (marici-int-add b c)) (marici-int-add (marici-int-add a b) c)
       (marici-int-add b (marici-int-add a c))
       (nima-frame-rev MariciInt (marici-int-add (marici-int-add a b) c) (marici-int-add a (marici-int-add b c)) (marici-int-add-assoc a b c))
       (nima-frame-concat MariciInt (marici-int-add (marici-int-add a b) c) (marici-int-add (marici-int-add b a) c)
         (marici-int-add b (marici-int-add a c))
         (nima-frame-ap MariciInt MariciInt (\ t -> marici-int-add t c) (marici-int-add a b) (marici-int-add b a) (marici-int-add-comm a b))
         (marici-int-add-assoc b a c))

#define nima-int-cancel-positive-prefix (a b : MariciInt)
  : marici-int-add a (marici-int-add (marici-int-negate a) b) = b
  := nima-frame-concat MariciInt
       (marici-int-add a (marici-int-add (marici-int-negate a) b))
       (marici-int-add (marici-int-add a (marici-int-negate a)) b) b
       (nima-frame-rev MariciInt (marici-int-add (marici-int-add a (marici-int-negate a)) b)
         (marici-int-add a (marici-int-add (marici-int-negate a) b)) (marici-int-add-assoc a (marici-int-negate a) b))
       (nima-frame-ap MariciInt MariciInt (\ t -> marici-int-add t b)
         (marici-int-add a (marici-int-negate a)) marici-int-zero (marici-int-add-inverse-right a))

#define nima-int-cancel-negative-prefix (a b : MariciInt)
  : marici-int-add (marici-int-negate a) (marici-int-add a b) = b
  := nima-frame-concat MariciInt
       (marici-int-add (marici-int-negate a) (marici-int-add a b))
       (marici-int-add (marici-int-add (marici-int-negate a) a) b) b
       (nima-frame-rev MariciInt (marici-int-add (marici-int-add (marici-int-negate a) a) b)
         (marici-int-add (marici-int-negate a) (marici-int-add a b)) (marici-int-add-assoc (marici-int-negate a) a b))
       (nima-frame-ap MariciInt MariciInt (\ t -> marici-int-add t b)
         (marici-int-add (marici-int-negate a) a) marici-int-zero (marici-int-add-inverse-left a))
```
