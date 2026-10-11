{-# OPTIONS --safe --cubical --guardedness #-}
module TetrahedralComparisonFeedback where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (equivFun)
open import Cubical.Data.Nat.Base using (ℕ; suc)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Whole
import TriangleComparisonFeedbackRegression as Prior
import TetrahedralHierarchyAtVertex as Hierarchy
import RetainedTetrahedralPackage as Retained

-- Adapter to the PRIOR exchange feedback, not a new response law.
-- Input is a filled tetrahedron. No equality of free seed paths is required
-- or derived here, and no missing seed face is manufactured.
module Adapter {ℓ : Level} (X : Type ℓ) where
  module T = Hierarchy.Hierarchy X
  module At (mark : T.C.Vertex) where
    module V = T.At mark
    Q = Whole.Universe.atom V.View
    module F = Prior.Feedback ℓ Q
    module N = F.Previous
    module H = N.H

    -- Compare one identity presentation step with two. They act on the
    -- complete marked tetrahedron, not merely its vertex projection.
    direct : H.Route H.original H.original
    direct = H.next (H.identity H.original) H.stop
    via : H.Route H.original H.original
    via = H.next {P = H.original} {R = H.original} {T = H.original}
      (H.identity H.original)
      (H.next {P = H.original} {R = H.original} {T = H.original}
        (H.identity H.original) (H.stop {P = H.original}))

    initial : T.C.Full → N.Compared
    initial p = N.compare-compilations direct via (V.decorate p)

    steps : {P R : H.Presentation} → H.Route P R → ℕ
    steps H.stop = 0
    steps (H.next f tail) = suc (steps tail)
    is-one : ℕ → Bool
    is-one 0 = false
    is-one (suc 0) = true
    is-one (suc (suc n)) = false

    before-first : (p : T.C.Full) → steps (N.Compared.first (initial p)) ≡ 1
    before-first p = refl
    after-first : (p : T.C.Full) → steps (N.Compared.first (F.exchange (initial p))) ≡ 2
    after-first p = refl
    exchange-changes-record : (p : T.C.Full) → F.exchange (initial p) ≡ initial p → ⊥
    exchange-changes-record p h = true≢false
      (sym (cong (λ r → is-one (steps (N.Compared.first r))) h))

    -- Decode through the retained presentation coordinates, not by casting
    -- an arbitrary comparison's input-value to the original carrier.
    decode-initial : N.Compared → V.View
    decode-initial r = H.N.reconstruct Q
      (equivFun (H.Presentation.coordinates (N.Compared.source r))
        (N.Compared.input-value r))
    initial-recovered : (p : T.C.Full) → decode-initial (initial p) ≡ V.decorate p
    initial-recovered p = refl

    cycle2 : T.C.Full → F.Next.Compared
    cycle2 p = F.run (initial p)

    module G = Prior.Feedback (ℓ-suc ℓ) (Whole.Universe.atom N.Compared)
    -- The exact promoted output is fed into the next prior constructor.
    cycle3 : T.C.Full → G.Next.Compared
    cycle3 p = G.run (Whole.Universe.value (F.promoted (initial p)))

    recover-comparison : G.Next.Compared → N.Compared
    recover-comparison r = F.decode (G.decode r)
    comparison-recovered : (p : T.C.Full) → recover-comparison (cycle3 p) ≡ initial p
    comparison-recovered p = cong F.decode (G.decode-run (cycle2 p))
      ∙ F.decode-run (initial p)

    recover-full : G.Next.Compared → T.C.Full
    recover-full r = V.recover (decode-initial (recover-comparison r))
    full-recovered : (p : T.C.Full) → recover-full (cycle3 p) ≡ p
    full-recovered p = cong (λ r → V.recover (decode-initial r)) (comparison-recovered p)

    cycle-injective : (p q : T.C.Full) → cycle3 p ≡ cycle3 q → p ≡ q
    cycle-injective p q h = sym (full-recovered p)
      ∙ (cong recover-full h ∙ full-recovered q)

    -- Conservation of the decoded mark is distinct from change of the
    -- comparison record. This theorem does not assert vertex dynamics.
    marked-value-recovered : (p : T.C.Full)
      → T.C.vertex (recover-full (cycle3 p)) mark ≡ T.C.vertex p mark
    marked-value-recovered p = cong (λ q → T.C.vertex q mark) (full-recovered p)

-- Nonvacuous instance: reuse the existing filled typed-value tetrahedron.
-- This is not an instantiation of the obstructed free-seed face hypotheses.
module Fixture where
  module A = Adapter (Retained.TypedValue ℓ-zero)
  module F = A.At A.T.C.zero
  input = Retained.TypedFixture.result
  output : F.G.Next.Compared
  output = F.cycle3 input
  recovered : F.recover-full output ≡ input
  recovered = F.full-recovered input
  changed : F.F.exchange (F.initial input) ≡ F.initial input → ⊥
  changed = F.exchange-changes-record input
