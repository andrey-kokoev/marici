# Native endpoint and four-term Q vectors

This module replaces symbolic projection labels by finite integral vectors with
all endpoint and generic coordinates retained.

```rzk
#lang rzk-1

#data NimaD03QTopState
  := nima-d03-q-top-T
  | nima-d03-q-normal-03
  | nima-d03-q-normal-14
  | nima-d03-q-normal-25
#define NimaD03QTopVector : U := NimaZSum NimaD03QTopState

#define nima-d03-q-four-term-vector : NimaD03QTopVector
  := nima-sum-add NimaD03QTopState
       (nima-sum-atom NimaD03QTopState nima-d03-q-top-T)
       (nima-sum-neg NimaD03QTopState
         (nima-sum-add NimaD03QTopState
          (nima-sum-atom NimaD03QTopState nima-d03-q-normal-03)
          (nima-sum-add NimaD03QTopState
           (nima-sum-atom NimaD03QTopState nima-d03-q-normal-14)
           (nima-sum-atom NimaD03QTopState nima-d03-q-normal-25))))

#define nima-d03-q-top-probe : NimaD03QTopState -> MariciInt
  := \ q -> match q
       (nima-d03-q-top-T => marici-int-one
       | nima-d03-q-normal-03 => marici-int-zero
       | nima-d03-q-normal-14 => marici-int-zero
       | nima-d03-q-normal-25 => marici-int-zero)
#define nima-d03-q-four-term-top-value
  : nima-sum-eval NimaD03QTopState nima-d03-q-top-probe
      nima-d03-q-four-term-vector = marici-int-one
  := refl

#data NimaD03QLowerState
  := nima-d03-q-facet-03
  | nima-d03-q-facet-14
  | nima-d03-q-facet-25
#define NimaD03QLowerVector : U := NimaZSum NimaD03QLowerState

#define nima-d03-q-radial-sum : NimaD03QLowerVector
  := nima-sum-add NimaD03QLowerState
       (nima-sum-atom NimaD03QLowerState nima-d03-q-facet-03)
       (nima-sum-add NimaD03QLowerState
        (nima-sum-atom NimaD03QLowerState nima-d03-q-facet-14)
        (nima-sum-atom NimaD03QLowerState nima-d03-q-facet-25))

#define nima-d03-q-boundary-column
  : NimaD03QTopState -> NimaD03QLowerVector
  := \ q -> match q
       (nima-d03-q-top-T => nima-d03-q-radial-sum
       | nima-d03-q-normal-03 => nima-sum-atom NimaD03QLowerState
          nima-d03-q-facet-03
       | nima-d03-q-normal-14 => nima-sum-atom NimaD03QLowerState
          nima-d03-q-facet-14
       | nima-d03-q-normal-25 => nima-sum-atom NimaD03QLowerState
          nima-d03-q-facet-25)
#define nima-d03-q-boundary : NimaD03QTopVector -> NimaD03QLowerVector
  := nima-sum-bind NimaD03QTopState NimaD03QLowerState
       nima-d03-q-boundary-column

#define nima-d03-q-four-term-cycle
  : nima-sum-equal NimaD03QLowerState
      (nima-d03-q-boundary nima-d03-q-four-term-vector)
      (nima-sum-zero NimaD03QLowerState)
  := nima-sum-add-inverse NimaD03QLowerState nima-d03-q-radial-sum

#data NimaD03EndpointTopState
  := nima-d03-endpoint-minus-top
  | nima-d03-endpoint-plus-occurrence-top
#define NimaD03EndpointTopVector : U := NimaZSum NimaD03EndpointTopState
#define nima-d03-endpoint-vector : NimaD03EndpointTopVector
  := nima-sum-add NimaD03EndpointTopState
       (nima-sum-atom NimaD03EndpointTopState nima-d03-endpoint-minus-top)
       (nima-sum-atom NimaD03EndpointTopState
         nima-d03-endpoint-plus-occurrence-top)

#data NimaD03EndpointConnectorState
  := nima-d03-connector-minus-02
  | nima-d03-connector-minus-04
  | nima-d03-connector-minus-24
  | nima-d03-connector-plus-13
  | nima-d03-connector-plus-15
  | nima-d03-connector-plus-35
#define NimaD03EndpointConnectorVector : U
  := NimaZSum NimaD03EndpointConnectorState

#define nima-d03-endpoint-connector-column
  : NimaD03EndpointTopState -> NimaD03EndpointConnectorVector
  := \ q -> match q
       (nima-d03-endpoint-minus-top =>
          nima-sum-add NimaD03EndpointConnectorState
           (nima-sum-atom NimaD03EndpointConnectorState
             nima-d03-connector-minus-02)
           (nima-sum-add NimaD03EndpointConnectorState
            (nima-sum-atom NimaD03EndpointConnectorState
              nima-d03-connector-minus-04)
            (nima-sum-atom NimaD03EndpointConnectorState
              nima-d03-connector-minus-24))
       | nima-d03-endpoint-plus-occurrence-top =>
          nima-sum-add NimaD03EndpointConnectorState
           (nima-sum-atom NimaD03EndpointConnectorState
             nima-d03-connector-plus-13)
           (nima-sum-add NimaD03EndpointConnectorState
            (nima-sum-atom NimaD03EndpointConnectorState
              nima-d03-connector-plus-15)
            (nima-sum-atom NimaD03EndpointConnectorState
              nima-d03-connector-plus-35)))

#define nima-d03-endpoint-connector
  : NimaD03EndpointTopVector -> NimaD03EndpointConnectorVector
  := nima-sum-bind NimaD03EndpointTopState NimaD03EndpointConnectorState
       nima-d03-endpoint-connector-column

#define nima-d03-Z-q-projection-column
  : NimaD03SpecializedState -> NimaD03QTopVector
  := \ q -> match q
       (nima-d03-specialized-Omega => nima-sum-zero NimaD03QTopState
       | nima-d03-specialized-S => nima-sum-zero NimaD03QTopState
       | nima-d03-specialized-Hmu => nima-d03-q-four-term-vector)
#define nima-d03-Z-q-projection
  : NimaD03SpecializedPacket -> NimaD03QTopVector
  := nima-sum-bind NimaD03SpecializedState NimaD03QTopState
       nima-d03-Z-q-projection-column

#define nima-d03-Z-endpoint-projection-column
  : NimaD03SpecializedState -> NimaD03EndpointTopVector
  := \ q -> match q
       (nima-d03-specialized-Omega => nima-sum-zero NimaD03EndpointTopState
       | nima-d03-specialized-S => nima-sum-zero NimaD03EndpointTopState
       | nima-d03-specialized-Hmu => nima-d03-endpoint-vector)
#define nima-d03-Z-endpoint-projection
  : NimaD03SpecializedPacket -> NimaD03EndpointTopVector
  := nima-sum-bind NimaD03SpecializedState NimaD03EndpointTopState
       nima-d03-Z-endpoint-projection-column

#define nima-d03-Z-has-four-term-q-projection
  : nima-sum-equal NimaD03QTopState
      (nima-d03-Z-q-projection nima-d03-specialized-Z-chain)
      nima-d03-q-four-term-vector
  := \ probe -> nima-frame-concat MariciInt
       (nima-sum-eval NimaD03QTopState probe
         (nima-d03-Z-q-projection nima-d03-specialized-Z-chain))
       (nima-sum-eval NimaD03QTopState probe
         (nima-sum-add NimaD03QTopState nima-d03-q-four-term-vector
           (nima-sum-zero NimaD03QTopState)))
       (nima-sum-eval NimaD03QTopState probe nima-d03-q-four-term-vector)
       refl
       (nima-sum-add-right-zero NimaD03QTopState
         nima-d03-q-four-term-vector probe)

#define nima-d03-Z-has-two-endpoint-components
  : nima-sum-equal NimaD03EndpointTopState
      (nima-d03-Z-endpoint-projection nima-d03-specialized-Z-chain)
      nima-d03-endpoint-vector
  := \ probe -> nima-frame-concat MariciInt
       (nima-sum-eval NimaD03EndpointTopState probe
         (nima-d03-Z-endpoint-projection nima-d03-specialized-Z-chain))
       (nima-sum-eval NimaD03EndpointTopState probe
         (nima-sum-add NimaD03EndpointTopState nima-d03-endpoint-vector
           (nima-sum-zero NimaD03EndpointTopState)))
       (nima-sum-eval NimaD03EndpointTopState probe nima-d03-endpoint-vector)
       refl
       (nima-sum-add-right-zero NimaD03EndpointTopState
         nima-d03-endpoint-vector probe)
```
