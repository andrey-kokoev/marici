{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyTripleNaturality where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import RamseySingleFrameFaces using (c0; m0; c1; m1)
open import RamseyNativeEdgeAttachments using (e01; e02; e03; e12; e13; e23)
open import RamseyEndpointPolicy using (Frame; base; complement; swap; side-map)
open import RamseyCommonSelection using (chart; edge-move; vertex-move)
import RamseyEdgeNaturality as N
import RamseyPermitEquivalence as M
import RamseyEdgeAttachmentsExamples as E
import RamseyEndpointFamily as H
ET VT : Frame → Frame → Frame → Type
ET a b c = E.A.S.Triple (chart a) (chart b) (chart c)
VT a b c = E.A.V.Triple (chart a) (chart b) (chart c)
edge-triple : (a b c : Frame) → ET a b c → ET (swap a) (swap b) (swap c)
edge-triple base base base (e01 , (p , (q , r))) = e01 , (N.move-0-0 p , (N.move-0-0 q , N.move-0-0 r))
edge-triple base base base (e02 , (p , (q , r))) = e13 , (N.move-0-1 p , (N.move-0-1 q , N.move-0-1 r))
edge-triple base base base (e03 , (p , (q , r))) = e12 , (N.move-0-2 p , (N.move-0-2 q , N.move-0-2 r))
edge-triple base base base (e12 , (p , (q , r))) = e03 , (N.move-0-3 p , (N.move-0-3 q , N.move-0-3 r))
edge-triple base base base (e13 , (p , (q , r))) = e02 , (N.move-0-4 p , (N.move-0-4 q , N.move-0-4 r))
edge-triple base base base (e23 , (p , (q , r))) = e23 , (N.move-0-5 p , (N.move-0-5 q , N.move-0-5 r))
edge-triple base base complement (e01 , (p , (q , r))) = e01 , (N.move-0-0 p , (N.move-0-0 q , N.move-7-0 r))
edge-triple base base complement (e02 , (p , (q , r))) = e13 , (N.move-0-1 p , (N.move-0-1 q , N.move-7-1 r))
edge-triple base base complement (e03 , (p , (q , r))) = e12 , (N.move-0-2 p , (N.move-0-2 q , N.move-7-2 r))
edge-triple base base complement (e12 , (p , (q , r))) = e03 , (N.move-0-3 p , (N.move-0-3 q , N.move-7-3 r))
edge-triple base base complement (e13 , (p , (q , r))) = e02 , (N.move-0-4 p , (N.move-0-4 q , N.move-7-4 r))
edge-triple base base complement (e23 , (p , (q , r))) = e23 , (N.move-0-5 p , (N.move-0-5 q , N.move-7-5 r))
edge-triple base complement base (e01 , (p , (q , r))) = e01 , (N.move-0-0 p , (N.move-7-0 q , N.move-0-0 r))
edge-triple base complement base (e02 , (p , (q , r))) = e13 , (N.move-0-1 p , (N.move-7-1 q , N.move-0-1 r))
edge-triple base complement base (e03 , (p , (q , r))) = e12 , (N.move-0-2 p , (N.move-7-2 q , N.move-0-2 r))
edge-triple base complement base (e12 , (p , (q , r))) = e03 , (N.move-0-3 p , (N.move-7-3 q , N.move-0-3 r))
edge-triple base complement base (e13 , (p , (q , r))) = e02 , (N.move-0-4 p , (N.move-7-4 q , N.move-0-4 r))
edge-triple base complement base (e23 , (p , (q , r))) = e23 , (N.move-0-5 p , (N.move-7-5 q , N.move-0-5 r))
edge-triple base complement complement (e01 , (p , (q , r))) = e01 , (N.move-0-0 p , (N.move-7-0 q , N.move-7-0 r))
edge-triple base complement complement (e02 , (p , (q , r))) = e13 , (N.move-0-1 p , (N.move-7-1 q , N.move-7-1 r))
edge-triple base complement complement (e03 , (p , (q , r))) = e12 , (N.move-0-2 p , (N.move-7-2 q , N.move-7-2 r))
edge-triple base complement complement (e12 , (p , (q , r))) = e03 , (N.move-0-3 p , (N.move-7-3 q , N.move-7-3 r))
edge-triple base complement complement (e13 , (p , (q , r))) = e02 , (N.move-0-4 p , (N.move-7-4 q , N.move-7-4 r))
edge-triple base complement complement (e23 , (p , (q , r))) = e23 , (N.move-0-5 p , (N.move-7-5 q , N.move-7-5 r))
edge-triple complement base base (e01 , (p , (q , r))) = e01 , (N.move-7-0 p , (N.move-0-0 q , N.move-0-0 r))
edge-triple complement base base (e02 , (p , (q , r))) = e13 , (N.move-7-1 p , (N.move-0-1 q , N.move-0-1 r))
edge-triple complement base base (e03 , (p , (q , r))) = e12 , (N.move-7-2 p , (N.move-0-2 q , N.move-0-2 r))
edge-triple complement base base (e12 , (p , (q , r))) = e03 , (N.move-7-3 p , (N.move-0-3 q , N.move-0-3 r))
edge-triple complement base base (e13 , (p , (q , r))) = e02 , (N.move-7-4 p , (N.move-0-4 q , N.move-0-4 r))
edge-triple complement base base (e23 , (p , (q , r))) = e23 , (N.move-7-5 p , (N.move-0-5 q , N.move-0-5 r))
edge-triple complement base complement (e01 , (p , (q , r))) = e01 , (N.move-7-0 p , (N.move-0-0 q , N.move-7-0 r))
edge-triple complement base complement (e02 , (p , (q , r))) = e13 , (N.move-7-1 p , (N.move-0-1 q , N.move-7-1 r))
edge-triple complement base complement (e03 , (p , (q , r))) = e12 , (N.move-7-2 p , (N.move-0-2 q , N.move-7-2 r))
edge-triple complement base complement (e12 , (p , (q , r))) = e03 , (N.move-7-3 p , (N.move-0-3 q , N.move-7-3 r))
edge-triple complement base complement (e13 , (p , (q , r))) = e02 , (N.move-7-4 p , (N.move-0-4 q , N.move-7-4 r))
edge-triple complement base complement (e23 , (p , (q , r))) = e23 , (N.move-7-5 p , (N.move-0-5 q , N.move-7-5 r))
edge-triple complement complement base (e01 , (p , (q , r))) = e01 , (N.move-7-0 p , (N.move-7-0 q , N.move-0-0 r))
edge-triple complement complement base (e02 , (p , (q , r))) = e13 , (N.move-7-1 p , (N.move-7-1 q , N.move-0-1 r))
edge-triple complement complement base (e03 , (p , (q , r))) = e12 , (N.move-7-2 p , (N.move-7-2 q , N.move-0-2 r))
edge-triple complement complement base (e12 , (p , (q , r))) = e03 , (N.move-7-3 p , (N.move-7-3 q , N.move-0-3 r))
edge-triple complement complement base (e13 , (p , (q , r))) = e02 , (N.move-7-4 p , (N.move-7-4 q , N.move-0-4 r))
edge-triple complement complement base (e23 , (p , (q , r))) = e23 , (N.move-7-5 p , (N.move-7-5 q , N.move-0-5 r))
edge-triple complement complement complement (e01 , (p , (q , r))) = e01 , (N.move-7-0 p , (N.move-7-0 q , N.move-7-0 r))
edge-triple complement complement complement (e02 , (p , (q , r))) = e13 , (N.move-7-1 p , (N.move-7-1 q , N.move-7-1 r))
edge-triple complement complement complement (e03 , (p , (q , r))) = e12 , (N.move-7-2 p , (N.move-7-2 q , N.move-7-2 r))
edge-triple complement complement complement (e12 , (p , (q , r))) = e03 , (N.move-7-3 p , (N.move-7-3 q , N.move-7-3 r))
edge-triple complement complement complement (e13 , (p , (q , r))) = e02 , (N.move-7-4 p , (N.move-7-4 q , N.move-7-4 r))
edge-triple complement complement complement (e23 , (p , (q , r))) = e23 , (N.move-7-5 p , (N.move-7-5 q , N.move-7-5 r))
vertex-triple : (a b c : Frame) → VT a b c → VT (swap a) (swap b) (swap c)
vertex-triple base base base (c0 , (p , (q , r))) = m0 , (M.move-0-0 p , (M.move-0-0 q , M.move-0-0 r))
vertex-triple base base base (m0 , (p , (q , r))) = c0 , (M.move-0-1 p , (M.move-0-1 q , M.move-0-1 r))
vertex-triple base base base (c1 , (p , (q , r))) = m1 , (M.move-0-2 p , (M.move-0-2 q , M.move-0-2 r))
vertex-triple base base base (m1 , (p , (q , r))) = c1 , (M.move-0-3 p , (M.move-0-3 q , M.move-0-3 r))
vertex-triple base base complement (c0 , (p , (q , r))) = m0 , (M.move-0-0 p , (M.move-0-0 q , M.move-7-0 r))
vertex-triple base base complement (m0 , (p , (q , r))) = c0 , (M.move-0-1 p , (M.move-0-1 q , M.move-7-1 r))
vertex-triple base base complement (c1 , (p , (q , r))) = m1 , (M.move-0-2 p , (M.move-0-2 q , M.move-7-2 r))
vertex-triple base base complement (m1 , (p , (q , r))) = c1 , (M.move-0-3 p , (M.move-0-3 q , M.move-7-3 r))
vertex-triple base complement base (c0 , (p , (q , r))) = m0 , (M.move-0-0 p , (M.move-7-0 q , M.move-0-0 r))
vertex-triple base complement base (m0 , (p , (q , r))) = c0 , (M.move-0-1 p , (M.move-7-1 q , M.move-0-1 r))
vertex-triple base complement base (c1 , (p , (q , r))) = m1 , (M.move-0-2 p , (M.move-7-2 q , M.move-0-2 r))
vertex-triple base complement base (m1 , (p , (q , r))) = c1 , (M.move-0-3 p , (M.move-7-3 q , M.move-0-3 r))
vertex-triple base complement complement (c0 , (p , (q , r))) = m0 , (M.move-0-0 p , (M.move-7-0 q , M.move-7-0 r))
vertex-triple base complement complement (m0 , (p , (q , r))) = c0 , (M.move-0-1 p , (M.move-7-1 q , M.move-7-1 r))
vertex-triple base complement complement (c1 , (p , (q , r))) = m1 , (M.move-0-2 p , (M.move-7-2 q , M.move-7-2 r))
vertex-triple base complement complement (m1 , (p , (q , r))) = c1 , (M.move-0-3 p , (M.move-7-3 q , M.move-7-3 r))
vertex-triple complement base base (c0 , (p , (q , r))) = m0 , (M.move-7-0 p , (M.move-0-0 q , M.move-0-0 r))
vertex-triple complement base base (m0 , (p , (q , r))) = c0 , (M.move-7-1 p , (M.move-0-1 q , M.move-0-1 r))
vertex-triple complement base base (c1 , (p , (q , r))) = m1 , (M.move-7-2 p , (M.move-0-2 q , M.move-0-2 r))
vertex-triple complement base base (m1 , (p , (q , r))) = c1 , (M.move-7-3 p , (M.move-0-3 q , M.move-0-3 r))
vertex-triple complement base complement (c0 , (p , (q , r))) = m0 , (M.move-7-0 p , (M.move-0-0 q , M.move-7-0 r))
vertex-triple complement base complement (m0 , (p , (q , r))) = c0 , (M.move-7-1 p , (M.move-0-1 q , M.move-7-1 r))
vertex-triple complement base complement (c1 , (p , (q , r))) = m1 , (M.move-7-2 p , (M.move-0-2 q , M.move-7-2 r))
vertex-triple complement base complement (m1 , (p , (q , r))) = c1 , (M.move-7-3 p , (M.move-0-3 q , M.move-7-3 r))
vertex-triple complement complement base (c0 , (p , (q , r))) = m0 , (M.move-7-0 p , (M.move-7-0 q , M.move-0-0 r))
vertex-triple complement complement base (m0 , (p , (q , r))) = c0 , (M.move-7-1 p , (M.move-7-1 q , M.move-0-1 r))
vertex-triple complement complement base (c1 , (p , (q , r))) = m1 , (M.move-7-2 p , (M.move-7-2 q , M.move-0-2 r))
vertex-triple complement complement base (m1 , (p , (q , r))) = c1 , (M.move-7-3 p , (M.move-7-3 q , M.move-0-3 r))
vertex-triple complement complement complement (c0 , (p , (q , r))) = m0 , (M.move-7-0 p , (M.move-7-0 q , M.move-7-0 r))
vertex-triple complement complement complement (m0 , (p , (q , r))) = c0 , (M.move-7-1 p , (M.move-7-1 q , M.move-7-1 r))
vertex-triple complement complement complement (c1 , (p , (q , r))) = m1 , (M.move-7-2 p , (M.move-7-2 q , M.move-7-2 r))
vertex-triple complement complement complement (m1 , (p , (q , r))) = c1 , (M.move-7-3 p , (M.move-7-3 q , M.move-7-3 r))
edge-ab : (a b c : Frame) → ET a b c → E.A.S.Common (chart a) (chart b)
edge-ab a b c t = E.A.S.ab-index {a = chart a} {b = chart b} {c = chart c} t
edge-projection-ab : (a b c : Frame) (t : ET a b c) → edge-move a b (edge-ab a b c t) ≡ edge-ab (swap a) (swap b) (swap c) (edge-triple a b c t)
edge-projection-ab base base base (e01 , (p , (q , r))) = refl
edge-projection-ab base base base (e02 , (p , (q , r))) = refl
edge-projection-ab base base base (e03 , (p , (q , r))) = refl
edge-projection-ab base base base (e12 , (p , (q , r))) = refl
edge-projection-ab base base base (e13 , (p , (q , r))) = refl
edge-projection-ab base base base (e23 , (p , (q , r))) = refl
edge-projection-ab base base complement (e01 , (p , (q , r))) = refl
edge-projection-ab base base complement (e02 , (p , (q , r))) = refl
edge-projection-ab base base complement (e03 , (p , (q , r))) = refl
edge-projection-ab base base complement (e12 , (p , (q , r))) = refl
edge-projection-ab base base complement (e13 , (p , (q , r))) = refl
edge-projection-ab base base complement (e23 , (p , (q , r))) = refl
edge-projection-ab base complement base (e01 , (p , (q , r))) = refl
edge-projection-ab base complement base (e02 , (p , (q , r))) = refl
edge-projection-ab base complement base (e03 , (p , (q , r))) = refl
edge-projection-ab base complement base (e12 , (p , (q , r))) = refl
edge-projection-ab base complement base (e13 , (p , (q , r))) = refl
edge-projection-ab base complement base (e23 , (p , (q , r))) = refl
edge-projection-ab base complement complement (e01 , (p , (q , r))) = refl
edge-projection-ab base complement complement (e02 , (p , (q , r))) = refl
edge-projection-ab base complement complement (e03 , (p , (q , r))) = refl
edge-projection-ab base complement complement (e12 , (p , (q , r))) = refl
edge-projection-ab base complement complement (e13 , (p , (q , r))) = refl
edge-projection-ab base complement complement (e23 , (p , (q , r))) = refl
edge-projection-ab complement base base (e01 , (p , (q , r))) = refl
edge-projection-ab complement base base (e02 , (p , (q , r))) = refl
edge-projection-ab complement base base (e03 , (p , (q , r))) = refl
edge-projection-ab complement base base (e12 , (p , (q , r))) = refl
edge-projection-ab complement base base (e13 , (p , (q , r))) = refl
edge-projection-ab complement base base (e23 , (p , (q , r))) = refl
edge-projection-ab complement base complement (e01 , (p , (q , r))) = refl
edge-projection-ab complement base complement (e02 , (p , (q , r))) = refl
edge-projection-ab complement base complement (e03 , (p , (q , r))) = refl
edge-projection-ab complement base complement (e12 , (p , (q , r))) = refl
edge-projection-ab complement base complement (e13 , (p , (q , r))) = refl
edge-projection-ab complement base complement (e23 , (p , (q , r))) = refl
edge-projection-ab complement complement base (e01 , (p , (q , r))) = refl
edge-projection-ab complement complement base (e02 , (p , (q , r))) = refl
edge-projection-ab complement complement base (e03 , (p , (q , r))) = refl
edge-projection-ab complement complement base (e12 , (p , (q , r))) = refl
edge-projection-ab complement complement base (e13 , (p , (q , r))) = refl
edge-projection-ab complement complement base (e23 , (p , (q , r))) = refl
edge-projection-ab complement complement complement (e01 , (p , (q , r))) = refl
edge-projection-ab complement complement complement (e02 , (p , (q , r))) = refl
edge-projection-ab complement complement complement (e03 , (p , (q , r))) = refl
edge-projection-ab complement complement complement (e12 , (p , (q , r))) = refl
edge-projection-ab complement complement complement (e13 , (p , (q , r))) = refl
edge-projection-ab complement complement complement (e23 , (p , (q , r))) = refl
edge-bc : (a b c : Frame) → ET a b c → E.A.S.Common (chart b) (chart c)
edge-bc a b c t = E.A.S.bc-index {a = chart a} {b = chart b} {c = chart c} t
edge-projection-bc : (a b c : Frame) (t : ET a b c) → edge-move b c (edge-bc a b c t) ≡ edge-bc (swap a) (swap b) (swap c) (edge-triple a b c t)
edge-projection-bc base base base (e01 , (p , (q , r))) = refl
edge-projection-bc base base base (e02 , (p , (q , r))) = refl
edge-projection-bc base base base (e03 , (p , (q , r))) = refl
edge-projection-bc base base base (e12 , (p , (q , r))) = refl
edge-projection-bc base base base (e13 , (p , (q , r))) = refl
edge-projection-bc base base base (e23 , (p , (q , r))) = refl
edge-projection-bc base base complement (e01 , (p , (q , r))) = refl
edge-projection-bc base base complement (e02 , (p , (q , r))) = refl
edge-projection-bc base base complement (e03 , (p , (q , r))) = refl
edge-projection-bc base base complement (e12 , (p , (q , r))) = refl
edge-projection-bc base base complement (e13 , (p , (q , r))) = refl
edge-projection-bc base base complement (e23 , (p , (q , r))) = refl
edge-projection-bc base complement base (e01 , (p , (q , r))) = refl
edge-projection-bc base complement base (e02 , (p , (q , r))) = refl
edge-projection-bc base complement base (e03 , (p , (q , r))) = refl
edge-projection-bc base complement base (e12 , (p , (q , r))) = refl
edge-projection-bc base complement base (e13 , (p , (q , r))) = refl
edge-projection-bc base complement base (e23 , (p , (q , r))) = refl
edge-projection-bc base complement complement (e01 , (p , (q , r))) = refl
edge-projection-bc base complement complement (e02 , (p , (q , r))) = refl
edge-projection-bc base complement complement (e03 , (p , (q , r))) = refl
edge-projection-bc base complement complement (e12 , (p , (q , r))) = refl
edge-projection-bc base complement complement (e13 , (p , (q , r))) = refl
edge-projection-bc base complement complement (e23 , (p , (q , r))) = refl
edge-projection-bc complement base base (e01 , (p , (q , r))) = refl
edge-projection-bc complement base base (e02 , (p , (q , r))) = refl
edge-projection-bc complement base base (e03 , (p , (q , r))) = refl
edge-projection-bc complement base base (e12 , (p , (q , r))) = refl
edge-projection-bc complement base base (e13 , (p , (q , r))) = refl
edge-projection-bc complement base base (e23 , (p , (q , r))) = refl
edge-projection-bc complement base complement (e01 , (p , (q , r))) = refl
edge-projection-bc complement base complement (e02 , (p , (q , r))) = refl
edge-projection-bc complement base complement (e03 , (p , (q , r))) = refl
edge-projection-bc complement base complement (e12 , (p , (q , r))) = refl
edge-projection-bc complement base complement (e13 , (p , (q , r))) = refl
edge-projection-bc complement base complement (e23 , (p , (q , r))) = refl
edge-projection-bc complement complement base (e01 , (p , (q , r))) = refl
edge-projection-bc complement complement base (e02 , (p , (q , r))) = refl
edge-projection-bc complement complement base (e03 , (p , (q , r))) = refl
edge-projection-bc complement complement base (e12 , (p , (q , r))) = refl
edge-projection-bc complement complement base (e13 , (p , (q , r))) = refl
edge-projection-bc complement complement base (e23 , (p , (q , r))) = refl
edge-projection-bc complement complement complement (e01 , (p , (q , r))) = refl
edge-projection-bc complement complement complement (e02 , (p , (q , r))) = refl
edge-projection-bc complement complement complement (e03 , (p , (q , r))) = refl
edge-projection-bc complement complement complement (e12 , (p , (q , r))) = refl
edge-projection-bc complement complement complement (e13 , (p , (q , r))) = refl
edge-projection-bc complement complement complement (e23 , (p , (q , r))) = refl
edge-ac : (a b c : Frame) → ET a b c → E.A.S.Common (chart a) (chart c)
edge-ac a b c t = E.A.S.ac-index {a = chart a} {b = chart b} {c = chart c} t
edge-projection-ac : (a b c : Frame) (t : ET a b c) → edge-move a c (edge-ac a b c t) ≡ edge-ac (swap a) (swap b) (swap c) (edge-triple a b c t)
edge-projection-ac base base base (e01 , (p , (q , r))) = refl
edge-projection-ac base base base (e02 , (p , (q , r))) = refl
edge-projection-ac base base base (e03 , (p , (q , r))) = refl
edge-projection-ac base base base (e12 , (p , (q , r))) = refl
edge-projection-ac base base base (e13 , (p , (q , r))) = refl
edge-projection-ac base base base (e23 , (p , (q , r))) = refl
edge-projection-ac base base complement (e01 , (p , (q , r))) = refl
edge-projection-ac base base complement (e02 , (p , (q , r))) = refl
edge-projection-ac base base complement (e03 , (p , (q , r))) = refl
edge-projection-ac base base complement (e12 , (p , (q , r))) = refl
edge-projection-ac base base complement (e13 , (p , (q , r))) = refl
edge-projection-ac base base complement (e23 , (p , (q , r))) = refl
edge-projection-ac base complement base (e01 , (p , (q , r))) = refl
edge-projection-ac base complement base (e02 , (p , (q , r))) = refl
edge-projection-ac base complement base (e03 , (p , (q , r))) = refl
edge-projection-ac base complement base (e12 , (p , (q , r))) = refl
edge-projection-ac base complement base (e13 , (p , (q , r))) = refl
edge-projection-ac base complement base (e23 , (p , (q , r))) = refl
edge-projection-ac base complement complement (e01 , (p , (q , r))) = refl
edge-projection-ac base complement complement (e02 , (p , (q , r))) = refl
edge-projection-ac base complement complement (e03 , (p , (q , r))) = refl
edge-projection-ac base complement complement (e12 , (p , (q , r))) = refl
edge-projection-ac base complement complement (e13 , (p , (q , r))) = refl
edge-projection-ac base complement complement (e23 , (p , (q , r))) = refl
edge-projection-ac complement base base (e01 , (p , (q , r))) = refl
edge-projection-ac complement base base (e02 , (p , (q , r))) = refl
edge-projection-ac complement base base (e03 , (p , (q , r))) = refl
edge-projection-ac complement base base (e12 , (p , (q , r))) = refl
edge-projection-ac complement base base (e13 , (p , (q , r))) = refl
edge-projection-ac complement base base (e23 , (p , (q , r))) = refl
edge-projection-ac complement base complement (e01 , (p , (q , r))) = refl
edge-projection-ac complement base complement (e02 , (p , (q , r))) = refl
edge-projection-ac complement base complement (e03 , (p , (q , r))) = refl
edge-projection-ac complement base complement (e12 , (p , (q , r))) = refl
edge-projection-ac complement base complement (e13 , (p , (q , r))) = refl
edge-projection-ac complement base complement (e23 , (p , (q , r))) = refl
edge-projection-ac complement complement base (e01 , (p , (q , r))) = refl
edge-projection-ac complement complement base (e02 , (p , (q , r))) = refl
edge-projection-ac complement complement base (e03 , (p , (q , r))) = refl
edge-projection-ac complement complement base (e12 , (p , (q , r))) = refl
edge-projection-ac complement complement base (e13 , (p , (q , r))) = refl
edge-projection-ac complement complement base (e23 , (p , (q , r))) = refl
edge-projection-ac complement complement complement (e01 , (p , (q , r))) = refl
edge-projection-ac complement complement complement (e02 , (p , (q , r))) = refl
edge-projection-ac complement complement complement (e03 , (p , (q , r))) = refl
edge-projection-ac complement complement complement (e12 , (p , (q , r))) = refl
edge-projection-ac complement complement complement (e13 , (p , (q , r))) = refl
edge-projection-ac complement complement complement (e23 , (p , (q , r))) = refl
vertex-ab : (a b c : Frame) → VT a b c → E.A.V.Common (chart a) (chart b)
vertex-ab a b c t = E.A.V.ab-index {a = chart a} {b = chart b} {c = chart c} t
vertex-projection-ab : (a b c : Frame) (t : VT a b c) → vertex-move a b (vertex-ab a b c t) ≡ vertex-ab (swap a) (swap b) (swap c) (vertex-triple a b c t)
vertex-projection-ab base base base (c0 , (p , (q , r))) = refl
vertex-projection-ab base base base (m0 , (p , (q , r))) = refl
vertex-projection-ab base base base (c1 , (p , (q , r))) = refl
vertex-projection-ab base base base (m1 , (p , (q , r))) = refl
vertex-projection-ab base base complement (c0 , (p , (q , r))) = refl
vertex-projection-ab base base complement (m0 , (p , (q , r))) = refl
vertex-projection-ab base base complement (c1 , (p , (q , r))) = refl
vertex-projection-ab base base complement (m1 , (p , (q , r))) = refl
vertex-projection-ab base complement base (c0 , (p , (q , r))) = refl
vertex-projection-ab base complement base (m0 , (p , (q , r))) = refl
vertex-projection-ab base complement base (c1 , (p , (q , r))) = refl
vertex-projection-ab base complement base (m1 , (p , (q , r))) = refl
vertex-projection-ab base complement complement (c0 , (p , (q , r))) = refl
vertex-projection-ab base complement complement (m0 , (p , (q , r))) = refl
vertex-projection-ab base complement complement (c1 , (p , (q , r))) = refl
vertex-projection-ab base complement complement (m1 , (p , (q , r))) = refl
vertex-projection-ab complement base base (c0 , (p , (q , r))) = refl
vertex-projection-ab complement base base (m0 , (p , (q , r))) = refl
vertex-projection-ab complement base base (c1 , (p , (q , r))) = refl
vertex-projection-ab complement base base (m1 , (p , (q , r))) = refl
vertex-projection-ab complement base complement (c0 , (p , (q , r))) = refl
vertex-projection-ab complement base complement (m0 , (p , (q , r))) = refl
vertex-projection-ab complement base complement (c1 , (p , (q , r))) = refl
vertex-projection-ab complement base complement (m1 , (p , (q , r))) = refl
vertex-projection-ab complement complement base (c0 , (p , (q , r))) = refl
vertex-projection-ab complement complement base (m0 , (p , (q , r))) = refl
vertex-projection-ab complement complement base (c1 , (p , (q , r))) = refl
vertex-projection-ab complement complement base (m1 , (p , (q , r))) = refl
vertex-projection-ab complement complement complement (c0 , (p , (q , r))) = refl
vertex-projection-ab complement complement complement (m0 , (p , (q , r))) = refl
vertex-projection-ab complement complement complement (c1 , (p , (q , r))) = refl
vertex-projection-ab complement complement complement (m1 , (p , (q , r))) = refl
vertex-bc : (a b c : Frame) → VT a b c → E.A.V.Common (chart b) (chart c)
vertex-bc a b c t = E.A.V.bc-index {a = chart a} {b = chart b} {c = chart c} t
vertex-projection-bc : (a b c : Frame) (t : VT a b c) → vertex-move b c (vertex-bc a b c t) ≡ vertex-bc (swap a) (swap b) (swap c) (vertex-triple a b c t)
vertex-projection-bc base base base (c0 , (p , (q , r))) = refl
vertex-projection-bc base base base (m0 , (p , (q , r))) = refl
vertex-projection-bc base base base (c1 , (p , (q , r))) = refl
vertex-projection-bc base base base (m1 , (p , (q , r))) = refl
vertex-projection-bc base base complement (c0 , (p , (q , r))) = refl
vertex-projection-bc base base complement (m0 , (p , (q , r))) = refl
vertex-projection-bc base base complement (c1 , (p , (q , r))) = refl
vertex-projection-bc base base complement (m1 , (p , (q , r))) = refl
vertex-projection-bc base complement base (c0 , (p , (q , r))) = refl
vertex-projection-bc base complement base (m0 , (p , (q , r))) = refl
vertex-projection-bc base complement base (c1 , (p , (q , r))) = refl
vertex-projection-bc base complement base (m1 , (p , (q , r))) = refl
vertex-projection-bc base complement complement (c0 , (p , (q , r))) = refl
vertex-projection-bc base complement complement (m0 , (p , (q , r))) = refl
vertex-projection-bc base complement complement (c1 , (p , (q , r))) = refl
vertex-projection-bc base complement complement (m1 , (p , (q , r))) = refl
vertex-projection-bc complement base base (c0 , (p , (q , r))) = refl
vertex-projection-bc complement base base (m0 , (p , (q , r))) = refl
vertex-projection-bc complement base base (c1 , (p , (q , r))) = refl
vertex-projection-bc complement base base (m1 , (p , (q , r))) = refl
vertex-projection-bc complement base complement (c0 , (p , (q , r))) = refl
vertex-projection-bc complement base complement (m0 , (p , (q , r))) = refl
vertex-projection-bc complement base complement (c1 , (p , (q , r))) = refl
vertex-projection-bc complement base complement (m1 , (p , (q , r))) = refl
vertex-projection-bc complement complement base (c0 , (p , (q , r))) = refl
vertex-projection-bc complement complement base (m0 , (p , (q , r))) = refl
vertex-projection-bc complement complement base (c1 , (p , (q , r))) = refl
vertex-projection-bc complement complement base (m1 , (p , (q , r))) = refl
vertex-projection-bc complement complement complement (c0 , (p , (q , r))) = refl
vertex-projection-bc complement complement complement (m0 , (p , (q , r))) = refl
vertex-projection-bc complement complement complement (c1 , (p , (q , r))) = refl
vertex-projection-bc complement complement complement (m1 , (p , (q , r))) = refl
vertex-ac : (a b c : Frame) → VT a b c → E.A.V.Common (chart a) (chart c)
vertex-ac a b c t = E.A.V.ac-index {a = chart a} {b = chart b} {c = chart c} t
vertex-projection-ac : (a b c : Frame) (t : VT a b c) → vertex-move a c (vertex-ac a b c t) ≡ vertex-ac (swap a) (swap b) (swap c) (vertex-triple a b c t)
vertex-projection-ac base base base (c0 , (p , (q , r))) = refl
vertex-projection-ac base base base (m0 , (p , (q , r))) = refl
vertex-projection-ac base base base (c1 , (p , (q , r))) = refl
vertex-projection-ac base base base (m1 , (p , (q , r))) = refl
vertex-projection-ac base base complement (c0 , (p , (q , r))) = refl
vertex-projection-ac base base complement (m0 , (p , (q , r))) = refl
vertex-projection-ac base base complement (c1 , (p , (q , r))) = refl
vertex-projection-ac base base complement (m1 , (p , (q , r))) = refl
vertex-projection-ac base complement base (c0 , (p , (q , r))) = refl
vertex-projection-ac base complement base (m0 , (p , (q , r))) = refl
vertex-projection-ac base complement base (c1 , (p , (q , r))) = refl
vertex-projection-ac base complement base (m1 , (p , (q , r))) = refl
vertex-projection-ac base complement complement (c0 , (p , (q , r))) = refl
vertex-projection-ac base complement complement (m0 , (p , (q , r))) = refl
vertex-projection-ac base complement complement (c1 , (p , (q , r))) = refl
vertex-projection-ac base complement complement (m1 , (p , (q , r))) = refl
vertex-projection-ac complement base base (c0 , (p , (q , r))) = refl
vertex-projection-ac complement base base (m0 , (p , (q , r))) = refl
vertex-projection-ac complement base base (c1 , (p , (q , r))) = refl
vertex-projection-ac complement base base (m1 , (p , (q , r))) = refl
vertex-projection-ac complement base complement (c0 , (p , (q , r))) = refl
vertex-projection-ac complement base complement (m0 , (p , (q , r))) = refl
vertex-projection-ac complement base complement (c1 , (p , (q , r))) = refl
vertex-projection-ac complement base complement (m1 , (p , (q , r))) = refl
vertex-projection-ac complement complement base (c0 , (p , (q , r))) = refl
vertex-projection-ac complement complement base (m0 , (p , (q , r))) = refl
vertex-projection-ac complement complement base (c1 , (p , (q , r))) = refl
vertex-projection-ac complement complement base (m1 , (p , (q , r))) = refl
vertex-projection-ac complement complement complement (c0 , (p , (q , r))) = refl
vertex-projection-ac complement complement complement (m0 , (p , (q , r))) = refl
vertex-projection-ac complement complement complement (c1 , (p , (q , r))) = refl
vertex-projection-ac complement complement complement (m1 , (p , (q , r))) = refl
restrict : (a b c : Frame) → ET a b c → Bool → VT a b c
restrict a b c t side = E.A.restrict-triple side {a = chart a} {b = chart b} {c = chart c} t
naturality : (a b c : Frame) (t : ET a b c) (side : Bool) → vertex-triple a b c (restrict a b c t side) ≡ restrict (swap a) (swap b) (swap c) (edge-triple a b c t) (side-map (fst t) side)
naturality base base base (e01 , (p , (q , r))) false i = m0 , (N.restrict-0-0-0 p i , (N.restrict-0-0-0 q i , N.restrict-0-0-0 r i))
naturality base base base (e01 , (p , (q , r))) true i = c0 , (N.restrict-0-0-1 p i , (N.restrict-0-0-1 q i , N.restrict-0-0-1 r i))
naturality base base base (e02 , (p , (q , r))) false i = m0 , (N.restrict-0-1-0 p i , (N.restrict-0-1-0 q i , N.restrict-0-1-0 r i))
naturality base base base (e02 , (p , (q , r))) true i = m1 , (N.restrict-0-1-1 p i , (N.restrict-0-1-1 q i , N.restrict-0-1-1 r i))
naturality base base base (e03 , (p , (q , r))) false i = m0 , (N.restrict-0-2-0 p i , (N.restrict-0-2-0 q i , N.restrict-0-2-0 r i))
naturality base base base (e03 , (p , (q , r))) true i = c1 , (N.restrict-0-2-1 p i , (N.restrict-0-2-1 q i , N.restrict-0-2-1 r i))
naturality base base base (e12 , (p , (q , r))) false i = c0 , (N.restrict-0-3-0 p i , (N.restrict-0-3-0 q i , N.restrict-0-3-0 r i))
naturality base base base (e12 , (p , (q , r))) true i = m1 , (N.restrict-0-3-1 p i , (N.restrict-0-3-1 q i , N.restrict-0-3-1 r i))
naturality base base base (e13 , (p , (q , r))) false i = c0 , (N.restrict-0-4-0 p i , (N.restrict-0-4-0 q i , N.restrict-0-4-0 r i))
naturality base base base (e13 , (p , (q , r))) true i = c1 , (N.restrict-0-4-1 p i , (N.restrict-0-4-1 q i , N.restrict-0-4-1 r i))
naturality base base base (e23 , (p , (q , r))) false i = m1 , (N.restrict-0-5-0 p i , (N.restrict-0-5-0 q i , N.restrict-0-5-0 r i))
naturality base base base (e23 , (p , (q , r))) true i = c1 , (N.restrict-0-5-1 p i , (N.restrict-0-5-1 q i , N.restrict-0-5-1 r i))
naturality base base complement (e01 , (p , (q , r))) false i = m0 , (N.restrict-0-0-0 p i , (N.restrict-0-0-0 q i , N.restrict-7-0-0 r i))
naturality base base complement (e01 , (p , (q , r))) true i = c0 , (N.restrict-0-0-1 p i , (N.restrict-0-0-1 q i , N.restrict-7-0-1 r i))
naturality base base complement (e02 , (p , (q , r))) false i = m0 , (N.restrict-0-1-0 p i , (N.restrict-0-1-0 q i , N.restrict-7-1-0 r i))
naturality base base complement (e02 , (p , (q , r))) true i = m1 , (N.restrict-0-1-1 p i , (N.restrict-0-1-1 q i , N.restrict-7-1-1 r i))
naturality base base complement (e03 , (p , (q , r))) false i = m0 , (N.restrict-0-2-0 p i , (N.restrict-0-2-0 q i , N.restrict-7-2-0 r i))
naturality base base complement (e03 , (p , (q , r))) true i = c1 , (N.restrict-0-2-1 p i , (N.restrict-0-2-1 q i , N.restrict-7-2-1 r i))
naturality base base complement (e12 , (p , (q , r))) false i = c0 , (N.restrict-0-3-0 p i , (N.restrict-0-3-0 q i , N.restrict-7-3-0 r i))
naturality base base complement (e12 , (p , (q , r))) true i = m1 , (N.restrict-0-3-1 p i , (N.restrict-0-3-1 q i , N.restrict-7-3-1 r i))
naturality base base complement (e13 , (p , (q , r))) false i = c0 , (N.restrict-0-4-0 p i , (N.restrict-0-4-0 q i , N.restrict-7-4-0 r i))
naturality base base complement (e13 , (p , (q , r))) true i = c1 , (N.restrict-0-4-1 p i , (N.restrict-0-4-1 q i , N.restrict-7-4-1 r i))
naturality base base complement (e23 , (p , (q , r))) false i = m1 , (N.restrict-0-5-0 p i , (N.restrict-0-5-0 q i , N.restrict-7-5-0 r i))
naturality base base complement (e23 , (p , (q , r))) true i = c1 , (N.restrict-0-5-1 p i , (N.restrict-0-5-1 q i , N.restrict-7-5-1 r i))
naturality base complement base (e01 , (p , (q , r))) false i = m0 , (N.restrict-0-0-0 p i , (N.restrict-7-0-0 q i , N.restrict-0-0-0 r i))
naturality base complement base (e01 , (p , (q , r))) true i = c0 , (N.restrict-0-0-1 p i , (N.restrict-7-0-1 q i , N.restrict-0-0-1 r i))
naturality base complement base (e02 , (p , (q , r))) false i = m0 , (N.restrict-0-1-0 p i , (N.restrict-7-1-0 q i , N.restrict-0-1-0 r i))
naturality base complement base (e02 , (p , (q , r))) true i = m1 , (N.restrict-0-1-1 p i , (N.restrict-7-1-1 q i , N.restrict-0-1-1 r i))
naturality base complement base (e03 , (p , (q , r))) false i = m0 , (N.restrict-0-2-0 p i , (N.restrict-7-2-0 q i , N.restrict-0-2-0 r i))
naturality base complement base (e03 , (p , (q , r))) true i = c1 , (N.restrict-0-2-1 p i , (N.restrict-7-2-1 q i , N.restrict-0-2-1 r i))
naturality base complement base (e12 , (p , (q , r))) false i = c0 , (N.restrict-0-3-0 p i , (N.restrict-7-3-0 q i , N.restrict-0-3-0 r i))
naturality base complement base (e12 , (p , (q , r))) true i = m1 , (N.restrict-0-3-1 p i , (N.restrict-7-3-1 q i , N.restrict-0-3-1 r i))
naturality base complement base (e13 , (p , (q , r))) false i = c0 , (N.restrict-0-4-0 p i , (N.restrict-7-4-0 q i , N.restrict-0-4-0 r i))
naturality base complement base (e13 , (p , (q , r))) true i = c1 , (N.restrict-0-4-1 p i , (N.restrict-7-4-1 q i , N.restrict-0-4-1 r i))
naturality base complement base (e23 , (p , (q , r))) false i = m1 , (N.restrict-0-5-0 p i , (N.restrict-7-5-0 q i , N.restrict-0-5-0 r i))
naturality base complement base (e23 , (p , (q , r))) true i = c1 , (N.restrict-0-5-1 p i , (N.restrict-7-5-1 q i , N.restrict-0-5-1 r i))
naturality base complement complement (e01 , (p , (q , r))) false i = m0 , (N.restrict-0-0-0 p i , (N.restrict-7-0-0 q i , N.restrict-7-0-0 r i))
naturality base complement complement (e01 , (p , (q , r))) true i = c0 , (N.restrict-0-0-1 p i , (N.restrict-7-0-1 q i , N.restrict-7-0-1 r i))
naturality base complement complement (e02 , (p , (q , r))) false i = m0 , (N.restrict-0-1-0 p i , (N.restrict-7-1-0 q i , N.restrict-7-1-0 r i))
naturality base complement complement (e02 , (p , (q , r))) true i = m1 , (N.restrict-0-1-1 p i , (N.restrict-7-1-1 q i , N.restrict-7-1-1 r i))
naturality base complement complement (e03 , (p , (q , r))) false i = m0 , (N.restrict-0-2-0 p i , (N.restrict-7-2-0 q i , N.restrict-7-2-0 r i))
naturality base complement complement (e03 , (p , (q , r))) true i = c1 , (N.restrict-0-2-1 p i , (N.restrict-7-2-1 q i , N.restrict-7-2-1 r i))
naturality base complement complement (e12 , (p , (q , r))) false i = c0 , (N.restrict-0-3-0 p i , (N.restrict-7-3-0 q i , N.restrict-7-3-0 r i))
naturality base complement complement (e12 , (p , (q , r))) true i = m1 , (N.restrict-0-3-1 p i , (N.restrict-7-3-1 q i , N.restrict-7-3-1 r i))
naturality base complement complement (e13 , (p , (q , r))) false i = c0 , (N.restrict-0-4-0 p i , (N.restrict-7-4-0 q i , N.restrict-7-4-0 r i))
naturality base complement complement (e13 , (p , (q , r))) true i = c1 , (N.restrict-0-4-1 p i , (N.restrict-7-4-1 q i , N.restrict-7-4-1 r i))
naturality base complement complement (e23 , (p , (q , r))) false i = m1 , (N.restrict-0-5-0 p i , (N.restrict-7-5-0 q i , N.restrict-7-5-0 r i))
naturality base complement complement (e23 , (p , (q , r))) true i = c1 , (N.restrict-0-5-1 p i , (N.restrict-7-5-1 q i , N.restrict-7-5-1 r i))
naturality complement base base (e01 , (p , (q , r))) false i = m0 , (N.restrict-7-0-0 p i , (N.restrict-0-0-0 q i , N.restrict-0-0-0 r i))
naturality complement base base (e01 , (p , (q , r))) true i = c0 , (N.restrict-7-0-1 p i , (N.restrict-0-0-1 q i , N.restrict-0-0-1 r i))
naturality complement base base (e02 , (p , (q , r))) false i = m0 , (N.restrict-7-1-0 p i , (N.restrict-0-1-0 q i , N.restrict-0-1-0 r i))
naturality complement base base (e02 , (p , (q , r))) true i = m1 , (N.restrict-7-1-1 p i , (N.restrict-0-1-1 q i , N.restrict-0-1-1 r i))
naturality complement base base (e03 , (p , (q , r))) false i = m0 , (N.restrict-7-2-0 p i , (N.restrict-0-2-0 q i , N.restrict-0-2-0 r i))
naturality complement base base (e03 , (p , (q , r))) true i = c1 , (N.restrict-7-2-1 p i , (N.restrict-0-2-1 q i , N.restrict-0-2-1 r i))
naturality complement base base (e12 , (p , (q , r))) false i = c0 , (N.restrict-7-3-0 p i , (N.restrict-0-3-0 q i , N.restrict-0-3-0 r i))
naturality complement base base (e12 , (p , (q , r))) true i = m1 , (N.restrict-7-3-1 p i , (N.restrict-0-3-1 q i , N.restrict-0-3-1 r i))
naturality complement base base (e13 , (p , (q , r))) false i = c0 , (N.restrict-7-4-0 p i , (N.restrict-0-4-0 q i , N.restrict-0-4-0 r i))
naturality complement base base (e13 , (p , (q , r))) true i = c1 , (N.restrict-7-4-1 p i , (N.restrict-0-4-1 q i , N.restrict-0-4-1 r i))
naturality complement base base (e23 , (p , (q , r))) false i = m1 , (N.restrict-7-5-0 p i , (N.restrict-0-5-0 q i , N.restrict-0-5-0 r i))
naturality complement base base (e23 , (p , (q , r))) true i = c1 , (N.restrict-7-5-1 p i , (N.restrict-0-5-1 q i , N.restrict-0-5-1 r i))
naturality complement base complement (e01 , (p , (q , r))) false i = m0 , (N.restrict-7-0-0 p i , (N.restrict-0-0-0 q i , N.restrict-7-0-0 r i))
naturality complement base complement (e01 , (p , (q , r))) true i = c0 , (N.restrict-7-0-1 p i , (N.restrict-0-0-1 q i , N.restrict-7-0-1 r i))
naturality complement base complement (e02 , (p , (q , r))) false i = m0 , (N.restrict-7-1-0 p i , (N.restrict-0-1-0 q i , N.restrict-7-1-0 r i))
naturality complement base complement (e02 , (p , (q , r))) true i = m1 , (N.restrict-7-1-1 p i , (N.restrict-0-1-1 q i , N.restrict-7-1-1 r i))
naturality complement base complement (e03 , (p , (q , r))) false i = m0 , (N.restrict-7-2-0 p i , (N.restrict-0-2-0 q i , N.restrict-7-2-0 r i))
naturality complement base complement (e03 , (p , (q , r))) true i = c1 , (N.restrict-7-2-1 p i , (N.restrict-0-2-1 q i , N.restrict-7-2-1 r i))
naturality complement base complement (e12 , (p , (q , r))) false i = c0 , (N.restrict-7-3-0 p i , (N.restrict-0-3-0 q i , N.restrict-7-3-0 r i))
naturality complement base complement (e12 , (p , (q , r))) true i = m1 , (N.restrict-7-3-1 p i , (N.restrict-0-3-1 q i , N.restrict-7-3-1 r i))
naturality complement base complement (e13 , (p , (q , r))) false i = c0 , (N.restrict-7-4-0 p i , (N.restrict-0-4-0 q i , N.restrict-7-4-0 r i))
naturality complement base complement (e13 , (p , (q , r))) true i = c1 , (N.restrict-7-4-1 p i , (N.restrict-0-4-1 q i , N.restrict-7-4-1 r i))
naturality complement base complement (e23 , (p , (q , r))) false i = m1 , (N.restrict-7-5-0 p i , (N.restrict-0-5-0 q i , N.restrict-7-5-0 r i))
naturality complement base complement (e23 , (p , (q , r))) true i = c1 , (N.restrict-7-5-1 p i , (N.restrict-0-5-1 q i , N.restrict-7-5-1 r i))
naturality complement complement base (e01 , (p , (q , r))) false i = m0 , (N.restrict-7-0-0 p i , (N.restrict-7-0-0 q i , N.restrict-0-0-0 r i))
naturality complement complement base (e01 , (p , (q , r))) true i = c0 , (N.restrict-7-0-1 p i , (N.restrict-7-0-1 q i , N.restrict-0-0-1 r i))
naturality complement complement base (e02 , (p , (q , r))) false i = m0 , (N.restrict-7-1-0 p i , (N.restrict-7-1-0 q i , N.restrict-0-1-0 r i))
naturality complement complement base (e02 , (p , (q , r))) true i = m1 , (N.restrict-7-1-1 p i , (N.restrict-7-1-1 q i , N.restrict-0-1-1 r i))
naturality complement complement base (e03 , (p , (q , r))) false i = m0 , (N.restrict-7-2-0 p i , (N.restrict-7-2-0 q i , N.restrict-0-2-0 r i))
naturality complement complement base (e03 , (p , (q , r))) true i = c1 , (N.restrict-7-2-1 p i , (N.restrict-7-2-1 q i , N.restrict-0-2-1 r i))
naturality complement complement base (e12 , (p , (q , r))) false i = c0 , (N.restrict-7-3-0 p i , (N.restrict-7-3-0 q i , N.restrict-0-3-0 r i))
naturality complement complement base (e12 , (p , (q , r))) true i = m1 , (N.restrict-7-3-1 p i , (N.restrict-7-3-1 q i , N.restrict-0-3-1 r i))
naturality complement complement base (e13 , (p , (q , r))) false i = c0 , (N.restrict-7-4-0 p i , (N.restrict-7-4-0 q i , N.restrict-0-4-0 r i))
naturality complement complement base (e13 , (p , (q , r))) true i = c1 , (N.restrict-7-4-1 p i , (N.restrict-7-4-1 q i , N.restrict-0-4-1 r i))
naturality complement complement base (e23 , (p , (q , r))) false i = m1 , (N.restrict-7-5-0 p i , (N.restrict-7-5-0 q i , N.restrict-0-5-0 r i))
naturality complement complement base (e23 , (p , (q , r))) true i = c1 , (N.restrict-7-5-1 p i , (N.restrict-7-5-1 q i , N.restrict-0-5-1 r i))
naturality complement complement complement (e01 , (p , (q , r))) false i = m0 , (N.restrict-7-0-0 p i , (N.restrict-7-0-0 q i , N.restrict-7-0-0 r i))
naturality complement complement complement (e01 , (p , (q , r))) true i = c0 , (N.restrict-7-0-1 p i , (N.restrict-7-0-1 q i , N.restrict-7-0-1 r i))
naturality complement complement complement (e02 , (p , (q , r))) false i = m0 , (N.restrict-7-1-0 p i , (N.restrict-7-1-0 q i , N.restrict-7-1-0 r i))
naturality complement complement complement (e02 , (p , (q , r))) true i = m1 , (N.restrict-7-1-1 p i , (N.restrict-7-1-1 q i , N.restrict-7-1-1 r i))
naturality complement complement complement (e03 , (p , (q , r))) false i = m0 , (N.restrict-7-2-0 p i , (N.restrict-7-2-0 q i , N.restrict-7-2-0 r i))
naturality complement complement complement (e03 , (p , (q , r))) true i = c1 , (N.restrict-7-2-1 p i , (N.restrict-7-2-1 q i , N.restrict-7-2-1 r i))
naturality complement complement complement (e12 , (p , (q , r))) false i = c0 , (N.restrict-7-3-0 p i , (N.restrict-7-3-0 q i , N.restrict-7-3-0 r i))
naturality complement complement complement (e12 , (p , (q , r))) true i = m1 , (N.restrict-7-3-1 p i , (N.restrict-7-3-1 q i , N.restrict-7-3-1 r i))
naturality complement complement complement (e13 , (p , (q , r))) false i = c0 , (N.restrict-7-4-0 p i , (N.restrict-7-4-0 q i , N.restrict-7-4-0 r i))
naturality complement complement complement (e13 , (p , (q , r))) true i = c1 , (N.restrict-7-4-1 p i , (N.restrict-7-4-1 q i , N.restrict-7-4-1 r i))
naturality complement complement complement (e23 , (p , (q , r))) false i = m1 , (N.restrict-7-5-0 p i , (N.restrict-7-5-0 q i , N.restrict-7-5-0 r i))
naturality complement complement complement (e23 , (p , (q , r))) true i = c1 , (N.restrict-7-5-1 p i , (N.restrict-7-5-1 q i , N.restrict-7-5-1 r i))
restriction-ab : (a b c : Frame) (t : ET a b c) (side : Bool) → H.family a b (edge-ab a b c t) side ≡ vertex-ab a b c (restrict a b c t side)
restriction-ab a b c t side = E.A.ab-restriction-cell side (chart a) (chart b) (chart c) t
pair-route-ab : (a b c : Frame) (t : ET a b c) (side : Bool) → vertex-move a b (H.family a b (edge-ab a b c t) side) ≡ vertex-ab (swap a) (swap b) (swap c) (restrict (swap a) (swap b) (swap c) (edge-triple a b c t) (side-map (fst t) side))
pair-route-ab a b c (e , (p , (q , r))) side = H.covariance a b (edge-ab a b c (e , (p , (q , r)))) side ∙ cong (λ x → H.family (swap a) (swap b) x (side-map e side)) (edge-projection-ab a b c (e , (p , (q , r)))) ∙ restriction-ab (swap a) (swap b) (swap c) (edge-triple a b c (e , (p , (q , r)))) (side-map e side)
triple-route-ab : (a b c : Frame) (t : ET a b c) (side : Bool) → vertex-move a b (H.family a b (edge-ab a b c t) side) ≡ vertex-ab (swap a) (swap b) (swap c) (restrict (swap a) (swap b) (swap c) (edge-triple a b c t) (side-map (fst t) side))
triple-route-ab a b c t side = cong (vertex-move a b) (restriction-ab a b c t side) ∙ vertex-projection-ab a b c (restrict a b c t side) ∙ cong (vertex-ab (swap a) (swap b) (swap c)) (naturality a b c t side)
interchange-ab : (a b c : Frame) (t : ET a b c) (side : Bool) → pair-route-ab a b c t side ≡ triple-route-ab a b c t side
interchange-ab a b c t side = H.common-set (swap a) (swap b) _ _ _ _
restriction-bc : (a b c : Frame) (t : ET a b c) (side : Bool) → H.family b c (edge-bc a b c t) side ≡ vertex-bc a b c (restrict a b c t side)
restriction-bc a b c t side = E.A.bc-restriction-cell side (chart a) (chart b) (chart c) t
pair-route-bc : (a b c : Frame) (t : ET a b c) (side : Bool) → vertex-move b c (H.family b c (edge-bc a b c t) side) ≡ vertex-bc (swap a) (swap b) (swap c) (restrict (swap a) (swap b) (swap c) (edge-triple a b c t) (side-map (fst t) side))
pair-route-bc a b c (e , (p , (q , r))) side = H.covariance b c (edge-bc a b c (e , (p , (q , r)))) side ∙ cong (λ x → H.family (swap b) (swap c) x (side-map e side)) (edge-projection-bc a b c (e , (p , (q , r)))) ∙ restriction-bc (swap a) (swap b) (swap c) (edge-triple a b c (e , (p , (q , r)))) (side-map e side)
triple-route-bc : (a b c : Frame) (t : ET a b c) (side : Bool) → vertex-move b c (H.family b c (edge-bc a b c t) side) ≡ vertex-bc (swap a) (swap b) (swap c) (restrict (swap a) (swap b) (swap c) (edge-triple a b c t) (side-map (fst t) side))
triple-route-bc a b c t side = cong (vertex-move b c) (restriction-bc a b c t side) ∙ vertex-projection-bc a b c (restrict a b c t side) ∙ cong (vertex-bc (swap a) (swap b) (swap c)) (naturality a b c t side)
interchange-bc : (a b c : Frame) (t : ET a b c) (side : Bool) → pair-route-bc a b c t side ≡ triple-route-bc a b c t side
interchange-bc a b c t side = H.common-set (swap b) (swap c) _ _ _ _
restriction-ac : (a b c : Frame) (t : ET a b c) (side : Bool) → H.family a c (edge-ac a b c t) side ≡ vertex-ac a b c (restrict a b c t side)
restriction-ac a b c t side = E.A.ac-restriction-cell side (chart a) (chart b) (chart c) t
pair-route-ac : (a b c : Frame) (t : ET a b c) (side : Bool) → vertex-move a c (H.family a c (edge-ac a b c t) side) ≡ vertex-ac (swap a) (swap b) (swap c) (restrict (swap a) (swap b) (swap c) (edge-triple a b c t) (side-map (fst t) side))
pair-route-ac a b c (e , (p , (q , r))) side = H.covariance a c (edge-ac a b c (e , (p , (q , r)))) side ∙ cong (λ x → H.family (swap a) (swap c) x (side-map e side)) (edge-projection-ac a b c (e , (p , (q , r)))) ∙ restriction-ac (swap a) (swap b) (swap c) (edge-triple a b c (e , (p , (q , r)))) (side-map e side)
triple-route-ac : (a b c : Frame) (t : ET a b c) (side : Bool) → vertex-move a c (H.family a c (edge-ac a b c t) side) ≡ vertex-ac (swap a) (swap b) (swap c) (restrict (swap a) (swap b) (swap c) (edge-triple a b c t) (side-map (fst t) side))
triple-route-ac a b c t side = cong (vertex-move a c) (restriction-ac a b c t side) ∙ vertex-projection-ac a b c (restrict a b c t side) ∙ cong (vertex-ac (swap a) (swap b) (swap c)) (naturality a b c t side)
interchange-ac : (a b c : Frame) (t : ET a b c) (side : Bool) → pair-route-ac a b c t side ≡ triple-route-ac a b c t side
interchange-ac a b c t side = H.common-set (swap a) (swap c) _ _ _ _
native : (a b c : Frame) (t : ET a b c) (side : Bool) → E.A.V.R.Resolve (E.A.V.composition-package (chart a) (chart b) (chart c) (restrict a b c t side))
native a b c t side = E.A.V.composition-proof (chart a) (chart b) (chart c) (restrict a b c t side)
middle-witness : ET base base base
middle-witness = e13 , (E.att-0-0-4 , (E.att-0-2-4 , E.att-0-0-4))
middle-retained : fst (fst (snd (snd (edge-triple base base base middle-witness)))) ≡ m1
middle-retained = refl
