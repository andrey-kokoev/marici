{-# OPTIONS --safe --cubical --guardedness #-}
module WholePackageUniversalProperty where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool.Base using (true; false)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution

module Universal (ℓ : Level) (S : Whole.Universe.Complete ℓ → Type (ℓ-suc ℓ)) where
  open Whole.Universe ℓ
  open Resolution.Generators ℓ

  -- A rule-respecting interpretation can retain arbitrary higher data.
  record Algebra : Type (ℓ-suc (ℓ-suc ℓ)) where
    field
      Carrier : Complete → Type (ℓ-suc ℓ)
      on-seed : {q : Complete} → S q → Carrier q
      on-rule : (r : Rule) → ((i : Arity r) → Carrier (input r i)) → Carrier (output r)
  open Algebra

  evaluate : (A : Algebra) → {q : Complete} → Resolve S q → Carrier A q
  evaluate A (seed s) = on-seed A s
  evaluate A (apply r ds) = on-rule A r (λ i → evaluate A (ds i))

  -- Every family containing the seeds and closed under the rules receives
  -- every generated history, with an explicit evaluator as witness.
  least-closed : (T : Complete → Type (ℓ-suc ℓ))
    → ({q : Complete} → S q → T q)
    → ((r : Rule) → ((i : Arity r) → T (input r i)) → T (output r))
    → {q : Complete} → Resolve S q → T q
  least-closed T s r = evaluate (record { Carrier = T ; on-seed = s ; on-rule = r })

  -- Uniqueness of the underlying evaluation function, given its laws.
  -- No claim of uniqueness of the supplied law witnesses is made here.
  evaluate-unique : (A : Algebra)
    (h : (q : Complete) → Resolve S q → Carrier A q)
    (hs : (q : Complete) (s : S q) → h q (seed s) ≡ on-seed A s)
    (hr : (r : Rule) (ds : (i : Arity r) → Resolve S (input r i))
      → h (output r) (apply r ds) ≡ on-rule A r (λ i → h (input r i) (ds i)))
    → (q : Complete) (d : Resolve S q) → h q d ≡ evaluate A d
  evaluate-unique A h hs hr q (seed s) = hs q s
  evaluate-unique A h hs hr q (apply r ds) =
    hr r ds ∙ cong (on-rule A r)
      (funExt (λ i → evaluate-unique A h hs hr (input r i) (ds i)))

  evaluate-unique-function : (A : Algebra)
    (h : (q : Complete) → Resolve S q → Carrier A q)
    (hs : (q : Complete) (s : S q) → h q (seed s) ≡ on-seed A s)
    (hr : (r : Rule) (ds : (i : Arity r) → Resolve S (input r i))
      → h (output r) (apply r ds) ≡ on-rule A r (λ i → h (input r i) (ds i)))
    → h ≡ (λ q d → evaluate A d)
  evaluate-unique-function A h hs hr =
    funExt (λ q → funExt (evaluate-unique A h hs hr q))

  syntax-algebra : Algebra
  syntax-algebra = record
    { Carrier = Resolve S ; on-seed = seed ; on-rule = apply }

  rebuild-retains-history : {q : Complete} (d : Resolve S q)
    → evaluate syntax-algebra d ≡ d
  rebuild-retains-history {q} d = sym
    (evaluate-unique syntax-algebra (λ _ d → d)
      (λ _ _ → refl) (λ _ _ → refl) q d)

  -- Fusion: interpreting first and then applying a rule-preserving map
  -- agrees with direct interpretation into the target algebra.
  fusion : (A B : Algebra)
    (f : (q : Complete) → Carrier A q → Carrier B q)
    (fs : (q : Complete) (s : S q) → f q (on-seed A s) ≡ on-seed B s)
    (fr : (r : Rule) (xs : (i : Arity r) → Carrier A (input r i))
      → f (output r) (on-rule A r xs) ≡ on-rule B r (λ i → f (input r i) (xs i)))
    → (q : Complete) (d : Resolve S q) → f q (evaluate A d) ≡ evaluate B d
  fusion A B f fs fr = evaluate-unique B
    (λ q d → f q (evaluate A d)) fs
    (λ r ds → fr r (λ i → evaluate A (ds i)))

  -- Ordinary and higher equalities of whole histories survive evaluation
  -- as actual equalities, rather than mere existence claims.
  evaluate-path : (A : Algebra) {q : Complete} {d e : Resolve S q}
    → d ≡ e → evaluate A d ≡ evaluate A e
  evaluate-path A = cong (evaluate A)

  evaluate-higher : (A : Algebra) {q : Complete} {d e : Resolve S q}
    {p r : d ≡ e} → p ≡ r → evaluate-path A p ≡ evaluate-path A r
  evaluate-higher A = cong (evaluate-path A)

  -- Witness-relative completeness: when the endpoints are reachable and
  -- the actual comparison is supplied, its complete package is reachable.
  admit-comparison : (a b : Complete) → Resolve S a → Resolve S b
    → (e : El (expression a) ≃ El (expression b))
    → (p : equivFun e (value a) ≡ value b)
    → Resolve S (comparison-package a b e p)
  admit-comparison a b da db e p = apply (compare-rule a b e p)
    (λ { (lift true) → da ; (lift false) → db })

  admit-higher : (Q : Code) (x y : El Q) (p q : x ≡ y)
    → Resolve S (path-package Q x y p) → Resolve S (path-package Q x y q)
    → (alpha : p ≡ q) → Resolve S (higher-package Q x y p q alpha)
  admit-higher Q x y p q dp dq alpha = apply (higher-rule Q x y p q alpha)
    (λ { (lift true) → dp ; (lift false) → dq })
