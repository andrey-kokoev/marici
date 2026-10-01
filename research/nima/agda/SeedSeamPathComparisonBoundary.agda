{-# OPTIONS --safe --cubical --guardedness #-}
module SeedSeamPathComparisonBoundary where

open import Cubical.Foundations.Prelude hiding (Path)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (ℕ; suc)
open import ActualSeedEndpointTable

-- Free endpoint-typed paths on exactly the supplied primitive occurrences.
-- No relation identifying distinct words is imposed.
data Path : Vertex → Vertex → Type where
  stop : {v : Vertex} → Path v v
  step : {t : Vertex} (e : Occurrence)
    → Path (target e) t → Path (source e) t

x0 x1 : Path A B
x0 = step AB stop
x1 = step AD (step DB stop)
y0 y1 : Path B A
y0 = step BA stop
y1 = step BC (step CA stop)

length : {s t : Vertex} → Path s t → ℕ
length stop = 0
length (step e rest) = suc (length rest)

is-one : ℕ → Bool
is-one 0 = false
is-one (suc 0) = true
is-one (suc (suc n)) = false

single : {s t : Vertex} → Path s t → Bool
single p = is-one (length p)

forward-distinct : x0 ≡ x1 → ⊥
forward-distinct p = true≢false (cong single p)
return-distinct : y0 ≡ y1 → ⊥
return-distinct p = true≢false (cong single p)

-- Even a general map (hence also any equivalence) cannot both preserve this
-- declared observation and send the direct path to its indirect alternative.
forward-observed-obstruction : (f : Path A B → Path A B)
  → ((p : Path A B) → single (f p) ≡ single p)
  → f x0 ≡ x1 → ⊥
forward-observed-obstruction f respects sends =
  true≢false (sym (respects x0) ∙ cong single sends)

return-observed-obstruction : (f : Path B A → Path B A)
  → ((p : Path B A) → single (f p) ≡ single p)
  → f y0 ≡ y1 → ⊥
return-observed-obstruction f respects sends =
  true≢false (sym (respects y0) ∙ cong single sends)

-- Both parallel paths may instead be retained as a comparison QUESTION.
-- A common endpoint or paired record is not an equality/effect witness.
record ForwardQuestion : Type where
  constructor forward-question
  field
    direct indirect : Path A B

record ReturnQuestion : Type where
  constructor return-question
  field
    direct indirect : Path B A

forward-boundary : ForwardQuestion
forward-boundary = forward-question x0 x1
return-boundary : ReturnQuestion
return-boundary = return-question y0 y1

retains-forward-direct : ForwardQuestion.direct forward-boundary ≡ x0
retains-forward-direct = refl
retains-forward-indirect : ForwardQuestion.indirect forward-boundary ≡ x1
retains-forward-indirect = refl
