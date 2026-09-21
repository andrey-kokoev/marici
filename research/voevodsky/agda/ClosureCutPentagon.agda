{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureCutPentagon where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (rUnit)
open import Cubical.Data.Unit
open import Cubical.HITs.Pushout.Base
open import Cubical.HITs.Pushout.Properties using (pushoutEquiv)
open import ClosureCanonicalRejoin using (module Naturality)
open import ClosureIntermediateCutComparison using (module CutComparison)

private
  reflexivePentagon : {X : Type} {x : X} →
    Path (x ≡ x) (refl ∙ refl ∙ refl) (refl ∙ refl)
  reflexivePentagon = sym (cong (λ p → refl ∙ p) (rUnit refl))

module Pentagon {A B C D E : Type}
  (f : A → B) (g : B → C) (h : C → D) (k : D → E) where
  module Before = CutComparison f g h
  module After = CutComparison f g (λ c → k (h c))
  module Target = Naturality f (λ b → h (g b)) k
  module First = CutComparison g h k
  module Second = CutComparison (λ a → g (f a)) h k
  module Third = CutComparison f (λ b → h (g b)) k

  -- Transport of triple quotients, with the complete double attachment
  -- boundary retained. Its cofiber is the common fourfold source.
  upper : Before.TripleQuotient → After.TripleQuotient
  upper (inl tt) = inl tt
  upper (inr x) = inr (Target.upper x)
  upper (push (inl tt) w) = push (inl tt) w
  upper (push (inr (inl tt)) w) = push (inr (inl tt)) w
  upper (push (inr (inr c)) w) = push (inr (inr c)) w
  upper (push (inr (push a u)) w) = push (inr (push a u)) w
  upper (push (push (inl tt) v) w) = push (push (inl tt) v) w
  upper (push (push (inr b) v) w) = push (push (inr b) v) w
  upper (push (push (push a u) v) w) = push (push (push a u) v) w

  FourfoldQuotient : Type
  FourfoldQuotient = cofib upper

  -- Collapse the first, second, or third adjacent pair of attachment axes.
  -- These maps have DIFFERENT intermediate quotient types.
  collapseFirst : FourfoldQuotient → First.TripleQuotient
  collapseFirst (inl tt) = inl tt
  collapseFirst (inr x) = inr (After.collapseA x)
  collapseFirst (push (inl tt) t) = push (Before.collapseA (inl tt)) t
  collapseFirst (push (inr (inl tt)) t) = push (Before.collapseA (inr (inl tt))) t
  collapseFirst (push (inr (inr (inl tt))) t) = push (Before.collapseA (inr (inr (inl tt)))) t
  collapseFirst (push (inr (inr (inr d))) t) = push (Before.collapseA (inr (inr (inr d)))) t
  collapseFirst (push (inr (inr (push a u))) t) = push (Before.collapseA (inr (inr (push a u)))) t
  collapseFirst (push (inr (push (inl tt) v)) t) = push (Before.collapseA (inr (push (inl tt) v))) t
  collapseFirst (push (inr (push (inr b) v)) t) = push (Before.collapseA (inr (push (inr b) v))) t
  collapseFirst (push (inr (push (push a u) v)) t) = push (Before.collapseA (inr (push (push a u) v))) t
  collapseFirst (push (push (inl tt) w) t) = push (Before.collapseA (push (inl tt) w)) t
  collapseFirst (push (push (inr (inl tt)) w) t) = push (Before.collapseA (push (inr (inl tt)) w)) t
  collapseFirst (push (push (inr (inr c)) w) t) = push (Before.collapseA (push (inr (inr c)) w)) t
  collapseFirst (push (push (inr (push a u)) w) t) = push (Before.collapseA (push (inr (push a u)) w)) t
  collapseFirst (push (push (push (inl tt) v) w) t) = push (Before.collapseA (push (push (inl tt) v) w)) t
  collapseFirst (push (push (push (inr b) v) w) t) = push (Before.collapseA (push (push (inr b) v) w)) t
  collapseFirst (push (push (push (push a u) v) w) t) = push (Before.collapseA (push (push (push a u) v) w)) t

  collapseSecond : FourfoldQuotient → Second.TripleQuotient
  collapseSecond (inl tt) = inl tt
  collapseSecond (inr x) = inr (After.collapseMiddle x)
  collapseSecond (push (inl tt) t) = push (Before.collapseMiddle (inl tt)) t
  collapseSecond (push (inr (inl tt)) t) = push (Before.collapseMiddle (inr (inl tt))) t
  collapseSecond (push (inr (inr (inl tt))) t) = push (Before.collapseMiddle (inr (inr (inl tt)))) t
  collapseSecond (push (inr (inr (inr d))) t) = push (Before.collapseMiddle (inr (inr (inr d)))) t
  collapseSecond (push (inr (inr (push a u))) t) = push (Before.collapseMiddle (inr (inr (push a u)))) t
  collapseSecond (push (inr (push (inl tt) v)) t) = push (Before.collapseMiddle (inr (push (inl tt) v))) t
  collapseSecond (push (inr (push (inr b) v)) t) = push (Before.collapseMiddle (inr (push (inr b) v))) t
  collapseSecond (push (inr (push (push a u) v)) t) = push (Before.collapseMiddle (inr (push (push a u) v))) t
  collapseSecond (push (push (inl tt) w) t) = push (Before.collapseMiddle (push (inl tt) w)) t
  collapseSecond (push (push (inr (inl tt)) w) t) = push (Before.collapseMiddle (push (inr (inl tt)) w)) t
  collapseSecond (push (push (inr (inr c)) w) t) = push (Before.collapseMiddle (push (inr (inr c)) w)) t
  collapseSecond (push (push (inr (push a u)) w) t) = push (Before.collapseMiddle (push (inr (push a u)) w)) t
  collapseSecond (push (push (push (inl tt) v) w) t) = push (Before.collapseMiddle (push (push (inl tt) v) w)) t
  collapseSecond (push (push (push (inr b) v) w) t) = push (Before.collapseMiddle (push (push (inr b) v) w)) t
  collapseSecond (push (push (push (push a u) v) w) t) = push (Before.collapseMiddle (push (push (push a u) v) w)) t

  collapseThird : FourfoldQuotient → Third.TripleQuotient
  collapseThird (inl tt) = inl tt
  collapseThird (inr (inl tt)) = inl tt
  collapseThird (inr (inr x)) = inr x
  collapseThird (inr (push (inl tt) w)) = push (Before.N.upper (inl tt)) w
  collapseThird (inr (push (inr (inl tt)) w)) = push (Before.N.upper (inr (inl tt))) w
  collapseThird (inr (push (inr (inr c)) w)) = push (Before.N.upper (inr (inr c))) w
  collapseThird (inr (push (inr (push a u)) w)) = push (Before.N.upper (inr (push a u))) w
  collapseThird (inr (push (push (inl tt) v) w)) = push (Before.N.upper (push (inl tt) v)) w
  collapseThird (inr (push (push (inr b) v) w)) = push (Before.N.upper (push (inr b) v)) w
  collapseThird (inr (push (push (push a u) v) w)) = push (Before.N.upper (push (push a u) v)) w
  collapseThird (push (inl tt) t) = inl tt
  collapseThird (push (inr x) t) = push x t
  collapseThird (push (push (inl tt) w) t) = push (Before.N.upper (inl tt)) (w ∧ t)
  collapseThird (push (push (inr (inl tt)) w) t) = push (Before.N.upper (inr (inl tt))) (w ∧ t)
  collapseThird (push (push (inr (inr c)) w) t) = push (Before.N.upper (inr (inr c))) (w ∧ t)
  collapseThird (push (push (inr (push a u)) w) t) = push (Before.N.upper (inr (push a u))) (w ∧ t)
  collapseThird (push (push (push (inl tt) v) w) t) = push (Before.N.upper (push (inl tt) v)) (w ∧ t)
  collapseThird (push (push (push (inr b) v) w) t) = push (Before.N.upper (push (inr b) v)) (w ∧ t)
  collapseThird (push (push (push (push a u) v) w) t) = push (Before.N.upper (push (push a u) v)) (w ∧ t)

  -- Five independently assembled routes, named by their deepest-cell brackets.
  v0 v1 v2 v3 v4 : FourfoldQuotient → cofib k
  v0 x = First.removeAFirst (collapseFirst x)       -- (((uv)w)t)
  v1 x = Second.removeAFirst (collapseSecond x)     -- ((u(vw))t)
  v2 x = Second.removeMiddleFirst (collapseSecond x) -- (u((vw)t))
  v3 x = Third.removeMiddleFirst (collapseThird x)  -- (u(v(wt)))
  v4 x = First.removeMiddleFirst (collapseFirst x)  -- ((uv)(wt))

  -- Two edges are actual instances of the previous intermediate-cut theorem.
  e12 : (x : FourfoldQuotient) → v1 x ≡ v2 x
  e12 x = Second.cutComparison (collapseSecond x)

  e04 : (x : FourfoldQuotient) → v0 x ≡ v4 x
  e04 x = First.cutComparison (collapseFirst x)

  e01 : (x : FourfoldQuotient) → v0 x ≡ v1 x
  e01 (inl tt) = refl
  e01 (inr (inl tt)) = refl
  e01 (inr (inr (inl tt))) = refl
  e01 (inr (inr (inr (inl tt)))) = refl
  e01 (inr (inr (inr (inr e)))) = refl
  e01 (inr (inr (inr (push a u)))) = refl
  e01 (inr (inr (push (inl tt) v))) = refl
  e01 (inr (inr (push (inr b) v))) = refl
  e01 (inr (inr (push (push a u) v))) = refl
  e01 (inr (push (inl tt) w)) = refl
  e01 (inr (push (inr (inl tt)) w)) = refl
  e01 (inr (push (inr (inr c)) w)) = refl
  e01 (inr (push (inr (push a u)) w)) = refl
  e01 (inr (push (push (inl tt) v) w)) = refl
  e01 (inr (push (push (inr b) v) w)) = refl
  e01 (inr (push (push (push a u) v) w)) = refl
  e01 (push (inl tt) t) = refl
  e01 (push (inr (inl tt)) t) = refl
  e01 (push (inr (inr (inl tt))) t) = refl
  e01 (push (inr (inr (inr d))) t) = refl
  e01 (push (inr (inr (push a u))) t) = refl
  e01 (push (inr (push (inl tt) v)) t) = refl
  e01 (push (inr (push (inr b) v)) t) = refl
  e01 (push (inr (push (push a u) v)) t) = refl
  e01 (push (push (inl tt) w) t) = refl
  e01 (push (push (inr (inl tt)) w) t) = refl
  e01 (push (push (inr (inr c)) w) t) = refl
  e01 (push (push (inr (push a u)) w) t) = refl
  e01 (push (push (push (inl tt) v) w) t) = refl
  e01 (push (push (push (inr b) v) w) t) = refl
  e01 (push (push (push (push a u) v) w) t) = refl

  e23 : (x : FourfoldQuotient) → v2 x ≡ v3 x
  e23 (inl tt) = refl
  e23 (inr (inl tt)) = refl
  e23 (inr (inr (inl tt))) = refl
  e23 (inr (inr (inr (inl tt)))) = refl
  e23 (inr (inr (inr (inr e)))) = refl
  e23 (inr (inr (inr (push a u)))) = refl
  e23 (inr (inr (push (inl tt) v))) = refl
  e23 (inr (inr (push (inr b) v))) = refl
  e23 (inr (inr (push (push a u) v))) = refl
  e23 (inr (push (inl tt) w)) = refl
  e23 (inr (push (inr (inl tt)) w)) = refl
  e23 (inr (push (inr (inr c)) w)) = refl
  e23 (inr (push (inr (push a u)) w)) = refl
  e23 (inr (push (push (inl tt) v) w)) = refl
  e23 (inr (push (push (inr b) v) w)) = refl
  e23 (inr (push (push (push a u) v) w)) = refl
  e23 (push (inl tt) t) = refl
  e23 (push (inr (inl tt)) t) = refl
  e23 (push (inr (inr (inl tt))) t) = refl
  e23 (push (inr (inr (inr d))) t) = refl
  e23 (push (inr (inr (push a u))) t) = refl
  e23 (push (inr (push (inl tt) v)) t) = refl
  e23 (push (inr (push (inr b) v)) t) = refl
  e23 (push (inr (push (push a u) v)) t) = refl
  e23 (push (push (inl tt) w) t) = refl
  e23 (push (push (inr (inl tt)) w) t) = refl
  e23 (push (push (inr (inr c)) w) t) = refl
  e23 (push (push (inr (push a u)) w) t) = refl
  e23 (push (push (push (inl tt) v) w) t) = refl
  e23 (push (push (push (inr b) v) w) t) = refl
  e23 (push (push (push (push a u) v) w) t) = refl

  e43 : (x : FourfoldQuotient) → v4 x ≡ v3 x
  e43 (inl tt) = refl
  e43 (inr (inl tt)) = refl
  e43 (inr (inr (inl tt))) = refl
  e43 (inr (inr (inr (inl tt)))) = refl
  e43 (inr (inr (inr (inr e)))) = refl
  e43 (inr (inr (inr (push a u)))) = refl
  e43 (inr (inr (push (inl tt) v))) = refl
  e43 (inr (inr (push (inr b) v))) = refl
  e43 (inr (inr (push (push a u) v))) = refl
  e43 (inr (push (inl tt) w)) = refl
  e43 (inr (push (inr (inl tt)) w)) = refl
  e43 (inr (push (inr (inr c)) w)) = refl
  e43 (inr (push (inr (push a u)) w)) = refl
  e43 (inr (push (push (inl tt) v) w)) = refl
  e43 (inr (push (push (inr b) v) w)) = refl
  e43 (inr (push (push (push a u) v) w)) = refl
  e43 (push (inl tt) t) = refl
  e43 (push (inr (inl tt)) t) = refl
  e43 (push (inr (inr (inl tt))) t) = refl
  e43 (push (inr (inr (inr d))) t) = refl
  e43 (push (inr (inr (push a u))) t) = refl
  e43 (push (inr (push (inl tt) v)) t) = refl
  e43 (push (inr (push (inr b) v)) t) = refl
  e43 (push (inr (push (push a u) v)) t) = refl
  e43 (push (push (inl tt) w) t) = refl
  e43 (push (push (inr (inl tt)) w) t) = refl
  e43 (push (push (inr (inr c)) w) t) = refl
  e43 (push (push (inr (push a u)) w) t) = refl
  e43 (push (push (push (inl tt) v) w) t) = refl
  e43 (push (push (push (inr b) v) w) t) = refl
  e43 (push (push (push (push a u) v) w) t) = refl

  longRoute shortRoute : (x : FourfoldQuotient) → v0 x ≡ v3 x
  longRoute x = e01 x ∙ e12 x ∙ e23 x
  shortRoute x = e04 x ∙ e43 x

  -- Equality of the two assembled PATHS, not just their endpoint functions.
  pentagon : (x : FourfoldQuotient) → longRoute x ≡ shortRoute x
  pentagon (inl tt) = reflexivePentagon
  pentagon (inr (inl tt)) = reflexivePentagon
  pentagon (inr (inr (inl tt))) = reflexivePentagon
  pentagon (inr (inr (inr (inl tt)))) = reflexivePentagon
  pentagon (inr (inr (inr (inr e)))) = reflexivePentagon
  pentagon (inr (inr (inr (push a u)))) = reflexivePentagon
  pentagon (inr (inr (push (inl tt) v))) = reflexivePentagon
  pentagon (inr (inr (push (inr b) v))) = reflexivePentagon
  pentagon (inr (inr (push (push a u) v))) = reflexivePentagon
  pentagon (inr (push (inl tt) w)) = reflexivePentagon
  pentagon (inr (push (inr (inl tt)) w)) = reflexivePentagon
  pentagon (inr (push (inr (inr c)) w)) = reflexivePentagon
  pentagon (inr (push (inr (push a u)) w)) = reflexivePentagon
  pentagon (inr (push (push (inl tt) v) w)) = reflexivePentagon
  pentagon (inr (push (push (inr b) v) w)) = reflexivePentagon
  pentagon (inr (push (push (push a u) v) w)) = reflexivePentagon
  pentagon (push (inl tt) t) = reflexivePentagon
  pentagon (push (inr (inl tt)) t) = reflexivePentagon
  pentagon (push (inr (inr (inl tt))) t) = reflexivePentagon
  pentagon (push (inr (inr (inr d))) t) = reflexivePentagon
  pentagon (push (inr (inr (push a u))) t) = reflexivePentagon
  pentagon (push (inr (push (inl tt) v)) t) = reflexivePentagon
  pentagon (push (inr (push (inr b) v)) t) = reflexivePentagon
  pentagon (push (inr (push (push a u) v)) t) = reflexivePentagon
  pentagon (push (push (inl tt) w) t) = reflexivePentagon
  pentagon (push (push (inr (inl tt)) w) t) = reflexivePentagon
  pentagon (push (push (inr (inr c)) w) t) = reflexivePentagon
  pentagon (push (push (inr (push a u)) w) t) = reflexivePentagon
  pentagon (push (push (push (inl tt) v) w) t) = reflexivePentagon
  pentagon (push (push (push (inr b) v) w) t) = reflexivePentagon
  pentagon (push (push (push (push a u) v) w) t) = reflexivePentagon

  -- Certify the first collapse via a span of the previously proved
  -- equivalences. Naturality is proved here on all triple-quotient cells.
  firstNaturality : (x : Before.TripleQuotient) →
    After.collapseA (upper x) ≡ First.N.upper (Before.collapseA x)
  firstNaturality (inl tt) = refl
  firstNaturality (inr (inl tt)) = refl
  firstNaturality (inr (inr (inl tt))) = refl
  firstNaturality (inr (inr (inr d))) = refl
  firstNaturality (inr (inr (push a u))) = refl
  firstNaturality (inr (push (inl tt) v)) = refl
  firstNaturality (inr (push (inr b) v)) = refl
  firstNaturality (inr (push (push a u) v)) = refl
  firstNaturality (push (inl tt) w) = refl
  firstNaturality (push (inr (inl tt)) w) = refl
  firstNaturality (push (inr (inr c)) w) = refl
  firstNaturality (push (inr (push a u)) w) = refl
  firstNaturality (push (push (inl tt) v) w) = refl
  firstNaturality (push (push (inr b) v) w) = refl
  firstNaturality (push (push (push a u) v) w) = refl

  firstSpanEquiv : FourfoldQuotient ≃ First.TripleQuotient
  firstSpanEquiv = pushoutEquiv
    (λ _ → tt) upper (λ _ → tt) First.N.upper
    Before.collapseAEquiv (idEquiv Unit) After.collapseAEquiv
    refl (funExt firstNaturality)

  firstSpanComparison : (x : FourfoldQuotient) →
    equivFun firstSpanEquiv x ≡ collapseFirst x
  firstSpanComparison (inl tt) = refl
  firstSpanComparison (inr x) = refl
  firstSpanComparison (push (inl tt) t) j = sym (rUnit (push (Before.collapseA (inl tt)))) j t
  firstSpanComparison (push (inr (inl tt)) t) j = sym (rUnit (push (Before.collapseA (inr (inl tt))))) j t
  firstSpanComparison (push (inr (inr (inl tt))) t) j = sym (rUnit (push (Before.collapseA (inr (inr (inl tt)))))) j t
  firstSpanComparison (push (inr (inr (inr d))) t) j = sym (rUnit (push (Before.collapseA (inr (inr (inr d)))))) j t
  firstSpanComparison (push (inr (inr (push a u))) t) j = sym (rUnit (push (Before.collapseA (inr (inr (push a u)))))) j t
  firstSpanComparison (push (inr (push (inl tt) v)) t) j = sym (rUnit (push (Before.collapseA (inr (push (inl tt) v))))) j t
  firstSpanComparison (push (inr (push (inr b) v)) t) j = sym (rUnit (push (Before.collapseA (inr (push (inr b) v))))) j t
  firstSpanComparison (push (inr (push (push a u) v)) t) j = sym (rUnit (push (Before.collapseA (inr (push (push a u) v))))) j t
  firstSpanComparison (push (push (inl tt) w) t) j = sym (rUnit (push (Before.collapseA (push (inl tt) w)))) j t
  firstSpanComparison (push (push (inr (inl tt)) w) t) j = sym (rUnit (push (Before.collapseA (push (inr (inl tt)) w)))) j t
  firstSpanComparison (push (push (inr (inr c)) w) t) j = sym (rUnit (push (Before.collapseA (push (inr (inr c)) w)))) j t
  firstSpanComparison (push (push (inr (push a u)) w) t) j = sym (rUnit (push (Before.collapseA (push (inr (push a u)) w)))) j t
  firstSpanComparison (push (push (push (inl tt) v) w) t) j = sym (rUnit (push (Before.collapseA (push (push (inl tt) v) w)))) j t
  firstSpanComparison (push (push (push (inr b) v) w) t) j = sym (rUnit (push (Before.collapseA (push (push (inr b) v) w)))) j t
  firstSpanComparison (push (push (push (push a u) v) w) t) j = sym (rUnit (push (Before.collapseA (push (push (push a u) v) w)))) j t

  abstract
    firstIsEquiv : isEquiv collapseFirst
    firstIsEquiv = subst isEquiv (funExt firstSpanComparison) (snd firstSpanEquiv)

  firstEquiv : FourfoldQuotient ≃ First.TripleQuotient
  firstEquiv = collapseFirst , firstIsEquiv

  abstract
    v0IsEquiv : isEquiv v0
    v0IsEquiv = snd (compEquiv firstEquiv First.removeAFirstEquiv)

    v1IsEquiv : isEquiv v1
    v1IsEquiv = subst isEquiv (funExt e01) v0IsEquiv

    v2IsEquiv : isEquiv v2
    v2IsEquiv = subst isEquiv (funExt e12) v1IsEquiv

    v3IsEquiv : isEquiv v3
    v3IsEquiv = subst isEquiv (funExt e23) v2IsEquiv

    v4IsEquiv : isEquiv v4
    v4IsEquiv = subst isEquiv (funExt e04) v0IsEquiv

  E0 E1 E2 E3 E4 : FourfoldQuotient ≃ cofib k
  E0 = v0 , v0IsEquiv
  E1 = v1 , v1IsEquiv
  E2 = v2 , v2IsEquiv
  E3 = v3 , v3IsEquiv
  E4 = v4 , v4IsEquiv

  -- The other two intermediate collapses are equivalences by cancellation
  -- with their already certified final rejoin routes.
  abstract
    secondIsEquiv : isEquiv collapseSecond
    secondIsEquiv = subst isEquiv
      (funExt (λ x → retEq Second.removeAFirstEquiv (collapseSecond x)))
      (snd (compEquiv E1 (invEquiv Second.removeAFirstEquiv)))

    thirdIsEquiv : isEquiv collapseThird
    thirdIsEquiv = subst isEquiv
      (funExt (λ x → retEq Third.removeMiddleFirstEquiv (collapseThird x)))
      (snd (compEquiv E3 (invEquiv Third.removeMiddleFirstEquiv)))

  secondEquiv : FourfoldQuotient ≃ Second.TripleQuotient
  secondEquiv = collapseSecond , secondIsEquiv

  thirdEquiv : FourfoldQuotient ≃ Third.TripleQuotient
  thirdEquiv = collapseThird , thirdIsEquiv

  -- A comparison of paths in the function space, with the same endpoints.
  functionPentagon : funExt longRoute ≡ funExt shortRoute
  functionPentagon i = funExt (λ x → pentagon x i)

-- This pentagon is for these canonical cofiber collapse assemblies. It does
-- not assert analytical realization or comparison with the opaque 3x3 choice.

