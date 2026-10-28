{-# OPTIONS --safe --cubical --guardedness #-}
module NativeResolvedDomainRepresentation where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (equivFun; invEq; retEq)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import NativeTableResolution as Native
import RetainedDomainRepresentation as Retained

-- Covers every actual original retained derivation under every source policy S.
-- Does not replace S by universal admission, or invent a derivation of a target.
module ForSource (ℓ : Level)
  (S : Whole.Universe.Complete ℓ → Type (ℓ-suc ℓ)) where
  module R = Resolution.Generators ℓ
  module N = Native.ForOldSeeds ℓ S
  module Next = Whole.Universe (ℓ-suc ℓ)

  Domain = R.Closure S
  NativeDomain = N.F.Closed

  reified-history-recovered : (d : Domain)
    → Next.value (R.reify-history (snd d)) ≡ d
  reified-history-recovered d = refl

  module Views (A B C : Type (ℓ-suc ℓ))
    (first : NativeDomain → A)
    (second : NativeDomain → B)
    (third : NativeDomain → C) where
    module T = Retained.Representation NativeDomain A B C first second third

    encode : Domain → T.TriangleRecord
    encode d = T.encode (equivFun N.closure-equivalence d)

    decode : T.TriangleRecord → Domain
    decode t = invEq N.closure-equivalence (T.decode t)

    recovered : (d : Domain) → decode (encode d) ≡ d
    recovered d =
      cong (invEq N.closure-equivalence)
        (T.decode-encode (equivFun N.closure-equivalence d))
      ∙ retEq N.closure-equivalence d

    endpoint-recovered : (d : Domain)
      → fst (decode (encode d)) ≡ fst d
    endpoint-recovered d = cong fst (recovered d)

    observe : {κ : Level} {O : Type κ} → (Domain → O) → T.TriangleRecord → O
    observe read t = read (decode t)

    observation-preserved : {κ : Level} {O : Type κ}
      (read : Domain → O) (d : Domain)
      → observe read (encode d) ≡ read d
    observation-preserved read d = cong read (recovered d)

    execute : (Domain → Domain) → T.TriangleRecord → T.TriangleRecord
    execute f t = encode (f (decode t))

    execute-composes : (f g : Domain → Domain) (t : T.TriangleRecord)
      → execute g (execute f t) ≡ execute (λ d → g (f d)) t
    execute-composes f g t =
      cong (λ d → encode (g d)) (recovered (f (decode t)))

    execute-on-encoded : (f : Domain → Domain) (d : Domain)
      → execute f (encode d) ≡ encode (f d)
    execute-on-encoded f d = cong (λ x → encode (f x)) (recovered d)
