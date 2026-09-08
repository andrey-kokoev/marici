# Supported local residue and primitive top class

The residue selects the constant `(u,s,t)=(0,0,0)` coefficient of the unique
degree-one state.  It is a detector, not an assumed quotient computation.

```rzk
#lang rzk-1

#define nima-local-residue-probe : NimaLocalBasis -> MariciInt
  := \ (q,(u,(s,t))) -> (match q into (\ _ -> MariciNat -> MariciNat -> MariciNat -> MariciInt) (
    nima-local-state-0 => \ _ _ _ -> marici-int-zero
  | nima-local-state-1 => \ _ _ _ -> marici-int-zero
  | nima-local-state-2 => \ _ _ _ -> marici-int-zero
  | nima-local-state-3 => \ _ _ _ -> marici-int-zero
  | nima-local-state-4 => \ _ _ _ -> marici-int-zero
  | nima-local-state-5 => \ _ _ _ -> marici-int-zero
  | nima-local-state-6 => \ _ _ _ -> marici-int-zero
  | nima-local-state-7 => \ _ _ _ -> marici-int-zero
  | nima-local-state-8 => \ _ _ _ -> marici-int-zero
  | nima-local-state-9 => \ _ _ _ -> marici-int-zero
  | nima-local-state-10 => \ _ _ _ -> marici-int-zero
  | nima-local-state-11 => \ _ _ _ -> marici-int-zero
  | nima-local-state-12 => \ _ _ _ -> marici-int-zero
  | nima-local-state-13 => \ _ _ _ -> marici-int-zero
  | nima-local-state-14 => \ _ _ _ -> marici-int-zero
  | nima-local-state-15 => \ u' s' t' -> match u'
      (marici-zero => match s'
        (marici-zero => match t' (marici-zero => marici-int-one | marici-succ _ _ => marici-int-zero)
        | marici-succ _ _ => marici-int-zero)
      | marici-succ _ _ => marici-int-zero)
  )) u s t

#define nima-local-residue (p : NimaLocalCoefficients) : MariciInt
  := nima-sum-eval NimaLocalBasis nima-local-residue-probe p

#define nima-local-eval-zero-atoms
  (probe : NimaLocalBasis -> MariciInt)
  (zero-atoms : (a : NimaLocalBasis) -> probe a = marici-int-zero)
  (p : NimaLocalCoefficients)
  : nima-sum-eval NimaLocalBasis probe p = marici-int-zero
  := match p
       (nima-sum-zero => refl
       | nima-sum-atom a => zero-atoms a
       | nima-sum-add x ihx y ihy => nima-cochain-ap2 MariciInt MariciInt MariciInt marici-int-add
           (nima-sum-eval NimaLocalBasis probe x) marici-int-zero
           (nima-sum-eval NimaLocalBasis probe y) marici-int-zero ihx ihy
       | nima-sum-neg x ih => nima-frame-ap MariciInt MariciInt marici-int-negate
           (nima-sum-eval NimaLocalBasis probe x) marici-int-zero ih
       | nima-sum-scale c x ih => nima-frame-concat MariciInt
           (marici-int-mul c (nima-sum-eval NimaLocalBasis probe x))
           (marici-int-mul c marici-int-zero) marici-int-zero
           (nima-frame-ap MariciInt MariciInt (marici-int-mul c)
             (nima-sum-eval NimaLocalBasis probe x) marici-int-zero ih)
           (marici-int-mul-zero-right c))

#define nima-local-column-residue-zero : (a : NimaLocalBasis) ->
  nima-local-residue (nima-local-column a) = marici-int-zero
  := \ (q,(u,(s,t))) -> (match q into (\ k -> (u' s' t' : MariciNat) ->
       nima-local-residue (nima-local-column (k,(u',(s',t')))) = marici-int-zero) (
    nima-local-state-0 => \ u' s' t' -> refl
  | nima-local-state-1 => \ u' s' t' -> refl
  | nima-local-state-2 => \ u' s' t' -> refl
  | nima-local-state-3 => \ u' s' t' -> refl
  | nima-local-state-4 => \ u' s' t' -> refl
  | nima-local-state-5 => \ u' s' t' -> refl
  | nima-local-state-6 => \ u' s' t' -> refl
  | nima-local-state-7 => \ u' s' t' -> refl
  | nima-local-state-8 => \ u' s' t' -> refl
  | nima-local-state-9 => \ u' s' t' -> refl
  | nima-local-state-10 => \ u' s' t' -> match u' (marici-zero => refl | marici-succ k _ => refl)
  | nima-local-state-11 => \ u' s' t' -> match u'
      (marici-zero => match s' (marici-zero => match t' (marici-zero => refl | marici-succ k _ => refl) | marici-succ k _ => refl)
      | marici-succ k _ => refl)
  | nima-local-state-12 => \ u' s' t' -> match u'
      (marici-zero => match s' (marici-zero => refl | marici-succ k _ => refl)
      | marici-succ k _ => refl)
  | nima-local-state-13 => \ u' s' t' -> match u'
      (marici-zero => match s' (marici-zero => match t' (marici-zero => refl | marici-succ k _ => refl) | marici-succ k _ => refl)
      | marici-succ k _ => refl)
  | nima-local-state-14 => \ u' s' t' -> match u'
      (marici-zero => match s' (marici-zero => refl | marici-succ k _ => refl)
      | marici-succ k _ => refl)
  | nima-local-state-15 => \ u' s' t' -> refl
  )) u s t

#define nima-local-boundary-residue-zero (p : NimaLocalCoefficients)
  : nima-local-residue (nima-local-d p) = marici-int-zero
  := nima-frame-concat MariciInt
       (nima-local-residue (nima-local-d p))
       (nima-sum-eval NimaLocalBasis (\ a -> nima-local-residue (nima-local-column a)) p)
       marici-int-zero
       (nima-sum-eval-bind NimaLocalBasis NimaLocalBasis nima-local-column nima-local-residue-probe p)
       (nima-local-eval-zero-atoms
         (\ a -> nima-local-residue (nima-local-column a))
         nima-local-column-residue-zero p)

#define nima-local-tau : NimaLocalCoefficients
  := nima-sum-atom NimaLocalBasis
       (nima-local-state-15,(marici-zero,(marici-zero,marici-zero)))

#define nima-local-tau-residue
  : nima-local-residue nima-local-tau = marici-int-one := refl

#define nima-local-tau-not-boundary
  (p : NimaLocalCoefficients)
  (boundary : nima-sum-equal NimaLocalBasis (nima-local-d p) nima-local-tau)
  : marici-int-zero = marici-int-one
  := nima-frame-concat MariciInt marici-int-zero
       (nima-local-residue (nima-local-d p)) marici-int-one
       (nima-frame-rev MariciInt (nima-local-residue (nima-local-d p)) marici-int-zero
         (nima-local-boundary-residue-zero p))
       (boundary nima-local-residue-probe)
```
