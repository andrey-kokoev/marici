{-# OPTIONS --safe --cubical --guardedness #-}
module FramedCellBadFrame where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; root)
open import InternalSourceComparisons using (exchange)
import GeneratedReaderClassification as G
import ForwardCertifiedPrograms as P
open import CertifiedFramedCells
p : P.Certificate (G.start A (root A))
p = P.certificate (P.initialP (P.rootI A)) refl
bad : Program exchange (A , G.start A (root A)) (A , G.start A (root A))
bad = program p p (refl , refl)
