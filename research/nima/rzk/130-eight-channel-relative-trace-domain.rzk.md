# Eight-channel source-relative trace domain

```rzk
#lang rzk-1
#data NimaRelativeTraceChannel
  := nima-trace-13-primary
  | nima-trace-13-excess
  | nima-trace-15-primary
  | nima-trace-15-excess
  | nima-trace-35-primary
  | nima-trace-35-excess
  | nima-trace-135-primary
  | nima-trace-135-excess
#data NimaRelativeTraceDegree
  := nima-relative-trace-degree-minus-4
  | nima-relative-trace-degree-minus-5
  | nima-relative-trace-degree-minus-6
#define nima-relative-trace-degree
  : NimaRelativeTraceChannel -> NimaRelativeTraceDegree
  := \ channel -> match channel
       (nima-trace-13-primary => nima-relative-trace-degree-minus-4
       | nima-trace-13-excess => nima-relative-trace-degree-minus-5
       | nima-trace-15-primary => nima-relative-trace-degree-minus-4
       | nima-trace-15-excess => nima-relative-trace-degree-minus-5
       | nima-trace-35-primary => nima-relative-trace-degree-minus-4
       | nima-trace-35-excess => nima-relative-trace-degree-minus-5
       | nima-trace-135-primary => nima-relative-trace-degree-minus-5
       | nima-trace-135-excess => nima-relative-trace-degree-minus-6)
#data NimaRelativeTraceMatrixShape
  := nima-45-closed-cap-terms-on-18-source-columns
  | nima-43-unclosed-terms-plus-two-corrections
  | nima-six-term-endpoint-differential
#define nima-relative-trace-matrix-shape : NimaRelativeTraceMatrixShape
  := nima-45-closed-cap-terms-on-18-source-columns
#data NimaRelativeTraceCohomology
  := nima-Hom-K-E-Q-each-one-integral-degree-four-class
  | nima-Hom-short-and-endpoint-support-acyclic
  | nima-fixed-generic-class-relative-lift-contractible
#define nima-relative-trace-cohomology : NimaRelativeTraceCohomology
  := nima-fixed-generic-class-relative-lift-contractible
#data NimaRelativeTraceFramePolicy
  := nima-output-coefficient-matrices-equal
  | nima-distinct-input-frames-not-identified
  | nima-physical-reflection-parity-unassigned
#define nima-relative-trace-frame-policy : NimaRelativeTraceFramePolicy
  := nima-distinct-input-frames-not-identified
#data NimaRelativeTraceReplayStatus
  := nima-source-relative-replay-423648
  | nima-physical-endpoint-replay-824081
#define nima-relative-trace-replay-status : NimaRelativeTraceReplayStatus
  := nima-source-relative-replay-423648
```
