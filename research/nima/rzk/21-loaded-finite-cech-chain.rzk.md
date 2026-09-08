# Loaded finite-to-Cech chain comparison

All 215 generator squares are present.  The final theorem extends them to
every finite integral coefficient expression by structural recursion.

```rzk
#lang rzk-1
#define nima-loaded-lambda-column-square : (v : NimaFiniteLoadedBasis) ->
  nima-sum-equal NimaCechLoadedBasis
    (nima-finite-cech-comparison (nima-finite-loaded-column v))
    (nima-cech-loaded-column (nima-finite-cech-monomial v))
  := \ (c,m) -> (match c into (\ k -> (v : NimaPolynomialMonomial) ->
       nima-sum-equal NimaCechLoadedBasis
         (nima-finite-cech-comparison (nima-finite-loaded-column (k,v)))
         (nima-cech-loaded-column (nima-finite-cech-monomial (k,v)))) (
    nima-loaded-cell-0 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-1 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-2 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-3 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-4 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-5 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-6 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-7 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-8 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-9 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-10 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-11 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-12 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-13 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-14 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-15 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-16 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-17 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-18 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-19 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-20 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-21 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-22 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-23 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-24 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-25 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-26 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-27 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-28 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-29 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-30 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-31 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-32 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-33 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-34 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-35 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-36 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-37 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-38 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-39 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-40 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-41 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-42 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-43 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-44 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-45 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-46 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-47 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-48 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-49 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-50 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-51 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-52 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-53 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-54 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-55 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-56 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-57 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-58 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-59 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-60 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-61 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-62 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-63 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-64 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-65 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-66 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-67 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-68 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-69 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-70 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-71 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-72 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-73 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-74 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-75 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-76 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-77 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-78 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-79 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-80 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-81 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-82 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-83 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-84 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-85 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-86 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-87 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-88 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-89 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-90 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-91 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-92 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-93 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-94 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-95 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-96 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-97 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-98 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-99 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-100 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-101 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-102 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-103 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-104 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-105 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-106 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-107 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-108 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-109 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-110 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-111 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-112 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-113 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-114 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-115 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-116 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-117 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-118 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-119 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-120 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-121 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-122 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-123 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-124 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-125 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-126 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-127 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-128 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-129 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-130 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-131 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-132 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-133 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-134 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-135 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-136 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-137 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-138 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-139 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-140 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-141 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-142 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-143 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-144 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-145 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-146 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-147 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-148 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-149 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-150 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-151 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-152 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-153 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-154 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-155 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-156 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-157 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-158 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-159 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-160 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-161 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-162 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-163 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-164 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-165 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-166 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-167 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-168 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-169 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-170 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-171 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-172 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-173 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-174 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-175 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-176 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-177 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-178 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-179 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-180 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-181 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-182 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-183 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-184 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-185 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-186 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-187 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-188 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-189 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-190 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-191 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-192 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-193 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-194 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-195 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-196 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-197 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-198 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-199 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-200 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-201 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-202 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-203 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-204 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-205 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-206 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-207 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-208 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-209 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-210 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-211 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-212 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-213 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  | nima-loaded-cell-214 => \ (x0,(x1,(x2,(x3,(x4,(x5,(x6,(x7,(x8,(u0,(u1,(u2,(u3,(u4,(u5,(u6,(u7,u8))))))))))))))))) probe -> refl
  )) m

#define nima-loaded-lambda-chain (p : NimaFiniteLoadedCoefficients)
  : nima-sum-equal NimaCechLoadedBasis
      (nima-finite-cech-comparison (nima-finite-loaded-d p))
      (nima-cech-loaded-d (nima-finite-cech-comparison p))
  := match p
       (nima-sum-zero => \ probe -> refl
       | nima-sum-atom a => nima-loaded-lambda-column-square a
       | nima-sum-add x ihx y ihy => \ probe -> nima-cochain-ap2 MariciInt MariciInt MariciInt marici-int-add
           (nima-sum-eval NimaCechLoadedBasis probe (nima-finite-cech-comparison (nima-finite-loaded-d x)))
           (nima-sum-eval NimaCechLoadedBasis probe (nima-cech-loaded-d (nima-finite-cech-comparison x)))
           (nima-sum-eval NimaCechLoadedBasis probe (nima-finite-cech-comparison (nima-finite-loaded-d y)))
           (nima-sum-eval NimaCechLoadedBasis probe (nima-cech-loaded-d (nima-finite-cech-comparison y))) (ihx probe) (ihy probe)
       | nima-sum-neg x ih => \ probe -> nima-frame-ap MariciInt MariciInt marici-int-negate
           (nima-sum-eval NimaCechLoadedBasis probe (nima-finite-cech-comparison (nima-finite-loaded-d x)))
           (nima-sum-eval NimaCechLoadedBasis probe (nima-cech-loaded-d (nima-finite-cech-comparison x))) (ih probe)
       | nima-sum-scale c x ih => \ probe -> nima-frame-ap MariciInt MariciInt (marici-int-mul c)
           (nima-sum-eval NimaCechLoadedBasis probe (nima-finite-cech-comparison (nima-finite-loaded-d x)))
           (nima-sum-eval NimaCechLoadedBasis probe (nima-cech-loaded-d (nima-finite-cech-comparison x))) (ih probe))
```
