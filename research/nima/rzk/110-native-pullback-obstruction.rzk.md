# Native derived-pullback obstruction

```rzk
#lang rzk-1
#data NimaNativePullbackTarget
  := nima-genuine-native-node-module-complex
  | nima-not-conductor-object
  | nima-not-derived-coinduced-ambient-target
#define nima-native-pullback-target : NimaNativePullbackTarget
  := nima-genuine-native-node-module-complex
#data NimaNativeEndpointPrimitive
  := nima-underlying-primitive-coefficient-class-exists
  | nima-no-normalized-native-branch-source-extension
#define nima-native-endpoint-primitive : NimaNativeEndpointPrimitive
  := nima-no-normalized-native-branch-source-extension
#data NimaNativePullbackFirstObstruction
  := nima-resolution-degree-two-mixed-relation
  | nima-primitive-nonzero-Tor-cannot-be-boundary
  | nima-integral-detector-covers-all-replacements
#define nima-native-pullback-first-obstruction
  : NimaNativePullbackFirstObstruction
  := nima-resolution-degree-two-mixed-relation
#data NimaNativePullbackTorRanks
  := nima-Tor-ranks-1-9-18-15-6-1
#data NimaNativePullbackScope
  := nima-direct-derived-pullback-route-falsified
  | nima-other-native-supported-targets-not-excluded
#define nima-native-pullback-scope : NimaNativePullbackScope
  := nima-direct-derived-pullback-route-falsified
```
