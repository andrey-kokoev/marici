{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEdgeNaturalityBadOrder where
open import Cubical.Data.Bool.Base using (false)
open import RamseySingleFrameFaces using (m0)
open import RamseyNativeEdgeAttachments using (e01)
import RamseyRequestedPortExamples as C
import RamseyEdgeAttachmentsExamples as E
open import RamseyEdgeNaturality
bad : E.A.VertexPermit C.q7 m0
bad = E.A.restrict false C.q7 e01 (move-0-0 E.att-0-2-0)
