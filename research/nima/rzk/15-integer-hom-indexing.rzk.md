# Canonical integer Hom indexing

This module reuses Grothendieck's canonical signed integers, addition laws,
and identity-path uniqueness. The dependency closure is read-only and
recorded with content digests. No duplicate integer datatype is introduced.

```rzk
#lang rzk-1

#define nima-z-next (i : MariciInt) : MariciInt
  := marici-int-add i marici-int-one

#define nima-z-shift (n i : MariciInt) : MariciInt
  := marici-int-add i n

#define nima-z-target-step (n i : MariciInt)
  : nima-z-next (nima-z-shift n i) = nima-z-shift (nima-z-next n) i
  := marici-int-add-assoc i n marici-int-one

#define nima-z-source-step (n i : MariciInt)
  : nima-z-shift n (nima-z-next i) = nima-z-shift (nima-z-next n) i
  := nima-frame-concat MariciInt
       (marici-int-add (marici-int-add i marici-int-one) n)
       (marici-int-add i (marici-int-add marici-int-one n))
       (marici-int-add i (marici-int-add n marici-int-one))
       (marici-int-add-assoc i marici-int-one n)
       (nima-frame-ap MariciInt MariciInt (marici-int-add i)
         (marici-int-add marici-int-one n) (marici-int-add n marici-int-one)
         (marici-int-add-comm marici-int-one n))

#define nima-z-compose-shift (n m i : MariciInt)
  : nima-z-shift m (nima-z-shift n i) = nima-z-shift (marici-int-add n m) i
  := marici-int-add-assoc i n m

#define nima-z-unit-shift (i : MariciInt)
  : nima-z-shift marici-int-zero i = i
  := marici-int-add-zero-right i

#define nima-z-inverse-shift (n i : MariciInt)
  : nima-z-shift (marici-int-negate n) (nima-z-shift n i) = i
  := nima-frame-concat MariciInt
       (marici-int-add (marici-int-add i n) (marici-int-negate n))
       (marici-int-add i (marici-int-add n (marici-int-negate n))) i
       (marici-int-add-assoc i n (marici-int-negate n))
       (nima-frame-concat MariciInt (marici-int-add i (marici-int-add n (marici-int-negate n)))
         (marici-int-add i marici-int-zero) i
         (nima-frame-ap MariciInt MariciInt (marici-int-add i)
           (marici-int-add n (marici-int-negate n)) marici-int-zero
           (marici-int-add-inverse-right n))
         (marici-int-add-zero-right i))

#define nima-z-alignment-coherent
  (i j : MariciInt) (p q : i = j) : p = q
  := marici-int-identity-path-unique i j p q

#define nima-z-transport-coherent
  (M : MariciInt -> U) (i j : MariciInt) (p q : i = j) (x : M i)
  : nima-hom-transport MariciInt M i j p x = nima-hom-transport MariciInt M i j q x
  := nima-frame-ap (i = j) (M j) (\ t -> nima-hom-transport MariciInt M i j t x)
       p q (nima-z-alignment-coherent i j p q)

#define nima-integer-hom
  (L M : MariciInt -> U) (n : MariciInt) : U
  := nima-hom-family MariciInt L M (nima-z-shift n)

#define nima-integer-hom-differential-even
  (L M : MariciInt -> U)
  (dL : (i : MariciInt) -> L i -> L (nima-z-next i))
  (dM : (i : MariciInt) -> M i -> M (nima-z-next i))
  (sub : (i : MariciInt) -> M i -> M i -> M i)
  (n : MariciInt) (f : nima-integer-hom L M n)
  : nima-integer-hom L M (nima-z-next n)
  := nima-hom-differential-even MariciInt L M nima-z-next
       (nima-z-shift n) (nima-z-shift (nima-z-next n))
       (nima-z-target-step n) (nima-z-source-step n) dL dM sub f

#define nima-integer-hom-differential-odd
  (L M : MariciInt -> U)
  (dL : (i : MariciInt) -> L i -> L (nima-z-next i))
  (dM : (i : MariciInt) -> M i -> M (nima-z-next i))
  (add : (i : MariciInt) -> M i -> M i -> M i)
  (n : MariciInt) (f : nima-integer-hom L M n)
  : nima-integer-hom L M (nima-z-next n)
  := nima-hom-differential-odd MariciInt L M nima-z-next
       (nima-z-shift n) (nima-z-shift (nima-z-next n))
       (nima-z-target-step n) (nima-z-source-step n) dL dM add f

#define nima-integer-hom-compose
  (L M N : MariciInt -> U) (p q : MariciInt)
  (g : nima-integer-hom M N p) (f : nima-integer-hom L M q)
  : nima-integer-hom L N (marici-int-add q p)
  := \ i x -> nima-hom-transport MariciInt N
       (nima-z-shift p (nima-z-shift q i)) (nima-z-shift (marici-int-add q p) i)
       (nima-z-compose-shift q p i) (g (nima-z-shift q i) (f i x))

#define nima-z-minus-one-step
  : nima-z-next marici-int-minus-one = marici-int-zero
  := refl

#define nima-z-minus-two-step
  : nima-z-next marici-int-minus-two = marici-int-minus-one
  := refl
```

