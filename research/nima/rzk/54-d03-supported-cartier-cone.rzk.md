# D03 supported Cartier cone

This module encodes the normalized one-divisor Hom cone

    D(a,b) = (d a, X03*a - d b)

and proves the full supported identity `(Omega',X03*S)=D(S,0)`.  Thus the
ordinary supported-Hom class is null by an exhibited cone primitive, not merely
because `Omega'` is a boundary in the underlying target.

```rzk
#lang rzk-1

#define NimaD03X03Basis : U
  := Sigma (_ : NimaD03SpecializedState), MariciNat
#define NimaD03X03Packet : U := NimaZSum NimaD03X03Basis

#define nima-d03-x03-column : NimaD03X03Basis -> NimaD03X03Packet
  := \ (q,n) -> match q
       (nima-d03-specialized-Omega => nima-sum-zero NimaD03X03Basis
       | nima-d03-specialized-S => nima-sum-atom NimaD03X03Basis
          (nima-d03-specialized-Omega,n)
       | nima-d03-specialized-Hmu => nima-sum-atom NimaD03X03Basis
          (nima-d03-specialized-Omega,n))

#define nima-d03-x03-d : NimaD03X03Packet -> NimaD03X03Packet
  := nima-sum-bind NimaD03X03Basis NimaD03X03Basis nima-d03-x03-column

#define nima-d03-x03-multiply-column : NimaD03X03Basis -> NimaD03X03Packet
  := \ (q,n) -> nima-sum-atom NimaD03X03Basis (q,marici-succ n)
#define nima-d03-x03-multiply : NimaD03X03Packet -> NimaD03X03Packet
  := nima-sum-bind NimaD03X03Basis NimaD03X03Basis
       nima-d03-x03-multiply-column

#define nima-d03-x03-Omega : NimaD03X03Packet
  := nima-sum-atom NimaD03X03Basis
       (nima-d03-specialized-Omega,marici-zero)
#define nima-d03-x03-S : NimaD03X03Packet
  := nima-sum-atom NimaD03X03Basis
       (nima-d03-specialized-S,marici-zero)

#define NimaD03SupportedCone : U
  := Sigma (_ : NimaD03X03Packet), NimaD03X03Packet

#define nima-d03-supported-cone-d
  : NimaD03SupportedCone -> NimaD03SupportedCone
  := \ (a,b) ->
       (nima-d03-x03-d a,
        nima-sum-add NimaD03X03Basis (nima-d03-x03-multiply a)
          (nima-sum-neg NimaD03X03Basis (nima-d03-x03-d b)))

#define NimaD03SupportedConeEqual
  (x y : NimaD03SupportedCone) : U
  := let (a,b) := x in let (a',b') := y in
     Sigma (_ : nima-sum-equal NimaD03X03Basis a a'),
       nima-sum-equal NimaD03X03Basis b b'

#define nima-d03-supported-primary : NimaD03SupportedCone
  := (nima-d03-x03-Omega,nima-d03-x03-multiply nima-d03-x03-S)
#define nima-d03-supported-primitive : NimaD03SupportedCone
  := (nima-d03-x03-S,nima-sum-zero NimaD03X03Basis)

#define nima-d03-supported-cone-second-identity
  : nima-sum-equal NimaD03X03Basis
      (nima-sum-add NimaD03X03Basis
        (nima-d03-x03-multiply nima-d03-x03-S)
        (nima-sum-neg NimaD03X03Basis
          (nima-d03-x03-d (nima-sum-zero NimaD03X03Basis))))
      (nima-d03-x03-multiply nima-d03-x03-S)
  := \ probe -> nima-frame-concat MariciInt
       (nima-sum-eval NimaD03X03Basis probe
         (nima-sum-add NimaD03X03Basis
          (nima-d03-x03-multiply nima-d03-x03-S)
          (nima-sum-neg NimaD03X03Basis
            (nima-d03-x03-d (nima-sum-zero NimaD03X03Basis)))))
       (nima-sum-eval NimaD03X03Basis probe
         (nima-sum-add NimaD03X03Basis
          (nima-d03-x03-multiply nima-d03-x03-S)
          (nima-sum-zero NimaD03X03Basis)))
       (nima-sum-eval NimaD03X03Basis probe
         (nima-d03-x03-multiply nima-d03-x03-S))
       refl
       (nima-sum-add-right-zero NimaD03X03Basis
         (nima-d03-x03-multiply nima-d03-x03-S) probe)

#define nima-d03-supported-cone-identity
  : NimaD03SupportedConeEqual
      (nima-d03-supported-cone-d nima-d03-supported-primitive)
      nima-d03-supported-primary
  := (\ probe -> refl,nima-d03-supported-cone-second-identity)

#define nima-d03-supported-primary-is-exact
  : NimaD03SupportedConeEqual
      nima-d03-supported-primary
      (nima-d03-supported-cone-d nima-d03-supported-primitive)
  := (\ probe -> refl,
      \ probe -> nima-frame-rev MariciInt
       (nima-sum-eval NimaD03X03Basis probe
         (nima-sum-add NimaD03X03Basis
          (nima-d03-x03-multiply nima-d03-x03-S)
          (nima-sum-neg NimaD03X03Basis
            (nima-d03-x03-d (nima-sum-zero NimaD03X03Basis)))))
       (nima-sum-eval NimaD03X03Basis probe
         (nima-d03-x03-multiply nima-d03-x03-S))
       (nima-d03-supported-cone-second-identity probe))
```
