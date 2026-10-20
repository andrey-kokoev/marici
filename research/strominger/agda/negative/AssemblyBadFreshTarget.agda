{-# OPTIONS --safe --cubical --guardedness #-}
module AssemblyBadFreshTarget where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (root)
open import InternalSourceComparisons using (stay)
import GeneratedReaderClassification as G
import ForwardCertifiedPrograms as P
import FiniteComparisonTrees as F
import MixedComparisonTrees as M
import CertifiedMixedRootHigher as Higher
import SourceCertifiedCoherentAssembly as Assembly
module X = Assembly.Regression.Bound
fresh : F.Object
fresh = fst X.target , G.start (fst X.target) (root (fst X.target))
bad : Higher.Tree stay X.target X.target
bad = Higher.checked (M.old (F.unit fresh))
  (P.certificate (P.initialP (P.rootI (fst X.target))) refl)
