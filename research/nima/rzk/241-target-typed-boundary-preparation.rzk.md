# Target-typed three-channel boundary preparation

```rzk
#lang rzk-1
#define nima-target-typed-boundary-source
  (PrimarySource ReciprocalSource RelationSource : U) : U
  := Sigma (_ : PrimarySource), Sigma (_ : ReciprocalSource), RelationSource

#define nima-target-typed-boundary-gysin
  (PrimarySource ReciprocalSource RelationSource Supported : U)
  (primary-gysin : PrimarySource -> Supported)
  (reciprocal-gysin : ReciprocalSource -> Supported)
  (relation-gysin : RelationSource -> Supported)
  (add : Supported -> Supported -> Supported)
  : nima-target-typed-boundary-source
      PrimarySource ReciprocalSource RelationSource -> Supported
  := \ preparation ->
       add (primary-gysin (first preparation))
         (add (reciprocal-gysin (first (second preparation)))
           (relation-gysin (second (second preparation))))

#define nima-target-typed-boundary-amplitude-witness
  (PrimarySource ReciprocalSource RelationSource Supported Scalars : U)
  (primary-gysin : PrimarySource -> Supported)
  (reciprocal-gysin : ReciprocalSource -> Supported)
  (relation-gysin : RelationSource -> Supported)
  (add : Supported -> Supported -> Supported)
  (primary reciprocal relation residue : Supported -> Scalars)
  (scalar-add scalar-multiply : Scalars -> Scalars -> Scalars)
  (scalar-negate : Scalars -> Scalars)
  (beta a b c : Scalars)
  : U
  := Sigma (preparation : nima-target-typed-boundary-source
       PrimarySource ReciprocalSource RelationSource),
       Sigma (_ : primary
         (nima-target-typed-boundary-gysin
           PrimarySource ReciprocalSource RelationSource Supported
           primary-gysin reciprocal-gysin relation-gysin add preparation) = a),
       Sigma (_ : reciprocal
         (nima-target-typed-boundary-gysin
           PrimarySource ReciprocalSource RelationSource Supported
           primary-gysin reciprocal-gysin relation-gysin add preparation) = b),
       Sigma (_ : relation
         (nima-target-typed-boundary-gysin
           PrimarySource ReciprocalSource RelationSource Supported
           primary-gysin reciprocal-gysin relation-gysin add preparation) = c),
       residue
         (nima-target-typed-boundary-gysin
           PrimarySource ReciprocalSource RelationSource Supported
           primary-gysin reciprocal-gysin relation-gysin add preparation)
       = scalar-negate
           (scalar-multiply beta (scalar-add a (scalar-add b c)))

#data NimaTargetTypedBoundarySourceGate
  := nima-generic-Q-primary-source-map-required
  | nima-paired-endpoint-reciprocal-source-map-required
  | nima-road-relation-source-map-required
  | nima-cross-channel-detector-orthogonality-required
  | nima-target-typed-product-source-is-minimal-symbolic-constructor
#define nima-target-typed-boundary-source-gate : NimaTargetTypedBoundarySourceGate
  := nima-target-typed-product-source-is-minimal-symbolic-constructor
```
