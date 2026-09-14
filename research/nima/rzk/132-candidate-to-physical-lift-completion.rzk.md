# Candidate-to-physical lift completion

The implemented endpoint/native-bar candidate is separated from the two missing
physical directions.  Completion requires road-Cech and physical group/reflection
coherence at the same physical point; these witnesses then assemble the full
five-direction lift.

```rzk
#lang rzk-1

#define nima-endpoint-normal-operation-candidate
  (Coefficient Physical Endpoint Normal Operation : U)
  (zeroEndpoint : Endpoint) (zeroNormal : Normal)
  (zeroOperation : Operation)
  (endpointDifference : Coefficient -> Physical -> Endpoint)
  (normalDifference : Coefficient -> Physical -> Normal)
  (operationDifference : Coefficient -> Physical -> Operation)
  (coefficient : Coefficient)
  : U
  := Sigma (physical : Physical),
       Sigma (_ : endpointDifference coefficient physical = zeroEndpoint),
       Sigma (_ : normalDifference coefficient physical = zeroNormal),
         operationDifference coefficient physical = zeroOperation

#define nima-candidate-physical-completion
  (Coefficient Physical Endpoint Cech Normal Group Operation : U)
  (zeroEndpoint : Endpoint) (zeroCech : Cech) (zeroNormal : Normal)
  (zeroGroup : Group) (zeroOperation : Operation)
  (endpointDifference : Coefficient -> Physical -> Endpoint)
  (cechDifference : Coefficient -> Physical -> Cech)
  (normalDifference : Coefficient -> Physical -> Normal)
  (groupDifference : Coefficient -> Physical -> Group)
  (operationDifference : Coefficient -> Physical -> Operation)
  (coefficient : Coefficient)
  (candidate : nima-endpoint-normal-operation-candidate
    Coefficient Physical Endpoint Normal Operation zeroEndpoint zeroNormal
    zeroOperation endpointDifference normalDifference operationDifference
    coefficient)
  : U
  := Sigma (_ : cechDifference coefficient (first candidate) = zeroCech),
       groupDifference coefficient (first candidate) = zeroGroup

#define nima-complete-candidate-to-five-direction-lift
  (Coefficient Physical Endpoint Cech Normal Group Operation : U)
  (zeroEndpoint : Endpoint) (zeroCech : Cech) (zeroNormal : Normal)
  (zeroGroup : Group) (zeroOperation : Operation)
  (endpointDifference : Coefficient -> Physical -> Endpoint)
  (cechDifference : Coefficient -> Physical -> Cech)
  (normalDifference : Coefficient -> Physical -> Normal)
  (groupDifference : Coefficient -> Physical -> Group)
  (operationDifference : Coefficient -> Physical -> Operation)
  (coefficient : Coefficient)
  (candidate : nima-endpoint-normal-operation-candidate
    Coefficient Physical Endpoint Normal Operation zeroEndpoint zeroNormal
    zeroOperation endpointDifference normalDifference operationDifference
    coefficient)
  (completion : nima-candidate-physical-completion
    Coefficient Physical Endpoint Cech Normal Group Operation
    zeroEndpoint zeroCech zeroNormal zeroGroup zeroOperation endpointDifference
    cechDifference normalDifference groupDifference operationDifference
    coefficient candidate)
  : nima-five-direction-physical-lifts
      Coefficient Physical Endpoint Cech Normal Group Operation
      zeroEndpoint zeroCech zeroNormal zeroGroup zeroOperation
      endpointDifference cechDifference normalDifference groupDifference
      operationDifference coefficient
  := (first candidate,
      (first (second candidate),
       (first completion,
        (first (second (second candidate)),
         (second completion, second (second (second candidate)))))))

#define nima-candidate-completion-amplitude
  (Coefficient Physical Endpoint Cech Normal Group Operation Supported Scalars : U)
  (zeroEndpoint : Endpoint) (zeroCech : Cech) (zeroNormal : Normal)
  (zeroGroup : Group) (zeroOperation : Operation)
  (endpointDifference : Coefficient -> Physical -> Endpoint)
  (cechDifference : Coefficient -> Physical -> Cech)
  (normalDifference : Coefficient -> Physical -> Normal)
  (groupDifference : Coefficient -> Physical -> Group)
  (operationDifference : Coefficient -> Physical -> Operation)
  (coefficient : Coefficient)
  (candidate : nima-endpoint-normal-operation-candidate
    Coefficient Physical Endpoint Normal Operation zeroEndpoint zeroNormal
    zeroOperation endpointDifference normalDifference operationDifference
    coefficient)
  (completion : nima-candidate-physical-completion
    Coefficient Physical Endpoint Cech Normal Group Operation
    zeroEndpoint zeroCech zeroNormal zeroGroup zeroOperation endpointDifference
    cechDifference normalDifference groupDifference operationDifference
    coefficient candidate)
  (gysin : Physical -> Supported) (residue : Supported -> Scalars)
  : Scalars
  := residue (gysin (first candidate))

#data NimaCandidateCompletionGate
  := nima-road-Cech-coherence-at-candidate-required
  | nima-physical-group-reflection-coherence-at-candidate-required
  | nima-same-physical-point-retained
#define nima-candidate-completion-gate : NimaCandidateCompletionGate
  := nima-road-Cech-coherence-at-candidate-required
```
