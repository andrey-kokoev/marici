{-# OPTIONS --safe --cubical --guardedness #-}
module ScalarActionWeights where
open import Cubical.Foundations.Prelude
import Cubical.Data.Empty as Empty
import Cubical.Data.Nat as N
import Cubical.Data.Int as Z
import Cubical.Data.NatPlusOne as P
import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing.Base
import SignedComponentArithmetic as S
import RationalComponentArithmetic as R
import ScalarActionDerivatives as D
import ScalarSixKernel as K
import ScalarSixFixture as Source
import NativeScalarFiberFixture as Reference
import NativeRationalComponentArithmetic as Native

module Action = D.Action R.rationalRing
half inv24 : R.Rational
half = R.fraction S.one (P.1+ 1)
inv24 = R.fraction S.one (P.1+ 23)
numeral-two : Action.W.numeral 2 ≡ R.fraction (S.fromInt (Z.pos 2)) (P.1+ 0)
numeral-two = R.faithful (Q.eq/ _ _ refl)
numeral-24 : Action.W.numeral 24 ≡ R.fraction (S.fromInt (Z.pos 24)) (P.1+ 0)
numeral-24 = R.faithful (Q.eq/ _ _ refl)
half-inverse : R.multiply (Action.W.numeral 2) half ≡ R.one
half-inverse = cong (λ x → R.multiply x half) numeral-two ∙ R.positive-inverse (P.1+ 1)
inv24-inverse : R.multiply (Action.W.numeral 24) inv24 ≡ R.one
inv24-inverse = cong (λ x → R.multiply x inv24) numeral-24 ∙ R.positive-inverse (P.1+ 23)
normalized-hessian : (k : R.Rational) → Action.at-zero (Action.derivative (Action.derivative (Action.quadratic k half))) ≡ k
normalized-hessian k = Action.hessian k half half-inverse
normalized-vertex : (g : R.Rational) → Action.at-zero (Action.derivative (Action.derivative (Action.derivative (Action.derivative (Action.quartic g inv24))))) ≡ R.negate g
normalized-vertex g = Action.vertex g inv24 inv24-inverse

-- Algorithmic inversion: all nonzero signed integers, no reciprocal lookup.
reciprocal : (z : Z.ℤ) → (z ≡ Z.pos 0 → Empty.⊥) → R.Rational
reciprocal (Z.pos N.zero) nonzero = Empty.rec (nonzero refl)
reciprocal (Z.pos (N.suc n)) nonzero = R.fraction S.one (P.1+ n)
reciprocal (Z.negsuc n) nonzero = R.fraction (S.negate S.one) (P.1+ n)
reciprocal-law : (z : Z.ℤ) (nonzero : z ≡ Z.pos 0 → Empty.⊥) →
  R.multiply (R.embed-signed (S.fromInt z)) (reciprocal z nonzero) ≡ R.one
reciprocal-law (Z.pos N.zero) nonzero = Empty.rec (nonzero refl)
reciprocal-law (Z.pos (N.suc n)) nonzero = R.positive-inverse (P.1+ n)
reciprocal-law (Z.negsuc n) nonzero = R.faithful
  (R.Multiply.preserves (R.embed-signed (S.fromInt (Z.negsuc n))) (reciprocal (Z.negsuc n) nonzero)
    ∙ Q.eq/ _ _ (Z.·IdR (Z.negsuc n Z.· Z.negsuc 0) ∙ Z.·Comm (Z.negsuc n) (Z.negsuc 0)
      ∙ sym (Z.-DistL· (Z.pos 1) (Z.negsuc n))
      ∙ cong (λ d → Z.pos (P.ℕ₊₁→ℕ d)) (sym (P.·₊₁-identityˡ (P.1+ n)))))

-- Metric, external data and action coupling are declared source inputs.
-- The actual inverse and vertex values are now computed, not supplied tables.
component : (K.Momentum → Z.ℤ) → Reference.Channel → S.Signed
component f c = S.add (S.fromInt (f (Source.momenta K.l0)))
  (S.add (S.fromInt (f (Source.momenta (K.Pair.left (Reference.attachment c)))))
    (S.fromInt (f (Source.momenta (K.Pair.right (Reference.attachment c))))))
kernel : Reference.Channel → S.Signed
kernel c = S.add (S.multiply (component K.Momentum.e c) (component K.Momentum.e c))
  (S.negate (S.add (S.multiply (component K.Momentum.x c) (component K.Momentum.x c))
    (S.add (S.multiply (component K.Momentum.y c) (component K.Momentum.y c))
      (S.multiply (component K.Momentum.z c) (component K.Momentum.z c)))))
nonpole : (c : Reference.Channel) → S.asInt (kernel c) ≡ Z.pos 0 → Empty.⊥
nonpole Reference.c12 p = N.snotz (cong Z.abs p)
nonpole Reference.c13 p = N.snotz (cong Z.abs p)
nonpole Reference.c14 p = N.snotz (cong Z.abs p)
nonpole Reference.c15 p = N.snotz (cong Z.abs p)
nonpole Reference.c23 p = N.snotz (cong Z.abs p)
nonpole Reference.c24 p = N.snotz (cong Z.abs p)
nonpole Reference.c25 p = N.snotz (cong Z.abs p)
nonpole Reference.c34 p = N.snotz (cong Z.abs p)
nonpole Reference.c35 p = N.snotz (cong Z.abs p)
nonpole Reference.c45 p = N.snotz (cong Z.abs p)
coupling : R.Rational
coupling = R.fraction (S.fromInt Source.couplingNumerator) (P.1+ 4)
coupling-denominator : Z.pos 5 ≡ Source.couplingDenominator
coupling-denominator = refl
weight : R.Rational → Reference.Channel → R.Rational
weight g c = R.multiply (R.negate (R.multiply g g)) (reciprocal (S.asInt (kernel c)) (nonpole c))
reference-weight : Reference.Channel → R.Rational
reference-weight c = R.fraction (S.fromInt (Reference.weight c)) (P.1+ 599)
weight-agrees : (c : Reference.Channel) → weight coupling c ≡ reference-weight c
weight-agrees Reference.c12 = R.faithful (Q.eq/ _ _ refl)
weight-agrees Reference.c13 = R.faithful (Q.eq/ _ _ refl)
weight-agrees Reference.c14 = R.faithful (Q.eq/ _ _ refl)
weight-agrees Reference.c15 = R.faithful (Q.eq/ _ _ refl)
weight-agrees Reference.c23 = R.faithful (Q.eq/ _ _ refl)
weight-agrees Reference.c24 = R.faithful (Q.eq/ _ _ refl)
weight-agrees Reference.c25 = R.faithful (Q.eq/ _ _ refl)
weight-agrees Reference.c34 = R.faithful (Q.eq/ _ _ refl)
weight-agrees Reference.c35 = R.faithful (Q.eq/ _ _ refl)
weight-agrees Reference.c45 = R.faithful (Q.eq/ _ _ refl)

-- Same native grammar admits distinct normalized quartic couplings.
-- These are different marked inputs, not identical complete packages.
module CouplingCounterexample where
  data Factor : Type where vertex : Factor
  first second : R.Rational
  first = coupling
  second = R.fraction (S.fromInt (Z.pos 6)) (P.1+ 4)
  module A = Native.FractionBridge Factor (λ _ → R.negate first)
  module B = Native.FractionBridge Factor (λ _ → R.negate second)
  first-run : A.Native.E.Run.Resolve (A.Native.E.package (A.Native.E.factor vertex))
  first-run = A.Native.E.native-run (A.Native.E.factor vertex)
  second-run : B.Native.E.Run.Resolve (B.Native.E.package (B.Native.E.factor vertex))
  second-run = B.Native.E.native-run (B.Native.E.factor vertex)
  readouts-distinct : R.asRational (A.Native.E.readout (A.Native.E.factor vertex) (snd (A.Native.E.package (A.Native.E.factor vertex))))
    ≡ R.asRational (B.Native.E.readout (B.Native.E.factor vertex) (snd (B.Native.E.package (B.Native.E.factor vertex)))) → Empty.⊥
  readouts-distinct p = N.znots (cong (λ z → Z.abs z N.∸ 15) (Q.eq/⁻¹ _ _ p))
