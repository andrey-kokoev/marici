{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyExternalPEExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (tt)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import RamseySingleFrameFaces using (Vertex; c0; m0; c1; m1)
import RamseyRequestedPortExamples as C
import RamseyEdgeAttachmentsExamples as E
import RamseyFourFacetVertexCells as F
open import RamseyExternalPE
module P = TracedSpans C.Chart Vertex E.A.VertexPermit E.A.vertex-packet
tree-0-1-2 : P.T.Tree
tree-0-1-2 = P.composition C.q0 C.q7 C.q0 F.triple-0-1-2
native-0-1-2 : P.T.R.Resolve (P.T.encode tree-0-1-2)
native-0-1-2 = P.T.realize tree-0-1-2
cell-0-1-2 : P.T.encode tree-0-1-2 ≡ E.A.V.composition-package C.q0 C.q7 C.q0 F.triple-0-1-2
cell-0-1-2 = P.composition-cell C.q0 C.q7 C.q0 F.triple-0-1-2
middle-0-1-2 : P.T.origin tree-0-1-2 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q7 , (m1 , F.vp-1-3))
middle-0-1-2 = refl
tree-0-1-3 : P.T.Tree
tree-0-1-3 = P.composition C.q0 C.q7 C.q7 F.triple-0-1-3
native-0-1-3 : P.T.R.Resolve (P.T.encode tree-0-1-3)
native-0-1-3 = P.T.realize tree-0-1-3
cell-0-1-3 : P.T.encode tree-0-1-3 ≡ E.A.V.composition-package C.q0 C.q7 C.q7 F.triple-0-1-3
cell-0-1-3 = P.composition-cell C.q0 C.q7 C.q7 F.triple-0-1-3
middle-0-1-3 : P.T.origin tree-0-1-3 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q7 , (c1 , F.vp-1-2))
middle-0-1-3 = refl
tree-0-2-1 : P.T.Tree
tree-0-2-1 = P.composition C.q0 C.q0 C.q7 F.triple-0-2-1
native-0-2-1 : P.T.R.Resolve (P.T.encode tree-0-2-1)
native-0-2-1 = P.T.realize tree-0-2-1
cell-0-2-1 : P.T.encode tree-0-2-1 ≡ E.A.V.composition-package C.q0 C.q0 C.q7 F.triple-0-2-1
cell-0-2-1 = P.composition-cell C.q0 C.q0 C.q7 F.triple-0-2-1
middle-0-2-1 : P.T.origin tree-0-2-1 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q0 , (m1 , F.vp-2-3))
middle-0-2-1 = refl
tree-0-2-3 : P.T.Tree
tree-0-2-3 = P.composition C.q0 C.q0 C.q7 F.triple-0-2-3
native-0-2-3 : P.T.R.Resolve (P.T.encode tree-0-2-3)
native-0-2-3 = P.T.realize tree-0-2-3
cell-0-2-3 : P.T.encode tree-0-2-3 ≡ E.A.V.composition-package C.q0 C.q0 C.q7 F.triple-0-2-3
cell-0-2-3 = P.composition-cell C.q0 C.q0 C.q7 F.triple-0-2-3
middle-0-2-3 : P.T.origin tree-0-2-3 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q0 , (m0 , F.vp-2-1))
middle-0-2-3 = refl
tree-0-3-1 : P.T.Tree
tree-0-3-1 = P.composition C.q0 C.q7 C.q7 F.triple-0-3-1
native-0-3-1 : P.T.R.Resolve (P.T.encode tree-0-3-1)
native-0-3-1 = P.T.realize tree-0-3-1
cell-0-3-1 : P.T.encode tree-0-3-1 ≡ E.A.V.composition-package C.q0 C.q7 C.q7 F.triple-0-3-1
cell-0-3-1 = P.composition-cell C.q0 C.q7 C.q7 F.triple-0-3-1
middle-0-3-1 : P.T.origin tree-0-3-1 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q7 , (c1 , F.vp-3-2))
middle-0-3-1 = refl
tree-0-3-2 : P.T.Tree
tree-0-3-2 = P.composition C.q0 C.q7 C.q0 F.triple-0-3-2
native-0-3-2 : P.T.R.Resolve (P.T.encode tree-0-3-2)
native-0-3-2 = P.T.realize tree-0-3-2
cell-0-3-2 : P.T.encode tree-0-3-2 ≡ E.A.V.composition-package C.q0 C.q7 C.q0 F.triple-0-3-2
cell-0-3-2 = P.composition-cell C.q0 C.q7 C.q0 F.triple-0-3-2
middle-0-3-2 : P.T.origin tree-0-3-2 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q7 , (m0 , F.vp-3-1))
middle-0-3-2 = refl
tree-1-0-2 : P.T.Tree
tree-1-0-2 = P.composition C.q7 C.q0 C.q0 F.triple-1-0-2
native-1-0-2 : P.T.R.Resolve (P.T.encode tree-1-0-2)
native-1-0-2 = P.T.realize tree-1-0-2
cell-1-0-2 : P.T.encode tree-1-0-2 ≡ E.A.V.composition-package C.q7 C.q0 C.q0 F.triple-1-0-2
cell-1-0-2 = P.composition-cell C.q7 C.q0 C.q0 F.triple-1-0-2
middle-1-0-2 : P.T.origin tree-1-0-2 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q0 , (m1 , F.vp-0-3))
middle-1-0-2 = refl
tree-1-0-3 : P.T.Tree
tree-1-0-3 = P.composition C.q7 C.q0 C.q7 F.triple-1-0-3
native-1-0-3 : P.T.R.Resolve (P.T.encode tree-1-0-3)
native-1-0-3 = P.T.realize tree-1-0-3
cell-1-0-3 : P.T.encode tree-1-0-3 ≡ E.A.V.composition-package C.q7 C.q0 C.q7 F.triple-1-0-3
cell-1-0-3 = P.composition-cell C.q7 C.q0 C.q7 F.triple-1-0-3
middle-1-0-3 : P.T.origin tree-1-0-3 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q0 , (c1 , F.vp-0-2))
middle-1-0-3 = refl
tree-1-2-0 : P.T.Tree
tree-1-2-0 = P.composition C.q7 C.q0 C.q0 F.triple-1-2-0
native-1-2-0 : P.T.R.Resolve (P.T.encode tree-1-2-0)
native-1-2-0 = P.T.realize tree-1-2-0
cell-1-2-0 : P.T.encode tree-1-2-0 ≡ E.A.V.composition-package C.q7 C.q0 C.q0 F.triple-1-2-0
cell-1-2-0 = P.composition-cell C.q7 C.q0 C.q0 F.triple-1-2-0
middle-1-2-0 : P.T.origin tree-1-2-0 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q0 , (m1 , F.vp-2-3))
middle-1-2-0 = refl
tree-1-2-3 : P.T.Tree
tree-1-2-3 = P.composition C.q7 C.q0 C.q7 F.triple-1-2-3
native-1-2-3 : P.T.R.Resolve (P.T.encode tree-1-2-3)
native-1-2-3 = P.T.realize tree-1-2-3
cell-1-2-3 : P.T.encode tree-1-2-3 ≡ E.A.V.composition-package C.q7 C.q0 C.q7 F.triple-1-2-3
cell-1-2-3 = P.composition-cell C.q7 C.q0 C.q7 F.triple-1-2-3
middle-1-2-3 : P.T.origin tree-1-2-3 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q0 , (c0 , F.vp-2-0))
middle-1-2-3 = refl
tree-1-3-0 : P.T.Tree
tree-1-3-0 = P.composition C.q7 C.q7 C.q0 F.triple-1-3-0
native-1-3-0 : P.T.R.Resolve (P.T.encode tree-1-3-0)
native-1-3-0 = P.T.realize tree-1-3-0
cell-1-3-0 : P.T.encode tree-1-3-0 ≡ E.A.V.composition-package C.q7 C.q7 C.q0 F.triple-1-3-0
cell-1-3-0 = P.composition-cell C.q7 C.q7 C.q0 F.triple-1-3-0
middle-1-3-0 : P.T.origin tree-1-3-0 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q7 , (c1 , F.vp-3-2))
middle-1-3-0 = refl
tree-1-3-2 : P.T.Tree
tree-1-3-2 = P.composition C.q7 C.q7 C.q0 F.triple-1-3-2
native-1-3-2 : P.T.R.Resolve (P.T.encode tree-1-3-2)
native-1-3-2 = P.T.realize tree-1-3-2
cell-1-3-2 : P.T.encode tree-1-3-2 ≡ E.A.V.composition-package C.q7 C.q7 C.q0 F.triple-1-3-2
cell-1-3-2 = P.composition-cell C.q7 C.q7 C.q0 F.triple-1-3-2
middle-1-3-2 : P.T.origin tree-1-3-2 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q7 , (c0 , F.vp-3-0))
middle-1-3-2 = refl
tree-2-0-1 : P.T.Tree
tree-2-0-1 = P.composition C.q0 C.q0 C.q7 F.triple-2-0-1
native-2-0-1 : P.T.R.Resolve (P.T.encode tree-2-0-1)
native-2-0-1 = P.T.realize tree-2-0-1
cell-2-0-1 : P.T.encode tree-2-0-1 ≡ E.A.V.composition-package C.q0 C.q0 C.q7 F.triple-2-0-1
cell-2-0-1 = P.composition-cell C.q0 C.q0 C.q7 F.triple-2-0-1
middle-2-0-1 : P.T.origin tree-2-0-1 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q0 , (m1 , F.vp-0-3))
middle-2-0-1 = refl
tree-2-0-3 : P.T.Tree
tree-2-0-3 = P.composition C.q0 C.q0 C.q7 F.triple-2-0-3
native-2-0-3 : P.T.R.Resolve (P.T.encode tree-2-0-3)
native-2-0-3 = P.T.realize tree-2-0-3
cell-2-0-3 : P.T.encode tree-2-0-3 ≡ E.A.V.composition-package C.q0 C.q0 C.q7 F.triple-2-0-3
cell-2-0-3 = P.composition-cell C.q0 C.q0 C.q7 F.triple-2-0-3
middle-2-0-3 : P.T.origin tree-2-0-3 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q0 , (m0 , F.vp-0-1))
middle-2-0-3 = refl
tree-2-1-0 : P.T.Tree
tree-2-1-0 = P.composition C.q0 C.q7 C.q0 F.triple-2-1-0
native-2-1-0 : P.T.R.Resolve (P.T.encode tree-2-1-0)
native-2-1-0 = P.T.realize tree-2-1-0
cell-2-1-0 : P.T.encode tree-2-1-0 ≡ E.A.V.composition-package C.q0 C.q7 C.q0 F.triple-2-1-0
cell-2-1-0 = P.composition-cell C.q0 C.q7 C.q0 F.triple-2-1-0
middle-2-1-0 : P.T.origin tree-2-1-0 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q7 , (m1 , F.vp-1-3))
middle-2-1-0 = refl
tree-2-1-3 : P.T.Tree
tree-2-1-3 = P.composition C.q0 C.q7 C.q7 F.triple-2-1-3
native-2-1-3 : P.T.R.Resolve (P.T.encode tree-2-1-3)
native-2-1-3 = P.T.realize tree-2-1-3
cell-2-1-3 : P.T.encode tree-2-1-3 ≡ E.A.V.composition-package C.q0 C.q7 C.q7 F.triple-2-1-3
cell-2-1-3 = P.composition-cell C.q0 C.q7 C.q7 F.triple-2-1-3
middle-2-1-3 : P.T.origin tree-2-1-3 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q7 , (c0 , F.vp-1-0))
middle-2-1-3 = refl
tree-2-3-0 : P.T.Tree
tree-2-3-0 = P.composition C.q0 C.q7 C.q0 F.triple-2-3-0
native-2-3-0 : P.T.R.Resolve (P.T.encode tree-2-3-0)
native-2-3-0 = P.T.realize tree-2-3-0
cell-2-3-0 : P.T.encode tree-2-3-0 ≡ E.A.V.composition-package C.q0 C.q7 C.q0 F.triple-2-3-0
cell-2-3-0 = P.composition-cell C.q0 C.q7 C.q0 F.triple-2-3-0
middle-2-3-0 : P.T.origin tree-2-3-0 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q7 , (m0 , F.vp-3-1))
middle-2-3-0 = refl
tree-2-3-1 : P.T.Tree
tree-2-3-1 = P.composition C.q0 C.q7 C.q7 F.triple-2-3-1
native-2-3-1 : P.T.R.Resolve (P.T.encode tree-2-3-1)
native-2-3-1 = P.T.realize tree-2-3-1
cell-2-3-1 : P.T.encode tree-2-3-1 ≡ E.A.V.composition-package C.q0 C.q7 C.q7 F.triple-2-3-1
cell-2-3-1 = P.composition-cell C.q0 C.q7 C.q7 F.triple-2-3-1
middle-2-3-1 : P.T.origin tree-2-3-1 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q7 , (c0 , F.vp-3-0))
middle-2-3-1 = refl
tree-3-0-1 : P.T.Tree
tree-3-0-1 = P.composition C.q7 C.q0 C.q7 F.triple-3-0-1
native-3-0-1 : P.T.R.Resolve (P.T.encode tree-3-0-1)
native-3-0-1 = P.T.realize tree-3-0-1
cell-3-0-1 : P.T.encode tree-3-0-1 ≡ E.A.V.composition-package C.q7 C.q0 C.q7 F.triple-3-0-1
cell-3-0-1 = P.composition-cell C.q7 C.q0 C.q7 F.triple-3-0-1
middle-3-0-1 : P.T.origin tree-3-0-1 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q0 , (c1 , F.vp-0-2))
middle-3-0-1 = refl
tree-3-0-2 : P.T.Tree
tree-3-0-2 = P.composition C.q7 C.q0 C.q0 F.triple-3-0-2
native-3-0-2 : P.T.R.Resolve (P.T.encode tree-3-0-2)
native-3-0-2 = P.T.realize tree-3-0-2
cell-3-0-2 : P.T.encode tree-3-0-2 ≡ E.A.V.composition-package C.q7 C.q0 C.q0 F.triple-3-0-2
cell-3-0-2 = P.composition-cell C.q7 C.q0 C.q0 F.triple-3-0-2
middle-3-0-2 : P.T.origin tree-3-0-2 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q0 , (m0 , F.vp-0-1))
middle-3-0-2 = refl
tree-3-1-0 : P.T.Tree
tree-3-1-0 = P.composition C.q7 C.q7 C.q0 F.triple-3-1-0
native-3-1-0 : P.T.R.Resolve (P.T.encode tree-3-1-0)
native-3-1-0 = P.T.realize tree-3-1-0
cell-3-1-0 : P.T.encode tree-3-1-0 ≡ E.A.V.composition-package C.q7 C.q7 C.q0 F.triple-3-1-0
cell-3-1-0 = P.composition-cell C.q7 C.q7 C.q0 F.triple-3-1-0
middle-3-1-0 : P.T.origin tree-3-1-0 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q7 , (c1 , F.vp-1-2))
middle-3-1-0 = refl
tree-3-1-2 : P.T.Tree
tree-3-1-2 = P.composition C.q7 C.q7 C.q0 F.triple-3-1-2
native-3-1-2 : P.T.R.Resolve (P.T.encode tree-3-1-2)
native-3-1-2 = P.T.realize tree-3-1-2
cell-3-1-2 : P.T.encode tree-3-1-2 ≡ E.A.V.composition-package C.q7 C.q7 C.q0 F.triple-3-1-2
cell-3-1-2 = P.composition-cell C.q7 C.q7 C.q0 F.triple-3-1-2
middle-3-1-2 : P.T.origin tree-3-1-2 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q7 , (c0 , F.vp-1-0))
middle-3-1-2 = refl
tree-3-2-0 : P.T.Tree
tree-3-2-0 = P.composition C.q7 C.q0 C.q0 F.triple-3-2-0
native-3-2-0 : P.T.R.Resolve (P.T.encode tree-3-2-0)
native-3-2-0 = P.T.realize tree-3-2-0
cell-3-2-0 : P.T.encode tree-3-2-0 ≡ E.A.V.composition-package C.q7 C.q0 C.q0 F.triple-3-2-0
cell-3-2-0 = P.composition-cell C.q7 C.q0 C.q0 F.triple-3-2-0
middle-3-2-0 : P.T.origin tree-3-2-0 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q0 , (m0 , F.vp-2-1))
middle-3-2-0 = refl
tree-3-2-1 : P.T.Tree
tree-3-2-1 = P.composition C.q7 C.q0 C.q7 F.triple-3-2-1
native-3-2-1 : P.T.R.Resolve (P.T.encode tree-3-2-1)
native-3-2-1 = P.T.realize tree-3-2-1
cell-3-2-1 : P.T.encode tree-3-2-1 ≡ E.A.V.composition-package C.q7 C.q0 C.q7 F.triple-3-2-1
cell-3-2-1 = P.composition-cell C.q7 C.q0 C.q7 F.triple-3-2-1
middle-3-2-1 : P.T.origin tree-3-2-1 (P.S.full-source , (P.S.middle-port , tt)) ≡ (C.q0 , (c0 , F.vp-2-0))
middle-3-2-1 = refl
module B = Trees Bool (λ _ → "same literal payload")
left right : B.Located
left = B.leaf false , tt
right = B.leaf true , tt
raw-equal : B.encode (fst left) ≡ B.encode (fst right)
raw-equal = refl
no-external-erasure : left ≡ right → ⊥
no-external-erasure path = false≢true (cong B.source-of path)
