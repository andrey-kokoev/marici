# Physical amplitude witness

A physical amplitude witness combines one simultaneous five-direction lift with
three supported detectors and their residue law.  An inhabitant therefore
produces an actual calibrated amplitude value, not merely an interface.

```rzk
#lang rzk-1

#define nima-physical-amplitude-witness
  (Coefficient Physical Endpoint Cech Normal Group Operation Supported : U)
  (zeroEndpoint : Endpoint) (zeroCech : Cech) (zeroNormal : Normal)
  (zeroGroup : Group) (zeroOperation : Operation)
  (endpointDifference : Coefficient -> Physical -> Endpoint)
  (cechDifference : Coefficient -> Physical -> Cech)
  (normalDifference : Coefficient -> Physical -> Normal)
  (groupDifference : Coefficient -> Physical -> Group)
  (operationDifference : Coefficient -> Physical -> Operation)
  (coefficient : Coefficient)
  (beta : MariciInt)
  (gysin : Physical -> Supported)
  (residue : Supported -> MariciInt)
  : U
  := Sigma (lift : nima-five-direction-physical-lifts
       Coefficient Physical Endpoint Cech Normal Group Operation
       zeroEndpoint zeroCech zeroNormal zeroGroup zeroOperation
       endpointDifference cechDifference normalDifference groupDifference
       operationDifference coefficient),
       Sigma (detectors : nima-three-supported-detectors Supported),
         nima-three-detector-residue-law Supported beta residue detectors

#define nima-physical-amplitude-witness-lift
  (Coefficient Physical Endpoint Cech Normal Group Operation Supported : U)
  (zeroEndpoint : Endpoint) (zeroCech : Cech) (zeroNormal : Normal)
  (zeroGroup : Group) (zeroOperation : Operation)
  (endpointDifference : Coefficient -> Physical -> Endpoint)
  (cechDifference : Coefficient -> Physical -> Cech)
  (normalDifference : Coefficient -> Physical -> Normal)
  (groupDifference : Coefficient -> Physical -> Group)
  (operationDifference : Coefficient -> Physical -> Operation)
  (coefficient : Coefficient) (beta : MariciInt)
  (gysin : Physical -> Supported) (residue : Supported -> MariciInt)
  (witness : nima-physical-amplitude-witness
    Coefficient Physical Endpoint Cech Normal Group Operation Supported
    zeroEndpoint zeroCech zeroNormal zeroGroup zeroOperation
    endpointDifference cechDifference normalDifference groupDifference
    operationDifference coefficient beta gysin residue)
  : Physical
  := first (first witness)

#define nima-physical-amplitude-witness-value
  (Coefficient Physical Endpoint Cech Normal Group Operation Supported : U)
  (zeroEndpoint : Endpoint) (zeroCech : Cech) (zeroNormal : Normal)
  (zeroGroup : Group) (zeroOperation : Operation)
  (endpointDifference : Coefficient -> Physical -> Endpoint)
  (cechDifference : Coefficient -> Physical -> Cech)
  (normalDifference : Coefficient -> Physical -> Normal)
  (groupDifference : Coefficient -> Physical -> Group)
  (operationDifference : Coefficient -> Physical -> Operation)
  (coefficient : Coefficient) (beta : MariciInt)
  (gysin : Physical -> Supported) (residue : Supported -> MariciInt)
  (witness : nima-physical-amplitude-witness
    Coefficient Physical Endpoint Cech Normal Group Operation Supported
    zeroEndpoint zeroCech zeroNormal zeroGroup zeroOperation
    endpointDifference cechDifference normalDifference groupDifference
    operationDifference coefficient beta gysin residue)
  : MariciInt
  := residue (gysin (first (first witness)))

#define nima-physical-amplitude-witness-calibrated
  (Coefficient Physical Endpoint Cech Normal Group Operation Supported : U)
  (zeroEndpoint : Endpoint) (zeroCech : Cech) (zeroNormal : Normal)
  (zeroGroup : Group) (zeroOperation : Operation)
  (endpointDifference : Coefficient -> Physical -> Endpoint)
  (cechDifference : Coefficient -> Physical -> Cech)
  (normalDifference : Coefficient -> Physical -> Normal)
  (groupDifference : Coefficient -> Physical -> Group)
  (operationDifference : Coefficient -> Physical -> Operation)
  (coefficient : Coefficient) (beta : MariciInt)
  (gysin : Physical -> Supported) (residue : Supported -> MariciInt)
  (witness : nima-physical-amplitude-witness
    Coefficient Physical Endpoint Cech Normal Group Operation Supported
    zeroEndpoint zeroCech zeroNormal zeroGroup zeroOperation
    endpointDifference cechDifference normalDifference groupDifference
    operationDifference coefficient beta gysin residue)
  : nima-physical-amplitude-witness-value
      Coefficient Physical Endpoint Cech Normal Group Operation Supported
      zeroEndpoint zeroCech zeroNormal zeroGroup zeroOperation
      endpointDifference cechDifference normalDifference groupDifference
      operationDifference coefficient beta gysin residue witness
    = nima-calibrated-coordinate-amplitude beta
       (nima-three-detector-coordinate-map Supported
         (first (second witness)) (gysin (first (first witness))))
  := second (second witness) (gysin (first (first witness)))

#data NimaPhysicalAmplitudeWitnessStatus
  := nima-complete-relative-witness-type-constructed
  | nima-concrete-physical-inhabitant-not-yet-supplied
#define nima-physical-amplitude-witness-status : NimaPhysicalAmplitudeWitnessStatus
  := nima-complete-relative-witness-type-constructed
```
