# Reverse endpoint Gysin lifts

```rzk
#lang rzk-1

#data NimaReverseEndpointConnectorBehavior
  := nima-reverse-connector-globally-nonzero
  | nima-reverse-connector-zero-on-all-cohomology-sheaves
#define nima-reverse-endpoint-connector-global
  : NimaReverseEndpointConnectorBehavior
  := nima-reverse-connector-globally-nonzero
#define nima-reverse-endpoint-connector-cohomology
  : NimaReverseEndpointConnectorBehavior
  := nima-reverse-connector-zero-on-all-cohomology-sheaves

#data NimaSupportedEndpointPolarity
  := nima-supported-positive-endpoint
  | nima-supported-negative-endpoint
#data NimaSupportedEndpointLiftStatus
  := nima-supported-Gysin-lift-exists
#define nima-supported-endpoint-lift
  : NimaSupportedEndpointPolarity -> NimaSupportedEndpointLiftStatus
  := \ polarity -> nima-supported-Gysin-lift-exists

#data NimaSupportedEndpointLiftSpace
  := nima-nonempty-discrete-torsor-seven-coefficient-families
#define nima-supported-endpoint-lift-space
  : NimaSupportedEndpointPolarity -> NimaSupportedEndpointLiftSpace
  := \ polarity -> nima-nonempty-discrete-torsor-seven-coefficient-families

#data NimaSupportedVersusGlobalEndpointStatus
  := nima-extraordinary-restriction-splits-without-global-splitting
#define nima-supported-versus-global-endpoint-status
  : NimaSupportedVersusGlobalEndpointStatus
  := nima-extraordinary-restriction-splits-without-global-splitting

#data NimaReverseEndpointPhysicalStatus
  := nima-supported-lifts-not-native-physical-connectors
#define nima-reverse-endpoint-physical-status : NimaReverseEndpointPhysicalStatus
  := nima-supported-lifts-not-native-physical-connectors
```
