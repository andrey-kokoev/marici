# Endpoint normal annihilators and full-cube forgetting

The six short-normal exponents are ordered `(u_x0,...,u_x5)`. This packet
retains the two endpoint primitive lines and the three legal one-mark witnesses
on each branch. No normal is inverted.

```rzk
#lang rzk-1

#data NimaEndpointNormalState
  := nima-endpoint-normal-e-plus
  | nima-endpoint-normal-e-minus
  | nima-endpoint-normal-m-plus-1
  | nima-endpoint-normal-m-plus-3
  | nima-endpoint-normal-m-plus-5
  | nima-endpoint-normal-m-minus-0
  | nima-endpoint-normal-m-minus-2
  | nima-endpoint-normal-m-minus-4

#define NimaShortNormalMonomial6 : U
  := Sigma (_ : MariciNat), Sigma (_ : MariciNat), Sigma (_ : MariciNat),
     Sigma (_ : MariciNat), Sigma (_ : MariciNat), MariciNat
#define NimaEndpointNormalBasis : U
  := Sigma (_ : NimaEndpointNormalState), NimaShortNormalMonomial6
#define NimaEndpointNormal : U := NimaZSum NimaEndpointNormalBasis

#define nima-short-normal-shift-0 : NimaShortNormalMonomial6 -> NimaShortNormalMonomial6
  := \ (a,(b,(c,(d,(e,f))))) -> (marici-succ a,(b,(c,(d,(e,f)))))
#define nima-short-normal-shift-1 : NimaShortNormalMonomial6 -> NimaShortNormalMonomial6
  := \ (a,(b,(c,(d,(e,f))))) -> (a,(marici-succ b,(c,(d,(e,f)))))
#define nima-short-normal-shift-2 : NimaShortNormalMonomial6 -> NimaShortNormalMonomial6
  := \ (a,(b,(c,(d,(e,f))))) -> (a,(b,(marici-succ c,(d,(e,f)))))
#define nima-short-normal-shift-3 : NimaShortNormalMonomial6 -> NimaShortNormalMonomial6
  := \ (a,(b,(c,(d,(e,f))))) -> (a,(b,(c,(marici-succ d,(e,f)))))
#define nima-short-normal-shift-4 : NimaShortNormalMonomial6 -> NimaShortNormalMonomial6
  := \ (a,(b,(c,(d,(e,f))))) -> (a,(b,(c,(d,(marici-succ e,f)))))
#define nima-short-normal-shift-5 : NimaShortNormalMonomial6 -> NimaShortNormalMonomial6
  := \ (a,(b,(c,(d,(e,f))))) -> (a,(b,(c,(d,(e,marici-succ f)))))

#define nima-endpoint-normal-single
  (q : NimaEndpointNormalState) (m : NimaShortNormalMonomial6)
  : NimaEndpointNormal
  := nima-sum-add NimaEndpointNormalBasis
       (nima-sum-atom NimaEndpointNormalBasis (q,m))
       (nima-sum-zero NimaEndpointNormalBasis)

#define nima-endpoint-normal-column : NimaEndpointNormalBasis -> NimaEndpointNormal
  := \ (q,m) -> (match q into (\ _ -> NimaShortNormalMonomial6 -> NimaEndpointNormal) (
    nima-endpoint-normal-e-plus => \ n -> nima-sum-zero NimaEndpointNormalBasis
  | nima-endpoint-normal-e-minus => \ n -> nima-sum-zero NimaEndpointNormalBasis
  | nima-endpoint-normal-m-plus-1 => \ n -> nima-endpoint-normal-single nima-endpoint-normal-e-plus (nima-short-normal-shift-1 n)
  | nima-endpoint-normal-m-plus-3 => \ n -> nima-endpoint-normal-single nima-endpoint-normal-e-plus (nima-short-normal-shift-3 n)
  | nima-endpoint-normal-m-plus-5 => \ n -> nima-endpoint-normal-single nima-endpoint-normal-e-plus (nima-short-normal-shift-5 n)
  | nima-endpoint-normal-m-minus-0 => \ n -> nima-endpoint-normal-single nima-endpoint-normal-e-minus (nima-short-normal-shift-0 n)
  | nima-endpoint-normal-m-minus-2 => \ n -> nima-endpoint-normal-single nima-endpoint-normal-e-minus (nima-short-normal-shift-2 n)
  | nima-endpoint-normal-m-minus-4 => \ n -> nima-endpoint-normal-single nima-endpoint-normal-e-minus (nima-short-normal-shift-4 n)
  )) m

#define nima-endpoint-normal-d : NimaEndpointNormal -> NimaEndpointNormal
  := nima-sum-bind NimaEndpointNormalBasis NimaEndpointNormalBasis nima-endpoint-normal-column

#define nima-endpoint-normal-column-square : (v : NimaEndpointNormalBasis) ->
  nima-sum-equal NimaEndpointNormalBasis
    (nima-endpoint-normal-d (nima-endpoint-normal-column v))
    (nima-sum-zero NimaEndpointNormalBasis)
  := \ (q,m) -> (match q into (\ k -> (n : NimaShortNormalMonomial6) ->
       nima-sum-equal NimaEndpointNormalBasis
         (nima-endpoint-normal-d (nima-endpoint-normal-column (k,n)))
         (nima-sum-zero NimaEndpointNormalBasis)) (
    nima-endpoint-normal-e-plus => \ n probe -> refl
  | nima-endpoint-normal-e-minus => \ n probe -> refl
  | nima-endpoint-normal-m-plus-1 => \ n probe -> refl
  | nima-endpoint-normal-m-plus-3 => \ n probe -> refl
  | nima-endpoint-normal-m-plus-5 => \ n probe -> refl
  | nima-endpoint-normal-m-minus-0 => \ n probe -> refl
  | nima-endpoint-normal-m-minus-2 => \ n probe -> refl
  | nima-endpoint-normal-m-minus-4 => \ n probe -> refl
  )) m

#define nima-endpoint-normal-square (p : NimaEndpointNormal)
  : nima-sum-equal NimaEndpointNormalBasis
      (nima-endpoint-normal-d (nima-endpoint-normal-d p))
      (nima-sum-zero NimaEndpointNormalBasis)
  := nima-sum-column-square NimaEndpointNormalBasis nima-endpoint-normal-column
       nima-endpoint-normal-column-square p

#define nima-short-normal-delta : NimaShortNormalMonomial6
  := (marici-one,(marici-one,(marici-one,(marici-one,(marici-one,marici-one)))))
#define nima-short-normal-without-1 : NimaShortNormalMonomial6
  := (marici-one,(marici-zero,(marici-one,(marici-one,(marici-one,marici-one)))))
#define nima-short-normal-without-0 : NimaShortNormalMonomial6
  := (marici-zero,(marici-one,(marici-one,(marici-one,(marici-one,marici-one)))))

#define nima-delta-e-plus : NimaEndpointNormal
  := nima-sum-atom NimaEndpointNormalBasis
       (nima-endpoint-normal-e-plus,nima-short-normal-delta)
#define nima-delta-e-minus : NimaEndpointNormal
  := nima-sum-atom NimaEndpointNormalBasis
       (nima-endpoint-normal-e-minus,nima-short-normal-delta)

#define nima-delta-plus-primitive : NimaEndpointNormal
  := nima-sum-atom NimaEndpointNormalBasis
       (nima-endpoint-normal-m-plus-1,nima-short-normal-without-1)
#define nima-delta-minus-primitive : NimaEndpointNormal
  := nima-sum-atom NimaEndpointNormalBasis
       (nima-endpoint-normal-m-minus-0,nima-short-normal-without-0)

#define nima-delta-kills-plus-endpoint
  : nima-sum-equal NimaEndpointNormalBasis
      (nima-endpoint-normal-d nima-delta-plus-primitive) nima-delta-e-plus
  := \ probe -> marici-int-add-zero-right
       (probe (nima-endpoint-normal-e-plus,nima-short-normal-delta))

#define nima-delta-kills-minus-endpoint
  : nima-sum-equal NimaEndpointNormalBasis
      (nima-endpoint-normal-d nima-delta-minus-primitive) nima-delta-e-minus
  := \ probe -> marici-int-add-zero-right
       (probe (nima-endpoint-normal-e-minus,nima-short-normal-delta))
```
