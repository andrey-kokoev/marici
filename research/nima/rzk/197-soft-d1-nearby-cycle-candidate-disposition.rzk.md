# Soft D1 nearby-cycle candidate disposition

```rzk
#lang rzk-1
#data NimaSoftD1OrdinaryCrossingDisposition
  := nima-508-ordinary-crossing-comparisons-kill-Tor1
  | nima-ordinary-crossing-cannot-realize-excess-class
#define nima-soft-D1-ordinary-crossing-disposition
  : NimaSoftD1OrdinaryCrossingDisposition
  := nima-ordinary-crossing-cannot-realize-excess-class
#data NimaSoftD1ProperTraceDisposition
  := nima-two-chart-blowup-dualizing-trace-recovers-base
  | nima-proper-trace-repairs-scalar-coefficients
  | nima-proper-trace-does-not-identify-log-endpoint-functor
#define nima-soft-D1-proper-trace-disposition : NimaSoftD1ProperTraceDisposition
  := nima-proper-trace-does-not-identify-log-endpoint-functor
#data NimaSoftD1CoefficientReadoutEvidence
  := nima-physical-readout-chain-map-passed59-checks-in-coefficient-model
#define nima-soft-D1-coefficient-readout-evidence : NimaSoftD1CoefficientReadoutEvidence
  := nima-physical-readout-chain-map-passed59-checks-in-coefficient-model
#data NimaSoftD1RequiredGeometricRoute
  := nima-logarithmic-nearby-cycle-excess-comparison
  | nima-must-retain-conductor-Tor1-class
#define nima-soft-D1-required-geometric-route : NimaSoftD1RequiredGeometricRoute
  := nima-logarithmic-nearby-cycle-excess-comparison
```
