{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyFourFacetVertexCells where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import RamseySingleFrameFaces using (c0; m0; c1; m1)
open import RamseyUniformRelative using (first; next)
import RamseyRequestedPortExamples as C
open import RamseyNativeEdgeAttachments
open import RamseyEdgeAttachmentsExamples
vp-0-1 : A.VertexPermit C.q0 m0
vp-0-1 = c0 , (refl , ((first) , refl))
vp-0-2 : A.VertexPermit C.q0 c1
vp-0-2 = c0 , (refl , ((next first) , refl))
vp-0-3 : A.VertexPermit C.q0 m1
vp-0-3 = c0 , (refl , ((next (next first)) , refl))
vp-1-0 : A.VertexPermit C.q7 c0
vp-1-0 = m0 , (refl , ((first) , refl))
vp-1-2 : A.VertexPermit C.q7 c1
vp-1-2 = m0 , (refl , ((next first) , refl))
vp-1-3 : A.VertexPermit C.q7 m1
vp-1-3 = m0 , (refl , ((next (next first)) , refl))
vp-2-0 : A.VertexPermit C.q0 c0
vp-2-0 = c1 , (refl , ((first) , refl))
vp-2-1 : A.VertexPermit C.q0 m0
vp-2-1 = c1 , (refl , ((next first) , refl))
vp-2-3 : A.VertexPermit C.q0 m1
vp-2-3 = c1 , (refl , ((next (next first)) , refl))
vp-3-0 : A.VertexPermit C.q7 c0
vp-3-0 = m1 , (refl , ((first) , refl))
vp-3-1 : A.VertexPermit C.q7 m0
vp-3-1 = m1 , (refl , ((next first) , refl))
vp-3-2 : A.VertexPermit C.q7 c1
vp-3-2 = m1 , (refl , ((next (next first)) , refl))
edge-0-1 : A.S.Common C.q0 C.q7
edge-0-1 = e23 , (att-0-0-5 , att-7-1-5)
edge-0-1-native : A.S.R.Resolve (A.S.selected-package C.q0 C.q7 edge-0-1)
edge-0-1-native = A.S.selected-proof C.q0 C.q7 edge-0-1
edge-0-2 : A.S.Common C.q0 C.q0
edge-0-2 = e13 , (att-0-0-4 , att-0-2-4)
edge-0-2-native : A.S.R.Resolve (A.S.selected-package C.q0 C.q0 edge-0-2)
edge-0-2-native = A.S.selected-proof C.q0 C.q0 edge-0-2
edge-0-3 : A.S.Common C.q0 C.q7
edge-0-3 = e12 , (att-0-0-3 , att-7-3-3)
edge-0-3-native : A.S.R.Resolve (A.S.selected-package C.q0 C.q7 edge-0-3)
edge-0-3-native = A.S.selected-proof C.q0 C.q7 edge-0-3
edge-1-0 : A.S.Common C.q7 C.q0
edge-1-0 = e23 , (att-7-1-5 , att-0-0-5)
edge-1-0-native : A.S.R.Resolve (A.S.selected-package C.q7 C.q0 edge-1-0)
edge-1-0-native = A.S.selected-proof C.q7 C.q0 edge-1-0
edge-1-2 : A.S.Common C.q7 C.q0
edge-1-2 = e03 , (att-7-1-2 , att-0-2-2)
edge-1-2-native : A.S.R.Resolve (A.S.selected-package C.q7 C.q0 edge-1-2)
edge-1-2-native = A.S.selected-proof C.q7 C.q0 edge-1-2
edge-1-3 : A.S.Common C.q7 C.q7
edge-1-3 = e02 , (att-7-1-1 , att-7-3-1)
edge-1-3-native : A.S.R.Resolve (A.S.selected-package C.q7 C.q7 edge-1-3)
edge-1-3-native = A.S.selected-proof C.q7 C.q7 edge-1-3
edge-2-0 : A.S.Common C.q0 C.q0
edge-2-0 = e13 , (att-0-2-4 , att-0-0-4)
edge-2-0-native : A.S.R.Resolve (A.S.selected-package C.q0 C.q0 edge-2-0)
edge-2-0-native = A.S.selected-proof C.q0 C.q0 edge-2-0
edge-2-1 : A.S.Common C.q0 C.q7
edge-2-1 = e03 , (att-0-2-2 , att-7-1-2)
edge-2-1-native : A.S.R.Resolve (A.S.selected-package C.q0 C.q7 edge-2-1)
edge-2-1-native = A.S.selected-proof C.q0 C.q7 edge-2-1
edge-2-3 : A.S.Common C.q0 C.q7
edge-2-3 = e01 , (att-0-2-0 , att-7-3-0)
edge-2-3-native : A.S.R.Resolve (A.S.selected-package C.q0 C.q7 edge-2-3)
edge-2-3-native = A.S.selected-proof C.q0 C.q7 edge-2-3
edge-3-0 : A.S.Common C.q7 C.q0
edge-3-0 = e12 , (att-7-3-3 , att-0-0-3)
edge-3-0-native : A.S.R.Resolve (A.S.selected-package C.q7 C.q0 edge-3-0)
edge-3-0-native = A.S.selected-proof C.q7 C.q0 edge-3-0
edge-3-1 : A.S.Common C.q7 C.q7
edge-3-1 = e02 , (att-7-3-1 , att-7-1-1)
edge-3-1-native : A.S.R.Resolve (A.S.selected-package C.q7 C.q7 edge-3-1)
edge-3-1-native = A.S.selected-proof C.q7 C.q7 edge-3-1
edge-3-2 : A.S.Common C.q7 C.q0
edge-3-2 = e01 , (att-7-3-0 , att-0-2-0)
edge-3-2-native : A.S.R.Resolve (A.S.selected-package C.q7 C.q0 edge-3-2)
edge-3-2-native = A.S.selected-proof C.q7 C.q0 edge-3-2
triple-0-1-2 : A.V.Triple C.q0 C.q7 C.q0
triple-0-1-2 = m1 , (vp-0-3 , (vp-1-3 , vp-2-3))
triple-0-1-2-native : A.V.R.Resolve (A.V.composition-package C.q0 C.q7 C.q0 triple-0-1-2)
triple-0-1-2-native = A.V.composition-proof C.q0 C.q7 C.q0 triple-0-1-2
route-ab-0-1-2 : A.V.Common C.q0 C.q7
route-ab-0-1-2 = A.restrict-common true {a = C.q0} {b = C.q7} edge-0-1
cell-ab-0-1-2 : route-ab-0-1-2 ≡ A.V.ab-index {a = C.q0} {b = C.q7} {c = C.q0} triple-0-1-2
cell-ab-0-1-2 = refl
route-bc-0-1-2 : A.V.Common C.q7 C.q0
route-bc-0-1-2 = A.restrict-common true {a = C.q7} {b = C.q0} edge-1-2
cell-bc-0-1-2 : route-bc-0-1-2 ≡ A.V.bc-index {a = C.q0} {b = C.q7} {c = C.q0} triple-0-1-2
cell-bc-0-1-2 = refl
route-ac-0-1-2 : A.V.Common C.q0 C.q0
route-ac-0-1-2 = A.restrict-common true {a = C.q0} {b = C.q0} edge-0-2
cell-ac-0-1-2 : route-ac-0-1-2 ≡ A.V.ac-index {a = C.q0} {b = C.q7} {c = C.q0} triple-0-1-2
cell-ac-0-1-2 = refl
middle-0-1-2 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-ab-0-1-2 , A.V.selected-proof C.q0 C.q7 route-ab-0-1-2) (lift route-ab-0-1-2)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-bc-0-1-2 , A.V.selected-proof C.q7 C.q0 route-bc-0-1-2) (lift route-bc-0-1-2)) (lift A.V.source-leg)
middle-0-1-2 = refl
triple-0-1-3 : A.V.Triple C.q0 C.q7 C.q7
triple-0-1-3 = c1 , (vp-0-2 , (vp-1-2 , vp-3-2))
triple-0-1-3-native : A.V.R.Resolve (A.V.composition-package C.q0 C.q7 C.q7 triple-0-1-3)
triple-0-1-3-native = A.V.composition-proof C.q0 C.q7 C.q7 triple-0-1-3
route-ab-0-1-3 : A.V.Common C.q0 C.q7
route-ab-0-1-3 = A.restrict-common false {a = C.q0} {b = C.q7} edge-0-1
cell-ab-0-1-3 : route-ab-0-1-3 ≡ A.V.ab-index {a = C.q0} {b = C.q7} {c = C.q7} triple-0-1-3
cell-ab-0-1-3 = refl
route-bc-0-1-3 : A.V.Common C.q7 C.q7
route-bc-0-1-3 = A.restrict-common true {a = C.q7} {b = C.q7} edge-1-3
cell-bc-0-1-3 : route-bc-0-1-3 ≡ A.V.bc-index {a = C.q0} {b = C.q7} {c = C.q7} triple-0-1-3
cell-bc-0-1-3 = refl
route-ac-0-1-3 : A.V.Common C.q0 C.q7
route-ac-0-1-3 = A.restrict-common true {a = C.q0} {b = C.q7} edge-0-3
cell-ac-0-1-3 : route-ac-0-1-3 ≡ A.V.ac-index {a = C.q0} {b = C.q7} {c = C.q7} triple-0-1-3
cell-ac-0-1-3 = refl
middle-0-1-3 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-ab-0-1-3 , A.V.selected-proof C.q0 C.q7 route-ab-0-1-3) (lift route-ab-0-1-3)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q7 route-bc-0-1-3 , A.V.selected-proof C.q7 C.q7 route-bc-0-1-3) (lift route-bc-0-1-3)) (lift A.V.source-leg)
middle-0-1-3 = refl
triple-0-2-1 : A.V.Triple C.q0 C.q0 C.q7
triple-0-2-1 = m1 , (vp-0-3 , (vp-2-3 , vp-1-3))
triple-0-2-1-native : A.V.R.Resolve (A.V.composition-package C.q0 C.q0 C.q7 triple-0-2-1)
triple-0-2-1-native = A.V.composition-proof C.q0 C.q0 C.q7 triple-0-2-1
route-ab-0-2-1 : A.V.Common C.q0 C.q0
route-ab-0-2-1 = A.restrict-common true {a = C.q0} {b = C.q0} edge-0-2
cell-ab-0-2-1 : route-ab-0-2-1 ≡ A.V.ab-index {a = C.q0} {b = C.q0} {c = C.q7} triple-0-2-1
cell-ab-0-2-1 = refl
route-bc-0-2-1 : A.V.Common C.q0 C.q7
route-bc-0-2-1 = A.restrict-common true {a = C.q0} {b = C.q7} edge-2-1
cell-bc-0-2-1 : route-bc-0-2-1 ≡ A.V.bc-index {a = C.q0} {b = C.q0} {c = C.q7} triple-0-2-1
cell-bc-0-2-1 = refl
route-ac-0-2-1 : A.V.Common C.q0 C.q7
route-ac-0-2-1 = A.restrict-common true {a = C.q0} {b = C.q7} edge-0-1
cell-ac-0-2-1 : route-ac-0-2-1 ≡ A.V.ac-index {a = C.q0} {b = C.q0} {c = C.q7} triple-0-2-1
cell-ac-0-2-1 = refl
middle-0-2-1 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q0 route-ab-0-2-1 , A.V.selected-proof C.q0 C.q0 route-ab-0-2-1) (lift route-ab-0-2-1)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-bc-0-2-1 , A.V.selected-proof C.q0 C.q7 route-bc-0-2-1) (lift route-bc-0-2-1)) (lift A.V.source-leg)
middle-0-2-1 = refl
triple-0-2-3 : A.V.Triple C.q0 C.q0 C.q7
triple-0-2-3 = m0 , (vp-0-1 , (vp-2-1 , vp-3-1))
triple-0-2-3-native : A.V.R.Resolve (A.V.composition-package C.q0 C.q0 C.q7 triple-0-2-3)
triple-0-2-3-native = A.V.composition-proof C.q0 C.q0 C.q7 triple-0-2-3
route-ab-0-2-3 : A.V.Common C.q0 C.q0
route-ab-0-2-3 = A.restrict-common false {a = C.q0} {b = C.q0} edge-0-2
cell-ab-0-2-3 : route-ab-0-2-3 ≡ A.V.ab-index {a = C.q0} {b = C.q0} {c = C.q7} triple-0-2-3
cell-ab-0-2-3 = refl
route-bc-0-2-3 : A.V.Common C.q0 C.q7
route-bc-0-2-3 = A.restrict-common true {a = C.q0} {b = C.q7} edge-2-3
cell-bc-0-2-3 : route-bc-0-2-3 ≡ A.V.bc-index {a = C.q0} {b = C.q0} {c = C.q7} triple-0-2-3
cell-bc-0-2-3 = refl
route-ac-0-2-3 : A.V.Common C.q0 C.q7
route-ac-0-2-3 = A.restrict-common false {a = C.q0} {b = C.q7} edge-0-3
cell-ac-0-2-3 : route-ac-0-2-3 ≡ A.V.ac-index {a = C.q0} {b = C.q0} {c = C.q7} triple-0-2-3
cell-ac-0-2-3 = refl
middle-0-2-3 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q0 route-ab-0-2-3 , A.V.selected-proof C.q0 C.q0 route-ab-0-2-3) (lift route-ab-0-2-3)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-bc-0-2-3 , A.V.selected-proof C.q0 C.q7 route-bc-0-2-3) (lift route-bc-0-2-3)) (lift A.V.source-leg)
middle-0-2-3 = refl
triple-0-3-1 : A.V.Triple C.q0 C.q7 C.q7
triple-0-3-1 = c1 , (vp-0-2 , (vp-3-2 , vp-1-2))
triple-0-3-1-native : A.V.R.Resolve (A.V.composition-package C.q0 C.q7 C.q7 triple-0-3-1)
triple-0-3-1-native = A.V.composition-proof C.q0 C.q7 C.q7 triple-0-3-1
route-ab-0-3-1 : A.V.Common C.q0 C.q7
route-ab-0-3-1 = A.restrict-common true {a = C.q0} {b = C.q7} edge-0-3
cell-ab-0-3-1 : route-ab-0-3-1 ≡ A.V.ab-index {a = C.q0} {b = C.q7} {c = C.q7} triple-0-3-1
cell-ab-0-3-1 = refl
route-bc-0-3-1 : A.V.Common C.q7 C.q7
route-bc-0-3-1 = A.restrict-common true {a = C.q7} {b = C.q7} edge-3-1
cell-bc-0-3-1 : route-bc-0-3-1 ≡ A.V.bc-index {a = C.q0} {b = C.q7} {c = C.q7} triple-0-3-1
cell-bc-0-3-1 = refl
route-ac-0-3-1 : A.V.Common C.q0 C.q7
route-ac-0-3-1 = A.restrict-common false {a = C.q0} {b = C.q7} edge-0-1
cell-ac-0-3-1 : route-ac-0-3-1 ≡ A.V.ac-index {a = C.q0} {b = C.q7} {c = C.q7} triple-0-3-1
cell-ac-0-3-1 = refl
middle-0-3-1 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-ab-0-3-1 , A.V.selected-proof C.q0 C.q7 route-ab-0-3-1) (lift route-ab-0-3-1)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q7 route-bc-0-3-1 , A.V.selected-proof C.q7 C.q7 route-bc-0-3-1) (lift route-bc-0-3-1)) (lift A.V.source-leg)
middle-0-3-1 = refl
triple-0-3-2 : A.V.Triple C.q0 C.q7 C.q0
triple-0-3-2 = m0 , (vp-0-1 , (vp-3-1 , vp-2-1))
triple-0-3-2-native : A.V.R.Resolve (A.V.composition-package C.q0 C.q7 C.q0 triple-0-3-2)
triple-0-3-2-native = A.V.composition-proof C.q0 C.q7 C.q0 triple-0-3-2
route-ab-0-3-2 : A.V.Common C.q0 C.q7
route-ab-0-3-2 = A.restrict-common false {a = C.q0} {b = C.q7} edge-0-3
cell-ab-0-3-2 : route-ab-0-3-2 ≡ A.V.ab-index {a = C.q0} {b = C.q7} {c = C.q0} triple-0-3-2
cell-ab-0-3-2 = refl
route-bc-0-3-2 : A.V.Common C.q7 C.q0
route-bc-0-3-2 = A.restrict-common true {a = C.q7} {b = C.q0} edge-3-2
cell-bc-0-3-2 : route-bc-0-3-2 ≡ A.V.bc-index {a = C.q0} {b = C.q7} {c = C.q0} triple-0-3-2
cell-bc-0-3-2 = refl
route-ac-0-3-2 : A.V.Common C.q0 C.q0
route-ac-0-3-2 = A.restrict-common false {a = C.q0} {b = C.q0} edge-0-2
cell-ac-0-3-2 : route-ac-0-3-2 ≡ A.V.ac-index {a = C.q0} {b = C.q7} {c = C.q0} triple-0-3-2
cell-ac-0-3-2 = refl
middle-0-3-2 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-ab-0-3-2 , A.V.selected-proof C.q0 C.q7 route-ab-0-3-2) (lift route-ab-0-3-2)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-bc-0-3-2 , A.V.selected-proof C.q7 C.q0 route-bc-0-3-2) (lift route-bc-0-3-2)) (lift A.V.source-leg)
middle-0-3-2 = refl
triple-1-0-2 : A.V.Triple C.q7 C.q0 C.q0
triple-1-0-2 = m1 , (vp-1-3 , (vp-0-3 , vp-2-3))
triple-1-0-2-native : A.V.R.Resolve (A.V.composition-package C.q7 C.q0 C.q0 triple-1-0-2)
triple-1-0-2-native = A.V.composition-proof C.q7 C.q0 C.q0 triple-1-0-2
route-ab-1-0-2 : A.V.Common C.q7 C.q0
route-ab-1-0-2 = A.restrict-common true {a = C.q7} {b = C.q0} edge-1-0
cell-ab-1-0-2 : route-ab-1-0-2 ≡ A.V.ab-index {a = C.q7} {b = C.q0} {c = C.q0} triple-1-0-2
cell-ab-1-0-2 = refl
route-bc-1-0-2 : A.V.Common C.q0 C.q0
route-bc-1-0-2 = A.restrict-common true {a = C.q0} {b = C.q0} edge-0-2
cell-bc-1-0-2 : route-bc-1-0-2 ≡ A.V.bc-index {a = C.q7} {b = C.q0} {c = C.q0} triple-1-0-2
cell-bc-1-0-2 = refl
route-ac-1-0-2 : A.V.Common C.q7 C.q0
route-ac-1-0-2 = A.restrict-common true {a = C.q7} {b = C.q0} edge-1-2
cell-ac-1-0-2 : route-ac-1-0-2 ≡ A.V.ac-index {a = C.q7} {b = C.q0} {c = C.q0} triple-1-0-2
cell-ac-1-0-2 = refl
middle-1-0-2 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-ab-1-0-2 , A.V.selected-proof C.q7 C.q0 route-ab-1-0-2) (lift route-ab-1-0-2)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q0 route-bc-1-0-2 , A.V.selected-proof C.q0 C.q0 route-bc-1-0-2) (lift route-bc-1-0-2)) (lift A.V.source-leg)
middle-1-0-2 = refl
triple-1-0-3 : A.V.Triple C.q7 C.q0 C.q7
triple-1-0-3 = c1 , (vp-1-2 , (vp-0-2 , vp-3-2))
triple-1-0-3-native : A.V.R.Resolve (A.V.composition-package C.q7 C.q0 C.q7 triple-1-0-3)
triple-1-0-3-native = A.V.composition-proof C.q7 C.q0 C.q7 triple-1-0-3
route-ab-1-0-3 : A.V.Common C.q7 C.q0
route-ab-1-0-3 = A.restrict-common false {a = C.q7} {b = C.q0} edge-1-0
cell-ab-1-0-3 : route-ab-1-0-3 ≡ A.V.ab-index {a = C.q7} {b = C.q0} {c = C.q7} triple-1-0-3
cell-ab-1-0-3 = refl
route-bc-1-0-3 : A.V.Common C.q0 C.q7
route-bc-1-0-3 = A.restrict-common true {a = C.q0} {b = C.q7} edge-0-3
cell-bc-1-0-3 : route-bc-1-0-3 ≡ A.V.bc-index {a = C.q7} {b = C.q0} {c = C.q7} triple-1-0-3
cell-bc-1-0-3 = refl
route-ac-1-0-3 : A.V.Common C.q7 C.q7
route-ac-1-0-3 = A.restrict-common true {a = C.q7} {b = C.q7} edge-1-3
cell-ac-1-0-3 : route-ac-1-0-3 ≡ A.V.ac-index {a = C.q7} {b = C.q0} {c = C.q7} triple-1-0-3
cell-ac-1-0-3 = refl
middle-1-0-3 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-ab-1-0-3 , A.V.selected-proof C.q7 C.q0 route-ab-1-0-3) (lift route-ab-1-0-3)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-bc-1-0-3 , A.V.selected-proof C.q0 C.q7 route-bc-1-0-3) (lift route-bc-1-0-3)) (lift A.V.source-leg)
middle-1-0-3 = refl
triple-1-2-0 : A.V.Triple C.q7 C.q0 C.q0
triple-1-2-0 = m1 , (vp-1-3 , (vp-2-3 , vp-0-3))
triple-1-2-0-native : A.V.R.Resolve (A.V.composition-package C.q7 C.q0 C.q0 triple-1-2-0)
triple-1-2-0-native = A.V.composition-proof C.q7 C.q0 C.q0 triple-1-2-0
route-ab-1-2-0 : A.V.Common C.q7 C.q0
route-ab-1-2-0 = A.restrict-common true {a = C.q7} {b = C.q0} edge-1-2
cell-ab-1-2-0 : route-ab-1-2-0 ≡ A.V.ab-index {a = C.q7} {b = C.q0} {c = C.q0} triple-1-2-0
cell-ab-1-2-0 = refl
route-bc-1-2-0 : A.V.Common C.q0 C.q0
route-bc-1-2-0 = A.restrict-common true {a = C.q0} {b = C.q0} edge-2-0
cell-bc-1-2-0 : route-bc-1-2-0 ≡ A.V.bc-index {a = C.q7} {b = C.q0} {c = C.q0} triple-1-2-0
cell-bc-1-2-0 = refl
route-ac-1-2-0 : A.V.Common C.q7 C.q0
route-ac-1-2-0 = A.restrict-common true {a = C.q7} {b = C.q0} edge-1-0
cell-ac-1-2-0 : route-ac-1-2-0 ≡ A.V.ac-index {a = C.q7} {b = C.q0} {c = C.q0} triple-1-2-0
cell-ac-1-2-0 = refl
middle-1-2-0 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-ab-1-2-0 , A.V.selected-proof C.q7 C.q0 route-ab-1-2-0) (lift route-ab-1-2-0)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q0 route-bc-1-2-0 , A.V.selected-proof C.q0 C.q0 route-bc-1-2-0) (lift route-bc-1-2-0)) (lift A.V.source-leg)
middle-1-2-0 = refl
triple-1-2-3 : A.V.Triple C.q7 C.q0 C.q7
triple-1-2-3 = c0 , (vp-1-0 , (vp-2-0 , vp-3-0))
triple-1-2-3-native : A.V.R.Resolve (A.V.composition-package C.q7 C.q0 C.q7 triple-1-2-3)
triple-1-2-3-native = A.V.composition-proof C.q7 C.q0 C.q7 triple-1-2-3
route-ab-1-2-3 : A.V.Common C.q7 C.q0
route-ab-1-2-3 = A.restrict-common false {a = C.q7} {b = C.q0} edge-1-2
cell-ab-1-2-3 : route-ab-1-2-3 ≡ A.V.ab-index {a = C.q7} {b = C.q0} {c = C.q7} triple-1-2-3
cell-ab-1-2-3 = refl
route-bc-1-2-3 : A.V.Common C.q0 C.q7
route-bc-1-2-3 = A.restrict-common false {a = C.q0} {b = C.q7} edge-2-3
cell-bc-1-2-3 : route-bc-1-2-3 ≡ A.V.bc-index {a = C.q7} {b = C.q0} {c = C.q7} triple-1-2-3
cell-bc-1-2-3 = refl
route-ac-1-2-3 : A.V.Common C.q7 C.q7
route-ac-1-2-3 = A.restrict-common false {a = C.q7} {b = C.q7} edge-1-3
cell-ac-1-2-3 : route-ac-1-2-3 ≡ A.V.ac-index {a = C.q7} {b = C.q0} {c = C.q7} triple-1-2-3
cell-ac-1-2-3 = refl
middle-1-2-3 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-ab-1-2-3 , A.V.selected-proof C.q7 C.q0 route-ab-1-2-3) (lift route-ab-1-2-3)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-bc-1-2-3 , A.V.selected-proof C.q0 C.q7 route-bc-1-2-3) (lift route-bc-1-2-3)) (lift A.V.source-leg)
middle-1-2-3 = refl
triple-1-3-0 : A.V.Triple C.q7 C.q7 C.q0
triple-1-3-0 = c1 , (vp-1-2 , (vp-3-2 , vp-0-2))
triple-1-3-0-native : A.V.R.Resolve (A.V.composition-package C.q7 C.q7 C.q0 triple-1-3-0)
triple-1-3-0-native = A.V.composition-proof C.q7 C.q7 C.q0 triple-1-3-0
route-ab-1-3-0 : A.V.Common C.q7 C.q7
route-ab-1-3-0 = A.restrict-common true {a = C.q7} {b = C.q7} edge-1-3
cell-ab-1-3-0 : route-ab-1-3-0 ≡ A.V.ab-index {a = C.q7} {b = C.q7} {c = C.q0} triple-1-3-0
cell-ab-1-3-0 = refl
route-bc-1-3-0 : A.V.Common C.q7 C.q0
route-bc-1-3-0 = A.restrict-common true {a = C.q7} {b = C.q0} edge-3-0
cell-bc-1-3-0 : route-bc-1-3-0 ≡ A.V.bc-index {a = C.q7} {b = C.q7} {c = C.q0} triple-1-3-0
cell-bc-1-3-0 = refl
route-ac-1-3-0 : A.V.Common C.q7 C.q0
route-ac-1-3-0 = A.restrict-common false {a = C.q7} {b = C.q0} edge-1-0
cell-ac-1-3-0 : route-ac-1-3-0 ≡ A.V.ac-index {a = C.q7} {b = C.q7} {c = C.q0} triple-1-3-0
cell-ac-1-3-0 = refl
middle-1-3-0 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q7 route-ab-1-3-0 , A.V.selected-proof C.q7 C.q7 route-ab-1-3-0) (lift route-ab-1-3-0)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-bc-1-3-0 , A.V.selected-proof C.q7 C.q0 route-bc-1-3-0) (lift route-bc-1-3-0)) (lift A.V.source-leg)
middle-1-3-0 = refl
triple-1-3-2 : A.V.Triple C.q7 C.q7 C.q0
triple-1-3-2 = c0 , (vp-1-0 , (vp-3-0 , vp-2-0))
triple-1-3-2-native : A.V.R.Resolve (A.V.composition-package C.q7 C.q7 C.q0 triple-1-3-2)
triple-1-3-2-native = A.V.composition-proof C.q7 C.q7 C.q0 triple-1-3-2
route-ab-1-3-2 : A.V.Common C.q7 C.q7
route-ab-1-3-2 = A.restrict-common false {a = C.q7} {b = C.q7} edge-1-3
cell-ab-1-3-2 : route-ab-1-3-2 ≡ A.V.ab-index {a = C.q7} {b = C.q7} {c = C.q0} triple-1-3-2
cell-ab-1-3-2 = refl
route-bc-1-3-2 : A.V.Common C.q7 C.q0
route-bc-1-3-2 = A.restrict-common false {a = C.q7} {b = C.q0} edge-3-2
cell-bc-1-3-2 : route-bc-1-3-2 ≡ A.V.bc-index {a = C.q7} {b = C.q7} {c = C.q0} triple-1-3-2
cell-bc-1-3-2 = refl
route-ac-1-3-2 : A.V.Common C.q7 C.q0
route-ac-1-3-2 = A.restrict-common false {a = C.q7} {b = C.q0} edge-1-2
cell-ac-1-3-2 : route-ac-1-3-2 ≡ A.V.ac-index {a = C.q7} {b = C.q7} {c = C.q0} triple-1-3-2
cell-ac-1-3-2 = refl
middle-1-3-2 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q7 route-ab-1-3-2 , A.V.selected-proof C.q7 C.q7 route-ab-1-3-2) (lift route-ab-1-3-2)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-bc-1-3-2 , A.V.selected-proof C.q7 C.q0 route-bc-1-3-2) (lift route-bc-1-3-2)) (lift A.V.source-leg)
middle-1-3-2 = refl
triple-2-0-1 : A.V.Triple C.q0 C.q0 C.q7
triple-2-0-1 = m1 , (vp-2-3 , (vp-0-3 , vp-1-3))
triple-2-0-1-native : A.V.R.Resolve (A.V.composition-package C.q0 C.q0 C.q7 triple-2-0-1)
triple-2-0-1-native = A.V.composition-proof C.q0 C.q0 C.q7 triple-2-0-1
route-ab-2-0-1 : A.V.Common C.q0 C.q0
route-ab-2-0-1 = A.restrict-common true {a = C.q0} {b = C.q0} edge-2-0
cell-ab-2-0-1 : route-ab-2-0-1 ≡ A.V.ab-index {a = C.q0} {b = C.q0} {c = C.q7} triple-2-0-1
cell-ab-2-0-1 = refl
route-bc-2-0-1 : A.V.Common C.q0 C.q7
route-bc-2-0-1 = A.restrict-common true {a = C.q0} {b = C.q7} edge-0-1
cell-bc-2-0-1 : route-bc-2-0-1 ≡ A.V.bc-index {a = C.q0} {b = C.q0} {c = C.q7} triple-2-0-1
cell-bc-2-0-1 = refl
route-ac-2-0-1 : A.V.Common C.q0 C.q7
route-ac-2-0-1 = A.restrict-common true {a = C.q0} {b = C.q7} edge-2-1
cell-ac-2-0-1 : route-ac-2-0-1 ≡ A.V.ac-index {a = C.q0} {b = C.q0} {c = C.q7} triple-2-0-1
cell-ac-2-0-1 = refl
middle-2-0-1 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q0 route-ab-2-0-1 , A.V.selected-proof C.q0 C.q0 route-ab-2-0-1) (lift route-ab-2-0-1)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-bc-2-0-1 , A.V.selected-proof C.q0 C.q7 route-bc-2-0-1) (lift route-bc-2-0-1)) (lift A.V.source-leg)
middle-2-0-1 = refl
triple-2-0-3 : A.V.Triple C.q0 C.q0 C.q7
triple-2-0-3 = m0 , (vp-2-1 , (vp-0-1 , vp-3-1))
triple-2-0-3-native : A.V.R.Resolve (A.V.composition-package C.q0 C.q0 C.q7 triple-2-0-3)
triple-2-0-3-native = A.V.composition-proof C.q0 C.q0 C.q7 triple-2-0-3
route-ab-2-0-3 : A.V.Common C.q0 C.q0
route-ab-2-0-3 = A.restrict-common false {a = C.q0} {b = C.q0} edge-2-0
cell-ab-2-0-3 : route-ab-2-0-3 ≡ A.V.ab-index {a = C.q0} {b = C.q0} {c = C.q7} triple-2-0-3
cell-ab-2-0-3 = refl
route-bc-2-0-3 : A.V.Common C.q0 C.q7
route-bc-2-0-3 = A.restrict-common false {a = C.q0} {b = C.q7} edge-0-3
cell-bc-2-0-3 : route-bc-2-0-3 ≡ A.V.bc-index {a = C.q0} {b = C.q0} {c = C.q7} triple-2-0-3
cell-bc-2-0-3 = refl
route-ac-2-0-3 : A.V.Common C.q0 C.q7
route-ac-2-0-3 = A.restrict-common true {a = C.q0} {b = C.q7} edge-2-3
cell-ac-2-0-3 : route-ac-2-0-3 ≡ A.V.ac-index {a = C.q0} {b = C.q0} {c = C.q7} triple-2-0-3
cell-ac-2-0-3 = refl
middle-2-0-3 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q0 route-ab-2-0-3 , A.V.selected-proof C.q0 C.q0 route-ab-2-0-3) (lift route-ab-2-0-3)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-bc-2-0-3 , A.V.selected-proof C.q0 C.q7 route-bc-2-0-3) (lift route-bc-2-0-3)) (lift A.V.source-leg)
middle-2-0-3 = refl
triple-2-1-0 : A.V.Triple C.q0 C.q7 C.q0
triple-2-1-0 = m1 , (vp-2-3 , (vp-1-3 , vp-0-3))
triple-2-1-0-native : A.V.R.Resolve (A.V.composition-package C.q0 C.q7 C.q0 triple-2-1-0)
triple-2-1-0-native = A.V.composition-proof C.q0 C.q7 C.q0 triple-2-1-0
route-ab-2-1-0 : A.V.Common C.q0 C.q7
route-ab-2-1-0 = A.restrict-common true {a = C.q0} {b = C.q7} edge-2-1
cell-ab-2-1-0 : route-ab-2-1-0 ≡ A.V.ab-index {a = C.q0} {b = C.q7} {c = C.q0} triple-2-1-0
cell-ab-2-1-0 = refl
route-bc-2-1-0 : A.V.Common C.q7 C.q0
route-bc-2-1-0 = A.restrict-common true {a = C.q7} {b = C.q0} edge-1-0
cell-bc-2-1-0 : route-bc-2-1-0 ≡ A.V.bc-index {a = C.q0} {b = C.q7} {c = C.q0} triple-2-1-0
cell-bc-2-1-0 = refl
route-ac-2-1-0 : A.V.Common C.q0 C.q0
route-ac-2-1-0 = A.restrict-common true {a = C.q0} {b = C.q0} edge-2-0
cell-ac-2-1-0 : route-ac-2-1-0 ≡ A.V.ac-index {a = C.q0} {b = C.q7} {c = C.q0} triple-2-1-0
cell-ac-2-1-0 = refl
middle-2-1-0 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-ab-2-1-0 , A.V.selected-proof C.q0 C.q7 route-ab-2-1-0) (lift route-ab-2-1-0)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-bc-2-1-0 , A.V.selected-proof C.q7 C.q0 route-bc-2-1-0) (lift route-bc-2-1-0)) (lift A.V.source-leg)
middle-2-1-0 = refl
triple-2-1-3 : A.V.Triple C.q0 C.q7 C.q7
triple-2-1-3 = c0 , (vp-2-0 , (vp-1-0 , vp-3-0))
triple-2-1-3-native : A.V.R.Resolve (A.V.composition-package C.q0 C.q7 C.q7 triple-2-1-3)
triple-2-1-3-native = A.V.composition-proof C.q0 C.q7 C.q7 triple-2-1-3
route-ab-2-1-3 : A.V.Common C.q0 C.q7
route-ab-2-1-3 = A.restrict-common false {a = C.q0} {b = C.q7} edge-2-1
cell-ab-2-1-3 : route-ab-2-1-3 ≡ A.V.ab-index {a = C.q0} {b = C.q7} {c = C.q7} triple-2-1-3
cell-ab-2-1-3 = refl
route-bc-2-1-3 : A.V.Common C.q7 C.q7
route-bc-2-1-3 = A.restrict-common false {a = C.q7} {b = C.q7} edge-1-3
cell-bc-2-1-3 : route-bc-2-1-3 ≡ A.V.bc-index {a = C.q0} {b = C.q7} {c = C.q7} triple-2-1-3
cell-bc-2-1-3 = refl
route-ac-2-1-3 : A.V.Common C.q0 C.q7
route-ac-2-1-3 = A.restrict-common false {a = C.q0} {b = C.q7} edge-2-3
cell-ac-2-1-3 : route-ac-2-1-3 ≡ A.V.ac-index {a = C.q0} {b = C.q7} {c = C.q7} triple-2-1-3
cell-ac-2-1-3 = refl
middle-2-1-3 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-ab-2-1-3 , A.V.selected-proof C.q0 C.q7 route-ab-2-1-3) (lift route-ab-2-1-3)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q7 route-bc-2-1-3 , A.V.selected-proof C.q7 C.q7 route-bc-2-1-3) (lift route-bc-2-1-3)) (lift A.V.source-leg)
middle-2-1-3 = refl
triple-2-3-0 : A.V.Triple C.q0 C.q7 C.q0
triple-2-3-0 = m0 , (vp-2-1 , (vp-3-1 , vp-0-1))
triple-2-3-0-native : A.V.R.Resolve (A.V.composition-package C.q0 C.q7 C.q0 triple-2-3-0)
triple-2-3-0-native = A.V.composition-proof C.q0 C.q7 C.q0 triple-2-3-0
route-ab-2-3-0 : A.V.Common C.q0 C.q7
route-ab-2-3-0 = A.restrict-common true {a = C.q0} {b = C.q7} edge-2-3
cell-ab-2-3-0 : route-ab-2-3-0 ≡ A.V.ab-index {a = C.q0} {b = C.q7} {c = C.q0} triple-2-3-0
cell-ab-2-3-0 = refl
route-bc-2-3-0 : A.V.Common C.q7 C.q0
route-bc-2-3-0 = A.restrict-common false {a = C.q7} {b = C.q0} edge-3-0
cell-bc-2-3-0 : route-bc-2-3-0 ≡ A.V.bc-index {a = C.q0} {b = C.q7} {c = C.q0} triple-2-3-0
cell-bc-2-3-0 = refl
route-ac-2-3-0 : A.V.Common C.q0 C.q0
route-ac-2-3-0 = A.restrict-common false {a = C.q0} {b = C.q0} edge-2-0
cell-ac-2-3-0 : route-ac-2-3-0 ≡ A.V.ac-index {a = C.q0} {b = C.q7} {c = C.q0} triple-2-3-0
cell-ac-2-3-0 = refl
middle-2-3-0 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-ab-2-3-0 , A.V.selected-proof C.q0 C.q7 route-ab-2-3-0) (lift route-ab-2-3-0)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-bc-2-3-0 , A.V.selected-proof C.q7 C.q0 route-bc-2-3-0) (lift route-bc-2-3-0)) (lift A.V.source-leg)
middle-2-3-0 = refl
triple-2-3-1 : A.V.Triple C.q0 C.q7 C.q7
triple-2-3-1 = c0 , (vp-2-0 , (vp-3-0 , vp-1-0))
triple-2-3-1-native : A.V.R.Resolve (A.V.composition-package C.q0 C.q7 C.q7 triple-2-3-1)
triple-2-3-1-native = A.V.composition-proof C.q0 C.q7 C.q7 triple-2-3-1
route-ab-2-3-1 : A.V.Common C.q0 C.q7
route-ab-2-3-1 = A.restrict-common false {a = C.q0} {b = C.q7} edge-2-3
cell-ab-2-3-1 : route-ab-2-3-1 ≡ A.V.ab-index {a = C.q0} {b = C.q7} {c = C.q7} triple-2-3-1
cell-ab-2-3-1 = refl
route-bc-2-3-1 : A.V.Common C.q7 C.q7
route-bc-2-3-1 = A.restrict-common false {a = C.q7} {b = C.q7} edge-3-1
cell-bc-2-3-1 : route-bc-2-3-1 ≡ A.V.bc-index {a = C.q0} {b = C.q7} {c = C.q7} triple-2-3-1
cell-bc-2-3-1 = refl
route-ac-2-3-1 : A.V.Common C.q0 C.q7
route-ac-2-3-1 = A.restrict-common false {a = C.q0} {b = C.q7} edge-2-1
cell-ac-2-3-1 : route-ac-2-3-1 ≡ A.V.ac-index {a = C.q0} {b = C.q7} {c = C.q7} triple-2-3-1
cell-ac-2-3-1 = refl
middle-2-3-1 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-ab-2-3-1 , A.V.selected-proof C.q0 C.q7 route-ab-2-3-1) (lift route-ab-2-3-1)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q7 route-bc-2-3-1 , A.V.selected-proof C.q7 C.q7 route-bc-2-3-1) (lift route-bc-2-3-1)) (lift A.V.source-leg)
middle-2-3-1 = refl
triple-3-0-1 : A.V.Triple C.q7 C.q0 C.q7
triple-3-0-1 = c1 , (vp-3-2 , (vp-0-2 , vp-1-2))
triple-3-0-1-native : A.V.R.Resolve (A.V.composition-package C.q7 C.q0 C.q7 triple-3-0-1)
triple-3-0-1-native = A.V.composition-proof C.q7 C.q0 C.q7 triple-3-0-1
route-ab-3-0-1 : A.V.Common C.q7 C.q0
route-ab-3-0-1 = A.restrict-common true {a = C.q7} {b = C.q0} edge-3-0
cell-ab-3-0-1 : route-ab-3-0-1 ≡ A.V.ab-index {a = C.q7} {b = C.q0} {c = C.q7} triple-3-0-1
cell-ab-3-0-1 = refl
route-bc-3-0-1 : A.V.Common C.q0 C.q7
route-bc-3-0-1 = A.restrict-common false {a = C.q0} {b = C.q7} edge-0-1
cell-bc-3-0-1 : route-bc-3-0-1 ≡ A.V.bc-index {a = C.q7} {b = C.q0} {c = C.q7} triple-3-0-1
cell-bc-3-0-1 = refl
route-ac-3-0-1 : A.V.Common C.q7 C.q7
route-ac-3-0-1 = A.restrict-common true {a = C.q7} {b = C.q7} edge-3-1
cell-ac-3-0-1 : route-ac-3-0-1 ≡ A.V.ac-index {a = C.q7} {b = C.q0} {c = C.q7} triple-3-0-1
cell-ac-3-0-1 = refl
middle-3-0-1 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-ab-3-0-1 , A.V.selected-proof C.q7 C.q0 route-ab-3-0-1) (lift route-ab-3-0-1)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-bc-3-0-1 , A.V.selected-proof C.q0 C.q7 route-bc-3-0-1) (lift route-bc-3-0-1)) (lift A.V.source-leg)
middle-3-0-1 = refl
triple-3-0-2 : A.V.Triple C.q7 C.q0 C.q0
triple-3-0-2 = m0 , (vp-3-1 , (vp-0-1 , vp-2-1))
triple-3-0-2-native : A.V.R.Resolve (A.V.composition-package C.q7 C.q0 C.q0 triple-3-0-2)
triple-3-0-2-native = A.V.composition-proof C.q7 C.q0 C.q0 triple-3-0-2
route-ab-3-0-2 : A.V.Common C.q7 C.q0
route-ab-3-0-2 = A.restrict-common false {a = C.q7} {b = C.q0} edge-3-0
cell-ab-3-0-2 : route-ab-3-0-2 ≡ A.V.ab-index {a = C.q7} {b = C.q0} {c = C.q0} triple-3-0-2
cell-ab-3-0-2 = refl
route-bc-3-0-2 : A.V.Common C.q0 C.q0
route-bc-3-0-2 = A.restrict-common false {a = C.q0} {b = C.q0} edge-0-2
cell-bc-3-0-2 : route-bc-3-0-2 ≡ A.V.bc-index {a = C.q7} {b = C.q0} {c = C.q0} triple-3-0-2
cell-bc-3-0-2 = refl
route-ac-3-0-2 : A.V.Common C.q7 C.q0
route-ac-3-0-2 = A.restrict-common true {a = C.q7} {b = C.q0} edge-3-2
cell-ac-3-0-2 : route-ac-3-0-2 ≡ A.V.ac-index {a = C.q7} {b = C.q0} {c = C.q0} triple-3-0-2
cell-ac-3-0-2 = refl
middle-3-0-2 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-ab-3-0-2 , A.V.selected-proof C.q7 C.q0 route-ab-3-0-2) (lift route-ab-3-0-2)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q0 route-bc-3-0-2 , A.V.selected-proof C.q0 C.q0 route-bc-3-0-2) (lift route-bc-3-0-2)) (lift A.V.source-leg)
middle-3-0-2 = refl
triple-3-1-0 : A.V.Triple C.q7 C.q7 C.q0
triple-3-1-0 = c1 , (vp-3-2 , (vp-1-2 , vp-0-2))
triple-3-1-0-native : A.V.R.Resolve (A.V.composition-package C.q7 C.q7 C.q0 triple-3-1-0)
triple-3-1-0-native = A.V.composition-proof C.q7 C.q7 C.q0 triple-3-1-0
route-ab-3-1-0 : A.V.Common C.q7 C.q7
route-ab-3-1-0 = A.restrict-common true {a = C.q7} {b = C.q7} edge-3-1
cell-ab-3-1-0 : route-ab-3-1-0 ≡ A.V.ab-index {a = C.q7} {b = C.q7} {c = C.q0} triple-3-1-0
cell-ab-3-1-0 = refl
route-bc-3-1-0 : A.V.Common C.q7 C.q0
route-bc-3-1-0 = A.restrict-common false {a = C.q7} {b = C.q0} edge-1-0
cell-bc-3-1-0 : route-bc-3-1-0 ≡ A.V.bc-index {a = C.q7} {b = C.q7} {c = C.q0} triple-3-1-0
cell-bc-3-1-0 = refl
route-ac-3-1-0 : A.V.Common C.q7 C.q0
route-ac-3-1-0 = A.restrict-common true {a = C.q7} {b = C.q0} edge-3-0
cell-ac-3-1-0 : route-ac-3-1-0 ≡ A.V.ac-index {a = C.q7} {b = C.q7} {c = C.q0} triple-3-1-0
cell-ac-3-1-0 = refl
middle-3-1-0 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q7 route-ab-3-1-0 , A.V.selected-proof C.q7 C.q7 route-ab-3-1-0) (lift route-ab-3-1-0)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-bc-3-1-0 , A.V.selected-proof C.q7 C.q0 route-bc-3-1-0) (lift route-bc-3-1-0)) (lift A.V.source-leg)
middle-3-1-0 = refl
triple-3-1-2 : A.V.Triple C.q7 C.q7 C.q0
triple-3-1-2 = c0 , (vp-3-0 , (vp-1-0 , vp-2-0))
triple-3-1-2-native : A.V.R.Resolve (A.V.composition-package C.q7 C.q7 C.q0 triple-3-1-2)
triple-3-1-2-native = A.V.composition-proof C.q7 C.q7 C.q0 triple-3-1-2
route-ab-3-1-2 : A.V.Common C.q7 C.q7
route-ab-3-1-2 = A.restrict-common false {a = C.q7} {b = C.q7} edge-3-1
cell-ab-3-1-2 : route-ab-3-1-2 ≡ A.V.ab-index {a = C.q7} {b = C.q7} {c = C.q0} triple-3-1-2
cell-ab-3-1-2 = refl
route-bc-3-1-2 : A.V.Common C.q7 C.q0
route-bc-3-1-2 = A.restrict-common false {a = C.q7} {b = C.q0} edge-1-2
cell-bc-3-1-2 : route-bc-3-1-2 ≡ A.V.bc-index {a = C.q7} {b = C.q7} {c = C.q0} triple-3-1-2
cell-bc-3-1-2 = refl
route-ac-3-1-2 : A.V.Common C.q7 C.q0
route-ac-3-1-2 = A.restrict-common false {a = C.q7} {b = C.q0} edge-3-2
cell-ac-3-1-2 : route-ac-3-1-2 ≡ A.V.ac-index {a = C.q7} {b = C.q7} {c = C.q0} triple-3-1-2
cell-ac-3-1-2 = refl
middle-3-1-2 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q7 route-ab-3-1-2 , A.V.selected-proof C.q7 C.q7 route-ab-3-1-2) (lift route-ab-3-1-2)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-bc-3-1-2 , A.V.selected-proof C.q7 C.q0 route-bc-3-1-2) (lift route-bc-3-1-2)) (lift A.V.source-leg)
middle-3-1-2 = refl
triple-3-2-0 : A.V.Triple C.q7 C.q0 C.q0
triple-3-2-0 = m0 , (vp-3-1 , (vp-2-1 , vp-0-1))
triple-3-2-0-native : A.V.R.Resolve (A.V.composition-package C.q7 C.q0 C.q0 triple-3-2-0)
triple-3-2-0-native = A.V.composition-proof C.q7 C.q0 C.q0 triple-3-2-0
route-ab-3-2-0 : A.V.Common C.q7 C.q0
route-ab-3-2-0 = A.restrict-common true {a = C.q7} {b = C.q0} edge-3-2
cell-ab-3-2-0 : route-ab-3-2-0 ≡ A.V.ab-index {a = C.q7} {b = C.q0} {c = C.q0} triple-3-2-0
cell-ab-3-2-0 = refl
route-bc-3-2-0 : A.V.Common C.q0 C.q0
route-bc-3-2-0 = A.restrict-common false {a = C.q0} {b = C.q0} edge-2-0
cell-bc-3-2-0 : route-bc-3-2-0 ≡ A.V.bc-index {a = C.q7} {b = C.q0} {c = C.q0} triple-3-2-0
cell-bc-3-2-0 = refl
route-ac-3-2-0 : A.V.Common C.q7 C.q0
route-ac-3-2-0 = A.restrict-common false {a = C.q7} {b = C.q0} edge-3-0
cell-ac-3-2-0 : route-ac-3-2-0 ≡ A.V.ac-index {a = C.q7} {b = C.q0} {c = C.q0} triple-3-2-0
cell-ac-3-2-0 = refl
middle-3-2-0 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-ab-3-2-0 , A.V.selected-proof C.q7 C.q0 route-ab-3-2-0) (lift route-ab-3-2-0)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q0 route-bc-3-2-0 , A.V.selected-proof C.q0 C.q0 route-bc-3-2-0) (lift route-bc-3-2-0)) (lift A.V.source-leg)
middle-3-2-0 = refl
triple-3-2-1 : A.V.Triple C.q7 C.q0 C.q7
triple-3-2-1 = c0 , (vp-3-0 , (vp-2-0 , vp-1-0))
triple-3-2-1-native : A.V.R.Resolve (A.V.composition-package C.q7 C.q0 C.q7 triple-3-2-1)
triple-3-2-1-native = A.V.composition-proof C.q7 C.q0 C.q7 triple-3-2-1
route-ab-3-2-1 : A.V.Common C.q7 C.q0
route-ab-3-2-1 = A.restrict-common false {a = C.q7} {b = C.q0} edge-3-2
cell-ab-3-2-1 : route-ab-3-2-1 ≡ A.V.ab-index {a = C.q7} {b = C.q0} {c = C.q7} triple-3-2-1
cell-ab-3-2-1 = refl
route-bc-3-2-1 : A.V.Common C.q0 C.q7
route-bc-3-2-1 = A.restrict-common false {a = C.q0} {b = C.q7} edge-2-1
cell-bc-3-2-1 : route-bc-3-2-1 ≡ A.V.bc-index {a = C.q7} {b = C.q0} {c = C.q7} triple-3-2-1
cell-bc-3-2-1 = refl
route-ac-3-2-1 : A.V.Common C.q7 C.q7
route-ac-3-2-1 = A.restrict-common false {a = C.q7} {b = C.q7} edge-3-1
cell-ac-3-2-1 : route-ac-3-2-1 ≡ A.V.ac-index {a = C.q7} {b = C.q0} {c = C.q7} triple-3-2-1
cell-ac-3-2-1 = refl
middle-3-2-1 : A.V.R.premise (A.V.R.premise (A.V.selected-package C.q7 C.q0 route-ab-3-2-1 , A.V.selected-proof C.q7 C.q0 route-ab-3-2-1) (lift route-ab-3-2-1)) (lift A.V.target-leg) ≡ A.V.R.premise (A.V.R.premise (A.V.selected-package C.q0 C.q7 route-bc-3-2-1 , A.V.selected-proof C.q0 C.q7 route-bc-3-2-1) (lift route-bc-3-2-1)) (lift A.V.source-leg)
middle-3-2-1 = refl
