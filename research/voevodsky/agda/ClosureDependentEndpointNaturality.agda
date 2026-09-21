{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureDependentEndpointNaturality where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (lUnit)
open import Cubical.Foundations.Path using (Square→compPath)

-- A dependent endpoint path is compared with the actual transport filler,
-- not with an independently selected path having the same endpoints.
module Along (A B : I → Type) (f : (i : I) → A i → B i)
  {a₀ : A i0} {a₁ : A i1} (a : PathP A a₀ a₁) where

  endpoint : transport (λ i → A i) a₀ ≡ a₁
  endpoint = fromPathP a

  frame : transport (λ i → B i) (f i0 a₀) ≡
    f i1 (transport (λ i → A i) a₀)
  frame = fromPathP (λ i → f i (transport-filler (λ j → A j) a₀ i))

  moving : transport (λ i → B i) (f i0 a₀) ≡ f i1 a₁
  moving = fromPathP (λ i → f i (a i))

  -- j=0 is transport-filler; j=1 is a; i=1 is fromPathP a.
  endpointFiller : (i j : I) → A i
  endpointFiller i j = transp (λ k → A (i ∧ (j ∨ k))) (j ∨ ~ i) (a (i ∧ j))

  factors : moving ≡ frame ∙ cong (f i1) endpoint
  factors = lUnit moving ∙ Square→compPath
    (λ j → fromPathP (λ i → f i (endpointFiller i j)))

  module Port {b₀ : B i0} {b₁ : B i1}
    (b : PathP B b₀ b₁)
    (h : (i : I) → f i (a i) ≡ b i) where

    source : transport (λ i → B i) (f i0 a₀) ≡ transport (λ i → B i) b₀
    source = cong (transport (λ i → B i)) (h i0)

    target : f i1 a₁ ≡ b₁
    target = h i1

    boundary : (frame ∙ cong (f i1) endpoint) ∙ target ≡ source ∙ fromPathP b
    boundary = cong (λ p → p ∙ target) (sym factors)
      ∙ Square→compPath (λ i j → fromPathP (λ k → h k j) i)

-- No equivalence, injectivity, or truncation assumption is needed. The
-- square is obtained from the given dependent diagram, including h.
