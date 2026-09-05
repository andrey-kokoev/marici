# Canonical-integer identity-code uniqueness

Every inhabited canonical-integer identity code has a unique inhabitant. The
zero code uses singleton uniqueness, equal-sign nonzero codes use natural-code
uniqueness, and mixed codes eliminate from emptiness.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-identity-code-unique
  ( z w : MariciInt)
  ( x y : MariciIntIdentityCode z w)
  : x =_{MariciIntIdentityCode z w} y
  := (match z into
        (\ z-prime → (w-prime : MariciInt)
          → (x-prime y-prime : MariciIntIdentityCode z-prime w-prime)
          → x-prime =_{MariciIntIdentityCode z-prime w-prime} y-prime)
      ( marici-int-zero ⇒ \ q → match q
          ( marici-int-zero ⇒ \ u v → marici-unit-unique u v
          | marici-int-pos b ⇒ \ u v →
              marici-empty-elim (u =_{MariciEmpty} v) u
          | marici-int-neg b ⇒ \ u v →
              marici-empty-elim (u =_{MariciEmpty} v) u)
      | marici-int-pos a ⇒ \ q → match q
          ( marici-int-zero ⇒ \ u v →
              marici-empty-elim (u =_{MariciEmpty} v) u
          | marici-int-pos b ⇒ \ u v →
              marici-nat-identity-code-unique a b u v
          | marici-int-neg b ⇒ \ u v →
              marici-empty-elim (u =_{MariciEmpty} v) u)
      | marici-int-neg a ⇒ \ q → match q
          ( marici-int-zero ⇒ \ u v →
              marici-empty-elim (u =_{MariciEmpty} v) u
          | marici-int-pos b ⇒ \ u v →
              marici-empty-elim (u =_{MariciEmpty} v) u
          | marici-int-neg b ⇒ \ u v →
              marici-nat-identity-code-unique a b u v))) w x y
```

## Boundary

Every canonical-integer identity code is proposition-valued. The reflexive and
arbitrary path-side decode--encode composites remain before this code
uniqueness transfers to integer identity-path uniqueness.
