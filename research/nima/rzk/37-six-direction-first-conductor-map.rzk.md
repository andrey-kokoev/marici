# Six native directions in the first conductor quotient

The first conductor quotient is presented by its six independent degree-one
occurrence classes. Rees factors remain coefficients; they are not inverted.

```rzk
#lang rzk-1

#data NimaFirstConductorDirection
  := nima-first-conductor-X02
  | nima-first-conductor-X04
  | nima-first-conductor-X24
  | nima-first-conductor-X13
  | nima-first-conductor-X15
  | nima-first-conductor-X35

#data NimaNativeEndpointDirection
  := nima-native-direction-plus-13
  | nima-native-direction-plus-15
  | nima-native-direction-plus-35
  | nima-native-direction-minus-02
  | nima-native-direction-minus-04
  | nima-native-direction-minus-24

#define NimaShortReesMonomial6 : U
  := Sigma (_ : MariciNat), Sigma (_ : MariciNat), Sigma (_ : MariciNat),
     Sigma (_ : MariciNat), Sigma (_ : MariciNat), MariciNat

#define NimaFirstConductorLineBasis : U
  := Sigma (_ : NimaEndpointLine), Sigma (_ : NimaFirstConductorDirection),
       NimaShortReesMonomial6
#define NimaFirstConductorLineModule : U := NimaZSum NimaFirstConductorLineBasis

#define nima-rees-unit-02 : NimaShortReesMonomial6
  := ((marici-succ marici-zero),(marici-zero,(marici-zero,(marici-zero,(marici-zero,marici-zero)))))
#define nima-rees-unit-04 : NimaShortReesMonomial6
  := (marici-zero,((marici-succ marici-zero),(marici-zero,(marici-zero,(marici-zero,marici-zero)))))
#define nima-rees-unit-24 : NimaShortReesMonomial6
  := (marici-zero,(marici-zero,((marici-succ marici-zero),(marici-zero,(marici-zero,marici-zero)))))
#define nima-rees-unit-13 : NimaShortReesMonomial6
  := (marici-zero,(marici-zero,(marici-zero,((marici-succ marici-zero),(marici-zero,marici-zero)))))
#define nima-rees-unit-15 : NimaShortReesMonomial6
  := (marici-zero,(marici-zero,(marici-zero,(marici-zero,((marici-succ marici-zero),marici-zero)))))
#define nima-rees-unit-35 : NimaShortReesMonomial6
  := (marici-zero,(marici-zero,(marici-zero,(marici-zero,(marici-zero,(marici-succ marici-zero))))))

#define nima-six-direction-first-conductor-map
  : NimaNativeEndpointDirection -> NimaFirstConductorLineModule
  := \ q -> match q
       (nima-native-direction-plus-13 =>
          nima-sum-neg NimaFirstConductorLineBasis
            (nima-sum-atom NimaFirstConductorLineBasis
              (nima-endpoint-line-plus,(nima-first-conductor-X13,nima-rees-unit-13)))
       | nima-native-direction-plus-15 =>
          nima-sum-neg NimaFirstConductorLineBasis
            (nima-sum-atom NimaFirstConductorLineBasis
              (nima-endpoint-line-plus,(nima-first-conductor-X15,nima-rees-unit-15)))
       | nima-native-direction-plus-35 =>
          nima-sum-neg NimaFirstConductorLineBasis
            (nima-sum-atom NimaFirstConductorLineBasis
              (nima-endpoint-line-plus,(nima-first-conductor-X35,nima-rees-unit-35)))
       | nima-native-direction-minus-02 =>
          nima-sum-neg NimaFirstConductorLineBasis
            (nima-sum-atom NimaFirstConductorLineBasis
              (nima-endpoint-line-minus,(nima-first-conductor-X02,nima-rees-unit-02)))
       | nima-native-direction-minus-04 =>
          nima-sum-neg NimaFirstConductorLineBasis
            (nima-sum-atom NimaFirstConductorLineBasis
              (nima-endpoint-line-minus,(nima-first-conductor-X04,nima-rees-unit-04)))
       | nima-native-direction-minus-24 =>
          nima-sum-neg NimaFirstConductorLineBasis
            (nima-sum-atom NimaFirstConductorLineBasis
              (nima-endpoint-line-minus,(nima-first-conductor-X24,nima-rees-unit-24))))

#define nima-six-direction-source-count : MariciNat
  := marici-succ (marici-succ (marici-succ (marici-succ (marici-succ (marici-succ marici-zero)))))

#define nima-six-direction-target-slot
  : NimaNativeEndpointDirection -> Sigma (_ : NimaEndpointLine), NimaFirstConductorDirection
  := \ q -> match q
       (nima-native-direction-plus-13 => (nima-endpoint-line-plus,nima-first-conductor-X13)
       | nima-native-direction-plus-15 => (nima-endpoint-line-plus,nima-first-conductor-X15)
       | nima-native-direction-plus-35 => (nima-endpoint-line-plus,nima-first-conductor-X35)
       | nima-native-direction-minus-02 => (nima-endpoint-line-minus,nima-first-conductor-X02)
       | nima-native-direction-minus-04 => (nima-endpoint-line-minus,nima-first-conductor-X04)
       | nima-native-direction-minus-24 => (nima-endpoint-line-minus,nima-first-conductor-X24))

#define nima-six-direction-rees-factor
  : NimaNativeEndpointDirection -> NimaShortReesMonomial6
  := \ q -> match q
       (nima-native-direction-plus-13 => nima-rees-unit-13
       | nima-native-direction-plus-15 => nima-rees-unit-15
       | nima-native-direction-plus-35 => nima-rees-unit-35
       | nima-native-direction-minus-02 => nima-rees-unit-02
       | nima-native-direction-minus-04 => nima-rees-unit-04
       | nima-native-direction-minus-24 => nima-rees-unit-24)
```
