{-# OPTIONS --safe --cubical --guardedness #-}
module NativeBadIncidenceAdmission where
open import NativeExtensionFamilyAudit

-- A valid native pointed comparison is NOT thereby incidence preserving.
-- Reusing sigma's edge witness for tau must be rejected by the kernel.
bad : PreservesEdges tauEquiv
bad s t e = sigmaEdge e
