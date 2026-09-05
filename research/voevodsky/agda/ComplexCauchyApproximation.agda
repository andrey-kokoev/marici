{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ComplexCauchyApproximation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Data.Sigma
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyMetricEquivalence
open import ConstructiveComplexCompletion

RationalComplex : Type
RationalComplex = Q.ℚ × Q.ℚ

rationalComplex : Q.ℚ → Q.ℚ → RationalComplex
rationalComplex real imaginary = real , imaginary

rationalRealPart : RationalComplex → Q.ℚ
rationalRealPart = fst

rationalImaginaryPart : RationalComplex → Q.ℚ
rationalImaginaryPart = snd

zeroRationalComplex : RationalComplex
zeroRationalComplex = rationalComplex 0 0

infixl 6 _+rationalComplex_
_+rationalComplex_ : RationalComplex → RationalComplex → RationalComplex
(ar , ai) +rationalComplex (br , bi) =
  rationalComplex (ar Q.+ br) (ai Q.+ bi)

negRationalComplex : RationalComplex → RationalComplex
negRationalComplex (ar , ai) = rationalComplex (Q.- ar) (Q.- ai)

infixl 7 _·rationalComplex_
_·rationalComplex_ : RationalComplex → RationalComplex → RationalComplex
(ar , ai) ·rationalComplex (br , bi) =
  rationalComplex
    ((ar Q.· br) Q.+ (Q.- (ai Q.· bi)))
    ((ar Q.· bi) Q.+ (ai Q.· br))

ComplexRegular : Type
ComplexRegular = RegularCauchy × RegularCauchy

complexApproximation : ComplexRegular → ℕ → RationalComplex
complexApproximation (real , imaginary) n =
  rationalComplex (approximation real n) (approximation imaginary n)

embedRationalComplexRegular : RationalComplex → ComplexRegular
embedRationalComplexRegular (real , imaginary) =
  constantCauchy real , constantCauchy imaginary

complexRegularClass : ComplexRegular → ComplexCompletion
complexRegularClass (real , imaginary) =
  SQ.[ real ] , SQ.[ imaginary ]

record RationalComplexDisk : Type where
  constructor rationalComplexDisk
  field
    center : RationalComplex
    radius : Q.ℚ
    radius-nonnegative : 0 ≤ radius
open RationalComplexDisk public

InsideBoxAt : ComplexRegular → RationalComplexDisk → ℕ → Type
InsideBoxAt z disk n =
  MagnitudeBound
    (rationalRealPart (complexApproximation z n) Q.+
      (Q.- rationalRealPart (center disk)))
    (radius disk) ×
  MagnitudeBound
    (rationalImaginaryPart (complexApproximation z n) Q.+
      (Q.- rationalImaginaryPart (center disk)))
    (radius disk)

zero-magnitude-at-nonnegative-radius : (radius : Q.ℚ) →
  0 ≤ radius → MagnitudeBound 0 radius
zero-magnitude-at-nonnegative-radius radius 0≤radius = record
  { positive-upper = 0≤radius
  ; negative-upper = 0≤radius
  }

canonicalComplexDisk : ComplexRegular → ℕ → RationalComplexDisk
canonicalComplexDisk z n = rationalComplexDisk
  (complexApproximation z n) (precision n) (precision-nonnegative n)

canonical-complex-disk-contains : (z : ComplexRegular) (n : ℕ) →
  InsideBoxAt z (canonicalComplexDisk z n) n
canonical-complex-disk-contains z n =
  transport-magnitude _ 0 (precision n)
    (Q.+InvR (rationalRealPart (complexApproximation z n)))
    (zero-magnitude-at-nonnegative-radius
      (precision n) (precision-nonnegative n)) ,
  transport-magnitude _ 0 (precision n)
    (Q.+InvR (rationalImaginaryPart (complexApproximation z n)))
    (zero-magnitude-at-nonnegative-radius
      (precision n) (precision-nonnegative n))

record CertifiedDiskName (z : ComplexRegular) : Type where
  field
    diskAt : ℕ → RationalComplexDisk
    containsAt : (n : ℕ) → InsideBoxAt z (diskAt n) n
    radius≤precision : (n : ℕ) → radius (diskAt n) ≤ precision n
open CertifiedDiskName public

canonicalCertifiedDiskName : (z : ComplexRegular) → CertifiedDiskName z
canonicalCertifiedDiskName z .diskAt = canonicalComplexDisk z
canonicalCertifiedDiskName z .containsAt = canonical-complex-disk-contains z
canonicalCertifiedDiskName z .radius≤precision n = isRefl≤ (precision n)

DiskRefines : RationalComplexDisk → RationalComplexDisk → Type
DiskRefines inner outer =
  MagnitudeBound
    (rationalRealPart (center inner) Q.+
      (Q.- rationalRealPart (center outer)))
    (radius outer Q.+ (Q.- radius inner)) ×
  MagnitudeBound
    (rationalImaginaryPart (center inner) Q.+
      (Q.- rationalImaginaryPart (center outer)))
    (radius outer Q.+ (Q.- radius inner))

record NestedCertifiedDiskName (z : ComplexRegular) : Type where
  field
    certifiedName : CertifiedDiskName z
    refines : (n : ℕ) →
      DiskRefines (diskAt certifiedName (suc n))
        (diskAt certifiedName n)
open NestedCertifiedDiskName public
