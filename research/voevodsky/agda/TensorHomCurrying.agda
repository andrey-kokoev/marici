{-# OPTIONS --safe --cubical --guardedness #-}
module TensorHomCurrying where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- Signed tensor-Hom currying for graded Koszul sources.  Degrees and parity
-- are explicit so the (-1)^(pq) interchange sign cannot be suppressed.
record SignedTensorHomCurrying {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Degree Sign : Type ℓ
    even odd : Sign
    degreeAdd : Degree → Degree → Degree
    koszulSign : Degree → Degree → Sign
    KoszulA KoszulP Target : Type ℓ
    degreeA : KoszulA → Degree
    degreeP : KoszulP → Degree

    NestedHom TensorHom : Type ℓ
    nestedEvaluate : NestedHom → KoszulA → KoszulP → Target
    tensorEvaluate : TensorHom → KoszulA → KoszulP → Target
    signTarget : Sign → Target → Target

    curry : TensorHom → NestedHom
    uncurry : NestedHom → TensorHom
    currySection : (f : TensorHom) → uncurry (curry f) ≡ f
    curryRetraction : (g : NestedHom) → curry (uncurry g) ≡ g

    -- The checked convention for moving a P-wedge of degree q through an
    -- A-wedge of degree p.
    uncurryEvaluation : (g : NestedHom) (a : KoszulA) (p : KoszulP) →
      tensorEvaluate (uncurry g) a p ≡
      signTarget (koszulSign (degreeA a) (degreeP p))
        (nestedEvaluate g a p)

    DifferentialA DifferentialP DifferentialTarget : Type ℓ
    nestedDifferential : NestedHom → NestedHom
    tensorDifferential : TensorHom → TensorHom
    uncurryChainMap : (g : NestedHom) →
      tensorDifferential (uncurry g) ≡ uncurry (nestedDifferential g)
    curryChainMap : (f : TensorHom) →
      nestedDifferential (curry f) ≡ curry (tensorDifferential f)

    zeroNested : NestedHom
    zeroTensor : TensorHom
    curryZero : curry zeroTensor ≡ zeroNested
    uncurryZero : uncurry zeroNested ≡ zeroTensor

-- In particular, replacing RHom(A,RHom(P,B)) by RHom(A tensor P,B) only
-- changes presentation and signs. It cannot erase a nonzero cochain/class.
record CurriedObstructionCertificate {ℓ : Level}
  (C : SignedTensorHomCurrying {ℓ}) : Type (ℓ-suc ℓ) where
  open SignedTensorHomCurrying C
  field
    nestedObstruction : NestedHom
    nestedObstructionNonzero : nestedObstruction ≡ zeroNested → ⊥

uncurriedObstructionNonzero : {ℓ : Level}
  {C : SignedTensorHomCurrying {ℓ}} →
  (O : CurriedObstructionCertificate C) →
  SignedTensorHomCurrying.uncurry C
    (CurriedObstructionCertificate.nestedObstruction O) ≡
    SignedTensorHomCurrying.zeroTensor C → ⊥
uncurriedObstructionNonzero {C = C} O uncurriedZero =
  CurriedObstructionCertificate.nestedObstructionNonzero O
    (sym (SignedTensorHomCurrying.curryRetraction C
      (CurriedObstructionCertificate.nestedObstruction O))
    ∙ cong (SignedTensorHomCurrying.curry C) uncurriedZero
    ∙ SignedTensorHomCurrying.curryZero C)
