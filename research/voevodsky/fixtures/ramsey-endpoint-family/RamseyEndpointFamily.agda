{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEndpointFamily where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import RamseySingleFrameFaces using (c0; m0; c1; m1)
open import RamseyNativeEdgeAttachments using (e01; e02; e03; e12; e13; e23)
open import RamseyEndpointPolicy using (Frame; base; complement; swap; side-map)
open import RamseyCommonSelection using (chart; reverse; edge-move; vertex-move; witness)
open import RamseyPermitFibers using (vertex-set; facet-fiber-prop)
import RamseyEdgeNaturality as N
import RamseyEdgeAttachmentsExamples as E
family : (a b : Frame) → E.A.S.Common (chart a) (chart b) → Bool → E.A.V.Common (chart a) (chart b)
family a b x side = E.A.restrict-common side {a = chart a} {b = chart b} x
reverse-vertex : (a b : Frame) → E.A.V.Common (chart a) (chart b) → E.A.V.Common (chart b) (chart a)
reverse-vertex a b (v , (p , q)) = v , (q , p)
family-native : (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) (side : Bool) → E.A.V.R.Resolve (E.A.V.selected-package (chart a) (chart b) (family a b x side))
family-native a b x side = E.A.restricted-selection side (chart a) (chart b) x
covariance : (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) (side : Bool) → vertex-move a b (family a b x side) ≡ family (swap a) (swap b) (edge-move a b x) (side-map (fst x) side)
covariance base base (e01 , (p , q)) false i = m0 , (N.restrict-0-0-0 p i , N.restrict-0-0-0 q i)
covariance base base (e01 , (p , q)) true i = c0 , (N.restrict-0-0-1 p i , N.restrict-0-0-1 q i)
covariance base base (e02 , (p , q)) false i = m0 , (N.restrict-0-1-0 p i , N.restrict-0-1-0 q i)
covariance base base (e02 , (p , q)) true i = m1 , (N.restrict-0-1-1 p i , N.restrict-0-1-1 q i)
covariance base base (e03 , (p , q)) false i = m0 , (N.restrict-0-2-0 p i , N.restrict-0-2-0 q i)
covariance base base (e03 , (p , q)) true i = c1 , (N.restrict-0-2-1 p i , N.restrict-0-2-1 q i)
covariance base base (e12 , (p , q)) false i = c0 , (N.restrict-0-3-0 p i , N.restrict-0-3-0 q i)
covariance base base (e12 , (p , q)) true i = m1 , (N.restrict-0-3-1 p i , N.restrict-0-3-1 q i)
covariance base base (e13 , (p , q)) false i = c0 , (N.restrict-0-4-0 p i , N.restrict-0-4-0 q i)
covariance base base (e13 , (p , q)) true i = c1 , (N.restrict-0-4-1 p i , N.restrict-0-4-1 q i)
covariance base base (e23 , (p , q)) false i = m1 , (N.restrict-0-5-0 p i , N.restrict-0-5-0 q i)
covariance base base (e23 , (p , q)) true i = c1 , (N.restrict-0-5-1 p i , N.restrict-0-5-1 q i)
covariance base complement (e01 , (p , q)) false i = m0 , (N.restrict-0-0-0 p i , N.restrict-7-0-0 q i)
covariance base complement (e01 , (p , q)) true i = c0 , (N.restrict-0-0-1 p i , N.restrict-7-0-1 q i)
covariance base complement (e02 , (p , q)) false i = m0 , (N.restrict-0-1-0 p i , N.restrict-7-1-0 q i)
covariance base complement (e02 , (p , q)) true i = m1 , (N.restrict-0-1-1 p i , N.restrict-7-1-1 q i)
covariance base complement (e03 , (p , q)) false i = m0 , (N.restrict-0-2-0 p i , N.restrict-7-2-0 q i)
covariance base complement (e03 , (p , q)) true i = c1 , (N.restrict-0-2-1 p i , N.restrict-7-2-1 q i)
covariance base complement (e12 , (p , q)) false i = c0 , (N.restrict-0-3-0 p i , N.restrict-7-3-0 q i)
covariance base complement (e12 , (p , q)) true i = m1 , (N.restrict-0-3-1 p i , N.restrict-7-3-1 q i)
covariance base complement (e13 , (p , q)) false i = c0 , (N.restrict-0-4-0 p i , N.restrict-7-4-0 q i)
covariance base complement (e13 , (p , q)) true i = c1 , (N.restrict-0-4-1 p i , N.restrict-7-4-1 q i)
covariance base complement (e23 , (p , q)) false i = m1 , (N.restrict-0-5-0 p i , N.restrict-7-5-0 q i)
covariance base complement (e23 , (p , q)) true i = c1 , (N.restrict-0-5-1 p i , N.restrict-7-5-1 q i)
covariance complement base (e01 , (p , q)) false i = m0 , (N.restrict-7-0-0 p i , N.restrict-0-0-0 q i)
covariance complement base (e01 , (p , q)) true i = c0 , (N.restrict-7-0-1 p i , N.restrict-0-0-1 q i)
covariance complement base (e02 , (p , q)) false i = m0 , (N.restrict-7-1-0 p i , N.restrict-0-1-0 q i)
covariance complement base (e02 , (p , q)) true i = m1 , (N.restrict-7-1-1 p i , N.restrict-0-1-1 q i)
covariance complement base (e03 , (p , q)) false i = m0 , (N.restrict-7-2-0 p i , N.restrict-0-2-0 q i)
covariance complement base (e03 , (p , q)) true i = c1 , (N.restrict-7-2-1 p i , N.restrict-0-2-1 q i)
covariance complement base (e12 , (p , q)) false i = c0 , (N.restrict-7-3-0 p i , N.restrict-0-3-0 q i)
covariance complement base (e12 , (p , q)) true i = m1 , (N.restrict-7-3-1 p i , N.restrict-0-3-1 q i)
covariance complement base (e13 , (p , q)) false i = c0 , (N.restrict-7-4-0 p i , N.restrict-0-4-0 q i)
covariance complement base (e13 , (p , q)) true i = c1 , (N.restrict-7-4-1 p i , N.restrict-0-4-1 q i)
covariance complement base (e23 , (p , q)) false i = m1 , (N.restrict-7-5-0 p i , N.restrict-0-5-0 q i)
covariance complement base (e23 , (p , q)) true i = c1 , (N.restrict-7-5-1 p i , N.restrict-0-5-1 q i)
covariance complement complement (e01 , (p , q)) false i = m0 , (N.restrict-7-0-0 p i , N.restrict-7-0-0 q i)
covariance complement complement (e01 , (p , q)) true i = c0 , (N.restrict-7-0-1 p i , N.restrict-7-0-1 q i)
covariance complement complement (e02 , (p , q)) false i = m0 , (N.restrict-7-1-0 p i , N.restrict-7-1-0 q i)
covariance complement complement (e02 , (p , q)) true i = m1 , (N.restrict-7-1-1 p i , N.restrict-7-1-1 q i)
covariance complement complement (e03 , (p , q)) false i = m0 , (N.restrict-7-2-0 p i , N.restrict-7-2-0 q i)
covariance complement complement (e03 , (p , q)) true i = c1 , (N.restrict-7-2-1 p i , N.restrict-7-2-1 q i)
covariance complement complement (e12 , (p , q)) false i = c0 , (N.restrict-7-3-0 p i , N.restrict-7-3-0 q i)
covariance complement complement (e12 , (p , q)) true i = m1 , (N.restrict-7-3-1 p i , N.restrict-7-3-1 q i)
covariance complement complement (e13 , (p , q)) false i = c0 , (N.restrict-7-4-0 p i , N.restrict-7-4-0 q i)
covariance complement complement (e13 , (p , q)) true i = c1 , (N.restrict-7-4-1 p i , N.restrict-7-4-1 q i)
covariance complement complement (e23 , (p , q)) false i = m1 , (N.restrict-7-5-0 p i , N.restrict-7-5-0 q i)
covariance complement complement (e23 , (p , q)) true i = c1 , (N.restrict-7-5-1 p i , N.restrict-7-5-1 q i)
reversal : (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) (side : Bool) → reverse-vertex a b (family a b x side) ≡ family b a (reverse a b x) side
reversal a b (e , (p , q)) false = refl
reversal a b (e , (p , q)) true = refl
edge-interchange : (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) → edge-move b a (reverse a b x) ≡ reverse (swap a) (swap b) (edge-move a b x)
edge-interchange base base (e01 , (p , q)) = refl
edge-interchange base base (e02 , (p , q)) = refl
edge-interchange base base (e03 , (p , q)) = refl
edge-interchange base base (e12 , (p , q)) = refl
edge-interchange base base (e13 , (p , q)) = refl
edge-interchange base base (e23 , (p , q)) = refl
edge-interchange base complement (e01 , (p , q)) = refl
edge-interchange base complement (e02 , (p , q)) = refl
edge-interchange base complement (e03 , (p , q)) = refl
edge-interchange base complement (e12 , (p , q)) = refl
edge-interchange base complement (e13 , (p , q)) = refl
edge-interchange base complement (e23 , (p , q)) = refl
edge-interchange complement base (e01 , (p , q)) = refl
edge-interchange complement base (e02 , (p , q)) = refl
edge-interchange complement base (e03 , (p , q)) = refl
edge-interchange complement base (e12 , (p , q)) = refl
edge-interchange complement base (e13 , (p , q)) = refl
edge-interchange complement base (e23 , (p , q)) = refl
edge-interchange complement complement (e01 , (p , q)) = refl
edge-interchange complement complement (e02 , (p , q)) = refl
edge-interchange complement complement (e03 , (p , q)) = refl
edge-interchange complement complement (e12 , (p , q)) = refl
edge-interchange complement complement (e13 , (p , q)) = refl
edge-interchange complement complement (e23 , (p , q)) = refl
vertex-interchange : (a b : Frame) (x : E.A.V.Common (chart a) (chart b)) → vertex-move b a (reverse-vertex a b x) ≡ reverse-vertex (swap a) (swap b) (vertex-move a b x)
vertex-interchange base base (c0 , (p , q)) = refl
vertex-interchange base base (m0 , (p , q)) = refl
vertex-interchange base base (c1 , (p , q)) = refl
vertex-interchange base base (m1 , (p , q)) = refl
vertex-interchange base complement (c0 , (p , q)) = refl
vertex-interchange base complement (m0 , (p , q)) = refl
vertex-interchange base complement (c1 , (p , q)) = refl
vertex-interchange base complement (m1 , (p , q)) = refl
vertex-interchange complement base (c0 , (p , q)) = refl
vertex-interchange complement base (m0 , (p , q)) = refl
vertex-interchange complement base (c1 , (p , q)) = refl
vertex-interchange complement base (m1 , (p , q)) = refl
vertex-interchange complement complement (c0 , (p , q)) = refl
vertex-interchange complement complement (m0 , (p , q)) = refl
vertex-interchange complement complement (c1 , (p , q)) = refl
vertex-interchange complement complement (m1 , (p , q)) = refl
common-set : (a b : Frame) → isSet (E.A.V.Common (chart a) (chart b))
common-set a b = isSetΣ vertex-set (λ v → isSetΣ (isSetΣ vertex-set (λ f → isProp→isSet (facet-fiber-prop (chart a) v f))) (λ _ → isSetΣ vertex-set (λ f → isProp→isSet (facet-fiber-prop (chart b) v f))))
reverse-then-move : (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) (side : Bool) → vertex-move b a (reverse-vertex a b (family a b x side)) ≡ family (swap b) (swap a) (edge-move b a (reverse a b x)) (side-map (fst x) side)
reverse-then-move a b (e , (p , q)) side = cong (vertex-move b a) (reversal a b (e , (p , q)) side) ∙ covariance b a (reverse a b (e , (p , q))) side
move-then-reverse : (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) (side : Bool) → vertex-move b a (reverse-vertex a b (family a b x side)) ≡ family (swap b) (swap a) (edge-move b a (reverse a b x)) (side-map (fst x) side)
move-then-reverse a b x side = vertex-interchange a b (family a b x side) ∙ cong (reverse-vertex (swap a) (swap b)) (covariance a b x side) ∙ reversal (swap a) (swap b) (edge-move a b x) (side-map (fst x) side) ∙ cong (λ y → family (swap b) (swap a) y (side-map (fst x) side)) (sym (edge-interchange a b x))
interchange : (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) (side : Bool) → reverse-then-move a b x side ≡ move-then-reverse a b x side
interchange a b x side = common-set (swap b) (swap a) _ _ _ _
