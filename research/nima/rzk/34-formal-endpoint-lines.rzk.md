# Formal endpoint coefficient lines

The endpoint lines are basis labels with occurrence multidegrees.  They are not
implemented as inverses or as localized coefficient monomials.

```rzk
#lang rzk-1

#data NimaEndpointLine
  := nima-endpoint-line-plus
  | nima-endpoint-line-minus

#define NimaOccurrenceDegree6 : U
  := Sigma (_ : MariciInt), Sigma (_ : MariciInt), Sigma (_ : MariciInt),
     Sigma (_ : MariciInt), Sigma (_ : MariciInt), MariciInt

#define nima-endpoint-line-degree : NimaEndpointLine -> NimaOccurrenceDegree6
  := \ line -> match line
       (nima-endpoint-line-plus =>
          (marici-int-zero,(marici-int-zero,(marici-int-zero,
           (marici-int-minus-one,(marici-int-minus-one,marici-int-minus-one)))))
       | nima-endpoint-line-minus =>
          (marici-int-minus-one,(marici-int-minus-one,(marici-int-minus-one,
           (marici-int-zero,(marici-int-zero,marici-int-zero))))))

#define NimaRelativeBoundaryBasis : U
  := Sigma (_ : NimaEndpointLine), NimaRelativeFBasis
#define NimaRelativeBoundary : U := NimaZSum NimaRelativeBoundaryBasis

#define nima-relative-boundary-plus (p : NimaRelativeF) : NimaRelativeBoundary
  := nima-sum-map NimaRelativeFBasis NimaRelativeBoundaryBasis
       (\ q -> (nima-endpoint-line-plus,q)) p
#define nima-relative-boundary-minus (p : NimaRelativeF) : NimaRelativeBoundary
  := nima-sum-map NimaRelativeFBasis NimaRelativeBoundaryBasis
       (\ q -> (nima-endpoint-line-minus,q)) p

#define nima-relative-plus-probe
  (probe : NimaRelativeFBasis -> MariciInt)
  : NimaRelativeBoundaryBasis -> MariciInt
  := \ (line,q) -> match line
       (nima-endpoint-line-plus => probe q
       | nima-endpoint-line-minus => marici-int-zero)

#define nima-relative-minus-probe
  (probe : NimaRelativeFBasis -> MariciInt)
  : NimaRelativeBoundaryBasis -> MariciInt
  := \ (line,q) -> match line
       (nima-endpoint-line-plus => marici-int-zero
       | nima-endpoint-line-minus => probe q)

#define nima-any-eval-zero-atoms
  (A : U)
  (probe : A -> MariciInt)
  (zero-atoms : (a : A) -> probe a = marici-int-zero)
  (p : NimaZSum A)
  : nima-sum-eval A probe p = marici-int-zero
  := match p
       (nima-sum-zero => refl
       | nima-sum-atom a => zero-atoms a
       | nima-sum-add x ihx y ihy => nima-cochain-ap2 MariciInt MariciInt MariciInt marici-int-add
          (nima-sum-eval A probe x) marici-int-zero
          (nima-sum-eval A probe y) marici-int-zero ihx ihy
       | nima-sum-neg x ih => nima-frame-ap MariciInt MariciInt marici-int-negate
          (nima-sum-eval A probe x) marici-int-zero ih
       | nima-sum-scale c x ih => nima-frame-concat MariciInt
          (marici-int-mul c (nima-sum-eval A probe x))
          (marici-int-mul c marici-int-zero) marici-int-zero
          (nima-frame-ap MariciInt MariciInt (marici-int-mul c)
            (nima-sum-eval A probe x) marici-int-zero ih)
          (marici-int-mul-zero-right c))

#define nima-relative-boundary-plus-recovery
  (probe : NimaRelativeFBasis -> MariciInt) (p : NimaRelativeF)
  : nima-sum-eval NimaRelativeBoundaryBasis (nima-relative-plus-probe probe)
      (nima-relative-boundary-plus p)
    = nima-sum-eval NimaRelativeFBasis probe p
  := nima-sum-eval-bind NimaRelativeFBasis NimaRelativeBoundaryBasis
       (\ q -> nima-sum-atom NimaRelativeBoundaryBasis (nima-endpoint-line-plus,q))
       (nima-relative-plus-probe probe) p

#define nima-relative-boundary-minus-recovery
  (probe : NimaRelativeFBasis -> MariciInt) (p : NimaRelativeF)
  : nima-sum-eval NimaRelativeBoundaryBasis (nima-relative-minus-probe probe)
      (nima-relative-boundary-minus p)
    = nima-sum-eval NimaRelativeFBasis probe p
  := nima-sum-eval-bind NimaRelativeFBasis NimaRelativeBoundaryBasis
       (\ q -> nima-sum-atom NimaRelativeBoundaryBasis (nima-endpoint-line-minus,q))
       (nima-relative-minus-probe probe) p

#define nima-relative-boundary-plus-on-minus-zero
  (probe : NimaRelativeFBasis -> MariciInt) (p : NimaRelativeF)
  : nima-sum-eval NimaRelativeBoundaryBasis (nima-relative-plus-probe probe)
      (nima-relative-boundary-minus p) = marici-int-zero
  := nima-frame-concat MariciInt
       (nima-sum-eval NimaRelativeBoundaryBasis (nima-relative-plus-probe probe)
         (nima-relative-boundary-minus p))
       (nima-sum-eval NimaRelativeFBasis
         (\ q -> nima-sum-eval NimaRelativeBoundaryBasis (nima-relative-plus-probe probe)
           (nima-sum-atom NimaRelativeBoundaryBasis (nima-endpoint-line-minus,q))) p)
       marici-int-zero
       (nima-sum-eval-bind NimaRelativeFBasis NimaRelativeBoundaryBasis
         (\ q -> nima-sum-atom NimaRelativeBoundaryBasis (nima-endpoint-line-minus,q))
         (nima-relative-plus-probe probe) p)
       (nima-any-eval-zero-atoms NimaRelativeFBasis
         (\ q -> nima-sum-eval NimaRelativeBoundaryBasis (nima-relative-plus-probe probe)
           (nima-sum-atom NimaRelativeBoundaryBasis (nima-endpoint-line-minus,q)))
         (\ q -> refl) p)

#define nima-relative-boundary-minus-on-plus-zero
  (probe : NimaRelativeFBasis -> MariciInt) (p : NimaRelativeF)
  : nima-sum-eval NimaRelativeBoundaryBasis (nima-relative-minus-probe probe)
      (nima-relative-boundary-plus p) = marici-int-zero
  := nima-frame-concat MariciInt
       (nima-sum-eval NimaRelativeBoundaryBasis (nima-relative-minus-probe probe)
         (nima-relative-boundary-plus p))
       (nima-sum-eval NimaRelativeFBasis
         (\ q -> nima-sum-eval NimaRelativeBoundaryBasis (nima-relative-minus-probe probe)
           (nima-sum-atom NimaRelativeBoundaryBasis (nima-endpoint-line-plus,q))) p)
       marici-int-zero
       (nima-sum-eval-bind NimaRelativeFBasis NimaRelativeBoundaryBasis
         (\ q -> nima-sum-atom NimaRelativeBoundaryBasis (nima-endpoint-line-plus,q))
         (nima-relative-minus-probe probe) p)
       (nima-any-eval-zero-atoms NimaRelativeFBasis
         (\ q -> nima-sum-eval NimaRelativeBoundaryBasis (nima-relative-minus-probe probe)
           (nima-sum-atom NimaRelativeBoundaryBasis (nima-endpoint-line-plus,q)))
         (\ q -> refl) p)
```
