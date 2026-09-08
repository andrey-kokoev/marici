# Corrected Morse-chain evaluation in the relative fibre

Only two of the five corrected boundary terms meet nonzero sparse columns. The
raw endpoint term and the occurrence correction produce opposite copies of the
same cubic monomial.

```rzk
#lang rzk-1

#define nima-relative-pi-plus : NimaPolynomialMonomial
  := (marici-zero,(marici-zero,(marici-zero,((marici-succ marici-zero),
     (marici-zero,((marici-succ marici-zero),(marici-zero,(marici-zero,
     ((marici-succ marici-zero),(marici-zero,(marici-zero,(marici-zero,
     (marici-zero,(marici-zero,(marici-zero,(marici-zero,
     (marici-zero,marici-zero)))))))))))))))))

#define nima-relative-pi-plus-z : NimaRelativePolynomialBoundary
  := nima-sum-add NimaRelativePolynomialBoundaryBasis
       (nima-sum-atom NimaRelativePolynomialBoundaryBasis
         (nima-endpoint-line-plus,(nima-relative-f-state-5,nima-relative-pi-plus)))
       (nima-sum-add NimaRelativePolynomialBoundaryBasis
         (nima-sum-atom NimaRelativePolynomialBoundaryBasis
           (nima-endpoint-line-plus,(nima-relative-f-state-7,nima-relative-pi-plus)))
         (nima-sum-zero NimaRelativePolynomialBoundaryBasis))

#define nima-relative-q-raw-image : NimaRelativePolynomialBoundary
  := nima-relative-pi-plus-z

#define nima-relative-q-occurrence-correction-image : NimaRelativePolynomialBoundary
  := nima-sum-neg NimaRelativePolynomialBoundaryBasis nima-relative-pi-plus-z

#define nima-relative-corrected-q-image : NimaRelativePolynomialBoundary
  := nima-sum-add NimaRelativePolynomialBoundaryBasis
       nima-relative-q-raw-image nima-relative-q-occurrence-correction-image

#define nima-relative-corrected-q-zero
  : nima-sum-equal NimaRelativePolynomialBoundaryBasis
      nima-relative-corrected-q-image
      (nima-sum-zero NimaRelativePolynomialBoundaryBasis)
  := nima-sum-add-inverse NimaRelativePolynomialBoundaryBasis nima-relative-pi-plus-z

#data NimaCorrectedHMorseTerm
  := nima-corrected-h-term-0
  | nima-corrected-h-term-1
  | nima-corrected-h-term-2
  | nima-corrected-h-term-3
  | nima-corrected-h-term-4
  | nima-corrected-h-term-5
  | nima-corrected-h-term-6
  | nima-corrected-h-term-7
  | nima-corrected-h-term-8
  | nima-corrected-h-term-9
  | nima-corrected-h-term-10
  | nima-corrected-h-term-11
  | nima-corrected-h-term-12

#define nima-relative-h-term-image : NimaCorrectedHMorseTerm -> NimaRelativePolynomialBoundary
  := \ q -> match q
       (nima-corrected-h-term-0 => nima-sum-zero NimaRelativePolynomialBoundaryBasis
       | nima-corrected-h-term-1 => nima-sum-zero NimaRelativePolynomialBoundaryBasis
       | nima-corrected-h-term-2 => nima-sum-zero NimaRelativePolynomialBoundaryBasis
       | nima-corrected-h-term-3 => nima-sum-zero NimaRelativePolynomialBoundaryBasis
       | nima-corrected-h-term-4 => nima-sum-zero NimaRelativePolynomialBoundaryBasis
       | nima-corrected-h-term-5 => nima-sum-zero NimaRelativePolynomialBoundaryBasis
       | nima-corrected-h-term-6 => nima-sum-zero NimaRelativePolynomialBoundaryBasis
       | nima-corrected-h-term-7 => nima-sum-zero NimaRelativePolynomialBoundaryBasis
       | nima-corrected-h-term-8 => nima-sum-zero NimaRelativePolynomialBoundaryBasis
       | nima-corrected-h-term-9 => nima-sum-zero NimaRelativePolynomialBoundaryBasis
       | nima-corrected-h-term-10 => nima-sum-zero NimaRelativePolynomialBoundaryBasis
       | nima-corrected-h-term-11 => nima-sum-zero NimaRelativePolynomialBoundaryBasis
       | nima-corrected-h-term-12 => nima-sum-zero NimaRelativePolynomialBoundaryBasis)

#define nima-relative-corrected-h-image
  (p : NimaZSum NimaCorrectedHMorseTerm) : NimaRelativePolynomialBoundary
  := nima-sum-bind NimaCorrectedHMorseTerm NimaRelativePolynomialBoundaryBasis
       nima-relative-h-term-image p

#define nima-relative-corrected-h-zero
  (p : NimaZSum NimaCorrectedHMorseTerm)
  : nima-sum-equal NimaRelativePolynomialBoundaryBasis
      (nima-relative-corrected-h-image p)
      (nima-sum-zero NimaRelativePolynomialBoundaryBasis)
  := \ probe -> nima-frame-concat MariciInt
       (nima-sum-eval NimaRelativePolynomialBoundaryBasis probe
         (nima-relative-corrected-h-image p))
       (nima-sum-eval NimaCorrectedHMorseTerm
         (\ q -> nima-sum-eval NimaRelativePolynomialBoundaryBasis probe
           (nima-relative-h-term-image q)) p)
       marici-int-zero
       (nima-sum-eval-bind NimaCorrectedHMorseTerm NimaRelativePolynomialBoundaryBasis
         nima-relative-h-term-image probe p)
       (nima-any-eval-zero-atoms NimaCorrectedHMorseTerm
         (\ q -> nima-sum-eval NimaRelativePolynomialBoundaryBasis probe
           (nima-relative-h-term-image q))
         (\ q -> match q
           (nima-corrected-h-term-0 => refl
           | nima-corrected-h-term-1 => refl
           | nima-corrected-h-term-2 => refl
           | nima-corrected-h-term-3 => refl
           | nima-corrected-h-term-4 => refl
           | nima-corrected-h-term-5 => refl
           | nima-corrected-h-term-6 => refl
           | nima-corrected-h-term-7 => refl
           | nima-corrected-h-term-8 => refl
           | nima-corrected-h-term-9 => refl
           | nima-corrected-h-term-10 => refl
           | nima-corrected-h-term-11 => refl
           | nima-corrected-h-term-12 => refl)) p)
```
