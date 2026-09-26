{-# OPTIONS --safe --cubical --guardedness #-}
module NativeBranchBoundaryCoordinates where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import DependentPackageNormalization as Normal
import DependentNormalizationCoherence as Coherence
import SingleSourceRouteCompiler as Compiler
import GuardedTransportComparisonBasis as Basis
import ProofRelevantCoherenceClosure as Paths

module Boundaries (ℓ : Level)
  (S : Whole.Universe.Complete ℓ → Type (ℓ-suc ℓ)) where
  open Whole.Universe ℓ
  module Old = Resolution.Generators ℓ
  module High = Whole.Universe (ℓ-suc ℓ)
  module N = Normal.Normalization (ℓ-suc ℓ)

  -- Family entries are COMPLETE packages. Child derivations are explicit
  -- data too, including unselected children of a native E application.
  E-fixed : (I : Type ℓ) → High.Code
  E-fixed I = High.E (I → Complete) (λ F →
    High.E ((i : I) → Old.Resolve S (F i)) (λ ds →
      High.atom (Lift {j = ℓ-suc ℓ} I)))

  Pi-fixed : (I : Type ℓ) → High.Code
  Pi-fixed I = High.E (I → Complete) (λ F →
    High.atom ((i : I) → Old.Resolve S (F i)))

  -- Even the index TYPE is retained as boundary data; none is enumerated.
  E-input Pi-input : High.Code
  E-input = High.E (Type ℓ) E-fixed
  Pi-input = High.E (Type ℓ) Pi-fixed

  evaluate-E-fixed : (I : Type ℓ) → High.El (E-fixed I) → Old.Closure S
  evaluate-E-fixed I (F , ds , lift i) = E-package I F i ,
    Old.apply (Old.E-rule I F i) (λ { (lift j) → ds j })

  evaluate-Pi-fixed : (I : Type ℓ) → High.El (Pi-fixed I) → Old.Closure S
  evaluate-Pi-fixed I (F , ds) = Pi-package I F ,
    Old.apply (Old.Pi-rule I F) (λ { (lift i) → ds i })

  evaluate-E : High.El E-input → Old.Closure S
  evaluate-E (I , b) = evaluate-E-fixed I b

  evaluate-Pi : High.El Pi-input → Old.Closure S
  evaluate-Pi (I , b) = evaluate-Pi-fixed I b

  -- The same construction also retains every field of any native rule head.
  Rule-input : High.Code
  Rule-input = High.E Old.Rule (λ r → High.atom ((i : Old.Arity r) → Old.Resolve S (Old.input r i)))

  evaluate-rule : High.El Rule-input → Old.Closure S
  evaluate-rule (r , ds) = Old.output r , Old.apply r ds

  E-to-rule : High.El E-input → High.El Rule-input
  E-to-rule (I , F , ds , lift i) = Old.E-rule I F i , (λ { (lift j) → ds j })

  Pi-to-rule : High.El Pi-input → High.El Rule-input
  Pi-to-rule (I , F , ds) = Old.Pi-rule I F , (λ { (lift i) → ds i })

  E-evaluation-agrees : (b : High.El E-input) → evaluate-rule (E-to-rule b) ≡ evaluate-E b
  E-evaluation-agrees (I , F , ds , lift i) = refl

  Pi-evaluation-agrees : (b : High.El Pi-input) → evaluate-rule (Pi-to-rule b) ≡ evaluate-Pi b
  Pi-evaluation-agrees (I , F , ds) = refl

  -- A full application is its whole boundary, actual native output closure,
  -- and an equality certifying evaluation. The output code may vary with b.
  module Application (Input : High.Code) (evaluate : High.El Input → Old.Closure S) where
    Output : High.Code
    Output = High.E (High.El Input) (λ b →
      High.E (Old.Closure S) (λ out → High.atom (evaluate b ≡ out)))

    enter : High.El Input → High.El Output
    enter b = b , evaluate b , refl

    boundary-equiv : High.El Input ≃ High.El Output
    boundary-equiv = isoToEquiv (iso enter fst
      (λ { (b , out , p) t → b , p t , (λ u → p (t ∧ u)) })
      (λ _ → refl))

    coordinates : High.El Output ≃ N.Value (N.normal Input)
    coordinates = compEquiv (invEquiv boundary-equiv) (N.normalize-equiv Input)

    application-paths : {v w : High.El Output}
      → (v ≡ w) ≃ (equivFun coordinates v ≡ equivFun coordinates w)
    application-paths = Paths.pathLift coordinates

    application-higher : {v w : High.El Output} (p q : v ≡ w)
      → (p ≡ q) ≃ (cong (equivFun coordinates) p ≡ cong (equivFun coordinates) q)
    application-higher = Paths.higherLift coordinates

    recover-boundary : (b : High.El Input) → fst (enter b) ≡ b
    recover-boundary b = refl

    reconstruct-application : (v : High.El Output) → enter (fst v) ≡ v
    reconstruct-application = secEq boundary-equiv

    module H = Coherence.Coherence (ℓ-suc ℓ) Input
    module C = Compiler.Compiler (ℓ-suc ℓ) Input
    module B = Basis.Basis (ℓ-suc ℓ) Input

    output-presentation : H.Presentation
    output-presentation = H.presentation Output coordinates

    evaluate-map : H.CoherentMap H.original output-presentation
    evaluate-map b = enter b , refl

    -- Faithful coordinates constrain the WHOLE graph, not only its input
    -- projection. This includes the output closure and evaluation witness.
    guarded-application : (f : H.CoherentMap H.original output-presentation)
      (b : High.El Input) → fst (f b) ≡ enter b
    guarded-application f b = cong (λ k → fst (k b))
      (H.compare-maps {H.original} {output-presentation} f evaluate-map)

    guarded-native-output : (f : H.CoherentMap H.original output-presentation)
      (b : High.El Input) → fst (snd (fst (f b))) ≡ evaluate b
    guarded-native-output f b = cong (λ v → fst (snd v)) (guarded-application f b)

    every-compiled-native-output : (route : H.Route H.original output-presentation)
      (b : High.El Input) →
      fst (snd (C.viewed-value (C.run route (C.start H.original b)))) ≡ evaluate b
    every-compiled-native-output route = guarded-native-output (B.observe route)

    evaluate-after-normalization : H.CoherentMap H.normal output-presentation
    evaluate-after-normalization v = enter (N.reconstruct Input v) , N.normal-roundtrip Input v

    direct normalize-first : H.Route H.original output-presentation
    direct = H.next {R = output-presentation} evaluate-map H.stop
    normalize-first = H.next {R = H.normal} H.normalize-map
      (H.next {R = output-presentation} evaluate-after-normalization H.stop)

    order-comparison : H.evaluate direct ≡ H.evaluate normalize-first
    order-comparison = H.route-comparison direct normalize-first

    native-direct : (b : High.El Input) →
      C.T.ResolveT (C.OnlySource (C.packet (C.start H.original b)))
        (C.packet (C.run direct (C.start H.original b)))
    native-direct = C.source-compile direct

    compiled-native-output : (b : High.El Input) →
      fst (snd (C.viewed-value (C.run direct (C.start H.original b)))) ≡ evaluate b
    compiled-native-output b = cong (λ v → fst (snd v)) (C.source-effect direct b)

    normalized-native-output : (b : High.El Input) →
      fst (snd (C.viewed-value (C.run normalize-first (C.start H.original b)))) ≡ evaluate b
    normalized-native-output b = cong (λ v → fst (snd v)) (C.source-effect normalize-first b)
      ∙ cong evaluate (N.source-roundtrip Input b)

    reconstruct-comparison : (p : B.Semantic direct normalize-first)
      → Σ[ proof ∈ B.Generated direct normalize-first ] (B.sound proof ≡ p)
    reconstruct-comparison = B.completeness direct normalize-first

    record Retained : Type (ℓ-suc (ℓ-suc ℓ)) where
      field
        boundary : High.El Input
        application : High.El Output
        application-agrees : application ≡ enter boundary
        route-certificate : H.Certificate
        source-only-compilation : C.Retained
        generated-comparison : B.Requested

    retain-requested : High.El Input → B.Semantic direct normalize-first → Retained
    retain-requested b p = record
      { boundary = b ; application = enter b ; application-agrees = refl
      ; route-certificate = H.certify direct normalize-first
      ; source-only-compilation = C.retain-compilation direct b
      ; generated-comparison = B.realize direct normalize-first b p }

    retain-application : High.El Input → Retained
    retain-application b = retain-requested b
      (H.compare-maps {H.original} {output-presentation} (B.observe direct) (B.observe normalize-first))

    next-requested : High.El Input → B.Semantic direct normalize-first
      → Whole.Universe.Complete (ℓ-suc (ℓ-suc ℓ))
    next-requested b p = Whole.Universe.pack (Whole.Universe.atom Retained) (retain-requested b p)

    next-Q : High.El Input → Whole.Universe.Complete (ℓ-suc (ℓ-suc ℓ))
    next-Q b = Whole.Universe.pack (Whole.Universe.atom Retained) (retain-application b)

  module E-application = Application E-input evaluate-E
  module Pi-application = Application Pi-input evaluate-Pi
  module Rule-application = Application Rule-input evaluate-rule
