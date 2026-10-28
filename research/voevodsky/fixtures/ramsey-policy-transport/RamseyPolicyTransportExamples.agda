{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPolicyTransportExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Agda.Builtin.String using (String)
import RamseyRequestedPortExamples as C
import RamseyEdgeAttachmentsExamples as E
import RamseyFourFacetVertexCells as F
open import RamseySingleFrameFaces using (m0; c0)
open import RamseyExternalPEExamples
import RamseyExternalSeedPolicyExamples as Policy
import RamseyOccurrenceEquivalence as O
import RamseyExternalPEPolicy as GP
open import RamseyExternalPolicyTransport
ComplementChart : C.Chart → Type
ComplementChart C.q0 = ⊥
ComplementChart C.q1 = ⊥
ComplementChart C.q2 = ⊥
ComplementChart C.q3 = ⊥
ComplementChart C.q4 = ⊥
ComplementChart C.q5 = ⊥
ComplementChart C.q6 = ⊥
ComplementChart C.q7 = Unit
ComplementChart C.q8 = ⊥
ComplementChart C.q9 = ⊥
ComplementChart C.q10 = ⊥
ComplementChart C.q11 = ⊥
ComplementChart C.q12 = ⊥
ComplementChart C.q13 = ⊥
ComplementChart C.q14 = ⊥
ComplementChart C.q15 = ⊥
ComplementChart C.q16 = ⊥
ComplementChart C.q17 = ⊥
ComplementChart C.q18 = ⊥
ComplementChart C.q19 = ⊥
ComplementChart C.q20 = ⊥
ComplementChart C.q21 = ⊥
ComplementChart C.q22 = ⊥
ComplementChart C.q23 = ⊥
PairAllowed BaseAllowed ComplementAllowed : P.S.InputIndex → Type
PairAllowed s = Policy.PairChart (fst s)
BaseAllowed s = Policy.BaseChart (fst s)
ComplementAllowed s = ComplementChart (fst s)
payload : P.S.InputIndex → String
payload = λ { (c , (v , p)) → E.A.vertex-packet c v p }
module Complement = GP.Policy P.S.InputIndex payload ComplementAllowed
module PairTransfer = Transfer P.S.InputIndex payload PairAllowed PairAllowed
module BaseTransfer = Transfer P.S.InputIndex payload BaseAllowed ComplementAllowed
module ComplementTransfer = Transfer P.S.InputIndex payload ComplementAllowed BaseAllowed
pair-back : {x y : P.S.InputIndex} → O.Transports x y → PairAllowed y → PairAllowed x
pair-back (O.input-0-0 p) allowed = tt
pair-back (O.input-0-1 p) allowed = tt
pair-back (O.input-0-2 p) allowed = tt
pair-back (O.input-0-3 p) allowed = tt
pair-back (O.input-7-0 p) allowed = tt
pair-back (O.input-7-1 p) allowed = tt
pair-back (O.input-7-2 p) allowed = tt
pair-back (O.input-7-3 p) allowed = tt
base-back : {x y : P.S.InputIndex} → O.Transports x y → BaseAllowed y → ComplementAllowed x
base-back (O.input-0-0 p) ()
base-back (O.input-0-1 p) ()
base-back (O.input-0-2 p) ()
base-back (O.input-0-3 p) ()
base-back (O.input-7-0 p) allowed = tt
base-back (O.input-7-1 p) allowed = tt
base-back (O.input-7-2 p) allowed = tt
base-back (O.input-7-3 p) allowed = tt
complement-back : {x y : P.S.InputIndex} → O.Transports x y → ComplementAllowed y → BaseAllowed x
complement-back (O.input-0-0 p) allowed = tt
complement-back (O.input-0-1 p) allowed = tt
complement-back (O.input-0-2 p) allowed = tt
complement-back (O.input-0-3 p) allowed = tt
complement-back (O.input-7-0 p) ()
complement-back (O.input-7-1 p) ()
complement-back (O.input-7-2 p) ()
complement-back (O.input-7-3 p) ()
pair-0-1-2 : Policy.Pair.Good tree-0-1-2 → Policy.Pair.Good tree-1-0-3
pair-0-1-2 = PairTransfer.transfer tree-0-1-2 tree-1-0-3 O.move-1-0-3 (λ o → pair-back (O.origin-1-0-3 o))
base-0-1-2 : Policy.Base.Good tree-0-1-2 → Complement.Good tree-1-0-3
base-0-1-2 = BaseTransfer.transfer tree-0-1-2 tree-1-0-3 O.move-1-0-3 (λ o → base-back (O.origin-1-0-3 o))
complement-0-1-2 : Complement.Good tree-0-1-2 → Policy.Base.Good tree-1-0-3
complement-0-1-2 = ComplementTransfer.transfer tree-0-1-2 tree-1-0-3 O.move-1-0-3 (λ o → complement-back (O.origin-1-0-3 o))
transported-good-0-1-2 : Policy.Pair.Good tree-1-0-3
transported-good-0-1-2 = pair-0-1-2 Policy.pair-good-0-1-2
transported-native-0-1-2 : Policy.Pair.R.Resolve (P.T.encode tree-1-0-3)
transported-native-0-1-2 = Policy.Pair.realize tree-1-0-3 transported-good-0-1-2
pair-0-1-3 : Policy.Pair.Good tree-0-1-3 → Policy.Pair.Good tree-1-0-2
pair-0-1-3 = PairTransfer.transfer tree-0-1-3 tree-1-0-2 O.move-1-0-2 (λ o → pair-back (O.origin-1-0-2 o))
base-0-1-3 : Policy.Base.Good tree-0-1-3 → Complement.Good tree-1-0-2
base-0-1-3 = BaseTransfer.transfer tree-0-1-3 tree-1-0-2 O.move-1-0-2 (λ o → base-back (O.origin-1-0-2 o))
complement-0-1-3 : Complement.Good tree-0-1-3 → Policy.Base.Good tree-1-0-2
complement-0-1-3 = ComplementTransfer.transfer tree-0-1-3 tree-1-0-2 O.move-1-0-2 (λ o → complement-back (O.origin-1-0-2 o))
transported-good-0-1-3 : Policy.Pair.Good tree-1-0-2
transported-good-0-1-3 = pair-0-1-3 Policy.pair-good-0-1-3
transported-native-0-1-3 : Policy.Pair.R.Resolve (P.T.encode tree-1-0-2)
transported-native-0-1-3 = Policy.Pair.realize tree-1-0-2 transported-good-0-1-3
pair-0-2-1 : Policy.Pair.Good tree-0-2-1 → Policy.Pair.Good tree-1-3-0
pair-0-2-1 = PairTransfer.transfer tree-0-2-1 tree-1-3-0 O.move-1-3-0 (λ o → pair-back (O.origin-1-3-0 o))
base-0-2-1 : Policy.Base.Good tree-0-2-1 → Complement.Good tree-1-3-0
base-0-2-1 = BaseTransfer.transfer tree-0-2-1 tree-1-3-0 O.move-1-3-0 (λ o → base-back (O.origin-1-3-0 o))
complement-0-2-1 : Complement.Good tree-0-2-1 → Policy.Base.Good tree-1-3-0
complement-0-2-1 = ComplementTransfer.transfer tree-0-2-1 tree-1-3-0 O.move-1-3-0 (λ o → complement-back (O.origin-1-3-0 o))
transported-good-0-2-1 : Policy.Pair.Good tree-1-3-0
transported-good-0-2-1 = pair-0-2-1 Policy.pair-good-0-2-1
transported-native-0-2-1 : Policy.Pair.R.Resolve (P.T.encode tree-1-3-0)
transported-native-0-2-1 = Policy.Pair.realize tree-1-3-0 transported-good-0-2-1
pair-0-2-3 : Policy.Pair.Good tree-0-2-3 → Policy.Pair.Good tree-1-3-2
pair-0-2-3 = PairTransfer.transfer tree-0-2-3 tree-1-3-2 O.move-1-3-2 (λ o → pair-back (O.origin-1-3-2 o))
base-0-2-3 : Policy.Base.Good tree-0-2-3 → Complement.Good tree-1-3-2
base-0-2-3 = BaseTransfer.transfer tree-0-2-3 tree-1-3-2 O.move-1-3-2 (λ o → base-back (O.origin-1-3-2 o))
complement-0-2-3 : Complement.Good tree-0-2-3 → Policy.Base.Good tree-1-3-2
complement-0-2-3 = ComplementTransfer.transfer tree-0-2-3 tree-1-3-2 O.move-1-3-2 (λ o → complement-back (O.origin-1-3-2 o))
transported-good-0-2-3 : Policy.Pair.Good tree-1-3-2
transported-good-0-2-3 = pair-0-2-3 Policy.pair-good-0-2-3
transported-native-0-2-3 : Policy.Pair.R.Resolve (P.T.encode tree-1-3-2)
transported-native-0-2-3 = Policy.Pair.realize tree-1-3-2 transported-good-0-2-3
pair-0-3-1 : Policy.Pair.Good tree-0-3-1 → Policy.Pair.Good tree-1-2-0
pair-0-3-1 = PairTransfer.transfer tree-0-3-1 tree-1-2-0 O.move-1-2-0 (λ o → pair-back (O.origin-1-2-0 o))
base-0-3-1 : Policy.Base.Good tree-0-3-1 → Complement.Good tree-1-2-0
base-0-3-1 = BaseTransfer.transfer tree-0-3-1 tree-1-2-0 O.move-1-2-0 (λ o → base-back (O.origin-1-2-0 o))
complement-0-3-1 : Complement.Good tree-0-3-1 → Policy.Base.Good tree-1-2-0
complement-0-3-1 = ComplementTransfer.transfer tree-0-3-1 tree-1-2-0 O.move-1-2-0 (λ o → complement-back (O.origin-1-2-0 o))
transported-good-0-3-1 : Policy.Pair.Good tree-1-2-0
transported-good-0-3-1 = pair-0-3-1 Policy.pair-good-0-3-1
transported-native-0-3-1 : Policy.Pair.R.Resolve (P.T.encode tree-1-2-0)
transported-native-0-3-1 = Policy.Pair.realize tree-1-2-0 transported-good-0-3-1
pair-0-3-2 : Policy.Pair.Good tree-0-3-2 → Policy.Pair.Good tree-1-2-3
pair-0-3-2 = PairTransfer.transfer tree-0-3-2 tree-1-2-3 O.move-1-2-3 (λ o → pair-back (O.origin-1-2-3 o))
base-0-3-2 : Policy.Base.Good tree-0-3-2 → Complement.Good tree-1-2-3
base-0-3-2 = BaseTransfer.transfer tree-0-3-2 tree-1-2-3 O.move-1-2-3 (λ o → base-back (O.origin-1-2-3 o))
complement-0-3-2 : Complement.Good tree-0-3-2 → Policy.Base.Good tree-1-2-3
complement-0-3-2 = ComplementTransfer.transfer tree-0-3-2 tree-1-2-3 O.move-1-2-3 (λ o → complement-back (O.origin-1-2-3 o))
transported-good-0-3-2 : Policy.Pair.Good tree-1-2-3
transported-good-0-3-2 = pair-0-3-2 Policy.pair-good-0-3-2
transported-native-0-3-2 : Policy.Pair.R.Resolve (P.T.encode tree-1-2-3)
transported-native-0-3-2 = Policy.Pair.realize tree-1-2-3 transported-good-0-3-2
pair-1-0-2 : Policy.Pair.Good tree-1-0-2 → Policy.Pair.Good tree-0-1-3
pair-1-0-2 = PairTransfer.transfer tree-1-0-2 tree-0-1-3 O.move-0-1-3 (λ o → pair-back (O.origin-0-1-3 o))
base-1-0-2 : Policy.Base.Good tree-1-0-2 → Complement.Good tree-0-1-3
base-1-0-2 = BaseTransfer.transfer tree-1-0-2 tree-0-1-3 O.move-0-1-3 (λ o → base-back (O.origin-0-1-3 o))
complement-1-0-2 : Complement.Good tree-1-0-2 → Policy.Base.Good tree-0-1-3
complement-1-0-2 = ComplementTransfer.transfer tree-1-0-2 tree-0-1-3 O.move-0-1-3 (λ o → complement-back (O.origin-0-1-3 o))
transported-good-1-0-2 : Policy.Pair.Good tree-0-1-3
transported-good-1-0-2 = pair-1-0-2 Policy.pair-good-1-0-2
transported-native-1-0-2 : Policy.Pair.R.Resolve (P.T.encode tree-0-1-3)
transported-native-1-0-2 = Policy.Pair.realize tree-0-1-3 transported-good-1-0-2
pair-1-0-3 : Policy.Pair.Good tree-1-0-3 → Policy.Pair.Good tree-0-1-2
pair-1-0-3 = PairTransfer.transfer tree-1-0-3 tree-0-1-2 O.move-0-1-2 (λ o → pair-back (O.origin-0-1-2 o))
base-1-0-3 : Policy.Base.Good tree-1-0-3 → Complement.Good tree-0-1-2
base-1-0-3 = BaseTransfer.transfer tree-1-0-3 tree-0-1-2 O.move-0-1-2 (λ o → base-back (O.origin-0-1-2 o))
complement-1-0-3 : Complement.Good tree-1-0-3 → Policy.Base.Good tree-0-1-2
complement-1-0-3 = ComplementTransfer.transfer tree-1-0-3 tree-0-1-2 O.move-0-1-2 (λ o → complement-back (O.origin-0-1-2 o))
transported-good-1-0-3 : Policy.Pair.Good tree-0-1-2
transported-good-1-0-3 = pair-1-0-3 Policy.pair-good-1-0-3
transported-native-1-0-3 : Policy.Pair.R.Resolve (P.T.encode tree-0-1-2)
transported-native-1-0-3 = Policy.Pair.realize tree-0-1-2 transported-good-1-0-3
pair-1-2-0 : Policy.Pair.Good tree-1-2-0 → Policy.Pair.Good tree-0-3-1
pair-1-2-0 = PairTransfer.transfer tree-1-2-0 tree-0-3-1 O.move-0-3-1 (λ o → pair-back (O.origin-0-3-1 o))
base-1-2-0 : Policy.Base.Good tree-1-2-0 → Complement.Good tree-0-3-1
base-1-2-0 = BaseTransfer.transfer tree-1-2-0 tree-0-3-1 O.move-0-3-1 (λ o → base-back (O.origin-0-3-1 o))
complement-1-2-0 : Complement.Good tree-1-2-0 → Policy.Base.Good tree-0-3-1
complement-1-2-0 = ComplementTransfer.transfer tree-1-2-0 tree-0-3-1 O.move-0-3-1 (λ o → complement-back (O.origin-0-3-1 o))
transported-good-1-2-0 : Policy.Pair.Good tree-0-3-1
transported-good-1-2-0 = pair-1-2-0 Policy.pair-good-1-2-0
transported-native-1-2-0 : Policy.Pair.R.Resolve (P.T.encode tree-0-3-1)
transported-native-1-2-0 = Policy.Pair.realize tree-0-3-1 transported-good-1-2-0
pair-1-2-3 : Policy.Pair.Good tree-1-2-3 → Policy.Pair.Good tree-0-3-2
pair-1-2-3 = PairTransfer.transfer tree-1-2-3 tree-0-3-2 O.move-0-3-2 (λ o → pair-back (O.origin-0-3-2 o))
base-1-2-3 : Policy.Base.Good tree-1-2-3 → Complement.Good tree-0-3-2
base-1-2-3 = BaseTransfer.transfer tree-1-2-3 tree-0-3-2 O.move-0-3-2 (λ o → base-back (O.origin-0-3-2 o))
complement-1-2-3 : Complement.Good tree-1-2-3 → Policy.Base.Good tree-0-3-2
complement-1-2-3 = ComplementTransfer.transfer tree-1-2-3 tree-0-3-2 O.move-0-3-2 (λ o → complement-back (O.origin-0-3-2 o))
transported-good-1-2-3 : Policy.Pair.Good tree-0-3-2
transported-good-1-2-3 = pair-1-2-3 Policy.pair-good-1-2-3
transported-native-1-2-3 : Policy.Pair.R.Resolve (P.T.encode tree-0-3-2)
transported-native-1-2-3 = Policy.Pair.realize tree-0-3-2 transported-good-1-2-3
pair-1-3-0 : Policy.Pair.Good tree-1-3-0 → Policy.Pair.Good tree-0-2-1
pair-1-3-0 = PairTransfer.transfer tree-1-3-0 tree-0-2-1 O.move-0-2-1 (λ o → pair-back (O.origin-0-2-1 o))
base-1-3-0 : Policy.Base.Good tree-1-3-0 → Complement.Good tree-0-2-1
base-1-3-0 = BaseTransfer.transfer tree-1-3-0 tree-0-2-1 O.move-0-2-1 (λ o → base-back (O.origin-0-2-1 o))
complement-1-3-0 : Complement.Good tree-1-3-0 → Policy.Base.Good tree-0-2-1
complement-1-3-0 = ComplementTransfer.transfer tree-1-3-0 tree-0-2-1 O.move-0-2-1 (λ o → complement-back (O.origin-0-2-1 o))
transported-good-1-3-0 : Policy.Pair.Good tree-0-2-1
transported-good-1-3-0 = pair-1-3-0 Policy.pair-good-1-3-0
transported-native-1-3-0 : Policy.Pair.R.Resolve (P.T.encode tree-0-2-1)
transported-native-1-3-0 = Policy.Pair.realize tree-0-2-1 transported-good-1-3-0
pair-1-3-2 : Policy.Pair.Good tree-1-3-2 → Policy.Pair.Good tree-0-2-3
pair-1-3-2 = PairTransfer.transfer tree-1-3-2 tree-0-2-3 O.move-0-2-3 (λ o → pair-back (O.origin-0-2-3 o))
base-1-3-2 : Policy.Base.Good tree-1-3-2 → Complement.Good tree-0-2-3
base-1-3-2 = BaseTransfer.transfer tree-1-3-2 tree-0-2-3 O.move-0-2-3 (λ o → base-back (O.origin-0-2-3 o))
complement-1-3-2 : Complement.Good tree-1-3-2 → Policy.Base.Good tree-0-2-3
complement-1-3-2 = ComplementTransfer.transfer tree-1-3-2 tree-0-2-3 O.move-0-2-3 (λ o → complement-back (O.origin-0-2-3 o))
transported-good-1-3-2 : Policy.Pair.Good tree-0-2-3
transported-good-1-3-2 = pair-1-3-2 Policy.pair-good-1-3-2
transported-native-1-3-2 : Policy.Pair.R.Resolve (P.T.encode tree-0-2-3)
transported-native-1-3-2 = Policy.Pair.realize tree-0-2-3 transported-good-1-3-2
pair-2-0-1 : Policy.Pair.Good tree-2-0-1 → Policy.Pair.Good tree-3-1-0
pair-2-0-1 = PairTransfer.transfer tree-2-0-1 tree-3-1-0 O.move-3-1-0 (λ o → pair-back (O.origin-3-1-0 o))
base-2-0-1 : Policy.Base.Good tree-2-0-1 → Complement.Good tree-3-1-0
base-2-0-1 = BaseTransfer.transfer tree-2-0-1 tree-3-1-0 O.move-3-1-0 (λ o → base-back (O.origin-3-1-0 o))
complement-2-0-1 : Complement.Good tree-2-0-1 → Policy.Base.Good tree-3-1-0
complement-2-0-1 = ComplementTransfer.transfer tree-2-0-1 tree-3-1-0 O.move-3-1-0 (λ o → complement-back (O.origin-3-1-0 o))
transported-good-2-0-1 : Policy.Pair.Good tree-3-1-0
transported-good-2-0-1 = pair-2-0-1 Policy.pair-good-2-0-1
transported-native-2-0-1 : Policy.Pair.R.Resolve (P.T.encode tree-3-1-0)
transported-native-2-0-1 = Policy.Pair.realize tree-3-1-0 transported-good-2-0-1
pair-2-0-3 : Policy.Pair.Good tree-2-0-3 → Policy.Pair.Good tree-3-1-2
pair-2-0-3 = PairTransfer.transfer tree-2-0-3 tree-3-1-2 O.move-3-1-2 (λ o → pair-back (O.origin-3-1-2 o))
base-2-0-3 : Policy.Base.Good tree-2-0-3 → Complement.Good tree-3-1-2
base-2-0-3 = BaseTransfer.transfer tree-2-0-3 tree-3-1-2 O.move-3-1-2 (λ o → base-back (O.origin-3-1-2 o))
complement-2-0-3 : Complement.Good tree-2-0-3 → Policy.Base.Good tree-3-1-2
complement-2-0-3 = ComplementTransfer.transfer tree-2-0-3 tree-3-1-2 O.move-3-1-2 (λ o → complement-back (O.origin-3-1-2 o))
transported-good-2-0-3 : Policy.Pair.Good tree-3-1-2
transported-good-2-0-3 = pair-2-0-3 Policy.pair-good-2-0-3
transported-native-2-0-3 : Policy.Pair.R.Resolve (P.T.encode tree-3-1-2)
transported-native-2-0-3 = Policy.Pair.realize tree-3-1-2 transported-good-2-0-3
pair-2-1-0 : Policy.Pair.Good tree-2-1-0 → Policy.Pair.Good tree-3-0-1
pair-2-1-0 = PairTransfer.transfer tree-2-1-0 tree-3-0-1 O.move-3-0-1 (λ o → pair-back (O.origin-3-0-1 o))
base-2-1-0 : Policy.Base.Good tree-2-1-0 → Complement.Good tree-3-0-1
base-2-1-0 = BaseTransfer.transfer tree-2-1-0 tree-3-0-1 O.move-3-0-1 (λ o → base-back (O.origin-3-0-1 o))
complement-2-1-0 : Complement.Good tree-2-1-0 → Policy.Base.Good tree-3-0-1
complement-2-1-0 = ComplementTransfer.transfer tree-2-1-0 tree-3-0-1 O.move-3-0-1 (λ o → complement-back (O.origin-3-0-1 o))
transported-good-2-1-0 : Policy.Pair.Good tree-3-0-1
transported-good-2-1-0 = pair-2-1-0 Policy.pair-good-2-1-0
transported-native-2-1-0 : Policy.Pair.R.Resolve (P.T.encode tree-3-0-1)
transported-native-2-1-0 = Policy.Pair.realize tree-3-0-1 transported-good-2-1-0
pair-2-1-3 : Policy.Pair.Good tree-2-1-3 → Policy.Pair.Good tree-3-0-2
pair-2-1-3 = PairTransfer.transfer tree-2-1-3 tree-3-0-2 O.move-3-0-2 (λ o → pair-back (O.origin-3-0-2 o))
base-2-1-3 : Policy.Base.Good tree-2-1-3 → Complement.Good tree-3-0-2
base-2-1-3 = BaseTransfer.transfer tree-2-1-3 tree-3-0-2 O.move-3-0-2 (λ o → base-back (O.origin-3-0-2 o))
complement-2-1-3 : Complement.Good tree-2-1-3 → Policy.Base.Good tree-3-0-2
complement-2-1-3 = ComplementTransfer.transfer tree-2-1-3 tree-3-0-2 O.move-3-0-2 (λ o → complement-back (O.origin-3-0-2 o))
transported-good-2-1-3 : Policy.Pair.Good tree-3-0-2
transported-good-2-1-3 = pair-2-1-3 Policy.pair-good-2-1-3
transported-native-2-1-3 : Policy.Pair.R.Resolve (P.T.encode tree-3-0-2)
transported-native-2-1-3 = Policy.Pair.realize tree-3-0-2 transported-good-2-1-3
pair-2-3-0 : Policy.Pair.Good tree-2-3-0 → Policy.Pair.Good tree-3-2-1
pair-2-3-0 = PairTransfer.transfer tree-2-3-0 tree-3-2-1 O.move-3-2-1 (λ o → pair-back (O.origin-3-2-1 o))
base-2-3-0 : Policy.Base.Good tree-2-3-0 → Complement.Good tree-3-2-1
base-2-3-0 = BaseTransfer.transfer tree-2-3-0 tree-3-2-1 O.move-3-2-1 (λ o → base-back (O.origin-3-2-1 o))
complement-2-3-0 : Complement.Good tree-2-3-0 → Policy.Base.Good tree-3-2-1
complement-2-3-0 = ComplementTransfer.transfer tree-2-3-0 tree-3-2-1 O.move-3-2-1 (λ o → complement-back (O.origin-3-2-1 o))
transported-good-2-3-0 : Policy.Pair.Good tree-3-2-1
transported-good-2-3-0 = pair-2-3-0 Policy.pair-good-2-3-0
transported-native-2-3-0 : Policy.Pair.R.Resolve (P.T.encode tree-3-2-1)
transported-native-2-3-0 = Policy.Pair.realize tree-3-2-1 transported-good-2-3-0
pair-2-3-1 : Policy.Pair.Good tree-2-3-1 → Policy.Pair.Good tree-3-2-0
pair-2-3-1 = PairTransfer.transfer tree-2-3-1 tree-3-2-0 O.move-3-2-0 (λ o → pair-back (O.origin-3-2-0 o))
base-2-3-1 : Policy.Base.Good tree-2-3-1 → Complement.Good tree-3-2-0
base-2-3-1 = BaseTransfer.transfer tree-2-3-1 tree-3-2-0 O.move-3-2-0 (λ o → base-back (O.origin-3-2-0 o))
complement-2-3-1 : Complement.Good tree-2-3-1 → Policy.Base.Good tree-3-2-0
complement-2-3-1 = ComplementTransfer.transfer tree-2-3-1 tree-3-2-0 O.move-3-2-0 (λ o → complement-back (O.origin-3-2-0 o))
transported-good-2-3-1 : Policy.Pair.Good tree-3-2-0
transported-good-2-3-1 = pair-2-3-1 Policy.pair-good-2-3-1
transported-native-2-3-1 : Policy.Pair.R.Resolve (P.T.encode tree-3-2-0)
transported-native-2-3-1 = Policy.Pair.realize tree-3-2-0 transported-good-2-3-1
pair-3-0-1 : Policy.Pair.Good tree-3-0-1 → Policy.Pair.Good tree-2-1-0
pair-3-0-1 = PairTransfer.transfer tree-3-0-1 tree-2-1-0 O.move-2-1-0 (λ o → pair-back (O.origin-2-1-0 o))
base-3-0-1 : Policy.Base.Good tree-3-0-1 → Complement.Good tree-2-1-0
base-3-0-1 = BaseTransfer.transfer tree-3-0-1 tree-2-1-0 O.move-2-1-0 (λ o → base-back (O.origin-2-1-0 o))
complement-3-0-1 : Complement.Good tree-3-0-1 → Policy.Base.Good tree-2-1-0
complement-3-0-1 = ComplementTransfer.transfer tree-3-0-1 tree-2-1-0 O.move-2-1-0 (λ o → complement-back (O.origin-2-1-0 o))
transported-good-3-0-1 : Policy.Pair.Good tree-2-1-0
transported-good-3-0-1 = pair-3-0-1 Policy.pair-good-3-0-1
transported-native-3-0-1 : Policy.Pair.R.Resolve (P.T.encode tree-2-1-0)
transported-native-3-0-1 = Policy.Pair.realize tree-2-1-0 transported-good-3-0-1
pair-3-0-2 : Policy.Pair.Good tree-3-0-2 → Policy.Pair.Good tree-2-1-3
pair-3-0-2 = PairTransfer.transfer tree-3-0-2 tree-2-1-3 O.move-2-1-3 (λ o → pair-back (O.origin-2-1-3 o))
base-3-0-2 : Policy.Base.Good tree-3-0-2 → Complement.Good tree-2-1-3
base-3-0-2 = BaseTransfer.transfer tree-3-0-2 tree-2-1-3 O.move-2-1-3 (λ o → base-back (O.origin-2-1-3 o))
complement-3-0-2 : Complement.Good tree-3-0-2 → Policy.Base.Good tree-2-1-3
complement-3-0-2 = ComplementTransfer.transfer tree-3-0-2 tree-2-1-3 O.move-2-1-3 (λ o → complement-back (O.origin-2-1-3 o))
transported-good-3-0-2 : Policy.Pair.Good tree-2-1-3
transported-good-3-0-2 = pair-3-0-2 Policy.pair-good-3-0-2
transported-native-3-0-2 : Policy.Pair.R.Resolve (P.T.encode tree-2-1-3)
transported-native-3-0-2 = Policy.Pair.realize tree-2-1-3 transported-good-3-0-2
pair-3-1-0 : Policy.Pair.Good tree-3-1-0 → Policy.Pair.Good tree-2-0-1
pair-3-1-0 = PairTransfer.transfer tree-3-1-0 tree-2-0-1 O.move-2-0-1 (λ o → pair-back (O.origin-2-0-1 o))
base-3-1-0 : Policy.Base.Good tree-3-1-0 → Complement.Good tree-2-0-1
base-3-1-0 = BaseTransfer.transfer tree-3-1-0 tree-2-0-1 O.move-2-0-1 (λ o → base-back (O.origin-2-0-1 o))
complement-3-1-0 : Complement.Good tree-3-1-0 → Policy.Base.Good tree-2-0-1
complement-3-1-0 = ComplementTransfer.transfer tree-3-1-0 tree-2-0-1 O.move-2-0-1 (λ o → complement-back (O.origin-2-0-1 o))
transported-good-3-1-0 : Policy.Pair.Good tree-2-0-1
transported-good-3-1-0 = pair-3-1-0 Policy.pair-good-3-1-0
transported-native-3-1-0 : Policy.Pair.R.Resolve (P.T.encode tree-2-0-1)
transported-native-3-1-0 = Policy.Pair.realize tree-2-0-1 transported-good-3-1-0
pair-3-1-2 : Policy.Pair.Good tree-3-1-2 → Policy.Pair.Good tree-2-0-3
pair-3-1-2 = PairTransfer.transfer tree-3-1-2 tree-2-0-3 O.move-2-0-3 (λ o → pair-back (O.origin-2-0-3 o))
base-3-1-2 : Policy.Base.Good tree-3-1-2 → Complement.Good tree-2-0-3
base-3-1-2 = BaseTransfer.transfer tree-3-1-2 tree-2-0-3 O.move-2-0-3 (λ o → base-back (O.origin-2-0-3 o))
complement-3-1-2 : Complement.Good tree-3-1-2 → Policy.Base.Good tree-2-0-3
complement-3-1-2 = ComplementTransfer.transfer tree-3-1-2 tree-2-0-3 O.move-2-0-3 (λ o → complement-back (O.origin-2-0-3 o))
transported-good-3-1-2 : Policy.Pair.Good tree-2-0-3
transported-good-3-1-2 = pair-3-1-2 Policy.pair-good-3-1-2
transported-native-3-1-2 : Policy.Pair.R.Resolve (P.T.encode tree-2-0-3)
transported-native-3-1-2 = Policy.Pair.realize tree-2-0-3 transported-good-3-1-2
pair-3-2-0 : Policy.Pair.Good tree-3-2-0 → Policy.Pair.Good tree-2-3-1
pair-3-2-0 = PairTransfer.transfer tree-3-2-0 tree-2-3-1 O.move-2-3-1 (λ o → pair-back (O.origin-2-3-1 o))
base-3-2-0 : Policy.Base.Good tree-3-2-0 → Complement.Good tree-2-3-1
base-3-2-0 = BaseTransfer.transfer tree-3-2-0 tree-2-3-1 O.move-2-3-1 (λ o → base-back (O.origin-2-3-1 o))
complement-3-2-0 : Complement.Good tree-3-2-0 → Policy.Base.Good tree-2-3-1
complement-3-2-0 = ComplementTransfer.transfer tree-3-2-0 tree-2-3-1 O.move-2-3-1 (λ o → complement-back (O.origin-2-3-1 o))
transported-good-3-2-0 : Policy.Pair.Good tree-2-3-1
transported-good-3-2-0 = pair-3-2-0 Policy.pair-good-3-2-0
transported-native-3-2-0 : Policy.Pair.R.Resolve (P.T.encode tree-2-3-1)
transported-native-3-2-0 = Policy.Pair.realize tree-2-3-1 transported-good-3-2-0
pair-3-2-1 : Policy.Pair.Good tree-3-2-1 → Policy.Pair.Good tree-2-3-0
pair-3-2-1 = PairTransfer.transfer tree-3-2-1 tree-2-3-0 O.move-2-3-0 (λ o → pair-back (O.origin-2-3-0 o))
base-3-2-1 : Policy.Base.Good tree-3-2-1 → Complement.Good tree-2-3-0
base-3-2-1 = BaseTransfer.transfer tree-3-2-1 tree-2-3-0 O.move-2-3-0 (λ o → base-back (O.origin-2-3-0 o))
complement-3-2-1 : Complement.Good tree-3-2-1 → Policy.Base.Good tree-2-3-0
complement-3-2-1 = ComplementTransfer.transfer tree-3-2-1 tree-2-3-0 O.move-2-3-0 (λ o → complement-back (O.origin-2-3-0 o))
transported-good-3-2-1 : Policy.Pair.Good tree-2-3-0
transported-good-3-2-1 = pair-3-2-1 Policy.pair-good-3-2-1
transported-native-3-2-1 : Policy.Pair.R.Resolve (P.T.encode tree-2-3-0)
transported-native-3-2-1 = Policy.Pair.realize tree-2-3-0 transported-good-3-2-1
source-leaf : P.T.Tree
source-leaf = P.port C.q0 m0 F.vp-0-1
target-leaf : P.T.Tree
target-leaf = P.port C.q7 c0 F.vp-1-0
source-leaf-good : Policy.Base.Good source-leaf
source-leaf-good = tt
target-leaf-good : Complement.Good target-leaf
target-leaf-good = BaseTransfer.transfer source-leaf target-leaf (λ _ → tt) (λ _ → base-back (O.input-7-0 F.vp-1-0)) source-leaf-good
not-base-target : Policy.Base.Good target-leaf → ⊥
not-base-target allowed = allowed
