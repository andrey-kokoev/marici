{-# OPTIONS --safe --cubical --guardedness #-}
module AssociativeDomainComposition where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (Iso; iso)
import MetaWitnessGenerator as Meta
import TripleWitnessSpecialization as Triple
import ComposeDomainWitness as Compose
import WitnessSelectionGenerator as Selection
import ReSpecializeWitnessSelection as First
import TripleWitnessSpecialization as TripleExample
import NestedWitnessSpecialization as Nested
open import Cubical.Data.Unit.Base using (tt)

-- A relative three-domain association test. The two pairwise source
-- compositions are actual proof-relevant FullComposition packages.
module Association {ℓ : Level} (S : Type ℓ) (R : S → S → Type ℓ)
  (first : Meta.Specialize.Compatible S R) where
  module T = Triple.Triple S R first
  module Pair12 = Compose.Composition S R first

  module AfterSecond (domain2 : T.N.M2.Domain)
    (agree2 : (v : T.N.C1.State)
      → fst (T.N.C1.generator v) ≡ T.N.M2.Domain.compute domain2 v)
    (closed2 : (v : T.N.C1.State) → T.N.M2.Domain.Allowed domain2 v
      → T.N.M2.Domain.Allowed domain2 (fst (T.N.C1.generator v))) where
    module B = T.AfterSecond domain2 agree2 closed2
    module LeftPair = Pair12.WithSecond domain2 agree2 closed2
    module Pair23 = Compose.Composition T.N.C1.State T.N.C1.Relation B.Two.second

    module AfterThird (domain3 : B.M3.Domain)
      (agree3 : (v : B.Two.C2.State)
        → fst (B.Two.C2.generator v) ≡ B.M3.Domain.compute domain3 v)
      (closed3 : (v : B.Two.C2.State) → B.M3.Domain.Allowed domain3 v
        → B.M3.Domain.Allowed domain3 (fst (B.Two.C2.generator v))) where
      module C = B.AfterThird domain3 agree3 closed3
      module RightPair = Pair23.WithSecond domain3 agree3 closed3

      -- Left grouping is (D1,D2),D3. Right grouping is D1,(D2,D3).
      -- A FullComposition is retained on either side, not only its readout.
      record Grouped : Type (ℓ-suc ℓ) where
        field
          left-pair : LeftPair.FullComposition
          left-certified : left-pair ≡ LeftPair.full-composition
          right-pair : RightPair.FullComposition
          right-certified : right-pair ≡ RightPair.full-composition
          associator : (v : C.C3.State) → Iso (C.StepLeft v) (C.StepRight v)
          generated-compatible : (v : C.C3.State)
            → Iso.fun (associator v) (C.generated-left v) ≡ C.generated-right v

      compose-three : Grouped
      compose-three = record
        { left-pair = LeftPair.full-composition
        ; left-certified = refl
        ; right-pair = RightPair.full-composition
        ; right-certified = refl
        ; associator = C.step-reassociate
        ; generated-compatible = C.generated-step-agrees }

      left-source-recovered :
        LeftPair.FullComposition.first-source (Grouped.left-pair compose-three) ≡ first
      left-source-recovered = refl
      right-source-recovered :
        RightPair.FullComposition.first-source (Grouped.right-pair compose-three)
          ≡ B.Two.second
      right-source-recovered = refl

      -- The first half of the triple step is exactly the full two-domain
      -- witness, before adding the third admission/comparison shell.
      first-pair-witness : (v : C.C3.State)
        → fst (snd (C.C3.generator v)) ≡
          snd (LeftPair.Two.C2.generator (fst v))
      first-pair-witness v = refl

      second-pair-witness : (s : S) (p : T.N.M1.Domain.Allowed (T.N.M1.Compatible.domain first) s)
        (q : T.N.M2.Domain.Allowed domain2 (s , p))
        (r : B.M3.Domain.Allowed domain3 ((s , p) , q))
        → snd (C.C3.generator (((s , p) , q) , r)) ≡
          snd (RightPair.full-generator ((s , p) , q , r))
      second-pair-witness s p q r = refl

module SelectionFixture where
  module A = Association Selection.State Selection.SelectionWitness First.selection-pair
  module B = A.AfterSecond Nested.Example.second-domain (λ v → refl) (λ v ok → ok)
  module C = B.AfterThird TripleExample.SelectionExample.third-domain
    (λ v → refl) (λ v ok → ok)
  request : C.C.C3.State
  request = Nested.Example.request , lift tt
  concrete-associator :
    Iso.fun (C.Grouped.associator C.compose-three request)
      (C.C.generated-left request) ≡ C.C.generated-right request
  concrete-associator = C.Grouped.generated-compatible C.compose-three request
