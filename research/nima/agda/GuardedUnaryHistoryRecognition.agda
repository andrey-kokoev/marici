{-# OPTIONS --safe --cubical --guardedness #-}
module GuardedUnaryHistoryRecognition where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels using (isContr→isContrPath)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Whole
import WholePackageResolution as OldResolution
import RetainedTransportResolution as Transport
import GuardedTransportComparisonBasis as Basis

module Recognition (ℓ : Level) (Q : Whole.Universe.Code ℓ) (initial : Whole.Universe.El ℓ Q) where
  open Whole.Universe ℓ
  module B = Basis.Basis ℓ Q
  module H = B.H
  module C = B.C
  module T = Transport.Extension ℓ
  module Old = OldResolution.Generators ℓ
  open H.Presentation

  source : Complete
  source = pack Q initial

  data Source : Complete → Type (ℓ-suc ℓ) where
    origin : Source source

  Normal = H.N.Value (H.N.normal Q)
  Chart : Complete → Type ℓ
  Chart q = El (expression q) ≃ Normal

  presented : (q : Complete) → Chart q → H.Presentation
  presented q c = H.presentation (expression q) c

  -- Annotates EXISTING raw extension histories. It does not ask that they
  -- were produced by the route compiler. Every actual transport e is kept.
  data Guarded : {q : Complete} → T.ResolveT Source q → Chart q → Type (ℓ-suc ℓ) where
    base : Guarded (T.seedT origin) (H.N.normalize-equiv Q)
    move : (a : Complete) (R : Code) (e : El (expression a) ≃ El R)
      (d : T.ResolveT Source a) (c : Chart a) (c' : Chart (T.transported a R e))
      → Guarded d c
      → ((x : El (expression a)) → equivFun c' (equivFun e x) ≡ equivFun c x)
      → Guarded (T.transportT a R e d) c'

  append : {P R U : H.Presentation} → H.Route P R → H.Route R U → H.Route P U
  append H.stop b = b
  append (H.next {R = R} f tail) b = H.next {R = R} f (append tail b)

  append-effect : {P R U : H.Presentation} (a : H.Route P R) (b : H.Route R U)
    (x : El (expression P)) → C.N.execute (append a b) x ≡ C.N.execute b (C.N.execute a x)
  append-effect H.stop b x = refl
  append-effect (H.next f tail) b x = append-effect tail b (fst (f x))

  actual : {q : Complete} {d : T.ResolveT Source q} {c : Chart q}
    → Guarded d c → El Q → El (expression q)
  actual base x = x
  actual (move a R e d c c' g h) x = equivFun e (actual g x)

  actual-at-source : {q : Complete} {d : T.ResolveT Source q} {c : Chart q}
    (g : Guarded d c) → actual g initial ≡ value q
  actual-at-source base = refl
  actual-at-source (move a R e d c c' g h) = cong (equivFun e) (actual-at-source g)

  coordinates-preserved : {q : Complete} {d : T.ResolveT Source q} {c : Chart q}
    (g : Guarded d c) (x : El Q) → equivFun c (actual g x) ≡ H.N.normalize Q x
  coordinates-preserved base x = refl
  coordinates-preserved (move a R e d c c' g h) x = h (actual g x) ∙ coordinates-preserved g x

  decode : {q : Complete} {d : T.ResolveT Source q} {c : Chart q}
    → Guarded d c → H.Route H.original (presented q c)
  decode base = H.stop
  decode (move a R e d c c' g h) = append (decode g)
    (H.next {P = presented a c} {R = presented (T.transported a R e) c'}
      (λ x → equivFun e x , h x) H.stop)

  decode-effect : {q : Complete} {d : T.ResolveT Source q} {c : Chart q}
    (g : Guarded d c) (x : El Q) → C.N.execute (decode g) x ≡ actual g x
  decode-effect base x = refl
  decode-effect (move a R e d c c' g h) x =
    append-effect (decode g)
      (H.next {P = presented a c} {R = presented (T.transported a R e) c'}
        (λ y → equivFun e y , h y) H.stop) x
    ∙ cong (equivFun e) (decode-effect g x)

  finish : (q : Complete) (c : Chart q) → H.Route (presented q c) H.normal
  finish q c = H.next {P = presented q c} {R = H.normal} (λ x → equivFun c x , refl) H.stop

  to-normal : {q : Complete} {d : T.ResolveT Source q} {c : Chart q}
    → Guarded d c → H.Route H.original H.normal
  to-normal {q} {c = c} g = append (decode g) (finish q c)

  normal-effect : {q : Complete} {d : T.ResolveT Source q} {c : Chart q}
    (g : Guarded d c) (x : El Q)
    → C.N.execute (to-normal g) x ≡ equivFun c (actual g x)
  normal-effect {q} {c = c} g x = append-effect (decode g) (finish q c) x
    ∙ cong (equivFun c) (decode-effect g x)

  observed : {q : Complete} {d : T.ResolveT Source q} {c : Chart q}
    → Guarded d c → H.CoherentMap H.original H.normal
  observed {c = c} g x = equivFun c (actual g x) , coordinates-preserved g x

  decoded-agrees : {q : Complete} {d : T.ResolveT Source q} {c : Chart q}
    (g : Guarded d c) → B.observe (to-normal g) ≡ observed g
  decoded-agrees g = H.compare-maps {H.original} {H.normal} _ _

  module Pair {q r : Complete} {d : T.ResolveT Source q} {e : T.ResolveT Source r}
    {c : Chart q} {c' : Chart r} (g : Guarded d c) (h : Guarded e c') where
    Semantic : Type ℓ
    Semantic = observed g ≡ observed h

    Derivation : Type (ℓ-suc ℓ)
    Derivation = B.Generated (to-normal g) (to-normal h)

    sound : Derivation → Semantic
    sound proof = sym (decoded-agrees g) ∙ B.sound proof ∙ decoded-agrees h

    completeness : (p : Semantic) → Σ[ proof ∈ Derivation ] (sound proof ≡ p)
    completeness p = proof , isContr→isProp comparison-space (sound proof) p
      where
      proof = B.compare (to-normal g) (to-normal h)
      comparison-space = isContr→isContrPath (H.map-contractible H.original H.normal) (observed g) (observed h)

    endpoint-effect : Semantic → equivFun c (value q) ≡ equivFun c' (value r)
    endpoint-effect p = sym (cong (equivFun c) (actual-at-source g))
      ∙ cong (λ f → C.N.underlying {H.original} {H.normal} f initial) p
      ∙ cong (equivFun c') (actual-at-source h)

  record Retained : Type (ℓ-suc ℓ) where
    field
      source-packet : Complete
      source-agrees : source-packet ≡ source
      first-endpoint second-endpoint : Complete
      first-history : T.ResolveT Source first-endpoint
      second-history : T.ResolveT Source second-endpoint
      first-chart : Chart first-endpoint
      second-chart : Chart second-endpoint
      first-guard : Guarded first-history first-chart
      second-guard : Guarded second-history second-chart
      witness : Pair.Semantic first-guard second-guard
      derivation : Pair.Derivation first-guard second-guard
      reconstructs : Pair.sound first-guard second-guard derivation ≡ witness
      endpoint-witness : equivFun first-chart (value first-endpoint)
        ≡ equivFun second-chart (value second-endpoint)

  retain-recognition : {q r : Complete} {d : T.ResolveT Source q} {e : T.ResolveT Source r}
    {c : Chart q} {c' : Chart r} (g : Guarded d c) (h : Guarded e c')
    → Pair.Semantic g h → Retained
  retain-recognition {q} {r} {d} {e} {c} {c'} g h p = record
    { source-packet = source ; source-agrees = refl
    ; first-endpoint = q ; second-endpoint = r
    ; first-history = d ; second-history = e
    ; first-chart = c ; second-chart = c'
    ; first-guard = g ; second-guard = h
    ; witness = p ; derivation = fst proof ; reconstructs = snd proof
    ; endpoint-witness = Pair.endpoint-effect g h p }
    where
    proof = Pair.completeness g h p

  next-Q : Retained → Whole.Universe.Complete (ℓ-suc ℓ)
  next-Q r = Whole.Universe.pack (Whole.Universe.atom Retained) r

  -- Explicit frontier: native branching nodes are not silently recognized.
  native-not-recognized : (r : Old.Rule)
    (ds : (i : Old.Arity r) → T.ResolveT Source (Old.input r i))
    (c : Chart (Old.output r)) → Guarded (T.nativeT r ds) c → ⊥
  native-not-recognized r ds c ()
