# Endpoint-complete reverse cone

```rzk
#lang rzk-1

#data NimaReverseConeChannel
  := nima-reverse-cone-branch-volume-plus-8
  | nima-reverse-cone-branch-volume-minus-8
  | nima-reverse-cone-conductor-lines-15
#data NimaReverseConeAttachment
  := nima-complete-15-by-16-normalization-attachment
  | nima-incorrect-split-cohomology-object
#define nima-reverse-cone-attachment : NimaReverseConeAttachment
  := nima-complete-15-by-16-normalization-attachment
#data NimaReverseEndpointBlock
  := nima-positive-triple-normal-residue-block
  | nima-negative-triple-normal-residue-block
#data NimaReverseEndpointExtensionStatus
  := nima-reversed-endpoint-extension-nonsplit-with-unchanged-annihilator
#define nima-reverse-endpoint-extension-status : NimaReverseEndpointExtensionStatus
  := nima-reversed-endpoint-extension-nonsplit-with-unchanged-annihilator
```