## Computed parity, including negative degrees

```rzk
#data NimaDegreeParity
  := nima-degree-even
  | nima-degree-odd

#define nima-degree-flip (p : NimaDegreeParity) : NimaDegreeParity
  := match p (nima-degree-even => nima-degree-odd | nima-degree-odd => nima-degree-even)

#define nima-degree-flip-involutive (p : NimaDegreeParity)
  : nima-degree-flip (nima-degree-flip p) = p
  := match p (nima-degree-even => refl | nima-degree-odd => refl)

#define nima-natural-parity (n : MariciNat) : NimaDegreeParity
  := match n (marici-zero => nima-degree-even | marici-succ k ih => nima-degree-flip ih)

#define nima-integer-parity (n : MariciInt) : NimaDegreeParity
  := match n
       (marici-int-zero => nima-degree-even
       | marici-int-pos k => nima-degree-flip (nima-natural-parity k)
       | marici-int-neg k => nima-degree-flip (nima-natural-parity k))

#define nima-integer-parity-next (n : MariciInt)
  : nima-integer-parity (nima-z-next n) = nima-degree-flip (nima-integer-parity n)
  := match n
       (marici-int-zero => refl
       | marici-int-pos k =>
         nima-frame-ap MariciNat NimaDegreeParity
           (\ j -> nima-degree-flip (nima-degree-flip (nima-natural-parity j)))
           (marici-add k marici-zero) k (marici-add-zero-right k)
       | marici-int-neg k => match k into
           (\ j -> nima-integer-parity (nima-z-next (marici-int-neg j))
             = nima-degree-flip (nima-integer-parity (marici-int-neg j)))
           (marici-zero => refl
           | marici-succ j ih =>
             nima-frame-concat NimaDegreeParity
               (nima-degree-flip (nima-natural-parity (marici-sub j marici-zero)))
               (nima-degree-flip (nima-natural-parity j))
               (nima-degree-flip (nima-degree-flip (nima-degree-flip (nima-natural-parity j))))
               (nima-frame-ap MariciNat NimaDegreeParity (\ k -> nima-degree-flip (nima-natural-parity k))
                 (marici-sub j marici-zero) j (marici-sub-zero-right j))
               (nima-frame-rev NimaDegreeParity
                 (nima-degree-flip (nima-degree-flip (nima-degree-flip (nima-natural-parity j))))
                 (nima-degree-flip (nima-natural-parity j))
                 (nima-degree-flip-involutive (nima-degree-flip (nima-natural-parity j))))))

#define nima-integer-hom-differential
  (L M : MariciInt -> U)
  (dL : (i : MariciInt) -> L i -> L (nima-z-next i))
  (dM : (i : MariciInt) -> M i -> M (nima-z-next i))
  (add sub : (i : MariciInt) -> M i -> M i -> M i)
  (n : MariciInt) (f : nima-integer-hom L M n)
  : nima-integer-hom L M (nima-z-next n)
  := match (nima-integer-parity n) into (\ _ -> nima-integer-hom L M (nima-z-next n))
       (nima-degree-even => nima-integer-hom-differential-even L M dL dM sub n f
       | nima-degree-odd => nima-integer-hom-differential-odd L M dL dM add n f)

#define nima-negative-one-is-odd
  : nima-integer-parity marici-int-minus-one = nima-degree-odd
  := refl

#define nima-negative-two-is-even
  : nima-integer-parity marici-int-minus-two = nima-degree-even
  := refl
```

Degree arithmetic, parallel alignment coherence and parity selection are
instantiated. The module/operator laws still need their concrete coefficient
instances; no derived-Hom realization follows from indexing alone. The index
is cochain degree, not physical time.
