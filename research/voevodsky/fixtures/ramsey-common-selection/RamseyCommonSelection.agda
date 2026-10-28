{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyCommonSelection where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Unit.Base using (tt)
open import Cubical.Data.Empty.Base using (⊥)
open import RamseySingleFrameFaces using (c0; m0; c1; m1)
open import RamseyNativeEdgeAttachments using (e01; e02; e03; e12; e13; e23)
open import RamseyEndpointPolicy using (Frame; base; complement; swap; choose; side-map; not-fixed)
import RamseyRequestedPortExamples as C
import RamseyEdgeAttachmentsExamples as E
import RamseyEdgeNaturality as N
import RamseyPermitEquivalence as M
chart : Frame → C.Chart
chart base = C.q0
chart complement = C.q7
reverse : (a b : Frame) → E.A.S.Common (chart a) (chart b) → E.A.S.Common (chart b) (chart a)
reverse a b (e , (p , q)) = e , (q , p)
edge-move : (a b : Frame) → E.A.S.Common (chart a) (chart b) → E.A.S.Common (chart (swap a)) (chart (swap b))
edge-move base base (e01 , (p , q)) = e01 , (N.move-0-0 p , N.move-0-0 q)
edge-move base base (e02 , (p , q)) = e13 , (N.move-0-1 p , N.move-0-1 q)
edge-move base base (e03 , (p , q)) = e12 , (N.move-0-2 p , N.move-0-2 q)
edge-move base base (e12 , (p , q)) = e03 , (N.move-0-3 p , N.move-0-3 q)
edge-move base base (e13 , (p , q)) = e02 , (N.move-0-4 p , N.move-0-4 q)
edge-move base base (e23 , (p , q)) = e23 , (N.move-0-5 p , N.move-0-5 q)
edge-move base complement (e01 , (p , q)) = e01 , (N.move-0-0 p , N.move-7-0 q)
edge-move base complement (e02 , (p , q)) = e13 , (N.move-0-1 p , N.move-7-1 q)
edge-move base complement (e03 , (p , q)) = e12 , (N.move-0-2 p , N.move-7-2 q)
edge-move base complement (e12 , (p , q)) = e03 , (N.move-0-3 p , N.move-7-3 q)
edge-move base complement (e13 , (p , q)) = e02 , (N.move-0-4 p , N.move-7-4 q)
edge-move base complement (e23 , (p , q)) = e23 , (N.move-0-5 p , N.move-7-5 q)
edge-move complement base (e01 , (p , q)) = e01 , (N.move-7-0 p , N.move-0-0 q)
edge-move complement base (e02 , (p , q)) = e13 , (N.move-7-1 p , N.move-0-1 q)
edge-move complement base (e03 , (p , q)) = e12 , (N.move-7-2 p , N.move-0-2 q)
edge-move complement base (e12 , (p , q)) = e03 , (N.move-7-3 p , N.move-0-3 q)
edge-move complement base (e13 , (p , q)) = e02 , (N.move-7-4 p , N.move-0-4 q)
edge-move complement base (e23 , (p , q)) = e23 , (N.move-7-5 p , N.move-0-5 q)
edge-move complement complement (e01 , (p , q)) = e01 , (N.move-7-0 p , N.move-7-0 q)
edge-move complement complement (e02 , (p , q)) = e13 , (N.move-7-1 p , N.move-7-1 q)
edge-move complement complement (e03 , (p , q)) = e12 , (N.move-7-2 p , N.move-7-2 q)
edge-move complement complement (e12 , (p , q)) = e03 , (N.move-7-3 p , N.move-7-3 q)
edge-move complement complement (e13 , (p , q)) = e02 , (N.move-7-4 p , N.move-7-4 q)
edge-move complement complement (e23 , (p , q)) = e23 , (N.move-7-5 p , N.move-7-5 q)
vertex-move : (a b : Frame) → E.A.V.Common (chart a) (chart b) → E.A.V.Common (chart (swap a)) (chart (swap b))
vertex-move base base (c0 , (p , q)) = m0 , (M.move-0-0 p , M.move-0-0 q)
vertex-move base base (m0 , (p , q)) = c0 , (M.move-0-1 p , M.move-0-1 q)
vertex-move base base (c1 , (p , q)) = m1 , (M.move-0-2 p , M.move-0-2 q)
vertex-move base base (m1 , (p , q)) = c1 , (M.move-0-3 p , M.move-0-3 q)
vertex-move base complement (c0 , (p , q)) = m0 , (M.move-0-0 p , M.move-7-0 q)
vertex-move base complement (m0 , (p , q)) = c0 , (M.move-0-1 p , M.move-7-1 q)
vertex-move base complement (c1 , (p , q)) = m1 , (M.move-0-2 p , M.move-7-2 q)
vertex-move base complement (m1 , (p , q)) = c1 , (M.move-0-3 p , M.move-7-3 q)
vertex-move complement base (c0 , (p , q)) = m0 , (M.move-7-0 p , M.move-0-0 q)
vertex-move complement base (m0 , (p , q)) = c0 , (M.move-7-1 p , M.move-0-1 q)
vertex-move complement base (c1 , (p , q)) = m1 , (M.move-7-2 p , M.move-0-2 q)
vertex-move complement base (m1 , (p , q)) = c1 , (M.move-7-3 p , M.move-0-3 q)
vertex-move complement complement (c0 , (p , q)) = m0 , (M.move-7-0 p , M.move-7-0 q)
vertex-move complement complement (m0 , (p , q)) = c0 , (M.move-7-1 p , M.move-7-1 q)
vertex-move complement complement (c1 , (p , q)) = m1 , (M.move-7-2 p , M.move-7-2 q)
vertex-move complement complement (m1 , (p , q)) = c1 , (M.move-7-3 p , M.move-7-3 q)
FullSelector : Type
FullSelector = (a b : Frame) → E.A.S.Common (chart a) (chart b) → Bool
ordered : FullSelector
ordered a b (e , ports) = choose a e
Covariant : FullSelector → Type
Covariant s = (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) → s (swap a) (swap b) (edge-move a b x) ≡ side-map (fst x) (s a b x)
ReversalInvariant : FullSelector → Type
ReversalInvariant s = (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) → s b a (reverse a b x) ≡ s a b x
ordered-covariant : Covariant ordered
ordered-covariant base base (e01 , (p , q)) = refl
ordered-covariant base base (e02 , (p , q)) = refl
ordered-covariant base base (e03 , (p , q)) = refl
ordered-covariant base base (e12 , (p , q)) = refl
ordered-covariant base base (e13 , (p , q)) = refl
ordered-covariant base base (e23 , (p , q)) = refl
ordered-covariant base complement (e01 , (p , q)) = refl
ordered-covariant base complement (e02 , (p , q)) = refl
ordered-covariant base complement (e03 , (p , q)) = refl
ordered-covariant base complement (e12 , (p , q)) = refl
ordered-covariant base complement (e13 , (p , q)) = refl
ordered-covariant base complement (e23 , (p , q)) = refl
ordered-covariant complement base (e01 , (p , q)) = refl
ordered-covariant complement base (e02 , (p , q)) = refl
ordered-covariant complement base (e03 , (p , q)) = refl
ordered-covariant complement base (e12 , (p , q)) = refl
ordered-covariant complement base (e13 , (p , q)) = refl
ordered-covariant complement base (e23 , (p , q)) = refl
ordered-covariant complement complement (e01 , (p , q)) = refl
ordered-covariant complement complement (e02 , (p , q)) = refl
ordered-covariant complement complement (e03 , (p , q)) = refl
ordered-covariant complement complement (e12 , (p , q)) = refl
ordered-covariant complement complement (e13 , (p , q)) = refl
ordered-covariant complement complement (e23 , (p , q)) = refl
select : (a b : Frame) → E.A.S.Common (chart a) (chart b) → E.A.V.Common (chart a) (chart b)
select a b x = E.A.restrict-common (ordered a b x) {a = chart a} {b = chart b} x
select-natural : (a b : Frame) (x : E.A.S.Common (chart a) (chart b)) → vertex-move a b (select a b x) ≡ select (swap a) (swap b) (edge-move a b x)
select-natural base base (e01 , (p , q)) i = m0 , (N.restrict-0-0-0 p i , N.restrict-0-0-0 q i)
select-natural base base (e02 , (p , q)) i = m0 , (N.restrict-0-1-0 p i , N.restrict-0-1-0 q i)
select-natural base base (e03 , (p , q)) i = m0 , (N.restrict-0-2-0 p i , N.restrict-0-2-0 q i)
select-natural base base (e12 , (p , q)) i = c0 , (N.restrict-0-3-0 p i , N.restrict-0-3-0 q i)
select-natural base base (e13 , (p , q)) i = c0 , (N.restrict-0-4-0 p i , N.restrict-0-4-0 q i)
select-natural base base (e23 , (p , q)) i = m1 , (N.restrict-0-5-0 p i , N.restrict-0-5-0 q i)
select-natural base complement (e01 , (p , q)) i = m0 , (N.restrict-0-0-0 p i , N.restrict-7-0-0 q i)
select-natural base complement (e02 , (p , q)) i = m0 , (N.restrict-0-1-0 p i , N.restrict-7-1-0 q i)
select-natural base complement (e03 , (p , q)) i = m0 , (N.restrict-0-2-0 p i , N.restrict-7-2-0 q i)
select-natural base complement (e12 , (p , q)) i = c0 , (N.restrict-0-3-0 p i , N.restrict-7-3-0 q i)
select-natural base complement (e13 , (p , q)) i = c0 , (N.restrict-0-4-0 p i , N.restrict-7-4-0 q i)
select-natural base complement (e23 , (p , q)) i = m1 , (N.restrict-0-5-0 p i , N.restrict-7-5-0 q i)
select-natural complement base (e01 , (p , q)) i = c0 , (N.restrict-7-0-1 p i , N.restrict-0-0-1 q i)
select-natural complement base (e02 , (p , q)) i = m0 , (N.restrict-7-1-0 p i , N.restrict-0-1-0 q i)
select-natural complement base (e03 , (p , q)) i = m0 , (N.restrict-7-2-0 p i , N.restrict-0-2-0 q i)
select-natural complement base (e12 , (p , q)) i = c0 , (N.restrict-7-3-0 p i , N.restrict-0-3-0 q i)
select-natural complement base (e13 , (p , q)) i = c0 , (N.restrict-7-4-0 p i , N.restrict-0-4-0 q i)
select-natural complement base (e23 , (p , q)) i = c1 , (N.restrict-7-5-1 p i , N.restrict-0-5-1 q i)
select-natural complement complement (e01 , (p , q)) i = c0 , (N.restrict-7-0-1 p i , N.restrict-7-0-1 q i)
select-natural complement complement (e02 , (p , q)) i = m0 , (N.restrict-7-1-0 p i , N.restrict-7-1-0 q i)
select-natural complement complement (e03 , (p , q)) i = m0 , (N.restrict-7-2-0 p i , N.restrict-7-2-0 q i)
select-natural complement complement (e12 , (p , q)) i = c0 , (N.restrict-7-3-0 p i , N.restrict-7-3-0 q i)
select-natural complement complement (e13 , (p , q)) i = c0 , (N.restrict-7-4-0 p i , N.restrict-7-4-0 q i)
select-natural complement complement (e23 , (p , q)) i = c1 , (N.restrict-7-5-1 p i , N.restrict-7-5-1 q i)
witness : E.A.S.Common C.q0 C.q7
witness = e01 , (E.att-0-2-0 , E.att-7-3-0)
witness-move-reverses : edge-move base complement witness ≡ reverse base complement witness
witness-move-reverses = refl
no-covariant-reversal : (s : FullSelector) → Covariant s → ReversalInvariant s → ⊥
no-covariant-reversal s covariance reversal = not-fixed (s base complement witness) (sym (covariance base complement witness) ∙ reversal base complement witness)
ordered-not-reversal : ReversalInvariant ordered → ⊥
ordered-not-reversal = no-covariant-reversal ordered ordered-covariant
left : FullSelector
left a b x = false
left-reversal : ReversalInvariant left
left-reversal a b x = refl
left-not-covariant : Covariant left → ⊥
left-not-covariant covariance = no-covariant-reversal left covariance left-reversal
different-selected-vertices : fst (select base complement witness) ≡ fst (select complement base (reverse base complement witness)) → ⊥
different-selected-vertices p = transport (cong (M.Is m0) (sym p)) tt
