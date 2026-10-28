{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEndpointPolicy where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Unit.Base using (tt)
open import Cubical.Data.Empty.Base using (⊥)
open import RamseySingleFrameFaces using (Vertex; c0; m0)
open import RamseyNativeEdgeAttachments using (Edge; e01; e02; e03; e12; e13; e23; endpoint)
import RamseyEdgeNaturality as N
import RamseyPermitEquivalence as M
import RamseyRequestedPortExamples as C
import RamseyEdgeAttachmentsExamples as E
edge-map : Edge → Edge
edge-map e01 = e01
edge-map e02 = e13
edge-map e03 = e12
edge-map e12 = e03
edge-map e13 = e02
edge-map e23 = e23
side-map : Edge → Bool → Bool
side-map e01 b = not b
side-map e02 b = b
side-map e03 b = b
side-map e12 b = b
side-map e13 b = b
side-map e23 b = not b
Selector : Type
Selector = Edge → Bool
turn : Selector → Selector
turn s e = side-map e (s (edge-map e))
not-square : (b : Bool) → not (not b) ≡ b
not-square false = refl
not-square true = refl
turn-square-at : (s : Selector) (e : Edge) → turn (turn s) e ≡ s e
turn-square-at s e01 = not-square (s e01)
turn-square-at s e02 = refl
turn-square-at s e03 = refl
turn-square-at s e12 = refl
turn-square-at s e13 = refl
turn-square-at s e23 = not-square (s e23)
turn-square : (s : Selector) → turn (turn s) ≡ s
turn-square s = funExt (turn-square-at s)
covariant : (s : Selector) (e : Edge) → N.vertex-map (endpoint (s e) e) ≡ endpoint (turn s (edge-map e)) (edge-map e)
covariant s e01 with s e01
... | false = refl
... | true = refl
covariant s e02 with s e02
... | false = refl
... | true = refl
covariant s e03 with s e03
... | false = refl
... | true = refl
covariant s e12 with s e12
... | false = refl
... | true = refl
covariant s e13 with s e13
... | false = refl
... | true = refl
covariant s e23 with s e23
... | false = refl
... | true = refl
not-fixed : (b : Bool) → not b ≡ b → ⊥
not-fixed false p = false≢true (sym p)
not-fixed true p = false≢true p
no-fixed-selector : (s : Selector) → turn s ≡ s → ⊥
no-fixed-selector s p = not-fixed (s e01) (cong (λ f → f e01) p)
fixed-endpoint-obstruction : (b : Bool) → N.vertex-map (endpoint b e01) ≡ endpoint b e01 → ⊥
fixed-endpoint-obstruction false p = transport (cong (M.Is c0) (sym p)) tt
fixed-endpoint-obstruction true p = transport (cong (M.Is m0) (sym p)) tt
no-geometric-selector : (s : Selector) → ((e : Edge) → N.vertex-map (endpoint (s e) e) ≡ endpoint (s (edge-map e)) (edge-map e)) → ⊥
no-geometric-selector s law = fixed-endpoint-obstruction (s e01) (law e01)
data Frame : Type where
  base complement : Frame
swap : Frame → Frame
swap base = complement
swap complement = base
choose : Frame → Selector
choose base e = false
choose complement e = side-map e false
context-covariant : (f : Frame) (e : Edge) → N.vertex-map (endpoint (choose f e) e) ≡ endpoint (choose (swap f) (edge-map e)) (edge-map e)
context-covariant base e01 = refl
context-covariant base e02 = refl
context-covariant base e03 = refl
context-covariant base e12 = refl
context-covariant base e13 = refl
context-covariant base e23 = refl
context-covariant complement e01 = refl
context-covariant complement e02 = refl
context-covariant complement e03 = refl
context-covariant complement e12 = refl
context-covariant complement e13 = refl
context-covariant complement e23 = refl
context-restrict-0-0 : (p : E.A.EdgePermit C.q0 e01) → M.move-0-0 (E.A.restrict false C.q0 e01 p) ≡ E.A.restrict true C.q7 e01 (N.move-0-0 p)
context-restrict-0-0 = N.restrict-0-0-0
context-restrict-0-1 : (p : E.A.EdgePermit C.q0 e02) → M.move-0-0 (E.A.restrict false C.q0 e02 p) ≡ E.A.restrict false C.q7 e13 (N.move-0-1 p)
context-restrict-0-1 = N.restrict-0-1-0
context-restrict-0-2 : (p : E.A.EdgePermit C.q0 e03) → M.move-0-0 (E.A.restrict false C.q0 e03 p) ≡ E.A.restrict false C.q7 e12 (N.move-0-2 p)
context-restrict-0-2 = N.restrict-0-2-0
context-restrict-0-3 : (p : E.A.EdgePermit C.q0 e12) → M.move-0-1 (E.A.restrict false C.q0 e12 p) ≡ E.A.restrict false C.q7 e03 (N.move-0-3 p)
context-restrict-0-3 = N.restrict-0-3-0
context-restrict-0-4 : (p : E.A.EdgePermit C.q0 e13) → M.move-0-1 (E.A.restrict false C.q0 e13 p) ≡ E.A.restrict false C.q7 e02 (N.move-0-4 p)
context-restrict-0-4 = N.restrict-0-4-0
context-restrict-0-5 : (p : E.A.EdgePermit C.q0 e23) → M.move-0-2 (E.A.restrict false C.q0 e23 p) ≡ E.A.restrict true C.q7 e23 (N.move-0-5 p)
context-restrict-0-5 = N.restrict-0-5-0
context-restrict-7-0 : (p : E.A.EdgePermit C.q7 e01) → M.move-7-1 (E.A.restrict true C.q7 e01 p) ≡ E.A.restrict false C.q0 e01 (N.move-7-0 p)
context-restrict-7-0 = N.restrict-7-0-1
context-restrict-7-1 : (p : E.A.EdgePermit C.q7 e02) → M.move-7-0 (E.A.restrict false C.q7 e02 p) ≡ E.A.restrict false C.q0 e13 (N.move-7-1 p)
context-restrict-7-1 = N.restrict-7-1-0
context-restrict-7-2 : (p : E.A.EdgePermit C.q7 e03) → M.move-7-0 (E.A.restrict false C.q7 e03 p) ≡ E.A.restrict false C.q0 e12 (N.move-7-2 p)
context-restrict-7-2 = N.restrict-7-2-0
context-restrict-7-3 : (p : E.A.EdgePermit C.q7 e12) → M.move-7-1 (E.A.restrict false C.q7 e12 p) ≡ E.A.restrict false C.q0 e03 (N.move-7-3 p)
context-restrict-7-3 = N.restrict-7-3-0
context-restrict-7-4 : (p : E.A.EdgePermit C.q7 e13) → M.move-7-1 (E.A.restrict false C.q7 e13 p) ≡ E.A.restrict false C.q0 e02 (N.move-7-4 p)
context-restrict-7-4 = N.restrict-7-4-0
context-restrict-7-5 : (p : E.A.EdgePermit C.q7 e23) → M.move-7-3 (E.A.restrict true C.q7 e23 p) ≡ E.A.restrict false C.q0 e23 (N.move-7-5 p)
context-restrict-7-5 = N.restrict-7-5-1
left-selector : Selector
left-selector e = false
