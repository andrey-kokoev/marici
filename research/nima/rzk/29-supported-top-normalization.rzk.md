# Normalization of arbitrary supported top coefficients

```rzk
#lang rzk-1

#define NimaUSTCoefficients : U := NimaZSum NimaUSTMonomial

#define nima-ust-top-atom (m : NimaUSTMonomial) : NimaLocalCoefficients
  := nima-sum-atom NimaLocalBasis (nima-local-state-15,m)

#define nima-ust-primitive-atom : NimaUSTMonomial -> NimaLocalCoefficients
  := \ (u,(s,t)) -> match u
       (marici-zero => match s
          (marici-zero => match t
             (marici-zero => nima-sum-zero NimaLocalBasis
             | marici-succ t' _ => nima-positive-primitive-atom (nima-positive-t t'))
          | marici-succ s' _ => nima-positive-primitive-atom (nima-positive-s s' t))
       | marici-succ u' _ => nima-positive-primitive-atom (nima-positive-u u' s t))

#define nima-ust-constant-atom : NimaUSTMonomial -> MariciInt
  := \ (u,(s,t)) -> match u
       (marici-zero => match s
          (marici-zero => match t
             (marici-zero => marici-int-one | marici-succ _ _ => marici-int-zero)
          | marici-succ _ _ => marici-int-zero)
       | marici-succ _ _ => marici-int-zero)

#define nima-ust-top (p : NimaUSTCoefficients) : NimaLocalCoefficients
  := nima-sum-bind NimaUSTMonomial NimaLocalBasis nima-ust-top-atom p
#define nima-ust-primitive (p : NimaUSTCoefficients) : NimaLocalCoefficients
  := nima-sum-bind NimaUSTMonomial NimaLocalBasis nima-ust-primitive-atom p
#define nima-ust-constant (p : NimaUSTCoefficients) : MariciInt
  := nima-sum-eval NimaUSTMonomial nima-ust-constant-atom p

#define nima-local-scaled-tau (c : MariciInt) : NimaLocalCoefficients
  := nima-sum-scale NimaLocalBasis c nima-local-tau

#define nima-local-decomposition (p : NimaUSTCoefficients) : U
  := nima-sum-equal NimaLocalBasis (nima-ust-top p)
       (nima-sum-add NimaLocalBasis
         (nima-local-d (nima-ust-primitive p))
         (nima-local-scaled-tau (nima-ust-constant p)))

#define nima-local-add-scaled-zero-right (x : NimaLocalCoefficients)
  : nima-sum-equal NimaLocalBasis
      (nima-sum-add NimaLocalBasis x (nima-local-scaled-tau marici-int-zero)) x
  := \ probe -> nima-frame-concat MariciInt
       (marici-int-add (nima-sum-eval NimaLocalBasis probe x)
         (marici-int-mul marici-int-zero (nima-sum-eval NimaLocalBasis probe nima-local-tau)))
       (marici-int-add (nima-sum-eval NimaLocalBasis probe x) marici-int-zero)
       (nima-sum-eval NimaLocalBasis probe x)
       (nima-cochain-ap2 MariciInt MariciInt MariciInt marici-int-add
         (nima-sum-eval NimaLocalBasis probe x) (nima-sum-eval NimaLocalBasis probe x)
         (marici-int-mul marici-int-zero (nima-sum-eval NimaLocalBasis probe nima-local-tau)) marici-int-zero
         refl (marici-int-mul-zero-left (nima-sum-eval NimaLocalBasis probe nima-local-tau)))
       (marici-int-add-zero-right (nima-sum-eval NimaLocalBasis probe x))

#define nima-ust-atom-decomposition : (m : NimaUSTMonomial) ->
  nima-local-decomposition (nima-sum-atom NimaUSTMonomial m)
  := \ (u,(s,t)) -> match u into
       (\ u0 -> nima-local-decomposition (nima-sum-atom NimaUSTMonomial (u0,(s,t)))) (
       marici-zero => match s into
          (\ s0 -> nima-local-decomposition (nima-sum-atom NimaUSTMonomial (marici-zero,(s0,t)))) (
          marici-zero => match t into
             (\ t0 -> nima-local-decomposition (nima-sum-atom NimaUSTMonomial (marici-zero,(marici-zero,t0)))) (
             marici-zero => \ probe -> nima-frame-rev MariciInt
                (marici-int-mul marici-int-one (probe (nima-local-state-15,(marici-zero,(marici-zero,marici-zero)))))
                (probe (nima-local-state-15,(marici-zero,(marici-zero,marici-zero))))
                (marici-int-mul-one-left (probe (nima-local-state-15,(marici-zero,(marici-zero,marici-zero)))))
             | marici-succ t' _ => nima-sum-equal-trans NimaLocalBasis
                (nima-positive-top-atom (nima-positive-t t'))
                (nima-local-d (nima-positive-primitive-atom (nima-positive-t t')))
                (nima-sum-add NimaLocalBasis
                  (nima-local-d (nima-positive-primitive-atom (nima-positive-t t')))
                  (nima-local-scaled-tau marici-int-zero))
                (nima-positive-atom-boundary (nima-positive-t t'))
                (nima-sum-equal-rev NimaLocalBasis
                  (nima-sum-add NimaLocalBasis (nima-local-d (nima-positive-primitive-atom (nima-positive-t t'))) (nima-local-scaled-tau marici-int-zero))
                  (nima-local-d (nima-positive-primitive-atom (nima-positive-t t')))
                  (nima-local-add-scaled-zero-right (nima-local-d (nima-positive-primitive-atom (nima-positive-t t'))))))
          | marici-succ s' _ => nima-sum-equal-trans NimaLocalBasis
                (nima-positive-top-atom (nima-positive-s s' t))
                (nima-local-d (nima-positive-primitive-atom (nima-positive-s s' t)))
                (nima-sum-add NimaLocalBasis
                  (nima-local-d (nima-positive-primitive-atom (nima-positive-s s' t)))
                  (nima-local-scaled-tau marici-int-zero))
                (nima-positive-atom-boundary (nima-positive-s s' t))
                (nima-sum-equal-rev NimaLocalBasis
                  (nima-sum-add NimaLocalBasis (nima-local-d (nima-positive-primitive-atom (nima-positive-s s' t))) (nima-local-scaled-tau marici-int-zero))
                  (nima-local-d (nima-positive-primitive-atom (nima-positive-s s' t)))
                  (nima-local-add-scaled-zero-right (nima-local-d (nima-positive-primitive-atom (nima-positive-s s' t))))))
       | marici-succ u' _ => nima-sum-equal-trans NimaLocalBasis
                (nima-positive-top-atom (nima-positive-u u' s t))
                (nima-local-d (nima-positive-primitive-atom (nima-positive-u u' s t)))
                (nima-sum-add NimaLocalBasis
                  (nima-local-d (nima-positive-primitive-atom (nima-positive-u u' s t)))
                  (nima-local-scaled-tau marici-int-zero))
                (nima-positive-atom-boundary (nima-positive-u u' s t))
                (nima-sum-equal-rev NimaLocalBasis
                  (nima-sum-add NimaLocalBasis (nima-local-d (nima-positive-primitive-atom (nima-positive-u u' s t))) (nima-local-scaled-tau marici-int-zero))
                  (nima-local-d (nima-positive-primitive-atom (nima-positive-u u' s t)))
                  (nima-local-add-scaled-zero-right (nima-local-d (nima-positive-primitive-atom (nima-positive-u u' s t))))))

#define nima-local-decomposition-add
  (px cx py cy a : MariciInt)
  : marici-int-add (marici-int-add px cx) (marici-int-add py cy)
    = marici-int-add (marici-int-add px py) (marici-int-add cx cy)
  := nima-frame-concat MariciInt
       (marici-int-add (marici-int-add px cx) (marici-int-add py cy))
       (marici-int-add px (marici-int-add cx (marici-int-add py cy)))
       (marici-int-add (marici-int-add px py) (marici-int-add cx cy))
       (marici-int-add-assoc px cx (marici-int-add py cy))
       (nima-frame-concat MariciInt
         (marici-int-add px (marici-int-add cx (marici-int-add py cy)))
         (marici-int-add px (marici-int-add py (marici-int-add cx cy)))
         (marici-int-add (marici-int-add px py) (marici-int-add cx cy))
         (nima-frame-ap MariciInt MariciInt (marici-int-add px)
           (marici-int-add cx (marici-int-add py cy))
           (marici-int-add py (marici-int-add cx cy))
           (nima-int-swap-prefix cx py cy))
         (nima-frame-rev MariciInt
           (marici-int-add (marici-int-add px py) (marici-int-add cx cy))
           (marici-int-add px (marici-int-add py (marici-int-add cx cy)))
           (marici-int-add-assoc px py (marici-int-add cx cy))))

#define nima-local-decomposition-add-scalars (p c q d a : MariciInt)
  : marici-int-add (marici-int-add p (marici-int-mul c a))
      (marici-int-add q (marici-int-mul d a))
    = marici-int-add (marici-int-add p q) (marici-int-mul (marici-int-add c d) a)
  := nima-frame-concat MariciInt
       (marici-int-add (marici-int-add p (marici-int-mul c a)) (marici-int-add q (marici-int-mul d a)))
       (marici-int-add (marici-int-add p q) (marici-int-add (marici-int-mul c a) (marici-int-mul d a)))
       (marici-int-add (marici-int-add p q) (marici-int-mul (marici-int-add c d) a))
       (nima-local-decomposition-add p (marici-int-mul c a) q (marici-int-mul d a) a)
       (nima-frame-ap MariciInt MariciInt (marici-int-add (marici-int-add p q))
         (marici-int-add (marici-int-mul c a) (marici-int-mul d a))
         (marici-int-mul (marici-int-add c d) a)
         (nima-frame-rev MariciInt
           (marici-int-mul (marici-int-add c d) a)
           (marici-int-add (marici-int-mul c a) (marici-int-mul d a))
           (marici-int-mul-add-right-distrib c d a)))

#define nima-local-decomposition-neg-scalars (p c a : MariciInt)
  : marici-int-negate (marici-int-add p (marici-int-mul c a))
    = marici-int-add (marici-int-negate p) (marici-int-mul (marici-int-negate c) a)
  := nima-frame-concat MariciInt
       (marici-int-negate (marici-int-add p (marici-int-mul c a)))
       (marici-int-add (marici-int-negate p) (marici-int-negate (marici-int-mul c a)))
       (marici-int-add (marici-int-negate p) (marici-int-mul (marici-int-negate c) a))
       (marici-int-negate-add p (marici-int-mul c a))
       (nima-cochain-ap2 MariciInt MariciInt MariciInt marici-int-add
         (marici-int-negate p) (marici-int-negate p)
         (marici-int-negate (marici-int-mul c a)) (marici-int-mul (marici-int-negate c) a) refl
         (nima-frame-rev MariciInt
           (marici-int-mul (marici-int-negate c) a) (marici-int-negate (marici-int-mul c a))
           (marici-int-mul-negate-left c a)))

#define nima-local-decomposition-scale-scalars (k p c a : MariciInt)
  : marici-int-mul k (marici-int-add p (marici-int-mul c a))
    = marici-int-add (marici-int-mul k p) (marici-int-mul (marici-int-mul k c) a)
  := nima-frame-concat MariciInt
       (marici-int-mul k (marici-int-add p (marici-int-mul c a)))
       (marici-int-add (marici-int-mul k p) (marici-int-mul k (marici-int-mul c a)))
       (marici-int-add (marici-int-mul k p) (marici-int-mul (marici-int-mul k c) a))
       (marici-int-mul-add-left-distrib k p (marici-int-mul c a))
       (nima-cochain-ap2 MariciInt MariciInt MariciInt marici-int-add
         (marici-int-mul k p) (marici-int-mul k p)
         (marici-int-mul k (marici-int-mul c a)) (marici-int-mul (marici-int-mul k c) a) refl
         (nima-frame-rev MariciInt
           (marici-int-mul (marici-int-mul k c) a) (marici-int-mul k (marici-int-mul c a))
           (marici-int-mul-assoc k c a)))

#define nima-ust-decomposition (p : NimaUSTCoefficients) : nima-local-decomposition p
  := match p
       (nima-sum-zero => \ probe -> refl
       | nima-sum-atom m => nima-ust-atom-decomposition m
       | nima-sum-add x ihx y ihy => \ probe -> nima-frame-concat MariciInt
          (marici-int-add (nima-sum-eval NimaLocalBasis probe (nima-ust-top x))
            (nima-sum-eval NimaLocalBasis probe (nima-ust-top y)))
          (marici-int-add
            (marici-int-add (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive x)))
              (marici-int-mul (nima-ust-constant x) (nima-sum-eval NimaLocalBasis probe nima-local-tau)))
            (marici-int-add (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive y)))
              (marici-int-mul (nima-ust-constant y) (nima-sum-eval NimaLocalBasis probe nima-local-tau))))
          (marici-int-add
            (marici-int-add (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive x)))
              (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive y))))
            (marici-int-mul (marici-int-add (nima-ust-constant x) (nima-ust-constant y))
              (nima-sum-eval NimaLocalBasis probe nima-local-tau)))
          (nima-cochain-ap2 MariciInt MariciInt MariciInt marici-int-add
            (nima-sum-eval NimaLocalBasis probe (nima-ust-top x))
            (marici-int-add (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive x)))
              (marici-int-mul (nima-ust-constant x) (nima-sum-eval NimaLocalBasis probe nima-local-tau)))
            (nima-sum-eval NimaLocalBasis probe (nima-ust-top y))
            (marici-int-add (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive y)))
              (marici-int-mul (nima-ust-constant y) (nima-sum-eval NimaLocalBasis probe nima-local-tau)))
            (ihx probe) (ihy probe))
          (nima-local-decomposition-add-scalars
            (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive x))) (nima-ust-constant x)
            (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive y))) (nima-ust-constant y)
            (nima-sum-eval NimaLocalBasis probe nima-local-tau))
       | nima-sum-neg x ih => \ probe -> nima-frame-concat MariciInt
          (marici-int-negate (nima-sum-eval NimaLocalBasis probe (nima-ust-top x)))
          (marici-int-negate (marici-int-add
            (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive x)))
            (marici-int-mul (nima-ust-constant x) (nima-sum-eval NimaLocalBasis probe nima-local-tau))))
          (marici-int-add
            (marici-int-negate (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive x))))
            (marici-int-mul (marici-int-negate (nima-ust-constant x)) (nima-sum-eval NimaLocalBasis probe nima-local-tau)))
          (nima-frame-ap MariciInt MariciInt marici-int-negate
            (nima-sum-eval NimaLocalBasis probe (nima-ust-top x))
            (marici-int-add (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive x)))
              (marici-int-mul (nima-ust-constant x) (nima-sum-eval NimaLocalBasis probe nima-local-tau))) (ih probe))
          (nima-local-decomposition-neg-scalars
            (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive x)))
            (nima-ust-constant x) (nima-sum-eval NimaLocalBasis probe nima-local-tau))
       | nima-sum-scale c x ih => \ probe -> nima-frame-concat MariciInt
          (marici-int-mul c (nima-sum-eval NimaLocalBasis probe (nima-ust-top x)))
          (marici-int-mul c (marici-int-add
            (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive x)))
            (marici-int-mul (nima-ust-constant x) (nima-sum-eval NimaLocalBasis probe nima-local-tau))))
          (marici-int-add
            (marici-int-mul c (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive x))))
            (marici-int-mul (marici-int-mul c (nima-ust-constant x)) (nima-sum-eval NimaLocalBasis probe nima-local-tau)))
          (nima-frame-ap MariciInt MariciInt (marici-int-mul c)
            (nima-sum-eval NimaLocalBasis probe (nima-ust-top x))
            (marici-int-add (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive x)))
              (marici-int-mul (nima-ust-constant x) (nima-sum-eval NimaLocalBasis probe nima-local-tau))) (ih probe))
          (nima-local-decomposition-scale-scalars c
            (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive x)))
            (nima-ust-constant x) (nima-sum-eval NimaLocalBasis probe nima-local-tau)))

#define nima-ust-zero-residue-is-boundary
  (p : NimaUSTCoefficients)
  (zero-residue : nima-ust-constant p = marici-int-zero)
  : nima-sum-equal NimaLocalBasis (nima-ust-top p)
      (nima-local-d (nima-ust-primitive p))
  := nima-sum-equal-trans NimaLocalBasis
       (nima-ust-top p)
       (nima-sum-add NimaLocalBasis (nima-local-d (nima-ust-primitive p))
         (nima-local-scaled-tau (nima-ust-constant p)))
       (nima-local-d (nima-ust-primitive p))
       (nima-ust-decomposition p)
       (\ probe -> nima-frame-concat MariciInt
         (marici-int-add (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive p)))
           (marici-int-mul (nima-ust-constant p) (nima-sum-eval NimaLocalBasis probe nima-local-tau)))
         (marici-int-add (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive p)))
           (marici-int-mul marici-int-zero (nima-sum-eval NimaLocalBasis probe nima-local-tau)))
         (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive p)))
         (nima-frame-ap MariciInt MariciInt
           (\ c -> marici-int-add
             (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-ust-primitive p)))
             (marici-int-mul c (nima-sum-eval NimaLocalBasis probe nima-local-tau)))
           (nima-ust-constant p) marici-int-zero zero-residue)
         (nima-local-add-scaled-zero-right
           (nima-local-d (nima-ust-primitive p)) probe))
```
