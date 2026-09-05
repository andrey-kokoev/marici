# Canonical-integer identity-path uniqueness

Integer-code uniqueness maps under decoding. Composing that equality with the
path-side decode--encode composites proves any two parallel canonical-integer
paths equal.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-identity-path-unique
  ( z w : MariciInt)
  ( e f : z =_{MariciInt} w)
  : e =_{(z =_{MariciInt} w)} f
  := concat (z =_{MariciInt} w)
      e
      (marici-int-identity-decode z w
        (marici-int-identity-encode z w e))
      f
      (rev (z =_{MariciInt} w)
        (marici-int-identity-decode z w
          (marici-int-identity-encode z w e)) e
        (marici-int-identity-decode-encode-all z w e))
      (concat (z =_{MariciInt} w)
        (marici-int-identity-decode z w
          (marici-int-identity-encode z w e))
        (marici-int-identity-decode z w
          (marici-int-identity-encode z w f))
        f
        (ap (MariciIntIdentityCode z w) (z =_{MariciInt} w)
          (marici-int-identity-encode z w e)
          (marici-int-identity-encode z w f)
          (marici-int-identity-decode z w)
          (marici-int-identity-code-unique z w
            (marici-int-identity-encode z w e)
            (marici-int-identity-encode z w f)))
        (marici-int-identity-decode-encode-all z w f))
```

## Boundary

Every canonical-integer identity type is proposition-valued. This closes
identity-path uniqueness, not decidable equality. Ring packaging still depends
on the outstanding mixed-sign addition associativity theorem.
