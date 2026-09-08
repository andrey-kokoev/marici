# Endpoint-relative source fibre and its two conductor states

This module separates the generic fibre construction from the large source
index.  The two conductor states are genuine new basis constructors, not
aliases for endpoint coefficients.

```rzk
#lang rzk-1

#data NimaEndpointRelativeState (A : U)
  := nima-endpoint-relative-old (a : A)
  | nima-endpoint-relative-conductor-plus
  | nima-endpoint-relative-conductor-minus

#define NimaEndpointRelativeCoefficients (A : U) : U
  := NimaZSum (NimaEndpointRelativeState A)

#define nima-endpoint-relative-old-column
  (A : U)
  (source-column : A -> NimaZSum A)
  (endpoint-plus endpoint-minus : A -> MariciInt)
  (a : A)
  : NimaEndpointRelativeCoefficients A
  := nima-sum-add (NimaEndpointRelativeState A)
       (nima-sum-map A (NimaEndpointRelativeState A)
         (nima-endpoint-relative-old A) (source-column a))
       (nima-sum-add (NimaEndpointRelativeState A)
         (nima-sum-scale (NimaEndpointRelativeState A) (endpoint-plus a)
           (nima-sum-atom (NimaEndpointRelativeState A)
             (nima-endpoint-relative-conductor-plus A)))
         (nima-sum-scale (NimaEndpointRelativeState A) (endpoint-minus a)
           (nima-sum-atom (NimaEndpointRelativeState A)
             (nima-endpoint-relative-conductor-minus A))))

#define nima-endpoint-relative-column
  (A : U)
  (source-column : A -> NimaZSum A)
  (endpoint-plus endpoint-minus : A -> MariciInt)
  : NimaEndpointRelativeState A -> NimaEndpointRelativeCoefficients A
  := \ q -> match q
       (nima-endpoint-relative-old a =>
          nima-endpoint-relative-old-column A source-column endpoint-plus endpoint-minus a
       | nima-endpoint-relative-conductor-plus =>
          nima-sum-zero (NimaEndpointRelativeState A)
       | nima-endpoint-relative-conductor-minus =>
          nima-sum-zero (NimaEndpointRelativeState A))

#define nima-endpoint-relative-d
  (A : U)
  (source-column : A -> NimaZSum A)
  (endpoint-plus endpoint-minus : A -> MariciInt)
  : NimaEndpointRelativeCoefficients A -> NimaEndpointRelativeCoefficients A
  := nima-sum-bind (NimaEndpointRelativeState A) (NimaEndpointRelativeState A)
       (nima-endpoint-relative-column A source-column endpoint-plus endpoint-minus)

#data NimaEndpointRelativeTestOld
  := nima-endpoint-relative-test-plus
  | nima-endpoint-relative-test-minus
  | nima-endpoint-relative-test-other

#define nima-endpoint-relative-test-source-column
  : NimaEndpointRelativeTestOld -> NimaZSum NimaEndpointRelativeTestOld
  := \ q -> nima-sum-zero NimaEndpointRelativeTestOld

#define nima-endpoint-relative-test-plus-augmentation
  : NimaEndpointRelativeTestOld -> MariciInt
  := \ q -> match q
       (nima-endpoint-relative-test-plus => marici-int-one
       | nima-endpoint-relative-test-minus => marici-int-zero
       | nima-endpoint-relative-test-other => marici-int-zero)

#define nima-endpoint-relative-test-minus-augmentation
  : NimaEndpointRelativeTestOld -> MariciInt
  := \ q -> match q
       (nima-endpoint-relative-test-plus => marici-int-zero
       | nima-endpoint-relative-test-minus => marici-int-one
       | nima-endpoint-relative-test-other => marici-int-zero)

#define NimaEndpointRelativeTest : U
  := NimaEndpointRelativeCoefficients NimaEndpointRelativeTestOld

#define nima-endpoint-relative-test-column
  : NimaEndpointRelativeState NimaEndpointRelativeTestOld -> NimaEndpointRelativeTest
  := nima-endpoint-relative-column NimaEndpointRelativeTestOld
       nima-endpoint-relative-test-source-column
       nima-endpoint-relative-test-plus-augmentation
       nima-endpoint-relative-test-minus-augmentation

#define nima-endpoint-relative-test-d : NimaEndpointRelativeTest -> NimaEndpointRelativeTest
  := nima-sum-bind (NimaEndpointRelativeState NimaEndpointRelativeTestOld)
       (NimaEndpointRelativeState NimaEndpointRelativeTestOld)
       nima-endpoint-relative-test-column

#define nima-endpoint-relative-test-cell-square
  (q : NimaEndpointRelativeState NimaEndpointRelativeTestOld)
  : nima-sum-equal (NimaEndpointRelativeState NimaEndpointRelativeTestOld)
      (nima-endpoint-relative-test-d (nima-endpoint-relative-test-column q))
      (nima-sum-zero (NimaEndpointRelativeState NimaEndpointRelativeTestOld))
  := match q
       (nima-endpoint-relative-old a => match a
          (nima-endpoint-relative-test-plus => \ probe -> refl
          | nima-endpoint-relative-test-minus => \ probe -> refl
          | nima-endpoint-relative-test-other => \ probe -> refl)
       | nima-endpoint-relative-conductor-plus => \ probe -> refl
       | nima-endpoint-relative-conductor-minus => \ probe -> refl)

#define nima-endpoint-relative-test-square (p : NimaEndpointRelativeTest)
  : nima-sum-equal (NimaEndpointRelativeState NimaEndpointRelativeTestOld)
      (nima-endpoint-relative-test-d (nima-endpoint-relative-test-d p))
      (nima-sum-zero (NimaEndpointRelativeState NimaEndpointRelativeTestOld))
  := nima-sum-column-square
       (NimaEndpointRelativeState NimaEndpointRelativeTestOld)
       nima-endpoint-relative-test-column
       nima-endpoint-relative-test-cell-square p

#define nima-endpoint-relative-test-plus-column
  : nima-endpoint-relative-test-column
      (nima-endpoint-relative-old NimaEndpointRelativeTestOld
        nima-endpoint-relative-test-plus)
    = nima-sum-add (NimaEndpointRelativeState NimaEndpointRelativeTestOld)
        (nima-sum-zero (NimaEndpointRelativeState NimaEndpointRelativeTestOld))
        (nima-sum-add (NimaEndpointRelativeState NimaEndpointRelativeTestOld)
          (nima-sum-scale (NimaEndpointRelativeState NimaEndpointRelativeTestOld) marici-int-one
            (nima-sum-atom (NimaEndpointRelativeState NimaEndpointRelativeTestOld)
              (nima-endpoint-relative-conductor-plus NimaEndpointRelativeTestOld)))
          (nima-sum-scale (NimaEndpointRelativeState NimaEndpointRelativeTestOld) marici-int-zero
            (nima-sum-atom (NimaEndpointRelativeState NimaEndpointRelativeTestOld)
              (nima-endpoint-relative-conductor-minus NimaEndpointRelativeTestOld))))
  := refl
```
