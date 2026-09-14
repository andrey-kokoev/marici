{-# OPTIONS --safe --cubical --guardedness #-}
module RHBoundaryConservationIndependence where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥; rec)
open import Cubical.Data.Unit using (Unit; tt)
open import RHThetaBoundaryConservation

data Bit : Type where
  zeroBit oneBit : Bit

_⊕b_ : Bit → Bit → Bit
zeroBit ⊕b y = y
oneBit ⊕b zeroBit = oneBit
oneBit ⊕b oneBit = zeroBit

_*b_ : Bit → Bit → Bit
zeroBit *b _ = zeroBit
oneBit *b y = y

distinguish : Bit → Type
distinguish zeroBit = ⊥
distinguish oneBit = Unit

oneNotZero : oneBit ≡ zeroBit → ⊥
oneNotZero p = subst distinguish p tt

-- A finite hostile Green problem: the Green identity and the stated
-- positive-bulk cancellation both hold, while boundary work is nonzero.
hostileGreen : UnsewnGreenProblem
hostileGreen = record
  { Scalar = Bit
  ; zero = zeroBit
  ; _+_ = _⊕b_
  ; _*_ = _*b_
  ; addZeroRight = λ where
      zeroBit → refl
      oneBit → refl
  ; transverse = oneBit
  ; bulk = oneBit
  ; work = oneBit
  ; greenIdentity = refl
  ; positiveBulkCancels = λ impossible →
      rec (oneNotZero impossible)
  }

hostileWorkIsNonzero : work hostileGreen ≡ zero hostileGreen → ⊥
hostileWorkIsNonzero = oneNotZero

hostileTransverseIsNonzero :
  transverse hostileGreen ≡ zero hostileGreen → ⊥
hostileTransverseIsNonzero = oneNotZero

-- Therefore Green identity plus positive-bulk cancellation cannot construct
-- the boundary sewing premise.  Theta-section incidence must provide new data.
noGenericWorkSewing :
  ((G : UnsewnGreenProblem) → work G ≡ zero G) → ⊥
noGenericWorkSewing claimed = hostileWorkIsNonzero (claimed hostileGreen)
