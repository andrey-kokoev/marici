{-# OPTIONS --safe --cubical --guardedness #-}
module NativeFamilyFeedbackBinding where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (equivFun)
import WholePackageSigmaPi as Whole
import TriangleComparisonFeedbackRegression as Native

-- Families and context are declared source data. No matrix calibration,
-- independent operand expansion, or tetrahedral face witness is assumed.
module Families {ℓ : Level} (R K : Type ℓ) (key : R → K) where
  record Family : Type (ℓ-suc ℓ) where
    field
      endpoint : K
      Members : Type ℓ
      member : Members → R
      belongs : (i : Members) → key (member i) ≡ endpoint
  open Family

  Q = Whole.Universe.atom Family
  module F = Native.Feedback (ℓ-suc ℓ) Q
  module Before = F.Previous
  module After = F.Next

  -- Explicit adapter, NOT identification of the original native filled input.
  -- Atomic family gets two empty routes in its own original presentation.
  embed : Family → Before.Compared
  embed family = Before.compare-compilations
    (Before.H.stop {P = Before.H.original})
    (Before.H.stop {P = Before.H.original}) family

  recover-before : Before.Compared → Family
  recover-before c = Before.H.N.reconstruct Q
    (equivFun (Before.H.Presentation.coordinates (Before.Compared.source c))
      (Before.Compared.input-value c))

  embed-recovered : (family : Family) → recover-before (embed family) ≡ family
  embed-recovered family = refl

  promote : Family → After.Compared
  promote family = F.run (embed family)

  decode : After.Compared → Family
  decode c = recover-before (F.decode c)

  family-recovered : (family : Family) → decode (promote family) ≡ family
  family-recovered family = cong recover-before (F.decode-run (embed family))
    ∙ embed-recovered family

  promote-injective : (a b : Family) → promote a ≡ promote b → a ≡ b
  promote-injective a b p = sym (family-recovered a)
    ∙ cong decode p ∙ family-recovered b

  source : After.Compared → Family
  source = decode
  target : After.Compared → K
  target c = endpoint (decode c)

  target-recovered : (family : Family)
    → target (promote family) ≡ endpoint family
  target-recovered family = cong endpoint (family-recovered family)

  target-preserves-context : (a b : Family)
    → endpoint a ≡ endpoint b → target (promote a) ≡ target (promote b)
  target-preserves-context a b p = target-recovered a ∙ p ∙ sym (target-recovered b)

  target-reflects-context : (a b : Family)
    → target (promote a) ≡ target (promote b) → endpoint a ≡ endpoint b
  target-reflects-context a b p = sym (target-recovered a) ∙ p ∙ target-recovered b

  -- The grouping endpoint and generated successor port need not be the same.
  -- Existing promotions tag inherited keys or collapse them to a common port.
  module NextPort {ℓ' : Level} (T : Type ℓ') (successor : K → T) where
    next-target : After.Compared → T
    next-target c = successor (target c)

    next-target-recovered : (family : Family)
      → next-target (promote family) ≡ successor (endpoint family)
    next-target-recovered family = cong successor (target-recovered family)

    preserves : (a b : Family)
      → successor (endpoint a) ≡ successor (endpoint b)
      → next-target (promote a) ≡ next-target (promote b)
    preserves a b p = next-target-recovered a ∙ p ∙ sym (next-target-recovered b)

    reflects : (a b : Family)
      → next-target (promote a) ≡ next-target (promote b)
      → successor (endpoint a) ≡ successor (endpoint b)
    reflects a b p = sym (next-target-recovered a) ∙ p ∙ next-target-recovered b

  -- Any supplied family observation travels through the actual native decode.
  -- Weighted means and their measure remain inputs, not selected by feedback.
  reading-square : {ℓ' : Level} {O : Type ℓ'} (read : Family → O)
    (family : Family) → read (decode (promote family)) ≡ read family
  reading-square read family = cong read (family-recovered family)

-- Feedback promotion itself performs no grouping or weighted averaging.
-- The separate map from rows to Family must be bound before naming this T9.
