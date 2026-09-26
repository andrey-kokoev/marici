{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverRRCGeneratedBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Transport using (transport⁻; transport⁻Transport)
open import Cubical.Data.Sigma.Base using (Σ; _,_)
import WholePackageSigmaPi as W
import WholePackageResolution as RRC
import WholePackageUniversalProperty as Universal
import WholeHistoryComparisons as Comparisons
import ObserverRRCRecursiveBridge as Recursive

module Bridge (ℓ : Level) (S : W.Universe.Complete ℓ → Type (ℓ-suc ℓ)) where
  module R = RRC.Generators ℓ
  module U = W.Universe ℓ
  module V = Universal.Universal ℓ S
  module B = Recursive.Bridge ℓ

  module Interpreted (A : V.Algebra)
    (Law : (q : U.Complete) → R.Resolve S q → R.Resolve S q → Type (ℓ-suc ℓ))
    (interpret-law : (q : U.Complete) (d e : R.Resolve S q)
      → Law q d e → V.evaluate A d ≡ V.evaluate A e) where

    module Original = Comparisons.Comparisons ℓ S
    module Sem = Original.Interpreted A
    module G = Sem.Structural Law interpret-law

    evaluate : {q : U.Complete} → B.Term S q → V.Algebra.Carrier A q
    evaluate t = V.evaluate A (B.decode t)

    Semantic : {q : U.Complete} → B.Term S q → B.Term S q → Type (ℓ-suc ℓ)
    Semantic t u = evaluate t ≡ evaluate u

    -- Source-law boundaries and actual law evidence remain explicit.
    -- There is no constructor importing an arbitrary Semantic witness.
    data Generated : {q : U.Complete} → B.Term S q → B.Term S q → Type (ℓ-suc ℓ) where
      reflexive : {q : U.Complete} (t : B.Term S q) → Generated t t
      invert : {q : U.Complete} {t u : B.Term S q} → Generated t u → Generated u t
      concatenate : {q : U.Complete} {t u v : B.Term S q}
        → Generated t u → Generated u v → Generated t v
      law : {q : U.Complete} {d e : R.Resolve S q}
        → Law q d e → Generated (B.encode d) (B.encode e)
      congruence : (r : R.Rule)
        (ts us : (i : R.Arity r) → B.Term S (R.input r i))
        → ((i : R.Arity r) → Generated (ts i) (us i))
        → Generated (B.call r ts) (B.call r us)

    transfer : {q : U.Complete} {d e : R.Resolve S q}
      → G.Generated d e → Generated (B.encode d) (B.encode e)
    transfer (G.reflexive d) = reflexive (B.encode d)
    transfer (G.invert c) = invert (transfer c)
    transfer (G.concatenate c c') = concatenate (transfer c) (transfer c')
    transfer (G.law w) = law w
    transfer (G.congruence r ds es cs) = congruence r
      (λ i → B.encode (ds i)) (λ i → B.encode (es i)) (λ i → transfer (cs i))

    boundary : {q : U.Complete} (d : R.Resolve S q)
      → evaluate (B.encode d) ≡ V.evaluate A d
    boundary d = cong (V.evaluate A) (B.decode-encode d)

    sound : {q : U.Complete} {t u : B.Term S q} → Generated t u → Semantic t u
    sound (reflexive t) = refl
    sound (invert c) = sym (sound c)
    sound (concatenate c c') = sound c ∙ sound c'
    sound (law {q} {d} {e} w) = boundary d ∙∙ interpret-law q d e w ∙∙ sym (boundary e)
    sound (congruence r ts us cs) =
      cong (V.Algebra.on-rule A r) (funExt (λ i → sound (cs i)))

    -- Exact witness preservation as a dependent square. This does not
    -- assume that interpreted path spaces are propositions or sets.
    sound-square : {q : U.Complete} {d e : R.Resolve S q} (c : G.Generated d e)
      → PathP (λ i → boundary d i ≡ boundary e i) (sound (transfer c)) (G.sound c)
    sound-square (G.reflexive d) i = refl
    sound-square (G.invert c) i = sym (sound-square c i)
    sound-square (G.concatenate c c') i = sound-square c i ∙ sound-square c' i
    sound-square (G.law {q} {d} {e} w) i =
      doubleCompPath-filler (boundary d) (interpret-law q d e w) (sym (boundary e)) (~ i)
    sound-square (G.congruence r ds es cs) j =
      cong (V.Algebra.on-rule A r) (funExt (λ i → sound-square (cs i) j))

    reflect : {q : U.Complete} {t u : B.Term S q}
      → Generated t u → G.Generated (B.decode t) (B.decode u)
    reflect (reflexive t) = G.reflexive (B.decode t)
    reflect (invert c) = G.invert (reflect c)
    reflect (concatenate c c') = G.concatenate (reflect c) (reflect c')
    reflect (law {q} {d} {e} w) = subst2 (λ d e → G.Generated {q} d e)
      (sym (B.decode-encode d)) (sym (B.decode-encode e)) (G.law w)
    reflect (congruence r ts us cs) = G.congruence r
      (λ i → B.decode (ts i)) (λ i → B.decode (us i)) (λ i → reflect (cs i))

    reflect-sound : {q : U.Complete} {t u : B.Term S q} (c : Generated t u)
      → sound c ≡ G.sound (reflect c)
    reflect-sound (reflexive t) = refl
    reflect-sound (invert c) = cong sym (reflect-sound c)
    reflect-sound (concatenate c c') = cong₂ _∙_ (reflect-sound c) (reflect-sound c')
    reflect-sound (law {q} {d} {e} w) =
      sym (fromPathP (symP (sound-square (G.law w)))) ∙
      fromPathP (λ i → G.sound (subst2-filler (λ d e → G.Generated {q} d e)
        (sym (B.decode-encode d)) (sym (B.decode-encode e)) (G.law w) i))
    reflect-sound (congruence r ts us cs) j =
      cong (V.Algebra.on-rule A r) (funExt (λ i → reflect-sound (cs i) j))

    transport-injective : {X Y : Type (ℓ-suc ℓ)} (P : X ≡ Y) {x y : X}
      → transport P x ≡ transport P y → x ≡ y
    transport-injective P {x} {y} equality =
      sym (transport⁻Transport P x) ∙ cong (transport⁻ P) equality ∙ transport⁻Transport P y

    -- CONDITIONAL completeness for each actual witness on encoded inputs.
    -- The source Completeness obligation is an input, not established here.
    image-complete : G.Completeness → (q : U.Complete) (d e : R.Resolve S q)
      → (p : Semantic (B.encode d) (B.encode e))
      → Σ (Generated (B.encode d) (B.encode e)) (λ c → sound c ≡ p)
    image-complete complete q d e p with complete q d e
      (transport (λ i → boundary d i ≡ boundary e i) p)
    ... | c , agreement = transfer c , transport-injective
      (λ i → boundary d i ≡ boundary e i) (fromPathP (sound-square c) ∙ agreement)
