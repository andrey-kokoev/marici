{-# OPTIONS --safe --cubical --guardedness #-}
module ProgramBadGuardBypass where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; C; CA)
open import InternalSourceComparisons using (stay)
open import SourceCertifiedPrograms
bad : Program A
bad = compareP stay (seedP A) (attachP (seedP C) (A , CA)) refl
