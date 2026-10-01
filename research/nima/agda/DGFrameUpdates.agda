{-# OPTIONS --safe --cubical --guardedness #-}
module DGFrameUpdates where

open import Cubical.Foundations.Prelude
open import DGHistoryTransport

-- Common endomorphism carrier version. A concrete instance and typed A/B
-- corners are NOT supplied here. These are generic algebra laws, not updated
-- frame equations. In particular multiplication is not commutative.
record FrameAlgebra : Type₁ where
  field
    fragment : DGFragment
  open DGFragment fragment public
  field
    one : D0
    sub0 : D0 → D0 → D0
    assoc : (a b c : D0) → m00 (m00 a b) c ≡ m00 a (m00 b c)
    unit-left : (a : D0) → m00 one a ≡ a
    unit-right : (a : D0) → m00 a one ≡ a
    sub-left : (a b c : D0) → m00 a (sub0 b c) ≡ sub0 (m00 a b) (m00 a c)
    sub-right : (a b c : D0) → m00 (sub0 a b) c ≡ sub0 (m00 a c) (m00 b c)
    sub-cancel : (a b c : D0) → sub0 a c ≡ sub0 b c → a ≡ b

module Updates (A : FrameAlgebra) where
  open FrameAlgebra A
  module T = Transport fragment

  record Frame : Type where
    field
      C d r : D0
      u v : D1
      W : D2
      unit-u : delta1 u ≡ sub0 (m00 r d) one
      unit-v : delta1 v ≡ sub0 (m00 d r) one
      triangle : delta2 W ≡ T.boundary d u v
  open Frame

  record Request (f : Frame) : Type where
    field
      g gi : D0
      K : D2
      inverse-left : m00 gi g ≡ one
      inverse-right : m00 g gi ≡ one
      protects-unit : m00 g (delta1 (v f)) ≡ m00 (delta1 (v f)) g
      certificate : delta2 K ≡ T.commutator g (v f)
  open Request

  commute-return : (f : Frame) (q : Request f)
    → m00 (g q) (m00 (d f) (r f)) ≡ m00 (m00 (d f) (r f)) (g q)
  commute-return f q = sub-cancel _ _ (g q)
    (sym (cong₂ sub0 refl (unit-right (g q)))
    ∙ sym (sub-left (g q) (m00 (d f) (r f)) one)
    ∙ cong (m00 (g q)) (sym (unit-v f))
    ∙ protects-unit q
    ∙ cong (λ x → m00 x (g q)) (unit-v f)
    ∙ sub-right (m00 (d f) (r f)) one (g q)
    ∙ cong₂ sub0 refl (unit-left (g q)))

  left-product : (f : Frame) (q : Request f)
    → m00 (m00 (r f) (gi q)) (m00 (g q) (d f)) ≡ m00 (r f) (d f)
  left-product f q = assoc (r f) (gi q) (m00 (g q) (d f))
    ∙ cong (m00 (r f))
      (sym (assoc (gi q) (g q) (d f))
      ∙ cong (λ x → m00 x (d f)) (inverse-left q)
      ∙ unit-left (d f))

  right-product : (f : Frame) (q : Request f)
    → m00 (m00 (g q) (d f)) (m00 (r f) (gi q)) ≡ m00 (d f) (r f)
  right-product f q = assoc (g q) (d f) (m00 (r f) (gi q))
    ∙ cong (m00 (g q)) (sym (assoc (d f) (r f) (gi q)))
    ∙ sym (assoc (g q) (m00 (d f) (r f)) (gi q))
    ∙ cong (λ x → m00 x (gi q)) (commute-return f q)
    ∙ assoc (m00 (d f) (r f)) (g q) (gi q)
    ∙ cong (m00 (m00 (d f) (r f))) (inverse-right q)
    ∙ unit-right (m00 (d f) (r f))

  active : (f : Frame) → Request f → Frame
  C (active f q) = m00 (g q) (C f)
  d (active f q) = m00 (g q) (d f)
  r (active f q) = m00 (r f) (gi q)
  u (active f q) = u f
  v (active f q) = v f
  W (active f q) = T.active-W (g q) (d f) (W f) (K q)
  unit-u (active f q) = unit-u f ∙ cong (λ x → sub0 x one) (sym (left-product f q))
  unit-v (active f q) = unit-v f ∙ cong (λ x → sub0 x one) (sym (right-product f q))
  triangle (active f q) = T.active-triangle (g q) (d f) (u f) (v f) (W f) (K q)
    (triangle f) (certificate q)

  -- Exact edit with maps and u fixed. Readout/cost permission is separate;
  -- this function establishes algebraic validity, not permission to execute.
  exact-edit : Frame → D2 → Frame
  C (exact-edit f z) = C f
  d (exact-edit f z) = d f
  r (exact-edit f z) = r f
  u (exact-edit f z) = u f
  v (exact-edit f z) = T.edited-v (v f) z
  W (exact-edit f z) = T.edited-W (d f) (W f) z
  unit-u (exact-edit f z) = unit-u f
  unit-v (exact-edit f z) = T.exact-edit-unit (v f) z ∙ unit-v f
  triangle (exact-edit f z) = T.exact-edit-triangle (d f) (u f) (v f) (W f) z (triangle f)

  protected-u : (f : Frame) (q : Request f) → u (active f q) ≡ u f
  protected-u f q = refl

  protected-v : (f : Frame) (q : Request f) → v (active f q) ≡ v f
  protected-v f q = refl
