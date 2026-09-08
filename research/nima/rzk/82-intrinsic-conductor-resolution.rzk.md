# Intrinsic conductor resolution

```rzk
#lang rzk-1

#data NimaIntrinsicConductorResolutionStatus
  := nima-alternating-word-resolution-all-degrees
#define nima-intrinsic-conductor-resolution-status
  : NimaIntrinsicConductorResolutionStatus
  := nima-alternating-word-resolution-all-degrees

#data NimaIntrinsicConductorTorRank
  := nima-conductor-Tor-rank-0-is-1
  | nima-conductor-Tor-rank-1-is-6
  | nima-conductor-Tor-rank-2-is-24
  | nima-conductor-Tor-rank-3-is-92
  | nima-conductor-Tor-rank-4-is-354
  | nima-conductor-Tor-rank-5-is-1362
  | nima-conductor-Tor-rank-6-is-5240

#data NimaIntrinsicS14FibreRank
  := nima-S14-fibre-rank-0-is-43
  | nima-S14-fibre-rank-1-is-168
  | nima-S14-fibre-rank-2-is-644
  | nima-S14-fibre-rank-3-is-2478
  | nima-S14-fibre-rank-4-is-9534
  | nima-S14-fibre-rank-5-is-36680
  | nima-S14-fibre-rank-6-is-141120

#data NimaIntrinsicExceptionalRestrictionStatus
  := nima-exceptional-reverse-conductor-restriction-unbounded-above
#define nima-intrinsic-exceptional-restriction-status
  : NimaIntrinsicExceptionalRestrictionStatus
  := nima-exceptional-reverse-conductor-restriction-unbounded-above

#data NimaIntrinsicFibreEndpointSensitivity
  := nima-isolated-fibre-forgets-endpoint-offdiagonal-residues
  | nima-global-chart-descent-retains-endpoint-extension
#define nima-intrinsic-fibre-endpoint-sensitivity
  : NimaIntrinsicFibreEndpointSensitivity
  := nima-isolated-fibre-forgets-endpoint-offdiagonal-residues

#data NimaIntrinsicS14PerfectionStatus
  := nima-S14-nonperfect-near-conductor
#define nima-intrinsic-S14-perfection-status : NimaIntrinsicS14PerfectionStatus
  := nima-S14-nonperfect-near-conductor
```
