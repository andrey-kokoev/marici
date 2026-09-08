# Positive `(u,s,t)` monomials are explicit boundaries

This is the constructive augmentation-ideal half of the local top-cohomology
calculation.  The datatype records which first positive exponent is factored;
there is no test or excluded-middle assumption on natural numbers.

```rzk
#lang rzk-1

#data NimaPositiveUSTMonomial
  := nima-positive-u (u s t : MariciNat)
  | nima-positive-s (s t : MariciNat)
  | nima-positive-t (t : MariciNat)

#define nima-positive-ust-monomial (m : NimaPositiveUSTMonomial) : NimaUSTMonomial
  := match m
       (nima-positive-u u s t => (marici-succ u,(s,t))
       | nima-positive-s s t => (marici-zero,(marici-succ s,t))
       | nima-positive-t t => (marici-zero,(marici-zero,marici-succ t)))

#define NimaPositiveUSTCoefficients : U := NimaZSum NimaPositiveUSTMonomial

#define nima-positive-top-atom (m : NimaPositiveUSTMonomial) : NimaLocalCoefficients
  := nima-sum-atom NimaLocalBasis
       (nima-local-state-15,nima-positive-ust-monomial m)

#define nima-positive-primitive-atom (m : NimaPositiveUSTMonomial) : NimaLocalCoefficients
  := match m
       (nima-positive-u u s t => nima-sum-neg NimaLocalBasis
          (nima-sum-atom NimaLocalBasis (nima-local-state-10,(u,(s,t))))
       | nima-positive-s s t => nima-sum-atom NimaLocalBasis
          (nima-local-state-12,(marici-zero,(s,t)))
       | nima-positive-t t => nima-sum-atom NimaLocalBasis
          (nima-local-state-11,(marici-zero,(marici-zero,t))))

#define nima-positive-top (p : NimaPositiveUSTCoefficients) : NimaLocalCoefficients
  := match p
       (nima-sum-zero => nima-sum-zero NimaLocalBasis
       | nima-sum-atom m => nima-positive-top-atom m
       | nima-sum-add x ihx y ihy => nima-sum-add NimaLocalBasis ihx ihy
       | nima-sum-neg x ih => nima-sum-neg NimaLocalBasis ih
       | nima-sum-scale c x ih => nima-sum-scale NimaLocalBasis c ih)

#define nima-positive-primitive (p : NimaPositiveUSTCoefficients) : NimaLocalCoefficients
  := match p
       (nima-sum-zero => nima-sum-zero NimaLocalBasis
       | nima-sum-atom m => nima-positive-primitive-atom m
       | nima-sum-add x ihx y ihy => nima-sum-add NimaLocalBasis ihx ihy
       | nima-sum-neg x ih => nima-sum-neg NimaLocalBasis ih
       | nima-sum-scale c x ih => nima-sum-scale NimaLocalBasis c ih)

#define nima-positive-atom-boundary (m : NimaPositiveUSTMonomial)
  : nima-sum-equal NimaLocalBasis
      (nima-positive-top-atom m)
      (nima-local-d (nima-positive-primitive-atom m))
  := match m
       (nima-positive-u u s t => \ probe ->
          nima-frame-concat MariciInt
            (probe (nima-local-state-15,(marici-succ u,(s,t))))
            (marici-int-negate (marici-int-negate
              (probe (nima-local-state-15,(marici-succ u,(s,t))))))
            (marici-int-negate (marici-int-add
              (marici-int-negate (probe (nima-local-state-15,(marici-succ u,(s,t)))))
              marici-int-zero))
            (nima-frame-rev MariciInt
              (marici-int-negate (marici-int-negate (probe (nima-local-state-15,(marici-succ u,(s,t))))))
              (probe (nima-local-state-15,(marici-succ u,(s,t))))
              (marici-int-negate-involutive (probe (nima-local-state-15,(marici-succ u,(s,t))))))
            (nima-frame-rev MariciInt
              (marici-int-negate (marici-int-add
                (marici-int-negate (probe (nima-local-state-15,(marici-succ u,(s,t))))) marici-int-zero))
              (marici-int-negate (marici-int-negate (probe (nima-local-state-15,(marici-succ u,(s,t))))))
              (nima-frame-ap MariciInt MariciInt marici-int-negate
                (marici-int-add (marici-int-negate (probe (nima-local-state-15,(marici-succ u,(s,t))))) marici-int-zero)
                (marici-int-negate (probe (nima-local-state-15,(marici-succ u,(s,t)))))
                (marici-int-add-zero-right (marici-int-negate (probe (nima-local-state-15,(marici-succ u,(s,t))))))))
       | nima-positive-s s t => \ probe -> nima-frame-rev MariciInt
          (marici-int-add (probe (nima-local-state-15,(marici-zero,(marici-succ s,t)))) marici-int-zero)
          (probe (nima-local-state-15,(marici-zero,(marici-succ s,t))))
          (marici-int-add-zero-right (probe (nima-local-state-15,(marici-zero,(marici-succ s,t)))))
       | nima-positive-t t => \ probe -> nima-frame-rev MariciInt
          (marici-int-add (probe (nima-local-state-15,(marici-zero,(marici-zero,marici-succ t)))) marici-int-zero)
          (probe (nima-local-state-15,(marici-zero,(marici-zero,marici-succ t))))
          (marici-int-add-zero-right (probe (nima-local-state-15,(marici-zero,(marici-zero,marici-succ t))))))

#define nima-positive-boundary (p : NimaPositiveUSTCoefficients)
  : nima-sum-equal NimaLocalBasis
      (nima-positive-top p)
      (nima-local-d (nima-positive-primitive p))
  := match p
       (nima-sum-zero => \ probe -> refl
       | nima-sum-atom m => nima-positive-atom-boundary m
       | nima-sum-add x ihx y ihy => \ probe -> nima-cochain-ap2 MariciInt MariciInt MariciInt marici-int-add
          (nima-sum-eval NimaLocalBasis probe (nima-positive-top x))
          (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-positive-primitive x)))
          (nima-sum-eval NimaLocalBasis probe (nima-positive-top y))
          (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-positive-primitive y))) (ihx probe) (ihy probe)
       | nima-sum-neg x ih => \ probe -> nima-frame-ap MariciInt MariciInt marici-int-negate
          (nima-sum-eval NimaLocalBasis probe (nima-positive-top x))
          (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-positive-primitive x))) (ih probe)
       | nima-sum-scale c x ih => \ probe -> nima-frame-ap MariciInt MariciInt (marici-int-mul c)
          (nima-sum-eval NimaLocalBasis probe (nima-positive-top x))
          (nima-sum-eval NimaLocalBasis probe (nima-local-d (nima-positive-primitive x))) (ih probe))
```
