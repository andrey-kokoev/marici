{-# OPTIONS --safe --cubical --guardedness #-}
module RHCR1GalleryQNoGo where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- Abstract form of the certified D03 support obstruction: a specialization
-- which factors through the ordinary relative-Q projection cannot send a
-- gallery supported in F1 to a prescribed nonzero extraordinary-costalk unit.
record GalleryQSpecializationData {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Gallery Q Costalk : Type ℓ
    markedGallery : Gallery
    zeroQ : Q
    zeroCostalk localUnit : Costalk
    galleryToQ : Gallery → Q
    qToCostalk : Q → Costalk

    galleryHasZeroQImage : galleryToQ markedGallery ≡ zeroQ
    specializationPreservesZero : qToCostalk zeroQ ≡ zeroCostalk
    localUnitNonzero : localUnit ≡ zeroCostalk → ⊥

open GalleryQSpecializationData public

ordinaryGallerySpecializationIsZero : {ℓ : Level}
  (D : GalleryQSpecializationData {ℓ}) →
  qToCostalk D (galleryToQ D (markedGallery D)) ≡ zeroCostalk D
ordinaryGallerySpecializationIsZero D =
  cong (qToCostalk D) (galleryHasZeroQImage D) ∙
  specializationPreservesZero D

ordinaryGalleryCannotRealizeLocalUnit : {ℓ : Level}
  (D : GalleryQSpecializationData {ℓ}) →
  qToCostalk D (galleryToQ D (markedGallery D)) ≡ localUnit D → ⊥
ordinaryGalleryCannotRealizeLocalUnit D realizes =
  localUnitNonzero D
    (sym realizes ∙ ordinaryGallerySpecializationIsZero D)

-- Therefore an inhabited unit-valued specialization has to be genuinely
-- extraordinary: it cannot definitionally be the ordinary gallery-to-Q map.
record ExtraordinaryGallerySpecialization {ℓ : Level}
  (D : GalleryQSpecializationData {ℓ}) : Type ℓ where
  field
    extraordinaryMap : Gallery D → Costalk D
    realizesLocalUnit : extraordinaryMap (markedGallery D) ≡ localUnit D

open ExtraordinaryGallerySpecialization public

extraordinaryCannotAgreeWithOrdinary : {ℓ : Level}
  {D : GalleryQSpecializationData {ℓ}} →
  (E : ExtraordinaryGallerySpecialization D) →
  extraordinaryMap E (markedGallery D) ≡
  qToCostalk D (galleryToQ D (markedGallery D)) → ⊥
extraordinaryCannotAgreeWithOrdinary {D = D} E agrees =
  ordinaryGalleryCannotRealizeLocalUnit D
    (sym agrees ∙ realizesLocalUnit E)
