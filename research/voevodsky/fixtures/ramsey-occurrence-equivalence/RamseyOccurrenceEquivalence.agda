{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyOccurrenceEquivalence where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Foundations.Isomorphism using (iso; isoToEquiv)
open import Cubical.Data.Unit.Base using (tt)
open import RamseySingleFrameFaces using (c0; m0; c1; m1)
import RamseyRequestedPortExamples as C
import RamseyEdgeAttachmentsExamples as E
import RamseyFourFacetVertexCells as F
import RamseyPermitEquivalence as M
open import RamseyExternalPEExamples
data Transports : P.S.InputIndex → P.S.InputIndex → Type where
  input-0-0 : (p : E.A.VertexPermit C.q0 c0) → Transports (C.q0 , (c0 , p)) (C.q7 , (m0 , M.move-0-0 p))
  input-0-1 : (p : E.A.VertexPermit C.q0 m0) → Transports (C.q0 , (m0 , p)) (C.q7 , (c0 , M.move-0-1 p))
  input-0-2 : (p : E.A.VertexPermit C.q0 c1) → Transports (C.q0 , (c1 , p)) (C.q7 , (m1 , M.move-0-2 p))
  input-0-3 : (p : E.A.VertexPermit C.q0 m1) → Transports (C.q0 , (m1 , p)) (C.q7 , (c1 , M.move-0-3 p))
  input-7-0 : (p : E.A.VertexPermit C.q7 c0) → Transports (C.q7 , (c0 , p)) (C.q0 , (m0 , M.move-7-0 p))
  input-7-1 : (p : E.A.VertexPermit C.q7 m0) → Transports (C.q7 , (m0 , p)) (C.q0 , (c0 , M.move-7-1 p))
  input-7-2 : (p : E.A.VertexPermit C.q7 c1) → Transports (C.q7 , (c1 , p)) (C.q0 , (m1 , M.move-7-2 p))
  input-7-3 : (p : E.A.VertexPermit C.q7 m1) → Transports (C.q7 , (m1 , p)) (C.q0 , (c1 , M.move-7-3 p))
move-0-1-2 : P.T.Occurrence tree-0-1-2 → P.T.Occurrence tree-1-0-3
move-0-1-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-0-1-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-0-1-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-0-1-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-0-1-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-0-1-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-0-1-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-0-1-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-0-1-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-0-1-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-0-1-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-0-1-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-0-1-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-0-1-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-0-1-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-0-1-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-0-1-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-0-1-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-0-1-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-0-1-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-0-1-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-0-1-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-0-1-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-0-1-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-0-1-2 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-0-1-2 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-0-1-2 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-0-1-3 : P.T.Occurrence tree-0-1-3 → P.T.Occurrence tree-1-0-2
move-0-1-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-0-1-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-0-1-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-0-1-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-0-1-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-0-1-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-0-1-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-0-1-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-0-1-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-0-1-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-0-1-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-0-1-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-0-1-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-0-1-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-0-1-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-0-1-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-0-1-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-0-1-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-0-1-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-0-1-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-0-1-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-0-1-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-0-1-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-0-1-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-0-1-3 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-0-1-3 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-0-1-3 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-0-2-1 : P.T.Occurrence tree-0-2-1 → P.T.Occurrence tree-1-3-0
move-0-2-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-0-2-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-0-2-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-0-2-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-0-2-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-0-2-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-0-2-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-0-2-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-0-2-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-0-2-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-0-2-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-0-2-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-0-2-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-0-2-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-0-2-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-0-2-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-0-2-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-0-2-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-0-2-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-0-2-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-0-2-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-0-2-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-0-2-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-0-2-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-0-2-1 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-0-2-1 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-0-2-1 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-0-2-3 : P.T.Occurrence tree-0-2-3 → P.T.Occurrence tree-1-3-2
move-0-2-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-0-2-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-0-2-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-0-2-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-0-2-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-0-2-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-0-2-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-0-2-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-0-2-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-0-2-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-0-2-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-0-2-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-0-2-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-0-2-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-0-2-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-0-2-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-0-2-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-0-2-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-0-2-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-0-2-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-0-2-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-0-2-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-0-2-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-0-2-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-0-2-3 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-0-2-3 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-0-2-3 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-0-3-1 : P.T.Occurrence tree-0-3-1 → P.T.Occurrence tree-1-2-0
move-0-3-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-0-3-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-0-3-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-0-3-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-0-3-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-0-3-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-0-3-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-0-3-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-0-3-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-0-3-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-0-3-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-0-3-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-0-3-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-0-3-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-0-3-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-0-3-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-0-3-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-0-3-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-0-3-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-0-3-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-0-3-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-0-3-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-0-3-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-0-3-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-0-3-1 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-0-3-1 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-0-3-1 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-0-3-2 : P.T.Occurrence tree-0-3-2 → P.T.Occurrence tree-1-2-3
move-0-3-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-0-3-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-0-3-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-0-3-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-0-3-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-0-3-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-0-3-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-0-3-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-0-3-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-0-3-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-0-3-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-0-3-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-0-3-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-0-3-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-0-3-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-0-3-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-0-3-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-0-3-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-0-3-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-0-3-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-0-3-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-0-3-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-0-3-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-0-3-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-0-3-2 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-0-3-2 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-0-3-2 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-1-0-2 : P.T.Occurrence tree-1-0-2 → P.T.Occurrence tree-0-1-3
move-1-0-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-1-0-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-1-0-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-1-0-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-1-0-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-1-0-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-1-0-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-1-0-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-1-0-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-1-0-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-1-0-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-1-0-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-1-0-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-1-0-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-1-0-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-1-0-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-1-0-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-1-0-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-1-0-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-1-0-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-1-0-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-1-0-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-1-0-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-1-0-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-1-0-2 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-1-0-2 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-1-0-2 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-1-0-3 : P.T.Occurrence tree-1-0-3 → P.T.Occurrence tree-0-1-2
move-1-0-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-1-0-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-1-0-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-1-0-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-1-0-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-1-0-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-1-0-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-1-0-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-1-0-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-1-0-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-1-0-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-1-0-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-1-0-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-1-0-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-1-0-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-1-0-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-1-0-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-1-0-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-1-0-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-1-0-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-1-0-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-1-0-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-1-0-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-1-0-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-1-0-3 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-1-0-3 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-1-0-3 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-1-2-0 : P.T.Occurrence tree-1-2-0 → P.T.Occurrence tree-0-3-1
move-1-2-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-1-2-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-1-2-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-1-2-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-1-2-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-1-2-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-1-2-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-1-2-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-1-2-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-1-2-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-1-2-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-1-2-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-1-2-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-1-2-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-1-2-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-1-2-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-1-2-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-1-2-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-1-2-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-1-2-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-1-2-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-1-2-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-1-2-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-1-2-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-1-2-0 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-1-2-0 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-1-2-0 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-1-2-3 : P.T.Occurrence tree-1-2-3 → P.T.Occurrence tree-0-3-2
move-1-2-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-1-2-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-1-2-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-1-2-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-1-2-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-1-2-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-1-2-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-1-2-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-1-2-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-1-2-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-1-2-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-1-2-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-1-2-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-1-2-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-1-2-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-1-2-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-1-2-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-1-2-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-1-2-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-1-2-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-1-2-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-1-2-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-1-2-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-1-2-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-1-2-3 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-1-2-3 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-1-2-3 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-1-3-0 : P.T.Occurrence tree-1-3-0 → P.T.Occurrence tree-0-2-1
move-1-3-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-1-3-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-1-3-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-1-3-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-1-3-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-1-3-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-1-3-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-1-3-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-1-3-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-1-3-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-1-3-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-1-3-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-1-3-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-1-3-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-1-3-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-1-3-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-1-3-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-1-3-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-1-3-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-1-3-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-1-3-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-1-3-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-1-3-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-1-3-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-1-3-0 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-1-3-0 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-1-3-0 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-1-3-2 : P.T.Occurrence tree-1-3-2 → P.T.Occurrence tree-0-2-3
move-1-3-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-1-3-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-1-3-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-1-3-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-1-3-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-1-3-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-1-3-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-1-3-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-1-3-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-1-3-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-1-3-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-1-3-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-1-3-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-1-3-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-1-3-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-1-3-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-1-3-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-1-3-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-1-3-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-1-3-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-1-3-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-1-3-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-1-3-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-1-3-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-1-3-2 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-1-3-2 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-1-3-2 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-2-0-1 : P.T.Occurrence tree-2-0-1 → P.T.Occurrence tree-3-1-0
move-2-0-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-2-0-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-2-0-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-2-0-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-2-0-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-2-0-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-2-0-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-2-0-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-2-0-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-2-0-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-2-0-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-2-0-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-2-0-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-2-0-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-2-0-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-2-0-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-2-0-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-2-0-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-2-0-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-2-0-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-2-0-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-2-0-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-2-0-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-2-0-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-2-0-1 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-2-0-1 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-2-0-1 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-2-0-3 : P.T.Occurrence tree-2-0-3 → P.T.Occurrence tree-3-1-2
move-2-0-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-2-0-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-2-0-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-2-0-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-2-0-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-2-0-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-2-0-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-2-0-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-2-0-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-2-0-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-2-0-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-2-0-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-2-0-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-2-0-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-2-0-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-2-0-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-2-0-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-2-0-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-2-0-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-2-0-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-2-0-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-2-0-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-2-0-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-2-0-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-2-0-3 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-2-0-3 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-2-0-3 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-2-1-0 : P.T.Occurrence tree-2-1-0 → P.T.Occurrence tree-3-0-1
move-2-1-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-2-1-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-2-1-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-2-1-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-2-1-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-2-1-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-2-1-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-2-1-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-2-1-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-2-1-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-2-1-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-2-1-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-2-1-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-2-1-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-2-1-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-2-1-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-2-1-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-2-1-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-2-1-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-2-1-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-2-1-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-2-1-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-2-1-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-2-1-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-2-1-0 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-2-1-0 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-2-1-0 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-2-1-3 : P.T.Occurrence tree-2-1-3 → P.T.Occurrence tree-3-0-2
move-2-1-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-2-1-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-2-1-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-2-1-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-2-1-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-2-1-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-2-1-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-2-1-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-2-1-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-2-1-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-2-1-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-2-1-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-2-1-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-2-1-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-2-1-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-2-1-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-2-1-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-2-1-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-2-1-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-2-1-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-2-1-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-2-1-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-2-1-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-2-1-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-2-1-3 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-2-1-3 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-2-1-3 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-2-3-0 : P.T.Occurrence tree-2-3-0 → P.T.Occurrence tree-3-2-1
move-2-3-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-2-3-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-2-3-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-2-3-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-2-3-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-2-3-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-2-3-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-2-3-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-2-3-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-2-3-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-2-3-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-2-3-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-2-3-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-2-3-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-2-3-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-2-3-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-2-3-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-2-3-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-2-3-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-2-3-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-2-3-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-2-3-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-2-3-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-2-3-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-2-3-0 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-2-3-0 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-2-3-0 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-2-3-1 : P.T.Occurrence tree-2-3-1 → P.T.Occurrence tree-3-2-0
move-2-3-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-2-3-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-2-3-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-2-3-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-2-3-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-2-3-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-2-3-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-2-3-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-2-3-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-2-3-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-2-3-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-2-3-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-2-3-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-2-3-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-2-3-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-2-3-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-2-3-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-2-3-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-2-3-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-2-3-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-2-3-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-2-3-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-2-3-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-2-3-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-2-3-1 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-2-3-1 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-2-3-1 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-3-0-1 : P.T.Occurrence tree-3-0-1 → P.T.Occurrence tree-2-1-0
move-3-0-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-3-0-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-3-0-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-3-0-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-3-0-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-3-0-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-3-0-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-3-0-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-3-0-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-3-0-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-3-0-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-3-0-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-3-0-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-3-0-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-3-0-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-3-0-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-3-0-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-3-0-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-3-0-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-3-0-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-3-0-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-3-0-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-3-0-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-3-0-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-3-0-1 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-3-0-1 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-3-0-1 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-3-0-2 : P.T.Occurrence tree-3-0-2 → P.T.Occurrence tree-2-1-3
move-3-0-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-3-0-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-3-0-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-3-0-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-3-0-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-3-0-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-3-0-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-3-0-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-3-0-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-3-0-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-3-0-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-3-0-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-3-0-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-3-0-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-3-0-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-3-0-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-3-0-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-3-0-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-3-0-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-3-0-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-3-0-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-3-0-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-3-0-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-3-0-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-3-0-2 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-3-0-2 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-3-0-2 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-3-1-0 : P.T.Occurrence tree-3-1-0 → P.T.Occurrence tree-2-0-1
move-3-1-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-3-1-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-3-1-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-3-1-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-3-1-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-3-1-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-3-1-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-3-1-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-3-1-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-3-1-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-3-1-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-3-1-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-3-1-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-3-1-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-3-1-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-3-1-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-3-1-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-3-1-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-3-1-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-3-1-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-3-1-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-3-1-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-3-1-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-3-1-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-3-1-0 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-3-1-0 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-3-1-0 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-3-1-2 : P.T.Occurrence tree-3-1-2 → P.T.Occurrence tree-2-0-3
move-3-1-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-3-1-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-3-1-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-3-1-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-3-1-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-3-1-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-3-1-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-3-1-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-3-1-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-3-1-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-3-1-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-3-1-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-3-1-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-3-1-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-3-1-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-3-1-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-3-1-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-3-1-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-3-1-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-3-1-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-3-1-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-3-1-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-3-1-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-3-1-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-3-1-2 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-3-1-2 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-3-1-2 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-3-2-0 : P.T.Occurrence tree-3-2-0 → P.T.Occurrence tree-2-3-1
move-3-2-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-3-2-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-3-2-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-3-2-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-3-2-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-3-2-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-3-2-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-3-2-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-3-2-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-3-2-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-3-2-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-3-2-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-3-2-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-3-2-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-3-2-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-3-2-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-3-2-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-3-2-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-3-2-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-3-2-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-3-2-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-3-2-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-3-2-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-3-2-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-3-2-0 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-3-2-0 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-3-2-0 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
move-3-2-1 : P.T.Occurrence tree-3-2-1 → P.T.Occurrence tree-2-3-0
move-3-2-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.source-leg , tt)))
move-3-2-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m0 , (M.move-7-0 p , M.move-0-0 q)) , (P.S.target-leg , tt)))
move-3-2-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.source-leg , tt)))
move-3-2-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c0 , (M.move-7-1 p , M.move-0-1 q)) , (P.S.target-leg , tt)))
move-3-2-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.source-leg , tt)))
move-3-2-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((m1 , (M.move-7-2 p , M.move-0-2 q)) , (P.S.target-leg , tt)))
move-3-2-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.source-leg , tt)))
move-3-2-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AB , ((c1 , (M.move-7-3 p , M.move-0-3 q)) , (P.S.target-leg , tt)))
move-3-2-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-3-2-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m0 , (M.move-0-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-3-2-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-3-2-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c0 , (M.move-0-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-3-2-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-3-2-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((m1 , (M.move-0-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-3-2-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-3-2-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.BC , ((c1 , (M.move-0-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-3-2-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.source-leg , tt)))
move-3-2-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m0 , (M.move-7-0 p , M.move-7-0 q)) , (P.S.target-leg , tt)))
move-3-2-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.source-leg , tt)))
move-3-2-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c0 , (M.move-7-1 p , M.move-7-1 q)) , (P.S.target-leg , tt)))
move-3-2-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.source-leg , tt)))
move-3-2-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((m1 , (M.move-7-2 p , M.move-7-2 q)) , (P.S.target-leg , tt)))
move-3-2-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.source-leg , tt)))
move-3-2-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = (P.S.AC , ((c1 , (M.move-7-3 p , M.move-7-3 q)) , (P.S.target-leg , tt)))
move-3-2-1 (P.S.full-source , (P.S.first-port , tt)) = (P.S.full-source , (P.S.first-port , tt))
move-3-2-1 (P.S.full-source , (P.S.middle-port , tt)) = (P.S.full-source , (P.S.middle-port , tt))
move-3-2-1 (P.S.full-source , (P.S.final-port , tt)) = (P.S.full-source , (P.S.final-port , tt))
square-0-1-2 : (o : P.T.Occurrence tree-0-1-2) → move-1-0-3 (move-0-1-2 o) ≡ o
square-0-1-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-0-1-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-0-1-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-0-1-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-0-1-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-0-1-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-0-1-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-0-1-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-0-1-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-0-1-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-0-1-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-0-1-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-0-1-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-0-1-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-0-1-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-0-1-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-0-1-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-0-1-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-0-1-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-0-1-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-0-1-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-0-1-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-0-1-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-0-1-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-0-1-2 (P.S.full-source , (P.S.first-port , tt)) = refl
square-0-1-2 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-0-1-2 (P.S.full-source , (P.S.final-port , tt)) = refl
square-0-1-3 : (o : P.T.Occurrence tree-0-1-3) → move-1-0-2 (move-0-1-3 o) ≡ o
square-0-1-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-0-1-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-0-1-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-0-1-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-0-1-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-0-1-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-0-1-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-0-1-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-0-1-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-0-1-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-0-1-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-0-1-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-0-1-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-0-1-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-0-1-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-0-1-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-0-1-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-0-1-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-0-1-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-0-1-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-0-1-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-0-1-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-0-1-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-0-1-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-0-1-3 (P.S.full-source , (P.S.first-port , tt)) = refl
square-0-1-3 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-0-1-3 (P.S.full-source , (P.S.final-port , tt)) = refl
square-0-2-1 : (o : P.T.Occurrence tree-0-2-1) → move-1-3-0 (move-0-2-1 o) ≡ o
square-0-2-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-0-2-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-0-2-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-0-2-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-0-2-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-0-2-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-0-2-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-0-2-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-0-2-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-0-2-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-0-2-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-0-2-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-0-2-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-0-2-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-0-2-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-0-2-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-0-2-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-0-2-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-0-2-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-0-2-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-0-2-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-0-2-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-0-2-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-0-2-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-0-2-1 (P.S.full-source , (P.S.first-port , tt)) = refl
square-0-2-1 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-0-2-1 (P.S.full-source , (P.S.final-port , tt)) = refl
square-0-2-3 : (o : P.T.Occurrence tree-0-2-3) → move-1-3-2 (move-0-2-3 o) ≡ o
square-0-2-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-0-2-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-0-2-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-0-2-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-0-2-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-0-2-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-0-2-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-0-2-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-0-2-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-0-2-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-0-2-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-0-2-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-0-2-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-0-2-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-0-2-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-0-2-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-0-2-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-0-2-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-0-2-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-0-2-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-0-2-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-0-2-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-0-2-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-0-2-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-0-2-3 (P.S.full-source , (P.S.first-port , tt)) = refl
square-0-2-3 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-0-2-3 (P.S.full-source , (P.S.final-port , tt)) = refl
square-0-3-1 : (o : P.T.Occurrence tree-0-3-1) → move-1-2-0 (move-0-3-1 o) ≡ o
square-0-3-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-0-3-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-0-3-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-0-3-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-0-3-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-0-3-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-0-3-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-0-3-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-0-3-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-0-3-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-0-3-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-0-3-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-0-3-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-0-3-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-0-3-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-0-3-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-0-3-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-0-3-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-0-3-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-0-3-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-0-3-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-0-3-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-0-3-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-0-3-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-0-3-1 (P.S.full-source , (P.S.first-port , tt)) = refl
square-0-3-1 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-0-3-1 (P.S.full-source , (P.S.final-port , tt)) = refl
square-0-3-2 : (o : P.T.Occurrence tree-0-3-2) → move-1-2-3 (move-0-3-2 o) ≡ o
square-0-3-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-0-3-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-0-3-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-0-3-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-0-3-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-0-3-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-0-3-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-0-3-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-0-3-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-0-3-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-0-3-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-0-3-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-0-3-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-0-3-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-0-3-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-0-3-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-0-3-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-0-3-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-0-3-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-0-3-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-0-3-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-0-3-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-0-3-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-0-3-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-0-3-2 (P.S.full-source , (P.S.first-port , tt)) = refl
square-0-3-2 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-0-3-2 (P.S.full-source , (P.S.final-port , tt)) = refl
square-1-0-2 : (o : P.T.Occurrence tree-1-0-2) → move-0-1-3 (move-1-0-2 o) ≡ o
square-1-0-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-1-0-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-1-0-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-1-0-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-1-0-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-1-0-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-1-0-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-1-0-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-1-0-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-1-0-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-1-0-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-1-0-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-1-0-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-1-0-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-1-0-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-1-0-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-1-0-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-1-0-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-1-0-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-1-0-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-1-0-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-1-0-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-1-0-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-1-0-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-1-0-2 (P.S.full-source , (P.S.first-port , tt)) = refl
square-1-0-2 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-1-0-2 (P.S.full-source , (P.S.final-port , tt)) = refl
square-1-0-3 : (o : P.T.Occurrence tree-1-0-3) → move-0-1-2 (move-1-0-3 o) ≡ o
square-1-0-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-1-0-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-1-0-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-1-0-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-1-0-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-1-0-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-1-0-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-1-0-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-1-0-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-1-0-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-1-0-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-1-0-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-1-0-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-1-0-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-1-0-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-1-0-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-1-0-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-1-0-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-1-0-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-1-0-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-1-0-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-1-0-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-1-0-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-1-0-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-1-0-3 (P.S.full-source , (P.S.first-port , tt)) = refl
square-1-0-3 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-1-0-3 (P.S.full-source , (P.S.final-port , tt)) = refl
square-1-2-0 : (o : P.T.Occurrence tree-1-2-0) → move-0-3-1 (move-1-2-0 o) ≡ o
square-1-2-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-1-2-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-1-2-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-1-2-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-1-2-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-1-2-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-1-2-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-1-2-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-1-2-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-1-2-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-1-2-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-1-2-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-1-2-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-1-2-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-1-2-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-1-2-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-1-2-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-1-2-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-1-2-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-1-2-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-1-2-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-1-2-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-1-2-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-1-2-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-1-2-0 (P.S.full-source , (P.S.first-port , tt)) = refl
square-1-2-0 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-1-2-0 (P.S.full-source , (P.S.final-port , tt)) = refl
square-1-2-3 : (o : P.T.Occurrence tree-1-2-3) → move-0-3-2 (move-1-2-3 o) ≡ o
square-1-2-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-1-2-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-1-2-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-1-2-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-1-2-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-1-2-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-1-2-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-1-2-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-1-2-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-1-2-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-1-2-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-1-2-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-1-2-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-1-2-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-1-2-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-1-2-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-1-2-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-1-2-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-1-2-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-1-2-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-1-2-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-1-2-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-1-2-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-1-2-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-1-2-3 (P.S.full-source , (P.S.first-port , tt)) = refl
square-1-2-3 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-1-2-3 (P.S.full-source , (P.S.final-port , tt)) = refl
square-1-3-0 : (o : P.T.Occurrence tree-1-3-0) → move-0-2-1 (move-1-3-0 o) ≡ o
square-1-3-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-1-3-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-1-3-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-1-3-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-1-3-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-1-3-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-1-3-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-1-3-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-1-3-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-1-3-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-1-3-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-1-3-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-1-3-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-1-3-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-1-3-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-1-3-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-1-3-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-1-3-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-1-3-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-1-3-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-1-3-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-1-3-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-1-3-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-1-3-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-1-3-0 (P.S.full-source , (P.S.first-port , tt)) = refl
square-1-3-0 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-1-3-0 (P.S.full-source , (P.S.final-port , tt)) = refl
square-1-3-2 : (o : P.T.Occurrence tree-1-3-2) → move-0-2-3 (move-1-3-2 o) ≡ o
square-1-3-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-1-3-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-1-3-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-1-3-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-1-3-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-1-3-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-1-3-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-1-3-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-1-3-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-1-3-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-1-3-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-1-3-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-1-3-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-1-3-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-1-3-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-1-3-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-1-3-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-1-3-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-1-3-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-1-3-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-1-3-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-1-3-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-1-3-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-1-3-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-1-3-2 (P.S.full-source , (P.S.first-port , tt)) = refl
square-1-3-2 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-1-3-2 (P.S.full-source , (P.S.final-port , tt)) = refl
square-2-0-1 : (o : P.T.Occurrence tree-2-0-1) → move-3-1-0 (move-2-0-1 o) ≡ o
square-2-0-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-2-0-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-2-0-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-2-0-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-2-0-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-2-0-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-2-0-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-2-0-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-2-0-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-2-0-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-2-0-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-2-0-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-2-0-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-2-0-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-2-0-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-2-0-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-2-0-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-2-0-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-2-0-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-2-0-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-2-0-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-2-0-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-2-0-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-2-0-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-2-0-1 (P.S.full-source , (P.S.first-port , tt)) = refl
square-2-0-1 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-2-0-1 (P.S.full-source , (P.S.final-port , tt)) = refl
square-2-0-3 : (o : P.T.Occurrence tree-2-0-3) → move-3-1-2 (move-2-0-3 o) ≡ o
square-2-0-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-2-0-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-2-0-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-2-0-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-2-0-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-2-0-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-2-0-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-2-0-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-2-0-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-2-0-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-2-0-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-2-0-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-2-0-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-2-0-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-2-0-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-2-0-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-2-0-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-2-0-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-2-0-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-2-0-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-2-0-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-2-0-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-2-0-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-2-0-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-2-0-3 (P.S.full-source , (P.S.first-port , tt)) = refl
square-2-0-3 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-2-0-3 (P.S.full-source , (P.S.final-port , tt)) = refl
square-2-1-0 : (o : P.T.Occurrence tree-2-1-0) → move-3-0-1 (move-2-1-0 o) ≡ o
square-2-1-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-2-1-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-2-1-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-2-1-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-2-1-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-2-1-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-2-1-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-2-1-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-2-1-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-2-1-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-2-1-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-2-1-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-2-1-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-2-1-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-2-1-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-2-1-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-2-1-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-2-1-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-2-1-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-2-1-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-2-1-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-2-1-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-2-1-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-2-1-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-2-1-0 (P.S.full-source , (P.S.first-port , tt)) = refl
square-2-1-0 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-2-1-0 (P.S.full-source , (P.S.final-port , tt)) = refl
square-2-1-3 : (o : P.T.Occurrence tree-2-1-3) → move-3-0-2 (move-2-1-3 o) ≡ o
square-2-1-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-2-1-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-2-1-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-2-1-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-2-1-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-2-1-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-2-1-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-2-1-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-2-1-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-2-1-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-2-1-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-2-1-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-2-1-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-2-1-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-2-1-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-2-1-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-2-1-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-2-1-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-2-1-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-2-1-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-2-1-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-2-1-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-2-1-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-2-1-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-2-1-3 (P.S.full-source , (P.S.first-port , tt)) = refl
square-2-1-3 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-2-1-3 (P.S.full-source , (P.S.final-port , tt)) = refl
square-2-3-0 : (o : P.T.Occurrence tree-2-3-0) → move-3-2-1 (move-2-3-0 o) ≡ o
square-2-3-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-2-3-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-2-3-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-2-3-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-2-3-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-2-3-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-2-3-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-2-3-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-2-3-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-2-3-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-2-3-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-2-3-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-2-3-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-2-3-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-2-3-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-2-3-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-2-3-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-2-3-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-2-3-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-2-3-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-2-3-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-2-3-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-2-3-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-2-3-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-2-3-0 (P.S.full-source , (P.S.first-port , tt)) = refl
square-2-3-0 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-2-3-0 (P.S.full-source , (P.S.final-port , tt)) = refl
square-2-3-1 : (o : P.T.Occurrence tree-2-3-1) → move-3-2-0 (move-2-3-1 o) ≡ o
square-2-3-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-2-3-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-2-3-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-2-3-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-2-3-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-2-3-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-2-3-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-2-3-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-2-3-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-2-3-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-2-3-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-2-3-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-2-3-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-2-3-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-2-3-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-2-3-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-2-3-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-2-3-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-2-3-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-2-3-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-2-3-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-2-3-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-2-3-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-2-3-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-2-3-1 (P.S.full-source , (P.S.first-port , tt)) = refl
square-2-3-1 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-2-3-1 (P.S.full-source , (P.S.final-port , tt)) = refl
square-3-0-1 : (o : P.T.Occurrence tree-3-0-1) → move-2-1-0 (move-3-0-1 o) ≡ o
square-3-0-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-3-0-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-3-0-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-3-0-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-3-0-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-3-0-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-3-0-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-3-0-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-3-0-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-3-0-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-3-0-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-3-0-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-3-0-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-3-0-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-3-0-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-3-0-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-3-0-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-3-0-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-3-0-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-3-0-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-3-0-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-3-0-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-3-0-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-3-0-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-3-0-1 (P.S.full-source , (P.S.first-port , tt)) = refl
square-3-0-1 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-3-0-1 (P.S.full-source , (P.S.final-port , tt)) = refl
square-3-0-2 : (o : P.T.Occurrence tree-3-0-2) → move-2-1-3 (move-3-0-2 o) ≡ o
square-3-0-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-3-0-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-3-0-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-3-0-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-3-0-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-3-0-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-3-0-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-3-0-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-3-0-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-3-0-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-3-0-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-3-0-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-3-0-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-3-0-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-3-0-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-3-0-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-3-0-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-3-0-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-3-0-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-3-0-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-3-0-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-3-0-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-3-0-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-3-0-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-3-0-2 (P.S.full-source , (P.S.first-port , tt)) = refl
square-3-0-2 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-3-0-2 (P.S.full-source , (P.S.final-port , tt)) = refl
square-3-1-0 : (o : P.T.Occurrence tree-3-1-0) → move-2-0-1 (move-3-1-0 o) ≡ o
square-3-1-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-3-1-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-3-1-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-3-1-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-3-1-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-3-1-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-3-1-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-3-1-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-3-1-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-3-1-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-3-1-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-3-1-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-3-1-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-3-1-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-3-1-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-3-1-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-3-1-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-3-1-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-3-1-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-3-1-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-3-1-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-3-1-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-3-1-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-3-1-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-3-1-0 (P.S.full-source , (P.S.first-port , tt)) = refl
square-3-1-0 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-3-1-0 (P.S.full-source , (P.S.final-port , tt)) = refl
square-3-1-2 : (o : P.T.Occurrence tree-3-1-2) → move-2-0-3 (move-3-1-2 o) ≡ o
square-3-1-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-3-1-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-3-1-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-3-1-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-3-1-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-3-1-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-3-1-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-3-1-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-3-1-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-3-1-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-3-1-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-3-1-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-3-1-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-3-1-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-3-1-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-3-1-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-3-1-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-3-1-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-3-1-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-3-1-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-3-1-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-3-1-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-3-1-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-3-1-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-3-1-2 (P.S.full-source , (P.S.first-port , tt)) = refl
square-3-1-2 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-3-1-2 (P.S.full-source , (P.S.final-port , tt)) = refl
square-3-2-0 : (o : P.T.Occurrence tree-3-2-0) → move-2-3-1 (move-3-2-0 o) ≡ o
square-3-2-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-3-2-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-3-2-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-3-2-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-3-2-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-3-2-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-3-2-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-3-2-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-3-2-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-3-2-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-3-2-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-3-2-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-3-2-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-3-2-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-3-2-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-3-2-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-3-2-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-3-2-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-3-2-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-3-2-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-3-2-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-3-2-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-3-2-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-3-2-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-3-2-0 (P.S.full-source , (P.S.first-port , tt)) = refl
square-3-2-0 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-3-2-0 (P.S.full-source , (P.S.final-port , tt)) = refl
square-3-2-1 : (o : P.T.Occurrence tree-3-2-1) → move-2-3-0 (move-3-2-1 o) ≡ o
square-3-2-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.source-leg , tt)))
square-3-2-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c0 , (M.square-7-0 p i , M.square-0-0 q i)) , (P.S.target-leg , tt)))
square-3-2-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.source-leg , tt)))
square-3-2-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m0 , (M.square-7-1 p i , M.square-0-1 q i)) , (P.S.target-leg , tt)))
square-3-2-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.source-leg , tt)))
square-3-2-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((c1 , (M.square-7-2 p i , M.square-0-2 q i)) , (P.S.target-leg , tt)))
square-3-2-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.source-leg , tt)))
square-3-2-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AB , ((m1 , (M.square-7-3 p i , M.square-0-3 q i)) , (P.S.target-leg , tt)))
square-3-2-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-3-2-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c0 , (M.square-0-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-3-2-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-3-2-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m0 , (M.square-0-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-3-2-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-3-2-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((c1 , (M.square-0-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-3-2-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-3-2-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.BC , ((m1 , (M.square-0-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-3-2-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.source-leg , tt)))
square-3-2-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c0 , (M.square-7-0 p i , M.square-7-0 q i)) , (P.S.target-leg , tt)))
square-3-2-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.source-leg , tt)))
square-3-2-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m0 , (M.square-7-1 p i , M.square-7-1 q i)) , (P.S.target-leg , tt)))
square-3-2-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.source-leg , tt)))
square-3-2-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((c1 , (M.square-7-2 p i , M.square-7-2 q i)) , (P.S.target-leg , tt)))
square-3-2-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.source-leg , tt)))
square-3-2-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) i = (P.S.AC , ((m1 , (M.square-7-3 p i , M.square-7-3 q i)) , (P.S.target-leg , tt)))
square-3-2-1 (P.S.full-source , (P.S.first-port , tt)) = refl
square-3-2-1 (P.S.full-source , (P.S.middle-port , tt)) = refl
square-3-2-1 (P.S.full-source , (P.S.final-port , tt)) = refl
equiv-0-1-2 : P.T.Occurrence tree-0-1-2 ≃ P.T.Occurrence tree-1-0-3
equiv-0-1-2 = isoToEquiv (iso move-0-1-2 move-1-0-3 square-1-0-3 square-0-1-2)
origin-0-1-2 : (o : P.T.Occurrence tree-0-1-2) → Transports (P.T.origin tree-0-1-2 o) (P.T.origin tree-1-0-3 (move-0-1-2 o))
origin-0-1-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-0-1-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-0-1-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-0-1-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-0-1-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-0-1-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-0-1-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-0-1-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-0-1-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-0-1-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-0-1-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-0-1-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-0-1-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-0-1-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-0-1-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-0-1-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-0-1-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-0-1-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-0-1-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-0-1-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-0-1-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-0-1-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-0-1-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-0-1-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-0-1-2 (P.S.full-source , (P.S.first-port , tt)) = input-0-3 F.vp-0-3
origin-0-1-2 (P.S.full-source , (P.S.middle-port , tt)) = input-7-3 F.vp-1-3
origin-0-1-2 (P.S.full-source , (P.S.final-port , tt)) = input-0-3 F.vp-2-3
selected-0-1-2-AB-source-leg : move-0-1-2 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
selected-0-1-2-AB-source-leg = refl
selected-0-1-2-AB-target-leg : move-0-1-2 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
selected-0-1-2-AB-target-leg = refl
selected-0-1-2-BC-source-leg : move-0-1-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
selected-0-1-2-BC-source-leg = refl
selected-0-1-2-BC-target-leg : move-0-1-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
selected-0-1-2-BC-target-leg = refl
selected-0-1-2-AC-source-leg : move-0-1-2 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
selected-0-1-2-AC-source-leg = refl
selected-0-1-2-AC-target-leg : move-0-1-2 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
selected-0-1-2-AC-target-leg = refl
equiv-0-1-3 : P.T.Occurrence tree-0-1-3 ≃ P.T.Occurrence tree-1-0-2
equiv-0-1-3 = isoToEquiv (iso move-0-1-3 move-1-0-2 square-1-0-2 square-0-1-3)
origin-0-1-3 : (o : P.T.Occurrence tree-0-1-3) → Transports (P.T.origin tree-0-1-3 o) (P.T.origin tree-1-0-2 (move-0-1-3 o))
origin-0-1-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-0-1-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-0-1-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-0-1-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-0-1-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-0-1-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-0-1-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-0-1-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-0-1-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-0-1-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-0-1-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-0-1-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-0-1-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-0-1-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-0-1-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-0-1-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-0-1-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-0-1-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-0-1-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-0-1-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-0-1-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-0-1-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-0-1-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-0-1-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-0-1-3 (P.S.full-source , (P.S.first-port , tt)) = input-0-2 F.vp-0-2
origin-0-1-3 (P.S.full-source , (P.S.middle-port , tt)) = input-7-2 F.vp-1-2
origin-0-1-3 (P.S.full-source , (P.S.final-port , tt)) = input-7-2 F.vp-3-2
selected-0-1-3-AB-source-leg : move-0-1-3 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
selected-0-1-3-AB-source-leg = refl
selected-0-1-3-AB-target-leg : move-0-1-3 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
selected-0-1-3-AB-target-leg = refl
selected-0-1-3-BC-source-leg : move-0-1-3 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
selected-0-1-3-BC-source-leg = refl
selected-0-1-3-BC-target-leg : move-0-1-3 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
selected-0-1-3-BC-target-leg = refl
selected-0-1-3-AC-source-leg : move-0-1-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
selected-0-1-3-AC-source-leg = refl
selected-0-1-3-AC-target-leg : move-0-1-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
selected-0-1-3-AC-target-leg = refl
equiv-0-2-1 : P.T.Occurrence tree-0-2-1 ≃ P.T.Occurrence tree-1-3-0
equiv-0-2-1 = isoToEquiv (iso move-0-2-1 move-1-3-0 square-1-3-0 square-0-2-1)
origin-0-2-1 : (o : P.T.Occurrence tree-0-2-1) → Transports (P.T.origin tree-0-2-1 o) (P.T.origin tree-1-3-0 (move-0-2-1 o))
origin-0-2-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-0-2-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-0-2-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-0-2-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-0-2-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-0-2-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-0-2-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-0-2-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-0-2-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-0-2-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-0-2-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-0-2-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-0-2-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-0-2-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-0-2-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-0-2-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-0-2-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-0-2-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-0-2-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-0-2-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-0-2-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-0-2-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-0-2-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-0-2-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-0-2-1 (P.S.full-source , (P.S.first-port , tt)) = input-0-3 F.vp-0-3
origin-0-2-1 (P.S.full-source , (P.S.middle-port , tt)) = input-0-3 F.vp-2-3
origin-0-2-1 (P.S.full-source , (P.S.final-port , tt)) = input-7-3 F.vp-1-3
selected-0-2-1-AB-source-leg : move-0-2-1 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
selected-0-2-1-AB-source-leg = refl
selected-0-2-1-AB-target-leg : move-0-2-1 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
selected-0-2-1-AB-target-leg = refl
selected-0-2-1-BC-source-leg : move-0-2-1 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
selected-0-2-1-BC-source-leg = refl
selected-0-2-1-BC-target-leg : move-0-2-1 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
selected-0-2-1-BC-target-leg = refl
selected-0-2-1-AC-source-leg : move-0-2-1 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
selected-0-2-1-AC-source-leg = refl
selected-0-2-1-AC-target-leg : move-0-2-1 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
selected-0-2-1-AC-target-leg = refl
equiv-0-2-3 : P.T.Occurrence tree-0-2-3 ≃ P.T.Occurrence tree-1-3-2
equiv-0-2-3 = isoToEquiv (iso move-0-2-3 move-1-3-2 square-1-3-2 square-0-2-3)
origin-0-2-3 : (o : P.T.Occurrence tree-0-2-3) → Transports (P.T.origin tree-0-2-3 o) (P.T.origin tree-1-3-2 (move-0-2-3 o))
origin-0-2-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-0-2-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-0-2-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-0-2-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-0-2-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-0-2-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-0-2-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-0-2-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-0-2-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-0-2-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-0-2-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-0-2-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-0-2-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-0-2-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-0-2-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-0-2-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-0-2-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-0-2-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-0-2-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-0-2-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-0-2-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-0-2-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-0-2-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-0-2-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-0-2-3 (P.S.full-source , (P.S.first-port , tt)) = input-0-1 F.vp-0-1
origin-0-2-3 (P.S.full-source , (P.S.middle-port , tt)) = input-0-1 F.vp-2-1
origin-0-2-3 (P.S.full-source , (P.S.final-port , tt)) = input-7-1 F.vp-3-1
selected-0-2-3-AB-source-leg : move-0-2-3 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
selected-0-2-3-AB-source-leg = refl
selected-0-2-3-AB-target-leg : move-0-2-3 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
selected-0-2-3-AB-target-leg = refl
selected-0-2-3-BC-source-leg : move-0-2-3 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
selected-0-2-3-BC-source-leg = refl
selected-0-2-3-BC-target-leg : move-0-2-3 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
selected-0-2-3-BC-target-leg = refl
selected-0-2-3-AC-source-leg : move-0-2-3 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
selected-0-2-3-AC-source-leg = refl
selected-0-2-3-AC-target-leg : move-0-2-3 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
selected-0-2-3-AC-target-leg = refl
equiv-0-3-1 : P.T.Occurrence tree-0-3-1 ≃ P.T.Occurrence tree-1-2-0
equiv-0-3-1 = isoToEquiv (iso move-0-3-1 move-1-2-0 square-1-2-0 square-0-3-1)
origin-0-3-1 : (o : P.T.Occurrence tree-0-3-1) → Transports (P.T.origin tree-0-3-1 o) (P.T.origin tree-1-2-0 (move-0-3-1 o))
origin-0-3-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-0-3-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-0-3-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-0-3-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-0-3-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-0-3-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-0-3-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-0-3-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-0-3-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-0-3-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-0-3-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-0-3-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-0-3-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-0-3-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-0-3-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-0-3-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-0-3-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-0-3-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-0-3-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-0-3-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-0-3-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-0-3-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-0-3-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-0-3-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-0-3-1 (P.S.full-source , (P.S.first-port , tt)) = input-0-2 F.vp-0-2
origin-0-3-1 (P.S.full-source , (P.S.middle-port , tt)) = input-7-2 F.vp-3-2
origin-0-3-1 (P.S.full-source , (P.S.final-port , tt)) = input-7-2 F.vp-1-2
selected-0-3-1-AB-source-leg : move-0-3-1 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
selected-0-3-1-AB-source-leg = refl
selected-0-3-1-AB-target-leg : move-0-3-1 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
selected-0-3-1-AB-target-leg = refl
selected-0-3-1-BC-source-leg : move-0-3-1 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
selected-0-3-1-BC-source-leg = refl
selected-0-3-1-BC-target-leg : move-0-3-1 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
selected-0-3-1-BC-target-leg = refl
selected-0-3-1-AC-source-leg : move-0-3-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
selected-0-3-1-AC-source-leg = refl
selected-0-3-1-AC-target-leg : move-0-3-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
selected-0-3-1-AC-target-leg = refl
equiv-0-3-2 : P.T.Occurrence tree-0-3-2 ≃ P.T.Occurrence tree-1-2-3
equiv-0-3-2 = isoToEquiv (iso move-0-3-2 move-1-2-3 square-1-2-3 square-0-3-2)
origin-0-3-2 : (o : P.T.Occurrence tree-0-3-2) → Transports (P.T.origin tree-0-3-2 o) (P.T.origin tree-1-2-3 (move-0-3-2 o))
origin-0-3-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-0-3-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-0-3-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-0-3-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-0-3-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-0-3-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-0-3-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-0-3-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-0-3-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-0-3-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-0-3-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-0-3-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-0-3-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-0-3-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-0-3-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-0-3-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-0-3-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-0-3-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-0-3-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-0-3-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-0-3-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-0-3-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-0-3-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-0-3-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-0-3-2 (P.S.full-source , (P.S.first-port , tt)) = input-0-1 F.vp-0-1
origin-0-3-2 (P.S.full-source , (P.S.middle-port , tt)) = input-7-1 F.vp-3-1
origin-0-3-2 (P.S.full-source , (P.S.final-port , tt)) = input-0-1 F.vp-2-1
selected-0-3-2-AB-source-leg : move-0-3-2 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
selected-0-3-2-AB-source-leg = refl
selected-0-3-2-AB-target-leg : move-0-3-2 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
selected-0-3-2-AB-target-leg = refl
selected-0-3-2-BC-source-leg : move-0-3-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
selected-0-3-2-BC-source-leg = refl
selected-0-3-2-BC-target-leg : move-0-3-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
selected-0-3-2-BC-target-leg = refl
selected-0-3-2-AC-source-leg : move-0-3-2 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
selected-0-3-2-AC-source-leg = refl
selected-0-3-2-AC-target-leg : move-0-3-2 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
selected-0-3-2-AC-target-leg = refl
equiv-1-0-2 : P.T.Occurrence tree-1-0-2 ≃ P.T.Occurrence tree-0-1-3
equiv-1-0-2 = isoToEquiv (iso move-1-0-2 move-0-1-3 square-0-1-3 square-1-0-2)
origin-1-0-2 : (o : P.T.Occurrence tree-1-0-2) → Transports (P.T.origin tree-1-0-2 o) (P.T.origin tree-0-1-3 (move-1-0-2 o))
origin-1-0-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-1-0-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-1-0-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-1-0-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-1-0-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-1-0-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-1-0-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-1-0-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-1-0-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-1-0-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-1-0-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-1-0-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-1-0-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-1-0-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-1-0-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-1-0-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-1-0-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-1-0-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-1-0-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-1-0-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-1-0-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-1-0-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-1-0-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-1-0-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-1-0-2 (P.S.full-source , (P.S.first-port , tt)) = input-7-3 F.vp-1-3
origin-1-0-2 (P.S.full-source , (P.S.middle-port , tt)) = input-0-3 F.vp-0-3
origin-1-0-2 (P.S.full-source , (P.S.final-port , tt)) = input-0-3 F.vp-2-3
selected-1-0-2-AB-source-leg : move-1-0-2 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
selected-1-0-2-AB-source-leg = refl
selected-1-0-2-AB-target-leg : move-1-0-2 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
selected-1-0-2-AB-target-leg = refl
selected-1-0-2-BC-source-leg : move-1-0-2 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
selected-1-0-2-BC-source-leg = refl
selected-1-0-2-BC-target-leg : move-1-0-2 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
selected-1-0-2-BC-target-leg = refl
selected-1-0-2-AC-source-leg : move-1-0-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
selected-1-0-2-AC-source-leg = refl
selected-1-0-2-AC-target-leg : move-1-0-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
selected-1-0-2-AC-target-leg = refl
equiv-1-0-3 : P.T.Occurrence tree-1-0-3 ≃ P.T.Occurrence tree-0-1-2
equiv-1-0-3 = isoToEquiv (iso move-1-0-3 move-0-1-2 square-0-1-2 square-1-0-3)
origin-1-0-3 : (o : P.T.Occurrence tree-1-0-3) → Transports (P.T.origin tree-1-0-3 o) (P.T.origin tree-0-1-2 (move-1-0-3 o))
origin-1-0-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-1-0-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-1-0-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-1-0-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-1-0-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-1-0-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-1-0-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-1-0-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-1-0-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-1-0-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-1-0-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-1-0-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-1-0-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-1-0-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-1-0-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-1-0-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-1-0-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-1-0-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-1-0-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-1-0-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-1-0-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-1-0-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-1-0-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-1-0-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-1-0-3 (P.S.full-source , (P.S.first-port , tt)) = input-7-2 F.vp-1-2
origin-1-0-3 (P.S.full-source , (P.S.middle-port , tt)) = input-0-2 F.vp-0-2
origin-1-0-3 (P.S.full-source , (P.S.final-port , tt)) = input-7-2 F.vp-3-2
selected-1-0-3-AB-source-leg : move-1-0-3 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
selected-1-0-3-AB-source-leg = refl
selected-1-0-3-AB-target-leg : move-1-0-3 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
selected-1-0-3-AB-target-leg = refl
selected-1-0-3-BC-source-leg : move-1-0-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
selected-1-0-3-BC-source-leg = refl
selected-1-0-3-BC-target-leg : move-1-0-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
selected-1-0-3-BC-target-leg = refl
selected-1-0-3-AC-source-leg : move-1-0-3 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
selected-1-0-3-AC-source-leg = refl
selected-1-0-3-AC-target-leg : move-1-0-3 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
selected-1-0-3-AC-target-leg = refl
equiv-1-2-0 : P.T.Occurrence tree-1-2-0 ≃ P.T.Occurrence tree-0-3-1
equiv-1-2-0 = isoToEquiv (iso move-1-2-0 move-0-3-1 square-0-3-1 square-1-2-0)
origin-1-2-0 : (o : P.T.Occurrence tree-1-2-0) → Transports (P.T.origin tree-1-2-0 o) (P.T.origin tree-0-3-1 (move-1-2-0 o))
origin-1-2-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-1-2-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-1-2-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-1-2-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-1-2-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-1-2-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-1-2-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-1-2-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-1-2-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-1-2-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-1-2-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-1-2-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-1-2-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-1-2-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-1-2-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-1-2-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-1-2-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-1-2-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-1-2-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-1-2-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-1-2-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-1-2-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-1-2-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-1-2-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-1-2-0 (P.S.full-source , (P.S.first-port , tt)) = input-7-3 F.vp-1-3
origin-1-2-0 (P.S.full-source , (P.S.middle-port , tt)) = input-0-3 F.vp-2-3
origin-1-2-0 (P.S.full-source , (P.S.final-port , tt)) = input-0-3 F.vp-0-3
selected-1-2-0-AB-source-leg : move-1-2-0 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
selected-1-2-0-AB-source-leg = refl
selected-1-2-0-AB-target-leg : move-1-2-0 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
selected-1-2-0-AB-target-leg = refl
selected-1-2-0-BC-source-leg : move-1-2-0 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
selected-1-2-0-BC-source-leg = refl
selected-1-2-0-BC-target-leg : move-1-2-0 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
selected-1-2-0-BC-target-leg = refl
selected-1-2-0-AC-source-leg : move-1-2-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
selected-1-2-0-AC-source-leg = refl
selected-1-2-0-AC-target-leg : move-1-2-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
selected-1-2-0-AC-target-leg = refl
equiv-1-2-3 : P.T.Occurrence tree-1-2-3 ≃ P.T.Occurrence tree-0-3-2
equiv-1-2-3 = isoToEquiv (iso move-1-2-3 move-0-3-2 square-0-3-2 square-1-2-3)
origin-1-2-3 : (o : P.T.Occurrence tree-1-2-3) → Transports (P.T.origin tree-1-2-3 o) (P.T.origin tree-0-3-2 (move-1-2-3 o))
origin-1-2-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-1-2-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-1-2-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-1-2-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-1-2-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-1-2-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-1-2-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-1-2-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-1-2-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-1-2-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-1-2-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-1-2-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-1-2-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-1-2-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-1-2-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-1-2-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-1-2-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-1-2-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-1-2-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-1-2-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-1-2-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-1-2-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-1-2-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-1-2-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-1-2-3 (P.S.full-source , (P.S.first-port , tt)) = input-7-0 F.vp-1-0
origin-1-2-3 (P.S.full-source , (P.S.middle-port , tt)) = input-0-0 F.vp-2-0
origin-1-2-3 (P.S.full-source , (P.S.final-port , tt)) = input-7-0 F.vp-3-0
selected-1-2-3-AB-source-leg : move-1-2-3 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
selected-1-2-3-AB-source-leg = refl
selected-1-2-3-AB-target-leg : move-1-2-3 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
selected-1-2-3-AB-target-leg = refl
selected-1-2-3-BC-source-leg : move-1-2-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
selected-1-2-3-BC-source-leg = refl
selected-1-2-3-BC-target-leg : move-1-2-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
selected-1-2-3-BC-target-leg = refl
selected-1-2-3-AC-source-leg : move-1-2-3 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
selected-1-2-3-AC-source-leg = refl
selected-1-2-3-AC-target-leg : move-1-2-3 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
selected-1-2-3-AC-target-leg = refl
equiv-1-3-0 : P.T.Occurrence tree-1-3-0 ≃ P.T.Occurrence tree-0-2-1
equiv-1-3-0 = isoToEquiv (iso move-1-3-0 move-0-2-1 square-0-2-1 square-1-3-0)
origin-1-3-0 : (o : P.T.Occurrence tree-1-3-0) → Transports (P.T.origin tree-1-3-0 o) (P.T.origin tree-0-2-1 (move-1-3-0 o))
origin-1-3-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-1-3-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-1-3-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-1-3-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-1-3-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-1-3-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-1-3-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-1-3-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-1-3-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-1-3-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-1-3-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-1-3-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-1-3-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-1-3-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-1-3-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-1-3-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-1-3-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-1-3-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-1-3-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-1-3-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-1-3-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-1-3-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-1-3-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-1-3-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-1-3-0 (P.S.full-source , (P.S.first-port , tt)) = input-7-2 F.vp-1-2
origin-1-3-0 (P.S.full-source , (P.S.middle-port , tt)) = input-7-2 F.vp-3-2
origin-1-3-0 (P.S.full-source , (P.S.final-port , tt)) = input-0-2 F.vp-0-2
selected-1-3-0-AB-source-leg : move-1-3-0 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
selected-1-3-0-AB-source-leg = refl
selected-1-3-0-AB-target-leg : move-1-3-0 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
selected-1-3-0-AB-target-leg = refl
selected-1-3-0-BC-source-leg : move-1-3-0 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
selected-1-3-0-BC-source-leg = refl
selected-1-3-0-BC-target-leg : move-1-3-0 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
selected-1-3-0-BC-target-leg = refl
selected-1-3-0-AC-source-leg : move-1-3-0 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
selected-1-3-0-AC-source-leg = refl
selected-1-3-0-AC-target-leg : move-1-3-0 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
selected-1-3-0-AC-target-leg = refl
equiv-1-3-2 : P.T.Occurrence tree-1-3-2 ≃ P.T.Occurrence tree-0-2-3
equiv-1-3-2 = isoToEquiv (iso move-1-3-2 move-0-2-3 square-0-2-3 square-1-3-2)
origin-1-3-2 : (o : P.T.Occurrence tree-1-3-2) → Transports (P.T.origin tree-1-3-2 o) (P.T.origin tree-0-2-3 (move-1-3-2 o))
origin-1-3-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-1-3-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-1-3-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-1-3-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-1-3-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-1-3-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-1-3-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-1-3-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-1-3-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-1-3-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-1-3-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-1-3-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-1-3-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-1-3-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-1-3-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-1-3-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-1-3-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-1-3-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-1-3-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-1-3-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-1-3-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-1-3-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-1-3-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-1-3-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-1-3-2 (P.S.full-source , (P.S.first-port , tt)) = input-7-0 F.vp-1-0
origin-1-3-2 (P.S.full-source , (P.S.middle-port , tt)) = input-7-0 F.vp-3-0
origin-1-3-2 (P.S.full-source , (P.S.final-port , tt)) = input-0-0 F.vp-2-0
selected-1-3-2-AB-source-leg : move-1-3-2 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
selected-1-3-2-AB-source-leg = refl
selected-1-3-2-AB-target-leg : move-1-3-2 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
selected-1-3-2-AB-target-leg = refl
selected-1-3-2-BC-source-leg : move-1-3-2 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
selected-1-3-2-BC-source-leg = refl
selected-1-3-2-BC-target-leg : move-1-3-2 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
selected-1-3-2-BC-target-leg = refl
selected-1-3-2-AC-source-leg : move-1-3-2 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
selected-1-3-2-AC-source-leg = refl
selected-1-3-2-AC-target-leg : move-1-3-2 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
selected-1-3-2-AC-target-leg = refl
equiv-2-0-1 : P.T.Occurrence tree-2-0-1 ≃ P.T.Occurrence tree-3-1-0
equiv-2-0-1 = isoToEquiv (iso move-2-0-1 move-3-1-0 square-3-1-0 square-2-0-1)
origin-2-0-1 : (o : P.T.Occurrence tree-2-0-1) → Transports (P.T.origin tree-2-0-1 o) (P.T.origin tree-3-1-0 (move-2-0-1 o))
origin-2-0-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-2-0-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-2-0-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-2-0-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-2-0-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-2-0-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-2-0-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-2-0-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-2-0-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-2-0-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-2-0-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-2-0-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-2-0-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-2-0-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-2-0-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-2-0-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-2-0-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-2-0-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-2-0-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-2-0-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-2-0-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-2-0-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-2-0-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-2-0-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-2-0-1 (P.S.full-source , (P.S.first-port , tt)) = input-0-3 F.vp-2-3
origin-2-0-1 (P.S.full-source , (P.S.middle-port , tt)) = input-0-3 F.vp-0-3
origin-2-0-1 (P.S.full-source , (P.S.final-port , tt)) = input-7-3 F.vp-1-3
selected-2-0-1-AB-source-leg : move-2-0-1 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
selected-2-0-1-AB-source-leg = refl
selected-2-0-1-AB-target-leg : move-2-0-1 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
selected-2-0-1-AB-target-leg = refl
selected-2-0-1-BC-source-leg : move-2-0-1 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
selected-2-0-1-BC-source-leg = refl
selected-2-0-1-BC-target-leg : move-2-0-1 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
selected-2-0-1-BC-target-leg = refl
selected-2-0-1-AC-source-leg : move-2-0-1 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
selected-2-0-1-AC-source-leg = refl
selected-2-0-1-AC-target-leg : move-2-0-1 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
selected-2-0-1-AC-target-leg = refl
equiv-2-0-3 : P.T.Occurrence tree-2-0-3 ≃ P.T.Occurrence tree-3-1-2
equiv-2-0-3 = isoToEquiv (iso move-2-0-3 move-3-1-2 square-3-1-2 square-2-0-3)
origin-2-0-3 : (o : P.T.Occurrence tree-2-0-3) → Transports (P.T.origin tree-2-0-3 o) (P.T.origin tree-3-1-2 (move-2-0-3 o))
origin-2-0-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-2-0-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-2-0-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-2-0-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-2-0-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-2-0-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-2-0-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-2-0-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-2-0-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-2-0-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-2-0-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-2-0-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-2-0-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-2-0-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-2-0-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-2-0-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-2-0-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-2-0-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-2-0-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-2-0-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-2-0-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-2-0-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-2-0-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-2-0-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-2-0-3 (P.S.full-source , (P.S.first-port , tt)) = input-0-1 F.vp-2-1
origin-2-0-3 (P.S.full-source , (P.S.middle-port , tt)) = input-0-1 F.vp-0-1
origin-2-0-3 (P.S.full-source , (P.S.final-port , tt)) = input-7-1 F.vp-3-1
selected-2-0-3-AB-source-leg : move-2-0-3 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
selected-2-0-3-AB-source-leg = refl
selected-2-0-3-AB-target-leg : move-2-0-3 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
selected-2-0-3-AB-target-leg = refl
selected-2-0-3-BC-source-leg : move-2-0-3 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
selected-2-0-3-BC-source-leg = refl
selected-2-0-3-BC-target-leg : move-2-0-3 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
selected-2-0-3-BC-target-leg = refl
selected-2-0-3-AC-source-leg : move-2-0-3 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
selected-2-0-3-AC-source-leg = refl
selected-2-0-3-AC-target-leg : move-2-0-3 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
selected-2-0-3-AC-target-leg = refl
equiv-2-1-0 : P.T.Occurrence tree-2-1-0 ≃ P.T.Occurrence tree-3-0-1
equiv-2-1-0 = isoToEquiv (iso move-2-1-0 move-3-0-1 square-3-0-1 square-2-1-0)
origin-2-1-0 : (o : P.T.Occurrence tree-2-1-0) → Transports (P.T.origin tree-2-1-0 o) (P.T.origin tree-3-0-1 (move-2-1-0 o))
origin-2-1-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-2-1-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-2-1-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-2-1-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-2-1-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-2-1-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-2-1-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-2-1-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-2-1-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-2-1-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-2-1-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-2-1-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-2-1-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-2-1-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-2-1-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-2-1-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-2-1-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-2-1-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-2-1-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-2-1-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-2-1-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-2-1-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-2-1-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-2-1-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-2-1-0 (P.S.full-source , (P.S.first-port , tt)) = input-0-3 F.vp-2-3
origin-2-1-0 (P.S.full-source , (P.S.middle-port , tt)) = input-7-3 F.vp-1-3
origin-2-1-0 (P.S.full-source , (P.S.final-port , tt)) = input-0-3 F.vp-0-3
selected-2-1-0-AB-source-leg : move-2-1-0 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
selected-2-1-0-AB-source-leg = refl
selected-2-1-0-AB-target-leg : move-2-1-0 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
selected-2-1-0-AB-target-leg = refl
selected-2-1-0-BC-source-leg : move-2-1-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
selected-2-1-0-BC-source-leg = refl
selected-2-1-0-BC-target-leg : move-2-1-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
selected-2-1-0-BC-target-leg = refl
selected-2-1-0-AC-source-leg : move-2-1-0 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
selected-2-1-0-AC-source-leg = refl
selected-2-1-0-AC-target-leg : move-2-1-0 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
selected-2-1-0-AC-target-leg = refl
equiv-2-1-3 : P.T.Occurrence tree-2-1-3 ≃ P.T.Occurrence tree-3-0-2
equiv-2-1-3 = isoToEquiv (iso move-2-1-3 move-3-0-2 square-3-0-2 square-2-1-3)
origin-2-1-3 : (o : P.T.Occurrence tree-2-1-3) → Transports (P.T.origin tree-2-1-3 o) (P.T.origin tree-3-0-2 (move-2-1-3 o))
origin-2-1-3 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-2-1-3 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-2-1-3 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-2-1-3 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-2-1-3 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-2-1-3 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-2-1-3 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-2-1-3 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-2-1-3 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-2-1-3 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-2-1-3 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-2-1-3 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-2-1-3 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-2-1-3 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-2-1-3 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-2-1-3 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-2-1-3 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-2-1-3 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-2-1-3 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-2-1-3 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-2-1-3 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-2-1-3 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-2-1-3 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-2-1-3 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-2-1-3 (P.S.full-source , (P.S.first-port , tt)) = input-0-0 F.vp-2-0
origin-2-1-3 (P.S.full-source , (P.S.middle-port , tt)) = input-7-0 F.vp-1-0
origin-2-1-3 (P.S.full-source , (P.S.final-port , tt)) = input-7-0 F.vp-3-0
selected-2-1-3-AB-source-leg : move-2-1-3 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
selected-2-1-3-AB-source-leg = refl
selected-2-1-3-AB-target-leg : move-2-1-3 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
selected-2-1-3-AB-target-leg = refl
selected-2-1-3-BC-source-leg : move-2-1-3 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
selected-2-1-3-BC-source-leg = refl
selected-2-1-3-BC-target-leg : move-2-1-3 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
selected-2-1-3-BC-target-leg = refl
selected-2-1-3-AC-source-leg : move-2-1-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
selected-2-1-3-AC-source-leg = refl
selected-2-1-3-AC-target-leg : move-2-1-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
selected-2-1-3-AC-target-leg = refl
equiv-2-3-0 : P.T.Occurrence tree-2-3-0 ≃ P.T.Occurrence tree-3-2-1
equiv-2-3-0 = isoToEquiv (iso move-2-3-0 move-3-2-1 square-3-2-1 square-2-3-0)
origin-2-3-0 : (o : P.T.Occurrence tree-2-3-0) → Transports (P.T.origin tree-2-3-0 o) (P.T.origin tree-3-2-1 (move-2-3-0 o))
origin-2-3-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-2-3-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-2-3-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-2-3-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-2-3-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-2-3-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-2-3-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-2-3-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-2-3-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-2-3-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-2-3-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-2-3-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-2-3-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-2-3-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-2-3-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-2-3-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-2-3-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-2-3-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-2-3-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-2-3-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-2-3-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-2-3-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-2-3-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-2-3-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-2-3-0 (P.S.full-source , (P.S.first-port , tt)) = input-0-1 F.vp-2-1
origin-2-3-0 (P.S.full-source , (P.S.middle-port , tt)) = input-7-1 F.vp-3-1
origin-2-3-0 (P.S.full-source , (P.S.final-port , tt)) = input-0-1 F.vp-0-1
selected-2-3-0-AB-source-leg : move-2-3-0 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
selected-2-3-0-AB-source-leg = refl
selected-2-3-0-AB-target-leg : move-2-3-0 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
selected-2-3-0-AB-target-leg = refl
selected-2-3-0-BC-source-leg : move-2-3-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
selected-2-3-0-BC-source-leg = refl
selected-2-3-0-BC-target-leg : move-2-3-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
selected-2-3-0-BC-target-leg = refl
selected-2-3-0-AC-source-leg : move-2-3-0 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
selected-2-3-0-AC-source-leg = refl
selected-2-3-0-AC-target-leg : move-2-3-0 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
selected-2-3-0-AC-target-leg = refl
equiv-2-3-1 : P.T.Occurrence tree-2-3-1 ≃ P.T.Occurrence tree-3-2-0
equiv-2-3-1 = isoToEquiv (iso move-2-3-1 move-3-2-0 square-3-2-0 square-2-3-1)
origin-2-3-1 : (o : P.T.Occurrence tree-2-3-1) → Transports (P.T.origin tree-2-3-1 o) (P.T.origin tree-3-2-0 (move-2-3-1 o))
origin-2-3-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-2-3-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-2-3-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-2-3-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-2-3-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-2-3-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-2-3-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-2-3-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-2-3-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-2-3-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-2-3-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-2-3-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-2-3-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-2-3-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-2-3-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-2-3-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-2-3-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-2-3-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-2-3-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-2-3-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-2-3-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-2-3-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-2-3-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-2-3-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-2-3-1 (P.S.full-source , (P.S.first-port , tt)) = input-0-0 F.vp-2-0
origin-2-3-1 (P.S.full-source , (P.S.middle-port , tt)) = input-7-0 F.vp-3-0
origin-2-3-1 (P.S.full-source , (P.S.final-port , tt)) = input-7-0 F.vp-1-0
selected-2-3-1-AB-source-leg : move-2-3-1 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
selected-2-3-1-AB-source-leg = refl
selected-2-3-1-AB-target-leg : move-2-3-1 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
selected-2-3-1-AB-target-leg = refl
selected-2-3-1-BC-source-leg : move-2-3-1 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
selected-2-3-1-BC-source-leg = refl
selected-2-3-1-BC-target-leg : move-2-3-1 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
selected-2-3-1-BC-target-leg = refl
selected-2-3-1-AC-source-leg : move-2-3-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
selected-2-3-1-AC-source-leg = refl
selected-2-3-1-AC-target-leg : move-2-3-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
selected-2-3-1-AC-target-leg = refl
equiv-3-0-1 : P.T.Occurrence tree-3-0-1 ≃ P.T.Occurrence tree-2-1-0
equiv-3-0-1 = isoToEquiv (iso move-3-0-1 move-2-1-0 square-2-1-0 square-3-0-1)
origin-3-0-1 : (o : P.T.Occurrence tree-3-0-1) → Transports (P.T.origin tree-3-0-1 o) (P.T.origin tree-2-1-0 (move-3-0-1 o))
origin-3-0-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-3-0-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-3-0-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-3-0-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-3-0-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-3-0-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-3-0-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-3-0-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-3-0-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-3-0-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-3-0-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-3-0-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-3-0-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-3-0-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-3-0-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-3-0-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-3-0-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-3-0-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-3-0-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-3-0-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-3-0-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-3-0-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-3-0-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-3-0-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-3-0-1 (P.S.full-source , (P.S.first-port , tt)) = input-7-2 F.vp-3-2
origin-3-0-1 (P.S.full-source , (P.S.middle-port , tt)) = input-0-2 F.vp-0-2
origin-3-0-1 (P.S.full-source , (P.S.final-port , tt)) = input-7-2 F.vp-1-2
selected-3-0-1-AB-source-leg : move-3-0-1 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
selected-3-0-1-AB-source-leg = refl
selected-3-0-1-AB-target-leg : move-3-0-1 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
selected-3-0-1-AB-target-leg = refl
selected-3-0-1-BC-source-leg : move-3-0-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
selected-3-0-1-BC-source-leg = refl
selected-3-0-1-BC-target-leg : move-3-0-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
selected-3-0-1-BC-target-leg = refl
selected-3-0-1-AC-source-leg : move-3-0-1 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
selected-3-0-1-AC-source-leg = refl
selected-3-0-1-AC-target-leg : move-3-0-1 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
selected-3-0-1-AC-target-leg = refl
equiv-3-0-2 : P.T.Occurrence tree-3-0-2 ≃ P.T.Occurrence tree-2-1-3
equiv-3-0-2 = isoToEquiv (iso move-3-0-2 move-2-1-3 square-2-1-3 square-3-0-2)
origin-3-0-2 : (o : P.T.Occurrence tree-3-0-2) → Transports (P.T.origin tree-3-0-2 o) (P.T.origin tree-2-1-3 (move-3-0-2 o))
origin-3-0-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-3-0-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-3-0-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-3-0-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-3-0-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-3-0-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-3-0-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-3-0-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-3-0-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-3-0-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-3-0-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-3-0-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-3-0-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-3-0-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-3-0-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-3-0-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-3-0-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-3-0-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-3-0-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-3-0-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-3-0-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-3-0-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-3-0-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-3-0-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-3-0-2 (P.S.full-source , (P.S.first-port , tt)) = input-7-1 F.vp-3-1
origin-3-0-2 (P.S.full-source , (P.S.middle-port , tt)) = input-0-1 F.vp-0-1
origin-3-0-2 (P.S.full-source , (P.S.final-port , tt)) = input-0-1 F.vp-2-1
selected-3-0-2-AB-source-leg : move-3-0-2 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
selected-3-0-2-AB-source-leg = refl
selected-3-0-2-AB-target-leg : move-3-0-2 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
selected-3-0-2-AB-target-leg = refl
selected-3-0-2-BC-source-leg : move-3-0-2 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
selected-3-0-2-BC-source-leg = refl
selected-3-0-2-BC-target-leg : move-3-0-2 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
selected-3-0-2-BC-target-leg = refl
selected-3-0-2-AC-source-leg : move-3-0-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
selected-3-0-2-AC-source-leg = refl
selected-3-0-2-AC-target-leg : move-3-0-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
selected-3-0-2-AC-target-leg = refl
equiv-3-1-0 : P.T.Occurrence tree-3-1-0 ≃ P.T.Occurrence tree-2-0-1
equiv-3-1-0 = isoToEquiv (iso move-3-1-0 move-2-0-1 square-2-0-1 square-3-1-0)
origin-3-1-0 : (o : P.T.Occurrence tree-3-1-0) → Transports (P.T.origin tree-3-1-0 o) (P.T.origin tree-2-0-1 (move-3-1-0 o))
origin-3-1-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-3-1-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-3-1-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-3-1-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-3-1-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-3-1-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-3-1-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-3-1-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-3-1-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-3-1-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-3-1-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-3-1-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-3-1-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-3-1-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-3-1-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-3-1-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-3-1-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-3-1-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-3-1-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-3-1-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-3-1-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-3-1-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-3-1-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-3-1-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-3-1-0 (P.S.full-source , (P.S.first-port , tt)) = input-7-2 F.vp-3-2
origin-3-1-0 (P.S.full-source , (P.S.middle-port , tt)) = input-7-2 F.vp-1-2
origin-3-1-0 (P.S.full-source , (P.S.final-port , tt)) = input-0-2 F.vp-0-2
selected-3-1-0-AB-source-leg : move-3-1-0 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
selected-3-1-0-AB-source-leg = refl
selected-3-1-0-AB-target-leg : move-3-1-0 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
selected-3-1-0-AB-target-leg = refl
selected-3-1-0-BC-source-leg : move-3-1-0 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
selected-3-1-0-BC-source-leg = refl
selected-3-1-0-BC-target-leg : move-3-1-0 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
selected-3-1-0-BC-target-leg = refl
selected-3-1-0-AC-source-leg : move-3-1-0 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
selected-3-1-0-AC-source-leg = refl
selected-3-1-0-AC-target-leg : move-3-1-0 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
selected-3-1-0-AC-target-leg = refl
equiv-3-1-2 : P.T.Occurrence tree-3-1-2 ≃ P.T.Occurrence tree-2-0-3
equiv-3-1-2 = isoToEquiv (iso move-3-1-2 move-2-0-3 square-2-0-3 square-3-1-2)
origin-3-1-2 : (o : P.T.Occurrence tree-3-1-2) → Transports (P.T.origin tree-3-1-2 o) (P.T.origin tree-2-0-3 (move-3-1-2 o))
origin-3-1-2 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-3-1-2 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-3-1-2 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-3-1-2 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-3-1-2 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-3-1-2 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-3-1-2 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-3-1-2 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-3-1-2 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-3-1-2 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-3-1-2 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-3-1-2 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-3-1-2 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-3-1-2 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-3-1-2 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-3-1-2 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-3-1-2 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-3-1-2 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-3-1-2 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-3-1-2 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-3-1-2 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-3-1-2 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-3-1-2 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-3-1-2 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-3-1-2 (P.S.full-source , (P.S.first-port , tt)) = input-7-0 F.vp-3-0
origin-3-1-2 (P.S.full-source , (P.S.middle-port , tt)) = input-7-0 F.vp-1-0
origin-3-1-2 (P.S.full-source , (P.S.final-port , tt)) = input-0-0 F.vp-2-0
selected-3-1-2-AB-source-leg : move-3-1-2 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
selected-3-1-2-AB-source-leg = refl
selected-3-1-2-AB-target-leg : move-3-1-2 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
selected-3-1-2-AB-target-leg = refl
selected-3-1-2-BC-source-leg : move-3-1-2 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
selected-3-1-2-BC-source-leg = refl
selected-3-1-2-BC-target-leg : move-3-1-2 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
selected-3-1-2-BC-target-leg = refl
selected-3-1-2-AC-source-leg : move-3-1-2 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
selected-3-1-2-AC-source-leg = refl
selected-3-1-2-AC-target-leg : move-3-1-2 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
selected-3-1-2-AC-target-leg = refl
equiv-3-2-0 : P.T.Occurrence tree-3-2-0 ≃ P.T.Occurrence tree-2-3-1
equiv-3-2-0 = isoToEquiv (iso move-3-2-0 move-2-3-1 square-2-3-1 square-3-2-0)
origin-3-2-0 : (o : P.T.Occurrence tree-3-2-0) → Transports (P.T.origin tree-3-2-0 o) (P.T.origin tree-2-3-1 (move-3-2-0 o))
origin-3-2-0 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-3-2-0 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-3-2-0 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-3-2-0 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-3-2-0 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-3-2-0 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-3-2-0 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-3-2-0 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-3-2-0 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-3-2-0 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-3-2-0 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-3-2-0 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-3-2-0 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-3-2-0 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-3-2-0 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-3-2-0 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-3-2-0 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-3-2-0 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-3-2-0 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-3-2-0 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-3-2-0 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-3-2-0 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-3-2-0 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-3-2-0 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-3-2-0 (P.S.full-source , (P.S.first-port , tt)) = input-7-1 F.vp-3-1
origin-3-2-0 (P.S.full-source , (P.S.middle-port , tt)) = input-0-1 F.vp-2-1
origin-3-2-0 (P.S.full-source , (P.S.final-port , tt)) = input-0-1 F.vp-0-1
selected-3-2-0-AB-source-leg : move-3-2-0 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
selected-3-2-0-AB-source-leg = refl
selected-3-2-0-AB-target-leg : move-3-2-0 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
selected-3-2-0-AB-target-leg = refl
selected-3-2-0-BC-source-leg : move-3-2-0 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
selected-3-2-0-BC-source-leg = refl
selected-3-2-0-BC-target-leg : move-3-2-0 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
selected-3-2-0-BC-target-leg = refl
selected-3-2-0-AC-source-leg : move-3-2-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
selected-3-2-0-AC-source-leg = refl
selected-3-2-0-AC-target-leg : move-3-2-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
selected-3-2-0-AC-target-leg = refl
equiv-3-2-1 : P.T.Occurrence tree-3-2-1 ≃ P.T.Occurrence tree-2-3-0
equiv-3-2-1 = isoToEquiv (iso move-3-2-1 move-2-3-0 square-2-3-0 square-3-2-1)
origin-3-2-1 : (o : P.T.Occurrence tree-3-2-1) → Transports (P.T.origin tree-3-2-1 o) (P.T.origin tree-2-3-0 (move-3-2-1 o))
origin-3-2-1 (P.S.AB , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-3-2-1 (P.S.AB , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-0-0 q
origin-3-2-1 (P.S.AB , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-3-2-1 (P.S.AB , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-0-1 q
origin-3-2-1 (P.S.AB , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-3-2-1 (P.S.AB , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-0-2 q
origin-3-2-1 (P.S.AB , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-3-2-1 (P.S.AB , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-0-3 q
origin-3-2-1 (P.S.BC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-0-0 p
origin-3-2-1 (P.S.BC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-3-2-1 (P.S.BC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-0-1 p
origin-3-2-1 (P.S.BC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-3-2-1 (P.S.BC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-0-2 p
origin-3-2-1 (P.S.BC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-3-2-1 (P.S.BC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-0-3 p
origin-3-2-1 (P.S.BC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-3-2-1 (P.S.AC , ((c0 , (p , q)) , (P.S.source-leg , tt))) = input-7-0 p
origin-3-2-1 (P.S.AC , ((c0 , (p , q)) , (P.S.target-leg , tt))) = input-7-0 q
origin-3-2-1 (P.S.AC , ((m0 , (p , q)) , (P.S.source-leg , tt))) = input-7-1 p
origin-3-2-1 (P.S.AC , ((m0 , (p , q)) , (P.S.target-leg , tt))) = input-7-1 q
origin-3-2-1 (P.S.AC , ((c1 , (p , q)) , (P.S.source-leg , tt))) = input-7-2 p
origin-3-2-1 (P.S.AC , ((c1 , (p , q)) , (P.S.target-leg , tt))) = input-7-2 q
origin-3-2-1 (P.S.AC , ((m1 , (p , q)) , (P.S.source-leg , tt))) = input-7-3 p
origin-3-2-1 (P.S.AC , ((m1 , (p , q)) , (P.S.target-leg , tt))) = input-7-3 q
origin-3-2-1 (P.S.full-source , (P.S.first-port , tt)) = input-7-0 F.vp-3-0
origin-3-2-1 (P.S.full-source , (P.S.middle-port , tt)) = input-0-0 F.vp-2-0
origin-3-2-1 (P.S.full-source , (P.S.final-port , tt)) = input-7-0 F.vp-1-0
selected-3-2-1-AB-source-leg : move-3-2-1 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
selected-3-2-1-AB-source-leg = refl
selected-3-2-1-AB-target-leg : move-3-2-1 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
selected-3-2-1-AB-target-leg = refl
selected-3-2-1-BC-source-leg : move-3-2-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
selected-3-2-1-BC-source-leg = refl
selected-3-2-1-BC-target-leg : move-3-2-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
selected-3-2-1-BC-target-leg = refl
selected-3-2-1-AC-source-leg : move-3-2-1 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
selected-3-2-1-AC-source-leg = refl
selected-3-2-1-AC-target-leg : move-3-2-1 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
selected-3-2-1-AC-target-leg = refl
