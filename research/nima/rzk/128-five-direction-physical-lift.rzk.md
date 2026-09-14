# Five-direction physical lift

The totalized comparison coherence is expanded into endpoint, Cech, normal,
group, and operation equations.  A physical lift must solve all five for one
and the same physical point.

```rzk
#lang rzk-1

#define nima-five-direction-comparison-coherence
  (Coefficient Physical Endpoint Cech Normal Group Operation : U)
  (zeroEndpoint : Endpoint) (zeroCech : Cech) (zeroNormal : Normal)
  (zeroGroup : Group) (zeroOperation : Operation)
  (endpointDifference : Coefficient -> Physical -> Endpoint)
  (cechDifference : Coefficient -> Physical -> Cech)
  (normalDifference : Coefficient -> Physical -> Normal)
  (groupDifference : Coefficient -> Physical -> Group)
  (operationDifference : Coefficient -> Physical -> Operation)
  (coefficient : Coefficient) (physical : Physical)
  : U
  := Sigma (_ : endpointDifference coefficient physical = zeroEndpoint),
       Sigma (_ : cechDifference coefficient physical = zeroCech),
       Sigma (_ : normalDifference coefficient physical = zeroNormal),
       Sigma (_ : groupDifference coefficient physical = zeroGroup),
         operationDifference coefficient physical = zeroOperation

#define nima-five-direction-physical-lifts
  (Coefficient Physical Endpoint Cech Normal Group Operation : U)
  (zeroEndpoint : Endpoint) (zeroCech : Cech) (zeroNormal : Normal)
  (zeroGroup : Group) (zeroOperation : Operation)
  (endpointDifference : Coefficient -> Physical -> Endpoint)
  (cechDifference : Coefficient -> Physical -> Cech)
  (normalDifference : Coefficient -> Physical -> Normal)
  (groupDifference : Coefficient -> Physical -> Group)
  (operationDifference : Coefficient -> Physical -> Operation)
  (coefficient : Coefficient)
  : U
  := Sigma (physical : Physical),
       nima-five-direction-comparison-coherence
         Coefficient Physical Endpoint Cech Normal Group Operation
         zeroEndpoint zeroCech zeroNormal zeroGroup zeroOperation
         endpointDifference cechDifference normalDifference groupDifference
         operationDifference coefficient physical

#define nima-five-direction-lift
  (Coefficient Physical Endpoint Cech Normal Group Operation : U)
  (zeroEndpoint : Endpoint) (zeroCech : Cech) (zeroNormal : Normal)
  (zeroGroup : Group) (zeroOperation : Operation)
  (endpointDifference : Coefficient -> Physical -> Endpoint)
  (cechDifference : Coefficient -> Physical -> Cech)
  (normalDifference : Coefficient -> Physical -> Normal)
  (groupDifference : Coefficient -> Physical -> Group)
  (operationDifference : Coefficient -> Physical -> Operation)
  (coefficient : Coefficient) (physical : Physical)
  (endpointCoherence : endpointDifference coefficient physical = zeroEndpoint)
  (cechCoherence : cechDifference coefficient physical = zeroCech)
  (normalCoherence : normalDifference coefficient physical = zeroNormal)
  (groupCoherence : groupDifference coefficient physical = zeroGroup)
  (operationCoherence : operationDifference coefficient physical = zeroOperation)
  : nima-five-direction-physical-lifts
      Coefficient Physical Endpoint Cech Normal Group Operation
      zeroEndpoint zeroCech zeroNormal zeroGroup zeroOperation
      endpointDifference cechDifference normalDifference groupDifference
      operationDifference coefficient
  := (physical,
      (endpointCoherence,
       (cechCoherence,
        (normalCoherence, (groupCoherence, operationCoherence)))))

#define nima-five-direction-lift-physical
  (Coefficient Physical Endpoint Cech Normal Group Operation : U)
  (zeroEndpoint : Endpoint) (zeroCech : Cech) (zeroNormal : Normal)
  (zeroGroup : Group) (zeroOperation : Operation)
  (endpointDifference : Coefficient -> Physical -> Endpoint)
  (cechDifference : Coefficient -> Physical -> Cech)
  (normalDifference : Coefficient -> Physical -> Normal)
  (groupDifference : Coefficient -> Physical -> Group)
  (operationDifference : Coefficient -> Physical -> Operation)
  (coefficient : Coefficient)
  (lift : nima-five-direction-physical-lifts
    Coefficient Physical Endpoint Cech Normal Group Operation
    zeroEndpoint zeroCech zeroNormal zeroGroup zeroOperation
    endpointDifference cechDifference normalDifference groupDifference
    operationDifference coefficient)
  : Physical
  := first lift

#define nima-five-direction-lift-amplitude
  (Coefficient Physical Endpoint Cech Normal Group Operation Supported Scalars : U)
  (zeroEndpoint : Endpoint) (zeroCech : Cech) (zeroNormal : Normal)
  (zeroGroup : Group) (zeroOperation : Operation)
  (endpointDifference : Coefficient -> Physical -> Endpoint)
  (cechDifference : Coefficient -> Physical -> Cech)
  (normalDifference : Coefficient -> Physical -> Normal)
  (groupDifference : Coefficient -> Physical -> Group)
  (operationDifference : Coefficient -> Physical -> Operation)
  (coefficient : Coefficient)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (lift : nima-five-direction-physical-lifts
    Coefficient Physical Endpoint Cech Normal Group Operation
    zeroEndpoint zeroCech zeroNormal zeroGroup zeroOperation
    endpointDifference cechDifference normalDifference groupDifference
    operationDifference coefficient)
  : Scalars
  := residue (gysin (first lift))

#data NimaFiveDirectionLiftGate
  := nima-one-physical-point-must-solve-all-five-directions
  | nima-endpoint-only-lift-insufficient
  | nima-operation-and-group-coherences-not-optional
#define nima-five-direction-lift-gate : NimaFiveDirectionLiftGate
  := nima-one-physical-point-must-solve-all-five-directions
```
