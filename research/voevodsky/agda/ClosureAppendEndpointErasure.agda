{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureAppendEndpointErasure where

open import Cubical.Foundations.Prelude
import ClosureAppendInduction as Original
import ClosureAppendBothEndpointInduction as Both

module Erasure (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module Old = Original.Induction K Piece Boundary attachL attachR
  module New = Both.Induction K Piece Boundary attachL attachR
  open Old.C.D.G.G.A.N

  forget : {a b c d e f : K} {u : Word a b} {v : Word c d} {w : Word e f} →
    New.C.Words.AppendData u v w → Old.C.Words.AppendData u v w
  forget {u = u} {v} {w} data′ = First.pointed
    (Full.AppendData.square data′) (Full.AppendData.firstCoherence data′)
    where
    module First = Old.C.Words u v w
    module Full = New.C.Words u v w

  module Check {a b c d e f : K} (u : Word a b) (v : Word c d) (w : Word e f) where
    module First = Old.C.Words u v w
    module Full = New.C.Words u v w
    retainsSquare : (data′ : Full.AppendData) →
      First.AppendData.square (forget data′) ≡ Full.AppendData.square data′
    retainsSquare data′ = refl

  firstAware : {a b c d e f : K} (u : Word a b) (v : Word c d) (w : Word e f) →
    Old.C.Words.AppendData u v w
  firstAware u v w = forget (New.coherentAppend u v w)

-- This projection retains the NEW square. Equality with Old.coherentAppend
-- is not asserted: adding a dependent field changes transport computation.
-- No proof irrelevance for normalization squares is used.
