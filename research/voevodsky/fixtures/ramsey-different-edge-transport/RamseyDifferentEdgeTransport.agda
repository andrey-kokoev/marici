{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyDifferentEdgeTransport where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import RamseySingleFrameFaces using (c0; m0; c1; m1)
open import RamseyEndpointPolicy using (base; complement; side-map)
import RamseyRequestedPortExamples as C
import RamseyEdgeAttachmentsExamples as E
import RamseyFourFacetVertexCells as F
import RamseyCommonSelection as K
import RamseyEndpointFamily as H
import RamseyTripleNaturality as T
import RamseyPermitEquivalence as M
edge-0-1 : K.edge-move base complement F.edge-0-1 ≡ F.edge-1-0
edge-0-1 = refl
edge-0-2 : K.edge-move base base F.edge-0-2 ≡ F.edge-1-3
edge-0-2 = refl
edge-0-3 : K.edge-move base complement F.edge-0-3 ≡ F.edge-1-2
edge-0-3 = refl
edge-1-0 : K.edge-move complement base F.edge-1-0 ≡ F.edge-0-1
edge-1-0 = refl
edge-1-2 : K.edge-move complement base F.edge-1-2 ≡ F.edge-0-3
edge-1-2 = refl
edge-1-3 : K.edge-move complement complement F.edge-1-3 ≡ F.edge-0-2
edge-1-3 = refl
edge-2-0 : K.edge-move base base F.edge-2-0 ≡ F.edge-3-1
edge-2-0 = refl
edge-2-1 : K.edge-move base complement F.edge-2-1 ≡ F.edge-3-0
edge-2-1 = refl
edge-2-3 : K.edge-move base complement F.edge-2-3 ≡ F.edge-3-2
edge-2-3 = refl
edge-3-0 : K.edge-move complement base F.edge-3-0 ≡ F.edge-2-1
edge-3-0 = refl
edge-3-1 : K.edge-move complement complement F.edge-3-1 ≡ F.edge-2-0
edge-3-1 = refl
edge-3-2 : K.edge-move complement base F.edge-3-2 ≡ F.edge-2-3
edge-3-2 = refl
triple-0-1-2 : T.vertex-triple base complement base F.triple-0-1-2 ≡ F.triple-1-0-3
triple-0-1-2 = refl
bind-ab-0-1-2 : F.route-ab-0-1-2 ≡ H.family base complement F.edge-0-1 true
bind-ab-0-1-2 = refl
side-ab-0-1-2 : side-map (fst F.edge-0-1) true ≡ false
side-ab-0-1-2 = refl
route-ab-0-1-2 : K.vertex-move base complement F.route-ab-0-1-2 ≡ F.route-ab-1-0-3
route-ab-0-1-2 = refl
natural-ab-0-1-2 : K.vertex-move base complement F.route-ab-0-1-2 ≡ F.route-ab-1-0-3
natural-ab-0-1-2 = H.covariance base complement F.edge-0-1 true
coherence-ab-0-1-2 : route-ab-0-1-2 ≡ natural-ab-0-1-2
coherence-ab-0-1-2 = H.common-set complement base _ _ _ _
bind-bc-0-1-2 : F.route-bc-0-1-2 ≡ H.family complement base F.edge-1-2 true
bind-bc-0-1-2 = refl
side-bc-0-1-2 : side-map (fst F.edge-1-2) true ≡ true
side-bc-0-1-2 = refl
route-bc-0-1-2 : K.vertex-move complement base F.route-bc-0-1-2 ≡ F.route-bc-1-0-3
route-bc-0-1-2 = refl
natural-bc-0-1-2 : K.vertex-move complement base F.route-bc-0-1-2 ≡ F.route-bc-1-0-3
natural-bc-0-1-2 = H.covariance complement base F.edge-1-2 true
coherence-bc-0-1-2 : route-bc-0-1-2 ≡ natural-bc-0-1-2
coherence-bc-0-1-2 = H.common-set base complement _ _ _ _
bind-ac-0-1-2 : F.route-ac-0-1-2 ≡ H.family base base F.edge-0-2 true
bind-ac-0-1-2 = refl
side-ac-0-1-2 : side-map (fst F.edge-0-2) true ≡ true
side-ac-0-1-2 = refl
route-ac-0-1-2 : K.vertex-move base base F.route-ac-0-1-2 ≡ F.route-ac-1-0-3
route-ac-0-1-2 = refl
natural-ac-0-1-2 : K.vertex-move base base F.route-ac-0-1-2 ≡ F.route-ac-1-0-3
natural-ac-0-1-2 = H.covariance base base F.edge-0-2 true
coherence-ac-0-1-2 : route-ac-0-1-2 ≡ natural-ac-0-1-2
coherence-ac-0-1-2 = H.common-set complement complement _ _ _ _
moved-ab-0-1-2 : E.A.V.InputIndex
moved-ab-0-1-2 = (C.q0 , (c1 , M.move-7-3 (snd (snd F.route-ab-0-1-2))))
moved-bc-0-1-2 : E.A.V.InputIndex
moved-bc-0-1-2 = (C.q0 , (c1 , M.move-7-3 (fst (snd F.route-bc-0-1-2))))
target-ab-0-1-2 : E.A.V.InputIndex
target-ab-0-1-2 = (C.q0 , (fst F.route-ab-1-0-3 , snd (snd F.route-ab-1-0-3)))
target-bc-0-1-2 : E.A.V.InputIndex
target-bc-0-1-2 = (C.q0 , (fst F.route-bc-1-0-3 , fst (snd F.route-bc-1-0-3)))
middle-0-1-2 : moved-ab-0-1-2 ≡ moved-bc-0-1-2
middle-0-1-2 = refl
middle-ab-0-1-2 : moved-ab-0-1-2 ≡ target-ab-0-1-2
middle-ab-0-1-2 = refl
middle-bc-0-1-2 : moved-bc-0-1-2 ≡ target-bc-0-1-2
middle-bc-0-1-2 = refl
target-native-seam-0-1-2 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-ab-1-0-3 , E.A.V.selected-proof C.q7 C.q0 F.route-ab-1-0-3) (lift F.route-ab-1-0-3)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-bc-1-0-3 , E.A.V.selected-proof C.q0 C.q7 F.route-bc-1-0-3) (lift F.route-bc-1-0-3)) (lift E.A.V.source-leg)
target-native-seam-0-1-2 = F.middle-1-0-3
triple-0-1-3 : T.vertex-triple base complement complement F.triple-0-1-3 ≡ F.triple-1-0-2
triple-0-1-3 = refl
bind-ab-0-1-3 : F.route-ab-0-1-3 ≡ H.family base complement F.edge-0-1 false
bind-ab-0-1-3 = refl
side-ab-0-1-3 : side-map (fst F.edge-0-1) false ≡ true
side-ab-0-1-3 = refl
route-ab-0-1-3 : K.vertex-move base complement F.route-ab-0-1-3 ≡ F.route-ab-1-0-2
route-ab-0-1-3 = refl
natural-ab-0-1-3 : K.vertex-move base complement F.route-ab-0-1-3 ≡ F.route-ab-1-0-2
natural-ab-0-1-3 = H.covariance base complement F.edge-0-1 false
coherence-ab-0-1-3 : route-ab-0-1-3 ≡ natural-ab-0-1-3
coherence-ab-0-1-3 = H.common-set complement base _ _ _ _
bind-bc-0-1-3 : F.route-bc-0-1-3 ≡ H.family complement complement F.edge-1-3 true
bind-bc-0-1-3 = refl
side-bc-0-1-3 : side-map (fst F.edge-1-3) true ≡ true
side-bc-0-1-3 = refl
route-bc-0-1-3 : K.vertex-move complement complement F.route-bc-0-1-3 ≡ F.route-bc-1-0-2
route-bc-0-1-3 = refl
natural-bc-0-1-3 : K.vertex-move complement complement F.route-bc-0-1-3 ≡ F.route-bc-1-0-2
natural-bc-0-1-3 = H.covariance complement complement F.edge-1-3 true
coherence-bc-0-1-3 : route-bc-0-1-3 ≡ natural-bc-0-1-3
coherence-bc-0-1-3 = H.common-set base base _ _ _ _
bind-ac-0-1-3 : F.route-ac-0-1-3 ≡ H.family base complement F.edge-0-3 true
bind-ac-0-1-3 = refl
side-ac-0-1-3 : side-map (fst F.edge-0-3) true ≡ true
side-ac-0-1-3 = refl
route-ac-0-1-3 : K.vertex-move base complement F.route-ac-0-1-3 ≡ F.route-ac-1-0-2
route-ac-0-1-3 = refl
natural-ac-0-1-3 : K.vertex-move base complement F.route-ac-0-1-3 ≡ F.route-ac-1-0-2
natural-ac-0-1-3 = H.covariance base complement F.edge-0-3 true
coherence-ac-0-1-3 : route-ac-0-1-3 ≡ natural-ac-0-1-3
coherence-ac-0-1-3 = H.common-set complement base _ _ _ _
moved-ab-0-1-3 : E.A.V.InputIndex
moved-ab-0-1-3 = (C.q0 , (m1 , M.move-7-2 (snd (snd F.route-ab-0-1-3))))
moved-bc-0-1-3 : E.A.V.InputIndex
moved-bc-0-1-3 = (C.q0 , (m1 , M.move-7-2 (fst (snd F.route-bc-0-1-3))))
target-ab-0-1-3 : E.A.V.InputIndex
target-ab-0-1-3 = (C.q0 , (fst F.route-ab-1-0-2 , snd (snd F.route-ab-1-0-2)))
target-bc-0-1-3 : E.A.V.InputIndex
target-bc-0-1-3 = (C.q0 , (fst F.route-bc-1-0-2 , fst (snd F.route-bc-1-0-2)))
middle-0-1-3 : moved-ab-0-1-3 ≡ moved-bc-0-1-3
middle-0-1-3 = refl
middle-ab-0-1-3 : moved-ab-0-1-3 ≡ target-ab-0-1-3
middle-ab-0-1-3 = refl
middle-bc-0-1-3 : moved-bc-0-1-3 ≡ target-bc-0-1-3
middle-bc-0-1-3 = refl
target-native-seam-0-1-3 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-ab-1-0-2 , E.A.V.selected-proof C.q7 C.q0 F.route-ab-1-0-2) (lift F.route-ab-1-0-2)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q0 F.route-bc-1-0-2 , E.A.V.selected-proof C.q0 C.q0 F.route-bc-1-0-2) (lift F.route-bc-1-0-2)) (lift E.A.V.source-leg)
target-native-seam-0-1-3 = F.middle-1-0-2
triple-0-2-1 : T.vertex-triple base base complement F.triple-0-2-1 ≡ F.triple-1-3-0
triple-0-2-1 = refl
bind-ab-0-2-1 : F.route-ab-0-2-1 ≡ H.family base base F.edge-0-2 true
bind-ab-0-2-1 = refl
side-ab-0-2-1 : side-map (fst F.edge-0-2) true ≡ true
side-ab-0-2-1 = refl
route-ab-0-2-1 : K.vertex-move base base F.route-ab-0-2-1 ≡ F.route-ab-1-3-0
route-ab-0-2-1 = refl
natural-ab-0-2-1 : K.vertex-move base base F.route-ab-0-2-1 ≡ F.route-ab-1-3-0
natural-ab-0-2-1 = H.covariance base base F.edge-0-2 true
coherence-ab-0-2-1 : route-ab-0-2-1 ≡ natural-ab-0-2-1
coherence-ab-0-2-1 = H.common-set complement complement _ _ _ _
bind-bc-0-2-1 : F.route-bc-0-2-1 ≡ H.family base complement F.edge-2-1 true
bind-bc-0-2-1 = refl
side-bc-0-2-1 : side-map (fst F.edge-2-1) true ≡ true
side-bc-0-2-1 = refl
route-bc-0-2-1 : K.vertex-move base complement F.route-bc-0-2-1 ≡ F.route-bc-1-3-0
route-bc-0-2-1 = refl
natural-bc-0-2-1 : K.vertex-move base complement F.route-bc-0-2-1 ≡ F.route-bc-1-3-0
natural-bc-0-2-1 = H.covariance base complement F.edge-2-1 true
coherence-bc-0-2-1 : route-bc-0-2-1 ≡ natural-bc-0-2-1
coherence-bc-0-2-1 = H.common-set complement base _ _ _ _
bind-ac-0-2-1 : F.route-ac-0-2-1 ≡ H.family base complement F.edge-0-1 true
bind-ac-0-2-1 = refl
side-ac-0-2-1 : side-map (fst F.edge-0-1) true ≡ false
side-ac-0-2-1 = refl
route-ac-0-2-1 : K.vertex-move base complement F.route-ac-0-2-1 ≡ F.route-ac-1-3-0
route-ac-0-2-1 = refl
natural-ac-0-2-1 : K.vertex-move base complement F.route-ac-0-2-1 ≡ F.route-ac-1-3-0
natural-ac-0-2-1 = H.covariance base complement F.edge-0-1 true
coherence-ac-0-2-1 : route-ac-0-2-1 ≡ natural-ac-0-2-1
coherence-ac-0-2-1 = H.common-set complement base _ _ _ _
moved-ab-0-2-1 : E.A.V.InputIndex
moved-ab-0-2-1 = (C.q7 , (c1 , M.move-0-3 (snd (snd F.route-ab-0-2-1))))
moved-bc-0-2-1 : E.A.V.InputIndex
moved-bc-0-2-1 = (C.q7 , (c1 , M.move-0-3 (fst (snd F.route-bc-0-2-1))))
target-ab-0-2-1 : E.A.V.InputIndex
target-ab-0-2-1 = (C.q7 , (fst F.route-ab-1-3-0 , snd (snd F.route-ab-1-3-0)))
target-bc-0-2-1 : E.A.V.InputIndex
target-bc-0-2-1 = (C.q7 , (fst F.route-bc-1-3-0 , fst (snd F.route-bc-1-3-0)))
middle-0-2-1 : moved-ab-0-2-1 ≡ moved-bc-0-2-1
middle-0-2-1 = refl
middle-ab-0-2-1 : moved-ab-0-2-1 ≡ target-ab-0-2-1
middle-ab-0-2-1 = refl
middle-bc-0-2-1 : moved-bc-0-2-1 ≡ target-bc-0-2-1
middle-bc-0-2-1 = refl
target-native-seam-0-2-1 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q7 F.route-ab-1-3-0 , E.A.V.selected-proof C.q7 C.q7 F.route-ab-1-3-0) (lift F.route-ab-1-3-0)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-bc-1-3-0 , E.A.V.selected-proof C.q7 C.q0 F.route-bc-1-3-0) (lift F.route-bc-1-3-0)) (lift E.A.V.source-leg)
target-native-seam-0-2-1 = F.middle-1-3-0
triple-0-2-3 : T.vertex-triple base base complement F.triple-0-2-3 ≡ F.triple-1-3-2
triple-0-2-3 = refl
bind-ab-0-2-3 : F.route-ab-0-2-3 ≡ H.family base base F.edge-0-2 false
bind-ab-0-2-3 = refl
side-ab-0-2-3 : side-map (fst F.edge-0-2) false ≡ false
side-ab-0-2-3 = refl
route-ab-0-2-3 : K.vertex-move base base F.route-ab-0-2-3 ≡ F.route-ab-1-3-2
route-ab-0-2-3 = refl
natural-ab-0-2-3 : K.vertex-move base base F.route-ab-0-2-3 ≡ F.route-ab-1-3-2
natural-ab-0-2-3 = H.covariance base base F.edge-0-2 false
coherence-ab-0-2-3 : route-ab-0-2-3 ≡ natural-ab-0-2-3
coherence-ab-0-2-3 = H.common-set complement complement _ _ _ _
bind-bc-0-2-3 : F.route-bc-0-2-3 ≡ H.family base complement F.edge-2-3 true
bind-bc-0-2-3 = refl
side-bc-0-2-3 : side-map (fst F.edge-2-3) true ≡ false
side-bc-0-2-3 = refl
route-bc-0-2-3 : K.vertex-move base complement F.route-bc-0-2-3 ≡ F.route-bc-1-3-2
route-bc-0-2-3 = refl
natural-bc-0-2-3 : K.vertex-move base complement F.route-bc-0-2-3 ≡ F.route-bc-1-3-2
natural-bc-0-2-3 = H.covariance base complement F.edge-2-3 true
coherence-bc-0-2-3 : route-bc-0-2-3 ≡ natural-bc-0-2-3
coherence-bc-0-2-3 = H.common-set complement base _ _ _ _
bind-ac-0-2-3 : F.route-ac-0-2-3 ≡ H.family base complement F.edge-0-3 false
bind-ac-0-2-3 = refl
side-ac-0-2-3 : side-map (fst F.edge-0-3) false ≡ false
side-ac-0-2-3 = refl
route-ac-0-2-3 : K.vertex-move base complement F.route-ac-0-2-3 ≡ F.route-ac-1-3-2
route-ac-0-2-3 = refl
natural-ac-0-2-3 : K.vertex-move base complement F.route-ac-0-2-3 ≡ F.route-ac-1-3-2
natural-ac-0-2-3 = H.covariance base complement F.edge-0-3 false
coherence-ac-0-2-3 : route-ac-0-2-3 ≡ natural-ac-0-2-3
coherence-ac-0-2-3 = H.common-set complement base _ _ _ _
moved-ab-0-2-3 : E.A.V.InputIndex
moved-ab-0-2-3 = (C.q7 , (c0 , M.move-0-1 (snd (snd F.route-ab-0-2-3))))
moved-bc-0-2-3 : E.A.V.InputIndex
moved-bc-0-2-3 = (C.q7 , (c0 , M.move-0-1 (fst (snd F.route-bc-0-2-3))))
target-ab-0-2-3 : E.A.V.InputIndex
target-ab-0-2-3 = (C.q7 , (fst F.route-ab-1-3-2 , snd (snd F.route-ab-1-3-2)))
target-bc-0-2-3 : E.A.V.InputIndex
target-bc-0-2-3 = (C.q7 , (fst F.route-bc-1-3-2 , fst (snd F.route-bc-1-3-2)))
middle-0-2-3 : moved-ab-0-2-3 ≡ moved-bc-0-2-3
middle-0-2-3 = refl
middle-ab-0-2-3 : moved-ab-0-2-3 ≡ target-ab-0-2-3
middle-ab-0-2-3 = refl
middle-bc-0-2-3 : moved-bc-0-2-3 ≡ target-bc-0-2-3
middle-bc-0-2-3 = refl
target-native-seam-0-2-3 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q7 F.route-ab-1-3-2 , E.A.V.selected-proof C.q7 C.q7 F.route-ab-1-3-2) (lift F.route-ab-1-3-2)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-bc-1-3-2 , E.A.V.selected-proof C.q7 C.q0 F.route-bc-1-3-2) (lift F.route-bc-1-3-2)) (lift E.A.V.source-leg)
target-native-seam-0-2-3 = F.middle-1-3-2
triple-0-3-1 : T.vertex-triple base complement complement F.triple-0-3-1 ≡ F.triple-1-2-0
triple-0-3-1 = refl
bind-ab-0-3-1 : F.route-ab-0-3-1 ≡ H.family base complement F.edge-0-3 true
bind-ab-0-3-1 = refl
side-ab-0-3-1 : side-map (fst F.edge-0-3) true ≡ true
side-ab-0-3-1 = refl
route-ab-0-3-1 : K.vertex-move base complement F.route-ab-0-3-1 ≡ F.route-ab-1-2-0
route-ab-0-3-1 = refl
natural-ab-0-3-1 : K.vertex-move base complement F.route-ab-0-3-1 ≡ F.route-ab-1-2-0
natural-ab-0-3-1 = H.covariance base complement F.edge-0-3 true
coherence-ab-0-3-1 : route-ab-0-3-1 ≡ natural-ab-0-3-1
coherence-ab-0-3-1 = H.common-set complement base _ _ _ _
bind-bc-0-3-1 : F.route-bc-0-3-1 ≡ H.family complement complement F.edge-3-1 true
bind-bc-0-3-1 = refl
side-bc-0-3-1 : side-map (fst F.edge-3-1) true ≡ true
side-bc-0-3-1 = refl
route-bc-0-3-1 : K.vertex-move complement complement F.route-bc-0-3-1 ≡ F.route-bc-1-2-0
route-bc-0-3-1 = refl
natural-bc-0-3-1 : K.vertex-move complement complement F.route-bc-0-3-1 ≡ F.route-bc-1-2-0
natural-bc-0-3-1 = H.covariance complement complement F.edge-3-1 true
coherence-bc-0-3-1 : route-bc-0-3-1 ≡ natural-bc-0-3-1
coherence-bc-0-3-1 = H.common-set base base _ _ _ _
bind-ac-0-3-1 : F.route-ac-0-3-1 ≡ H.family base complement F.edge-0-1 false
bind-ac-0-3-1 = refl
side-ac-0-3-1 : side-map (fst F.edge-0-1) false ≡ true
side-ac-0-3-1 = refl
route-ac-0-3-1 : K.vertex-move base complement F.route-ac-0-3-1 ≡ F.route-ac-1-2-0
route-ac-0-3-1 = refl
natural-ac-0-3-1 : K.vertex-move base complement F.route-ac-0-3-1 ≡ F.route-ac-1-2-0
natural-ac-0-3-1 = H.covariance base complement F.edge-0-1 false
coherence-ac-0-3-1 : route-ac-0-3-1 ≡ natural-ac-0-3-1
coherence-ac-0-3-1 = H.common-set complement base _ _ _ _
moved-ab-0-3-1 : E.A.V.InputIndex
moved-ab-0-3-1 = (C.q0 , (m1 , M.move-7-2 (snd (snd F.route-ab-0-3-1))))
moved-bc-0-3-1 : E.A.V.InputIndex
moved-bc-0-3-1 = (C.q0 , (m1 , M.move-7-2 (fst (snd F.route-bc-0-3-1))))
target-ab-0-3-1 : E.A.V.InputIndex
target-ab-0-3-1 = (C.q0 , (fst F.route-ab-1-2-0 , snd (snd F.route-ab-1-2-0)))
target-bc-0-3-1 : E.A.V.InputIndex
target-bc-0-3-1 = (C.q0 , (fst F.route-bc-1-2-0 , fst (snd F.route-bc-1-2-0)))
middle-0-3-1 : moved-ab-0-3-1 ≡ moved-bc-0-3-1
middle-0-3-1 = refl
middle-ab-0-3-1 : moved-ab-0-3-1 ≡ target-ab-0-3-1
middle-ab-0-3-1 = refl
middle-bc-0-3-1 : moved-bc-0-3-1 ≡ target-bc-0-3-1
middle-bc-0-3-1 = refl
target-native-seam-0-3-1 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-ab-1-2-0 , E.A.V.selected-proof C.q7 C.q0 F.route-ab-1-2-0) (lift F.route-ab-1-2-0)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q0 F.route-bc-1-2-0 , E.A.V.selected-proof C.q0 C.q0 F.route-bc-1-2-0) (lift F.route-bc-1-2-0)) (lift E.A.V.source-leg)
target-native-seam-0-3-1 = F.middle-1-2-0
triple-0-3-2 : T.vertex-triple base complement base F.triple-0-3-2 ≡ F.triple-1-2-3
triple-0-3-2 = refl
bind-ab-0-3-2 : F.route-ab-0-3-2 ≡ H.family base complement F.edge-0-3 false
bind-ab-0-3-2 = refl
side-ab-0-3-2 : side-map (fst F.edge-0-3) false ≡ false
side-ab-0-3-2 = refl
route-ab-0-3-2 : K.vertex-move base complement F.route-ab-0-3-2 ≡ F.route-ab-1-2-3
route-ab-0-3-2 = refl
natural-ab-0-3-2 : K.vertex-move base complement F.route-ab-0-3-2 ≡ F.route-ab-1-2-3
natural-ab-0-3-2 = H.covariance base complement F.edge-0-3 false
coherence-ab-0-3-2 : route-ab-0-3-2 ≡ natural-ab-0-3-2
coherence-ab-0-3-2 = H.common-set complement base _ _ _ _
bind-bc-0-3-2 : F.route-bc-0-3-2 ≡ H.family complement base F.edge-3-2 true
bind-bc-0-3-2 = refl
side-bc-0-3-2 : side-map (fst F.edge-3-2) true ≡ false
side-bc-0-3-2 = refl
route-bc-0-3-2 : K.vertex-move complement base F.route-bc-0-3-2 ≡ F.route-bc-1-2-3
route-bc-0-3-2 = refl
natural-bc-0-3-2 : K.vertex-move complement base F.route-bc-0-3-2 ≡ F.route-bc-1-2-3
natural-bc-0-3-2 = H.covariance complement base F.edge-3-2 true
coherence-bc-0-3-2 : route-bc-0-3-2 ≡ natural-bc-0-3-2
coherence-bc-0-3-2 = H.common-set base complement _ _ _ _
bind-ac-0-3-2 : F.route-ac-0-3-2 ≡ H.family base base F.edge-0-2 false
bind-ac-0-3-2 = refl
side-ac-0-3-2 : side-map (fst F.edge-0-2) false ≡ false
side-ac-0-3-2 = refl
route-ac-0-3-2 : K.vertex-move base base F.route-ac-0-3-2 ≡ F.route-ac-1-2-3
route-ac-0-3-2 = refl
natural-ac-0-3-2 : K.vertex-move base base F.route-ac-0-3-2 ≡ F.route-ac-1-2-3
natural-ac-0-3-2 = H.covariance base base F.edge-0-2 false
coherence-ac-0-3-2 : route-ac-0-3-2 ≡ natural-ac-0-3-2
coherence-ac-0-3-2 = H.common-set complement complement _ _ _ _
moved-ab-0-3-2 : E.A.V.InputIndex
moved-ab-0-3-2 = (C.q0 , (c0 , M.move-7-1 (snd (snd F.route-ab-0-3-2))))
moved-bc-0-3-2 : E.A.V.InputIndex
moved-bc-0-3-2 = (C.q0 , (c0 , M.move-7-1 (fst (snd F.route-bc-0-3-2))))
target-ab-0-3-2 : E.A.V.InputIndex
target-ab-0-3-2 = (C.q0 , (fst F.route-ab-1-2-3 , snd (snd F.route-ab-1-2-3)))
target-bc-0-3-2 : E.A.V.InputIndex
target-bc-0-3-2 = (C.q0 , (fst F.route-bc-1-2-3 , fst (snd F.route-bc-1-2-3)))
middle-0-3-2 : moved-ab-0-3-2 ≡ moved-bc-0-3-2
middle-0-3-2 = refl
middle-ab-0-3-2 : moved-ab-0-3-2 ≡ target-ab-0-3-2
middle-ab-0-3-2 = refl
middle-bc-0-3-2 : moved-bc-0-3-2 ≡ target-bc-0-3-2
middle-bc-0-3-2 = refl
target-native-seam-0-3-2 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-ab-1-2-3 , E.A.V.selected-proof C.q7 C.q0 F.route-ab-1-2-3) (lift F.route-ab-1-2-3)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-bc-1-2-3 , E.A.V.selected-proof C.q0 C.q7 F.route-bc-1-2-3) (lift F.route-bc-1-2-3)) (lift E.A.V.source-leg)
target-native-seam-0-3-2 = F.middle-1-2-3
triple-1-0-2 : T.vertex-triple complement base base F.triple-1-0-2 ≡ F.triple-0-1-3
triple-1-0-2 = refl
bind-ab-1-0-2 : F.route-ab-1-0-2 ≡ H.family complement base F.edge-1-0 true
bind-ab-1-0-2 = refl
side-ab-1-0-2 : side-map (fst F.edge-1-0) true ≡ false
side-ab-1-0-2 = refl
route-ab-1-0-2 : K.vertex-move complement base F.route-ab-1-0-2 ≡ F.route-ab-0-1-3
route-ab-1-0-2 = refl
natural-ab-1-0-2 : K.vertex-move complement base F.route-ab-1-0-2 ≡ F.route-ab-0-1-3
natural-ab-1-0-2 = H.covariance complement base F.edge-1-0 true
coherence-ab-1-0-2 : route-ab-1-0-2 ≡ natural-ab-1-0-2
coherence-ab-1-0-2 = H.common-set base complement _ _ _ _
bind-bc-1-0-2 : F.route-bc-1-0-2 ≡ H.family base base F.edge-0-2 true
bind-bc-1-0-2 = refl
side-bc-1-0-2 : side-map (fst F.edge-0-2) true ≡ true
side-bc-1-0-2 = refl
route-bc-1-0-2 : K.vertex-move base base F.route-bc-1-0-2 ≡ F.route-bc-0-1-3
route-bc-1-0-2 = refl
natural-bc-1-0-2 : K.vertex-move base base F.route-bc-1-0-2 ≡ F.route-bc-0-1-3
natural-bc-1-0-2 = H.covariance base base F.edge-0-2 true
coherence-bc-1-0-2 : route-bc-1-0-2 ≡ natural-bc-1-0-2
coherence-bc-1-0-2 = H.common-set complement complement _ _ _ _
bind-ac-1-0-2 : F.route-ac-1-0-2 ≡ H.family complement base F.edge-1-2 true
bind-ac-1-0-2 = refl
side-ac-1-0-2 : side-map (fst F.edge-1-2) true ≡ true
side-ac-1-0-2 = refl
route-ac-1-0-2 : K.vertex-move complement base F.route-ac-1-0-2 ≡ F.route-ac-0-1-3
route-ac-1-0-2 = refl
natural-ac-1-0-2 : K.vertex-move complement base F.route-ac-1-0-2 ≡ F.route-ac-0-1-3
natural-ac-1-0-2 = H.covariance complement base F.edge-1-2 true
coherence-ac-1-0-2 : route-ac-1-0-2 ≡ natural-ac-1-0-2
coherence-ac-1-0-2 = H.common-set base complement _ _ _ _
moved-ab-1-0-2 : E.A.V.InputIndex
moved-ab-1-0-2 = (C.q7 , (c1 , M.move-0-3 (snd (snd F.route-ab-1-0-2))))
moved-bc-1-0-2 : E.A.V.InputIndex
moved-bc-1-0-2 = (C.q7 , (c1 , M.move-0-3 (fst (snd F.route-bc-1-0-2))))
target-ab-1-0-2 : E.A.V.InputIndex
target-ab-1-0-2 = (C.q7 , (fst F.route-ab-0-1-3 , snd (snd F.route-ab-0-1-3)))
target-bc-1-0-2 : E.A.V.InputIndex
target-bc-1-0-2 = (C.q7 , (fst F.route-bc-0-1-3 , fst (snd F.route-bc-0-1-3)))
middle-1-0-2 : moved-ab-1-0-2 ≡ moved-bc-1-0-2
middle-1-0-2 = refl
middle-ab-1-0-2 : moved-ab-1-0-2 ≡ target-ab-1-0-2
middle-ab-1-0-2 = refl
middle-bc-1-0-2 : moved-bc-1-0-2 ≡ target-bc-1-0-2
middle-bc-1-0-2 = refl
target-native-seam-1-0-2 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-ab-0-1-3 , E.A.V.selected-proof C.q0 C.q7 F.route-ab-0-1-3) (lift F.route-ab-0-1-3)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q7 F.route-bc-0-1-3 , E.A.V.selected-proof C.q7 C.q7 F.route-bc-0-1-3) (lift F.route-bc-0-1-3)) (lift E.A.V.source-leg)
target-native-seam-1-0-2 = F.middle-0-1-3
triple-1-0-3 : T.vertex-triple complement base complement F.triple-1-0-3 ≡ F.triple-0-1-2
triple-1-0-3 = refl
bind-ab-1-0-3 : F.route-ab-1-0-3 ≡ H.family complement base F.edge-1-0 false
bind-ab-1-0-3 = refl
side-ab-1-0-3 : side-map (fst F.edge-1-0) false ≡ true
side-ab-1-0-3 = refl
route-ab-1-0-3 : K.vertex-move complement base F.route-ab-1-0-3 ≡ F.route-ab-0-1-2
route-ab-1-0-3 = refl
natural-ab-1-0-3 : K.vertex-move complement base F.route-ab-1-0-3 ≡ F.route-ab-0-1-2
natural-ab-1-0-3 = H.covariance complement base F.edge-1-0 false
coherence-ab-1-0-3 : route-ab-1-0-3 ≡ natural-ab-1-0-3
coherence-ab-1-0-3 = H.common-set base complement _ _ _ _
bind-bc-1-0-3 : F.route-bc-1-0-3 ≡ H.family base complement F.edge-0-3 true
bind-bc-1-0-3 = refl
side-bc-1-0-3 : side-map (fst F.edge-0-3) true ≡ true
side-bc-1-0-3 = refl
route-bc-1-0-3 : K.vertex-move base complement F.route-bc-1-0-3 ≡ F.route-bc-0-1-2
route-bc-1-0-3 = refl
natural-bc-1-0-3 : K.vertex-move base complement F.route-bc-1-0-3 ≡ F.route-bc-0-1-2
natural-bc-1-0-3 = H.covariance base complement F.edge-0-3 true
coherence-bc-1-0-3 : route-bc-1-0-3 ≡ natural-bc-1-0-3
coherence-bc-1-0-3 = H.common-set complement base _ _ _ _
bind-ac-1-0-3 : F.route-ac-1-0-3 ≡ H.family complement complement F.edge-1-3 true
bind-ac-1-0-3 = refl
side-ac-1-0-3 : side-map (fst F.edge-1-3) true ≡ true
side-ac-1-0-3 = refl
route-ac-1-0-3 : K.vertex-move complement complement F.route-ac-1-0-3 ≡ F.route-ac-0-1-2
route-ac-1-0-3 = refl
natural-ac-1-0-3 : K.vertex-move complement complement F.route-ac-1-0-3 ≡ F.route-ac-0-1-2
natural-ac-1-0-3 = H.covariance complement complement F.edge-1-3 true
coherence-ac-1-0-3 : route-ac-1-0-3 ≡ natural-ac-1-0-3
coherence-ac-1-0-3 = H.common-set base base _ _ _ _
moved-ab-1-0-3 : E.A.V.InputIndex
moved-ab-1-0-3 = (C.q7 , (m1 , M.move-0-2 (snd (snd F.route-ab-1-0-3))))
moved-bc-1-0-3 : E.A.V.InputIndex
moved-bc-1-0-3 = (C.q7 , (m1 , M.move-0-2 (fst (snd F.route-bc-1-0-3))))
target-ab-1-0-3 : E.A.V.InputIndex
target-ab-1-0-3 = (C.q7 , (fst F.route-ab-0-1-2 , snd (snd F.route-ab-0-1-2)))
target-bc-1-0-3 : E.A.V.InputIndex
target-bc-1-0-3 = (C.q7 , (fst F.route-bc-0-1-2 , fst (snd F.route-bc-0-1-2)))
middle-1-0-3 : moved-ab-1-0-3 ≡ moved-bc-1-0-3
middle-1-0-3 = refl
middle-ab-1-0-3 : moved-ab-1-0-3 ≡ target-ab-1-0-3
middle-ab-1-0-3 = refl
middle-bc-1-0-3 : moved-bc-1-0-3 ≡ target-bc-1-0-3
middle-bc-1-0-3 = refl
target-native-seam-1-0-3 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-ab-0-1-2 , E.A.V.selected-proof C.q0 C.q7 F.route-ab-0-1-2) (lift F.route-ab-0-1-2)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-bc-0-1-2 , E.A.V.selected-proof C.q7 C.q0 F.route-bc-0-1-2) (lift F.route-bc-0-1-2)) (lift E.A.V.source-leg)
target-native-seam-1-0-3 = F.middle-0-1-2
triple-1-2-0 : T.vertex-triple complement base base F.triple-1-2-0 ≡ F.triple-0-3-1
triple-1-2-0 = refl
bind-ab-1-2-0 : F.route-ab-1-2-0 ≡ H.family complement base F.edge-1-2 true
bind-ab-1-2-0 = refl
side-ab-1-2-0 : side-map (fst F.edge-1-2) true ≡ true
side-ab-1-2-0 = refl
route-ab-1-2-0 : K.vertex-move complement base F.route-ab-1-2-0 ≡ F.route-ab-0-3-1
route-ab-1-2-0 = refl
natural-ab-1-2-0 : K.vertex-move complement base F.route-ab-1-2-0 ≡ F.route-ab-0-3-1
natural-ab-1-2-0 = H.covariance complement base F.edge-1-2 true
coherence-ab-1-2-0 : route-ab-1-2-0 ≡ natural-ab-1-2-0
coherence-ab-1-2-0 = H.common-set base complement _ _ _ _
bind-bc-1-2-0 : F.route-bc-1-2-0 ≡ H.family base base F.edge-2-0 true
bind-bc-1-2-0 = refl
side-bc-1-2-0 : side-map (fst F.edge-2-0) true ≡ true
side-bc-1-2-0 = refl
route-bc-1-2-0 : K.vertex-move base base F.route-bc-1-2-0 ≡ F.route-bc-0-3-1
route-bc-1-2-0 = refl
natural-bc-1-2-0 : K.vertex-move base base F.route-bc-1-2-0 ≡ F.route-bc-0-3-1
natural-bc-1-2-0 = H.covariance base base F.edge-2-0 true
coherence-bc-1-2-0 : route-bc-1-2-0 ≡ natural-bc-1-2-0
coherence-bc-1-2-0 = H.common-set complement complement _ _ _ _
bind-ac-1-2-0 : F.route-ac-1-2-0 ≡ H.family complement base F.edge-1-0 true
bind-ac-1-2-0 = refl
side-ac-1-2-0 : side-map (fst F.edge-1-0) true ≡ false
side-ac-1-2-0 = refl
route-ac-1-2-0 : K.vertex-move complement base F.route-ac-1-2-0 ≡ F.route-ac-0-3-1
route-ac-1-2-0 = refl
natural-ac-1-2-0 : K.vertex-move complement base F.route-ac-1-2-0 ≡ F.route-ac-0-3-1
natural-ac-1-2-0 = H.covariance complement base F.edge-1-0 true
coherence-ac-1-2-0 : route-ac-1-2-0 ≡ natural-ac-1-2-0
coherence-ac-1-2-0 = H.common-set base complement _ _ _ _
moved-ab-1-2-0 : E.A.V.InputIndex
moved-ab-1-2-0 = (C.q7 , (c1 , M.move-0-3 (snd (snd F.route-ab-1-2-0))))
moved-bc-1-2-0 : E.A.V.InputIndex
moved-bc-1-2-0 = (C.q7 , (c1 , M.move-0-3 (fst (snd F.route-bc-1-2-0))))
target-ab-1-2-0 : E.A.V.InputIndex
target-ab-1-2-0 = (C.q7 , (fst F.route-ab-0-3-1 , snd (snd F.route-ab-0-3-1)))
target-bc-1-2-0 : E.A.V.InputIndex
target-bc-1-2-0 = (C.q7 , (fst F.route-bc-0-3-1 , fst (snd F.route-bc-0-3-1)))
middle-1-2-0 : moved-ab-1-2-0 ≡ moved-bc-1-2-0
middle-1-2-0 = refl
middle-ab-1-2-0 : moved-ab-1-2-0 ≡ target-ab-1-2-0
middle-ab-1-2-0 = refl
middle-bc-1-2-0 : moved-bc-1-2-0 ≡ target-bc-1-2-0
middle-bc-1-2-0 = refl
target-native-seam-1-2-0 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-ab-0-3-1 , E.A.V.selected-proof C.q0 C.q7 F.route-ab-0-3-1) (lift F.route-ab-0-3-1)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q7 F.route-bc-0-3-1 , E.A.V.selected-proof C.q7 C.q7 F.route-bc-0-3-1) (lift F.route-bc-0-3-1)) (lift E.A.V.source-leg)
target-native-seam-1-2-0 = F.middle-0-3-1
triple-1-2-3 : T.vertex-triple complement base complement F.triple-1-2-3 ≡ F.triple-0-3-2
triple-1-2-3 = refl
bind-ab-1-2-3 : F.route-ab-1-2-3 ≡ H.family complement base F.edge-1-2 false
bind-ab-1-2-3 = refl
side-ab-1-2-3 : side-map (fst F.edge-1-2) false ≡ false
side-ab-1-2-3 = refl
route-ab-1-2-3 : K.vertex-move complement base F.route-ab-1-2-3 ≡ F.route-ab-0-3-2
route-ab-1-2-3 = refl
natural-ab-1-2-3 : K.vertex-move complement base F.route-ab-1-2-3 ≡ F.route-ab-0-3-2
natural-ab-1-2-3 = H.covariance complement base F.edge-1-2 false
coherence-ab-1-2-3 : route-ab-1-2-3 ≡ natural-ab-1-2-3
coherence-ab-1-2-3 = H.common-set base complement _ _ _ _
bind-bc-1-2-3 : F.route-bc-1-2-3 ≡ H.family base complement F.edge-2-3 false
bind-bc-1-2-3 = refl
side-bc-1-2-3 : side-map (fst F.edge-2-3) false ≡ true
side-bc-1-2-3 = refl
route-bc-1-2-3 : K.vertex-move base complement F.route-bc-1-2-3 ≡ F.route-bc-0-3-2
route-bc-1-2-3 = refl
natural-bc-1-2-3 : K.vertex-move base complement F.route-bc-1-2-3 ≡ F.route-bc-0-3-2
natural-bc-1-2-3 = H.covariance base complement F.edge-2-3 false
coherence-bc-1-2-3 : route-bc-1-2-3 ≡ natural-bc-1-2-3
coherence-bc-1-2-3 = H.common-set complement base _ _ _ _
bind-ac-1-2-3 : F.route-ac-1-2-3 ≡ H.family complement complement F.edge-1-3 false
bind-ac-1-2-3 = refl
side-ac-1-2-3 : side-map (fst F.edge-1-3) false ≡ false
side-ac-1-2-3 = refl
route-ac-1-2-3 : K.vertex-move complement complement F.route-ac-1-2-3 ≡ F.route-ac-0-3-2
route-ac-1-2-3 = refl
natural-ac-1-2-3 : K.vertex-move complement complement F.route-ac-1-2-3 ≡ F.route-ac-0-3-2
natural-ac-1-2-3 = H.covariance complement complement F.edge-1-3 false
coherence-ac-1-2-3 : route-ac-1-2-3 ≡ natural-ac-1-2-3
coherence-ac-1-2-3 = H.common-set base base _ _ _ _
moved-ab-1-2-3 : E.A.V.InputIndex
moved-ab-1-2-3 = (C.q7 , (m0 , M.move-0-0 (snd (snd F.route-ab-1-2-3))))
moved-bc-1-2-3 : E.A.V.InputIndex
moved-bc-1-2-3 = (C.q7 , (m0 , M.move-0-0 (fst (snd F.route-bc-1-2-3))))
target-ab-1-2-3 : E.A.V.InputIndex
target-ab-1-2-3 = (C.q7 , (fst F.route-ab-0-3-2 , snd (snd F.route-ab-0-3-2)))
target-bc-1-2-3 : E.A.V.InputIndex
target-bc-1-2-3 = (C.q7 , (fst F.route-bc-0-3-2 , fst (snd F.route-bc-0-3-2)))
middle-1-2-3 : moved-ab-1-2-3 ≡ moved-bc-1-2-3
middle-1-2-3 = refl
middle-ab-1-2-3 : moved-ab-1-2-3 ≡ target-ab-1-2-3
middle-ab-1-2-3 = refl
middle-bc-1-2-3 : moved-bc-1-2-3 ≡ target-bc-1-2-3
middle-bc-1-2-3 = refl
target-native-seam-1-2-3 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-ab-0-3-2 , E.A.V.selected-proof C.q0 C.q7 F.route-ab-0-3-2) (lift F.route-ab-0-3-2)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-bc-0-3-2 , E.A.V.selected-proof C.q7 C.q0 F.route-bc-0-3-2) (lift F.route-bc-0-3-2)) (lift E.A.V.source-leg)
target-native-seam-1-2-3 = F.middle-0-3-2
triple-1-3-0 : T.vertex-triple complement complement base F.triple-1-3-0 ≡ F.triple-0-2-1
triple-1-3-0 = refl
bind-ab-1-3-0 : F.route-ab-1-3-0 ≡ H.family complement complement F.edge-1-3 true
bind-ab-1-3-0 = refl
side-ab-1-3-0 : side-map (fst F.edge-1-3) true ≡ true
side-ab-1-3-0 = refl
route-ab-1-3-0 : K.vertex-move complement complement F.route-ab-1-3-0 ≡ F.route-ab-0-2-1
route-ab-1-3-0 = refl
natural-ab-1-3-0 : K.vertex-move complement complement F.route-ab-1-3-0 ≡ F.route-ab-0-2-1
natural-ab-1-3-0 = H.covariance complement complement F.edge-1-3 true
coherence-ab-1-3-0 : route-ab-1-3-0 ≡ natural-ab-1-3-0
coherence-ab-1-3-0 = H.common-set base base _ _ _ _
bind-bc-1-3-0 : F.route-bc-1-3-0 ≡ H.family complement base F.edge-3-0 true
bind-bc-1-3-0 = refl
side-bc-1-3-0 : side-map (fst F.edge-3-0) true ≡ true
side-bc-1-3-0 = refl
route-bc-1-3-0 : K.vertex-move complement base F.route-bc-1-3-0 ≡ F.route-bc-0-2-1
route-bc-1-3-0 = refl
natural-bc-1-3-0 : K.vertex-move complement base F.route-bc-1-3-0 ≡ F.route-bc-0-2-1
natural-bc-1-3-0 = H.covariance complement base F.edge-3-0 true
coherence-bc-1-3-0 : route-bc-1-3-0 ≡ natural-bc-1-3-0
coherence-bc-1-3-0 = H.common-set base complement _ _ _ _
bind-ac-1-3-0 : F.route-ac-1-3-0 ≡ H.family complement base F.edge-1-0 false
bind-ac-1-3-0 = refl
side-ac-1-3-0 : side-map (fst F.edge-1-0) false ≡ true
side-ac-1-3-0 = refl
route-ac-1-3-0 : K.vertex-move complement base F.route-ac-1-3-0 ≡ F.route-ac-0-2-1
route-ac-1-3-0 = refl
natural-ac-1-3-0 : K.vertex-move complement base F.route-ac-1-3-0 ≡ F.route-ac-0-2-1
natural-ac-1-3-0 = H.covariance complement base F.edge-1-0 false
coherence-ac-1-3-0 : route-ac-1-3-0 ≡ natural-ac-1-3-0
coherence-ac-1-3-0 = H.common-set base complement _ _ _ _
moved-ab-1-3-0 : E.A.V.InputIndex
moved-ab-1-3-0 = (C.q0 , (m1 , M.move-7-2 (snd (snd F.route-ab-1-3-0))))
moved-bc-1-3-0 : E.A.V.InputIndex
moved-bc-1-3-0 = (C.q0 , (m1 , M.move-7-2 (fst (snd F.route-bc-1-3-0))))
target-ab-1-3-0 : E.A.V.InputIndex
target-ab-1-3-0 = (C.q0 , (fst F.route-ab-0-2-1 , snd (snd F.route-ab-0-2-1)))
target-bc-1-3-0 : E.A.V.InputIndex
target-bc-1-3-0 = (C.q0 , (fst F.route-bc-0-2-1 , fst (snd F.route-bc-0-2-1)))
middle-1-3-0 : moved-ab-1-3-0 ≡ moved-bc-1-3-0
middle-1-3-0 = refl
middle-ab-1-3-0 : moved-ab-1-3-0 ≡ target-ab-1-3-0
middle-ab-1-3-0 = refl
middle-bc-1-3-0 : moved-bc-1-3-0 ≡ target-bc-1-3-0
middle-bc-1-3-0 = refl
target-native-seam-1-3-0 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q0 F.route-ab-0-2-1 , E.A.V.selected-proof C.q0 C.q0 F.route-ab-0-2-1) (lift F.route-ab-0-2-1)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-bc-0-2-1 , E.A.V.selected-proof C.q0 C.q7 F.route-bc-0-2-1) (lift F.route-bc-0-2-1)) (lift E.A.V.source-leg)
target-native-seam-1-3-0 = F.middle-0-2-1
triple-1-3-2 : T.vertex-triple complement complement base F.triple-1-3-2 ≡ F.triple-0-2-3
triple-1-3-2 = refl
bind-ab-1-3-2 : F.route-ab-1-3-2 ≡ H.family complement complement F.edge-1-3 false
bind-ab-1-3-2 = refl
side-ab-1-3-2 : side-map (fst F.edge-1-3) false ≡ false
side-ab-1-3-2 = refl
route-ab-1-3-2 : K.vertex-move complement complement F.route-ab-1-3-2 ≡ F.route-ab-0-2-3
route-ab-1-3-2 = refl
natural-ab-1-3-2 : K.vertex-move complement complement F.route-ab-1-3-2 ≡ F.route-ab-0-2-3
natural-ab-1-3-2 = H.covariance complement complement F.edge-1-3 false
coherence-ab-1-3-2 : route-ab-1-3-2 ≡ natural-ab-1-3-2
coherence-ab-1-3-2 = H.common-set base base _ _ _ _
bind-bc-1-3-2 : F.route-bc-1-3-2 ≡ H.family complement base F.edge-3-2 false
bind-bc-1-3-2 = refl
side-bc-1-3-2 : side-map (fst F.edge-3-2) false ≡ true
side-bc-1-3-2 = refl
route-bc-1-3-2 : K.vertex-move complement base F.route-bc-1-3-2 ≡ F.route-bc-0-2-3
route-bc-1-3-2 = refl
natural-bc-1-3-2 : K.vertex-move complement base F.route-bc-1-3-2 ≡ F.route-bc-0-2-3
natural-bc-1-3-2 = H.covariance complement base F.edge-3-2 false
coherence-bc-1-3-2 : route-bc-1-3-2 ≡ natural-bc-1-3-2
coherence-bc-1-3-2 = H.common-set base complement _ _ _ _
bind-ac-1-3-2 : F.route-ac-1-3-2 ≡ H.family complement base F.edge-1-2 false
bind-ac-1-3-2 = refl
side-ac-1-3-2 : side-map (fst F.edge-1-2) false ≡ false
side-ac-1-3-2 = refl
route-ac-1-3-2 : K.vertex-move complement base F.route-ac-1-3-2 ≡ F.route-ac-0-2-3
route-ac-1-3-2 = refl
natural-ac-1-3-2 : K.vertex-move complement base F.route-ac-1-3-2 ≡ F.route-ac-0-2-3
natural-ac-1-3-2 = H.covariance complement base F.edge-1-2 false
coherence-ac-1-3-2 : route-ac-1-3-2 ≡ natural-ac-1-3-2
coherence-ac-1-3-2 = H.common-set base complement _ _ _ _
moved-ab-1-3-2 : E.A.V.InputIndex
moved-ab-1-3-2 = (C.q0 , (m0 , M.move-7-0 (snd (snd F.route-ab-1-3-2))))
moved-bc-1-3-2 : E.A.V.InputIndex
moved-bc-1-3-2 = (C.q0 , (m0 , M.move-7-0 (fst (snd F.route-bc-1-3-2))))
target-ab-1-3-2 : E.A.V.InputIndex
target-ab-1-3-2 = (C.q0 , (fst F.route-ab-0-2-3 , snd (snd F.route-ab-0-2-3)))
target-bc-1-3-2 : E.A.V.InputIndex
target-bc-1-3-2 = (C.q0 , (fst F.route-bc-0-2-3 , fst (snd F.route-bc-0-2-3)))
middle-1-3-2 : moved-ab-1-3-2 ≡ moved-bc-1-3-2
middle-1-3-2 = refl
middle-ab-1-3-2 : moved-ab-1-3-2 ≡ target-ab-1-3-2
middle-ab-1-3-2 = refl
middle-bc-1-3-2 : moved-bc-1-3-2 ≡ target-bc-1-3-2
middle-bc-1-3-2 = refl
target-native-seam-1-3-2 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q0 F.route-ab-0-2-3 , E.A.V.selected-proof C.q0 C.q0 F.route-ab-0-2-3) (lift F.route-ab-0-2-3)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-bc-0-2-3 , E.A.V.selected-proof C.q0 C.q7 F.route-bc-0-2-3) (lift F.route-bc-0-2-3)) (lift E.A.V.source-leg)
target-native-seam-1-3-2 = F.middle-0-2-3
triple-2-0-1 : T.vertex-triple base base complement F.triple-2-0-1 ≡ F.triple-3-1-0
triple-2-0-1 = refl
bind-ab-2-0-1 : F.route-ab-2-0-1 ≡ H.family base base F.edge-2-0 true
bind-ab-2-0-1 = refl
side-ab-2-0-1 : side-map (fst F.edge-2-0) true ≡ true
side-ab-2-0-1 = refl
route-ab-2-0-1 : K.vertex-move base base F.route-ab-2-0-1 ≡ F.route-ab-3-1-0
route-ab-2-0-1 = refl
natural-ab-2-0-1 : K.vertex-move base base F.route-ab-2-0-1 ≡ F.route-ab-3-1-0
natural-ab-2-0-1 = H.covariance base base F.edge-2-0 true
coherence-ab-2-0-1 : route-ab-2-0-1 ≡ natural-ab-2-0-1
coherence-ab-2-0-1 = H.common-set complement complement _ _ _ _
bind-bc-2-0-1 : F.route-bc-2-0-1 ≡ H.family base complement F.edge-0-1 true
bind-bc-2-0-1 = refl
side-bc-2-0-1 : side-map (fst F.edge-0-1) true ≡ false
side-bc-2-0-1 = refl
route-bc-2-0-1 : K.vertex-move base complement F.route-bc-2-0-1 ≡ F.route-bc-3-1-0
route-bc-2-0-1 = refl
natural-bc-2-0-1 : K.vertex-move base complement F.route-bc-2-0-1 ≡ F.route-bc-3-1-0
natural-bc-2-0-1 = H.covariance base complement F.edge-0-1 true
coherence-bc-2-0-1 : route-bc-2-0-1 ≡ natural-bc-2-0-1
coherence-bc-2-0-1 = H.common-set complement base _ _ _ _
bind-ac-2-0-1 : F.route-ac-2-0-1 ≡ H.family base complement F.edge-2-1 true
bind-ac-2-0-1 = refl
side-ac-2-0-1 : side-map (fst F.edge-2-1) true ≡ true
side-ac-2-0-1 = refl
route-ac-2-0-1 : K.vertex-move base complement F.route-ac-2-0-1 ≡ F.route-ac-3-1-0
route-ac-2-0-1 = refl
natural-ac-2-0-1 : K.vertex-move base complement F.route-ac-2-0-1 ≡ F.route-ac-3-1-0
natural-ac-2-0-1 = H.covariance base complement F.edge-2-1 true
coherence-ac-2-0-1 : route-ac-2-0-1 ≡ natural-ac-2-0-1
coherence-ac-2-0-1 = H.common-set complement base _ _ _ _
moved-ab-2-0-1 : E.A.V.InputIndex
moved-ab-2-0-1 = (C.q7 , (c1 , M.move-0-3 (snd (snd F.route-ab-2-0-1))))
moved-bc-2-0-1 : E.A.V.InputIndex
moved-bc-2-0-1 = (C.q7 , (c1 , M.move-0-3 (fst (snd F.route-bc-2-0-1))))
target-ab-2-0-1 : E.A.V.InputIndex
target-ab-2-0-1 = (C.q7 , (fst F.route-ab-3-1-0 , snd (snd F.route-ab-3-1-0)))
target-bc-2-0-1 : E.A.V.InputIndex
target-bc-2-0-1 = (C.q7 , (fst F.route-bc-3-1-0 , fst (snd F.route-bc-3-1-0)))
middle-2-0-1 : moved-ab-2-0-1 ≡ moved-bc-2-0-1
middle-2-0-1 = refl
middle-ab-2-0-1 : moved-ab-2-0-1 ≡ target-ab-2-0-1
middle-ab-2-0-1 = refl
middle-bc-2-0-1 : moved-bc-2-0-1 ≡ target-bc-2-0-1
middle-bc-2-0-1 = refl
target-native-seam-2-0-1 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q7 F.route-ab-3-1-0 , E.A.V.selected-proof C.q7 C.q7 F.route-ab-3-1-0) (lift F.route-ab-3-1-0)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-bc-3-1-0 , E.A.V.selected-proof C.q7 C.q0 F.route-bc-3-1-0) (lift F.route-bc-3-1-0)) (lift E.A.V.source-leg)
target-native-seam-2-0-1 = F.middle-3-1-0
triple-2-0-3 : T.vertex-triple base base complement F.triple-2-0-3 ≡ F.triple-3-1-2
triple-2-0-3 = refl
bind-ab-2-0-3 : F.route-ab-2-0-3 ≡ H.family base base F.edge-2-0 false
bind-ab-2-0-3 = refl
side-ab-2-0-3 : side-map (fst F.edge-2-0) false ≡ false
side-ab-2-0-3 = refl
route-ab-2-0-3 : K.vertex-move base base F.route-ab-2-0-3 ≡ F.route-ab-3-1-2
route-ab-2-0-3 = refl
natural-ab-2-0-3 : K.vertex-move base base F.route-ab-2-0-3 ≡ F.route-ab-3-1-2
natural-ab-2-0-3 = H.covariance base base F.edge-2-0 false
coherence-ab-2-0-3 : route-ab-2-0-3 ≡ natural-ab-2-0-3
coherence-ab-2-0-3 = H.common-set complement complement _ _ _ _
bind-bc-2-0-3 : F.route-bc-2-0-3 ≡ H.family base complement F.edge-0-3 false
bind-bc-2-0-3 = refl
side-bc-2-0-3 : side-map (fst F.edge-0-3) false ≡ false
side-bc-2-0-3 = refl
route-bc-2-0-3 : K.vertex-move base complement F.route-bc-2-0-3 ≡ F.route-bc-3-1-2
route-bc-2-0-3 = refl
natural-bc-2-0-3 : K.vertex-move base complement F.route-bc-2-0-3 ≡ F.route-bc-3-1-2
natural-bc-2-0-3 = H.covariance base complement F.edge-0-3 false
coherence-bc-2-0-3 : route-bc-2-0-3 ≡ natural-bc-2-0-3
coherence-bc-2-0-3 = H.common-set complement base _ _ _ _
bind-ac-2-0-3 : F.route-ac-2-0-3 ≡ H.family base complement F.edge-2-3 true
bind-ac-2-0-3 = refl
side-ac-2-0-3 : side-map (fst F.edge-2-3) true ≡ false
side-ac-2-0-3 = refl
route-ac-2-0-3 : K.vertex-move base complement F.route-ac-2-0-3 ≡ F.route-ac-3-1-2
route-ac-2-0-3 = refl
natural-ac-2-0-3 : K.vertex-move base complement F.route-ac-2-0-3 ≡ F.route-ac-3-1-2
natural-ac-2-0-3 = H.covariance base complement F.edge-2-3 true
coherence-ac-2-0-3 : route-ac-2-0-3 ≡ natural-ac-2-0-3
coherence-ac-2-0-3 = H.common-set complement base _ _ _ _
moved-ab-2-0-3 : E.A.V.InputIndex
moved-ab-2-0-3 = (C.q7 , (c0 , M.move-0-1 (snd (snd F.route-ab-2-0-3))))
moved-bc-2-0-3 : E.A.V.InputIndex
moved-bc-2-0-3 = (C.q7 , (c0 , M.move-0-1 (fst (snd F.route-bc-2-0-3))))
target-ab-2-0-3 : E.A.V.InputIndex
target-ab-2-0-3 = (C.q7 , (fst F.route-ab-3-1-2 , snd (snd F.route-ab-3-1-2)))
target-bc-2-0-3 : E.A.V.InputIndex
target-bc-2-0-3 = (C.q7 , (fst F.route-bc-3-1-2 , fst (snd F.route-bc-3-1-2)))
middle-2-0-3 : moved-ab-2-0-3 ≡ moved-bc-2-0-3
middle-2-0-3 = refl
middle-ab-2-0-3 : moved-ab-2-0-3 ≡ target-ab-2-0-3
middle-ab-2-0-3 = refl
middle-bc-2-0-3 : moved-bc-2-0-3 ≡ target-bc-2-0-3
middle-bc-2-0-3 = refl
target-native-seam-2-0-3 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q7 F.route-ab-3-1-2 , E.A.V.selected-proof C.q7 C.q7 F.route-ab-3-1-2) (lift F.route-ab-3-1-2)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-bc-3-1-2 , E.A.V.selected-proof C.q7 C.q0 F.route-bc-3-1-2) (lift F.route-bc-3-1-2)) (lift E.A.V.source-leg)
target-native-seam-2-0-3 = F.middle-3-1-2
triple-2-1-0 : T.vertex-triple base complement base F.triple-2-1-0 ≡ F.triple-3-0-1
triple-2-1-0 = refl
bind-ab-2-1-0 : F.route-ab-2-1-0 ≡ H.family base complement F.edge-2-1 true
bind-ab-2-1-0 = refl
side-ab-2-1-0 : side-map (fst F.edge-2-1) true ≡ true
side-ab-2-1-0 = refl
route-ab-2-1-0 : K.vertex-move base complement F.route-ab-2-1-0 ≡ F.route-ab-3-0-1
route-ab-2-1-0 = refl
natural-ab-2-1-0 : K.vertex-move base complement F.route-ab-2-1-0 ≡ F.route-ab-3-0-1
natural-ab-2-1-0 = H.covariance base complement F.edge-2-1 true
coherence-ab-2-1-0 : route-ab-2-1-0 ≡ natural-ab-2-1-0
coherence-ab-2-1-0 = H.common-set complement base _ _ _ _
bind-bc-2-1-0 : F.route-bc-2-1-0 ≡ H.family complement base F.edge-1-0 true
bind-bc-2-1-0 = refl
side-bc-2-1-0 : side-map (fst F.edge-1-0) true ≡ false
side-bc-2-1-0 = refl
route-bc-2-1-0 : K.vertex-move complement base F.route-bc-2-1-0 ≡ F.route-bc-3-0-1
route-bc-2-1-0 = refl
natural-bc-2-1-0 : K.vertex-move complement base F.route-bc-2-1-0 ≡ F.route-bc-3-0-1
natural-bc-2-1-0 = H.covariance complement base F.edge-1-0 true
coherence-bc-2-1-0 : route-bc-2-1-0 ≡ natural-bc-2-1-0
coherence-bc-2-1-0 = H.common-set base complement _ _ _ _
bind-ac-2-1-0 : F.route-ac-2-1-0 ≡ H.family base base F.edge-2-0 true
bind-ac-2-1-0 = refl
side-ac-2-1-0 : side-map (fst F.edge-2-0) true ≡ true
side-ac-2-1-0 = refl
route-ac-2-1-0 : K.vertex-move base base F.route-ac-2-1-0 ≡ F.route-ac-3-0-1
route-ac-2-1-0 = refl
natural-ac-2-1-0 : K.vertex-move base base F.route-ac-2-1-0 ≡ F.route-ac-3-0-1
natural-ac-2-1-0 = H.covariance base base F.edge-2-0 true
coherence-ac-2-1-0 : route-ac-2-1-0 ≡ natural-ac-2-1-0
coherence-ac-2-1-0 = H.common-set complement complement _ _ _ _
moved-ab-2-1-0 : E.A.V.InputIndex
moved-ab-2-1-0 = (C.q0 , (c1 , M.move-7-3 (snd (snd F.route-ab-2-1-0))))
moved-bc-2-1-0 : E.A.V.InputIndex
moved-bc-2-1-0 = (C.q0 , (c1 , M.move-7-3 (fst (snd F.route-bc-2-1-0))))
target-ab-2-1-0 : E.A.V.InputIndex
target-ab-2-1-0 = (C.q0 , (fst F.route-ab-3-0-1 , snd (snd F.route-ab-3-0-1)))
target-bc-2-1-0 : E.A.V.InputIndex
target-bc-2-1-0 = (C.q0 , (fst F.route-bc-3-0-1 , fst (snd F.route-bc-3-0-1)))
middle-2-1-0 : moved-ab-2-1-0 ≡ moved-bc-2-1-0
middle-2-1-0 = refl
middle-ab-2-1-0 : moved-ab-2-1-0 ≡ target-ab-2-1-0
middle-ab-2-1-0 = refl
middle-bc-2-1-0 : moved-bc-2-1-0 ≡ target-bc-2-1-0
middle-bc-2-1-0 = refl
target-native-seam-2-1-0 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-ab-3-0-1 , E.A.V.selected-proof C.q7 C.q0 F.route-ab-3-0-1) (lift F.route-ab-3-0-1)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-bc-3-0-1 , E.A.V.selected-proof C.q0 C.q7 F.route-bc-3-0-1) (lift F.route-bc-3-0-1)) (lift E.A.V.source-leg)
target-native-seam-2-1-0 = F.middle-3-0-1
triple-2-1-3 : T.vertex-triple base complement complement F.triple-2-1-3 ≡ F.triple-3-0-2
triple-2-1-3 = refl
bind-ab-2-1-3 : F.route-ab-2-1-3 ≡ H.family base complement F.edge-2-1 false
bind-ab-2-1-3 = refl
side-ab-2-1-3 : side-map (fst F.edge-2-1) false ≡ false
side-ab-2-1-3 = refl
route-ab-2-1-3 : K.vertex-move base complement F.route-ab-2-1-3 ≡ F.route-ab-3-0-2
route-ab-2-1-3 = refl
natural-ab-2-1-3 : K.vertex-move base complement F.route-ab-2-1-3 ≡ F.route-ab-3-0-2
natural-ab-2-1-3 = H.covariance base complement F.edge-2-1 false
coherence-ab-2-1-3 : route-ab-2-1-3 ≡ natural-ab-2-1-3
coherence-ab-2-1-3 = H.common-set complement base _ _ _ _
bind-bc-2-1-3 : F.route-bc-2-1-3 ≡ H.family complement complement F.edge-1-3 false
bind-bc-2-1-3 = refl
side-bc-2-1-3 : side-map (fst F.edge-1-3) false ≡ false
side-bc-2-1-3 = refl
route-bc-2-1-3 : K.vertex-move complement complement F.route-bc-2-1-3 ≡ F.route-bc-3-0-2
route-bc-2-1-3 = refl
natural-bc-2-1-3 : K.vertex-move complement complement F.route-bc-2-1-3 ≡ F.route-bc-3-0-2
natural-bc-2-1-3 = H.covariance complement complement F.edge-1-3 false
coherence-bc-2-1-3 : route-bc-2-1-3 ≡ natural-bc-2-1-3
coherence-bc-2-1-3 = H.common-set base base _ _ _ _
bind-ac-2-1-3 : F.route-ac-2-1-3 ≡ H.family base complement F.edge-2-3 false
bind-ac-2-1-3 = refl
side-ac-2-1-3 : side-map (fst F.edge-2-3) false ≡ true
side-ac-2-1-3 = refl
route-ac-2-1-3 : K.vertex-move base complement F.route-ac-2-1-3 ≡ F.route-ac-3-0-2
route-ac-2-1-3 = refl
natural-ac-2-1-3 : K.vertex-move base complement F.route-ac-2-1-3 ≡ F.route-ac-3-0-2
natural-ac-2-1-3 = H.covariance base complement F.edge-2-3 false
coherence-ac-2-1-3 : route-ac-2-1-3 ≡ natural-ac-2-1-3
coherence-ac-2-1-3 = H.common-set complement base _ _ _ _
moved-ab-2-1-3 : E.A.V.InputIndex
moved-ab-2-1-3 = (C.q0 , (m0 , M.move-7-0 (snd (snd F.route-ab-2-1-3))))
moved-bc-2-1-3 : E.A.V.InputIndex
moved-bc-2-1-3 = (C.q0 , (m0 , M.move-7-0 (fst (snd F.route-bc-2-1-3))))
target-ab-2-1-3 : E.A.V.InputIndex
target-ab-2-1-3 = (C.q0 , (fst F.route-ab-3-0-2 , snd (snd F.route-ab-3-0-2)))
target-bc-2-1-3 : E.A.V.InputIndex
target-bc-2-1-3 = (C.q0 , (fst F.route-bc-3-0-2 , fst (snd F.route-bc-3-0-2)))
middle-2-1-3 : moved-ab-2-1-3 ≡ moved-bc-2-1-3
middle-2-1-3 = refl
middle-ab-2-1-3 : moved-ab-2-1-3 ≡ target-ab-2-1-3
middle-ab-2-1-3 = refl
middle-bc-2-1-3 : moved-bc-2-1-3 ≡ target-bc-2-1-3
middle-bc-2-1-3 = refl
target-native-seam-2-1-3 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-ab-3-0-2 , E.A.V.selected-proof C.q7 C.q0 F.route-ab-3-0-2) (lift F.route-ab-3-0-2)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q0 F.route-bc-3-0-2 , E.A.V.selected-proof C.q0 C.q0 F.route-bc-3-0-2) (lift F.route-bc-3-0-2)) (lift E.A.V.source-leg)
target-native-seam-2-1-3 = F.middle-3-0-2
triple-2-3-0 : T.vertex-triple base complement base F.triple-2-3-0 ≡ F.triple-3-2-1
triple-2-3-0 = refl
bind-ab-2-3-0 : F.route-ab-2-3-0 ≡ H.family base complement F.edge-2-3 true
bind-ab-2-3-0 = refl
side-ab-2-3-0 : side-map (fst F.edge-2-3) true ≡ false
side-ab-2-3-0 = refl
route-ab-2-3-0 : K.vertex-move base complement F.route-ab-2-3-0 ≡ F.route-ab-3-2-1
route-ab-2-3-0 = refl
natural-ab-2-3-0 : K.vertex-move base complement F.route-ab-2-3-0 ≡ F.route-ab-3-2-1
natural-ab-2-3-0 = H.covariance base complement F.edge-2-3 true
coherence-ab-2-3-0 : route-ab-2-3-0 ≡ natural-ab-2-3-0
coherence-ab-2-3-0 = H.common-set complement base _ _ _ _
bind-bc-2-3-0 : F.route-bc-2-3-0 ≡ H.family complement base F.edge-3-0 false
bind-bc-2-3-0 = refl
side-bc-2-3-0 : side-map (fst F.edge-3-0) false ≡ false
side-bc-2-3-0 = refl
route-bc-2-3-0 : K.vertex-move complement base F.route-bc-2-3-0 ≡ F.route-bc-3-2-1
route-bc-2-3-0 = refl
natural-bc-2-3-0 : K.vertex-move complement base F.route-bc-2-3-0 ≡ F.route-bc-3-2-1
natural-bc-2-3-0 = H.covariance complement base F.edge-3-0 false
coherence-bc-2-3-0 : route-bc-2-3-0 ≡ natural-bc-2-3-0
coherence-bc-2-3-0 = H.common-set base complement _ _ _ _
bind-ac-2-3-0 : F.route-ac-2-3-0 ≡ H.family base base F.edge-2-0 false
bind-ac-2-3-0 = refl
side-ac-2-3-0 : side-map (fst F.edge-2-0) false ≡ false
side-ac-2-3-0 = refl
route-ac-2-3-0 : K.vertex-move base base F.route-ac-2-3-0 ≡ F.route-ac-3-2-1
route-ac-2-3-0 = refl
natural-ac-2-3-0 : K.vertex-move base base F.route-ac-2-3-0 ≡ F.route-ac-3-2-1
natural-ac-2-3-0 = H.covariance base base F.edge-2-0 false
coherence-ac-2-3-0 : route-ac-2-3-0 ≡ natural-ac-2-3-0
coherence-ac-2-3-0 = H.common-set complement complement _ _ _ _
moved-ab-2-3-0 : E.A.V.InputIndex
moved-ab-2-3-0 = (C.q0 , (c0 , M.move-7-1 (snd (snd F.route-ab-2-3-0))))
moved-bc-2-3-0 : E.A.V.InputIndex
moved-bc-2-3-0 = (C.q0 , (c0 , M.move-7-1 (fst (snd F.route-bc-2-3-0))))
target-ab-2-3-0 : E.A.V.InputIndex
target-ab-2-3-0 = (C.q0 , (fst F.route-ab-3-2-1 , snd (snd F.route-ab-3-2-1)))
target-bc-2-3-0 : E.A.V.InputIndex
target-bc-2-3-0 = (C.q0 , (fst F.route-bc-3-2-1 , fst (snd F.route-bc-3-2-1)))
middle-2-3-0 : moved-ab-2-3-0 ≡ moved-bc-2-3-0
middle-2-3-0 = refl
middle-ab-2-3-0 : moved-ab-2-3-0 ≡ target-ab-2-3-0
middle-ab-2-3-0 = refl
middle-bc-2-3-0 : moved-bc-2-3-0 ≡ target-bc-2-3-0
middle-bc-2-3-0 = refl
target-native-seam-2-3-0 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-ab-3-2-1 , E.A.V.selected-proof C.q7 C.q0 F.route-ab-3-2-1) (lift F.route-ab-3-2-1)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-bc-3-2-1 , E.A.V.selected-proof C.q0 C.q7 F.route-bc-3-2-1) (lift F.route-bc-3-2-1)) (lift E.A.V.source-leg)
target-native-seam-2-3-0 = F.middle-3-2-1
triple-2-3-1 : T.vertex-triple base complement complement F.triple-2-3-1 ≡ F.triple-3-2-0
triple-2-3-1 = refl
bind-ab-2-3-1 : F.route-ab-2-3-1 ≡ H.family base complement F.edge-2-3 false
bind-ab-2-3-1 = refl
side-ab-2-3-1 : side-map (fst F.edge-2-3) false ≡ true
side-ab-2-3-1 = refl
route-ab-2-3-1 : K.vertex-move base complement F.route-ab-2-3-1 ≡ F.route-ab-3-2-0
route-ab-2-3-1 = refl
natural-ab-2-3-1 : K.vertex-move base complement F.route-ab-2-3-1 ≡ F.route-ab-3-2-0
natural-ab-2-3-1 = H.covariance base complement F.edge-2-3 false
coherence-ab-2-3-1 : route-ab-2-3-1 ≡ natural-ab-2-3-1
coherence-ab-2-3-1 = H.common-set complement base _ _ _ _
bind-bc-2-3-1 : F.route-bc-2-3-1 ≡ H.family complement complement F.edge-3-1 false
bind-bc-2-3-1 = refl
side-bc-2-3-1 : side-map (fst F.edge-3-1) false ≡ false
side-bc-2-3-1 = refl
route-bc-2-3-1 : K.vertex-move complement complement F.route-bc-2-3-1 ≡ F.route-bc-3-2-0
route-bc-2-3-1 = refl
natural-bc-2-3-1 : K.vertex-move complement complement F.route-bc-2-3-1 ≡ F.route-bc-3-2-0
natural-bc-2-3-1 = H.covariance complement complement F.edge-3-1 false
coherence-bc-2-3-1 : route-bc-2-3-1 ≡ natural-bc-2-3-1
coherence-bc-2-3-1 = H.common-set base base _ _ _ _
bind-ac-2-3-1 : F.route-ac-2-3-1 ≡ H.family base complement F.edge-2-1 false
bind-ac-2-3-1 = refl
side-ac-2-3-1 : side-map (fst F.edge-2-1) false ≡ false
side-ac-2-3-1 = refl
route-ac-2-3-1 : K.vertex-move base complement F.route-ac-2-3-1 ≡ F.route-ac-3-2-0
route-ac-2-3-1 = refl
natural-ac-2-3-1 : K.vertex-move base complement F.route-ac-2-3-1 ≡ F.route-ac-3-2-0
natural-ac-2-3-1 = H.covariance base complement F.edge-2-1 false
coherence-ac-2-3-1 : route-ac-2-3-1 ≡ natural-ac-2-3-1
coherence-ac-2-3-1 = H.common-set complement base _ _ _ _
moved-ab-2-3-1 : E.A.V.InputIndex
moved-ab-2-3-1 = (C.q0 , (m0 , M.move-7-0 (snd (snd F.route-ab-2-3-1))))
moved-bc-2-3-1 : E.A.V.InputIndex
moved-bc-2-3-1 = (C.q0 , (m0 , M.move-7-0 (fst (snd F.route-bc-2-3-1))))
target-ab-2-3-1 : E.A.V.InputIndex
target-ab-2-3-1 = (C.q0 , (fst F.route-ab-3-2-0 , snd (snd F.route-ab-3-2-0)))
target-bc-2-3-1 : E.A.V.InputIndex
target-bc-2-3-1 = (C.q0 , (fst F.route-bc-3-2-0 , fst (snd F.route-bc-3-2-0)))
middle-2-3-1 : moved-ab-2-3-1 ≡ moved-bc-2-3-1
middle-2-3-1 = refl
middle-ab-2-3-1 : moved-ab-2-3-1 ≡ target-ab-2-3-1
middle-ab-2-3-1 = refl
middle-bc-2-3-1 : moved-bc-2-3-1 ≡ target-bc-2-3-1
middle-bc-2-3-1 = refl
target-native-seam-2-3-1 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-ab-3-2-0 , E.A.V.selected-proof C.q7 C.q0 F.route-ab-3-2-0) (lift F.route-ab-3-2-0)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q0 F.route-bc-3-2-0 , E.A.V.selected-proof C.q0 C.q0 F.route-bc-3-2-0) (lift F.route-bc-3-2-0)) (lift E.A.V.source-leg)
target-native-seam-2-3-1 = F.middle-3-2-0
triple-3-0-1 : T.vertex-triple complement base complement F.triple-3-0-1 ≡ F.triple-2-1-0
triple-3-0-1 = refl
bind-ab-3-0-1 : F.route-ab-3-0-1 ≡ H.family complement base F.edge-3-0 true
bind-ab-3-0-1 = refl
side-ab-3-0-1 : side-map (fst F.edge-3-0) true ≡ true
side-ab-3-0-1 = refl
route-ab-3-0-1 : K.vertex-move complement base F.route-ab-3-0-1 ≡ F.route-ab-2-1-0
route-ab-3-0-1 = refl
natural-ab-3-0-1 : K.vertex-move complement base F.route-ab-3-0-1 ≡ F.route-ab-2-1-0
natural-ab-3-0-1 = H.covariance complement base F.edge-3-0 true
coherence-ab-3-0-1 : route-ab-3-0-1 ≡ natural-ab-3-0-1
coherence-ab-3-0-1 = H.common-set base complement _ _ _ _
bind-bc-3-0-1 : F.route-bc-3-0-1 ≡ H.family base complement F.edge-0-1 false
bind-bc-3-0-1 = refl
side-bc-3-0-1 : side-map (fst F.edge-0-1) false ≡ true
side-bc-3-0-1 = refl
route-bc-3-0-1 : K.vertex-move base complement F.route-bc-3-0-1 ≡ F.route-bc-2-1-0
route-bc-3-0-1 = refl
natural-bc-3-0-1 : K.vertex-move base complement F.route-bc-3-0-1 ≡ F.route-bc-2-1-0
natural-bc-3-0-1 = H.covariance base complement F.edge-0-1 false
coherence-bc-3-0-1 : route-bc-3-0-1 ≡ natural-bc-3-0-1
coherence-bc-3-0-1 = H.common-set complement base _ _ _ _
bind-ac-3-0-1 : F.route-ac-3-0-1 ≡ H.family complement complement F.edge-3-1 true
bind-ac-3-0-1 = refl
side-ac-3-0-1 : side-map (fst F.edge-3-1) true ≡ true
side-ac-3-0-1 = refl
route-ac-3-0-1 : K.vertex-move complement complement F.route-ac-3-0-1 ≡ F.route-ac-2-1-0
route-ac-3-0-1 = refl
natural-ac-3-0-1 : K.vertex-move complement complement F.route-ac-3-0-1 ≡ F.route-ac-2-1-0
natural-ac-3-0-1 = H.covariance complement complement F.edge-3-1 true
coherence-ac-3-0-1 : route-ac-3-0-1 ≡ natural-ac-3-0-1
coherence-ac-3-0-1 = H.common-set base base _ _ _ _
moved-ab-3-0-1 : E.A.V.InputIndex
moved-ab-3-0-1 = (C.q7 , (m1 , M.move-0-2 (snd (snd F.route-ab-3-0-1))))
moved-bc-3-0-1 : E.A.V.InputIndex
moved-bc-3-0-1 = (C.q7 , (m1 , M.move-0-2 (fst (snd F.route-bc-3-0-1))))
target-ab-3-0-1 : E.A.V.InputIndex
target-ab-3-0-1 = (C.q7 , (fst F.route-ab-2-1-0 , snd (snd F.route-ab-2-1-0)))
target-bc-3-0-1 : E.A.V.InputIndex
target-bc-3-0-1 = (C.q7 , (fst F.route-bc-2-1-0 , fst (snd F.route-bc-2-1-0)))
middle-3-0-1 : moved-ab-3-0-1 ≡ moved-bc-3-0-1
middle-3-0-1 = refl
middle-ab-3-0-1 : moved-ab-3-0-1 ≡ target-ab-3-0-1
middle-ab-3-0-1 = refl
middle-bc-3-0-1 : moved-bc-3-0-1 ≡ target-bc-3-0-1
middle-bc-3-0-1 = refl
target-native-seam-3-0-1 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-ab-2-1-0 , E.A.V.selected-proof C.q0 C.q7 F.route-ab-2-1-0) (lift F.route-ab-2-1-0)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-bc-2-1-0 , E.A.V.selected-proof C.q7 C.q0 F.route-bc-2-1-0) (lift F.route-bc-2-1-0)) (lift E.A.V.source-leg)
target-native-seam-3-0-1 = F.middle-2-1-0
triple-3-0-2 : T.vertex-triple complement base base F.triple-3-0-2 ≡ F.triple-2-1-3
triple-3-0-2 = refl
bind-ab-3-0-2 : F.route-ab-3-0-2 ≡ H.family complement base F.edge-3-0 false
bind-ab-3-0-2 = refl
side-ab-3-0-2 : side-map (fst F.edge-3-0) false ≡ false
side-ab-3-0-2 = refl
route-ab-3-0-2 : K.vertex-move complement base F.route-ab-3-0-2 ≡ F.route-ab-2-1-3
route-ab-3-0-2 = refl
natural-ab-3-0-2 : K.vertex-move complement base F.route-ab-3-0-2 ≡ F.route-ab-2-1-3
natural-ab-3-0-2 = H.covariance complement base F.edge-3-0 false
coherence-ab-3-0-2 : route-ab-3-0-2 ≡ natural-ab-3-0-2
coherence-ab-3-0-2 = H.common-set base complement _ _ _ _
bind-bc-3-0-2 : F.route-bc-3-0-2 ≡ H.family base base F.edge-0-2 false
bind-bc-3-0-2 = refl
side-bc-3-0-2 : side-map (fst F.edge-0-2) false ≡ false
side-bc-3-0-2 = refl
route-bc-3-0-2 : K.vertex-move base base F.route-bc-3-0-2 ≡ F.route-bc-2-1-3
route-bc-3-0-2 = refl
natural-bc-3-0-2 : K.vertex-move base base F.route-bc-3-0-2 ≡ F.route-bc-2-1-3
natural-bc-3-0-2 = H.covariance base base F.edge-0-2 false
coherence-bc-3-0-2 : route-bc-3-0-2 ≡ natural-bc-3-0-2
coherence-bc-3-0-2 = H.common-set complement complement _ _ _ _
bind-ac-3-0-2 : F.route-ac-3-0-2 ≡ H.family complement base F.edge-3-2 true
bind-ac-3-0-2 = refl
side-ac-3-0-2 : side-map (fst F.edge-3-2) true ≡ false
side-ac-3-0-2 = refl
route-ac-3-0-2 : K.vertex-move complement base F.route-ac-3-0-2 ≡ F.route-ac-2-1-3
route-ac-3-0-2 = refl
natural-ac-3-0-2 : K.vertex-move complement base F.route-ac-3-0-2 ≡ F.route-ac-2-1-3
natural-ac-3-0-2 = H.covariance complement base F.edge-3-2 true
coherence-ac-3-0-2 : route-ac-3-0-2 ≡ natural-ac-3-0-2
coherence-ac-3-0-2 = H.common-set base complement _ _ _ _
moved-ab-3-0-2 : E.A.V.InputIndex
moved-ab-3-0-2 = (C.q7 , (c0 , M.move-0-1 (snd (snd F.route-ab-3-0-2))))
moved-bc-3-0-2 : E.A.V.InputIndex
moved-bc-3-0-2 = (C.q7 , (c0 , M.move-0-1 (fst (snd F.route-bc-3-0-2))))
target-ab-3-0-2 : E.A.V.InputIndex
target-ab-3-0-2 = (C.q7 , (fst F.route-ab-2-1-3 , snd (snd F.route-ab-2-1-3)))
target-bc-3-0-2 : E.A.V.InputIndex
target-bc-3-0-2 = (C.q7 , (fst F.route-bc-2-1-3 , fst (snd F.route-bc-2-1-3)))
middle-3-0-2 : moved-ab-3-0-2 ≡ moved-bc-3-0-2
middle-3-0-2 = refl
middle-ab-3-0-2 : moved-ab-3-0-2 ≡ target-ab-3-0-2
middle-ab-3-0-2 = refl
middle-bc-3-0-2 : moved-bc-3-0-2 ≡ target-bc-3-0-2
middle-bc-3-0-2 = refl
target-native-seam-3-0-2 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-ab-2-1-3 , E.A.V.selected-proof C.q0 C.q7 F.route-ab-2-1-3) (lift F.route-ab-2-1-3)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q7 F.route-bc-2-1-3 , E.A.V.selected-proof C.q7 C.q7 F.route-bc-2-1-3) (lift F.route-bc-2-1-3)) (lift E.A.V.source-leg)
target-native-seam-3-0-2 = F.middle-2-1-3
triple-3-1-0 : T.vertex-triple complement complement base F.triple-3-1-0 ≡ F.triple-2-0-1
triple-3-1-0 = refl
bind-ab-3-1-0 : F.route-ab-3-1-0 ≡ H.family complement complement F.edge-3-1 true
bind-ab-3-1-0 = refl
side-ab-3-1-0 : side-map (fst F.edge-3-1) true ≡ true
side-ab-3-1-0 = refl
route-ab-3-1-0 : K.vertex-move complement complement F.route-ab-3-1-0 ≡ F.route-ab-2-0-1
route-ab-3-1-0 = refl
natural-ab-3-1-0 : K.vertex-move complement complement F.route-ab-3-1-0 ≡ F.route-ab-2-0-1
natural-ab-3-1-0 = H.covariance complement complement F.edge-3-1 true
coherence-ab-3-1-0 : route-ab-3-1-0 ≡ natural-ab-3-1-0
coherence-ab-3-1-0 = H.common-set base base _ _ _ _
bind-bc-3-1-0 : F.route-bc-3-1-0 ≡ H.family complement base F.edge-1-0 false
bind-bc-3-1-0 = refl
side-bc-3-1-0 : side-map (fst F.edge-1-0) false ≡ true
side-bc-3-1-0 = refl
route-bc-3-1-0 : K.vertex-move complement base F.route-bc-3-1-0 ≡ F.route-bc-2-0-1
route-bc-3-1-0 = refl
natural-bc-3-1-0 : K.vertex-move complement base F.route-bc-3-1-0 ≡ F.route-bc-2-0-1
natural-bc-3-1-0 = H.covariance complement base F.edge-1-0 false
coherence-bc-3-1-0 : route-bc-3-1-0 ≡ natural-bc-3-1-0
coherence-bc-3-1-0 = H.common-set base complement _ _ _ _
bind-ac-3-1-0 : F.route-ac-3-1-0 ≡ H.family complement base F.edge-3-0 true
bind-ac-3-1-0 = refl
side-ac-3-1-0 : side-map (fst F.edge-3-0) true ≡ true
side-ac-3-1-0 = refl
route-ac-3-1-0 : K.vertex-move complement base F.route-ac-3-1-0 ≡ F.route-ac-2-0-1
route-ac-3-1-0 = refl
natural-ac-3-1-0 : K.vertex-move complement base F.route-ac-3-1-0 ≡ F.route-ac-2-0-1
natural-ac-3-1-0 = H.covariance complement base F.edge-3-0 true
coherence-ac-3-1-0 : route-ac-3-1-0 ≡ natural-ac-3-1-0
coherence-ac-3-1-0 = H.common-set base complement _ _ _ _
moved-ab-3-1-0 : E.A.V.InputIndex
moved-ab-3-1-0 = (C.q0 , (m1 , M.move-7-2 (snd (snd F.route-ab-3-1-0))))
moved-bc-3-1-0 : E.A.V.InputIndex
moved-bc-3-1-0 = (C.q0 , (m1 , M.move-7-2 (fst (snd F.route-bc-3-1-0))))
target-ab-3-1-0 : E.A.V.InputIndex
target-ab-3-1-0 = (C.q0 , (fst F.route-ab-2-0-1 , snd (snd F.route-ab-2-0-1)))
target-bc-3-1-0 : E.A.V.InputIndex
target-bc-3-1-0 = (C.q0 , (fst F.route-bc-2-0-1 , fst (snd F.route-bc-2-0-1)))
middle-3-1-0 : moved-ab-3-1-0 ≡ moved-bc-3-1-0
middle-3-1-0 = refl
middle-ab-3-1-0 : moved-ab-3-1-0 ≡ target-ab-3-1-0
middle-ab-3-1-0 = refl
middle-bc-3-1-0 : moved-bc-3-1-0 ≡ target-bc-3-1-0
middle-bc-3-1-0 = refl
target-native-seam-3-1-0 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q0 F.route-ab-2-0-1 , E.A.V.selected-proof C.q0 C.q0 F.route-ab-2-0-1) (lift F.route-ab-2-0-1)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-bc-2-0-1 , E.A.V.selected-proof C.q0 C.q7 F.route-bc-2-0-1) (lift F.route-bc-2-0-1)) (lift E.A.V.source-leg)
target-native-seam-3-1-0 = F.middle-2-0-1
triple-3-1-2 : T.vertex-triple complement complement base F.triple-3-1-2 ≡ F.triple-2-0-3
triple-3-1-2 = refl
bind-ab-3-1-2 : F.route-ab-3-1-2 ≡ H.family complement complement F.edge-3-1 false
bind-ab-3-1-2 = refl
side-ab-3-1-2 : side-map (fst F.edge-3-1) false ≡ false
side-ab-3-1-2 = refl
route-ab-3-1-2 : K.vertex-move complement complement F.route-ab-3-1-2 ≡ F.route-ab-2-0-3
route-ab-3-1-2 = refl
natural-ab-3-1-2 : K.vertex-move complement complement F.route-ab-3-1-2 ≡ F.route-ab-2-0-3
natural-ab-3-1-2 = H.covariance complement complement F.edge-3-1 false
coherence-ab-3-1-2 : route-ab-3-1-2 ≡ natural-ab-3-1-2
coherence-ab-3-1-2 = H.common-set base base _ _ _ _
bind-bc-3-1-2 : F.route-bc-3-1-2 ≡ H.family complement base F.edge-1-2 false
bind-bc-3-1-2 = refl
side-bc-3-1-2 : side-map (fst F.edge-1-2) false ≡ false
side-bc-3-1-2 = refl
route-bc-3-1-2 : K.vertex-move complement base F.route-bc-3-1-2 ≡ F.route-bc-2-0-3
route-bc-3-1-2 = refl
natural-bc-3-1-2 : K.vertex-move complement base F.route-bc-3-1-2 ≡ F.route-bc-2-0-3
natural-bc-3-1-2 = H.covariance complement base F.edge-1-2 false
coherence-bc-3-1-2 : route-bc-3-1-2 ≡ natural-bc-3-1-2
coherence-bc-3-1-2 = H.common-set base complement _ _ _ _
bind-ac-3-1-2 : F.route-ac-3-1-2 ≡ H.family complement base F.edge-3-2 false
bind-ac-3-1-2 = refl
side-ac-3-1-2 : side-map (fst F.edge-3-2) false ≡ true
side-ac-3-1-2 = refl
route-ac-3-1-2 : K.vertex-move complement base F.route-ac-3-1-2 ≡ F.route-ac-2-0-3
route-ac-3-1-2 = refl
natural-ac-3-1-2 : K.vertex-move complement base F.route-ac-3-1-2 ≡ F.route-ac-2-0-3
natural-ac-3-1-2 = H.covariance complement base F.edge-3-2 false
coherence-ac-3-1-2 : route-ac-3-1-2 ≡ natural-ac-3-1-2
coherence-ac-3-1-2 = H.common-set base complement _ _ _ _
moved-ab-3-1-2 : E.A.V.InputIndex
moved-ab-3-1-2 = (C.q0 , (m0 , M.move-7-0 (snd (snd F.route-ab-3-1-2))))
moved-bc-3-1-2 : E.A.V.InputIndex
moved-bc-3-1-2 = (C.q0 , (m0 , M.move-7-0 (fst (snd F.route-bc-3-1-2))))
target-ab-3-1-2 : E.A.V.InputIndex
target-ab-3-1-2 = (C.q0 , (fst F.route-ab-2-0-3 , snd (snd F.route-ab-2-0-3)))
target-bc-3-1-2 : E.A.V.InputIndex
target-bc-3-1-2 = (C.q0 , (fst F.route-bc-2-0-3 , fst (snd F.route-bc-2-0-3)))
middle-3-1-2 : moved-ab-3-1-2 ≡ moved-bc-3-1-2
middle-3-1-2 = refl
middle-ab-3-1-2 : moved-ab-3-1-2 ≡ target-ab-3-1-2
middle-ab-3-1-2 = refl
middle-bc-3-1-2 : moved-bc-3-1-2 ≡ target-bc-3-1-2
middle-bc-3-1-2 = refl
target-native-seam-3-1-2 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q0 F.route-ab-2-0-3 , E.A.V.selected-proof C.q0 C.q0 F.route-ab-2-0-3) (lift F.route-ab-2-0-3)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-bc-2-0-3 , E.A.V.selected-proof C.q0 C.q7 F.route-bc-2-0-3) (lift F.route-bc-2-0-3)) (lift E.A.V.source-leg)
target-native-seam-3-1-2 = F.middle-2-0-3
triple-3-2-0 : T.vertex-triple complement base base F.triple-3-2-0 ≡ F.triple-2-3-1
triple-3-2-0 = refl
bind-ab-3-2-0 : F.route-ab-3-2-0 ≡ H.family complement base F.edge-3-2 true
bind-ab-3-2-0 = refl
side-ab-3-2-0 : side-map (fst F.edge-3-2) true ≡ false
side-ab-3-2-0 = refl
route-ab-3-2-0 : K.vertex-move complement base F.route-ab-3-2-0 ≡ F.route-ab-2-3-1
route-ab-3-2-0 = refl
natural-ab-3-2-0 : K.vertex-move complement base F.route-ab-3-2-0 ≡ F.route-ab-2-3-1
natural-ab-3-2-0 = H.covariance complement base F.edge-3-2 true
coherence-ab-3-2-0 : route-ab-3-2-0 ≡ natural-ab-3-2-0
coherence-ab-3-2-0 = H.common-set base complement _ _ _ _
bind-bc-3-2-0 : F.route-bc-3-2-0 ≡ H.family base base F.edge-2-0 false
bind-bc-3-2-0 = refl
side-bc-3-2-0 : side-map (fst F.edge-2-0) false ≡ false
side-bc-3-2-0 = refl
route-bc-3-2-0 : K.vertex-move base base F.route-bc-3-2-0 ≡ F.route-bc-2-3-1
route-bc-3-2-0 = refl
natural-bc-3-2-0 : K.vertex-move base base F.route-bc-3-2-0 ≡ F.route-bc-2-3-1
natural-bc-3-2-0 = H.covariance base base F.edge-2-0 false
coherence-bc-3-2-0 : route-bc-3-2-0 ≡ natural-bc-3-2-0
coherence-bc-3-2-0 = H.common-set complement complement _ _ _ _
bind-ac-3-2-0 : F.route-ac-3-2-0 ≡ H.family complement base F.edge-3-0 false
bind-ac-3-2-0 = refl
side-ac-3-2-0 : side-map (fst F.edge-3-0) false ≡ false
side-ac-3-2-0 = refl
route-ac-3-2-0 : K.vertex-move complement base F.route-ac-3-2-0 ≡ F.route-ac-2-3-1
route-ac-3-2-0 = refl
natural-ac-3-2-0 : K.vertex-move complement base F.route-ac-3-2-0 ≡ F.route-ac-2-3-1
natural-ac-3-2-0 = H.covariance complement base F.edge-3-0 false
coherence-ac-3-2-0 : route-ac-3-2-0 ≡ natural-ac-3-2-0
coherence-ac-3-2-0 = H.common-set base complement _ _ _ _
moved-ab-3-2-0 : E.A.V.InputIndex
moved-ab-3-2-0 = (C.q7 , (c0 , M.move-0-1 (snd (snd F.route-ab-3-2-0))))
moved-bc-3-2-0 : E.A.V.InputIndex
moved-bc-3-2-0 = (C.q7 , (c0 , M.move-0-1 (fst (snd F.route-bc-3-2-0))))
target-ab-3-2-0 : E.A.V.InputIndex
target-ab-3-2-0 = (C.q7 , (fst F.route-ab-2-3-1 , snd (snd F.route-ab-2-3-1)))
target-bc-3-2-0 : E.A.V.InputIndex
target-bc-3-2-0 = (C.q7 , (fst F.route-bc-2-3-1 , fst (snd F.route-bc-2-3-1)))
middle-3-2-0 : moved-ab-3-2-0 ≡ moved-bc-3-2-0
middle-3-2-0 = refl
middle-ab-3-2-0 : moved-ab-3-2-0 ≡ target-ab-3-2-0
middle-ab-3-2-0 = refl
middle-bc-3-2-0 : moved-bc-3-2-0 ≡ target-bc-3-2-0
middle-bc-3-2-0 = refl
target-native-seam-3-2-0 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-ab-2-3-1 , E.A.V.selected-proof C.q0 C.q7 F.route-ab-2-3-1) (lift F.route-ab-2-3-1)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q7 F.route-bc-2-3-1 , E.A.V.selected-proof C.q7 C.q7 F.route-bc-2-3-1) (lift F.route-bc-2-3-1)) (lift E.A.V.source-leg)
target-native-seam-3-2-0 = F.middle-2-3-1
triple-3-2-1 : T.vertex-triple complement base complement F.triple-3-2-1 ≡ F.triple-2-3-0
triple-3-2-1 = refl
bind-ab-3-2-1 : F.route-ab-3-2-1 ≡ H.family complement base F.edge-3-2 false
bind-ab-3-2-1 = refl
side-ab-3-2-1 : side-map (fst F.edge-3-2) false ≡ true
side-ab-3-2-1 = refl
route-ab-3-2-1 : K.vertex-move complement base F.route-ab-3-2-1 ≡ F.route-ab-2-3-0
route-ab-3-2-1 = refl
natural-ab-3-2-1 : K.vertex-move complement base F.route-ab-3-2-1 ≡ F.route-ab-2-3-0
natural-ab-3-2-1 = H.covariance complement base F.edge-3-2 false
coherence-ab-3-2-1 : route-ab-3-2-1 ≡ natural-ab-3-2-1
coherence-ab-3-2-1 = H.common-set base complement _ _ _ _
bind-bc-3-2-1 : F.route-bc-3-2-1 ≡ H.family base complement F.edge-2-1 false
bind-bc-3-2-1 = refl
side-bc-3-2-1 : side-map (fst F.edge-2-1) false ≡ false
side-bc-3-2-1 = refl
route-bc-3-2-1 : K.vertex-move base complement F.route-bc-3-2-1 ≡ F.route-bc-2-3-0
route-bc-3-2-1 = refl
natural-bc-3-2-1 : K.vertex-move base complement F.route-bc-3-2-1 ≡ F.route-bc-2-3-0
natural-bc-3-2-1 = H.covariance base complement F.edge-2-1 false
coherence-bc-3-2-1 : route-bc-3-2-1 ≡ natural-bc-3-2-1
coherence-bc-3-2-1 = H.common-set complement base _ _ _ _
bind-ac-3-2-1 : F.route-ac-3-2-1 ≡ H.family complement complement F.edge-3-1 false
bind-ac-3-2-1 = refl
side-ac-3-2-1 : side-map (fst F.edge-3-1) false ≡ false
side-ac-3-2-1 = refl
route-ac-3-2-1 : K.vertex-move complement complement F.route-ac-3-2-1 ≡ F.route-ac-2-3-0
route-ac-3-2-1 = refl
natural-ac-3-2-1 : K.vertex-move complement complement F.route-ac-3-2-1 ≡ F.route-ac-2-3-0
natural-ac-3-2-1 = H.covariance complement complement F.edge-3-1 false
coherence-ac-3-2-1 : route-ac-3-2-1 ≡ natural-ac-3-2-1
coherence-ac-3-2-1 = H.common-set base base _ _ _ _
moved-ab-3-2-1 : E.A.V.InputIndex
moved-ab-3-2-1 = (C.q7 , (m0 , M.move-0-0 (snd (snd F.route-ab-3-2-1))))
moved-bc-3-2-1 : E.A.V.InputIndex
moved-bc-3-2-1 = (C.q7 , (m0 , M.move-0-0 (fst (snd F.route-bc-3-2-1))))
target-ab-3-2-1 : E.A.V.InputIndex
target-ab-3-2-1 = (C.q7 , (fst F.route-ab-2-3-0 , snd (snd F.route-ab-2-3-0)))
target-bc-3-2-1 : E.A.V.InputIndex
target-bc-3-2-1 = (C.q7 , (fst F.route-bc-2-3-0 , fst (snd F.route-bc-2-3-0)))
middle-3-2-1 : moved-ab-3-2-1 ≡ moved-bc-3-2-1
middle-3-2-1 = refl
middle-ab-3-2-1 : moved-ab-3-2-1 ≡ target-ab-3-2-1
middle-ab-3-2-1 = refl
middle-bc-3-2-1 : moved-bc-3-2-1 ≡ target-bc-3-2-1
middle-bc-3-2-1 = refl
target-native-seam-3-2-1 : E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q0 C.q7 F.route-ab-2-3-0 , E.A.V.selected-proof C.q0 C.q7 F.route-ab-2-3-0) (lift F.route-ab-2-3-0)) (lift E.A.V.target-leg) ≡ E.A.V.R.premise (E.A.V.R.premise (E.A.V.selected-package C.q7 C.q0 F.route-bc-2-3-0 , E.A.V.selected-proof C.q7 C.q0 F.route-bc-2-3-0) (lift F.route-bc-2-3-0)) (lift E.A.V.source-leg)
target-native-seam-3-2-1 = F.middle-2-3-0
