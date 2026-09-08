# Cubical supported-dual critical edge

The complete cubical carrier is indexed by the existing 215 loaded cells.  This
module internalizes its critical relative edge: the forbidden upper endpoint
is relative, so the edge boundary is the negative generic D25 vertex.  With
the product orientation, negating the edge gives the primitive reverse
transgression.

```rzk
#lang rzk-1

#define NimaCubicalSupportedDualCell : U := NimaLoadedCell

#data NimaCriticalRelativeCubeState
  := nima-critical-relative-edge-J
  | nima-critical-generic-D25-vertex
#define NimaCriticalRelativeCube : U := NimaZSum NimaCriticalRelativeCubeState

#define nima-critical-relative-cube-column
  : NimaCriticalRelativeCubeState -> NimaCriticalRelativeCube
  := \ q -> match q
       (nima-critical-relative-edge-J =>
          nima-sum-neg NimaCriticalRelativeCubeState
            (nima-sum-atom NimaCriticalRelativeCubeState
              nima-critical-generic-D25-vertex)
       | nima-critical-generic-D25-vertex =>
          nima-sum-zero NimaCriticalRelativeCubeState)
#define nima-critical-relative-cube-boundary
  : NimaCriticalRelativeCube -> NimaCriticalRelativeCube
  := nima-sum-bind NimaCriticalRelativeCubeState NimaCriticalRelativeCubeState
       nima-critical-relative-cube-column

#define nima-critical-Xi-B : NimaCriticalRelativeCube
  := nima-sum-neg NimaCriticalRelativeCubeState
       (nima-sum-atom NimaCriticalRelativeCubeState
         nima-critical-relative-edge-J)
#define nima-critical-Xi-Q : NimaCriticalRelativeCube
  := nima-sum-atom NimaCriticalRelativeCubeState
       nima-critical-generic-D25-vertex

#define nima-critical-reverse-transgression
  : nima-sum-equal NimaCriticalRelativeCubeState
      (nima-critical-relative-cube-boundary nima-critical-Xi-B)
      nima-critical-Xi-Q
  := \ probe -> marici-int-negate-involutive
       (probe nima-critical-generic-D25-vertex)

#define nima-critical-short-pairing
  : NimaCriticalRelativeCube -> MariciInt
  := nima-sum-eval NimaCriticalRelativeCubeState
       (\ q -> match q
         (nima-critical-relative-edge-J => marici-int-minus-one
         | nima-critical-generic-D25-vertex => marici-int-zero))
#define nima-critical-generic-pairing
  : NimaCriticalRelativeCube -> MariciInt
  := nima-sum-eval NimaCriticalRelativeCubeState
       (\ q -> match q
         (nima-critical-relative-edge-J => marici-int-zero
         | nima-critical-generic-D25-vertex => marici-int-one))

#define nima-critical-Xi-B-pairs-primitively
  : nima-critical-short-pairing nima-critical-Xi-B = marici-int-one
  := refl
#define nima-critical-Xi-Q-pairs-primitively
  : nima-critical-generic-pairing nima-critical-Xi-Q = marici-int-one
  := refl

#data NimaCubicalComplementarySupport
  := nima-cubical-full-W
  | nima-cubical-endpoint-complement-WE
  | nima-cubical-generic-tripod-WQ

#data NimaCubicalDiagonalCompatibility
  := nima-cubical-cap-strictly-coassociative
  | nima-cubical-cap-equals-AW-after-triangulation

#data NimaCubicalEndpointMeridian
  := nima-cubical-positive-endpoint-meridian
  | nima-cubical-negative-endpoint-meridian

#define nima-cubical-endpoint-meridian-value
  : NimaCubicalEndpointMeridian -> MariciInt
  := \ endpoint -> marici-int-one
#define nima-cubical-positive-meridian-primitive
  : nima-cubical-endpoint-meridian-value
      nima-cubical-positive-endpoint-meridian = marici-int-one
  := refl
#define nima-cubical-negative-meridian-primitive
  : nima-cubical-endpoint-meridian-value
      nima-cubical-negative-endpoint-meridian = marici-int-one
  := refl
```
