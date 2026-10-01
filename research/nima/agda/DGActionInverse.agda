{-# OPTIONS --safe --cubical --guardedness #-}
module DGActionInverse where

open import Cubical.Foundations.Prelude
open import DGFrameUpdates
open import DGCertificateTransport
open import DGActionComposition

record InverseAlgebra : Type₁ where
  field
    actions : ActionAlgebra
  open ActionAlgebra actions public
  field
    unit02 : (w : D2) → m02 one w ≡ w
    right-neg2 : (k : D2) (d : D0) → m20 (neg2 k) d ≡ neg2 (m20 k d)
    add-neg-cancel : (w k : D2) → add2 (add2 w k) (neg2 k) ≡ w

module Inversion (A : InverseAlgebra) where
  open InverseAlgebra A
  module U = Updates frame-algebra
  module Kt = Certificates certificates
  module Comp = Composition actions
  open U using (Frame; Request; active)
  open Frame
  open Request
  open Comp using (SameData)
  open SameData

  commute-inverse : (g gi x : D0)
    → m00 gi g ≡ one → m00 g gi ≡ one
    → m00 g x ≡ m00 x g
    → m00 gi x ≡ m00 x gi
  commute-inverse g gi x li ri p =
    sym (unit-right (m00 gi x))
    ∙ cong (m00 (m00 gi x)) (sym ri)
    ∙ sym (assoc (m00 gi x) g gi)
    ∙ cong (λ y → m00 y gi) (assoc gi x g)
    ∙ cong (λ y → m00 (m00 gi y) gi) (sym p)
    ∙ cong (λ y → m00 y gi) (sym (assoc gi g x))
    ∙ cong (λ y → m00 (m00 y x) gi) li
    ∙ cong (λ y → m00 y gi) (unit-left x)

  inverse : (f : Frame) (q : Request f) → Request (active f q)
  g (inverse f q) = gi q
  gi (inverse f q) = g q
  K (inverse f q) = Kt.inverse-K (gi q) (K q)
  inverse-left (inverse f q) = inverse-right q
  inverse-right (inverse f q) = inverse-left q
  protects-unit (inverse f q) = commute-inverse (g q) (gi q) (delta1 (v f))
    (inverse-left q) (inverse-right q) (protects-unit q)
  certificate (inverse f q) = Kt.inverse-certificate (g q) (gi q) (v f) (K q)
    (inverse-left q) (inverse-right q) (certificate q)

  left-undo : (g gi x : D0) → m00 gi g ≡ one → m00 gi (m00 g x) ≡ x
  left-undo g gi x p = sym (assoc gi g x) ∙ cong (λ y → m00 y x) p ∙ unit-left x

  undo-W : (f : Frame) (q : Request f)
    → W (active (active f q) (inverse f q)) ≡ W f
  undo-W f q =
    cong₂ add2
      (left-add2 (gi q) (m02 (g q) (W f)) (m20 (K q) (d f))
       ∙ cong₂ add2
         (assoc002 (gi q) (g q) (W f)
          ∙ cong (λ x → m02 x (W f)) (inverse-left q) ∙ unit02 (W f))
         (assoc020 (gi q) (K q) (d f)))
      (right-neg2 (m20 (m02 (gi q) (K q)) (gi q)) (m00 (g q) (d f))
       ∙ cong neg2
         (assoc200 (m02 (gi q) (K q)) (gi q) (m00 (g q) (d f))
          ∙ cong (m20 (m02 (gi q) (K q))) (left-undo (g q) (gi q) (d f) (inverse-left q))))
    ∙ add-neg-cancel (W f) (m20 (m02 (gi q) (K q)) (d f))

  active-inverse : (f : Frame) (q : Request f)
    → SameData (active (active f q) (inverse f q)) f
  same-C (active-inverse f q) = left-undo (g q) (gi q) (C f) (inverse-left q)
  same-d (active-inverse f q) = left-undo (g q) (gi q) (d f) (inverse-left q)
  same-r (active-inverse f q) = assoc (r f) (gi q) (g q)
    ∙ cong (m00 (r f)) (inverse-left q) ∙ unit-right (r f)
  same-u (active-inverse f q) = refl
  same-v (active-inverse f q) = refl
  same-W (active-inverse f q) = undo-W f q
