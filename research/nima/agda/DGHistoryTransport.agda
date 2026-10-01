{-# OPTIONS --safe --cubical --guardedness #-}
module DGHistoryTransport where

open import Cubical.Foundations.Prelude

-- Homogeneous endomorphism algebra interface (e.g. block endomorphisms of
-- A ⊕ B). D0 consists of CLOSED degree-zero maps. D1 and D2 have degrees
-- one and two. No commutativity of composition is assumed. Endpoint corner
-- constraints and a concrete matrix/DG instance remain separate obligations.
record DGFragment : Type₁ where
  field
    D0 D1 D2 : Type
    add0 : D0 → D0 → D0
    zero0 : D0
    add1 sub1 : D1 → D1 → D1
    add2 sub2 : D2 → D2 → D2
    m00 : D0 → D0 → D0
    m01 : D0 → D1 → D1
    m10 : D1 → D0 → D1
    m02 : D0 → D2 → D2
    m20 : D2 → D0 → D2
    delta1 : D1 → D0
    delta2 : D2 → D1

    -- Additive laws used below, stated independently of frame data.
    telescope : (a b c : D1) → add1 (sub1 a b) (sub1 b c) ≡ sub1 a c
    subtract-sum : (a b c : D1) → sub1 (sub1 a b) c ≡ sub1 a (add1 b c)
    add0-zero : (a : D0) → add0 a zero0 ≡ a
    left-sub : (g : D0) (x y : D1)
      → m01 g (sub1 x y) ≡ sub1 (m01 g x) (m01 g y)
    right-sub : (x y : D1) (d : D0)
      → m10 (sub1 x y) d ≡ sub1 (m10 x d) (m10 y d)
    right-add : (x y : D1) (d : D0)
      → m10 (add1 x y) d ≡ add1 (m10 x d) (m10 y d)
    assoc001 : (g d : D0) (u : D1) → m01 g (m01 d u) ≡ m01 (m00 g d) u
    assoc010 : (g : D0) (v : D1) (d : D0) → m01 g (m10 v d) ≡ m10 (m01 g v) d
    assoc100 : (v : D1) (g d : D0) → m10 (m10 v g) d ≡ m10 v (m00 g d)

    -- Differential linearity, square-zero and closed degree-zero Leibniz.
    delta-add : (x y : D2) → delta2 (add2 x y) ≡ add1 (delta2 x) (delta2 y)
    delta-sub : (x y : D2) → delta2 (sub2 x y) ≡ sub1 (delta2 x) (delta2 y)
    delta-left : (g : D0) (w : D2) → delta2 (m02 g w) ≡ m01 g (delta2 w)
    delta-right : (k : D2) (d : D0) → delta2 (m20 k d) ≡ m10 (delta2 k) d
    delta1-add : (x y : D1) → delta1 (add1 x y) ≡ add0 (delta1 x) (delta1 y)
    square-zero : (z : D2) → delta1 (delta2 z) ≡ zero0

module Transport (D : DGFragment) where
  open DGFragment D

  boundary : D0 → D1 → D1 → D1
  boundary d u v = sub1 (m01 d u) (m10 v d)

  commutator : D0 → D1 → D1
  commutator g v = sub1 (m01 g v) (m10 v g)

  active-W : D0 → D0 → D2 → D2 → D2
  active-W g d w k = add2 (m02 g w) (m20 k d)

  -- This is the noncommutative cancellation at the heart of the update.
  cancellation : (g d : D0) (u v : D1)
    → add1 (m01 g (boundary d u v)) (m10 (commutator g v) d)
      ≡ boundary (m00 g d) u v
  cancellation g d u v =
    cong₂ add1 (left-sub g (m01 d u) (m10 v d))
      (right-sub (m01 g v) (m10 v g) d)
    ∙ cong₂ add1
        (cong₂ sub1 (assoc001 g d u) (assoc010 g v d))
        (cong (sub1 (m10 (m01 g v) d)) (assoc100 v g d))
    ∙ telescope (m01 (m00 g d) u) (m10 (m01 g v) d) (m10 v (m00 g d))

  active-triangle : (g d : D0) (u v : D1) (w k : D2)
    → delta2 w ≡ boundary d u v
    → delta2 k ≡ commutator g v
    → delta2 (active-W g d w k) ≡ boundary (m00 g d) u v
  active-triangle g d u v w k triangle certificate =
    delta-add (m02 g w) (m20 k d)
    ∙ cong₂ add1 (delta-left g w) (delta-right k d)
    ∙ cong₂ add1 (cong (m01 g) triangle) (cong (λ t → m10 t d) certificate)
    ∙ cancellation g d u v

  edited-v : D1 → D2 → D1
  edited-v v z = add1 v (delta2 z)

  edited-W : D0 → D2 → D2 → D2
  edited-W d w z = sub2 w (m20 z d)

  exact-edit-unit : (v : D1) (z : D2) → delta1 (edited-v v z) ≡ delta1 v
  exact-edit-unit v z = delta1-add v (delta2 z)
    ∙ cong (add0 (delta1 v)) (square-zero z)
    ∙ add0-zero (delta1 v)

  exact-edit-triangle : (d : D0) (u v : D1) (w z : D2)
    → delta2 w ≡ boundary d u v
    → delta2 (edited-W d w z) ≡ boundary d u (edited-v v z)
  exact-edit-triangle d u v w z triangle =
    delta-sub w (m20 z d)
    ∙ cong₂ sub1 triangle (delta-right z d)
    ∙ subtract-sum (m01 d u) (m10 v d) (m10 (delta2 z) d)
    ∙ cong (sub1 (m01 d u)) (sym (right-add v (delta2 z) d))
