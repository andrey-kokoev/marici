# Soft D1 Cartier nearby model

```rzk
#lang rzk-1
#data NimaSoftD1NearbyGeometry
  := nima-translated-soft-section-z-zero
  | nima-pushforward-relation-a2-equals-u-times-quadratic
  | nima-generic-locus-b2-not-one
#define nima-soft-D1-nearby-geometry : NimaSoftD1NearbyGeometry
  := nima-translated-soft-section-z-zero
#data NimaSoftD1NearbyMonodromy
  := nima-nearby-rank-two
  | nima-semisimple-eigenvalues-plus-one-minus-one
  | nima-nilpotent-log-rank-zero
#define nima-soft-D1-nearby-monodromy : NimaSoftD1NearbyMonodromy
  := nima-semisimple-eigenvalues-plus-one-minus-one
#data NimaSoftD1NearbyOrientation
  := nima-even-degree-character-plus-one
  | nima-odd-degree-character-minus-one
  | nima-odd-boundary-divisor-three-four
#define nima-soft-D1-nearby-orientation : NimaSoftD1NearbyOrientation
  := nima-odd-degree-character-minus-one
#data NimaSoftD1NearbySupport
  := nima-carrier-monodromy-identity
  | nima-nontrivial-monodromy-in-Cartier-support-framing
  | nima-excluded-support-b-plus-minus-one
#define nima-soft-D1-nearby-support : NimaSoftD1NearbySupport
  := nima-nontrivial-monodromy-in-Cartier-support-framing
#data NimaSoftD1RoadCechStatus
  := nima-local-Cartier-nearby-model-constructed
  | nima-full-exact-complex-nearby-identification-open
#define nima-soft-D1-road-Cech-status : NimaSoftD1RoadCechStatus
  := nima-full-exact-complex-nearby-identification-open
```
