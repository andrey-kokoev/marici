{-# OPTIONS --safe --cubical --guardedness #-}
module DGActionComposition where

open import Cubical.Foundations.Prelude
open import DGHistoryTransport
open import DGFrameUpdates
open import DGCertificateTransport

record ActionAlgebra : Type₁ where
  field
    certificates : CertificateAlgebra
  open CertificateAlgebra certificates public
  field
    add2-assoc : (x y z : D2) → add2 (add2 x y) z ≡ add2 x (add2 y z)
    left-add2 : (h : D0) (x y : D2) → m02 h (add2 x y) ≡ add2 (m02 h x) (m02 h y)
    right-add2 : (x y : D2) (d : D0) → m20 (add2 x y) d ≡ add2 (m20 x d) (m20 y d)
    assoc002 : (h g : D0) (w : D2) → m02 h (m02 g w) ≡ m02 (m00 h g) w
    assoc020 : (h : D0) (k : D2) (d : D0) → m02 h (m20 k d) ≡ m20 (m02 h k) d
    assoc200 : (k : D2) (g d : D0) → m20 (m20 k g) d ≡ m20 k (m00 g d)

module Composition (A : ActionAlgebra) where
  open ActionAlgebra A
  module U = Updates frame-algebra
  module T = Transport fragment
  module Kt = Certificates certificates
  open U using (Frame; Request; active)
  open Frame
  open Request

  cancel-middle : (a b c d : D0) → m00 b c ≡ one
    → m00 (m00 a b) (m00 c d) ≡ m00 a d
  cancel-middle a b c d p = assoc a b (m00 c d)
    ∙ cong (m00 a) (sym (assoc b c d) ∙ cong (λ x → m00 x d) p ∙ unit-left d)

  commute-product : (h g x : D0) → m00 h x ≡ m00 x h → m00 g x ≡ m00 x g
    → m00 (m00 h g) x ≡ m00 x (m00 h g)
  commute-product h g x ph pg = assoc h g x
    ∙ cong (m00 h) pg ∙ sym (assoc h x g)
    ∙ cong (λ y → m00 y g) ph ∙ assoc x h g

  composite : (f : Frame) (q : Request f) → Request (active f q) → Request f
  g (composite f q t) = m00 (g t) (g q)
  gi (composite f q t) = m00 (gi q) (gi t)
  K (composite f q t) = Kt.composite-K (g t) (g q) (K t) (K q)
  inverse-left (composite f q t) =
    cancel-middle (gi q) (gi t) (g t) (g q) (inverse-left t) ∙ inverse-left q
  inverse-right (composite f q t) =
    cancel-middle (g t) (g q) (gi q) (gi t) (inverse-right q) ∙ inverse-right t
  protects-unit (composite f q t) = commute-product (g t) (g q) (delta1 (v f))
    (protects-unit t) (protects-unit q)
  certificate (composite f q t) = Kt.composite-certificate (g t) (g q) (v f)
    (K t) (K q) (certificate t) (certificate q)

  triangle-composition : (h g d : D0) (w kh kg : D2)
    → T.active-W h (m00 g d) (T.active-W g d w kg) kh
      ≡ T.active-W (m00 h g) d w (Kt.composite-K h g kh kg)
  triangle-composition h g d w kh kg =
    cong (λ x → add2 x (m20 kh (m00 g d))) (left-add2 h (m02 g w) (m20 kg d))
    ∙ cong₂ add2 (cong₂ add2 (assoc002 h g w) (assoc020 h kg d))
        (sym (assoc200 kh g d))
    ∙ add2-assoc (m02 (m00 h g) w) (m20 (m02 h kg) d) (m20 (m20 kh g) d)
    ∙ cong (add2 (m02 (m00 h g) w)) (sym (right-add2 (m02 h kg) (m20 kh g) d))

  -- Equality of stored data, not equality of all proof fields of Frame.
  record SameData (f j : Frame) : Type where
    field
      same-C : C f ≡ C j
      same-d : d f ≡ d j
      same-r : r f ≡ r j
      same-u : u f ≡ u j
      same-v : v f ≡ v j
      same-W : W f ≡ W j
  open SameData

  active-composition : (f : Frame) (q : Request f) (t : Request (active f q))
    → SameData (active (active f q) t) (active f (composite f q t))
  same-C (active-composition f q t) = sym (assoc (g t) (g q) (C f))
  same-d (active-composition f q t) = sym (assoc (g t) (g q) (d f))
  same-r (active-composition f q t) = assoc (r f) (gi q) (gi t)
  same-u (active-composition f q t) = refl
  same-v (active-composition f q t) = refl
  same-W (active-composition f q t) = triangle-composition (g t) (g q) (d f) (W f) (K t) (K q)
