{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyFourFacetConstructor where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_; idEquiv)
open import Cubical.Foundations.Isomorphism using (iso; isoToEquiv)
open import Agda.Builtin.String using (String)
open import RamseySingleFrameFaces using (c0; m0; c1; m1)
open import RamseyEndpointPolicy using (base; complement)
import RamseyRequestedPortExamples as C
import RamseyEdgeAttachmentsExamples as E
import RamseyFourFacetVertexCells as F
import RamseyPermitEquivalence as M
import RamseyCommonSelection as K
import RamseyOccurrenceEquivalence as O
open import RamseyExternalPEExamples
open import RamseyPEConstructorComparison
payload : P.S.InputIndex → String
payload = λ { (c , (v , p)) → E.A.vertex-packet c v p }
module D = Compare P.S.InputIndex payload O.Transports
square-0-0 : (x : P.S.Common C.q0 C.q0) → K.vertex-move complement complement (K.vertex-move base base x) ≡ x
square-0-0 (c0 , (p , q)) i = c0 , (M.square-0-0 p i , M.square-0-0 q i)
square-0-0 (m0 , (p , q)) i = m0 , (M.square-0-1 p i , M.square-0-1 q i)
square-0-0 (c1 , (p , q)) i = c1 , (M.square-0-2 p i , M.square-0-2 q i)
square-0-0 (m1 , (p , q)) i = m1 , (M.square-0-3 p i , M.square-0-3 q i)
square-0-7 : (x : P.S.Common C.q0 C.q7) → K.vertex-move complement base (K.vertex-move base complement x) ≡ x
square-0-7 (c0 , (p , q)) i = c0 , (M.square-0-0 p i , M.square-7-0 q i)
square-0-7 (m0 , (p , q)) i = m0 , (M.square-0-1 p i , M.square-7-1 q i)
square-0-7 (c1 , (p , q)) i = c1 , (M.square-0-2 p i , M.square-7-2 q i)
square-0-7 (m1 , (p , q)) i = m1 , (M.square-0-3 p i , M.square-7-3 q i)
square-7-0 : (x : P.S.Common C.q7 C.q0) → K.vertex-move base complement (K.vertex-move complement base x) ≡ x
square-7-0 (c0 , (p , q)) i = c0 , (M.square-7-0 p i , M.square-0-0 q i)
square-7-0 (m0 , (p , q)) i = m0 , (M.square-7-1 p i , M.square-0-1 q i)
square-7-0 (c1 , (p , q)) i = c1 , (M.square-7-2 p i , M.square-0-2 q i)
square-7-0 (m1 , (p , q)) i = m1 , (M.square-7-3 p i , M.square-0-3 q i)
square-7-7 : (x : P.S.Common C.q7 C.q7) → K.vertex-move base base (K.vertex-move complement complement x) ≡ x
square-7-7 (c0 , (p , q)) i = c0 , (M.square-7-0 p i , M.square-7-0 q i)
square-7-7 (m0 , (p , q)) i = m0 , (M.square-7-1 p i , M.square-7-1 q i)
square-7-7 (c1 , (p , q)) i = c1 , (M.square-7-2 p i , M.square-7-2 q i)
square-7-7 (m1 , (p , q)) i = m1 , (M.square-7-3 p i , M.square-7-3 q i)
common-0-0 : P.S.Common C.q0 C.q0 ≃ P.S.Common C.q7 C.q7
common-0-0 = isoToEquiv (iso (K.vertex-move base base) (K.vertex-move complement complement) square-7-7 square-0-0)
leg-0-0 : (x : P.S.Common C.q0 C.q0) (side : P.S.Side) → D.Correspondence (P.leg C.q0 C.q0 x side) (P.leg C.q7 C.q7 (K.vertex-move base base x) side)
leg-0-0 (c0 , (p , q)) P.S.source-leg = D.leaf (C.q0 , (c0 , p)) (C.q7 , (m0 , M.move-0-0 p)) (O.input-0-0 p)
leg-0-0 (c0 , (p , q)) P.S.target-leg = D.leaf (C.q0 , (c0 , q)) (C.q7 , (m0 , M.move-0-0 q)) (O.input-0-0 q)
leg-0-0 (m0 , (p , q)) P.S.source-leg = D.leaf (C.q0 , (m0 , p)) (C.q7 , (c0 , M.move-0-1 p)) (O.input-0-1 p)
leg-0-0 (m0 , (p , q)) P.S.target-leg = D.leaf (C.q0 , (m0 , q)) (C.q7 , (c0 , M.move-0-1 q)) (O.input-0-1 q)
leg-0-0 (c1 , (p , q)) P.S.source-leg = D.leaf (C.q0 , (c1 , p)) (C.q7 , (m1 , M.move-0-2 p)) (O.input-0-2 p)
leg-0-0 (c1 , (p , q)) P.S.target-leg = D.leaf (C.q0 , (c1 , q)) (C.q7 , (m1 , M.move-0-2 q)) (O.input-0-2 q)
leg-0-0 (m1 , (p , q)) P.S.source-leg = D.leaf (C.q0 , (m1 , p)) (C.q7 , (c1 , M.move-0-3 p)) (O.input-0-3 p)
leg-0-0 (m1 , (p , q)) P.S.target-leg = D.leaf (C.q0 , (m1 , q)) (C.q7 , (c1 , M.move-0-3 q)) (O.input-0-3 q)
pair-0-0 : (x : P.S.Common C.q0 C.q0) → D.Correspondence (P.pair C.q0 C.q0 x) (P.pair C.q7 C.q7 (K.vertex-move base base x))
pair-0-0 x = D.product P.S.Side P.S.Side (idEquiv P.S.Side) (P.leg C.q0 C.q0 x) (P.leg C.q7 C.q7 (K.vertex-move base base x)) (leg-0-0 x)
selected-0-0 : (x : P.S.Common C.q0 C.q0) → D.Correspondence (P.selected C.q0 C.q0 x) (P.selected C.q7 C.q7 (K.vertex-move base base x))
selected-0-0 x = D.selection (P.S.Common C.q0 C.q0) (P.S.Common C.q7 C.q7) common-0-0 (P.pair C.q0 C.q0) (P.pair C.q7 C.q7) x (K.vertex-move base base x) refl pair-0-0
common-0-7 : P.S.Common C.q0 C.q7 ≃ P.S.Common C.q7 C.q0
common-0-7 = isoToEquiv (iso (K.vertex-move base complement) (K.vertex-move complement base) square-7-0 square-0-7)
leg-0-7 : (x : P.S.Common C.q0 C.q7) (side : P.S.Side) → D.Correspondence (P.leg C.q0 C.q7 x side) (P.leg C.q7 C.q0 (K.vertex-move base complement x) side)
leg-0-7 (c0 , (p , q)) P.S.source-leg = D.leaf (C.q0 , (c0 , p)) (C.q7 , (m0 , M.move-0-0 p)) (O.input-0-0 p)
leg-0-7 (c0 , (p , q)) P.S.target-leg = D.leaf (C.q7 , (c0 , q)) (C.q0 , (m0 , M.move-7-0 q)) (O.input-7-0 q)
leg-0-7 (m0 , (p , q)) P.S.source-leg = D.leaf (C.q0 , (m0 , p)) (C.q7 , (c0 , M.move-0-1 p)) (O.input-0-1 p)
leg-0-7 (m0 , (p , q)) P.S.target-leg = D.leaf (C.q7 , (m0 , q)) (C.q0 , (c0 , M.move-7-1 q)) (O.input-7-1 q)
leg-0-7 (c1 , (p , q)) P.S.source-leg = D.leaf (C.q0 , (c1 , p)) (C.q7 , (m1 , M.move-0-2 p)) (O.input-0-2 p)
leg-0-7 (c1 , (p , q)) P.S.target-leg = D.leaf (C.q7 , (c1 , q)) (C.q0 , (m1 , M.move-7-2 q)) (O.input-7-2 q)
leg-0-7 (m1 , (p , q)) P.S.source-leg = D.leaf (C.q0 , (m1 , p)) (C.q7 , (c1 , M.move-0-3 p)) (O.input-0-3 p)
leg-0-7 (m1 , (p , q)) P.S.target-leg = D.leaf (C.q7 , (m1 , q)) (C.q0 , (c1 , M.move-7-3 q)) (O.input-7-3 q)
pair-0-7 : (x : P.S.Common C.q0 C.q7) → D.Correspondence (P.pair C.q0 C.q7 x) (P.pair C.q7 C.q0 (K.vertex-move base complement x))
pair-0-7 x = D.product P.S.Side P.S.Side (idEquiv P.S.Side) (P.leg C.q0 C.q7 x) (P.leg C.q7 C.q0 (K.vertex-move base complement x)) (leg-0-7 x)
selected-0-7 : (x : P.S.Common C.q0 C.q7) → D.Correspondence (P.selected C.q0 C.q7 x) (P.selected C.q7 C.q0 (K.vertex-move base complement x))
selected-0-7 x = D.selection (P.S.Common C.q0 C.q7) (P.S.Common C.q7 C.q0) common-0-7 (P.pair C.q0 C.q7) (P.pair C.q7 C.q0) x (K.vertex-move base complement x) refl pair-0-7
common-7-0 : P.S.Common C.q7 C.q0 ≃ P.S.Common C.q0 C.q7
common-7-0 = isoToEquiv (iso (K.vertex-move complement base) (K.vertex-move base complement) square-0-7 square-7-0)
leg-7-0 : (x : P.S.Common C.q7 C.q0) (side : P.S.Side) → D.Correspondence (P.leg C.q7 C.q0 x side) (P.leg C.q0 C.q7 (K.vertex-move complement base x) side)
leg-7-0 (c0 , (p , q)) P.S.source-leg = D.leaf (C.q7 , (c0 , p)) (C.q0 , (m0 , M.move-7-0 p)) (O.input-7-0 p)
leg-7-0 (c0 , (p , q)) P.S.target-leg = D.leaf (C.q0 , (c0 , q)) (C.q7 , (m0 , M.move-0-0 q)) (O.input-0-0 q)
leg-7-0 (m0 , (p , q)) P.S.source-leg = D.leaf (C.q7 , (m0 , p)) (C.q0 , (c0 , M.move-7-1 p)) (O.input-7-1 p)
leg-7-0 (m0 , (p , q)) P.S.target-leg = D.leaf (C.q0 , (m0 , q)) (C.q7 , (c0 , M.move-0-1 q)) (O.input-0-1 q)
leg-7-0 (c1 , (p , q)) P.S.source-leg = D.leaf (C.q7 , (c1 , p)) (C.q0 , (m1 , M.move-7-2 p)) (O.input-7-2 p)
leg-7-0 (c1 , (p , q)) P.S.target-leg = D.leaf (C.q0 , (c1 , q)) (C.q7 , (m1 , M.move-0-2 q)) (O.input-0-2 q)
leg-7-0 (m1 , (p , q)) P.S.source-leg = D.leaf (C.q7 , (m1 , p)) (C.q0 , (c1 , M.move-7-3 p)) (O.input-7-3 p)
leg-7-0 (m1 , (p , q)) P.S.target-leg = D.leaf (C.q0 , (m1 , q)) (C.q7 , (c1 , M.move-0-3 q)) (O.input-0-3 q)
pair-7-0 : (x : P.S.Common C.q7 C.q0) → D.Correspondence (P.pair C.q7 C.q0 x) (P.pair C.q0 C.q7 (K.vertex-move complement base x))
pair-7-0 x = D.product P.S.Side P.S.Side (idEquiv P.S.Side) (P.leg C.q7 C.q0 x) (P.leg C.q0 C.q7 (K.vertex-move complement base x)) (leg-7-0 x)
selected-7-0 : (x : P.S.Common C.q7 C.q0) → D.Correspondence (P.selected C.q7 C.q0 x) (P.selected C.q0 C.q7 (K.vertex-move complement base x))
selected-7-0 x = D.selection (P.S.Common C.q7 C.q0) (P.S.Common C.q0 C.q7) common-7-0 (P.pair C.q7 C.q0) (P.pair C.q0 C.q7) x (K.vertex-move complement base x) refl pair-7-0
common-7-7 : P.S.Common C.q7 C.q7 ≃ P.S.Common C.q0 C.q0
common-7-7 = isoToEquiv (iso (K.vertex-move complement complement) (K.vertex-move base base) square-0-0 square-7-7)
leg-7-7 : (x : P.S.Common C.q7 C.q7) (side : P.S.Side) → D.Correspondence (P.leg C.q7 C.q7 x side) (P.leg C.q0 C.q0 (K.vertex-move complement complement x) side)
leg-7-7 (c0 , (p , q)) P.S.source-leg = D.leaf (C.q7 , (c0 , p)) (C.q0 , (m0 , M.move-7-0 p)) (O.input-7-0 p)
leg-7-7 (c0 , (p , q)) P.S.target-leg = D.leaf (C.q7 , (c0 , q)) (C.q0 , (m0 , M.move-7-0 q)) (O.input-7-0 q)
leg-7-7 (m0 , (p , q)) P.S.source-leg = D.leaf (C.q7 , (m0 , p)) (C.q0 , (c0 , M.move-7-1 p)) (O.input-7-1 p)
leg-7-7 (m0 , (p , q)) P.S.target-leg = D.leaf (C.q7 , (m0 , q)) (C.q0 , (c0 , M.move-7-1 q)) (O.input-7-1 q)
leg-7-7 (c1 , (p , q)) P.S.source-leg = D.leaf (C.q7 , (c1 , p)) (C.q0 , (m1 , M.move-7-2 p)) (O.input-7-2 p)
leg-7-7 (c1 , (p , q)) P.S.target-leg = D.leaf (C.q7 , (c1 , q)) (C.q0 , (m1 , M.move-7-2 q)) (O.input-7-2 q)
leg-7-7 (m1 , (p , q)) P.S.source-leg = D.leaf (C.q7 , (m1 , p)) (C.q0 , (c1 , M.move-7-3 p)) (O.input-7-3 p)
leg-7-7 (m1 , (p , q)) P.S.target-leg = D.leaf (C.q7 , (m1 , q)) (C.q0 , (c1 , M.move-7-3 q)) (O.input-7-3 q)
pair-7-7 : (x : P.S.Common C.q7 C.q7) → D.Correspondence (P.pair C.q7 C.q7 x) (P.pair C.q0 C.q0 (K.vertex-move complement complement x))
pair-7-7 x = D.product P.S.Side P.S.Side (idEquiv P.S.Side) (P.leg C.q7 C.q7 x) (P.leg C.q0 C.q0 (K.vertex-move complement complement x)) (leg-7-7 x)
selected-7-7 : (x : P.S.Common C.q7 C.q7) → D.Correspondence (P.selected C.q7 C.q7 x) (P.selected C.q0 C.q0 (K.vertex-move complement complement x))
selected-7-7 x = D.selection (P.S.Common C.q7 C.q7) (P.S.Common C.q0 C.q0) common-7-7 (P.pair C.q7 C.q7) (P.pair C.q0 C.q0) x (K.vertex-move complement complement x) refl pair-7-7
piece-0-1-2 : (part : P.S.Piece) → D.Correspondence (P.piece C.q0 C.q7 C.q0 F.triple-0-1-2 part) (P.piece C.q7 C.q0 C.q7 F.triple-1-0-3 part)
piece-0-1-2 P.S.AB = selected-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-1-2)
piece-0-1-2 P.S.BC = selected-7-0 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-1-2)
piece-0-1-2 P.S.AC = selected-0-0 (P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-1-2)
piece-0-1-2 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q0 C.q7 C.q0 F.triple-0-1-2) (P.whole C.q7 C.q0 C.q7 F.triple-1-0-3) (λ { P.S.first-port → D.leaf _ _ (O.input-0-3 F.vp-0-3) ; P.S.middle-port → D.leaf _ _ (O.input-7-3 F.vp-1-3) ; P.S.final-port → D.leaf _ _ (O.input-0-3 F.vp-2-3) })
comparison-0-1-2 : D.Correspondence tree-0-1-2 tree-1-0-3
comparison-0-1-2 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q0 F.triple-0-1-2) (P.piece C.q7 C.q0 C.q7 F.triple-1-0-3) piece-0-1-2
compiled-0-1-2 : D.NativeComparison (D.closed tree-0-1-2) (D.closed tree-1-0-3)
compiled-0-1-2 = D.compile comparison-0-1-2
outer-premises-0-1-2 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-0-1-2) (lift part)) (D.T.R.premise (D.closed tree-1-0-3) (lift part))
outer-premises-0-1-2 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q0 F.triple-0-1-2) (P.piece C.q7 C.q0 C.q7 F.triple-1-0-3) piece-0-1-2
piece-0-1-3 : (part : P.S.Piece) → D.Correspondence (P.piece C.q0 C.q7 C.q7 F.triple-0-1-3 part) (P.piece C.q7 C.q0 C.q0 F.triple-1-0-2 part)
piece-0-1-3 P.S.AB = selected-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-1-3)
piece-0-1-3 P.S.BC = selected-7-7 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-1-3)
piece-0-1-3 P.S.AC = selected-0-7 (P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-1-3)
piece-0-1-3 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q0 C.q7 C.q7 F.triple-0-1-3) (P.whole C.q7 C.q0 C.q0 F.triple-1-0-2) (λ { P.S.first-port → D.leaf _ _ (O.input-0-2 F.vp-0-2) ; P.S.middle-port → D.leaf _ _ (O.input-7-2 F.vp-1-2) ; P.S.final-port → D.leaf _ _ (O.input-7-2 F.vp-3-2) })
comparison-0-1-3 : D.Correspondence tree-0-1-3 tree-1-0-2
comparison-0-1-3 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q7 F.triple-0-1-3) (P.piece C.q7 C.q0 C.q0 F.triple-1-0-2) piece-0-1-3
compiled-0-1-3 : D.NativeComparison (D.closed tree-0-1-3) (D.closed tree-1-0-2)
compiled-0-1-3 = D.compile comparison-0-1-3
outer-premises-0-1-3 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-0-1-3) (lift part)) (D.T.R.premise (D.closed tree-1-0-2) (lift part))
outer-premises-0-1-3 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q7 F.triple-0-1-3) (P.piece C.q7 C.q0 C.q0 F.triple-1-0-2) piece-0-1-3
piece-0-2-1 : (part : P.S.Piece) → D.Correspondence (P.piece C.q0 C.q0 C.q7 F.triple-0-2-1 part) (P.piece C.q7 C.q7 C.q0 F.triple-1-3-0 part)
piece-0-2-1 P.S.AB = selected-0-0 (P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-1)
piece-0-2-1 P.S.BC = selected-0-7 (P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-1)
piece-0-2-1 P.S.AC = selected-0-7 (P.S.ac-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-1)
piece-0-2-1 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q0 C.q0 C.q7 F.triple-0-2-1) (P.whole C.q7 C.q7 C.q0 F.triple-1-3-0) (λ { P.S.first-port → D.leaf _ _ (O.input-0-3 F.vp-0-3) ; P.S.middle-port → D.leaf _ _ (O.input-0-3 F.vp-2-3) ; P.S.final-port → D.leaf _ _ (O.input-7-3 F.vp-1-3) })
comparison-0-2-1 : D.Correspondence tree-0-2-1 tree-1-3-0
comparison-0-2-1 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q0 C.q7 F.triple-0-2-1) (P.piece C.q7 C.q7 C.q0 F.triple-1-3-0) piece-0-2-1
compiled-0-2-1 : D.NativeComparison (D.closed tree-0-2-1) (D.closed tree-1-3-0)
compiled-0-2-1 = D.compile comparison-0-2-1
outer-premises-0-2-1 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-0-2-1) (lift part)) (D.T.R.premise (D.closed tree-1-3-0) (lift part))
outer-premises-0-2-1 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q0 C.q7 F.triple-0-2-1) (P.piece C.q7 C.q7 C.q0 F.triple-1-3-0) piece-0-2-1
piece-0-2-3 : (part : P.S.Piece) → D.Correspondence (P.piece C.q0 C.q0 C.q7 F.triple-0-2-3 part) (P.piece C.q7 C.q7 C.q0 F.triple-1-3-2 part)
piece-0-2-3 P.S.AB = selected-0-0 (P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-3)
piece-0-2-3 P.S.BC = selected-0-7 (P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-3)
piece-0-2-3 P.S.AC = selected-0-7 (P.S.ac-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-3)
piece-0-2-3 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q0 C.q0 C.q7 F.triple-0-2-3) (P.whole C.q7 C.q7 C.q0 F.triple-1-3-2) (λ { P.S.first-port → D.leaf _ _ (O.input-0-1 F.vp-0-1) ; P.S.middle-port → D.leaf _ _ (O.input-0-1 F.vp-2-1) ; P.S.final-port → D.leaf _ _ (O.input-7-1 F.vp-3-1) })
comparison-0-2-3 : D.Correspondence tree-0-2-3 tree-1-3-2
comparison-0-2-3 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q0 C.q7 F.triple-0-2-3) (P.piece C.q7 C.q7 C.q0 F.triple-1-3-2) piece-0-2-3
compiled-0-2-3 : D.NativeComparison (D.closed tree-0-2-3) (D.closed tree-1-3-2)
compiled-0-2-3 = D.compile comparison-0-2-3
outer-premises-0-2-3 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-0-2-3) (lift part)) (D.T.R.premise (D.closed tree-1-3-2) (lift part))
outer-premises-0-2-3 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q0 C.q7 F.triple-0-2-3) (P.piece C.q7 C.q7 C.q0 F.triple-1-3-2) piece-0-2-3
piece-0-3-1 : (part : P.S.Piece) → D.Correspondence (P.piece C.q0 C.q7 C.q7 F.triple-0-3-1 part) (P.piece C.q7 C.q0 C.q0 F.triple-1-2-0 part)
piece-0-3-1 P.S.AB = selected-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-3-1)
piece-0-3-1 P.S.BC = selected-7-7 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-3-1)
piece-0-3-1 P.S.AC = selected-0-7 (P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-3-1)
piece-0-3-1 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q0 C.q7 C.q7 F.triple-0-3-1) (P.whole C.q7 C.q0 C.q0 F.triple-1-2-0) (λ { P.S.first-port → D.leaf _ _ (O.input-0-2 F.vp-0-2) ; P.S.middle-port → D.leaf _ _ (O.input-7-2 F.vp-3-2) ; P.S.final-port → D.leaf _ _ (O.input-7-2 F.vp-1-2) })
comparison-0-3-1 : D.Correspondence tree-0-3-1 tree-1-2-0
comparison-0-3-1 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q7 F.triple-0-3-1) (P.piece C.q7 C.q0 C.q0 F.triple-1-2-0) piece-0-3-1
compiled-0-3-1 : D.NativeComparison (D.closed tree-0-3-1) (D.closed tree-1-2-0)
compiled-0-3-1 = D.compile comparison-0-3-1
outer-premises-0-3-1 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-0-3-1) (lift part)) (D.T.R.premise (D.closed tree-1-2-0) (lift part))
outer-premises-0-3-1 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q7 F.triple-0-3-1) (P.piece C.q7 C.q0 C.q0 F.triple-1-2-0) piece-0-3-1
piece-0-3-2 : (part : P.S.Piece) → D.Correspondence (P.piece C.q0 C.q7 C.q0 F.triple-0-3-2 part) (P.piece C.q7 C.q0 C.q7 F.triple-1-2-3 part)
piece-0-3-2 P.S.AB = selected-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-3-2)
piece-0-3-2 P.S.BC = selected-7-0 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-3-2)
piece-0-3-2 P.S.AC = selected-0-0 (P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-3-2)
piece-0-3-2 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q0 C.q7 C.q0 F.triple-0-3-2) (P.whole C.q7 C.q0 C.q7 F.triple-1-2-3) (λ { P.S.first-port → D.leaf _ _ (O.input-0-1 F.vp-0-1) ; P.S.middle-port → D.leaf _ _ (O.input-7-1 F.vp-3-1) ; P.S.final-port → D.leaf _ _ (O.input-0-1 F.vp-2-1) })
comparison-0-3-2 : D.Correspondence tree-0-3-2 tree-1-2-3
comparison-0-3-2 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q0 F.triple-0-3-2) (P.piece C.q7 C.q0 C.q7 F.triple-1-2-3) piece-0-3-2
compiled-0-3-2 : D.NativeComparison (D.closed tree-0-3-2) (D.closed tree-1-2-3)
compiled-0-3-2 = D.compile comparison-0-3-2
outer-premises-0-3-2 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-0-3-2) (lift part)) (D.T.R.premise (D.closed tree-1-2-3) (lift part))
outer-premises-0-3-2 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q0 F.triple-0-3-2) (P.piece C.q7 C.q0 C.q7 F.triple-1-2-3) piece-0-3-2
piece-1-0-2 : (part : P.S.Piece) → D.Correspondence (P.piece C.q7 C.q0 C.q0 F.triple-1-0-2 part) (P.piece C.q0 C.q7 C.q7 F.triple-0-1-3 part)
piece-1-0-2 P.S.AB = selected-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-0-2)
piece-1-0-2 P.S.BC = selected-0-0 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-0-2)
piece-1-0-2 P.S.AC = selected-7-0 (P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-0-2)
piece-1-0-2 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q7 C.q0 C.q0 F.triple-1-0-2) (P.whole C.q0 C.q7 C.q7 F.triple-0-1-3) (λ { P.S.first-port → D.leaf _ _ (O.input-7-3 F.vp-1-3) ; P.S.middle-port → D.leaf _ _ (O.input-0-3 F.vp-0-3) ; P.S.final-port → D.leaf _ _ (O.input-0-3 F.vp-2-3) })
comparison-1-0-2 : D.Correspondence tree-1-0-2 tree-0-1-3
comparison-1-0-2 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q0 F.triple-1-0-2) (P.piece C.q0 C.q7 C.q7 F.triple-0-1-3) piece-1-0-2
compiled-1-0-2 : D.NativeComparison (D.closed tree-1-0-2) (D.closed tree-0-1-3)
compiled-1-0-2 = D.compile comparison-1-0-2
outer-premises-1-0-2 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-1-0-2) (lift part)) (D.T.R.premise (D.closed tree-0-1-3) (lift part))
outer-premises-1-0-2 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q0 F.triple-1-0-2) (P.piece C.q0 C.q7 C.q7 F.triple-0-1-3) piece-1-0-2
piece-1-0-3 : (part : P.S.Piece) → D.Correspondence (P.piece C.q7 C.q0 C.q7 F.triple-1-0-3 part) (P.piece C.q0 C.q7 C.q0 F.triple-0-1-2 part)
piece-1-0-3 P.S.AB = selected-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-0-3)
piece-1-0-3 P.S.BC = selected-0-7 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-0-3)
piece-1-0-3 P.S.AC = selected-7-7 (P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-0-3)
piece-1-0-3 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q7 C.q0 C.q7 F.triple-1-0-3) (P.whole C.q0 C.q7 C.q0 F.triple-0-1-2) (λ { P.S.first-port → D.leaf _ _ (O.input-7-2 F.vp-1-2) ; P.S.middle-port → D.leaf _ _ (O.input-0-2 F.vp-0-2) ; P.S.final-port → D.leaf _ _ (O.input-7-2 F.vp-3-2) })
comparison-1-0-3 : D.Correspondence tree-1-0-3 tree-0-1-2
comparison-1-0-3 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q7 F.triple-1-0-3) (P.piece C.q0 C.q7 C.q0 F.triple-0-1-2) piece-1-0-3
compiled-1-0-3 : D.NativeComparison (D.closed tree-1-0-3) (D.closed tree-0-1-2)
compiled-1-0-3 = D.compile comparison-1-0-3
outer-premises-1-0-3 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-1-0-3) (lift part)) (D.T.R.premise (D.closed tree-0-1-2) (lift part))
outer-premises-1-0-3 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q7 F.triple-1-0-3) (P.piece C.q0 C.q7 C.q0 F.triple-0-1-2) piece-1-0-3
piece-1-2-0 : (part : P.S.Piece) → D.Correspondence (P.piece C.q7 C.q0 C.q0 F.triple-1-2-0 part) (P.piece C.q0 C.q7 C.q7 F.triple-0-3-1 part)
piece-1-2-0 P.S.AB = selected-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-2-0)
piece-1-2-0 P.S.BC = selected-0-0 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-2-0)
piece-1-2-0 P.S.AC = selected-7-0 (P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-2-0)
piece-1-2-0 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q7 C.q0 C.q0 F.triple-1-2-0) (P.whole C.q0 C.q7 C.q7 F.triple-0-3-1) (λ { P.S.first-port → D.leaf _ _ (O.input-7-3 F.vp-1-3) ; P.S.middle-port → D.leaf _ _ (O.input-0-3 F.vp-2-3) ; P.S.final-port → D.leaf _ _ (O.input-0-3 F.vp-0-3) })
comparison-1-2-0 : D.Correspondence tree-1-2-0 tree-0-3-1
comparison-1-2-0 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q0 F.triple-1-2-0) (P.piece C.q0 C.q7 C.q7 F.triple-0-3-1) piece-1-2-0
compiled-1-2-0 : D.NativeComparison (D.closed tree-1-2-0) (D.closed tree-0-3-1)
compiled-1-2-0 = D.compile comparison-1-2-0
outer-premises-1-2-0 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-1-2-0) (lift part)) (D.T.R.premise (D.closed tree-0-3-1) (lift part))
outer-premises-1-2-0 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q0 F.triple-1-2-0) (P.piece C.q0 C.q7 C.q7 F.triple-0-3-1) piece-1-2-0
piece-1-2-3 : (part : P.S.Piece) → D.Correspondence (P.piece C.q7 C.q0 C.q7 F.triple-1-2-3 part) (P.piece C.q0 C.q7 C.q0 F.triple-0-3-2 part)
piece-1-2-3 P.S.AB = selected-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-2-3)
piece-1-2-3 P.S.BC = selected-0-7 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-2-3)
piece-1-2-3 P.S.AC = selected-7-7 (P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-2-3)
piece-1-2-3 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q7 C.q0 C.q7 F.triple-1-2-3) (P.whole C.q0 C.q7 C.q0 F.triple-0-3-2) (λ { P.S.first-port → D.leaf _ _ (O.input-7-0 F.vp-1-0) ; P.S.middle-port → D.leaf _ _ (O.input-0-0 F.vp-2-0) ; P.S.final-port → D.leaf _ _ (O.input-7-0 F.vp-3-0) })
comparison-1-2-3 : D.Correspondence tree-1-2-3 tree-0-3-2
comparison-1-2-3 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q7 F.triple-1-2-3) (P.piece C.q0 C.q7 C.q0 F.triple-0-3-2) piece-1-2-3
compiled-1-2-3 : D.NativeComparison (D.closed tree-1-2-3) (D.closed tree-0-3-2)
compiled-1-2-3 = D.compile comparison-1-2-3
outer-premises-1-2-3 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-1-2-3) (lift part)) (D.T.R.premise (D.closed tree-0-3-2) (lift part))
outer-premises-1-2-3 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q7 F.triple-1-2-3) (P.piece C.q0 C.q7 C.q0 F.triple-0-3-2) piece-1-2-3
piece-1-3-0 : (part : P.S.Piece) → D.Correspondence (P.piece C.q7 C.q7 C.q0 F.triple-1-3-0 part) (P.piece C.q0 C.q0 C.q7 F.triple-0-2-1 part)
piece-1-3-0 P.S.AB = selected-7-7 (P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-0)
piece-1-3-0 P.S.BC = selected-7-0 (P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-0)
piece-1-3-0 P.S.AC = selected-7-0 (P.S.ac-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-0)
piece-1-3-0 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q7 C.q7 C.q0 F.triple-1-3-0) (P.whole C.q0 C.q0 C.q7 F.triple-0-2-1) (λ { P.S.first-port → D.leaf _ _ (O.input-7-2 F.vp-1-2) ; P.S.middle-port → D.leaf _ _ (O.input-7-2 F.vp-3-2) ; P.S.final-port → D.leaf _ _ (O.input-0-2 F.vp-0-2) })
comparison-1-3-0 : D.Correspondence tree-1-3-0 tree-0-2-1
comparison-1-3-0 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q7 C.q0 F.triple-1-3-0) (P.piece C.q0 C.q0 C.q7 F.triple-0-2-1) piece-1-3-0
compiled-1-3-0 : D.NativeComparison (D.closed tree-1-3-0) (D.closed tree-0-2-1)
compiled-1-3-0 = D.compile comparison-1-3-0
outer-premises-1-3-0 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-1-3-0) (lift part)) (D.T.R.premise (D.closed tree-0-2-1) (lift part))
outer-premises-1-3-0 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q7 C.q0 F.triple-1-3-0) (P.piece C.q0 C.q0 C.q7 F.triple-0-2-1) piece-1-3-0
piece-1-3-2 : (part : P.S.Piece) → D.Correspondence (P.piece C.q7 C.q7 C.q0 F.triple-1-3-2 part) (P.piece C.q0 C.q0 C.q7 F.triple-0-2-3 part)
piece-1-3-2 P.S.AB = selected-7-7 (P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-2)
piece-1-3-2 P.S.BC = selected-7-0 (P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-2)
piece-1-3-2 P.S.AC = selected-7-0 (P.S.ac-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-2)
piece-1-3-2 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q7 C.q7 C.q0 F.triple-1-3-2) (P.whole C.q0 C.q0 C.q7 F.triple-0-2-3) (λ { P.S.first-port → D.leaf _ _ (O.input-7-0 F.vp-1-0) ; P.S.middle-port → D.leaf _ _ (O.input-7-0 F.vp-3-0) ; P.S.final-port → D.leaf _ _ (O.input-0-0 F.vp-2-0) })
comparison-1-3-2 : D.Correspondence tree-1-3-2 tree-0-2-3
comparison-1-3-2 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q7 C.q0 F.triple-1-3-2) (P.piece C.q0 C.q0 C.q7 F.triple-0-2-3) piece-1-3-2
compiled-1-3-2 : D.NativeComparison (D.closed tree-1-3-2) (D.closed tree-0-2-3)
compiled-1-3-2 = D.compile comparison-1-3-2
outer-premises-1-3-2 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-1-3-2) (lift part)) (D.T.R.premise (D.closed tree-0-2-3) (lift part))
outer-premises-1-3-2 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q7 C.q0 F.triple-1-3-2) (P.piece C.q0 C.q0 C.q7 F.triple-0-2-3) piece-1-3-2
piece-2-0-1 : (part : P.S.Piece) → D.Correspondence (P.piece C.q0 C.q0 C.q7 F.triple-2-0-1 part) (P.piece C.q7 C.q7 C.q0 F.triple-3-1-0 part)
piece-2-0-1 P.S.AB = selected-0-0 (P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-1)
piece-2-0-1 P.S.BC = selected-0-7 (P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-1)
piece-2-0-1 P.S.AC = selected-0-7 (P.S.ac-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-1)
piece-2-0-1 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q0 C.q0 C.q7 F.triple-2-0-1) (P.whole C.q7 C.q7 C.q0 F.triple-3-1-0) (λ { P.S.first-port → D.leaf _ _ (O.input-0-3 F.vp-2-3) ; P.S.middle-port → D.leaf _ _ (O.input-0-3 F.vp-0-3) ; P.S.final-port → D.leaf _ _ (O.input-7-3 F.vp-1-3) })
comparison-2-0-1 : D.Correspondence tree-2-0-1 tree-3-1-0
comparison-2-0-1 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q0 C.q7 F.triple-2-0-1) (P.piece C.q7 C.q7 C.q0 F.triple-3-1-0) piece-2-0-1
compiled-2-0-1 : D.NativeComparison (D.closed tree-2-0-1) (D.closed tree-3-1-0)
compiled-2-0-1 = D.compile comparison-2-0-1
outer-premises-2-0-1 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-2-0-1) (lift part)) (D.T.R.premise (D.closed tree-3-1-0) (lift part))
outer-premises-2-0-1 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q0 C.q7 F.triple-2-0-1) (P.piece C.q7 C.q7 C.q0 F.triple-3-1-0) piece-2-0-1
piece-2-0-3 : (part : P.S.Piece) → D.Correspondence (P.piece C.q0 C.q0 C.q7 F.triple-2-0-3 part) (P.piece C.q7 C.q7 C.q0 F.triple-3-1-2 part)
piece-2-0-3 P.S.AB = selected-0-0 (P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-3)
piece-2-0-3 P.S.BC = selected-0-7 (P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-3)
piece-2-0-3 P.S.AC = selected-0-7 (P.S.ac-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-3)
piece-2-0-3 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q0 C.q0 C.q7 F.triple-2-0-3) (P.whole C.q7 C.q7 C.q0 F.triple-3-1-2) (λ { P.S.first-port → D.leaf _ _ (O.input-0-1 F.vp-2-1) ; P.S.middle-port → D.leaf _ _ (O.input-0-1 F.vp-0-1) ; P.S.final-port → D.leaf _ _ (O.input-7-1 F.vp-3-1) })
comparison-2-0-3 : D.Correspondence tree-2-0-3 tree-3-1-2
comparison-2-0-3 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q0 C.q7 F.triple-2-0-3) (P.piece C.q7 C.q7 C.q0 F.triple-3-1-2) piece-2-0-3
compiled-2-0-3 : D.NativeComparison (D.closed tree-2-0-3) (D.closed tree-3-1-2)
compiled-2-0-3 = D.compile comparison-2-0-3
outer-premises-2-0-3 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-2-0-3) (lift part)) (D.T.R.premise (D.closed tree-3-1-2) (lift part))
outer-premises-2-0-3 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q0 C.q7 F.triple-2-0-3) (P.piece C.q7 C.q7 C.q0 F.triple-3-1-2) piece-2-0-3
piece-2-1-0 : (part : P.S.Piece) → D.Correspondence (P.piece C.q0 C.q7 C.q0 F.triple-2-1-0 part) (P.piece C.q7 C.q0 C.q7 F.triple-3-0-1 part)
piece-2-1-0 P.S.AB = selected-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-1-0)
piece-2-1-0 P.S.BC = selected-7-0 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-1-0)
piece-2-1-0 P.S.AC = selected-0-0 (P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-1-0)
piece-2-1-0 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q0 C.q7 C.q0 F.triple-2-1-0) (P.whole C.q7 C.q0 C.q7 F.triple-3-0-1) (λ { P.S.first-port → D.leaf _ _ (O.input-0-3 F.vp-2-3) ; P.S.middle-port → D.leaf _ _ (O.input-7-3 F.vp-1-3) ; P.S.final-port → D.leaf _ _ (O.input-0-3 F.vp-0-3) })
comparison-2-1-0 : D.Correspondence tree-2-1-0 tree-3-0-1
comparison-2-1-0 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q0 F.triple-2-1-0) (P.piece C.q7 C.q0 C.q7 F.triple-3-0-1) piece-2-1-0
compiled-2-1-0 : D.NativeComparison (D.closed tree-2-1-0) (D.closed tree-3-0-1)
compiled-2-1-0 = D.compile comparison-2-1-0
outer-premises-2-1-0 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-2-1-0) (lift part)) (D.T.R.premise (D.closed tree-3-0-1) (lift part))
outer-premises-2-1-0 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q0 F.triple-2-1-0) (P.piece C.q7 C.q0 C.q7 F.triple-3-0-1) piece-2-1-0
piece-2-1-3 : (part : P.S.Piece) → D.Correspondence (P.piece C.q0 C.q7 C.q7 F.triple-2-1-3 part) (P.piece C.q7 C.q0 C.q0 F.triple-3-0-2 part)
piece-2-1-3 P.S.AB = selected-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-1-3)
piece-2-1-3 P.S.BC = selected-7-7 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-1-3)
piece-2-1-3 P.S.AC = selected-0-7 (P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-1-3)
piece-2-1-3 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q0 C.q7 C.q7 F.triple-2-1-3) (P.whole C.q7 C.q0 C.q0 F.triple-3-0-2) (λ { P.S.first-port → D.leaf _ _ (O.input-0-0 F.vp-2-0) ; P.S.middle-port → D.leaf _ _ (O.input-7-0 F.vp-1-0) ; P.S.final-port → D.leaf _ _ (O.input-7-0 F.vp-3-0) })
comparison-2-1-3 : D.Correspondence tree-2-1-3 tree-3-0-2
comparison-2-1-3 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q7 F.triple-2-1-3) (P.piece C.q7 C.q0 C.q0 F.triple-3-0-2) piece-2-1-3
compiled-2-1-3 : D.NativeComparison (D.closed tree-2-1-3) (D.closed tree-3-0-2)
compiled-2-1-3 = D.compile comparison-2-1-3
outer-premises-2-1-3 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-2-1-3) (lift part)) (D.T.R.premise (D.closed tree-3-0-2) (lift part))
outer-premises-2-1-3 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q7 F.triple-2-1-3) (P.piece C.q7 C.q0 C.q0 F.triple-3-0-2) piece-2-1-3
piece-2-3-0 : (part : P.S.Piece) → D.Correspondence (P.piece C.q0 C.q7 C.q0 F.triple-2-3-0 part) (P.piece C.q7 C.q0 C.q7 F.triple-3-2-1 part)
piece-2-3-0 P.S.AB = selected-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-3-0)
piece-2-3-0 P.S.BC = selected-7-0 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-3-0)
piece-2-3-0 P.S.AC = selected-0-0 (P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-3-0)
piece-2-3-0 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q0 C.q7 C.q0 F.triple-2-3-0) (P.whole C.q7 C.q0 C.q7 F.triple-3-2-1) (λ { P.S.first-port → D.leaf _ _ (O.input-0-1 F.vp-2-1) ; P.S.middle-port → D.leaf _ _ (O.input-7-1 F.vp-3-1) ; P.S.final-port → D.leaf _ _ (O.input-0-1 F.vp-0-1) })
comparison-2-3-0 : D.Correspondence tree-2-3-0 tree-3-2-1
comparison-2-3-0 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q0 F.triple-2-3-0) (P.piece C.q7 C.q0 C.q7 F.triple-3-2-1) piece-2-3-0
compiled-2-3-0 : D.NativeComparison (D.closed tree-2-3-0) (D.closed tree-3-2-1)
compiled-2-3-0 = D.compile comparison-2-3-0
outer-premises-2-3-0 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-2-3-0) (lift part)) (D.T.R.premise (D.closed tree-3-2-1) (lift part))
outer-premises-2-3-0 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q0 F.triple-2-3-0) (P.piece C.q7 C.q0 C.q7 F.triple-3-2-1) piece-2-3-0
piece-2-3-1 : (part : P.S.Piece) → D.Correspondence (P.piece C.q0 C.q7 C.q7 F.triple-2-3-1 part) (P.piece C.q7 C.q0 C.q0 F.triple-3-2-0 part)
piece-2-3-1 P.S.AB = selected-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-3-1)
piece-2-3-1 P.S.BC = selected-7-7 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-3-1)
piece-2-3-1 P.S.AC = selected-0-7 (P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-3-1)
piece-2-3-1 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q0 C.q7 C.q7 F.triple-2-3-1) (P.whole C.q7 C.q0 C.q0 F.triple-3-2-0) (λ { P.S.first-port → D.leaf _ _ (O.input-0-0 F.vp-2-0) ; P.S.middle-port → D.leaf _ _ (O.input-7-0 F.vp-3-0) ; P.S.final-port → D.leaf _ _ (O.input-7-0 F.vp-1-0) })
comparison-2-3-1 : D.Correspondence tree-2-3-1 tree-3-2-0
comparison-2-3-1 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q7 F.triple-2-3-1) (P.piece C.q7 C.q0 C.q0 F.triple-3-2-0) piece-2-3-1
compiled-2-3-1 : D.NativeComparison (D.closed tree-2-3-1) (D.closed tree-3-2-0)
compiled-2-3-1 = D.compile comparison-2-3-1
outer-premises-2-3-1 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-2-3-1) (lift part)) (D.T.R.premise (D.closed tree-3-2-0) (lift part))
outer-premises-2-3-1 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q0 C.q7 C.q7 F.triple-2-3-1) (P.piece C.q7 C.q0 C.q0 F.triple-3-2-0) piece-2-3-1
piece-3-0-1 : (part : P.S.Piece) → D.Correspondence (P.piece C.q7 C.q0 C.q7 F.triple-3-0-1 part) (P.piece C.q0 C.q7 C.q0 F.triple-2-1-0 part)
piece-3-0-1 P.S.AB = selected-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-0-1)
piece-3-0-1 P.S.BC = selected-0-7 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-0-1)
piece-3-0-1 P.S.AC = selected-7-7 (P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-0-1)
piece-3-0-1 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q7 C.q0 C.q7 F.triple-3-0-1) (P.whole C.q0 C.q7 C.q0 F.triple-2-1-0) (λ { P.S.first-port → D.leaf _ _ (O.input-7-2 F.vp-3-2) ; P.S.middle-port → D.leaf _ _ (O.input-0-2 F.vp-0-2) ; P.S.final-port → D.leaf _ _ (O.input-7-2 F.vp-1-2) })
comparison-3-0-1 : D.Correspondence tree-3-0-1 tree-2-1-0
comparison-3-0-1 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q7 F.triple-3-0-1) (P.piece C.q0 C.q7 C.q0 F.triple-2-1-0) piece-3-0-1
compiled-3-0-1 : D.NativeComparison (D.closed tree-3-0-1) (D.closed tree-2-1-0)
compiled-3-0-1 = D.compile comparison-3-0-1
outer-premises-3-0-1 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-3-0-1) (lift part)) (D.T.R.premise (D.closed tree-2-1-0) (lift part))
outer-premises-3-0-1 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q7 F.triple-3-0-1) (P.piece C.q0 C.q7 C.q0 F.triple-2-1-0) piece-3-0-1
piece-3-0-2 : (part : P.S.Piece) → D.Correspondence (P.piece C.q7 C.q0 C.q0 F.triple-3-0-2 part) (P.piece C.q0 C.q7 C.q7 F.triple-2-1-3 part)
piece-3-0-2 P.S.AB = selected-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-0-2)
piece-3-0-2 P.S.BC = selected-0-0 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-0-2)
piece-3-0-2 P.S.AC = selected-7-0 (P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-0-2)
piece-3-0-2 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q7 C.q0 C.q0 F.triple-3-0-2) (P.whole C.q0 C.q7 C.q7 F.triple-2-1-3) (λ { P.S.first-port → D.leaf _ _ (O.input-7-1 F.vp-3-1) ; P.S.middle-port → D.leaf _ _ (O.input-0-1 F.vp-0-1) ; P.S.final-port → D.leaf _ _ (O.input-0-1 F.vp-2-1) })
comparison-3-0-2 : D.Correspondence tree-3-0-2 tree-2-1-3
comparison-3-0-2 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q0 F.triple-3-0-2) (P.piece C.q0 C.q7 C.q7 F.triple-2-1-3) piece-3-0-2
compiled-3-0-2 : D.NativeComparison (D.closed tree-3-0-2) (D.closed tree-2-1-3)
compiled-3-0-2 = D.compile comparison-3-0-2
outer-premises-3-0-2 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-3-0-2) (lift part)) (D.T.R.premise (D.closed tree-2-1-3) (lift part))
outer-premises-3-0-2 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q0 F.triple-3-0-2) (P.piece C.q0 C.q7 C.q7 F.triple-2-1-3) piece-3-0-2
piece-3-1-0 : (part : P.S.Piece) → D.Correspondence (P.piece C.q7 C.q7 C.q0 F.triple-3-1-0 part) (P.piece C.q0 C.q0 C.q7 F.triple-2-0-1 part)
piece-3-1-0 P.S.AB = selected-7-7 (P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-0)
piece-3-1-0 P.S.BC = selected-7-0 (P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-0)
piece-3-1-0 P.S.AC = selected-7-0 (P.S.ac-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-0)
piece-3-1-0 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q7 C.q7 C.q0 F.triple-3-1-0) (P.whole C.q0 C.q0 C.q7 F.triple-2-0-1) (λ { P.S.first-port → D.leaf _ _ (O.input-7-2 F.vp-3-2) ; P.S.middle-port → D.leaf _ _ (O.input-7-2 F.vp-1-2) ; P.S.final-port → D.leaf _ _ (O.input-0-2 F.vp-0-2) })
comparison-3-1-0 : D.Correspondence tree-3-1-0 tree-2-0-1
comparison-3-1-0 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q7 C.q0 F.triple-3-1-0) (P.piece C.q0 C.q0 C.q7 F.triple-2-0-1) piece-3-1-0
compiled-3-1-0 : D.NativeComparison (D.closed tree-3-1-0) (D.closed tree-2-0-1)
compiled-3-1-0 = D.compile comparison-3-1-0
outer-premises-3-1-0 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-3-1-0) (lift part)) (D.T.R.premise (D.closed tree-2-0-1) (lift part))
outer-premises-3-1-0 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q7 C.q0 F.triple-3-1-0) (P.piece C.q0 C.q0 C.q7 F.triple-2-0-1) piece-3-1-0
piece-3-1-2 : (part : P.S.Piece) → D.Correspondence (P.piece C.q7 C.q7 C.q0 F.triple-3-1-2 part) (P.piece C.q0 C.q0 C.q7 F.triple-2-0-3 part)
piece-3-1-2 P.S.AB = selected-7-7 (P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-2)
piece-3-1-2 P.S.BC = selected-7-0 (P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-2)
piece-3-1-2 P.S.AC = selected-7-0 (P.S.ac-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-2)
piece-3-1-2 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q7 C.q7 C.q0 F.triple-3-1-2) (P.whole C.q0 C.q0 C.q7 F.triple-2-0-3) (λ { P.S.first-port → D.leaf _ _ (O.input-7-0 F.vp-3-0) ; P.S.middle-port → D.leaf _ _ (O.input-7-0 F.vp-1-0) ; P.S.final-port → D.leaf _ _ (O.input-0-0 F.vp-2-0) })
comparison-3-1-2 : D.Correspondence tree-3-1-2 tree-2-0-3
comparison-3-1-2 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q7 C.q0 F.triple-3-1-2) (P.piece C.q0 C.q0 C.q7 F.triple-2-0-3) piece-3-1-2
compiled-3-1-2 : D.NativeComparison (D.closed tree-3-1-2) (D.closed tree-2-0-3)
compiled-3-1-2 = D.compile comparison-3-1-2
outer-premises-3-1-2 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-3-1-2) (lift part)) (D.T.R.premise (D.closed tree-2-0-3) (lift part))
outer-premises-3-1-2 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q7 C.q0 F.triple-3-1-2) (P.piece C.q0 C.q0 C.q7 F.triple-2-0-3) piece-3-1-2
piece-3-2-0 : (part : P.S.Piece) → D.Correspondence (P.piece C.q7 C.q0 C.q0 F.triple-3-2-0 part) (P.piece C.q0 C.q7 C.q7 F.triple-2-3-1 part)
piece-3-2-0 P.S.AB = selected-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-2-0)
piece-3-2-0 P.S.BC = selected-0-0 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-2-0)
piece-3-2-0 P.S.AC = selected-7-0 (P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-2-0)
piece-3-2-0 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q7 C.q0 C.q0 F.triple-3-2-0) (P.whole C.q0 C.q7 C.q7 F.triple-2-3-1) (λ { P.S.first-port → D.leaf _ _ (O.input-7-1 F.vp-3-1) ; P.S.middle-port → D.leaf _ _ (O.input-0-1 F.vp-2-1) ; P.S.final-port → D.leaf _ _ (O.input-0-1 F.vp-0-1) })
comparison-3-2-0 : D.Correspondence tree-3-2-0 tree-2-3-1
comparison-3-2-0 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q0 F.triple-3-2-0) (P.piece C.q0 C.q7 C.q7 F.triple-2-3-1) piece-3-2-0
compiled-3-2-0 : D.NativeComparison (D.closed tree-3-2-0) (D.closed tree-2-3-1)
compiled-3-2-0 = D.compile comparison-3-2-0
outer-premises-3-2-0 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-3-2-0) (lift part)) (D.T.R.premise (D.closed tree-2-3-1) (lift part))
outer-premises-3-2-0 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q0 F.triple-3-2-0) (P.piece C.q0 C.q7 C.q7 F.triple-2-3-1) piece-3-2-0
piece-3-2-1 : (part : P.S.Piece) → D.Correspondence (P.piece C.q7 C.q0 C.q7 F.triple-3-2-1 part) (P.piece C.q0 C.q7 C.q0 F.triple-2-3-0 part)
piece-3-2-1 P.S.AB = selected-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-2-1)
piece-3-2-1 P.S.BC = selected-0-7 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-2-1)
piece-3-2-1 P.S.AC = selected-7-7 (P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-2-1)
piece-3-2-1 P.S.full-source = D.product P.S.Three P.S.Three (idEquiv P.S.Three) (P.whole C.q7 C.q0 C.q7 F.triple-3-2-1) (P.whole C.q0 C.q7 C.q0 F.triple-2-3-0) (λ { P.S.first-port → D.leaf _ _ (O.input-7-0 F.vp-3-0) ; P.S.middle-port → D.leaf _ _ (O.input-0-0 F.vp-2-0) ; P.S.final-port → D.leaf _ _ (O.input-7-0 F.vp-1-0) })
comparison-3-2-1 : D.Correspondence tree-3-2-1 tree-2-3-0
comparison-3-2-1 = D.product P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q7 F.triple-3-2-1) (P.piece C.q0 C.q7 C.q0 F.triple-2-3-0) piece-3-2-1
compiled-3-2-1 : D.NativeComparison (D.closed tree-3-2-1) (D.closed tree-2-3-0)
compiled-3-2-1 = D.compile comparison-3-2-1
outer-premises-3-2-1 : (part : P.S.Piece) → D.NativeComparison (D.T.R.premise (D.closed tree-3-2-1) (lift part)) (D.T.R.premise (D.closed tree-2-3-0) (lift part))
outer-premises-3-2-1 = D.product-premises P.S.Piece P.S.Piece (idEquiv P.S.Piece) (P.piece C.q7 C.q0 C.q7 F.triple-3-2-1) (P.piece C.q0 C.q7 C.q0 F.triple-2-3-0) piece-3-2-1
middle-ab-0-1-2 : D.T.R.Closed
middle-ab-0-1-2 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-0-1-2) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-1-2))) (lift P.S.target-leg)
middle-bc-0-1-2 : D.T.R.Closed
middle-bc-0-1-2 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-0-1-2) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-1-2))) (lift P.S.source-leg)
compiled-middle-seam-0-1-2 : middle-ab-0-1-2 ≡ middle-bc-0-1-2
compiled-middle-seam-0-1-2 = refl
middle-ab-0-1-3 : D.T.R.Closed
middle-ab-0-1-3 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-0-1-3) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-1-3))) (lift P.S.target-leg)
middle-bc-0-1-3 : D.T.R.Closed
middle-bc-0-1-3 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-0-1-3) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-1-3))) (lift P.S.source-leg)
compiled-middle-seam-0-1-3 : middle-ab-0-1-3 ≡ middle-bc-0-1-3
compiled-middle-seam-0-1-3 = refl
middle-ab-0-2-1 : D.T.R.Closed
middle-ab-0-2-1 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-0-2-1) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-1))) (lift P.S.target-leg)
middle-bc-0-2-1 : D.T.R.Closed
middle-bc-0-2-1 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-0-2-1) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-1))) (lift P.S.source-leg)
compiled-middle-seam-0-2-1 : middle-ab-0-2-1 ≡ middle-bc-0-2-1
compiled-middle-seam-0-2-1 = refl
middle-ab-0-2-3 : D.T.R.Closed
middle-ab-0-2-3 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-0-2-3) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-3))) (lift P.S.target-leg)
middle-bc-0-2-3 : D.T.R.Closed
middle-bc-0-2-3 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-0-2-3) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-3))) (lift P.S.source-leg)
compiled-middle-seam-0-2-3 : middle-ab-0-2-3 ≡ middle-bc-0-2-3
compiled-middle-seam-0-2-3 = refl
middle-ab-0-3-1 : D.T.R.Closed
middle-ab-0-3-1 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-0-3-1) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-3-1))) (lift P.S.target-leg)
middle-bc-0-3-1 : D.T.R.Closed
middle-bc-0-3-1 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-0-3-1) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-3-1))) (lift P.S.source-leg)
compiled-middle-seam-0-3-1 : middle-ab-0-3-1 ≡ middle-bc-0-3-1
compiled-middle-seam-0-3-1 = refl
middle-ab-0-3-2 : D.T.R.Closed
middle-ab-0-3-2 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-0-3-2) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-3-2))) (lift P.S.target-leg)
middle-bc-0-3-2 : D.T.R.Closed
middle-bc-0-3-2 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-0-3-2) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-3-2))) (lift P.S.source-leg)
compiled-middle-seam-0-3-2 : middle-ab-0-3-2 ≡ middle-bc-0-3-2
compiled-middle-seam-0-3-2 = refl
middle-ab-1-0-2 : D.T.R.Closed
middle-ab-1-0-2 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-1-0-2) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-0-2))) (lift P.S.target-leg)
middle-bc-1-0-2 : D.T.R.Closed
middle-bc-1-0-2 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-1-0-2) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-0-2))) (lift P.S.source-leg)
compiled-middle-seam-1-0-2 : middle-ab-1-0-2 ≡ middle-bc-1-0-2
compiled-middle-seam-1-0-2 = refl
middle-ab-1-0-3 : D.T.R.Closed
middle-ab-1-0-3 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-1-0-3) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-0-3))) (lift P.S.target-leg)
middle-bc-1-0-3 : D.T.R.Closed
middle-bc-1-0-3 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-1-0-3) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-0-3))) (lift P.S.source-leg)
compiled-middle-seam-1-0-3 : middle-ab-1-0-3 ≡ middle-bc-1-0-3
compiled-middle-seam-1-0-3 = refl
middle-ab-1-2-0 : D.T.R.Closed
middle-ab-1-2-0 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-1-2-0) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-2-0))) (lift P.S.target-leg)
middle-bc-1-2-0 : D.T.R.Closed
middle-bc-1-2-0 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-1-2-0) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-2-0))) (lift P.S.source-leg)
compiled-middle-seam-1-2-0 : middle-ab-1-2-0 ≡ middle-bc-1-2-0
compiled-middle-seam-1-2-0 = refl
middle-ab-1-2-3 : D.T.R.Closed
middle-ab-1-2-3 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-1-2-3) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-2-3))) (lift P.S.target-leg)
middle-bc-1-2-3 : D.T.R.Closed
middle-bc-1-2-3 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-1-2-3) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-2-3))) (lift P.S.source-leg)
compiled-middle-seam-1-2-3 : middle-ab-1-2-3 ≡ middle-bc-1-2-3
compiled-middle-seam-1-2-3 = refl
middle-ab-1-3-0 : D.T.R.Closed
middle-ab-1-3-0 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-1-3-0) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-0))) (lift P.S.target-leg)
middle-bc-1-3-0 : D.T.R.Closed
middle-bc-1-3-0 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-1-3-0) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-0))) (lift P.S.source-leg)
compiled-middle-seam-1-3-0 : middle-ab-1-3-0 ≡ middle-bc-1-3-0
compiled-middle-seam-1-3-0 = refl
middle-ab-1-3-2 : D.T.R.Closed
middle-ab-1-3-2 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-1-3-2) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-2))) (lift P.S.target-leg)
middle-bc-1-3-2 : D.T.R.Closed
middle-bc-1-3-2 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-1-3-2) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-2))) (lift P.S.source-leg)
compiled-middle-seam-1-3-2 : middle-ab-1-3-2 ≡ middle-bc-1-3-2
compiled-middle-seam-1-3-2 = refl
middle-ab-2-0-1 : D.T.R.Closed
middle-ab-2-0-1 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-2-0-1) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-1))) (lift P.S.target-leg)
middle-bc-2-0-1 : D.T.R.Closed
middle-bc-2-0-1 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-2-0-1) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-1))) (lift P.S.source-leg)
compiled-middle-seam-2-0-1 : middle-ab-2-0-1 ≡ middle-bc-2-0-1
compiled-middle-seam-2-0-1 = refl
middle-ab-2-0-3 : D.T.R.Closed
middle-ab-2-0-3 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-2-0-3) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-3))) (lift P.S.target-leg)
middle-bc-2-0-3 : D.T.R.Closed
middle-bc-2-0-3 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-2-0-3) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-3))) (lift P.S.source-leg)
compiled-middle-seam-2-0-3 : middle-ab-2-0-3 ≡ middle-bc-2-0-3
compiled-middle-seam-2-0-3 = refl
middle-ab-2-1-0 : D.T.R.Closed
middle-ab-2-1-0 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-2-1-0) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-1-0))) (lift P.S.target-leg)
middle-bc-2-1-0 : D.T.R.Closed
middle-bc-2-1-0 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-2-1-0) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-1-0))) (lift P.S.source-leg)
compiled-middle-seam-2-1-0 : middle-ab-2-1-0 ≡ middle-bc-2-1-0
compiled-middle-seam-2-1-0 = refl
middle-ab-2-1-3 : D.T.R.Closed
middle-ab-2-1-3 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-2-1-3) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-1-3))) (lift P.S.target-leg)
middle-bc-2-1-3 : D.T.R.Closed
middle-bc-2-1-3 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-2-1-3) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-1-3))) (lift P.S.source-leg)
compiled-middle-seam-2-1-3 : middle-ab-2-1-3 ≡ middle-bc-2-1-3
compiled-middle-seam-2-1-3 = refl
middle-ab-2-3-0 : D.T.R.Closed
middle-ab-2-3-0 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-2-3-0) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-3-0))) (lift P.S.target-leg)
middle-bc-2-3-0 : D.T.R.Closed
middle-bc-2-3-0 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-2-3-0) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-3-0))) (lift P.S.source-leg)
compiled-middle-seam-2-3-0 : middle-ab-2-3-0 ≡ middle-bc-2-3-0
compiled-middle-seam-2-3-0 = refl
middle-ab-2-3-1 : D.T.R.Closed
middle-ab-2-3-1 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-2-3-1) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-3-1))) (lift P.S.target-leg)
middle-bc-2-3-1 : D.T.R.Closed
middle-bc-2-3-1 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-2-3-1) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-3-1))) (lift P.S.source-leg)
compiled-middle-seam-2-3-1 : middle-ab-2-3-1 ≡ middle-bc-2-3-1
compiled-middle-seam-2-3-1 = refl
middle-ab-3-0-1 : D.T.R.Closed
middle-ab-3-0-1 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-3-0-1) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-0-1))) (lift P.S.target-leg)
middle-bc-3-0-1 : D.T.R.Closed
middle-bc-3-0-1 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-3-0-1) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-0-1))) (lift P.S.source-leg)
compiled-middle-seam-3-0-1 : middle-ab-3-0-1 ≡ middle-bc-3-0-1
compiled-middle-seam-3-0-1 = refl
middle-ab-3-0-2 : D.T.R.Closed
middle-ab-3-0-2 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-3-0-2) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-0-2))) (lift P.S.target-leg)
middle-bc-3-0-2 : D.T.R.Closed
middle-bc-3-0-2 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-3-0-2) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-0-2))) (lift P.S.source-leg)
compiled-middle-seam-3-0-2 : middle-ab-3-0-2 ≡ middle-bc-3-0-2
compiled-middle-seam-3-0-2 = refl
middle-ab-3-1-0 : D.T.R.Closed
middle-ab-3-1-0 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-3-1-0) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-0))) (lift P.S.target-leg)
middle-bc-3-1-0 : D.T.R.Closed
middle-bc-3-1-0 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-3-1-0) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-0))) (lift P.S.source-leg)
compiled-middle-seam-3-1-0 : middle-ab-3-1-0 ≡ middle-bc-3-1-0
compiled-middle-seam-3-1-0 = refl
middle-ab-3-1-2 : D.T.R.Closed
middle-ab-3-1-2 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-3-1-2) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-2))) (lift P.S.target-leg)
middle-bc-3-1-2 : D.T.R.Closed
middle-bc-3-1-2 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-3-1-2) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-2))) (lift P.S.source-leg)
compiled-middle-seam-3-1-2 : middle-ab-3-1-2 ≡ middle-bc-3-1-2
compiled-middle-seam-3-1-2 = refl
middle-ab-3-2-0 : D.T.R.Closed
middle-ab-3-2-0 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-3-2-0) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-2-0))) (lift P.S.target-leg)
middle-bc-3-2-0 : D.T.R.Closed
middle-bc-3-2-0 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-3-2-0) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-2-0))) (lift P.S.source-leg)
compiled-middle-seam-3-2-0 : middle-ab-3-2-0 ≡ middle-bc-3-2-0
compiled-middle-seam-3-2-0 = refl
middle-ab-3-2-1 : D.T.R.Closed
middle-ab-3-2-1 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-3-2-1) (lift P.S.AB)) (lift (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-2-1))) (lift P.S.target-leg)
middle-bc-3-2-1 : D.T.R.Closed
middle-bc-3-2-1 = D.T.R.premise (D.T.R.premise (D.T.R.premise (D.closed tree-3-2-1) (lift P.S.BC)) (lift (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-2-1))) (lift P.S.source-leg)
compiled-middle-seam-3-2-1 : middle-ab-3-2-1 ≡ middle-bc-3-2-1
compiled-middle-seam-3-2-1 = refl
middle-comparison-ab-0-1-2 : D.NativeComparison middle-ab-0-1-2 middle-ab-1-0-3
middle-comparison-ab-0-1-2 = D.compile (leg-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-1-2) P.S.target-leg)
middle-comparison-bc-0-1-2 : D.NativeComparison middle-bc-0-1-2 middle-bc-1-0-3
middle-comparison-bc-0-1-2 = D.compile (leg-7-0 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-1-2) P.S.source-leg)
middle-comparison-agreement-0-1-2 : middle-comparison-ab-0-1-2 ≡ middle-comparison-bc-0-1-2
middle-comparison-agreement-0-1-2 = refl
middle-comparison-ab-0-1-3 : D.NativeComparison middle-ab-0-1-3 middle-ab-1-0-2
middle-comparison-ab-0-1-3 = D.compile (leg-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-1-3) P.S.target-leg)
middle-comparison-bc-0-1-3 : D.NativeComparison middle-bc-0-1-3 middle-bc-1-0-2
middle-comparison-bc-0-1-3 = D.compile (leg-7-7 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-1-3) P.S.source-leg)
middle-comparison-agreement-0-1-3 : middle-comparison-ab-0-1-3 ≡ middle-comparison-bc-0-1-3
middle-comparison-agreement-0-1-3 = refl
middle-comparison-ab-0-2-1 : D.NativeComparison middle-ab-0-2-1 middle-ab-1-3-0
middle-comparison-ab-0-2-1 = D.compile (leg-0-0 (P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-1) P.S.target-leg)
middle-comparison-bc-0-2-1 : D.NativeComparison middle-bc-0-2-1 middle-bc-1-3-0
middle-comparison-bc-0-2-1 = D.compile (leg-0-7 (P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-1) P.S.source-leg)
middle-comparison-agreement-0-2-1 : middle-comparison-ab-0-2-1 ≡ middle-comparison-bc-0-2-1
middle-comparison-agreement-0-2-1 = refl
middle-comparison-ab-0-2-3 : D.NativeComparison middle-ab-0-2-3 middle-ab-1-3-2
middle-comparison-ab-0-2-3 = D.compile (leg-0-0 (P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-3) P.S.target-leg)
middle-comparison-bc-0-2-3 : D.NativeComparison middle-bc-0-2-3 middle-bc-1-3-2
middle-comparison-bc-0-2-3 = D.compile (leg-0-7 (P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-3) P.S.source-leg)
middle-comparison-agreement-0-2-3 : middle-comparison-ab-0-2-3 ≡ middle-comparison-bc-0-2-3
middle-comparison-agreement-0-2-3 = refl
middle-comparison-ab-0-3-1 : D.NativeComparison middle-ab-0-3-1 middle-ab-1-2-0
middle-comparison-ab-0-3-1 = D.compile (leg-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-3-1) P.S.target-leg)
middle-comparison-bc-0-3-1 : D.NativeComparison middle-bc-0-3-1 middle-bc-1-2-0
middle-comparison-bc-0-3-1 = D.compile (leg-7-7 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-3-1) P.S.source-leg)
middle-comparison-agreement-0-3-1 : middle-comparison-ab-0-3-1 ≡ middle-comparison-bc-0-3-1
middle-comparison-agreement-0-3-1 = refl
middle-comparison-ab-0-3-2 : D.NativeComparison middle-ab-0-3-2 middle-ab-1-2-3
middle-comparison-ab-0-3-2 = D.compile (leg-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-3-2) P.S.target-leg)
middle-comparison-bc-0-3-2 : D.NativeComparison middle-bc-0-3-2 middle-bc-1-2-3
middle-comparison-bc-0-3-2 = D.compile (leg-7-0 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-3-2) P.S.source-leg)
middle-comparison-agreement-0-3-2 : middle-comparison-ab-0-3-2 ≡ middle-comparison-bc-0-3-2
middle-comparison-agreement-0-3-2 = refl
middle-comparison-ab-1-0-2 : D.NativeComparison middle-ab-1-0-2 middle-ab-0-1-3
middle-comparison-ab-1-0-2 = D.compile (leg-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-0-2) P.S.target-leg)
middle-comparison-bc-1-0-2 : D.NativeComparison middle-bc-1-0-2 middle-bc-0-1-3
middle-comparison-bc-1-0-2 = D.compile (leg-0-0 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-0-2) P.S.source-leg)
middle-comparison-agreement-1-0-2 : middle-comparison-ab-1-0-2 ≡ middle-comparison-bc-1-0-2
middle-comparison-agreement-1-0-2 = refl
middle-comparison-ab-1-0-3 : D.NativeComparison middle-ab-1-0-3 middle-ab-0-1-2
middle-comparison-ab-1-0-3 = D.compile (leg-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-0-3) P.S.target-leg)
middle-comparison-bc-1-0-3 : D.NativeComparison middle-bc-1-0-3 middle-bc-0-1-2
middle-comparison-bc-1-0-3 = D.compile (leg-0-7 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-0-3) P.S.source-leg)
middle-comparison-agreement-1-0-3 : middle-comparison-ab-1-0-3 ≡ middle-comparison-bc-1-0-3
middle-comparison-agreement-1-0-3 = refl
middle-comparison-ab-1-2-0 : D.NativeComparison middle-ab-1-2-0 middle-ab-0-3-1
middle-comparison-ab-1-2-0 = D.compile (leg-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-2-0) P.S.target-leg)
middle-comparison-bc-1-2-0 : D.NativeComparison middle-bc-1-2-0 middle-bc-0-3-1
middle-comparison-bc-1-2-0 = D.compile (leg-0-0 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-2-0) P.S.source-leg)
middle-comparison-agreement-1-2-0 : middle-comparison-ab-1-2-0 ≡ middle-comparison-bc-1-2-0
middle-comparison-agreement-1-2-0 = refl
middle-comparison-ab-1-2-3 : D.NativeComparison middle-ab-1-2-3 middle-ab-0-3-2
middle-comparison-ab-1-2-3 = D.compile (leg-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-2-3) P.S.target-leg)
middle-comparison-bc-1-2-3 : D.NativeComparison middle-bc-1-2-3 middle-bc-0-3-2
middle-comparison-bc-1-2-3 = D.compile (leg-0-7 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-2-3) P.S.source-leg)
middle-comparison-agreement-1-2-3 : middle-comparison-ab-1-2-3 ≡ middle-comparison-bc-1-2-3
middle-comparison-agreement-1-2-3 = refl
middle-comparison-ab-1-3-0 : D.NativeComparison middle-ab-1-3-0 middle-ab-0-2-1
middle-comparison-ab-1-3-0 = D.compile (leg-7-7 (P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-0) P.S.target-leg)
middle-comparison-bc-1-3-0 : D.NativeComparison middle-bc-1-3-0 middle-bc-0-2-1
middle-comparison-bc-1-3-0 = D.compile (leg-7-0 (P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-0) P.S.source-leg)
middle-comparison-agreement-1-3-0 : middle-comparison-ab-1-3-0 ≡ middle-comparison-bc-1-3-0
middle-comparison-agreement-1-3-0 = refl
middle-comparison-ab-1-3-2 : D.NativeComparison middle-ab-1-3-2 middle-ab-0-2-3
middle-comparison-ab-1-3-2 = D.compile (leg-7-7 (P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-2) P.S.target-leg)
middle-comparison-bc-1-3-2 : D.NativeComparison middle-bc-1-3-2 middle-bc-0-2-3
middle-comparison-bc-1-3-2 = D.compile (leg-7-0 (P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-2) P.S.source-leg)
middle-comparison-agreement-1-3-2 : middle-comparison-ab-1-3-2 ≡ middle-comparison-bc-1-3-2
middle-comparison-agreement-1-3-2 = refl
middle-comparison-ab-2-0-1 : D.NativeComparison middle-ab-2-0-1 middle-ab-3-1-0
middle-comparison-ab-2-0-1 = D.compile (leg-0-0 (P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-1) P.S.target-leg)
middle-comparison-bc-2-0-1 : D.NativeComparison middle-bc-2-0-1 middle-bc-3-1-0
middle-comparison-bc-2-0-1 = D.compile (leg-0-7 (P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-1) P.S.source-leg)
middle-comparison-agreement-2-0-1 : middle-comparison-ab-2-0-1 ≡ middle-comparison-bc-2-0-1
middle-comparison-agreement-2-0-1 = refl
middle-comparison-ab-2-0-3 : D.NativeComparison middle-ab-2-0-3 middle-ab-3-1-2
middle-comparison-ab-2-0-3 = D.compile (leg-0-0 (P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-3) P.S.target-leg)
middle-comparison-bc-2-0-3 : D.NativeComparison middle-bc-2-0-3 middle-bc-3-1-2
middle-comparison-bc-2-0-3 = D.compile (leg-0-7 (P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-3) P.S.source-leg)
middle-comparison-agreement-2-0-3 : middle-comparison-ab-2-0-3 ≡ middle-comparison-bc-2-0-3
middle-comparison-agreement-2-0-3 = refl
middle-comparison-ab-2-1-0 : D.NativeComparison middle-ab-2-1-0 middle-ab-3-0-1
middle-comparison-ab-2-1-0 = D.compile (leg-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-1-0) P.S.target-leg)
middle-comparison-bc-2-1-0 : D.NativeComparison middle-bc-2-1-0 middle-bc-3-0-1
middle-comparison-bc-2-1-0 = D.compile (leg-7-0 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-1-0) P.S.source-leg)
middle-comparison-agreement-2-1-0 : middle-comparison-ab-2-1-0 ≡ middle-comparison-bc-2-1-0
middle-comparison-agreement-2-1-0 = refl
middle-comparison-ab-2-1-3 : D.NativeComparison middle-ab-2-1-3 middle-ab-3-0-2
middle-comparison-ab-2-1-3 = D.compile (leg-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-1-3) P.S.target-leg)
middle-comparison-bc-2-1-3 : D.NativeComparison middle-bc-2-1-3 middle-bc-3-0-2
middle-comparison-bc-2-1-3 = D.compile (leg-7-7 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-1-3) P.S.source-leg)
middle-comparison-agreement-2-1-3 : middle-comparison-ab-2-1-3 ≡ middle-comparison-bc-2-1-3
middle-comparison-agreement-2-1-3 = refl
middle-comparison-ab-2-3-0 : D.NativeComparison middle-ab-2-3-0 middle-ab-3-2-1
middle-comparison-ab-2-3-0 = D.compile (leg-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-3-0) P.S.target-leg)
middle-comparison-bc-2-3-0 : D.NativeComparison middle-bc-2-3-0 middle-bc-3-2-1
middle-comparison-bc-2-3-0 = D.compile (leg-7-0 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-3-0) P.S.source-leg)
middle-comparison-agreement-2-3-0 : middle-comparison-ab-2-3-0 ≡ middle-comparison-bc-2-3-0
middle-comparison-agreement-2-3-0 = refl
middle-comparison-ab-2-3-1 : D.NativeComparison middle-ab-2-3-1 middle-ab-3-2-0
middle-comparison-ab-2-3-1 = D.compile (leg-0-7 (P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-3-1) P.S.target-leg)
middle-comparison-bc-2-3-1 : D.NativeComparison middle-bc-2-3-1 middle-bc-3-2-0
middle-comparison-bc-2-3-1 = D.compile (leg-7-7 (P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-3-1) P.S.source-leg)
middle-comparison-agreement-2-3-1 : middle-comparison-ab-2-3-1 ≡ middle-comparison-bc-2-3-1
middle-comparison-agreement-2-3-1 = refl
middle-comparison-ab-3-0-1 : D.NativeComparison middle-ab-3-0-1 middle-ab-2-1-0
middle-comparison-ab-3-0-1 = D.compile (leg-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-0-1) P.S.target-leg)
middle-comparison-bc-3-0-1 : D.NativeComparison middle-bc-3-0-1 middle-bc-2-1-0
middle-comparison-bc-3-0-1 = D.compile (leg-0-7 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-0-1) P.S.source-leg)
middle-comparison-agreement-3-0-1 : middle-comparison-ab-3-0-1 ≡ middle-comparison-bc-3-0-1
middle-comparison-agreement-3-0-1 = refl
middle-comparison-ab-3-0-2 : D.NativeComparison middle-ab-3-0-2 middle-ab-2-1-3
middle-comparison-ab-3-0-2 = D.compile (leg-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-0-2) P.S.target-leg)
middle-comparison-bc-3-0-2 : D.NativeComparison middle-bc-3-0-2 middle-bc-2-1-3
middle-comparison-bc-3-0-2 = D.compile (leg-0-0 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-0-2) P.S.source-leg)
middle-comparison-agreement-3-0-2 : middle-comparison-ab-3-0-2 ≡ middle-comparison-bc-3-0-2
middle-comparison-agreement-3-0-2 = refl
middle-comparison-ab-3-1-0 : D.NativeComparison middle-ab-3-1-0 middle-ab-2-0-1
middle-comparison-ab-3-1-0 = D.compile (leg-7-7 (P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-0) P.S.target-leg)
middle-comparison-bc-3-1-0 : D.NativeComparison middle-bc-3-1-0 middle-bc-2-0-1
middle-comparison-bc-3-1-0 = D.compile (leg-7-0 (P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-0) P.S.source-leg)
middle-comparison-agreement-3-1-0 : middle-comparison-ab-3-1-0 ≡ middle-comparison-bc-3-1-0
middle-comparison-agreement-3-1-0 = refl
middle-comparison-ab-3-1-2 : D.NativeComparison middle-ab-3-1-2 middle-ab-2-0-3
middle-comparison-ab-3-1-2 = D.compile (leg-7-7 (P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-2) P.S.target-leg)
middle-comparison-bc-3-1-2 : D.NativeComparison middle-bc-3-1-2 middle-bc-2-0-3
middle-comparison-bc-3-1-2 = D.compile (leg-7-0 (P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-2) P.S.source-leg)
middle-comparison-agreement-3-1-2 : middle-comparison-ab-3-1-2 ≡ middle-comparison-bc-3-1-2
middle-comparison-agreement-3-1-2 = refl
middle-comparison-ab-3-2-0 : D.NativeComparison middle-ab-3-2-0 middle-ab-2-3-1
middle-comparison-ab-3-2-0 = D.compile (leg-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-2-0) P.S.target-leg)
middle-comparison-bc-3-2-0 : D.NativeComparison middle-bc-3-2-0 middle-bc-2-3-1
middle-comparison-bc-3-2-0 = D.compile (leg-0-0 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-2-0) P.S.source-leg)
middle-comparison-agreement-3-2-0 : middle-comparison-ab-3-2-0 ≡ middle-comparison-bc-3-2-0
middle-comparison-agreement-3-2-0 = refl
middle-comparison-ab-3-2-1 : D.NativeComparison middle-ab-3-2-1 middle-ab-2-3-0
middle-comparison-ab-3-2-1 = D.compile (leg-7-0 (P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-2-1) P.S.target-leg)
middle-comparison-bc-3-2-1 : D.NativeComparison middle-bc-3-2-1 middle-bc-2-3-0
middle-comparison-bc-3-2-1 = D.compile (leg-0-7 (P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-2-1) P.S.source-leg)
middle-comparison-agreement-3-2-1 : middle-comparison-ab-3-2-1 ≡ middle-comparison-bc-3-2-1
middle-comparison-agreement-3-2-1 = refl
