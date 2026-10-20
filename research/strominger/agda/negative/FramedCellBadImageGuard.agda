{-# OPTIONS --safe --cubical --guardedness #-}
module FramedCellBadImageGuard where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; B; AB; root)
open import InternalSourceComparisons using (exchange)
import GeneratedReaderClassification as G
import ForwardCertifiedPrograms as P
open import CertifiedFramedCells
p : P.Certificate (G.start A (root A))
p = P.certificate (P.initialP (P.rootI A)) refl
q : P.Certificate (G.attachF (G.start A (root A)) (B , AB))
q = P.certificate (P.attachP (P.initialP (P.rootI A)) (B , AB)) refl
bad : Program exchange (A , G.start A (root A)) (B , G.attachF (G.start A (root A)) (B , AB))
bad = program p q (refl , refl)
