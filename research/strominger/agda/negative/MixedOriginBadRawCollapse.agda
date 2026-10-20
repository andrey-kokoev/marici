{-# OPTIONS --safe --cubical --guardedness #-}
module MixedOriginBadRawCollapse where
open import Cubical.Foundations.Prelude
import ForwardCertifiedPrograms as P
import FiniteComparisonTrees as F
import MixedComparisonTrees as M
import MixedHistoryCertificates as H
import InternalComparisonInterchange as Native
import CertifiedMixedHistoryOrigins
bad : (a : F.Object) (ca : P.Certificate (snd a))
  → Native.closure (fst a , H.root (M.join (M.old (F.unit a)) (M.old (F.unit a))))
    ≡ H.endClosure (M.fold (M.join (M.old (F.unit a)) (M.old (F.unit a))))
bad a ca = refl
