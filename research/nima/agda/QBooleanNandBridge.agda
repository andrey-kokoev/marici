{-# OPTIONS --safe --cubical --guardedness #-}
module QBooleanNandBridge where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence using (pathToEquiv)
open import Cubical.Data.Bool.Base using (Bool; false)
open import Cubical.Data.Bool.Properties using (isSetBool)
import NandConstructions as N
import WholePackageSigmaPi as Whole
open import BooleanNandEquivalence

module Theory = FromWolfram Bool isSetBool false N.nand N.wolfram
module B = BooleanStructure Theory.boolean

-- The actual Q/E/P type construction realizes NAND in the Boolean
-- structure reconstructed from Wolfram's identity.
q-realization : (a b : Bool)
  → Whole.Universe.El ℓ-zero (N.nandCode (N.Truth a) (N.Truth b))
      ≃ N.Truth (B.neg (B.meet a b))
q-realization a b = compEquiv (N.nand-realization a b)
  (pathToEquiv (cong N.Truth (Theory.recovered-operation a b)))
