{-# OPTIONS --safe --cubical --guardedness #-}
module ProgramBadFunctionCertificate where
open import Cubical.Data.Bool using (Bool; not)
open import NativeExtensionFamilyAudit using (A)
open import SourceCertifiedPrograms
module Hostile = SuppliedFunction Bool Bool not
bad : Produced Hostile.encoded Hostile.admitted
bad = produced (bodyP (seedP A))
