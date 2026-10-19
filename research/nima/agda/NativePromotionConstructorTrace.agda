{-# OPTIONS --safe --cubical --guardedness #-}
module NativePromotionConstructorTrace where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Whole
import NativeFeedbackRouteReadout as Source

-- Follow ONE existing native constructor. No new update law, seed family,
-- diagram labelling, numerical response, or physical observer is supplied.
module F = Source.F.F
module Before = F.Previous
module After = F.Next

input : Before.Compared
input = Source.input

output : After.Compared
output = F.run input

-- The promoted payload is the actual next comparison, not its old decoded
-- tetrahedron and not a new externally supplied carrier.
packed-output : Whole.Universe.Complete (ℓ-suc (ℓ-suc (ℓ-suc ℓ-zero)))
packed-output = F.promoted input

packed-value : Whole.Universe.value packed-output ≡ output
packed-value = refl

-- Source and target are the constructor's transported PRESENTATIONS of
-- the full previous-comparison carrier, not primitive seed vertices.
source-presentation : After.Compared.source output ≡ F.A
source-presentation = F.run-source input

target-presentation : After.Compared.target output ≡ F.C
target-presentation = F.run-target input

-- Pull an already attached native question through the actual decoder.
-- This is a precise observation comparison, not an arbitrary new reader.
inherited-question : After.Compared → ℕ × ℕ
inherited-question c = Source.reading (F.decode c)

question-square : (c : Before.Compared)
  → inherited-question (F.run c) ≡ Source.reading c
question-square c = cong Source.reading (F.decode-run c)

-- The NEW outer routes are direct(identity) and via(exchange,exchange).
-- Their lengths are not the inherited routes' changing lengths.
outer-question : After.Compared → ℕ × ℕ
outer-question c = F.steps (After.Compared.first c) , F.steps (After.Compared.second c)

outer-question-trace : (c : Before.Compared)
  → outer-question (F.run c) ≡ (1 , 2)
outer-question-trace c i = F.run-first-steps c i , F.run-second-steps c i

inherited-original : inherited-question output ≡ (1 , 2)
inherited-original = question-square input ∙ Source.initial-reading

inherited-exchanged : inherited-question (F.run (F.exchange input)) ≡ (2 , 1)
inherited-exchanged = question-square (F.exchange input) ∙ Source.returned-reading

-- Both histories remain distinguished after promotion; a new outer step
-- count is not a replacement for the old attached question.
inherited-distinction : inherited-question (F.run (F.exchange input))
  ≡ inherited-question output → ⊥
inherited-distinction p = Source.reading-changes
  (sym (question-square (F.exchange input)) ∙ p ∙ question-square input)

-- Feed the exact promoted value through the existing SECOND constructor.
module G = Source.F.G
second-output : G.Next.Compared
second-output = G.run (Whole.Universe.value packed-output)

second-inherited-question : G.Next.Compared → ℕ × ℕ
second-inherited-question c = inherited-question (G.decode c)

second-question-square : second-inherited-question second-output ≡ Source.reading input
second-question-square = cong inherited-question (G.decode-run output) ∙ question-square input

-- Important boundary: no theorem in this module identifies F.run with the
-- intended T9, its presentations with rung12/6, or these questions with J4.
