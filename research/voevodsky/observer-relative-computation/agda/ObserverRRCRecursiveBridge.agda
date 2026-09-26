{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverRRCRecursiveBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
import WholePackageSigmaPi as W
import WholePackageResolution as RRC
import ResolutionNetDependentSubstitution as DSC

-- Signature-relative syntax extension, NOT a derivation of RRC's primitive
-- generators from DSC composition alone. No Resolve subtree payloads.
module Bridge (ℓ : Level) where
  module U = W.Universe ℓ
  module R = RRC.Generators ℓ
  module D = DSC.Dependent {ℓ-suc ℓ}
  Source = U.Complete → Type (ℓ-suc ℓ)

  data Term (S : Source) : U.Complete → Type (ℓ-suc ℓ) where
    var : {q : U.Complete} → S q → Term S q
    call : (r : R.Rule) → ((i : R.Arity r) → Term S (R.input r i)) → Term S (R.output r)

  encode : {S : Source} {q : U.Complete} → R.Resolve S q → Term S q
  encode (R.seed s) = var s
  encode (R.apply r ds) = call r (λ i → encode (ds i))

  decode : {S : Source} {q : U.Complete} → Term S q → R.Resolve S q
  decode (var s) = R.seed s
  decode (call r ts) = R.apply r (λ i → decode (ts i))

  decode-encode : {S : Source} {q : U.Complete} (d : R.Resolve S q) → decode (encode d) ≡ d
  decode-encode (R.seed s) = refl
  decode-encode (R.apply r ds) j = R.apply r (λ i → decode-encode (ds i) j)

  encode-decode : {S : Source} {q : U.Complete} (t : Term S q) → encode (decode t) ≡ t
  encode-decode (var s) = refl
  encode-decode (call r ts) j = call r (λ i → encode-decode (ts i) j)

  representation : (S : Source) (q : U.Complete) → R.Resolve S q ≃ Term S q
  representation S q = isoToEquiv (iso encode decode encode-decode decode-encode)

  rename : {S T : Source} → ((q : U.Complete) → S q → T q) → {q : U.Complete} → Term S q → Term T q
  rename f (var s) = var (f _ s)
  rename f (call r ts) = call r (λ i → rename f (ts i))

  bind : {S T : Source} → ((q : U.Complete) → S q → Term T q) → {q : U.Complete} → Term S q → Term T q
  bind f (var s) = f _ s
  bind f (call r ts) = call r (λ i → bind f (ts i))

  seed-map-compatible : {S T : Source} (f : (q : U.Complete) → S q → T q)
    {q : U.Complete} (d : R.Resolve S q) → encode (R.mapSeeds f d) ≡ rename f (encode d)
  seed-map-compatible f (R.seed s) = refl
  seed-map-compatible f (R.apply r ds) j = call r (λ i → seed-map-compatible f (ds i) j)

  flatten-compatible : {S : Source} {q : U.Complete} (d : R.Resolve (R.Resolve S) q)
    → encode (R.flatten d) ≡ bind (λ _ h → encode h) (encode d)
  flatten-compatible (R.seed d) = refl
  flatten-compatible (R.apply r ds) j = call r (λ i → flatten-compatible (ds i) j)

  substitution-compatible : {S T : Source} (f : (q : U.Complete) → S q → R.Resolve T q)
    {q : U.Complete} (d : R.Resolve S q)
    → encode (R.flatten (R.mapSeeds f d)) ≡ bind (λ q s → encode (f q s)) (encode d)
  substitution-compatible f (R.seed s) = refl
  substitution-compatible f (R.apply r ds) j = call r (λ i → substitution-compatible f (ds i) j)

  bind-unit : {S : Source} {q : U.Complete} (t : Term S q) → bind (λ _ → var) t ≡ t
  bind-unit (var s) = refl
  bind-unit (call r ts) j = call r (λ i → bind-unit (ts i) j)

  bind-associative : {S T V : Source}
    (f : (q : U.Complete) → S q → Term T q) (g : (q : U.Complete) → T q → Term V q)
    {q : U.Complete} (t : Term S q)
    → bind g (bind f t) ≡ bind (λ q s → bind g (f q s)) t
  bind-associative f g (var s) = refl
  bind-associative f g (call r ts) j = call r (λ i → bind-associative f g (ts i) j)

  -- Actual DSC dependent execute reconstructs one recursive syntax node.
  -- All generator evidence is supplied in the explicit Rule signature.
  Boundary : Source → Type (ℓ-suc ℓ)
  Boundary S = Σ R.Rule (λ r → (i : R.Arity r) → Term S (R.input r i))

  assemble : {S : Source} (b : Boundary S) → Term S (R.output (fst b))
  assemble (r , ts) = call r ts

  execute : {S : Source} {Γ : Type (ℓ-suc ℓ)} (r : Γ → R.Rule)
    → ((γ : Γ) → (i : R.Arity (r γ)) → Term S (R.input (r γ) i))
    → (γ : Γ) → Term S (R.output (r γ))
  execute = D.execute (λ b → Term _ (R.output (fst b))) assemble
