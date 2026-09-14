# Mixed-kernel physical butterfly gate

```rzk
#lang rzk-1
#define nima-mixed-kernel-physical-butterfly-witness
  (Connector PhysicalGysin SupportedPacket : U)
  (kernel-connector : Connector)
  (selected-physical-gysin : PhysicalGysin)
  (pullback-butterfly : Connector -> PhysicalGysin -> SupportedPacket)
  (selected-packet : SupportedPacket)
  : U
  := pullback-butterfly kernel-connector selected-physical-gysin
       = selected-packet

#define nima-mixed-kernel-image-is-selected-packet
  (Connector PhysicalGysin SupportedPacket : U)
  (kernel-connector : Connector)
  (selected-physical-gysin : PhysicalGysin)
  (pullback-butterfly : Connector -> PhysicalGysin -> SupportedPacket)
  (selected-packet : SupportedPacket)
  (witness : nima-mixed-kernel-physical-butterfly-witness
    Connector PhysicalGysin SupportedPacket kernel-connector
    selected-physical-gysin pullback-butterfly selected-packet)
  : pullback-butterfly kernel-connector selected-physical-gysin = selected-packet
  := witness

#data NimaMixedKernelButterflyInputs
  := nima-fixed-fs-Kato-kernel-connector
  | nima-fixed-road-inclusion
  | nima-selected-physical-Gysin-class
  | nima-selected-supported-packet-a-s-plus-b-W-plus-c-v
#define nima-mixed-kernel-butterfly-inputs : NimaMixedKernelButterflyInputs
  := nima-fixed-fs-Kato-kernel-connector

#data NimaMixedKernelButterflyStatus
  := nima-butterfly-witness-type-constructed
  | nima-ring-generator-specialization-not-required
  | nima-class-level-pullback-equality-still-uninhabited
#define nima-mixed-kernel-butterfly-status : NimaMixedKernelButterflyStatus
  := nima-class-level-pullback-equality-still-uninhabited
```
