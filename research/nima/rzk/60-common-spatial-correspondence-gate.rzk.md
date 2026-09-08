# Common spatial-correspondence factorization gate

This module records two decisive finite consequences: the factorized generic
map has an explicit nullhomotopy even after retaining the Gysin frame, and the
smaller chamber/long-facet projection is not a chain map because it discards
the mixed faces of an actual triangle.

```rzk
#lang rzk-1

#data NimaSpatialGenericState
  := nima-spatial-generic-roof
  | nima-spatial-generic-Morse-homotopy
#define NimaSpatialGenericPacket : U := NimaZSum NimaSpatialGenericState

#define nima-spatial-generic-column
  : NimaSpatialGenericState -> NimaSpatialGenericPacket
  := \ q -> match q
       (nima-spatial-generic-roof => nima-sum-zero NimaSpatialGenericState
       | nima-spatial-generic-Morse-homotopy =>
          nima-sum-atom NimaSpatialGenericState nima-spatial-generic-roof)
#define nima-spatial-generic-d
  : NimaSpatialGenericPacket -> NimaSpatialGenericPacket
  := nima-sum-bind NimaSpatialGenericState NimaSpatialGenericState
       nima-spatial-generic-column

#define nima-spatial-generic-map : NimaSpatialGenericPacket
  := nima-sum-atom NimaSpatialGenericState nima-spatial-generic-roof
#define nima-spatial-generic-nullhomotopy : NimaSpatialGenericPacket
  := nima-sum-atom NimaSpatialGenericState nima-spatial-generic-Morse-homotopy
#define nima-spatial-generic-map-is-nullhomotopic
  : nima-sum-equal NimaSpatialGenericState
      (nima-spatial-generic-d nima-spatial-generic-nullhomotopy)
      nima-spatial-generic-map
  := \ probe -> refl

#define NimaGysinFramedSpatialGeneric : U
  := Sigma (_ : NimaCentralGysinFrame), NimaSpatialGenericPacket
#define nima-gysin-framed-spatial-generic-map : NimaGysinFramedSpatialGeneric
  := (nima-central-gysin-degree-three-dual-determinant,
      nima-spatial-generic-map)
#define nima-gysin-framed-spatial-nullhomotopy : NimaGysinFramedSpatialGeneric
  := (nima-central-gysin-degree-three-dual-determinant,
      nima-spatial-generic-nullhomotopy)
#define nima-gysin-framed-spatial-d
  : NimaGysinFramedSpatialGeneric -> NimaGysinFramedSpatialGeneric
  := \ (frame,p) -> (frame,nima-spatial-generic-d p)
#define NimaGysinFramedSpatialEqual
  (x y : NimaGysinFramedSpatialGeneric) : U
  := let (frame,p) := x in let (frame',p') := y in
     Sigma (_ : frame = frame'),
       nima-sum-equal NimaSpatialGenericState p p'
#define nima-gysin-frame-does-not-remove-nullhomotopy
  : NimaGysinFramedSpatialEqual
      (nima-gysin-framed-spatial-d nima-gysin-framed-spatial-nullhomotopy)
      nima-gysin-framed-spatial-generic-map
  := (refl,\ probe -> refl)

#data NimaMixedFlagTriangleState
  := nima-mixed-flag-triangle
  | nima-mixed-flag-D03-c
  | nima-mixed-flag-o-c
  | nima-mixed-flag-o-D03
#define NimaMixedFlagPacket : U := NimaZSum NimaMixedFlagTriangleState

#define nima-mixed-flag-boundary-column
  : NimaMixedFlagTriangleState -> NimaMixedFlagPacket
  := \ q -> match q
       (nima-mixed-flag-triangle =>
          nima-sum-add NimaMixedFlagTriangleState
           (nima-sum-atom NimaMixedFlagTriangleState nima-mixed-flag-D03-c)
           (nima-sum-add NimaMixedFlagTriangleState
            (nima-sum-neg NimaMixedFlagTriangleState
              (nima-sum-atom NimaMixedFlagTriangleState nima-mixed-flag-o-c))
            (nima-sum-atom NimaMixedFlagTriangleState nima-mixed-flag-o-D03))
       | nima-mixed-flag-D03-c => nima-sum-zero NimaMixedFlagTriangleState
       | nima-mixed-flag-o-c => nima-sum-zero NimaMixedFlagTriangleState
       | nima-mixed-flag-o-D03 => nima-sum-zero NimaMixedFlagTriangleState)
#define nima-mixed-flag-boundary : NimaMixedFlagPacket -> NimaMixedFlagPacket
  := nima-sum-bind NimaMixedFlagTriangleState NimaMixedFlagTriangleState
       nima-mixed-flag-boundary-column

#data NimaWrongGenericState := nima-wrong-generic-edge-o-D03
#define NimaWrongGenericPacket : U := NimaZSum NimaWrongGenericState
#define nima-wrong-generic-projection-column
  : NimaMixedFlagTriangleState -> NimaWrongGenericPacket
  := \ q -> match q
       (nima-mixed-flag-triangle => nima-sum-zero NimaWrongGenericState
       | nima-mixed-flag-D03-c => nima-sum-zero NimaWrongGenericState
       | nima-mixed-flag-o-c => nima-sum-zero NimaWrongGenericState
       | nima-mixed-flag-o-D03 =>
          nima-sum-atom NimaWrongGenericState nima-wrong-generic-edge-o-D03)
#define nima-wrong-generic-projection
  : NimaMixedFlagPacket -> NimaWrongGenericPacket
  := nima-sum-bind NimaMixedFlagTriangleState NimaWrongGenericState
       nima-wrong-generic-projection-column

#define nima-mixed-triangle : NimaMixedFlagPacket
  := nima-sum-atom NimaMixedFlagTriangleState nima-mixed-flag-triangle
#define nima-wrong-projection-chain-defect
  : nima-sum-equal NimaWrongGenericState
      (nima-wrong-generic-projection
        (nima-mixed-flag-boundary nima-mixed-triangle))
      (nima-sum-atom NimaWrongGenericState nima-wrong-generic-edge-o-D03)
  := \ probe -> refl

#define nima-wrong-edge-probe : NimaWrongGenericState -> MariciInt
  := \ edge -> marici-int-one
#define nima-wrong-projection-defect-is-unit
  : nima-sum-eval NimaWrongGenericState nima-wrong-edge-probe
      (nima-wrong-generic-projection
        (nima-mixed-flag-boundary nima-mixed-triangle)) = marici-int-one
  := refl

#define nima-wrong-generic-d : NimaWrongGenericPacket -> NimaWrongGenericPacket
  := \ p -> nima-sum-zero NimaWrongGenericState

#define nima-wrong-projection-cannot-be-chain-map
  (commutes : nima-sum-equal NimaWrongGenericState
    (nima-wrong-generic-projection
      (nima-mixed-flag-boundary nima-mixed-triangle))
    (nima-wrong-generic-d
      (nima-wrong-generic-projection nima-mixed-triangle)))
  : marici-int-zero = marici-int-one
  := nima-frame-concat MariciInt marici-int-zero
       (nima-sum-eval NimaWrongGenericState nima-wrong-edge-probe
         (nima-wrong-generic-projection
           (nima-mixed-flag-boundary nima-mixed-triangle)))
       marici-int-one
       (nima-frame-rev MariciInt
         (nima-sum-eval NimaWrongGenericState nima-wrong-edge-probe
           (nima-wrong-generic-projection
             (nima-mixed-flag-boundary nima-mixed-triangle)))
         marici-int-zero
         (commutes nima-wrong-edge-probe))
       nima-wrong-projection-defect-is-unit
```
