# Voevodsky Cubical Agda interface bridge

This module carries the checked aggregate's principal certificate boundaries
into the Rzk ledger.  Constructors record typed interface evidence, not a
physical packet or filler.

```rzk
#lang rzk-1
#data NimaVoevodskyAggregateClosure
  := nima-agda-safe-cubical-guarded-aggregate-passes
#define nima-voevodsky-aggregate-closure : NimaVoevodskyAggregateClosure
  := nima-agda-safe-cubical-guarded-aggregate-passes

#data NimaSourceEquivalenceCertificate
  := nima-ordinary-pulled-normal-cellular-equivalence
  | nima-endpoint-short-boundary-restrictions-retained
  | nima-corrected-Morse-evaluation-retained
#data NimaQFillingAttachmentCertificate
  := nima-three-zeta-variations-with-diagonal-relation
  | nima-lower-attachment-injective
  | nima-fixed-lower-support-forces-trivial-variation
#define nima-Q-filling-rigidity : NimaQFillingAttachmentCertificate
  := nima-fixed-lower-support-forces-trivial-variation

#data NimaEndpointNormalCubeCertificate
  := nima-64-grade-endpoint-normal-cube
  | nima-full-normal-terminal-contractible
  | nima-positive-negative-primitives-remain-distinct
  | nima-full-multiplication-forgets-primitive-normalization
#define nima-endpoint-normal-cube-certificate
  : NimaEndpointNormalCubeCertificate
  := nima-64-grade-endpoint-normal-cube

#data NimaPhysicalFirstJetCertificate
  := nima-eight-framed-first-jet-cases-pass
  | nima-endpoint-and-conormal-share-top-source-state
  | nima-first-jet-ambiguity-by-Cartier-and-three-endpoint-normals
#define nima-physical-first-jet-certificate : NimaPhysicalFirstJetCertificate
  := nima-eight-framed-first-jet-cases-pass

#data NimaP24DorrohBridgeCertificate
  := nima-reduced-Dorroh-and-P24-low-degree-complexes-isomorphic
  | nima-trace-extension-transports-both-directions
  | nima-unitalization-not-claimed-Q-manifold
#define nima-P24-Dorroh-bridge-certificate : NimaP24DorrohBridgeCertificate
  := nima-trace-extension-transports-both-directions

#data NimaMixedVarianceMateRequirement
  := nima-source-equivalence-and-endpoint-compatibility-required
  | nima-normal-cube-and-external-Tor-placement-required
  | nima-operation-antipode-and-reflection-transport-required
  | nima-support-attachment-and-higher-coherences-required
#define nima-mixed-variance-mate-requirement
  : NimaMixedVarianceMateRequirement
  := nima-support-attachment-and-higher-coherences-required

#data NimaVoevodskyPhysicalPacketStatus
  := nima-partial-packet-is-certificate-boundary
  | nima-physical-bivariant-comparison-unconstructed
  | nima-operation-linear-frame-mate-open
  | nima-final-physical-packet-not-inhabited
#define nima-voevodsky-physical-packet-status
  : NimaVoevodskyPhysicalPacketStatus
  := nima-final-physical-packet-not-inhabited

#data NimaAgdaRzkBridgeScope
  := nima-interfaces-carried-not-proof-term-translated
  | nima-no-physical-filler-promoted
#define nima-agda-Rzk-bridge-scope : NimaAgdaRzkBridgeScope
  := nima-interfaces-carried-not-proof-term-translated
```
