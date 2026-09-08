# Regulator-supported vertex decomposition

```rzk
#lang rzk-1

#data NimaHexagonTriangulation14
  := nima-tri-020304 | nima-tri-020424 | nima-tri-022425
  | nima-tri-030413 | nima-tri-041314 | nima-tri-041424
  | nima-tri-131415 | nima-tri-141524 | nima-tri-152425
  | nima-tri-with35-0 | nima-tri-with35-1 | nima-tri-with35-2
  | nima-tri-with35-3 | nima-tri-with35-4

#define NimaVertexComparisonPacket : U := NimaZSum NimaHexagonTriangulation14

#define nima-nine-vertex-difference : NimaVertexComparisonPacket
  := nima-sum-add NimaHexagonTriangulation14
       (nima-sum-atom NimaHexagonTriangulation14 nima-tri-020304)
       (nima-sum-add NimaHexagonTriangulation14
        (nima-sum-atom NimaHexagonTriangulation14 nima-tri-020424)
        (nima-sum-add NimaHexagonTriangulation14
         (nima-sum-atom NimaHexagonTriangulation14 nima-tri-022425)
         (nima-sum-add NimaHexagonTriangulation14
          (nima-sum-atom NimaHexagonTriangulation14 nima-tri-030413)
          (nima-sum-add NimaHexagonTriangulation14
           (nima-sum-atom NimaHexagonTriangulation14 nima-tri-041314)
           (nima-sum-add NimaHexagonTriangulation14
            (nima-sum-atom NimaHexagonTriangulation14 nima-tri-041424)
            (nima-sum-add NimaHexagonTriangulation14
             (nima-sum-atom NimaHexagonTriangulation14 nima-tri-131415)
             (nima-sum-add NimaHexagonTriangulation14
              (nima-sum-atom NimaHexagonTriangulation14 nima-tri-141524)
              (nima-sum-atom NimaHexagonTriangulation14 nima-tri-152425))))))))

#define nima-vertex-augmentation : NimaHexagonTriangulation14 -> MariciInt
  := \ face -> marici-int-one
#define nima-nine-vertex-count-value
  : nima-sum-eval NimaHexagonTriangulation14 nima-vertex-augmentation
      nima-nine-vertex-difference
    = marici-int-embed-nat
       (marici-succ (marici-succ (marici-succ (marici-succ
        (marici-succ (marici-succ (marici-succ (marici-succ
         (marici-succ marici-zero)))))))))
  := refl

#data NimaFixedPrimaryDirection
  := nima-fixed-primary-Psi
  | nima-fixed-primary-Z
#data NimaEndpointTopSignature
  := nima-endpoint-both
  | nima-endpoint-negative-only

#define nima-fixed-primary-endpoint-signature
  : NimaFixedPrimaryDirection -> NimaEndpointTopSignature
  := \ direction -> match direction
       (nima-fixed-primary-Psi => nima-endpoint-both
       | nima-fixed-primary-Z => nima-endpoint-negative-only)

#data NimaEndpointQuotientVertex8
  := nima-endpoint-quotient-030413 | nima-endpoint-quotient-041314
  | nima-endpoint-quotient-041424 | nima-endpoint-quotient-131415
  | nima-endpoint-quotient-141524 | nima-endpoint-quotient-152425
  | nima-endpoint-quotient-022425 | nima-endpoint-quotient-020424

#define NimaEndpointQuotientDifference : U := NimaZSum NimaEndpointQuotientVertex8
#define nima-endpoint-quotient-eight-vector : NimaEndpointQuotientDifference
  := nima-sum-add NimaEndpointQuotientVertex8
       (nima-sum-atom NimaEndpointQuotientVertex8 nima-endpoint-quotient-030413)
       (nima-sum-add NimaEndpointQuotientVertex8
        (nima-sum-atom NimaEndpointQuotientVertex8 nima-endpoint-quotient-041314)
        (nima-sum-add NimaEndpointQuotientVertex8
         (nima-sum-atom NimaEndpointQuotientVertex8 nima-endpoint-quotient-041424)
         (nima-sum-add NimaEndpointQuotientVertex8
          (nima-sum-atom NimaEndpointQuotientVertex8 nima-endpoint-quotient-131415)
          (nima-sum-add NimaEndpointQuotientVertex8
           (nima-sum-atom NimaEndpointQuotientVertex8 nima-endpoint-quotient-141524)
           (nima-sum-add NimaEndpointQuotientVertex8
            (nima-sum-atom NimaEndpointQuotientVertex8 nima-endpoint-quotient-152425)
            (nima-sum-add NimaEndpointQuotientVertex8
             (nima-sum-atom NimaEndpointQuotientVertex8 nima-endpoint-quotient-022425)
             (nima-sum-atom NimaEndpointQuotientVertex8
               nima-endpoint-quotient-020424)))))))
```
