# Marici canonical signed-integer normal form

Integers are represented without a quotient: zero is separate, while positive
and negative constructors carry the predecessor of a strictly positive
magnitude. Thus zero has exactly one constructor-level normal form.

```rzk
#lang rzk-1

#data MariciInt
  := marici-int-zero
  | marici-int-pos (n : MariciNat)
  | marici-int-neg (n : MariciNat)
```

```rzk
#define marici-int-embed-nat
  ( n : MariciNat)
  : MariciInt
  := match n
      ( marici-zero ⇒ marici-int-zero
      | marici-succ k ih ⇒ marici-int-pos k)

#define marici-int-negate
  ( z : MariciInt)
  : MariciInt
  := match z
      ( marici-int-zero ⇒ marici-int-zero
      | marici-int-pos n ⇒ marici-int-neg n
      | marici-int-neg n ⇒ marici-int-pos n)

#define marici-int-negate-involutive
  ( z : MariciInt)
  : marici-int-negate (marici-int-negate z) =_{MariciInt} z
  := match z
      ( marici-int-zero ⇒ refl
      | marici-int-pos n ⇒ refl
      | marici-int-neg n ⇒ refl)
```

Mixed-sign addition compares predecessor magnitudes. Equal predecessors cancel;
the unequal cases use truncated subtraction with one successor removed so that
the result remains in predecessor encoding.

```rzk
#define marici-int-add-pos-neg
  ( a b : MariciNat)
  : MariciInt
  := match (marici-compare a b) into (\ _ → MariciInt)
      ( marici-less ⇒ marici-int-neg (marici-sub b (marici-succ a))
      | marici-equal ⇒ marici-int-zero
      | marici-greater ⇒ marici-int-pos (marici-sub a (marici-succ b)))

#define marici-int-add-neg-pos
  ( a b : MariciNat)
  : MariciInt
  := marici-int-add-pos-neg b a

#define marici-int-add
  ( x y : MariciInt)
  : MariciInt
  := (match x into (\ _ → MariciInt → MariciInt)
      ( marici-int-zero ⇒ \ q → q
      | marici-int-pos a ⇒
          \ q → match q
            ( marici-int-zero ⇒ marici-int-pos a
            | marici-int-pos b ⇒ marici-int-pos (marici-succ (marici-add a b))
            | marici-int-neg b ⇒ marici-int-add-pos-neg a b)
      | marici-int-neg a ⇒
          \ q → match q
            ( marici-int-zero ⇒ marici-int-neg a
            | marici-int-pos b ⇒ marici-int-add-neg-pos a b
            | marici-int-neg b ⇒ marici-int-neg (marici-succ (marici-add a b))))) y
```

```rzk
#define marici-int-one : MariciInt := marici-int-pos marici-zero
#define marici-int-minus-one : MariciInt := marici-int-neg marici-zero
#define marici-int-two : MariciInt := marici-int-pos marici-one
#define marici-int-minus-two : MariciInt := marici-int-neg marici-one

#define marici-int-one-plus-minus-one
  : marici-int-add marici-int-one marici-int-minus-one
    =_{MariciInt} marici-int-zero
  := refl

#define marici-int-two-plus-minus-one
  : marici-int-add marici-int-two marici-int-minus-one
    =_{MariciInt} marici-int-one
  := refl

#define marici-int-minus-two-plus-one
  : marici-int-add marici-int-minus-two marici-int-one
    =_{MariciInt} marici-int-minus-one
  := refl

#define marici-int-minus-one-plus-minus-one
  : marici-int-add marici-int-minus-one marici-int-minus-one
    =_{MariciInt} marici-int-minus-two
  := refl
```

## Boundary

The datatype makes constructor-level zero normalization computational and the
listed examples check. This does not yet prove semantic uniqueness of identity
paths, addition commutativity/associativity, additive inverses for every value,
or the integer universal property. Those claims require comparison and
subtraction interaction lemmas plus sethood.
